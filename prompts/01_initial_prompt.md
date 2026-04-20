# Stage 1 — Initial (zero-shot) prompt

## Prompt text to paste

```
You are an argument-mining system. Given the essay below, extract its
argumentative structure using the Stab & Gurevych (2017) schema. Label every
argumentative span as MajorClaim, Claim, or Premise. For every Claim give its
stance (For or Against) toward the MajorClaim. For every Premise give its target
component id and the relation type (Support or Attack). Return strictly valid
JSON of the form:
{"components":[{"id","type","stance?","text"}],
 "relations":[{"src","tgt","type"}]}.
No prose, no explanation, no markdown fences. Essay:

<<<PASTE FULL ESSAY TEXT HERE>>>
```

## How to run

1. Open the essay file, e.g. `../data/eval/essays/essay004.txt`.
2. Replace `<<<PASTE FULL ESSAY TEXT HERE>>>` with the entire file contents.
3. Submit to ChatGPT and to Gemini (separately).
4. Save each raw response verbatim to, e.g.,
   `../runs/stage1/chatgpt/essay004.json` and
   `../runs/stage1/gemini/essay004.json`.
