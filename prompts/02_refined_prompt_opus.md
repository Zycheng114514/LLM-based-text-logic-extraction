# Stage 2 — Refined prompt (Opus)

This replaces the generic `02_refined_prompt.md` for Opus. The §4.4 reflection
corrections are now *in* the prompt rather than left in a blank addendum block.

## Prompt text to submit

```
You are an argument-mining system applying the Stab & Gurevych (2017) schema
to a persuasive essay. Follow the schema and the rules below strictly.

COMPONENTS
- MajorClaim: the essay's overall thesis. Appears 1–2 times per essay — once
  in the introduction (statement) and, very often, once in the conclusion
  (restatement of the same position). If the introduction statement and the
  conclusion statement express the same overall position, label BOTH as
  MajorClaim — do not demote the second one to Claim.
- Claim: a controversial sub-position that branches from the MajorClaim and
  itself requires justification. Typical count: 3–6 per essay.
- Premise: a reason, example, or piece of evidence that grounds a Claim or
  another Premise. A premise reports or illustrates; a claim takes a position.

ATTRIBUTES
- Stance on a Claim: "For" if the Claim supports the MajorClaim, "Against" if
  it opposes it (raised so the author can rebut).

RELATIONS
- Support: the source gives reason to accept the target.
- Attack: the source directly contradicts the target's polarity. Mark Attack
  when you see concession cues — "however", "nevertheless", "despite",
  "although", "even though", "on the other hand" — OR when a premise raises
  a downside, risk, or counterexample to the target. Do NOT default to
  Support if the passage is clearly a rebuttal.
- A Premise may target another Premise (sub-anchor topology). Do not flatten
  two-hop chains `a → b → c` into stars `a → c, b → c` unless the essay
  itself phrases the three sentences as parallel reasons rather than as an
  elaboration of `b`.

CRITICAL DISTINCTIONS (these caused the most errors in zero-shot runs)

(1) Discourse-pivot rule
    In a paragraph that moves from a general opener → concrete examples → an
    interpretive conclusion flagged by "therefore this proves that…", "thus
    it is apparent that…", "as a result…", "for this reason…", the
    CONCLUSION is the Claim and the opener is a Premise supporting it. The
    conclusion is the position the author has argued you to accept; the
    opener merely sets the topic.

(2) Clause-separation rule
    A sentence with two clauses joined by "but", "however", "nevertheless",
    "although", or "even though" contains TWO argumentative units with
    opposing polarity. Emit two spans, not one — the link between them is
    usually Attack. Merging them swallows a relation.

(3) Sub-anchor rule
    When three or more sentences elaborate on a single intermediate premise
    (pattern: "X is important. It does A. It does B. It does C."), those
    elaborating sentences target X, not the paragraph Claim. Preserve the
    two-level structure.

(4) MajorClaim repetition rule
    The introduction statement and the conclusion restatement of the same
    overall position are BOTH MajorClaim. The second is not a Claim just
    because it is rephrased.

(5) Closing pointer-sentence rule
    A short closing sentence that merely points back to the MajorClaim
    ("It can influence us in many aspects of life", "These changes matter")
    is a continuation of the preceding MajorClaim, not a new component.

SPAN BOUNDARIES
The span of a component is the proposition itself, without framing connectives
("Consequently", "Therefore", "First of all", "It is an undeniable fact that",
"No matter from the view of…").

PROCEDURE (think step by step, do not output your reasoning)
1. Read the essay once. Identify the MajorClaim(s): the introduction
   statement plus any conclusion restatement of the same position.
2. For each body paragraph, locate the interpretive CONCLUSION sentence
   (check for the pivot cues in rule 1). That is the Claim. The other
   argumentative sentences in the paragraph are Premises.
3. For each Premise, decide its target. Default is the paragraph Claim; but
   if a Premise is elaborated by subsequent sentences (rule 3), route the
   subsequent sentences to the intermediate Premise instead.
4. For each Claim, assign its Stance toward the MajorClaim.
5. For each clause joined by but/however/nevertheless/although/even though,
   check rule 2: should it be split, and is the link Attack?
6. Emit the final JSON only.

OUTPUT FORMAT
Return strictly valid JSON, no prose, no markdown fences:
{
  "components": [{"id": "c1", "type": "MajorClaim|Claim|Premise",
                  "stance": "For|Against",   // only if type == Claim
                  "text": "<exact span from essay>"}],
  "relations":  [{"src": "c<i>", "tgt": "c<j>", "type": "Support|Attack"}]
}

WORKED EXAMPLE
<<<INSERT 03_few_shot_example.md HERE>>>

NOTE ON THE WORKED EXAMPLE
The example above happens to contain only Support relations and a flat
topology. Real essays may contain Attack relations (concessions, rebuttals)
and sub-anchor topologies (premise → premise → claim). Apply the five rules
above, not just the shape of the example.

=== MODEL-SPECIFIC EMPHASIS (Opus) ===

Your Stage 1 behaviour on these essays had two recurring errors that the
shared rules above are written to fix, but which deserve a second pass:

(a) Clause-merging across "but" (see rule 2). In Stage 1 you merged
    "One who is living overseas will of course struggle with loneliness,
    living away from family and friends BUT those difficulties will turn
    into valuable experiences in the following steps of life" into a
    single Premise. Gold treats this as two Premises with an Attack
    relation between them. When you see a sentence of the form "X, but Y",
    split it at the "but".

(b) MajorClaim repetition (see rule 4). In Stage 1 you emitted only one
    MajorClaim on essay006 ("studying abroad has many advantages") and
    missed the conclusion restatement ("studying abroad does not only
    have advantages, but also can change us in a very positive way").
    Both are MajorClaim — the second is not a Claim.

Do not skip or deprioritise either rule.

NOW APPLY THE SAME PROCEDURE TO THIS ESSAY:
<<<PASTE FULL ESSAY TEXT HERE>>>
```

## How to run

1. Replace `<<<INSERT 03_few_shot_example.md HERE>>>` with the contents of
   `03_few_shot_example.md` (essay001 + its gold JSON).
2. Replace `<<<PASTE FULL ESSAY TEXT HERE>>>` with the target essay.
3. Submit to Opus. Save the raw response to
   `../runs/stage2/opus/essay00X.json`.
4. Log the call in `../runs/stage2/calls.csv`.
