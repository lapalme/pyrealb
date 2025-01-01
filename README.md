# *pyrealb* - A Python Bilingual Text Realizer

*Version 3.2 - January 2025*

*pyrealb* is a Python adaptation of the JavaScript [**jsRealB**](http://rali.iro.umontreal.ca/jsRealB) 
text realizer with the same constituent and dependency syntax notation. 
It facilitates its integration within Python applications by simply adding

	from pyrealb import *

[Online documentation](http://www.iro.umontreal.ca/~lapalme/pyrealb/documentation.html?lang=en)

Version 3.0.0 was a major code reorganization, but without any new feature, to clearly separate language dependent 
parts from the language independent ones. This organization is described  [here](docs/README.md) .

The use of pyrealb for [Bilingual Data-to-text generation is described in this document](https://arxiv.org/pdf/2311.14808.pdf).

### Installing the distribution package from PyPI

    pip install pyrealb

**Caution**: do not forget the `b` at the end of `pyrealb`. On _PyPI_, there is an unrelated package `pyreal` _for evaluating and deploying human readable machine learning explanations_.

### Upgrading the version 

    pip install pyrealb --upgrade

### Building and installing the package from the sources

1. `cd` into this directory (with `pyproject.toml` file)
2. Build the distribution package `python3 -m build`
3. Install with `python3 -m pip install .`

## First realization tests at the Python 3 prompt

1. `from pyrealb import *`
2. `loadEn()` 
3. `print(S(Pro("I").g("f"),VP(V("say"),"hello",PP(P("to"),NP(D("the"),N("world"))))))`
4. this should print `She says hello to the world.`
5. `print(root(V("say").t("ps"),subj(Pro("him").c("nom")),comp(N("goodbye"))).typ({"neg":True}))`
6. this should print `He did not say goodbye.`

## Use pyrealb in a _Jupyter notebook_

- Thru *Binder*, load one of these links: [English](https://mybinder.org/v2/gh/lapalme/pyrealb-jupyter/HEAD?labpath=pyrealb-en.ipynb)  [French](https://mybinder.org/v2/gh/lapalme/pyrealb-jupyter/HEAD?labpath=pyrealb-fr.ipynb) 
- From a terminal:
  - if the Python notebook module is not already installed, do: `pip3 install notebook` and watch a lot of loading...
  - `cd Notebooks`
  - `python3 -m notebook`  this should open a browser window with links to the [English](pyrealb-en.ipynb) and [French](pyrealb-fr.ipynb) notebooks 

## Directories

* [`src/pyrealb`](./src/pyrealb)
    * `__init__.py` : import classes and functions and export relevant symbols. 
    * `Constituent.py`: *Constituent* is the top class for methods shared between *Phrase*s and *Terminal*s 
    * `ConstituentEn.py`, `ConstituentFr.py` : English and French specific processing of `Constituent`
    * `Dependent.py` : subclass of *Constituent* for creating complex phrases using dependencies
    * `DependentEn.py`, `DependentFr.py` : English and French specific processing of `Dependent`
    * `Lexicon.py`: class to access lexicon entries and syntactic rules
    * `LICENSE.txt`: Apache 2.0 License
    * `NonTerminalEn.py`, `NonTerminalFr.py` : language dependent processing common to `Phrase` and `Dependent`
    * `Number.py` : utility functions for dealing with number formatting
    * `Phrase.py` : subclass of *Constituent* for creating complex phrases
    * `PhraseEn.py`, `PhraseFr.py` : English and French specific processing of `Phrase` 
    * `Terminal.py` : subclass of *Constituent* for creating a single unit (most often a single word)
    * `TerminalEn.py`, `TerminalFr.py` : English and French specific processing of `Terminal`
    * `utils.py`  : some useful functions
* [`./src/pyrealb/data`](./src/pyrealb/data):
    * `LICENSE.txt` : Creative Common license
    * `lexicon-en.json` : English lexicon (33,932 entries) in json format
    * `rule-en.js` : English conjugation and declension tables
    * `lexicon-fr.json` : French lexicon (52,547 entries) in json format
    * `rule-fr.js` : French conjugation and declension tables 

_Nota bene_:
1. In the following directories, the `__init__.py` file is used to set the appropriate search path for  *pyrealb* functions; this ensures that the current Python source files are used for execution. 
2. Some directories include `markup.py` which should be loaded using `pip`. Unfortunately I never managed to make 
   this "piped" version work, it does not import the name `oneliner`although it should. It works only if the file is in the local directory.

* [`docs`](./docs): in both English and French. 
    * `documentation.html` : generated documentation (used for consultation) **DO NOT EDIT directly**  [Online version](http://www.iro.umontreal.ca/~lapalme/pyrealb/documentation.html?lang=en)
    * `documentation.py`: Python program for generating `documentation.html` using `markup.py`  
          once this is run `documentation.html` should be copied at `http://www.iro.umontreal.ca/~lapalme/pyrealb/documentation.html` which is used for consultation 
    * `style.css`: style sheet for the documentation
    * `userinfos.py`: definitions of variables containing the examples
    * `user.js`  : Python helper script.
    
* [`IDE`](./IDE) : Integrated Development Environment 
    
    * `ide.py`: built on the Python *read-eval-print loop*, it imports *pyrealb* to get the realization of an expression, to consult the lexicon, the conjugation and declension tables. It is also possible to get a *lemmatization*: i.e. the *pyrealb* expression corresponding to a form. 
    * `README.html`: documentation and examples
    
    *Nota bene*: The [evaluation demo of *jsRealB*](http://rali.iro.umontreal.ca/JSrealB/current/demos/Evaluation/index.html) is more convenient than this IDE to develop *pyrealb* expressions as both programs share the same formalism. The *jsRealB* demo provides an editor and access to the lexicons and  rules.
    
* [Notebooks](./NoteBooks) : Jupyter notebooks (in English and French) with can be used as an executable introduction to *pyrealb*
    
* [`tests`](./tests) : unit tests of special features of *pyrealb* in both French and English. Files have the pattern `*_{en|fr}.py`
    
    * `test.py`: simplistic function to check if a function returns the expected answer and display appropriate message
    * `testAll.html` : run this file to run all tests

## Demos

* `99bottlesofbeer/99bottlesofbeer.py` : simple generation of a classic repetitive text in English.
* `basketball/sportsettsum.py` : generation of French and English basketball summaries [paper describing the approach](demos/basketball/docs/SportSettSum.md)
* `Bilinguo/bilinguo.py` : generation of translation drill exercises
* `dev_example/dev_example.py`: examples of English and French expressions to be realized and checked against expected output,  useful for debugging when adding a new expression and enabling tracing.
* `eliza/eliza-talk.py`: French version of Eliza. It illustrates some interesting features of pyrealb. See [this document](https://github.com/rali-udem/jsRealB/blob/master/demos/Eliza/Eliza_en_français.md) (in French) for an explanation and rationale. It is a Python translation of [this jsRealB demo](https://github.com/rali-udem/jsRealB/tree/master/demos/Eliza). 
* `evenements/evenements.py` : Description (in French) of a list of events, it creates HTML.
* `flight_infos/README.md` : development of a RASA NLG server giving information about flights, aircrafts, etc...
* `gen_from_words.py` : generation of English and French sentences  from a plain list of words, adding some structure.
* `gophypi/amr2text.py` : generate a literal reading of an AMR (Abstract Meaning Representation);
                          [paper describing the approach](gophypi/Doc/GoPhiPy.pdf) 
* `inflection/inflection.py` : French or English conjugation and declension of a form.
* `kilometresapied/kilometresapied.py` : simple generation of a classic repetitive text in French.
* `methodius/methodius.py` : generation of English sentences from a logical form expressed in XML.
* `randomgen/randomgen.py`: Generation of random English sentences
* `RDFpyrealb/WebGenerate.py` : Generation from RDF triples
* `report/report.py` : Single sentence parameterized by language, tense and subject using two different program organization
* `variantes/variantes.py`: French or English sentences realized with all possible sentence modifiers; some challenging examples are in `examples.py`.
* `weather/Bulletin.py`: French and English weather bulletins generated from information in a *json-line* file. (`weather-data.jsonl`). It uses the packages in the `Realization` directory.

## Licenses
* _pyrealb_ source code is licensed under _Apache-2.0_ 
* linguistic resources in the `./data` directory are licensed under _CC-BY-SA-4.0_

## Contact
[Guy Lapalme](http://rali.iro.umontreal.ca/lapalme)

## Acknowledgement
Thanks to Fabrizio Gotti, François Lareau and Ludan Stoeckle for interesting suggestions.

## For the maintainer mainly
### Updating package version on PyPI 

see [this tutorial](https://packaging.python.org/en/latest/tutorials/packaging-projects/)

These steps take for granted that the password for PyPI has already been given...

1. Update version number in `setup.cfg` (it should be the same as `python_version` in `src/pyrealb/utils.py` and at 
   the beginning of this document). 
2. Run `docs/documentation.py` to update the version number in `docs/documentation.html`
3. Commit pyrealb on GitHub
4. `cd` into the directory with the `pyproject.toml` file (the same as this `README.md`)
5. Build the distribution package  
       `python3 -m build`
6. Upload to PyPi the last version I.J.K
      `twine upload dist/*-I.J.K.*`
7. Install new version from PyPI  
    `python3 -m pip install pyrealb --upgrade`

### Useful trick for debugging with breaking point and tracing in PyCharm
1. add `pyrealb` expression to debug at the end of `demo/dev_example/dev_example.py`
2. comment the line calling `testPreviousExamples()`
3. debug `demo/dev_example/dev_example.py`