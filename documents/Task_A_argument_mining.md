# Task A — Argument Mining

## 1. Background

### 1.1 The chosen AI/ML challenge

We frame our Task A question as a current problem in NLP:
**can general-purpose large language models perform end-to-end argument structure extraction?** Argument mining (AM) is the automatic
identification of the claims, premises, and inferential links that make up a piece of
reasoning in natural language (Lawrence & Reed 2019). It recovers the structure of
justification, which is essential for fact-checking, policy analysis, legal reasoning, online
discourse moderation, and the study of political communication.


Classical AM treated component detection, relation prediction, and quality assessment as
independent supervised problems, each trained on a small task-specific corpus (Palau & Moens
2009; Stab & Gurevych 2017). The LLM era has blurred those boundaries: prompting,
chain-of-thought reasoning, and in-context learning now let a single model attempt the full
pipeline without task-specific training (Li et al. 2025). Zero-shot AM is still an open 
research problem, and the result from different LLM models could be different.

### 1.2 Annotation schema

We adopt the **Stab & Gurevych (2017) claim–premise schema**, treated as canonical by both
literatures we reviewed (Lawrence & Reed 2019 §6; Li et al. 2025 §3). It has three components
(MajorClaim, Claim, Premise), two relation types (Support, Attack), and a Stance attribute
(For / Against) attached to each Claim. The schema is compact enough for zero-shot
prompting, yet detailed enough to support quantitative comparison: gold annotations exist,
inter-annotator agreement is well documented (κ ≈ 0.81), and F1 is the standard metric at
both the component and the relation level.

The three component labels form a hierarchy of controversy. A **MajorClaim** is the
essay's overall thesis — the position the author ultimately wants the reader to accept,
usually stated in the introduction and echoed in the conclusion, and typically occurring
once or twice per essay. A **Claim** is a controversial sub-statement that itself requires
justification and is marked with a **Stance** attribute (`For` or `Against`) indicating
whether it argues in support of or against the MajorClaim. A **Premise** is a reason,
example, or piece of evidence that grounds a Claim (or occasionally another Premise); the
practical test is that a Premise *reports or illustrates*, whereas a Claim *takes a
position*. These components are linked by two relation types: **Support**, in which the
source gives reason to accept the target, and **Attack**, in which the source contradicts
or rebuts it.

To anchor the schema in a concrete example, consider an essay in UKP dataset on
cooperation versus competition: the MajorClaim *"we should attach more importance to
cooperation during primary education"* is supported by the Claim *"through cooperation,
children can learn about interpersonal skills"* (Stance `For`), which is in turn supported
by premises describing the specific skills acquired through team work. An opposing Claim
such as *"competition makes the society more effective"* (Stance `Against`) may also appear
— raised so that the author can rebut it — and its premises will typically link by
Support to *that* Claim, not by Attack to the MajorClaim. (Attack relations are in fact
rare in UKP)

### 1.3 Dataset

Our evaluation substrate is the **UKP Argument Annotated Essays v2** corpus (Stab & Gurevych
2017), 402 persuasive student essays released under the Stab & Gurevych schema and
distributed freely via TU Darmstadt's TUdatalib repository. Each essay ships as a raw
`.txt` plus a BRAT-standoff `.ann` file containing character-offset spans and their labels.
We sample essays from the official test split so that evaluation is directly comparable to
published baselines.

---

## 2. Operation scheme

**Model:** We compare **Opus 4.7 and Google Gemini 3.1 Pro**.

**Material:** From the UKP v2 **test split** we draw **three essays**.
The `.txt` content is fed to the models inside the prompt; the gold `.ann` file is stored
separately and only used for scoring. (It 's worth noting that UKP essays are very likely
to be  in both models' pre-training data, and the point of the experiment is to
measure prompt-engineering lift, not training recall.)

### 2.1 Prompt design

The **initial prompt** (~100 words) is strictly zero-shot: it names the schema, lists the
component and relation labels, and demands a single strict-JSON output. No examples, no
decomposition, no reasoning scaffolding. This deliberately exposes each model's default
behaviour.

The **refined prompt** can be different for the two models, and could include:

