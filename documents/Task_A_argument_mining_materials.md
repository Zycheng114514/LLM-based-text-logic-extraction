# Task A — Argument Mining: Materials

## How this document is organized

1. **Section 1 — Source essays and gold annotations.**
   The three evaluation essays (`essay004`, `essay005`, `essay006`) appear in
   full, each followed immediately by the gold-standard `.ann` file from the
   UKP corpus that we used as the reference target. The few-shot example
   essay (`essay001`) is *not* repeated here because it is embedded inside
   Prompt 3 in Section 2.

2. **Section 2 — Prompts, in the order of the pipeline.**
   - 2.1 Stage 1 initial prompt (zero-shot).
   - 2.2 Stage 2 base prompt (the shared, model-agnostic refined prompt
     produced after Stage 1 reflection).
   - 2.3 The one-shot example (`prompts/03_few_shot_example.md`) that fills
     the `<<<INSERT 03_few_shot_example.md HERE>>>` placeholder in every
     Stage 2 prompt.
   - 2.4 Stage 2 Opus-tailored prompt (replaces 2.2 for Opus).
   - 2.5 Stage 2 Gemini-tailored prompt (replaces 2.2 for Gemini).
   The prompts are reproduced verbatim from `prompts/`. The placeholders
   `<<<PASTE FULL ESSAY TEXT HERE>>>` and
   `<<<INSERT 03_few_shot_example.md HERE>>>` are left in place — they are
   not pre-substituted with the essay text or the few-shot example, so the
   reader sees the prompt template that was actually authored.

3. **Section 3 — Model JSON responses.**
   Outputs are grouped by model (3.1 Opus, 3.2 Gemini), and within each
   model by essay. For every essay, the Stage 1 (initial) response appears
   directly above the Stage 2 (improved) response, so the Stage 1 → Stage 2
   delta for a single (model, essay) cell can be read in one downward
   scroll.

---

# Section 1 — Source essays and gold annotations

## 1.1 Essay 004

### Essay text (`data/eval/essays/essay004.txt`)

```
International tourism is now more common than ever before

The last 50 years have seen a significant increase in the number of tourist traveling worldwide. While some might think the tourism bring large profit for the destination countries, I would contend that this industry has affected the cultural attributes and damaged the natural environment of the tourist destinations.
Firstly, it is an undeniable fact that tourists from different cultures will probably cause changes to the cultural identity of the tourist destinations. Take Thailand for example, in the Vietnam War, many American soldiers came to Thailand for a break and involved in sexual and drug activities, these huge demands caused many local businesses opened and expanded, even illegally involved in under-age prostitutes to maximize their profits. This was due to the lack of adequate controls by authorities and lead to a bad image of Thailand tourism. Therefore this proves that international tourism can create negative impacts on the destination countries.
Secondly, there are clear evidences that tourism increasingly create harms to the natural habitats of the destination appeals. As the Australia's Great Barrier Reef has shown, the billion visitors per annum has generated immense destruction to this nature wonder, namely breaking the corals caused by walking or throwing boat's anchors, dropping fuel and other sorts of pollutions. For this reason, many marine lives have been endangered, in the extremes part of the reef become uninhabitable for these marine species. Thus, it is apparent that tourism has threatened the nature environments.
To conclude, I strongly believe that the tourism has created threatening pressure on both the sociocultural and natural environments. If authorities do not take steps to appropriately conserve these precious values, they will be destroyed in the near future.
```

### Gold annotation (`data/eval/gold/essay004.ann`)

```
T1	MajorClaim 262 376	this industry has affected the cultural attributes and damaged the natural environment of the tourist destinations
T2	MajorClaim 1663 1758	the tourism has created threatening pressure on both the sociocultural and natural environments
T3	Claim 179 239	the tourism bring large profit for the destination countries
A1	Stance T3 Against
T4	Claim 953 1031	international tourism can create negative impacts on the destination countries
A2	Stance T4 For
T5	Claim 1578 1624	tourism has threatened the nature environments
A3	Stance T5 For
T6	Premise 417 530	tourists from different cultures will probably cause changes to the cultural identity of the tourist destinations
T7	Premise 532 818	Take Thailand for example, in the Vietnam War, many American soldiers came to Thailand for a break and involved in sexual and drug activities, these huge demands caused many local businesses opened and expanded, even illegally involved in under-age prostitutes to maximize their profits
T8	Premise 820 924	This was due to the lack of adequate controls by authorities and lead to a bad image of Thailand tourism
T9	Premise 1074 1158	tourism increasingly create harms to the natural habitats of the destination appeals
T10	Premise 1160 1413	As the Australia's Great Barrier Reef has shown, the billion visitors per annum has generated immense destruction to this nature wonder, namely breaking the corals caused by walking or throwing boat's anchors, dropping fuel and other sorts of pollutions
T11	Premise 1432 1550	many marine lives have been endangered, in the extremes part of the reef become uninhabitable for these marine species
R1	supports Arg1:T8 Arg2:T4	
R2	supports Arg1:T7 Arg2:T4	
R3	supports Arg1:T6 Arg2:T4	
R4	supports Arg1:T10 Arg2:T11	
R5	supports Arg1:T9 Arg2:T5	
R6	supports Arg1:T11 Arg2:T5	
```

## 1.2 Essay 005

### Essay text (`data/eval/essays/essay005.txt`)

```
Living and studying overseas

It is every student's desire to study at a good university and experience a new environment. While some students study and live overseas to achieve this, some prefer to study home because of the difficulties of living and studying overseas. In my opinion, one who studies overseas will gain many skills throughout this experience for several reasons.
First, studying at an overseas university gives individuals the opportunity to improve social skills by interacting and communicating with students from different origins and cultures. Compared to the peers studying in the home country, it will be more likely for the one who is living overseas to be successful in adapting himself/herself into new environments and situations in life.
Second, living and studying overseas is an irreplaceable experience when it comes to learn standing on your own feet. One who is living overseas will of course struggle with loneliness, living away from family and friends but those difficulties will turn into valuable experiences in the following steps of life. Moreover, the one will learn living without depending on anyone else.
Also, employers are mostly looking for people who have international and language skills. Becoming successful in this study will give the student an edge in job market. Therefore, one who has studied and lived overseas will become more eligible for the job than his/her peers.
In conclusion, there are many difficulties a student might face when studying and living overseas. However, living and studying overseas gives the individual a new perspective on the subject that is studied or in general life.
```

