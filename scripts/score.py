"""
Score Stage-1 / Stage-2 model outputs against BRAT gold.

Alignment: predicted span aligns to a gold span if
    |pred_tokens ∩ gold_tokens| / max(|pred|, |gold|) >= 0.5
(symmetric token-overlap; one-to-one, greedy by overlap).

Metrics per essay + per model:
  - Component precision/recall/F1  micro (all 3 labels pooled)
  - Component F1 macro (mean over MajorClaim / Claim / Premise)
  - Stance accuracy (over aligned Claim pairs)
  - Relation F1: a predicted (src, tgt, type) is TP iff both src and tgt
                 are aligned to gold components and the directed pair with
                 matching type exists in gold.

Usage:
    python scripts/score.py stage1
"""

from __future__ import annotations
import argparse, csv, json, re, sys
from pathlib import Path
from collections import defaultdict

ROOT = Path(__file__).resolve().parent.parent
GOLD_DIR = ROOT / "data" / "eval" / "gold"
ESSAYS = ["essay004", "essay005", "essay006"]
MODELS = ["opus", "gemini"]
LABELS = ["MajorClaim", "Claim", "Premise"]
OVERLAP_THR = 0.5

TOKEN_RE = re.compile(r"[A-Za-z0-9]+")
def toks(s: str) -> set[str]:
    return {t.lower() for t in TOKEN_RE.findall(s)}

def overlap(a: set[str], b: set[str]) -> float:
    if not a or not b: return 0.0
    return len(a & b) / max(len(a), len(b))


def parse_ann(path: Path) -> dict:
    """Parse BRAT .ann -> {components: [...], relations: [...]}"""
    comps = {}        # tid -> {id, type, text, tokens, stance?}
    stances = {}      # tid -> 'For' / 'Against'
    rels = []         # list[(src, tgt, type)]
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip(): continue
        parts = line.split("\t")
        tag = parts[0]
        if tag.startswith("T"):
            # e.g. T1  MajorClaim 262 376\tthe text
            meta, text = parts[1], parts[2]
            typ = meta.split(" ", 1)[0]
            comps[tag] = {"id": tag, "type": typ, "text": text, "tokens": toks(text)}
        elif tag.startswith("A"):
            # A1  Stance T3 Against
            m = parts[1].split()
            if len(m) >= 3 and m[0] == "Stance":
                stances[m[1]] = m[2]
        elif tag.startswith("R"):
            # R1  supports Arg1:T8 Arg2:T4
            m = parts[1].split()
            rtype = "Support" if m[0] == "supports" else "Attack"
            src = m[1].split(":")[1]
            tgt = m[2].split(":")[1]
            rels.append({"src": src, "tgt": tgt, "type": rtype})
    for tid, s in stances.items():
        if tid in comps: comps[tid]["stance"] = s
    return {"components": list(comps.values()), "relations": rels}


def parse_pred(path: Path) -> dict:
    data = json.loads(path.read_text(encoding="utf-8"))
    for c in data.get("components", []):
        c["tokens"] = toks(c.get("text", ""))
    return data


def align(pred_comps: list[dict], gold_comps: list[dict]) -> dict:
    """Greedy one-to-one alignment by best overlap (>= OVERLAP_THR)."""
    pairs = []
    for p in pred_comps:
        for g in gold_comps:
            o = overlap(p["tokens"], g["tokens"])
            if o >= OVERLAP_THR:
                pairs.append((o, p["id"], g["id"]))
    pairs.sort(reverse=True)
    used_p, used_g, mapping = set(), set(), {}
    for o, pid, gid in pairs:
        if pid in used_p or gid in used_g: continue
        used_p.add(pid); used_g.add(gid); mapping[pid] = gid
    return mapping


def prf(tp: int, fp: int, fn: int) -> tuple[float, float, float]:
    p = tp / (tp + fp) if tp + fp else 0.0
    r = tp / (tp + fn) if tp + fn else 0.0
    f = 2 * p * r / (p + r) if p + r else 0.0
    return p, r, f


