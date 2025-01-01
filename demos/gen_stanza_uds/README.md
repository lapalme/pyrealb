# Generation of English and French Universal Dependency Structures

## Context
This work was prompted by an e-mail of John Bauer, the *maintainer* of the Stanza parser, who sent me a list of French tokens (adjectives, adverbs, nouns and verbs) that are known to the Stanza parser for French. John suspected that the French lemmatization is not very good.

I started a small experiment with the 22 verbs that should be known by 75% of children at the end of their first year in school (`niveau == 1` in the *lexicon-fr.json*).  I conjugated them at 4 tenses of indicative and a few participles (29 forms for each, but some forms are the same only differing in their person: e.g "aime" can be 1st or 3rd person of present). This already created 638 forms. 

To display the results (lemma and features), I used the CONLLU format for a token with the `form`, `lemma` and `feats` fields filled.  I also added "Missing" in the `misc` field when that form did not appear in the *verb.txt* file. There were already 338 (53%) missing! About a third of them for `Tense=Past`, *passé simple* in French which is used mostly in literary or official context. 

John then suggested to create sentences with pronouns to help the tagger learn with a bit of context for the word although the lemmatizer would still be able to make use of the data.

## Experiments in English
To *simplify* the problem we decided to first experiment with English *irregular* verbs determined using different criteria. The last criterion was the selection of the 1,309 verbs whose conjugation table are used less than 2,000 times. 

The generated UDs correspond to sentences made of:

- a pronoun: *I*, *you*, *he*, *she*, *it*, *we* and *they*;

-  a verb conjugated at *present*, *simple past* and present participle with the be auxiliary,

This generated 27,300 sentences and UDs, defective verbs were not generated. 

 John reported that for 3,238 (12%) of them Stanza had not found the right lemma.

## Experiments in French

A first experiment in French is done with the 22 verbs described above.

The generated UDs correspond to sentences made of: 

- a pronoun: *je*, *tu*, *il*, *nous*, *vous*, *ils*
- a verb conjugated at: 
  - *présent*
  - *passé composé* with the appropriate auxiliary,
  - *participe présent* with the auxiliary être
  - participe passé with the auxiliary être but with pronouns: *il*, *elle*, *ils*, *elles*

This generated 478 sentences and UDs for which 83 (17%) verbs were missing from the list sent by John.