### Gold annotation (`data/eval/gold/essay005.ann`)

```
T1	MajorClaim 286 359	one who studies overseas will gain many skills throughout this experience
T2	MajorClaim 1535 1652	living and studying overseas gives the individual a new perspective on the subject that is studied or in general life
T3	Claim 388 564	studying at an overseas university gives individuals the opportunity to improve social skills by interacting and communicating with students from different origins and cultures
A1	Stance T3 For
T4	Claim 775 883	living and studying overseas is an irreplaceable experience when it comes to learn standing on your own feet
A2	Stance T4 For
T5	Claim 1330 1425	one who has studied and lived overseas will become more eligible for the job than his/her peers
A3	Stance T5 For
T6	Premise 566 765	Compared to the peers studying in the home country, it will be more likely for the one who is living overseas to be successful in adapting himself/herself into new environments and situations in life
T7	Premise 885 988	One who is living overseas will of course struggle with loneliness, living away from family and friends
T8	Premise 993 1078	those difficulties will turn into valuable experiences in the following steps of life
T9	Premise 1090 1148	the one will learn living without depending on anyone else
T10	Premise 1156 1238	employers are mostly looking for people who have international and language skills
T11	Premise 1240 1317	Becoming successful in this study will give the student an edge in job market
R1	supports Arg1:T6 Arg2:T3	
R2	attacks Arg1:T7 Arg2:T4	
R3	attacks Arg1:T8 Arg2:T7	
R4	supports Arg1:T9 Arg2:T4	
R5	supports Arg1:T10 Arg2:T5	
R6	supports Arg1:T11 Arg2:T5	
T12	Claim 1442 1524	there are many difficulties a student might face when studying and living overseas
A4	Stance T12 Against
```

## 1.3 Essay 006

### Essay text (`data/eval/essays/essay006.txt`)

```
Studies abroad and the cultural aspect of the experience

Studying abroad is one very common thing that students do, and they have different reasons for that. I believe that studying abroad has many advantages. Students gain a lot out of the experience personally, academically, and culturally.
First of all, students who study outside their countries can get a lot of experience living in a foreign country. Living in a new country requires a great amount of flexibility and adaptability in one's character. For example, students might face many challenges in the host country. Therefore, they should be able to deal with the obstacles that they may encounter. Overcoming problems teaches the students how to be more mature and self-independence. 
One other important factor is the new academic experience that the students can obtain at the institution where they are pursuing their studies. For example, they will get exposed to a different educational system. They will meet new professors and new classmates which makes the academic experience different from that in their home country.
Most important is the cultural aspect of the experience. While living in a foreign country, students can learn a lot about the culture of that country. Furthermore, they can meet different people of the country. They can learn about their way of thinking, their customs and traditions, and way of life. Learning about others' cultures is so important. It contributes in building a new understanding in us of how we see the world. It makes us more open, and willing to accept different ideas and thoughts. Also it educates us about the world we are living in. 
In conclusion, studying abroad does not only have advantages, but also can change us in a very positive way. It can influence us in different aspects of life.
```

### Gold annotation (`data/eval/gold/essay006.ann`)

```
T1	MajorClaim 174 209	studying abroad has many advantages
T2	MajorClaim 1667 1759	studying abroad does not only have advantages, but also can change us in a very positive way
T3	Claim 211 293	Students gain a lot out of the experience personally, academically, and culturally
A1	Stance T3 For
T4	Claim 309 407	students who study outside their countries can get a lot of experience living in a foreign country
A2	Stance T4 For
T5	Claim 779 892	the new academic experience that the students can obtain at the institution where they are pursuing their studies
A3	Stance T5 For
T6	Claim 1092 1147	Most important is the cultural aspect of the experience
A4	Stance T6 For
T7	Premise 409 507	Living in a new country requires a great amount of flexibility and adaptability in one's character
T8	Premise 522 577	students might face many challenges in the host country
T9	Premise 590 660	they should be able to deal with the obstacles that they may encounter
T10	Premise 662 746	Overcoming problems teaches the students how to be more mature and self-independence
T11	Premise 907 962	they will get exposed to a different educational system
T12	Premise 964 1090	They will meet new professors and new classmates which makes the academic experience different from that in their home country
T13	Premise 1149 1242	While living in a foreign country, students can learn a lot about the culture of that country
T14	Premise 1257 1302	they can meet different people of the country
T15	Premise 1304 1393	They can learn about their way of thinking, their customs and traditions, and way of life
T16	Premise 1395 1442	Learning about others' cultures is so important
T17	Premise 1444 1520	It contributes in building a new understanding in us of how we see the world
T18	Premise 1522 1595	It makes us more open, and willing to accept different ideas and thoughts
T19	Premise 1602 1649	it educates us about the world we are living in
R1	supports Arg1:T7 Arg2:T4	
R2	supports Arg1:T8 Arg2:T9	
R3	supports Arg1:T10 Arg2:T9	
R4	supports Arg1:T9 Arg2:T4	
R5	supports Arg1:T11 Arg2:T5	
R6	supports Arg1:T12 Arg2:T5	
R7	supports Arg1:T13 Arg2:T6	
R8	supports Arg1:T14 Arg2:T6	
R9	supports Arg1:T15 Arg2:T6	
R10	supports Arg1:T16 Arg2:T6	
R11	supports Arg1:T17 Arg2:T16	
R12	supports Arg1:T18 Arg2:T16	
R13	supports Arg1:T19 Arg2:T16	
```

---

# Section 2 — Prompts (in pipeline order)

## 2.1 Stage 1 — Initial (zero-shot) prompt

Source file: `prompts/01_initial_prompt.md`.

