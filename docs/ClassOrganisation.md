# Class *re-*organisation of *pyrealb*

## Original class organization

*pyrealb* is symbolic system for realizing English and French sentences, even bilingual ones. It has be built incrementally over the years as single python program for both languages. It uses an object oriented approach with class names based on the usual names used in linguistic. Each class is defined in a python file of the same name.

- `Constituent`: the root class for all objects, its methods are used by all kinds of objects. This class is the superclass of the next three classes.
- `Terminal`: this class corresponds roughly to the *words* of the realization, e.g. a noun or a verb;  a terminal can be realized as more than one word (e.g for a conjugated verb) or even none (e.g. plural of the definite determiner *a*)
- `Phrase`: this class groups `Terminal` or other `Phrase` instances; it corresponds to the organization of a sentence in a constituency grammar such as a *Verb Phrase* or a *Noun Phrase*
- `Dependent`: an alternative grouping of `Terminal` and `Dependent` instances using a Dependency grammar formalism; *programmatically* this class also inherits from `Constituent` even though linguists might be reluctant to consider a `Dependent` as a kind of  `Constituent`. This dubious choice of class name is the result of the fact that the dependency formalism was added later in the development.  

The other python files: `Lexicon.py`, `Number.py` and `utils.py` serve as containers for functions that are called from the instances of the classes.

## Revised class organization

The language associated with instances`Terminal,` `Phrase`, and `Dependent` classes is determined when the object is 
created depending on the current language. It can also be specified at creation time.

Previously language specific operations such as conjugation, elision, position of certain words were determined by testing the language associated with each object. The language tests were scattered in the source file.

In order to make the language dependent parts more explicit, we decided to split the processing in three kinds of classes: methods common to both languages, classes with English specific methods (ending with `En`) and French specific (ending with `Fr`). Language specific instances are created from classes that inherit from two or more of these classes.

The previous single inheritance hierarchy is kept to which a parallel language dependent hierarchy (its class names end by `En` or `Fr`) is added. For example: 

-  `TerminalEn` inherits from `ConstituentEn` and `Terminal`. 
- `PhraseEn` inherits from `ConstituentEn`, `Phrase` and `NonTerminalEn`. The latter containing some language dependent functions are common to `Phrase` and `Dependent` instances such as the *Affix Hopping* algorithm for conjugating English verbs or the adverb or pronoun placement in French.
- `DependentEn` inherits from `ConstituentEn`, `Dependent`, `NonTerminalEn`.

A similar hierarchy is defined for French. This is illustrated in the following UML diagram showing classes with their main attributes and methods. Arrows indicates subclass relationships from child to parent.



![pyrealb-classes](/Users/lapalme/Library/CloudStorage/Dropbox/Test_pyrealb/pyrealb-classes.png)

As `Terminal`, `Phrase` and `Dependent` instances will be created in a specific language, the language dependent processing will be selected automatically by the python method dispatching mechanism. In fact there are no more any language test in the code. As can be seen in the diagram, methods in corresponding language classes have the same.  If a processing is needed in only one language, then an empty method with the same name is defined in the other language.

### Creation of `Terminal` instances

The selection of the appropriate `TerminalXy` class is done by the following factory function for which the language can be specified as parameter, which is seldom the case. The appropriate class is determined by the current language as set by the last encountered`loadEn()` or `loadFr()`.

```python
def terminal(constType,lemma,lang=None):
    if lang is None:lang=currentLanguage()
    if lang == "en": return TerminalEn(constType, lemma)
    return TerminalFr(constType, lemma)
```

Using this function, we can define 11  functions for creating new Terminals. Here, we only show the function for create a *noun*, but all others (`D,A,V,Pro`...) follow the same pattern.

```python
def N(lemma=None,lang=None):
    return terminal("N",lemma,lang)
```

### Creation of `Phrase` and `Dependent` instances

The same class selection mechanism is used for phrases and dependents. Here we show only one Phrase and dependent creation factory functions, but all others (`VP`, `S`, `SP`, `CP`, ...) and (`det`, `mod`, `coord`,...) are similar.

```python
def phrase(constType,elems,lang=None):
    if lang is None:lang = currentLanguage()
    if lang == "en":return PhraseEn(constType, elems)
    return  PhraseFr(constType, elems)
  
def dep(params,deprel,lang=None):
    if lang is None: lang=currentLanguage()
    if lang == "en": return DependentEn(params, deprel)
    return DependentFr(params, deprel)

def NP(*elems,lang=None):
    return phrase("NP",elems,lang)

def root(*params,lang=None):
    return dep(params,"root",lang)
```