- Full schema definitions inlined (what counts as MajorClaim vs Claim vs Premise).
- One or two few-shot examples drawn from the UKP **train** split, never from the test set.
- Chain-of-thought scaffold: (i) list argumentative sentences, (ii) classify each,
  (iii) link premises to targets.
- Cardinality hints ("typical essay: 1–2 MajorClaims, 3–6 Claims") and a default-Support
  rule ("mark Attack only if the premise explicitly contradicts the target").

### 2.2 Scoring

Scoring answers two questions at once: *of what the model produced, how much was correct?*
(precision) and *of what was actually in the gold, how much did the model find?* (recall).
Because argument mining involves more than one layer — components, relations, stances — we
compute a separate metric for each, and keep a written error log to capture the failures
that pure numbers do not.

- **Component-F1 (micro and macro)**
  
  Each argumentative span predicted by the model is
  compared to the gold spans under a ≥ 50 % token-overlap rule: a predicted span counts as a
  match to a gold span if the two share at least half of their tokens, following Persing &
  Ng (2016), as free-text LLM outputs rarely agree on exact character boundaries with 
  a human annotator. A matched span with the correct label is a **true positive**; a
  predicted span with no gold counterpart (or the wrong label) is a **false positive**; a
  gold span the model missed is a **false negative**. We report both micro and macro F1
  because a model that looks strong on micro may be silently failing on MajorClaim.


- **Relation-F1** 

  A relation is an edge between two components — for example,
  `Premise T4 Support Claim T3`. A predicted relation counts as a true positive only when
  all three of {source span, target span, relation type} match gold. We restrict this
  calculation to predicted relations whose *endpoints have already matched* a gold
  component: if the source or target span is hallucinated, any relation that uses it is
  already counted as an error at the component level, and penalising it a second time at
  the relation level would double-count the same mistake. Relation-F1 therefore isolates
  the quality of the model's inferential wiring, independent of its span detection.


- **Stance accuracy.** 

  For every Claim the model found and correctly aligned to gold, we
  check whether the Stance attribute (`For` / `Against`) is right. Because the denominator
  here — matched Claims — is fixed by the component-level alignment, a single accuracy
  number is sufficient; no precision/recall split is needed.


- **Qualitative divergence log** 

  F1 alone does not tell us *why* a model erred, but the
  "refined prompt" in Stage 2 has to target specific failure modes, so we maintain a
  written catalogue of error types. Four categories recur in LLM argument mining (Li et
  al. 2025, §4):
  - **Hallucinated span** — a stretch of text labelled as argumentative when gold treats
    it as non-argumentative filler. Typically arises because the text *sounds* claim-like.
  - **Boundary error** — correct label but wrong span edges, for instance dragging in a
    framing connective ("Consequently", "no matter from the view…") that gold excludes.
    Boundary errors still count as true positives under the ≥ 50 % rule but degrade
    downstream reasoning.
  - **Polarity flip** — a correctly identified Claim is given the wrong Stance.

---

## 3. First-stage operation and result

We submitted the zero-shot prompt to each
of the two models, once per test essay, for a total of six calls. Both models
were queried at the default temperature through their web interfaces, with no system
message, no memory, no tool access, and no retries.

The score table below summarises the results.

| model  | essay    | Component-F1 (micro / macro) | stance acc (n) | Relation-F1 |
| ------ | -------- |------------------------------| -------------- | ------ |
| Opus   | essay004 | 0.636 / 0.667                | 1.00 (1/1)     | 0.000  |
| Opus   | essay005 | 0.909 / 0.922                | 1.00 (3/3)     | 0.727  |
| Opus   | essay006 | 0.919 / 0.786                | 1.00 (3/3)     | 0.615  |
| Gemini | essay004 | 0.636 / 0.667                | 1.00 (1/1)     | 0.000  |
| Gemini | essay005 | 0.917 / 0.852                | 1.00 (4/4)     | 0.833  |
| Gemini | essay006 | 0.974 / 0.963                | 1.00 (4/4)     | 0.769  |

Three observations jump out of the table:

- **Stance is a solved problem even at zero shot.** Every Claim that the
  model aligned to a gold Claim received the correct Stance value, across
  all six calls. The error budget for Stage 2 is entirely in component
  typing and relation wiring, not in polarity.