def score_essay(pred: dict, gold: dict) -> dict:
    pred_comps = pred["components"]
    gold_comps = gold["components"]
    g_by_id = {g["id"]: g for g in gold_comps}

    mapping = align(pred_comps, gold_comps)  # pred_id -> gold_id

    # --- component scoring: a pred TP iff aligned AND type matches gold ---
    per_label = {L: {"tp": 0, "fp": 0, "fn": 0} for L in LABELS}
    tp_mic = fp_mic = fn_mic = 0
    for p in pred_comps:
        typ = p["type"]
        if typ not in per_label:  # unknown label -> count as fp under all labels? just mark mic
            fp_mic += 1
            continue
        gid = mapping.get(p["id"])
        if gid and g_by_id[gid]["type"] == typ:
            per_label[typ]["tp"] += 1; tp_mic += 1
        else:
            per_label[typ]["fp"] += 1; fp_mic += 1
    matched_gold = {mapping[pid] for pid in mapping}
    for g in gold_comps:
        if g["id"] in matched_gold:
            # if the predicted type at that slot did not match, it's an fn for gold's type
            # find which pred mapped to this gold
            pid = next(pid for pid, gid in mapping.items() if gid == g["id"])
            ppred = next(p for p in pred_comps if p["id"] == pid)
            if ppred["type"] != g["type"]:
                per_label[g["type"]]["fn"] += 1; fn_mic += 1
        else:
            per_label[g["type"]]["fn"] += 1; fn_mic += 1

    comp_p, comp_r, comp_f = prf(tp_mic, fp_mic, fn_mic)
    macro_fs = []
    for L in LABELS:
        _, _, f = prf(per_label[L]["tp"], per_label[L]["fp"], per_label[L]["fn"])
        macro_fs.append(f)
    comp_macro_f = sum(macro_fs) / len(macro_fs)

    # --- stance accuracy: Claim aligned to Claim, compare stance ---
    stance_correct = stance_total = 0
    for p in pred_comps:
        if p["type"] != "Claim": continue
        gid = mapping.get(p["id"])
        if not gid: continue
        g = g_by_id[gid]
        if g["type"] != "Claim": continue
        stance_total += 1
        if p.get("stance") == g.get("stance"):
            stance_correct += 1
    stance_acc = stance_correct / stance_total if stance_total else None

    # --- relation F1: endpoint-restricted ---
    # build gold set of (gold_src, gold_tgt, type)
    gold_rel_set = {(r["src"], r["tgt"], r["type"]) for r in gold["relations"]}
    rel_tp = rel_fp = 0
    mapped_pred_rels = []
    for r in pred["relations"]:
        gs = mapping.get(r["src"]); gt = mapping.get(r["tgt"])
        if gs is None or gt is None:
            rel_fp += 1
            mapped_pred_rels.append(None)
            continue
        key = (gs, gt, r["type"])
        mapped_pred_rels.append(key)
        if key in gold_rel_set:
            rel_tp += 1
        else:
            rel_fp += 1
    matched_pred = {k for k in mapped_pred_rels if k is not None and k in gold_rel_set}
    rel_fn = len(gold_rel_set) - len(matched_pred)
    rel_p, rel_r, rel_f = prf(rel_tp, rel_fp, rel_fn)

    return {
        "n_pred_comp": len(pred_comps),
        "n_gold_comp": len(gold_comps),
        "n_pred_rel": len(pred["relations"]),
        "n_gold_rel": len(gold["relations"]),
        "comp_p_micro": round(comp_p, 4),
        "comp_r_micro": round(comp_r, 4),
        "comp_f1_micro": round(comp_f, 4),
        "comp_f1_macro": round(comp_macro_f, 4),
        "stance_acc": round(stance_acc, 4) if stance_acc is not None else "",
        "stance_n": stance_total,
        "rel_p": round(rel_p, 4),
        "rel_r": round(rel_r, 4),
        "rel_f1": round(rel_f, 4),
        "mapping": mapping,
        "per_label": per_label,
    }


def main(stage: str):
    run_dir = ROOT / "runs" / stage
    rows = []
    details = {}
    for model in MODELS:
        for essay in ESSAYS:
            pred_path = run_dir / model / f"{essay}.json"
            gold_path = GOLD_DIR / f"{essay}.ann"
            if not pred_path.exists():
                print(f"missing: {pred_path}", file=sys.stderr); continue
            pred = parse_pred(pred_path)
            gold = parse_ann(gold_path)
            s = score_essay(pred, gold)
            row = {
                "stage": stage, "model": model, "essay": essay,
                **{k: v for k, v in s.items() if k not in ("mapping", "per_label")},
            }
            rows.append(row)
            details[(model, essay)] = s
            print(f"{model:6s} {essay}  "
                  f"comp_F1_micro={s['comp_f1_micro']:.3f} "
                  f"macro={s['comp_f1_macro']:.3f}  "
                  f"stance={s['stance_acc']}  "
                  f"rel_F1={s['rel_f1']:.3f}")

    # write scores.csv
    out = run_dir / "scores.csv"
    fields = ["stage","model","essay","n_pred_comp","n_gold_comp","n_pred_rel","n_gold_rel",
              "comp_p_micro","comp_r_micro","comp_f1_micro","comp_f1_macro",
              "stance_acc","stance_n","rel_p","rel_r","rel_f1"]
    with out.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader(); w.writerows(rows)
    print(f"\nwrote {out}")
    return rows, details


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("stage", choices=["stage1", "stage2"])
    args = ap.parse_args()
    main(args.stage)
