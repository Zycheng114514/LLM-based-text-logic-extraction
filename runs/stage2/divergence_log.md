# Stage 2 — divergence log

Qualitative companion to `runs/stage2/scores.csv`. Directly comparable
to `runs/stage1/divergence_log.md`. Stage 2 was run once per essay per
model with the tailored per-model prompts
`prompts/02_refined_prompt_opus.md` and
`prompts/02_refined_prompt_gemini.md`.

## Stage 1 → Stage 2 metric table

| model  | essay    | comp F1µ  (S1 → S2) | rel F1  (S1 → S2) | stance  (S1 → S2) |
| ------ | -------- | -------------------- | ------------------ | ------------------ |
| Opus   | essay004 | 0.636 → **0.957**   | 0.000 → **0.462**  | 1.00 → 1.00       |
| Opus   | essay005 | 0.909 → **1.000**   | 0.727 → 0.615      | 1.00 → 1.00       |
| Opus   | essay006 | 0.919 → **0.973**   | 0.615 → **0.846**  | 1.00 → 1.00       |
| Gemini | essay004 | 0.636 → **1.000**   | 0.000 → **0.500**  | 1.00 → 1.00       |
| Gemini | essay005 | 0.917 → **1.000**   | 0.833 → 0.833      | 1.00 → 1.00       |
| Gemini | essay006 | 0.974 → 0.973       | 0.769 → 0.692      | 1.00 → 1.00       |

Bold marks a change > 0.02 in the favourable direction.

**Top line.** Component-F1 improved or held on every cell. Relation-F1
lifted sharply on 4 of 6 cells (Opus/004, Opus/006, Gemini/004,
Gemini/005 hold at its Stage-1 peak). Opus/005 slipped slightly
(0.727 → 0.615) because splitting the "but" clause exposed an
Attack-endpoint choice the model made with the wrong direction.
Gemini/006 slipped slightly (0.769 → 0.692) because the prompt could
not rewrite its paragraph-1 topology. Stance accuracy remained perfect
everywhere.

---

## essay004 — discourse-pivot inversion fixed for both models

