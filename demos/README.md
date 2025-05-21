# [Demos](https://github.com/lapalme/pyrealb/blob/main/README.md#demos)

- `99bottlesofbeer/99bottlesofbeer.py` : simple generation of a classic repetitive text in English.
- `basketball/sportsettsum.py` : generation of French and English basketball summaries [paper describing the approach](demos/basketball/docs/SportSettSum.md)
- `Bilinguo/bilinguo.py` : generation of translation drill exercises
- `dev_example/dev_example.py`: examples of English and French expressions to be realized and checked against expected output,  useful for debugging when adding a new expression and enabling tracing.
- `eliza/eliza-talk.py`: French version of Eliza. It illustrates some interesting features of pyrealb. See [this document](https://github.com/rali-udem/jsRealB/blob/master/demos/Eliza/Eliza_en_français.md) (in French) for an explanation and rationale. It is a Python translation of [this jsRealB demo](https://github.com/rali-udem/jsRealB/tree/master/demos/Eliza). 
- `evenements/evenements.py` : Description (in French) of a list of events, it creates HTML.
- `flight_infos/README.md` : development of a RASA NLG server giving information about flights, aircrafts, etc...
- `gen_from_words.py` : generation of English and French sentences  from a plain list of words, adding some structure.
- `gen_stanza_uds/*.py` : various programs used for generating sentences for *helping* the Stanza lemmatizing learn new inflected forms in French but also in English.
- `gophypi/amr2text.py` : generate a literal reading of an AMR (Abstract Meaning Representation);
      [paper describing the approach](gophypi/Doc/GoPhiPy.pdf) 
- `inflection/inflection.py` : French or English conjugation and declension of a form.
- `kilometresapied/kilometresapied.py` : simple generation of a classic repetitive text in French.
- `methodius/methodius.py` : generation of English sentences from a logical form expressed in XML.
- `randomgen/randomgen.py`: Generation of random English sentences
- `RDFpyrealb/WebGenerate.py` : Generation from RDF triples
- `report/report.py` : Single sentence parameterized by language, tense and subject using two different program organization
- `S+7/s_plus_7.py`: parse sentences and realize these sentences but with nouns, adjectives and verbs changed with the 7th following word in the *pyrealb* lexicon. See details in `S+7/doc/S+7.html` created by `S+7/doc/S+7.md`
- `variantes/variantes.py`: French or English sentences realized with all possible sentence modifiers; some challenging examples are in `examples.py`.
- `weather/Bulletin.py`: French and English weather bulletins generated from information in a *json-line* file. (`weather-data.jsonl`). It uses the packages in the `Realization` directory.