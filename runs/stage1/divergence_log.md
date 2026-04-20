# Stage 1 — divergence log

Qualitative companion to `scores.csv`. Each section records how the model
output diverges from gold: alignment misses, type errors, polarity flips,
relation-topology errors.

## Summary table

| model  | essay    | comp F1 (µ / M) | stance acc | rel F1 |
| ------ | -------- | --------------- | ---------- | ------ |
| opus   | essay004 | 0.636 / 0.667   | 1.00 (1/1) | 0.000  |
| opus   | essay005 | 0.909 / 0.922   | 1.00 (3/3) | 0.727  |
| opus   | essay006 | 0.919 / 0.786   | 1.00 (3/3) | 0.615  |
| gemini | essay004 | 0.636 / 0.667   | 1.00 (1/1) | 0.000  |
| gemini | essay005 | 0.917 / 0.852   | 1.00 (4/4) | 0.833  |
| gemini | essay006 | 0.974 / 0.963   | 1.00 (4/4) | 0.769  |

- **Stance accuracy is perfect for both models on all three essays.** When a
  model correctly classifies something as a Claim and it aligns to a gold
  Claim, it never flipped For ↔ Against. The residual error is entirely in
  the component-type and relation-topology layers, not in polarity.
- **Gemini beats Opus on every metric on essay005 and essay006.** The gap is
  largest on relation F1 (+0.106 on essay005, +0.154 on essay006).
- **Both models are identical and terrible on essay004** — same per-label
  counts, same relation F1 = 0.000, same seven matched spans. This is the
  automation-anchoring pattern Li et al. (2025 §3.2) warn about.

---

## essay004 — identical structural inversion (both models)

Gold structure (paragraph 1):
`T6 "tourists from different cultures..." (Premise)`  →
`T4 "international tourism can create negative impacts" (Claim)`, with
Thailand exemplar premises T7/T8 supporting T4.

Both models inverted this: they treated the topic-sentence opener
(*"it is an undeniable fact that tourists..."*) as the **Claim** and the
paragraph's concluding line (*"this proves that international tourism can
create negative impacts"*) as a **Premise** supporting it. The Thailand
premises were then all redirected to the opener. The same inversion
happened in paragraph 2 with the Great Barrier Reef claim.

Consequence:
- Per-label counts **identical across the two models**:
  `MajorClaim 2/0/0, Claim 1/2/2, Premise 4/2/2` (TP/FP/FN).
- All six predicted relations land at the wrong target node → relation
  F1 = 0.000 for both.

This is not a bug in alignment — every predicted span is aligned to the
right gold span with ≥ 50% token overlap. The spans are correct; the
**role assignments** and therefore the **edges** are wrong in the same way
for both models.

Why this is worth flagging: the two independent models converged to each
other, not to gold. Exactly the warning sign the survey describes —
"automation anchoring" — which tempts evaluators to treat cross-model
agreement as a proxy for correctness. It isn't.

Failure mode label: **discourse-pivot inversion** — when a paragraph opens
with a generic claim-like sentence and ends with a more specific
interpretive sentence marked by "therefore this proves that…", both
models pick the opener as the Claim and the pivot as a Premise. Gold does
the opposite.

---

## essay005 — attack relations are the differentiator

Gold has 2 Attack relations (rare in this corpus):
- R2 attacks T7→T4 : "struggle with loneliness" attacks "irreplaceable experience…"
- R3 attacks T8→T7 : "difficulties turn into valuable experiences" attacks "struggle with loneliness"

**Gemini**: captured R2 correctly as `T5(→T7) → T4 Attack`. Missed R3 —
predicted `T6→T4 Support` instead of `T6→T5 Attack` (kept the polarity on the
wrong parent).

**Opus**: captured zero Attacks. Root cause: Opus merged gold T7 + T8
into a single Premise (T6 in the Opus output), collapsing the attack
chain into one relation which it then labeled Support. This is the
*span-boundary error feeding a polarity error* — the two failure modes
compound.

Opus also dropped gold T12 ("there are many difficulties a student might
face…" — an Against-stance Claim) entirely. It over-promoted the
conclusion line to MajorClaim T2 and never emitted the concession Claim.
Gemini got T12 right with stance=Against.

That's a clean 2-point Claim gap on this essay: Gemini 4 correct Claims,
Opus 3.

---

## essay006 — Gemini's sub-anchor wins the rel-F1 margin

Gold routes the final paragraph through a sub-anchor:
`T17, T18, T19 → T16` (each supports "Learning about others' cultures is so
important"), and `T13, T14, T15, T16 → T6` (the paragraph Claim).

**Gemini** reproduced the sub-anchor exactly:
`T16→T15, T17→T15, T18→T15` (Gemini T15 = gold T16). +3 correct edges from this topology alone.

**Opus** flattened the same sentences into parallel supports of the
paragraph claim: `T16→T11, T17→T11, T18→T11`. Three edges wrong, three TP
lost.

Both models missed the same internal chain `T8→T9, T10→T9` in the first
paragraph — gold routes "challenges in the host country" and "overcoming
problems" *into* the modal premise "should be able to deal with the
obstacles", and both models read those as parallel supports of the main
Claim instead. So there's a shared failure mode here too: **chain
flattening** — reading two-hop argument chains as one-hop stars.

Opus also dropped one of the two MajorClaims entirely (missed the
conclusion "studying abroad does not only have advantages, but also can
change us in a very positive way"), while Gemini captured both. That
accounts for Opus's macro-F1 dropping to 0.786 on essay006 despite
micro-F1 being 0.919 — the MajorClaim class dips to F1 = 0.667.

Gemini over-segmented: it emitted one extra unaligned Claim (T20 "It can
influence us in different aserects of life") which gold treats as part of
the conclusion MajorClaim. Minor +1 FP.

---

## Failure modes to target in Stage 2

Ranked by impact on F1:

1. **Discourse-pivot inversion** (essay004, both models) — when a
   paragraph pivots from a general opener to a specific conclusion via
   "therefore this proves that…", the **conclusion** is the Claim and the
   **opener** is the Premise. The refined prompt needs to name this
   pattern explicitly.
2. **Chain flattening** (essay006, both models) — support chains of
   length 2 (`a → b → c`) get collapsed into stars (`a → c, b → c`). The
   refined prompt should note that intermediate premises can themselves
   be targets of support.
3. **Span-boundary merging** (essay005, Opus only) — Opus merged a
   clause chain joined by "but" into one premise, swallowing an Attack
   relation. Need a rule: "but", "however", "nevertheless" often
   separate two distinct argumentative units with opposing polarity.
4. **Attack under-prediction** (essay005, Opus especially) — given the
   rarity of Attacks in the corpus, models default to Support. Need to
   highlight the concession/objection pattern.
5. **MajorClaim dropping** (essay006, Opus) — Opus under-emits the second
   MajorClaim. Prompt should remind the model that MajorClaim often
   appears twice: introduction and conclusion, as restatements.

Opus-specific corrections for Stage 2:
- MajorClaim-repetition reminder (§5)
- Clause-separation rule for "but/however/nevertheless" (§3)

Gemini-specific corrections for Stage 2:
- Closing pointer-sentence rule: "It can influence us in different
  aspects of life" is part of the preceding MajorClaim, not a separate
  Claim (§ essay006 T20 over-segmentation).

Both-models corrections for Stage 2:
- Discourse-pivot rule: opener-vs-conclusion Claim assignment (§1).
- Chain-flattening rule: premises can target other premises (§2).
- Attack-cue list (§4).
