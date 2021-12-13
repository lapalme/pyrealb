# *pyRealB* - A Python Bilingual Text Realizer

*Version 1.0 - December 2021*

*pyRealB* is a Python adaptation of the JavaScript [**jsRealB**](http://rali.iro.umontreal.ca/jsRealB) with the same dependency syntax notation. It facilitates its integration within Python applications by simply adding

	from pyRealB import *

CAUTION: some directories include `markup.py` which should be loaded using `pip`. Unfortunately I never managed to make this "piped" version work,it does not import the name `oneliner`although it should. It works once the file is in the local directory.

## Program files
* `pyRealB.py` : main program that exports all relevant symbols and defines a few utility functions.   
              Running this file will exercise a few typical functions, but usually it is `import`ed.
* `Constituent.py`: *Constituent* is the top class for methods shared between *Phrase*s and *Terminal*s 
* `Lexicon.py`: class to access lexicon entries and syntactic rules
* `Number.py` : utility functions for dealing with number formatting
* `Phrase.py` : subclass of *Constituent* for creating complex phrases
* `Terminal.py` : subclass of *Constituent* for creating a single unit (most often a single word)
* `Warnings.py` : function to generate warnings in case of erroneous specifications using *pyRealB* itself

## Directories
* [`data`](data/):
    * `lexicon-en.json` : English lexicon (33,926 entries) in json format
    * `rule-en.js` : English conjugation and declension tables
    * `lexicon-fr.json` : French lexicon (52,512 entries) in json format
    * `rule-fr.js` : French conjugation and declension tables 

* [`Documentation`](documentation/): in both English and French. 
    * `documentation.html` : generated documentation (used for consultation)
    * `documentation.py`: Python program for generating `documentation.html` using `markup.py`
    * `style.css`: style sheet for the documentation
    * `userinfos.py`: definitions of variables containing the examples
    * `user.js`  : Python helper script.
    
* [`IDE`](IDE/) : Integrated Development Environment 
	* `pyRealB_ide.py`: built on the Python *read-eval-print loop*, it imports *pyRealB* to get the realization of an expression, to consult the lexicon, the conjugation and declension tables. It is also possible to get a *lemmatization*: i.e. the *pyRealB* expression corresponding to a form.
	* `pyReealB_ide.html`: documentation and examples

* [`Tests`](Tests/) : unit tests of special features of *pyRealB* in both French and English. Files have the pattern `*_{en|fr}.py`
 
	* `test.py`: simplistic function to check if a function the expected answer
	* `testAll.html` : run this file to run all tests

## Demos

* `EvenementsDemo/evenements.py` : Description (in French) of a list of events, it creates HTML.
* `InflectionDemo/inflection.py` : French or English conjugation and declension of a form.
* `RandomGenDemo/RandomGen.py`: Generation of random English sentences
* `VariantesDemo/variantes.py`: French or English sentences realized with all possible sentence modifiers; some challenging examples are in `examples.py`
* `WeatherDemo/Bulletin.py`: French and English weather bulletins generated from information in a *json-line* file (`weather-data.jsonl`)

## Contact
[Guy Lapalme](http://rali.iro.umontreal.ca/lapalme).      
