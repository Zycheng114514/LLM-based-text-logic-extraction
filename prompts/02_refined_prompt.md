# Stage 2 — Refined prompt


## Refined prompt template

```
You are an argument-mining system applying the Stab & Gurevych (2017) schema
to a persuasive essay. Follow this schema strictly.

COMPONENTS
- MajorClaim: the essay's overall thesis. Usually 1–2 per essay, stated in the
  introduction and/or conclusion.
- Claim: a controversial sub-statement that branches from the MajorClaim and
  itself needs justification. Typical count: 3–6 per essay.
- Premise: a reason, example, or piece of evidence that grounds a Claim (or
  occasionally another Premise). A premise reports or illustrates; a claim
  takes a position.

ATTRIBUTES
- Stance on a Claim: "For" if the Claim supports the MajorClaim, "Against" if
  the Claim opposes it (typically raised so the author can rebut it).

RELATIONS
- Support: the source component gives reason to accept the target.
- Attack: the source component directly contradicts or rebuts the target.
  Default to Support. Mark Attack ONLY when the source explicitly contradicts
  the target's polarity — do not infer Attack from discourse pivots such as
  "however" or "on the other hand".

SPAN BOUNDARIES
- The span of a component is the proposition itself, without framing connectives
  ("Consequently", "Therefore", "First of all", "No matter from the view of…").

PROCEDURE (think step by step, but do not output your reasoning)
1. List every sentence that makes an argumentative assertion.
2. Label each as MajorClaim, Claim, or Premise using the definitions above.
3. For each Claim, decide its Stance toward the MajorClaim.
4. For each Premise, identify its single target component and the relation type.
5. Emit the final JSON only.

OUTPUT FORMAT
Return strictly valid JSON, no prose, no markdown fences:
{
  "components": [{"id": "c1", "type": "MajorClaim|Claim|Premise",
                  "stance": "For|Against",        // only if type == Claim
                  "text": "<exact span from essay>"}],
  "relations":  [{"src": "c<i>", "tgt": "c<j>", "type": "Support|Attack"}]
}

WORKED EXAMPLE
<<<INSERT 03_few_shot_example.md HERE>>>

NOW APPLY THE SAME PROCEDURE TO THIS ESSAY:
<<<PASTE FULL ESSAY TEXT HERE>>>
```

## Per-model adjustments (fill in after Stage 1)

ChatGPT-specific correction (if applicable):
- …

Gemini-specific correction (if applicable):
- …

## How to run

1. Replace `<<<INSERT 03_few_shot_example.md HERE>>>` with the *contents* of
   `03_few_shot_example.md` (essay + its gold JSON).
2. Replace `<<<PASTE FULL ESSAY TEXT HERE>>>` with the target essay.
3. Submit to ChatGPT and to Gemini.
4. Save outputs to `../runs/stage2/chatgpt/essay00X.json` and `../runs/stage2/gemini/essay00X.json`.
