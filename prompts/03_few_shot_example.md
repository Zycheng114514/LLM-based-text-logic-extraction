# One-shot example for the refined prompt

Source: UKP essay001 (TRAIN split — safe to use as demonstration because it is
not in our evaluation set).

Paste everything between the fences into the refined prompt at the
`<<<INSERT 03_few_shot_example.md HERE>>>` placeholder.

---

```
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
```