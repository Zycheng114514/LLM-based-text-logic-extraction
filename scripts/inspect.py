"""Dump per-label counts, alignment map, and relation-by-relation verdict."""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).parent))
from score import parse_ann, parse_pred, score_essay, ROOT, MODELS, ESSAYS, GOLD_DIR

STAGE = sys.argv[1] if len(sys.argv) > 1 else "stage1"
for essay in ESSAYS:
    gold = parse_ann(GOLD_DIR / f"{essay}.ann")
    g_by_id = {g["id"]: g for g in gold["components"]}
    gold_rel_set = {(r["src"], r["tgt"], r["type"]) for r in gold["relations"]}
    for model in MODELS:
        p = parse_pred(ROOT / f"runs/{STAGE}" / model / f"{essay}.json")
        s = score_essay(p, gold)
        mapping = s["mapping"]
        p_by_id = {c["id"]: c for c in p["components"]}
        print(f"\n=== {model} {essay} ===")
        print("per-label:", s["per_label"])
        print("alignment (pred_id -> gold_id  [pred_type -> gold_type]  'pred text'[:40]):")
        for pid, c in p_by_id.items():
            gid = mapping.get(pid)
            if gid:
                gt = g_by_id[gid]["type"]
                tag = "OK" if gt == c["type"] else "TYPE_MISMATCH"
                print(f"  {pid:4s}->{gid:4s}  [{c['type']:10s}->{gt:10s}] {tag}  {c['text'][:60]!r}")
            else:
                print(f"  {pid:4s}->----  [{c['type']:10s}]             UNALIGNED  {c['text'][:60]!r}")
        print("unaligned gold:")
        matched_gold = set(mapping.values())
        for g in gold["components"]:
            if g["id"] not in matched_gold:
                print(f"  {g['id']:4s}  [{g['type']:10s}]  {g['text'][:60]!r}")
        print("relations (pred → mapped gold pair, verdict):")
        for r in p["relations"]:
            gs = mapping.get(r["src"]); gt = mapping.get(r["tgt"])
            key = (gs, gt, r["type"]) if gs and gt else None
            verdict = "TP" if key in gold_rel_set else ("FP(unaligned)" if not gs or not gt else "FP")
            print(f"  {r['src']}->{r['tgt']} {r['type']:7s}  =>  "
                  f"{gs}->{gt}  {verdict}")
        print("missed gold relations:")
        pred_keys = {(mapping.get(r['src']), mapping.get(r['tgt']), r['type']) for r in p['relations']}
        for r in gold['relations']:
            k = (r['src'], r['tgt'], r['type'])
            if k not in pred_keys:
                print(f"  MISSED: {r['src']}->{r['tgt']} {r['type']}")