````
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
````

## 2.2 Stage 2 — Refined (base) prompt 
### We didn't run this base prompt but run model specific prompts in stage 2

Source file: `prompts/02_refined_prompt.md`. This is the model-agnostic
refined prompt produced after the Stage 1 reflection. For the actual Stage 2
runs it was specialized into the Opus and Gemini variants in 2.4 and 2.5
below; both of those variants share the body of this base prompt and only
add a final `MODEL-SPECIFIC EMPHASIS` block.

````
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
````

## 2.3 One-shot example (fills the `<<<INSERT 03_few_shot_example.md HERE>>>` placeholder)

Source file: `prompts/03_few_shot_example.md`. The example essay is UKP
`essay001` from the TRAIN split — disjoint from our three evaluation essays.

````
EXAMPLE ESSAY:

Should students be taught to compete or to cooperate?

It is always said that competition can effectively promote the development of
economy. In order to survive in the competition, companies continue to improve
their products and service, and as a result, the whole society prospers.
However, when we discuss the issue of competition or cooperation, what we are
concerned about is not the whole society, but the development of an
individual's whole life. From this point of view, I firmly believe that we
should attach more importance to cooperation during primary education.

First of all, through cooperation, children can learn about interpersonal
skills which are significant in the future life of all students. What we
acquired from team work is not only how to achieve the same goal with others
but more importantly, how to get along with others. During the process of
cooperation, children can learn about how to listen to opinions of others, how
to communicate with others, how to think comprehensively, and even how to
compromise with other team members when conflicts occurred. All of these
skills help them to get on well with other people and will benefit them for
the whole life.

On the other hand, the significance of competition is that how to become more
excellence to gain the victory. Hence it is always said that competition makes
the society more effective. However, when we consider about the question that
how to win the game, we always find that we need the cooperation. The greater
our goal is, the more competition we need. Take Olympic games which is a form
of competition for instance, it is hard to imagine how an athlete could win
the game without the training of his or her coach, and the help of other
professional staffs such as the people who take care of his diet, and those
who are in charge of the medical care. The winner is the athlete but the
success belongs to the whole team. Therefore without the cooperation, there
would be no victory of competition.

Consequently, no matter from the view of individual development or the
relationship between competition and cooperation we can receive the same
conclusion that a more cooperative attitudes towards life is more profitable
in one's success.

EXPECTED OUTPUT (gold):

{
  "components": [
    {"id": "c1",  "type": "MajorClaim", "text": "we should attach more importance to cooperation during primary education"},
    {"id": "c2",  "type": "Claim", "stance": "For",     "text": "through cooperation, children can learn about interpersonal skills which are significant in the future life of all students"},
    {"id": "c3",  "type": "Premise",                    "text": "What we acquired from team work is not only how to achieve the same goal with others but more importantly, how to get along with others"},
    {"id": "c4",  "type": "Premise",                    "text": "During the process of cooperation, children can learn about how to listen to opinions of others, how to communicate with others, how to think comprehensively, and even how to compromise with other team members when conflicts occurred"},
    {"id": "c5",  "type": "Premise",                    "text": "All of these skills help them to get on well with other people and will benefit them for the whole life"},
    {"id": "c6",  "type": "Claim", "stance": "Against", "text": "competition makes the society more effective"},
    {"id": "c7",  "type": "Premise",                    "text": "the significance of competition is that how to become more excellence to gain the victory"},
    {"id": "c8",  "type": "Premise",                    "text": "when we consider about the question that how to win the game, we always find that we need the cooperation"},
    {"id": "c9",  "type": "Premise",                    "text": "Take Olympic games which is a form of competition for instance, it is hard to imagine how an athlete could win the game without the training of his or her coach, and the help of other professional staffs such as the people who take care of his diet, and those who are in charge of the medical care"},
    {"id": "c10", "type": "Claim", "stance": "For",     "text": "without the cooperation, there would be no victory of competition"},
    {"id": "c11", "type": "MajorClaim", "text": "a more cooperative attitudes towards life is more profitable in one's success"}
  ],
  "relations": [
    {"src": "c3",  "tgt": "c2",  "type": "Support"},
    {"src": "c4",  "tgt": "c2",  "type": "Support"},
    {"src": "c5",  "tgt": "c2",  "type": "Support"},
    {"src": "c7",  "tgt": "c6",  "type": "Support"},
    {"src": "c8",  "tgt": "c10", "type": "Support"},
    {"src": "c9",  "tgt": "c10", "type": "Support"}
  ]
}
````

## 2.4 Stage 2 — Refined prompt (Opus tailored)

Source file: `prompts/02_refined_prompt_opus.md`. Submitted to Opus for the
three Stage 2 Opus runs.

````
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
````

## 2.5 Stage 2 — Refined prompt (Gemini tailored)

Source file: `prompts/02_refined_prompt_gemini.md`. Submitted to Gemini for
the three Stage 2 Gemini runs. Identical to 2.4 except for the final
`MODEL-SPECIFIC EMPHASIS` block.

````
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

=== MODEL-SPECIFIC EMPHASIS (Gemini) ===

Your Stage 1 behaviour on these essays had two strengths and two weaknesses
that deserve explicit calibration:

(a) STRENGTHS TO PRESERVE.
    - You correctly identified an Attack relation on one essay at Stage 1
      (struggling with loneliness attacking "irreplaceable experience").
      Keep this behaviour. Do NOT let the Support-only shape of the worked
      example above override what the text itself shows — if a premise
      rebuts the target, mark it Attack. Re-read rule (2) and the Attack
      definition in the RELATIONS section before emitting any edge that
      involves a concession clause.
    - You correctly identified a sub-anchor topology at Stage 1, routing
      three sentences through an intermediate premise rather than flattening
      them. Keep this. The worked example above is flat, but real essays
      commonly have a sub-anchor in the final body paragraph. Re-read rule
      (3) before flattening.