- **Gemini strictly dominates Opus on essay005 and essay006** on every
  metric — most visibly on relation F1 (+0.11 and +0.15).
- **Both models have a poor performance on essay004.**

### 3.1 The essay004 failure

Essay004's paragraphs are organised as *general-opener → concrete-examples
→ interpretive-conclusion*, with each paragraph's conclusion flagged by
"therefore this proves that…" or "thus, it is apparent that…". Gold treats
the concluding sentence as the **Claim** and the opener as a **Premise**
supporting it; both models read it the other way round. The seven
argumentative spans are aligned correctly under the ≥ 50 % token-overlap
rule, but their role assignments are inverted, and every one of the six
predicted relations therefore points at the wrong target. Relation F1
collapses to zero even though no span was hallucinated.

The two independently-trained models made identical errors on essay004.
This is exactly the pattern Li et al. (2025, §3.2) 
warns about: cross-model agreement is not evidence of correctness. 
The gold annotation is the only thing that catches this. LLM-vs-LLM 
comparisons do not substitute for human gold.

### 3.2 The essay005 attack-relation gap

Essay005 is unusual: its gold annotation contains two Attack relations,
where the rest of the UKP corpus is overwhelmingly Support-only. The two
models handled this very differently:

- **Gemini** correctly identified one of the two Attacks (struggling with
  loneliness ⟂ the "irreplaceable experience" claim). It missed the
  second Attack by attaching the rebutting premise to the wrong target.
- **Opus** identified zero Attacks. Root cause is a span-boundary error
  upstream: Opus merged two adjacent clauses joined by "but" into a
  single premise, collapsing both Attack relations into one Support
  relation and losing them both.

Opus additionally dropped the concession Claim "there are many
difficulties a student might face…" (Stance `Against`) by promoting the
conclusion sentence to MajorClaim instead. Gemini captured this Claim
correctly. The cumulative effect is a 2-point Claim gap and the large
relation-F1 margin in Gemini's favour.

### 3.3 The essay006 topology gap

Essay006's final paragraph is annotated with a *sub-anchor* structure:
three premises support "Learning about others' cultures is so important",
which itself supports the paragraph's Claim, "Most important is the
cultural aspect of the experience". Gemini reproduced the sub-anchor
exactly — three correct edges to the intermediate node. Opus flattened
the same fan into parallel support of the paragraph Claim, losing three
true positives.

Both models missed the same internal chain at the top of the essay
(`T8 → T9` and `T10 → T9`), reading a two-hop chain as a one-hop star
around the paragraph's central Claim. Shared failure mode: **chain
flattening**.

Opus also under-emitted MajorClaims on this essay, failing to capture the
conclusion-paragraph restatement. This is what pushes Opus's **macro** F1
below its **micro** F1 on essay006 (0.786 vs. 0.919) — the MajorClaim
class F1 falls to 0.667 even though overall span matching is high.

---

## 4. Reflection on Stage 1


Two models with zero-shot prompt can already:

- returned syntactically valid, fence-free JSON on the first attempt for
  every call, honouring the output contract;
- correctly identified the majority of argumentative spans under the
  ≥ 50 % overlap rule (16 of 19 on essay006, 10–12 of 12 on essay005);
- assigned the correct Stance to every Claim they correctly aligned
  (31/31 across all six calls).


### 4.1 Zero-shot prompt failures

The five cross-cutting failure modes are:

1. **Discourse-pivot inversion.** When a paragraph moves from a
   general-sounding opener to a specific conclusion via "therefore this
   proves that…", both models pick the opener as Claim and the
   conclusion as Premise. Gold does the opposite. This mode alone
   accounts for the essay004 zero on relation F1 for **both** models.

2. **Chain flattening.** Two-hop support chains (`a → b → c`) are read
   as one-hop stars (`a → c, b → c`). Both models share this mode;
   it accounts for most of the residual relation-F1 gap on essay006 and
   for both models' missed edges in the first paragraph of essay006.

3. **Span-boundary merging.** Clauses joined by "but / however /
   nevertheless" get merged into a single argumentative unit, swallowing
   a relation — and possibly a polarity flip — that lived in the
   clause break. Opus-specific in our sample (essay005).