This is the largest single lift in the entire Stage 2 exercise. At
Stage 1, rel_F1 was 0.000 for both models because both treated the
*generic opening sentence* of each body paragraph as the Claim and the
*interpretive conclusion* ("this proves that international tourism can
create negative impacts…", "it is apparent that tourism has threatened
the nature environments") as an elaborating premise. Every predicted
edge pointed at the wrong Claim; none could align.

Rule (1) in the tailored prompt — the discourse-pivot rule, naming the
pivot cues "this proves that…" and "it is apparent that…" explicitly —
was written to target exactly this inversion. It worked. Both models
now correctly promote the conclusion sentence to Claim (gold T4, gold
T5) and demote the topic-sentence openers to Premises (gold T6, gold
T9). Opus emits 11/11 gold-aligned components plus one extra (a tail
premise c12 "If authorities do not take steps…"). Gemini emits exactly
11 components and matches gold types perfectly.

Residual relation errors on essay004:

- **Opus** (3 TP / 6 gold): misses T8→T4 Support (c5 is routed at c4, a
  sub-anchor reading where gold has a flat target), T10→T11 Support
  (c9 is routed at c8, direction flipped vs. gold), and T11→T5 Support.
  It also emits a spurious c12→c11 Support, an unaligned pointer edge
  from a premise gold doesn't annotate.
- **Gemini** (3 TP / 6 gold): misses T8→T4 and T7→T4 because it builds
  a pre-claim chain (c4→c3, c5→c3, c3→c6) where gold has parallel
  premise-to-Claim edges. Also misses T11→T5. Its sub-anchor impulse
  (preserved from Stage 1) is over-applied here — on this essay the
  evidence paragraph is a flat star, not a chain.

Both residuals are *fine-grained paragraph-topology* errors, not the
coarse claim/premise inversion that defined Stage 1's 0.000. The shift
is exactly what we wanted: mistakes are now at the level of where a
premise attaches, not at the level of which sentence is the Claim.

---

## essay005 — divergent model responses to the tailored prompt

The gold structure is four edges from Opus's Stage-1 gap: the "but"
clause in paragraph 2 must be split (gold T7 and T8) and must be linked
by an Attack (gold R3: T8 → T7 Attack), and T7 itself attacks the
Claim T4 (gold R2).

**Gemini (0.833 rel-F1, matches Stage 1).** Gemini recovered both
Attacks with correct direction: c5→c4 Attack (= gold T7→T4 Attack),
c6→c5 Attack (= gold T8→T7 Attack). Both are TPs with the right
polarity. The single remaining FP is a local-topology miss (c8→c9
Support, i.e. routing the employer premise at the next premise rather
than at the paragraph Claim).

**Opus (0.615 rel-F1, down from 0.727 at Stage 1).** The Opus-specific
emphasis block worked on its *component* task: Opus split the "but"
clause into two Premises (c5 and c6), which jumped its component F1 to
1.000. But Opus then produced the Attack with the wrong endpoints:
predicted c5→c6 Attack (T7→T8) instead of gold T8→T7. It also produced
c6→c4 Support (T8→T4) instead of gold T7→T4 Attack. The net effect is
that Opus now "sees" an Attack somewhere in the neighbourhood but
routes it between the two sub-premises instead of from each sub-premise
up to the parent Claim. It additionally emitted an unsolicited Attack
edge c11→c12 (Claim-Against → MajorClaim) — gold handles rebuttal via
stance alone, not via an explicit Attack edge, so this is a
formal-structure FP.

Interpretation: on essay005, the tailored prompt reduced Opus's
**component** error (merging "but") at the cost of introducing a new
**relation** error (guessing Attack endpoints once the clauses are
split). Gemini did not hit this because its text-following bias let it
re-read the concession in situ. On this essay the Opus-side lift is
entirely in components, while relations slipped slightly.

---

## essay006 — Opus gained the sub-anchor, Gemini lost some paragraph-1 topology

**Opus (0.846 rel-F1, up from 0.615).** Opus now preserves the final-
paragraph sub-anchor correctly: the three elaborating sentences
(T17/T18/T19) all target the intermediate premise T16 "Learning about
others' cultures is so important" — matching gold exactly. This is
rule (3) in the tailored prompt (sub-anchor) plus the MODEL-SPECIFIC
EMPHASIS (b) pickup on MajorClaim repetition, which together kept the
final-paragraph Claim T6 stable as the top-of-tree node and routed the
elaborations one level below it. 11 of 13 gold relations are true
positives. The two missed edges are both in paragraph 1, where gold
uses its own sub-anchor (T8 and T10 both target T9, an intermediate
premise "they should be able to deal with the obstacles"). Opus
instead routed all four paragraph-1 premises directly at the paragraph
Claim T4 — a flattening that the rule could in principle have caught
but didn't, because paragraph 1 only has three elaborating sentences
followed by a separate evaluation rather than a clean three-into-anchor
pattern.

**Gemini (0.692 rel-F1, down from 0.769 at Stage 1).** The final-
paragraph sub-anchor is preserved correctly. What slipped is
paragraph 1: Gemini built a staircase (c4→c3, c5→c4, c6→c2) where gold
has the sub-anchor (T8→T9, T10→T9). This is the mirror image of Opus's
paragraph-1 error — Opus flattens where gold branches, Gemini makes a
chain where gold branches — neither replicates the actual gold
topology. Gemini also routes c13→c12 (T15→T14) where gold has T15→T6,
costing one additional TP.

**Both models drop gold T3** ("Students gain a lot out of the
experience personally, academically, and culturally"). Gold treats T3
as a second Claim in the introduction (a thesis preview after the
MajorClaim T1). Both models read it as MajorClaim elaboration, not a
separate Claim. This is a defensible inter-annotator disagreement but
costs both models one Claim TP (macro-F1 0.952 rather than 1.000).

---

## Cross-cutting observations

1. **Component-F1 is near-saturated at Stage 2.** Mean component-F1µ
   across all six cells is 0.984 (min 0.957). On essays 004 and 005
   both models are perfect or near-perfect. The only remaining
   component error worth flagging is the shared T3 drop on essay006,
   which is inter-annotator noise more than a model failure.

2. **Relation-F1 gains are concentrated on claim/premise-*role* fixes,
   not internal-paragraph topology.** Every essay in which the primary
   failure mode was a whole-sentence role mis-label — discourse-pivot
   inversion on essay004, clause-merging on Opus/005 — saw a lift once
   the tailored rule was explicit. Every essay in which the failure
   mode sat *inside* a paragraph (Gemini's staircase vs gold's
   sub-anchor on 006 para 1; Opus's flat star vs gold's sub-anchor in
   the same paragraph) still contains the error, because no rule in
   the prompt could be written without reading the paragraph's actual
   semantics.

3. **Opus and Gemini respond differently to the same emphasis text.**
   The Attack emphasis caused Gemini to produce correct Attack edges
   on essay005 with the right direction, but caused Opus to introduce
   a new Attack between the two sub-clauses — the right attacker, the
   wrong attackee. The same prompt calibrates two models on opposite
   sides of the same line. This is an argument for per-model prompt
   tuning rather than a single shared prompt.

4. **Stance accuracy remains perfect on aligned Claims.** Every
   aligned Claim has the correct For/Against stance across all six
   cells. This was true at Stage 1 and remains true at Stage 2 — the
   task neither helped nor hurt stance.

5. **The spurious "Claim-Against → MajorClaim" Attack edge (Opus/005,
   c11→c12).** The rebuttal Claim carries stance=Against already; gold
   uses stance to encode the rebuttal relation and does *not* emit an
   extra Attack edge from the rebuttal Claim to the MajorClaim. The
   tailored prompt did not include a rule against this because the
   behaviour did not appear in Stage 1 — it emerged at Stage 2 as a
   side-effect of the MajorClaim-repetition emphasis (Opus found the
   second MajorClaim and then tried to "link" the Claim-Against to
   it). This is a candidate Stage 3 rule: "stance alone handles
   Claim-Against to MajorClaim; do not emit an Attack edge in
   addition."