(b) WEAKNESSES TO CORRECT.
    - In Stage 1 you sometimes promoted the final closing sentence
      ("It can influence us in many aspects of life") to a separate Claim.
      Rule (5) above says this is a continuation of the preceding MajorClaim,
      not a new component. Do not emit it as a separate span.
    - On one essay you gave the second MajorClaim slot the same id
      ambiguity. When the introduction and conclusion state the same
      position, emit both as MajorClaim (rule 4).

Use id prefix `c` consistently for all components (`c1, c2, …`). Do not mix
prefixes within a single output.

NOW APPLY THE SAME PROCEDURE TO THIS ESSAY:
<<<PASTE FULL ESSAY TEXT HERE>>>
````

---

# Section 3 — Model JSON responses (Stage 1 → Stage 2 paired by essay)

## 3.1 Opus (Claude Opus 4.7)

### 3.1.1 Essay 004 — Opus

**Stage 1 (initial response, `runs/stage1/opus/essay004.json`):**

```json
{"components":[
  {"id":"T1","type":"MajorClaim","text":"this industry has affected the cultural attributes and damaged the natural environment of the tourist destinations"},
  {"id":"T2","type":"MajorClaim","text":"the tourism has created threatening pressure on both the sociocultural and natural environments"},
  {"id":"T3","type":"Claim","stance":"For","text":"it is an undeniable fact that tourists from different cultures will probably cause changes to the cultural identity of the tourist destinations"},
  {"id":"T4","type":"Premise","text":"in the Vietnam War, many American soldiers came to Thailand for a break and involved in sexual and drug activities, these huge demands caused many local businesses opened and expanded, even illegally involved in under-age prostitutes to maximize their profits"},
  {"id":"T5","type":"Premise","text":"This was due to the lack of adequate controls by authorities and lead to a bad image of Thailand tourism"},
  {"id":"T6","type":"Premise","text":"international tourism can create negative impacts on the destination countries"},
  {"id":"T7","type":"Claim","stance":"For","text":"there are clear evidences that tourism increasingly create harms to the natural habitats of the destination appeals"},
  {"id":"T8","type":"Premise","text":"the billion visitors per annum has generated immense destruction to this nature wonder, namely breaking the corals caused by walking or throwing boat's anchors, dropping fuel and other sorts of pollutions"},
  {"id":"T9","type":"Premise","text":"many marine lives have been endangered, in the extremes part of the reef become uninhabitable for these marine species"},
  {"id":"T10","type":"Premise","text":"it is apparent that tourism has threatened the nature environments"},
  {"id":"T11","type":"Claim","stance":"Against","text":"the tourism bring large profit for the destination countries"}],
 "relations":[
  {"src":"T4","tgt":"T3","type":"Support"},
  {"src":"T5","tgt":"T3","type":"Support"},
  {"src":"T6","tgt":"T3","type":"Support"},
  {"src":"T8","tgt":"T7","type":"Support"},
  {"src":"T9","tgt":"T7","type":"Support"},
  {"src":"T10","tgt":"T7","type":"Support"}]}
```

**Stage 2 (improved response, `runs/stage2/opus/essay004.json`):**

```json
{
  "components": [
    {"id": "c1", "type": "MajorClaim", "text": "this industry has affected the cultural attributes and damaged the natural environment of the tourist destinations"},
    {"id": "c2", "type": "Claim", "stance": "Against", "text": "the tourism bring large profit for the destination countries"},
    {"id": "c3", "type": "Premise", "text": "tourists from different cultures will probably cause changes to the cultural identity of the tourist destinations"},
    {"id": "c4", "type": "Premise", "text": "in the Vietnam War, many American soldiers came to Thailand for a break and involved in sexual and drug activities, these huge demands caused many local businesses opened and expanded, even illegally involved in under-age prostitutes to maximize their profits"},
    {"id": "c5", "type": "Premise", "text": "This was due to the lack of adequate controls by authorities and lead to a bad image of Thailand tourism"},
    {"id": "c6", "type": "Claim", "stance": "For", "text": "international tourism can create negative impacts on the destination countries"},
    {"id": "c7", "type": "Premise", "text": "tourism increasingly create harms to the natural habitats of the destination appeals"},
    {"id": "c8", "type": "Premise", "text": "the billion visitors per annum has generated immense destruction to this nature wonder, namely breaking the corals caused by walking or throwing boat's anchors, dropping fuel and other sorts of pollutions"},
    {"id": "c9", "type": "Premise", "text": "many marine lives have been endangered, in the extremes part of the reef become uninhabitable for these marine species"},
    {"id": "c10", "type": "Claim", "stance": "For", "text": "tourism has threatened the nature environments"},
    {"id": "c11", "type": "MajorClaim", "text": "the tourism has created threatening pressure on both the sociocultural and natural environments"},
    {"id": "c12", "type": "Premise", "text": "If authorities do not take steps to appropriately conserve these precious values, they will be destroyed in the near future"}
  ],
  "relations": [
    {"src": "c3", "tgt": "c6", "type": "Support"},
    {"src": "c4", "tgt": "c6", "type": "Support"},
    {"src": "c5", "tgt": "c4", "type": "Support"},
    {"src": "c7", "tgt": "c10", "type": "Support"},
    {"src": "c8", "tgt": "c10", "type": "Support"},
    {"src": "c9", "tgt": "c8", "type": "Support"},
    {"src": "c12", "tgt": "c11", "type": "Support"}
  ]
}
```

### 3.1.2 Essay 005 — Opus

**Stage 1 (initial response, `runs/stage1/opus/essay005.json`):**