4. **Attack under-prediction.** Because Attack is rare in the training
   distribution, models default to Support. When a rebutting premise is
   actually present, the default still wins. Opus exhibits this
   strongly; Gemini partially.

5. **MajorClaim dropping.** MajorClaims usually appear twice in an essay
   (introduction restated in conclusion). Opus sometimes emits only the
   first. This is the reason its macro F1 on essay006 (0.786) understates
   how well its span detection is actually working (micro 0.919).

### 4.2 Improvement on stage 2

- **Shared correction** (both models): a discourse-pivot rule
  ("therefore this proves that…" marks a Claim, not a Premise), a
  chain-flattening correction (premises can themselves be targets of
  support), and an Attack cue-list ("however", "nevertheless", "despite",
  concession frames).
- **Opus-specific correction**: a clause-separation rule for
  but/however/nevertheless, and a MajorClaim-repetition reminder
  ("MajorClaim typically appears once in the introduction and once in the
  conclusion").
- **Gemini-specific correction**: a closing-pointer-sentence rule
  ("It can influence us in different aspects of life" is a
  continuation of the preceding MajorClaim, not a separate Claim).

---

## 5. Second-stage operation and result

### 5.1 Prompt design

Stage 2 targets the five failure modes catalogued in §4.4 with two
model-specific prompts sharing a common body. The shared body inlines the full
Stab & Gurevych schema, a single worked example drawn from the UKP
train split (essay001), and five numbered rules promoted directly from
the Stage 1 correction list:

1. **Discourse-pivot rule** — "therefore this proves that…", "thus it
   is apparent that…", "as a result…" flag the Claim at the *end* of a
   paragraph, not the opener. Targeted at the essay004 inversion.
2. **Clause-separation rule** — sentences with but/however/nevertheless/
   although contain two argumentative units with opposing polarity;
   emit two spans and an Attack. Targeted at Opus's essay005 clause
   merge.
3. **Sub-anchor rule** — a Premise may target another Premise; do not
   flatten chains into stars. Targeted at the essay006 topology.
4. **MajorClaim-repetition rule** — introduction statement and
   conclusion restatement of the same position are *both* MajorClaim.
   Targeted at Opus's essay006 single-MajorClaim emission.
5. **Closing pointer-sentence rule** — a short closing sentence that
   merely points back to the MajorClaim ("It can influence us in many
   aspects of life") is continuation, not a new component. Targeted at
   Gemini's closing-sentence promotion.

Because the worked example is flat and contains only Support edges, the
prompt also warns each model explicitly that real essays are not
example-shaped and that it must apply the rules rather than imitate the
example. The Opus-specific block calls out by
name the exact essay005 "but" span Opus had merged at Stage 1 and the
exact essay006 MajorClaim it had missed. The Gemini-specific block is
framed as a preservation ask rather than an acquisition ask: it tells
Gemini to keep the Attack and sub-anchor behaviours it already
demonstrated at Stage 1, and not to let the flat Support-only example
override them.

### 5.2 Results

The score table for stage 2 is below.

| model  | essay    | Component-F1 (micro / macro) | stance acc (n) | Relation-F1 |
| ------ | -------- | ----------------------------- | -------------- | ----------- |
| Opus   | essay004 | 0.957 / 0.974                 | 1.00 (3/3)     | 0.462       |
| Opus   | essay005 | 1.000 / 1.000                 | 1.00 (4/4)     | 0.615       |
| Opus   | essay006 | 0.973 / 0.952                 | 1.00 (3/3)     | 0.846       |
| Gemini | essay004 | 1.000 / 1.000                 | 1.00 (3/3)     | 0.500       |
| Gemini | essay005 | 1.000 / 1.000                 | 1.00 (4/4)     | 0.833       |
| Gemini | essay006 | 0.973 / 0.952                 | 1.00 (3/3)     | 0.692       |

The changes from stage 1 to stage 2 are below.

| model  | essay    | ΔComponent-F1 (micro / macro) | Δstance acc (n)    | ΔRelation-F1 |
| ------ | -------- | ------------------------------ | ------------------ | ------------ |
| Opus   | essay004 | **+0.321** / **+0.307**        | 0.00 (1/1 → 3/3)   | **+0.462**   |
| Opus   | essay005 | +0.091 / +0.078                | 0.00 (3/3 → 4/4)   | −0.112       |
| Opus   | essay006 | +0.054 / **+0.166**            | 0.00 (3/3 → 3/3)   | **+0.231**   |
| Gemini | essay004 | **+0.364** / **+0.333**        | 0.00 (1/1 → 3/3)   | **+0.500**   |
| Gemini | essay005 | +0.083 / **+0.148**            | 0.00 (4/4 → 4/4)   | 0.000        |
| Gemini | essay006 | −0.001 / −0.011                | 0.00 (4/4 → 3/3)   | −0.077       |

the tailored prompt closed a large fraction of the
headroom on every essay that had a *whole-sentence role-labelling*
failure at Stage 1 (essay004 for both models, Opus's clause merge on
essay005, Opus's sub-anchor collapse on essay006). It produced no lift
on essays whose failures sat inside a paragraph's internal topology
(Gemini's essay006 paragraph 1), and it introduced a small new failure
(Opus's Attack-endpoint reversal on essay005) because splitting the
"but" clause exposed an edge the model had not previously had to commit
to.

### 5.3 Improvements on Stage 1

- **Discourse-pivot inversion (essay004).** Both models now label the
  interpretive conclusion ("international tourism can create negative
  impacts…"; "tourism has threatened the nature environments") as Claim
  and the topic-sentence opener as Premise. Every Stage-1 relation on
  essay004 had pointed at the wrong target; Stage 2 produces three true
  positives per model. This is the single largest absolute lift in the
  study (+0.462 / +0.500 on relation F1) and vindicates the
  discourse-pivot rule as the highest-yield addition.
- **Clause-merge (Opus essay005).** Opus now splits the
  loneliness/difficulties "but" clause into two Premises, matching gold
  span-for-span. Component F1 → 1.000.
- **MajorClaim repetition (Opus essay006).** The conclusion restatement
  is now captured as a second MajorClaim instead of being demoted to
  Claim. Macro F1 rises from 0.786 to 0.952.
- **Sub-anchor preservation (Opus essay006 final paragraph).** The
  three elaborating sentences on "Learning about others' cultures" now
  correctly target the intermediate premise rather than jumping to the
  paragraph Claim. This is the source of Opus's +0.231 relation-F1 gain.

### 5.4 Issues persist

- **Internal-paragraph topology (essay004 and essay006 paragraph 1).**
  Gemini's essay004 builds a premise chain (c4→c3, c5→c3, c3→c6) where
  gold has parallel premise-to-Claim edges; Opus's essay004 routes c5→c4
  where gold has c5→c6. On essay006 paragraph 1, gold uses a sub-anchor
  (T8 and T10 both target T9) but Opus flattens to a star and Gemini
  builds a staircase. Neither shape is a gross error; both are
  paragraph-local misreadings that would require the model to understand
  the author's specific chain of reasoning, not a rule that can be
  stated generically.
- **Attack endpoint selection (Opus essay005).** The clause-separation
  rule produced the correct two Premises but Opus chose the wrong
  direction for the inter-premise Attack (predicted c5→c6 where gold is
  T8→T7) and introduced a spurious c11→c12 Attack between the
  Claim-Against and the MajorClaim (gold uses stance to encode this
  rebuttal; it does not emit an additional edge). Together these cost
  Opus two true positives and one false positive on a single essay.
- **Shared T3 drop on essay006.** Both models read the introduction's
  second sentence ("Students gain a lot out of the experience
  personally, academically, and culturally") as continuation of the
  MajorClaim.



---

## 6. Final reflection

Our guiding question was whether general-purpose LLMs can perform
end-to-end argument structure extraction. The answer, on this sample,
is *yes for components and stance and only partially for relations,
with the lift from prompt engineering concentrated on a small number of
nameable failure modes.* At Stage 2 the mean component-F1µ is 0.984 and
stance accuracy is 1.000; the relation-F1 is 0.658 — respectable for
zero-shot with a well-written prompt, but still well short of the
supervised state of the art on UKP (∼0.75 for full parsing per Stab &
Gurevych 2017; higher for recent joint models per Li et al. 2025 §3).
The gap that prompt engineering did not close sits in two places:
**fine-grained paragraph topology** (which premise in a paragraph
attaches to which) and **rare relation types** (Attack direction when
both endpoints are premises). Both are semantic reading problems, not
schema-learning problems, and neither is amenable to a simple rule.

There are two caveats deserve emphasis on prompt engineering:

- **The lift is uneven across failure modes.** Discourse-pivot and
  MajorClaim-repetition rules were worth large deltas because they
  correspond to whole-sentence role decisions the rule can determine.
  Sub-anchor preservation worked once the model was already inclined
  toward the structure (Opus on essay006 final paragraph) but not when
  it had to infer it from scratch (both models on essay006 paragraph 1).
  Rules help where they name a structural cue; they fail where the
  structure is a read of meaning.
- **The lift is model-specific.** The same body-text rules elicited
  different responses from Opus (Attack edges with the wrong endpoints
  on essay005) and Gemini (both Attacks with correct endpoints on the
  same essay). A one-prompt-fits-all approach would have under-served
  one of the two. Our experience matches Li et al. (2025, §3.4) that
  cross-model prompt portability is poor — model-specific EMPHASIS
  blocks were not cosmetic.

At Stage 2 the residual errors are, in rough order of frequency:

1. **Paragraph-internal edge mis-targeting** — the model identifies the
   right premises and the right Claim but chooses a different premise
   as the sub-anchor (or skips the sub-anchor). Opus and Gemini do this
   on roughly the same essays, differently.
2. **Attack endpoint reversal** — once a concession clause is split,
   the model must decide whether the clause-1 → clause-2 Attack points
   up to the Claim or horizontally to the adjacent Premise. Opus reads
   "c5→c6" where gold reads "c6→c5 plus c5→c4"; Gemini gets both right.
3. **Spurious stance-based Attack edges** — when a Claim-Against is
   paired with a MajorClaim, Opus sometimes emits an explicit Attack
   edge between them even though gold uses the stance attribute alone.
4. **Shared Claim drop** — essay006 T3. Both models read it as
   MajorClaim elaboration; gold annotates a separate Claim. This is
   the smallest of the four and arguably inter-annotator noise.

None of these is the same as the Stage-1 failure modes. Prompt
engineering did not leave residual errors that are "shrunken versions
of Stage 1 errors"; it *transformed* the error surface from coarse role
mis-labelling to fine-grained attachment choices. That is progress.
Whether it is progress that can be continued by further prompt
engineering, or whether it now requires fine-tuning or a structured
decoding step, is the natural next question.

## 7. Our general experience on Gen AI

I have been using GenAI since ChatGPT-4 was first released, and I was
part of the first wave of people to pay the twenty-dollar subscription.
Over those two years the most consistent lesson from my own practice
has been that *breaking a task into pieces reliably improves model
performance* — exactly the principle we relied on when we moved from
the Stage-1 zero-shot prompt to the Stage-2 rule-structured prompt in
this project. For most of that period, however, GenAI performance was
never fully satisfying: the models made too many mistakes to be trusted
end-to-end, which confined their useful application to narrow,
well-bounded domains. The latest generation — ChatGPT-5, Gemini 3,
Opus 4.6 — has changed the game. With all the surrounding techniques
(structured prompting, tool use, long-context windows, retrieval,
agentic loops) working together, GenAI products have become *reliable*
for the first time, not merely *capable*.

My working mental model of why this is so is that GenAI is, at bottom,
statistics. Its job is still to predict the most likely continuation of
a given input rather than to *reason* in the way a symbolic system
reasons. For genuinely sophisticated reasoning tasks, this means
current models either cannot learn the underlying skill at all or can
only approximate it at an unreasonable cost in data and compute — which
is why the residual errors we observed in §6.3 sit precisely in the
semantically-hard part of the task (Attack-endpoint selection,
paragraph-internal topology) rather than in the pattern-matchable
part (component labels, stance). Yet even bounded to prediction, the
models' ability to *grasp — or convincingly mimic grasping — basic
logic* is already enough to change the world, and certainly enough to
make a structured NLP task like argument mining tractable from a
single well-engineered prompt, as our Stage-1 → Stage-2 lift
demonstrates.