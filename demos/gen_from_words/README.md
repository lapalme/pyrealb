# Generation from a list of words

This *pyrealb* demo was prompted by  

> Garcia-Méndez *et, al.*  "A Library for Automatic Natural Language Generation of Spanish Texts", 
> Expert Systems with Applications, 120, 372-386
> https://doi.org/10.48550/arXiv.2405.17280. 

This paper describe a system which generates short Spanish sentences from a set of *meaningful* words (nouns, verbs and adjectives) using a mixture of grammatical patterns and statistical  language information for determining prepositions. They then performed extensive evaluation of their system.

We decided to port this type of input to *pyrealb* to generate well-formed English and French sentences from list of words given in their base form. As we did not want to rely on a language model, the preposition must also be specified in the input. A word that should be set to plural is suffixed by a `+`. A negative or interrogative sentence can be obtained by adding `-` or `?`  (both can be given) as a last token.

The following table gives English and French examples of input with the corresponding generated sentences.

| Input                            | Generated sentence by *pyrealb*             |
| -------------------------------- | ------------------------------------------- |
| cat, sleep, in, basket           | The cat sleeps in the basket.               |
| dog+, climb, to, tree, -         | Dogs do not climb to a tree.                |
| loup, frapper, à, porte          | Le loup frappe à la porte.                  |
| garçon, nager, dans, rivière, -? | Le garçon ne nage-t-il pas dans la rivière? |

The generated sentences are very simple SVO pattern with randomly chosen determiners (definite or indefinite). This demo illustrates the incremental building of noun phrases and their combination into coordinate phrases. The same algorithm is used for both English and French only differing in a few terminal symbols.

When a token is read, it is looked into the lexicon to find its part of speech (e.g. noun, adjective, verb, etc.) tag (POS). If a token can take many POS (e.g. both a noun and an adjective, which happens quite often especially in English),  heuristics based on its position and on previous POS are used to choose a single POS. This creates three lists of `Terminal`s : subject, verb and object (SVO).

It is also possible to force a specific POS by suffixing the word with an underline followed by the POS as shown in the next table. In the first example, `blue` is *guessed* as a noun and `ball` as a verb which is coordinated with the verb `be`. In the second example, `blue_A` is forced to be an adjective, while `ball_N` is specified as a noun which results in the expected sentence.

| Input                         | Generated sentence by *pyrealb*     |
| ----------------------------- | ----------------------------------- |
| blue, ball, be, on, beach     | The blue balls and is on the beach. |
| blue_A, ball_N, be, on, beach | A blue ball is on the beach.        |

Both subject and object `Terminal` lists are then combined into one or more `NP`s. If there are more than one, a coordinate sentence is created. A single verb is embedded in a VP with its complements. If there are more than one verb, they are combined into a coordinate phrase with the complement inserted in the last VP. 

There are two lists of words (`English-words.txt` and `French-words.txt`) that are read by `gen_from_words.py`.

[Guy Lapalme](mailto:lapalme@iro.umontreal,ca), june 2024









































 