```json
{"components":[
  {"id":"T1","type":"MajorClaim","text":"one who studies overseas will gain many skills throughout this experience for several reasons"},
  {"id":"T2","type":"MajorClaim","text":"living and studying overseas gives the individual a new perspective on the subject that is studied or in general life"},
  {"id":"T3","type":"Claim","stance":"For","text":"studying at an overseas university gives individuals the opportunity to improve social skills by interacting and communicating with students from different origins and cultures"},
  {"id":"T4","type":"Premise","text":"Compared to the peers studying in the home country, it will be more likely for the one who is living overseas to be successful in adapting himself/herself into new environments and situations in life"},
  {"id":"T5","type":"Claim","stance":"For","text":"living and studying overseas is an irreplaceable experience when it comes to learn standing on your own feet"},
  {"id":"T6","type":"Premise","text":"One who is living overseas will of course struggle with loneliness, living away from family and friends but those difficulties will turn into valuable experiences in the following steps of life"},
  {"id":"T7","type":"Premise","text":"the one will learn living without depending on anyone else"},
  {"id":"T8","type":"Premise","text":"employers are mostly looking for people who have international and language skills"},
  {"id":"T9","type":"Premise","text":"Becoming successful in this study will give the student an edge in job market"},
  {"id":"T10","type":"Claim","stance":"For","text":"one who has studied and lived overseas will become more eligible for the job than his/her peers"}],
 "relations":[
  {"src":"T4","tgt":"T3","type":"Support"},
  {"src":"T6","tgt":"T5","type":"Support"},
  {"src":"T7","tgt":"T5","type":"Support"},
  {"src":"T8","tgt":"T10","type":"Support"},
  {"src":"T9","tgt":"T10","type":"Support"}]}
```

**Stage 2 (improved response, `runs/stage2/opus/essay005.json`):**

```json
{
  "components": [
    {"id": "c1", "type": "MajorClaim", "text": "one who studies overseas will gain many skills throughout this experience"},
    {"id": "c2", "type": "Claim", "stance": "For", "text": "studying at an overseas university gives individuals the opportunity to improve social skills by interacting and communicating with students from different origins and cultures"},
    {"id": "c3", "type": "Premise", "text": "it will be more likely for the one who is living overseas to be successful in adapting himself/herself into new environments and situations in life"},
    {"id": "c4", "type": "Claim", "stance": "For", "text": "living and studying overseas is an irreplaceable experience when it comes to learn standing on your own feet"},
    {"id": "c5", "type": "Premise", "text": "One who is living overseas will of course struggle with loneliness, living away from family and friends"},
    {"id": "c6", "type": "Premise", "text": "those difficulties will turn into valuable experiences in the following steps of life"},
    {"id": "c7", "type": "Premise", "text": "the one will learn living without depending on anyone else"},
    {"id": "c8", "type": "Premise", "text": "employers are mostly looking for people who have international and language skills"},
    {"id": "c9", "type": "Premise", "text": "Becoming successful in this study will give the student an edge in job market"},
    {"id": "c10", "type": "Claim", "stance": "For", "text": "one who has studied and lived overseas will become more eligible for the job than his/her peers"},
    {"id": "c11", "type": "Claim", "stance": "Against", "text": "there are many difficulties a student might face when studying and living overseas"},
    {"id": "c12", "type": "MajorClaim", "text": "living and studying overseas gives the individual a new perspective on the subject that is studied or in general life"}
  ],
  "relations": [
    {"src": "c3", "tgt": "c2", "type": "Support"},
    {"src": "c5", "tgt": "c6", "type": "Attack"},
    {"src": "c6", "tgt": "c4", "type": "Support"},
    {"src": "c7", "tgt": "c4", "type": "Support"},
    {"src": "c8", "tgt": "c10", "type": "Support"},
    {"src": "c9", "tgt": "c10", "type": "Support"},
    {"src": "c11", "tgt": "c12", "type": "Attack"}
  ]
}
```

### 3.1.3 Essay 006 — Opus

**Stage 1 (initial response, `runs/stage1/opus/essay006.json`):**

```json
{"components":[
  {"id":"T1","type":"MajorClaim","text":"studying abroad has many advantages"},
  {"id":"T2","type":"MajorClaim","text":"Students gain a lot out of the experience personally, academically, and culturally"},
  {"id":"T3","type":"Claim","stance":"For","text":"students who study outside their countries can get a lot of experience living in a foreign country"},
  {"id":"T4","type":"Premise","text":"Living in a new country requires a great amount of flexibility and adaptability in one's character"},
  {"id":"T5","type":"Premise","text":"students might face many challenges in the host country"},
  {"id":"T6","type":"Premise","text":"they should be able to deal with the obstacles that they may encounter"},
  {"id":"T7","type":"Premise","text":"Overcoming problems teaches the students how to be more mature and self-independence"},
  {"id":"T8","type":"Claim","stance":"For","text":"One other important factor is the new academic experience that the students can obtain at the institution where they are pursuing their studies"},
  {"id":"T9","type":"Premise","text":"they will get exposed to a different educational system"},
  {"id":"T10","type":"Premise","text":"They will meet new professors and new classmates which makes the academic experience different from that in their home country"},
  {"id":"T11","type":"Claim","stance":"For","text":"Most important is the cultural aspect of the experience"},
  {"id":"T12","type":"Premise","text":"While living in a foreign country, students can learn a lot about the culture of that country"},
  {"id":"T13","type":"Premise","text":"they can meet different people of the country"},
  {"id":"T14","type":"Premise","text":"They can learn about their way of thinking, their customs and traditions, and way of life"},
  {"id":"T15","type":"Premise","text":"Learning about others' cultures is so important"},
  {"id":"T16","type":"Premise","text":"It contributes in building a new understanding in us of how we see the world"},
  {"id":"T17","type":"Premise","text":"It makes us more open, and willing to accept different ideas and thoughts"},
  {"id":"T18","type":"Premise","text":"it educates us about the world we are living in"}],
 "relations":[
  {"src":"T4","tgt":"T3","type":"Support"},
  {"src":"T5","tgt":"T3","type":"Support"},
  {"src":"T6","tgt":"T3","type":"Support"},
  {"src":"T7","tgt":"T3","type":"Support"},
  {"src":"T9","tgt":"T8","type":"Support"},
  {"src":"T10","tgt":"T8","type":"Support"},
  {"src":"T12","tgt":"T11","type":"Support"},
  {"src":"T13","tgt":"T11","type":"Support"},
  {"src":"T14","tgt":"T11","type":"Support"},
  {"src":"T15","tgt":"T11","type":"Support"},
  {"src":"T16","tgt":"T11","type":"Support"},
  {"src":"T17","tgt":"T11","type":"Support"},
  {"src":"T18","tgt":"T11","type":"Support"}]}
```

