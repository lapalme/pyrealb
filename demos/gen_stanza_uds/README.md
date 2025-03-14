# Generation of English and French Universal Dependency Structures

## Context
This work was prompted by an e-mail of John Bauer, the *maintainer* of the Stanza parser, who sent me a list of French tokens (adjectives, adverbs, nouns and verbs) that are known to the Stanza parser for French. John suspected that the French lemmatization is not very good.

I started a small experiment with the 22 verbs that should be known by 75% of children at the end of their first year in school (`niveau == 1` in the *lexicon-fr.json*).  I conjugated them at 4 tenses of indicative and a few participles (29 forms for each, but some forms are the same only differing in their person: e.g "aime" can be 1st or 3rd person of present). This already created 638 forms. 

To display the results (lemma and features), I used the CONLLU format for a token with the `form`, `lemma` and `feats` fields filled.  I also added *Missing* in the `misc` field when that form did not appear in the *verb.txt* file. There were already 338 (53%) missing! About a third of them for `Tense=Past`, *passé simple* in French which is used mostly in literary or official context. 

John then suggested to create sentences with pronouns to help the tagger learn with a bit of context for the word although the lemmatizer would still be able to make use of the data.

## Experiments in English

### Verbs [[source](./GenerateEnglishVerbs.py)]

To *simplify* the problem we decided to first experiment with English *irregular* verbs determined using different criteria. 

The generated UDs correspond to sentences made of:

- a pronoun: *I*, *you*, *he*, *she*, *it*, *we* and *they*;

-  a verb conjugated at *present*, *simple past* and present participle with the *be* auxiliary,

After experimentation, the final criterion for choosing a verb was an "irregular" verbs, i.e. its conjugation table number is not `v1` nor `v3`  satisfying the following conditions:

- its lemma does not contain a `"-"`

- it cannot also be an adjective nor a noun
- its lemma is not in `{"instal","withhold","furnish","terrify"}`

The following verb lemma were added `["ache", "interfere", "revert", "shoo", "woo"]`

*pyrealb* was then used to realize 11,158 *sentences* for 536 verbs in the files

- `irregularVerbs-noNnoAdj.conllu` : Universal Dependency structures of the sentences
- `irregularVerbs-noNnoAdj.txt`: list of the verbs with their table number and number of occurrences of this table number in the English lexicon. These statistics were used, during development, for choosing verb criteria.

### Comparative of adjective and adverbs [[source](./GenerateEnglishComparative.py)]

This script realizes a list of the comparative and superlative forms of adjective and adverbs that are not preceded by *more* or *most*. John used it for *teaching the lemmatizer*.

## Experiments in French

A first experiment in French is done with the 22 verbs described above. After a few interactions with John, we settled on the following setting French UDs with 407 verbs of *niveau*<=6:

- a pronoun: *je*, *tu*, *il*, *nous*, *vous*, *ils*
- a verb conjugated at: 
  - *présent*, *futur*, *passé simple*, *conditionnel présent*.
  - *passé composé* with the appropriate auxiliary,
  - *participe présent* with the auxiliary être
  - participe passé with the auxiliary être but with pronouns: *il*, *elle*, *ils*, *elles*
- when a conjugated verb form does not exist in the *verb.txt* file, then `missing` is added in the `misc` field.

This created 18,646 *sentences* with the corresponding UDs. 12,172 `missing` forms were detected (65%).

Once these *sentences* were added to the French learning corpus of Stanza, John Bauer reported some improvement for previously unseen verb forms.

[Guy Lapalme](mailto:lapalme@iro.umontreal.ca)
