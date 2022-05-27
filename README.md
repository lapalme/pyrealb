# *pyRealB* - A Python Bilingual Text Realizer

*Version 2.1 - May 2022*

*pyRealB* is a Python adaptation of the JavaScript [**jsRealB**](http://rali.iro.umontreal.ca/jsRealB) 
with the same constituent and dependency syntax notation. 
It facilitates its integration within Python applications by simply adding

	from pyrealb import *


### Installing the distribution package from PyPI

1. `pip install pyrealb`

## Upgrading the version 

1. `pip install pyrealb --upgrade`

### building and installing the package from the sources

1. `cd` into this directory (with `pyproject.toml` file) 
2. Build the distribution package `python3 -m build`
3. Install with `python3 -m pip install .`

## First realization tests at the Python 3 prompt

1. `from pyrealb import *` 
2. `print(S(Pro("I").g("f"),VP(V("say"),"hello",PP(P("to"),NP(D("the"),N("world"))))))`
3. this should print `She says hello to the world.`
4. `print(root(V("say").t("ps"),subj(Pro("him").c("nom")),comp(N("goodbye"))).typ({"neg":True}))`
5. this should print `He did not say goodbye.`

## Directories

* [`src`](./src)
    * `__init__.py` : empty program that imports subpackages and exports relevant symbols. 
    * `Constituent.py`: *Constituent* is the top class for methods shared between *Phrase*s and *Terminal*s 
    * `Lexicon.py`: class to access lexicon entries and syntactic rules
    * `Number.py` : utility functions for dealing with number formatting
    * `Phrase.py` : subclass of *Constituent* for creating complex phrases
    * `Dependent.py` : subclass of *Constituent* for creating complex phrases using dependencies
    * `Terminal.py` : subclass of *Constituent* for creating a single unit (most often a single word)
    * `util.py`  : some useful functions
    * `Warning.py` : function to generate warnings in case of erroneous specifications using *pyRealB* itself
    * [`data`](./src/pyrealb/data):
        * `lexicon-en.json` : English lexicon (33,932 entries) in json format
        * `rule-en.js` : English conjugation and declension tables
        * `lexicon-fr.json` : French lexicon (52,547 entries) in json format
        * `rule-fr.js` : French conjugation and declension tables 

In most of the following directories, a `context.py` file is used to set the appropriate search path for  *pyRealB* functions. Thus, many example programs start with the following lines:

    from context import pyrealb
    from pyrealb import *

Some directories include `markup.py` which should be loaded using `pip`. Unfortunately I never managed to make this "piped" version work, it does not import the name `oneliner`although it should. It works once the file is in the local directory.

* [`docs`](./docs): in both English and French. 
    * `documentation.html` : generated documentation (used for consultation) **DO NOT EDIT directly**
    * `documentation.py`: Python program for generating `documentation.html` using `markup.py`
    * `style.css`: style sheet for the documentation
    * `userinfos.py`: definitions of variables containing the examples
    * `user.js`  : Python helper script.
    
* [`IDE`](./IDE) : Integrated Development Environment 
	* `ide.py`: built on the Python *read-eval-print loop*, it imports *pyRealB* to get the realization of an expression, to consult the lexicon, the conjugation and declension tables. It is also possible to get a *lemmatization*: i.e. the *pyRealB* expression corresponding to a form.
	* `README.html`: documentation and examples

* [`tests`](./tests) : unit tests of special features of *pyRealB* in both French and English. Files have the pattern `*_{en|fr}.py`
	* `test.py`: simplistic function to check if a function returns the expected answer and display appropriate message
	* `testAll.html` : run this file to run all tests

## Demos

* `99bottlesofbeer/99bottlesofbeer.py` : simple generation of a classic repetitive text in English.
* `evenementsDemo/evenements.py` : Description (in French) of a list of events, it creates HTML.
* `gophypi/amr2text.py` : generate a literal reading of an AMR (Abstract Meaning Representation);  
                          [paper describing the approach](gophypi/Doc/GoPhiPy.pdf) 
* `inflectionDemo/inflection.py` : French or English conjugation and declension of a form.
* `kilometresapied/kilometresapied.py` : simple generation of a classic repetitive text in French.
* `randomgen/randomgen.py`: Generation of random English sentences
* `report/report.py` : Single sentence parameterized by language, tense and subject
* `simple_example/simple_example.py`: a few examples of English and French expressions to be realized
* `variantes/variantes.py`: French or English sentences realized with all possible sentence modifiers; some challenging examples are in `examples.py`.
* `weather/Bulletin.py`: French and English weather bulletins generated from information in a *json-line* file. (`weather-data.jsonl`). It uses the packages in the `Realization` directory.

## Contact
[Guy Lapalme](http://rali.iro.umontreal.ca/lapalme)

### Acknowledgement
Thanks to Fabrizio Gotti for helping to organize the Python package.

### Updating package version on PyPI (for the maintainer only)

see [this tutorial](https://packaging.python.org/en/latest/tutorials/packaging-projects/)

These steps take for granted that the password for PyPI has already been given...

1. update version number in `setup.cfg`
2. `cd` into the directory with the `pyproject.toml` file 
3. Build the distribution package  
       `python3 -m build`
4. Upload to PyPi  
      `twine upload dist/*`
5. Install new version from PyPI  
    `python3 -m pip install pyrealb --upgrade`