**Stage 2 (improved response, `runs/stage2/opus/essay006.json`):**

```json
{
  "components": [
    {"id": "c1", "type": "MajorClaim", "text": "studying abroad has many advantages"},
    {"id": "c2", "type": "Claim", "stance": "For", "text": "students who study outside their countries can get a lot of experience living in a foreign country"},
    {"id": "c3", "type": "Premise", "text": "Living in a new country requires a great amount of flexibility and adaptability in one's character"},
    {"id": "c4", "type": "Premise", "text": "students might face many challenges in the host country"},
    {"id": "c5", "type": "Premise", "text": "they should be able to deal with the obstacles that they may encounter"},
    {"id": "c6", "type": "Premise", "text": "Overcoming problems teaches the students how to be more mature and self-independence"},
    {"id": "c7", "type": "Claim", "stance": "For", "text": "the new academic experience that the students can obtain at the institution where they are pursuing their studies"},
    {"id": "c8", "type": "Premise", "text": "they will get exposed to a different educational system"},
    {"id": "c9", "type": "Premise", "text": "They will meet new professors and new classmates which makes the academic experience different from that in their home country"},
    {"id": "c10", "type": "Claim", "stance": "For", "text": "Most important is the cultural aspect of the experience"},
    {"id": "c11", "type": "Premise", "text": "While living in a foreign country, students can learn a lot about the culture of that country"},
    {"id": "c12", "type": "Premise", "text": "they can meet different people of the country"},
    {"id": "c13", "type": "Premise", "text": "They can learn about their way of thinking, their customs and traditions, and way of life"},
    {"id": "c14", "type": "Premise", "text": "Learning about others' cultures is so important"},
    {"id": "c15", "type": "Premise", "text": "It contributes in building a new understanding in us of how we see the world"},
    {"id": "c16", "type": "Premise", "text": "It makes us more open, and willing to accept different ideas and thoughts"},
    {"id": "c17", "type": "Premise", "text": "it educates us about the world we are living in"},
    {"id": "c18", "type": "MajorClaim", "text": "studying abroad does not only have advantages, but also can change us in a very positive way"}
  ],
  "relations": [
    {"src": "c3", "tgt": "c2", "type": "Support"},
    {"src": "c4", "tgt": "c2", "type": "Support"},
    {"src": "c5", "tgt": "c2", "type": "Support"},
    {"src": "c6", "tgt": "c2", "type": "Support"},
    {"src": "c8", "tgt": "c7", "type": "Support"},
    {"src": "c9", "tgt": "c7", "type": "Support"},
    {"src": "c11", "tgt": "c10", "type": "Support"},
    {"src": "c12", "tgt": "c10", "type": "Support"},
    {"src": "c13", "tgt": "c10", "type": "Support"},
    {"src": "c14", "tgt": "c10", "type": "Support"},
    {"src": "c15", "tgt": "c14", "type": "Support"},
    {"src": "c16", "tgt": "c14", "type": "Support"},
    {"src": "c17", "tgt": "c14", "type": "Support"}
  ]
}
```

## 3.2 Gemini (Gemini 3.1 Pro)

### 3.2.1 Essay 004 — Gemini

**Stage 1 (initial response, `runs/stage1/gemini/essay004.json`):**

```json
{"components":[
  {"id":"c1","type":"MajorClaim","text":"this industry has affected the cultural attributes and damaged the natural environment of the tourist destinations"},
  {"id":"c2","type":"Claim","stance":"Against","text":"the tourism bring large profit for the destination countries"},
  {"id":"c3","type":"Claim","stance":"For","text":"tourists from different cultures will probably cause changes to the cultural identity of the tourist destinations"},
  {"id":"c4","type":"Premise","text":"Take Thailand for example, in the Vietnam War, many American soldiers came to Thailand for a break and involved in sexual and drug activities, these huge demands caused many local businesses opened and expanded, even illegally involved in under-age prostitutes to maximize their profits"},
  {"id":"c5","type":"Premise","text":"This was due to the lack of adequate controls by authorities and lead to a bad image of Thailand tourism"},
  {"id":"c6","type":"Premise","text":"international tourism can create negative impacts on the destination countries"},
  {"id":"c7","type":"Claim","stance":"For","text":"tourism increasingly create harms to the natural habitats of the destination appeals"},
  {"id":"c8","type":"Premise","text":"As the Australia's Great Barrier Reef has shown, the billion visitors per annum has generated immense destruction to this nature wonder, namely breaking the corals caused by walking or throwing boat's anchors, dropping fuel and other sorts of pollutions"},
  {"id":"c9","type":"Premise","text":"many marine lives have been endangered, in the extremes part of the reef become uninhabitable for these marine species"},
  {"id":"c10","type":"Premise","text":"tourism has threatened the nature environments"},
  {"id":"c11","type":"MajorClaim","text":"the tourism has created threatening pressure on both the sociocultural and natural environments"}],
 "relations":[
  {"src":"c4","tgt":"c3","type":"Support"},
  {"src":"c5","tgt":"c3","type":"Support"},
  {"src":"c6","tgt":"c3","type":"Support"},
  {"src":"c8","tgt":"c7","type":"Support"},
  {"src":"c9","tgt":"c7","type":"Support"},
  {"src":"c10","tgt":"c7","type":"Support"}]}
```

**Stage 2 (improved response, `runs/stage2/gemini/essay004.json`):**

