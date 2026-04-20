# Group Assignment II — Task A (Argument Mining)

**Course**: PPOL 5204 Data Science II, Spring 2025

**Assignment**: Group Assignment II, Question 1, Task A — Prompt Engineering

**Chosen AI/ML challenge**: Can general-purpose LLMs perform end-to-end argument structure
extraction at the level of specialist fine-tuned systems?

We prompt **Opus** and **Google Gemini** with the same argument-mining task over
held-out essays from the UKP Argument Annotated Essays v2 corpus, score their outputs
against gold annotations, then refine the prompt and re-score — measuring both the lift
from prompt engineering and the residual limitations of current GenAI.

This README is the operation manual. Read it top-to-bottom before running anything.

---

## 1. Folder layout

```
group_assignment_2/
├── README.md                                       operation manual (this file)
│
├── documents/
│   ├── Group_Assignment_II.pdf                          original assignment brief
│   ├── Task_A_argument_mining.md                        Task A write-up / final report
│   ├── argument_mining_task_A_scheme.md                 full technical scheme + Claude dry-run
│   ├── argument_mining_preliminary_research_report.md   preliminary research notes
│   └── Task_A_argument_mining_materials.md              single-file submission bundle
│                                                        (essays + .ann + prompts + JSON outputs)
│
├── data/
│   ├── ArgumentAnnotatedEssays-2.0.zip   original archive from TUdatalib
│   ├── sample/                           essay001 (pedagogical sample, also embedded in
│   │                                     03_few_shot_example.md)
│   ├── ukp_essays_v2/                    unpacked corpus — 402 essays + docs
│   │   ├── brat-project-final/           .txt + .ann for every essay
│   │   ├── brat-project-final.zip        original BRAT archive
│   │   ├── guideline.pdf                 Stab & Gurevych annotation manual
│   │   ├── prompts.csv                   essay → prompt topic mapping
│   │   ├── README.txt                    UKP release notes
│   │   └── train-test-split.csv          official TRAIN / TEST assignment
│   └── eval/
│       ├── essays/                       essay004/005/006 — LLM input
│       └── gold/                         .ann answer keys — scoring only
│
├── prompts/
│   ├── 01_initial_prompt.md              Stage 1, zero-shot, ~100 words
│   ├── 02_refined_prompt.md              Stage 2 base (model-agnostic) — superseded
│   │                                     at runtime by the two model-specific variants
│   ├── 02_refined_prompt_opus.md         Stage 2 Opus-tailored (used for Opus runs)
│   ├── 02_refined_prompt_gemini.md       Stage 2 Gemini-tailored (used for Gemini runs)
│   └── 03_few_shot_example.md            essay001 + gold JSON demonstration
│
├── runs/
│   ├── stage1/
│   │   ├── opus/essay00X.json            Stage 1 raw responses (Opus)
│   │   ├── gemini/essay00X.json          Stage 1 raw responses (Gemini)
│   │   ├── calls.csv                     per-call bookkeeping
│   │   ├── scores.csv                    component-F1 / relation-F1 / stance-acc
│   │   └── divergence_log.md             qualitative error notes
│   └── stage2/                           same shape as stage1/
│
└── scripts/
    ├── score.py                          alignment + F1 scoring
    └── inspect.py                        helper for eyeballing aligned spans
```

---

## 2. Evaluation material

Three essays drawn from the UKP v2 **TEST split** (per `data/ukp_essays_v2/train-test-split.csv`),
never part of Stab & Gurevych's training data and therefore legitimate held-out material.

| Essay | Words | Gold components | Gold relations | Prompt topic | Role |
| --- | --- | --- | --- | --- | --- |
| essay004 | 288 | 11 | 6  | International tourism — positive trend? | warm-up |
| essay005 | 262 | 12 | 6  | Studying abroad vs staying home | medium |
| essay006 | 298 | 19 | 13 | Why students choose to study abroad | stress test |

essay006 has the most components and relations — keep it in to probe the ceiling.

---

## 3. What to send the model, and when

| Stage | Prompt file | Paired with | Essay source |
| --- | --- | --- | --- |
| 1 — zero-shot | `prompts/01_initial_prompt.md` | — | `data/eval/essays/essay00X.txt` |
| 2 — refined (Opus)   | `prompts/02_refined_prompt_opus.md`   | `prompts/03_few_shot_example.md` inlined | same essay |
| 2 — refined (Gemini) | `prompts/02_refined_prompt_gemini.md` | `prompts/03_few_shot_example.md` inlined | same essay |

The Stage 2 prompt was split into two model-specific variants after the
Stage 1 reflection showed Opus and Gemini fail differently; both variants
share their body with `02_refined_prompt.md` (kept as the base / audit trail)
and only differ in the final `MODEL-SPECIFIC EMPHASIS` block.

Each stage runs **three times** (once per test essay) on **each** of the two models:
**3 × 2 × 2 = 12 model calls total.**

---

## 4. Operation manual — step by step

### Step 1 — Stage 1, zero-shot

For each essay in `data/eval/essays/`:

1. Open `prompts/01_initial_prompt.md`.
2. Replace the `<<<PASTE FULL ESSAY TEXT HERE>>>` placeholder with the full contents of the `.txt` file.
3. Submit to **Opus**. Save the raw response verbatim as
   `runs/stage1/opus/essay00X.json`.
4. Submit the same prompt (unmodified) to **Gemini**. Save as
   `runs/stage1/gemini/essay00X.json`.
