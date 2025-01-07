# [Demos](https://github.com/lapalme/pyrealb/blob/main/README.md#demos)

- `99bottlesofbeer/99bottlesofbeer.py` : simple generation of a classic repetitive text in English.
- `basketball/sportsettsum.py` : generation of French and English basketball summaries [paper describing the approach](https://github.com/lapalme/pyrealb/blob/main/demos/basketball/docs/SportSettSum.md)
- `Bilinguo/bilinguo.py` : generation of translation drill exercises
- `dev_example/dev_example.py`: examples of English and French expressions to be realized and checked against expected output,
  useful for debugging when adding a new expression and enabling tracing
- `e2e_challenge/e2e_challenge.py`: solve the original end to end challenge in both English and French
- `eliza/eliza-talk.py`: French version of Eliza. It illustrates some interesting features of pyrealb. See [this document](https://github.com/rali-udem/jsRealB/blob/master/demos/Eliza/Eliza_en_français.md) (in French) for an explanation and rationale. It is a Python translation of [this jsRealB demo](https://github.com/rali-udem/jsRealB/tree/master/demos/Eliza). 
- `evenementsDemo/evenements.py` : Description (in French) of a list of events, it creates HTML.
- `flight_infos/README.md` : development of a RASA NLG server giving information about flights, aircrafts, etc...
- `gen_from_words.py` : generation of English and French sentences  from a plain list of words, adding some structure.
- `gen_stanza_uds/GenerateEnglishVerbs.py` or `gen_stanza_uds/genFrenchVerbs.txt`: generate *gold* Universal Dependency Structure to check Stanza output
- `gophypi/amr2text.py` : generate a literal reading of an AMR (Abstract Meaning Representation); [paper describing the approach](https://github.com/lapalme/pyrealb/blob/main/gophypi/Doc/GoPhiPy.pdf)
- `inflectionDemo/inflection.py` : French or English conjugation and declension of a form.
- `kilometresapied/kilometresapied.py` : simple generation of a classic repetitive text in French.
- `methodius/methodius.py` : generation of English sentences from a logical form expressed in XML.
- `randomgen/randomgen.py`: Generation of random English sentences
- `RDFpyrealb/WebGenerate.py` : Generation from RDF triples
- `report/report.py` : Single sentence parameterized by language, tense and subject using two different program organization
- `variantes/variantes.py`: French or English sentences realized with all possible sentence modifiers; some challenging examples are in `examples.py`.
- `weather/Bulletin.py`: French and English weather bulletins generated from information in a *json-line* file. (`weather-data.jsonl`). It uses the packages in the `Realization` directory.