```json
{
  "components": [
    {"id": "c1", "type": "Claim", "stance": "Against", "text": "the tourism bring large profit for the destination countries"},
    {"id": "c2", "type": "MajorClaim", "text": "this industry has affected the cultural attributes and damaged the natural environment of the tourist destinations"},
    {"id": "c3", "type": "Premise", "text": "tourists from different cultures will probably cause changes to the cultural identity of the tourist destinations"},
    {"id": "c4", "type": "Premise", "text": "in the Vietnam War, many American soldiers came to Thailand for a break and involved in sexual and drug activities, these huge demands caused many local businesses opened and expanded, even illegally involved in under-age prostitutes to maximize their profits"},
    {"id": "c5", "type": "Premise", "text": "This was due to the lack of adequate controls by authorities and lead to a bad image of Thailand tourism"},
    {"id": "c6", "type": "Claim", "stance": "For", "text": "international tourism can create negative impacts on the destination countries"},
    {"id": "c7", "type": "Premise", "text": "tourism increasingly create harms to the natural habitats of the destination appeals"},
    {"id": "c8", "type": "Premise", "text": "the billion visitors per annum has generated immense destruction to this nature wonder, namely breaking the corals caused by walking or throwing boat\u2019s anchors, dropping fuel and other sorts of pollutions"},
    {"id": "c9", "type": "Premise", "text": "many marine lives have been endangered, in the extremes part of the reef become uninhabitable for these marine species"},
    {"id": "c10", "type": "Claim", "stance": "For", "text": "tourism has threatened the nature environments"},
    {"id": "c11", "type": "MajorClaim", "text": "the tourism has created threatening pressure on both the sociocultural and natural environments"}
  ],
  "relations": [
    {"src": "c4", "tgt": "c3", "type": "Support"},
    {"src": "c5", "tgt": "c3", "type": "Support"},
    {"src": "c3", "tgt": "c6", "type": "Support"},
    {"src": "c8", "tgt": "c9", "type": "Support"},
    {"src": "c9", "tgt": "c7", "type": "Support"},
    {"src": "c7", "tgt": "c10", "type": "Support"}
  ]
}
```

### 3.2.2 Essay 005 — Gemini

**Stage 1 (initial response, `runs/stage1/gemini/essay005.json`):**

```json
{"components":[
  {"id":"T1","type":"MajorClaim","text":"one who studies overseas will gain many skills throughout this experience"},
  {"id":"T2","type":"Claim","stance":"For","text":"studying at an overseas university gives individuals the opportunity to improve social skills by interacting and communicating with students from different origins and cultures"},
  {"id":"T3","type":"Premise","text":"Compared to the peers studying in the home country, it will be more likely for the one who is living overseas to be successful in adapting himself/herself into new environments and situations in life"},
  {"id":"T4","type":"Claim","stance":"For","text":"living and studying overseas is an irreplaceable experience when it comes to learn standing on your own feet"},
  {"id":"T5","type":"Premise","text":"One who is living overseas will of course struggle with loneliness, living away from family and friends"},
  {"id":"T6","type":"Premise","text":"those difficulties will turn into valuable experiences in the following steps of life"},
  {"id":"T7","type":"Premise","text":"the one will learn living without depending on anyone else"},
  {"id":"T8","type":"Premise","text":"employers are mostly looking for people who have international and language skills"},
  {"id":"T9","type":"Premise","text":"Becoming successful in this study will give the student an edge in job market"},
  {"id":"T10","type":"Claim","stance":"For","text":"one who has studied and lived overseas will become more eligible for the job than his/her peers"},
  {"id":"T11","type":"Claim","stance":"Against","text":"there are many difficulties a student might face when studying and living overseas"},
  {"id":"T12","type":"Claim","stance":"For","text":"living and studying overseas gives the individual a new perspective on the subject that is studied or in general life"}],
 "relations":[
  {"src":"T3","tgt":"T2","type":"Support"},
  {"src":"T5","tgt":"T4","type":"Attack"},
  {"src":"T6","tgt":"T4","type":"Support"},
  {"src":"T7","tgt":"T4","type":"Support"},
  {"src":"T8","tgt":"T10","type":"Support"},
  {"src":"T9","tgt":"T10","type":"Support"}]}
```

**Stage 2 (improved response, `runs/stage2/gemini/essay005.json`):**

```json
{
  "components": [
    {"id": "c1", "type": "MajorClaim", "text": "one who studies overseas will gain many skills throughout this experience for several reasons"},
    {"id": "c2", "type": "Claim", "stance": "For", "text": "studying at an overseas university gives individuals the opportunity to improve social skills by interacting and communicating with students from different origins and cultures"},
    {"id": "c3", "type": "Premise", "text": "Compared to the peers studying in the home country, it will be more likely for the one who is living overseas to be successful in adapting himself/herself into new environments and situations in life"},
    {"id": "c4", "type": "Claim", "stance": "For", "text": "living and studying overseas is an irreplaceable experience when it comes to learn standing on your own feet"},
    {"id": "c5", "type": "Premise", "text": "One who is living overseas will of course struggle with loneliness, living away from family and friends"},
    {"id": "c6", "type": "Premise", "text": "those difficulties will turn into valuable experiences in the following steps of life"},
    {"id": "c7", "type": "Premise", "text": "the one will learn living without depending on anyone else"},
    {"id": "c8", "type": "Premise", "text": "employers are mostly looking for people who have international and language skills"},
    {"id": "c9", "type": "Premise", "text": "Becoming successful in this study will give the student an edge in job market"},
    {"id": "c10", "type": "Claim", "stance": "For", "text": "one who has studied and lived overseas will become more eligible for the job than his/her peers"},
    {"id": "c11", "type": "Claim", "stance": "Against", "text": "there are many difficulties a student might face when studying and living overseas"},
    {"id": "c12", "type": "MajorClaim", "text": "living and studying overseas gives the individual a new perspective on the subject that is studied or in general life"}
  ],
  "relations": [
    {"src": "c3", "tgt": "c2", "type": "Support"},
    {"src": "c5", "tgt": "c4", "type": "Attack"},
    {"src": "c6", "tgt": "c5", "type": "Attack"},
    {"src": "c7", "tgt": "c4", "type": "Support"},
    {"src": "c8", "tgt": "c9", "type": "Support"},
    {"src": "c9", "tgt": "c10", "type": "Support"}
  ]
}
```

### 3.2.3 Essay 006 — Gemini

**Stage 1 (initial response, `runs/stage1/gemini/essay006.json`):**