5. Log one row per call in `runs/stage1/calls.csv` — see Step 6 for fields.

After Step 1 you should have 6 JSON files (3 essays × 2 models) and 6 log rows.

### Step 2 — score Stage 1

For each of the 6 outputs, against the matching `data/eval/gold/essay00X.ann`:

- Parse the model output as JSON.
- Align predicted spans to gold with a ≥ 50 % token-overlap rule.
- Compute **component-F1** (micro and macro), **relation-F1** (endpoint-restricted),
  **stance accuracy**.
- Maintain a **divergence log** listing: hallucinated spans, boundary errors, polarity
  flips, over-predicted Attack relations.

Write scores to `runs/stage1/scores.csv` and the qualitative notes to
`runs/stage1/divergence_log.md`.

### Step 3 — design the refined prompts

- Use the Stage 1 divergence log to identify the two or three most common failure modes
  per model.
- Encode the *shared* failure modes (rules that apply to both models) into the body of
  `prompts/02_refined_prompt.md` — this remains the audited base prompt.
- Encode the *model-specific* corrections into the final
  `=== MODEL-SPECIFIC EMPHASIS ===` block of `prompts/02_refined_prompt_opus.md` and
  `prompts/02_refined_prompt_gemini.md`. Both files share their body with the base prompt;
  only the emphasis block differs.
- Do **not** change the schema block, the procedure block, or the few-shot example.
  Changing too much blurs the signal between prompt engineering and arbitrary rewriting.

### Step 4 — Stage 2, refined

For each essay in `data/eval/essays/` and each model:

1. Start from the model-specific prompt — `prompts/02_refined_prompt_opus.md` for Opus,
   `prompts/02_refined_prompt_gemini.md` for Gemini.
2. Replace the `<<<INSERT 03_few_shot_example.md HERE>>>` placeholder with the contents of
   `prompts/03_few_shot_example.md` (essay001 + gold JSON).
3. Replace the `<<<PASTE FULL ESSAY TEXT HERE>>>` placeholder with the target essay's text.
4. Submit to the corresponding model and save as
   `runs/stage2/opus/essay00X.json` or `runs/stage2/gemini/essay00X.json`.
5. Log the call in `runs/stage2/calls.csv`.

After Step 4 you should have 6 more JSON files and 6 more log rows.

### Step 5 — score Stage 2 and report

Same scoring procedure as Step 2, writing to `runs/stage2/scores.csv` and
`runs/stage2/divergence_log.md`.

Compose the final comparison in `documents/Task_A_argument_mining.md`:

- **Stage 1 → Stage 2 delta** per metric per model — the prompt-engineering *lift*.
- **Gap between the two models** at Stage 2 — which one is currently better and by how much.
- **Gap between each Stage-2 model and gold** — the residual GenAI limitation.
- Whether the two models **converged to each other or to gold** — Li et al. (2025, §3.2)
  call convergence-to-each-other-only "automation anchoring" and treat it as a warning sign.

### Step 6 — bookkeeping required for every call

For each of the 12 model calls, record one row in the appropriate `calls.csv` with fields:

| Field | Example                                              |
| --- |------------------------------------------------------|
| `timestamp` | 2025-04-15T14:02:17-04:00                            |
| `stage` | stage1 / stage2                                      |
| `model_family` | opus / gemini                                        |
| `model_version` | claude-opus-4-7 / gemini-3.1-pro                     |
| `temperature` | 0 (if adjustable), otherwise "default"               |
| `essay_id` | essay004 / essay005 / essay006                       |
| `prompt_path` | relative path to the prompt file used                |
| `output_path` | relative path to the saved response                  |
| `notes` | any interface quirks (retries, truncation, refusals) |

The assignment rubric asks for this paper trail — write it as you go; recovering it
afterwards is painful.

### Step 7 — assemble the submission bundle

The assignment brief asks us to submit "the initial prompt, the response generated by
the language models, and the improved response with added content highlighted for
clarity." The single-file deliverable that satisfies this is
`documents/submission_task_A.md`. It bundles, in one document:

- the three source essays + their gold `.ann` answer keys;
- all five prompt files in pipeline order (Stage 1 initial, Stage 2 base, the few-shot
  example, Stage 2 Opus-tailored, Stage 2 Gemini-tailored);
- every Stage 1 and Stage 2 model JSON output, grouped by model and paired by essay so
  the Stage 1 → Stage 2 delta for each (model, essay) cell reads in one downward scroll.

The analytical commentary on *why* the responses changed is not in the bundle — it
lives in `documents/Task_A_argument_mining.md` and the two `divergence_log.md` files.

---

## 5. Dataset provenance

- **Corpus**: UKP Argument Annotated Essays v2 (Stab & Gurevych, 2017).
- **Download**: <https://tudatalib.ulb.tu-darmstadt.de/handle/tudatalib/2422>.
- **License**: see `data/ukp_essays_v2/license.pdf`.
- **Citation**: Stab, C. & Gurevych, I. (2017). Parsing Argumentation Structures in
  Persuasive Essays. *Computational Linguistics*, 43(3), 619–659.
  <https://aclanthology.org/J17-3005/>.

## 6. Literature grounding

- Lawrence, J. & Reed, C. (2019). Argument Mining: A Survey. *Computational Linguistics*,
  45(4). <https://doi.org/10.1162/coli_a_00364>
- Li, H. et al. (2025). Large Language Models in Argument Mining: A Survey.
  arXiv:2506.16383. <https://arxiv.org/abs/2506.16383>