```json
{"components":[
  {"id":"T1","type":"MajorClaim","text":"studying abroad has many advantages"},
  {"id":"T2","type":"Claim","stance":"For","text":"Students gain a lot out of the experience personally, academically, and culturally."},
  {"id":"T3","type":"Claim","stance":"For","text":"students who study outside their countries can get a lot of experience living in a foreign country."},
  {"id":"T4","type":"Premise","text":"Living in a new country requires a great amount of flexibility and adaptability in one's character."},
  {"id":"T5","type":"Premise","text":"students might face many challenges in the host country."},
  {"id":"T6","type":"Premise","text":"they should be able to deal with the obstacles that they may encounter."},
  {"id":"T7","type":"Premise","text":"Overcoming problems teaches the students how to be more mature and self-independence."},
  {"id":"T8","type":"Claim","stance":"For","text":"One other important factor is the new academic experience that the students can obtain at the institution where they are pursuing their studies."},
  {"id":"T9","type":"Premise","text":"they will get exposed to a different educational system."},
  {"id":"T10","type":"Premise","text":"They will meet new professors and new classmates which makes the academic experience different from that in their home country."},
  {"id":"T11","type":"Claim","stance":"For","text":"Most important is the cultural aspect of the experience."},
  {"id":"T12","type":"Premise","text":"While living in a foreign country, students can learn a lot about the culture of that country."},
  {"id":"T13","type":"Premise","text":"Furthermore, they can meet different people of the country."},
  {"id":"T14","type":"Premise","text":"They can learn about their way of thinking, their customs and traditions, and way of life."},
  {"id":"T15","type":"Premise","text":"Learning about others' cultures is so important."},
  {"id":"T16","type":"Premise","text":"It contributes in building a new understanding in us of how we see the world."},
  {"id":"T17","type":"Premise","text":"It makes us more open, and willing to accept different ideas and thoughts."},
  {"id":"T18","type":"Premise","text":"Also it educates us about the world we are living in."},
  {"id":"T19","type":"MajorClaim","text":"studying abroad does not only have advantages, but also can change us in a very positive way."},
  {"id":"T20","type":"Claim","stance":"For","text":"It can influence us in different aserects of life."}],
 "relations":[
  {"src":"T4","tgt":"T3","type":"Support"},
  {"src":"T5","tgt":"T4","type":"Support"},
  {"src":"T6","tgt":"T4","type":"Support"},
  {"src":"T7","tgt":"T3","type":"Support"},
  {"src":"T9","tgt":"T8","type":"Support"},
  {"src":"T10","tgt":"T8","type":"Support"},
  {"src":"T12","tgt":"T11","type":"Support"},
  {"src":"T13","tgt":"T11","type":"Support"},
  {"src":"T14","tgt":"T11","type":"Support"},
  {"src":"T15","tgt":"T11","type":"Support"},
  {"src":"T16","tgt":"T15","type":"Support"},
  {"src":"T17","tgt":"T15","type":"Support"},
  {"src":"T18","tgt":"T15","type":"Support"}]}
```

**Stage 2 (improved response, `runs/stage2/gemini/essay006.json`):**

```json
{
  "components": [
    {"id": "c1", "type": "MajorClaim", "text": "studying abroad has many advantages"},
    {"id": "c2", "type": "Claim", "stance": "For", "text": "students who study outside their countries can get a lot of experience living in a foreign country"},
    {"id": "c3", "type": "Premise", "text": "Living in a new country requires a great amount of flexibility and adaptability in one's character"},
    {"id": "c4", "type": "Premise", "text": "students might face many challenges in the host country"},
    {"id": "c5", "type": "Premise", "text": "they should be able to deal with the obstacles that they may encounter"},
    {"id": "c6", "type": "Premise", "text": "Overcoming problems teaches the students how to be more mature and self-independence"},
    {"id": "c7", "type": "Claim", "stance": "For", "text": "One other important factor is the new academic experience that the students can obtain at the institution where they are pursuing their studies"},
    {"id": "c8", "type": "Premise", "text": "they will get exposed to a different educational system"},
    {"id": "c9", "type": "Premise", "text": "They will meet new professors and new classmates which makes the academic experience different from that in their home country"},
    {"id": "c10", "type": "Claim", "stance": "For", "text": "Most important is the cultural aspect of the experience"},
    {"id": "c11", "type": "Premise", "text": "While living in a foreign country, students can learn a lot about the culture of that country"},
    {"id": "c12", "type": "Premise", "text": "they can meet different people of the country"},
    {"id": "c13", "type": "Premise", "text": "They can learn about their way of thinking, their customs and traditions, and way of life"},
    {"id": "c14", "type": "Premise", "text": "Learning about others' cultures is so important"},
    {"id": "c15", "type": "Premise", "text": "It contributes in building a new understanding in us of how we see the world"},
    {"id": "c16", "type": "Premise", "text": "It makes us more open, and willing to accept different ideas and thoughts"},
    {"id": "c17", "type": "Premise", "text": "it educates us about the world we are living in"},
    {"id": "c18", "type": "MajorClaim", "text": "studying abroad does not only have advantages, but also can change us in a very positive way"}
  ],
  "relations": [
    {"src": "c3", "tgt": "c2", "type": "Support"},
    {"src": "c4", "tgt": "c3", "type": "Support"},
    {"src": "c5", "tgt": "c4", "type": "Support"},
    {"src": "c6", "tgt": "c2", "type": "Support"},
    {"src": "c8", "tgt": "c7", "type": "Support"},
    {"src": "c9", "tgt": "c7", "type": "Support"},
    {"src": "c11", "tgt": "c10", "type": "Support"},
    {"src": "c12", "tgt": "c10", "type": "Support"},
    {"src": "c13", "tgt": "c12", "type": "Support"},
    {"src": "c14", "tgt": "c10", "type": "Support"},
    {"src": "c15", "tgt": "c14", "type": "Support"},
    {"src": "c16", "tgt": "c14", "type": "Support"},
    {"src": "c17", "tgt": "c14", "type": "Support"}
  ]
}
```
