## Python version of jsRealB
##   the organization parallels the one of JavaScript version (version 4.0)
##   in fact, the JavaScript version was sometimes revised in order to make it
##   similar
## Guy Lapalme, December 2021

import datetime
import random
import sys

from .Lexicon import getLanguage

pyrealb_oneOf_dict = {}  # internal Map for keeping track of calls to specific oneOf call

# Select a random element in a list useful to have some variety in the generated text
# if the first argument is a list, selection is done within the list,
# otherwise the selection is among the arguments
# Implements the "mode:once" of RosaeNLG
#    (https://rosaenlg.org/rosaenlg/4.3.0/mixins_ref/synonyms.html#_choose_randomly_but_try_not_to_repeat)
# Select an alternative randomly, but tries not to repeat the same alternative.
# When all alternatives have been triggered, it will reset, but will not run the last triggered alternative
# as the first new one, avoiding repetitions.
# if the chosen element is "callable" (lambda:...) , then it is applied to ()
def oneOf(*elems):
    if len(elems) == 1:
        if isinstance(elems[0], list):
            elems = elems[0]
    l = len(elems)
    if l==0:
        return None
    if l==1:
        e = elems[0]
    else:
        elems_key = repr(elems)  # HACK: create key from the array
        if elems_key not in pyrealb_oneOf_dict :  # first call
            indices = list(range(l))  # a list of indices to return
            random.shuffle(indices)
            idx = indices.pop()       # return last element as index
            pyrealb_oneOf_dict[elems_key]=indices # initialise dict element
        else:
            indices = pyrealb_oneOf_dict[elems_key] # a list of past indices
            idx = indices.pop()                     # return last element as index
            if len(indices) == 0:
                indices = list(range(l))  # a list of indices to return
                random.shuffle(indices)
                if indices[-1] ==idx:
                    # swap first and last so that last will not be returned next time
                    indices[0],indices[-1] = indices[-1],indices[0]
                pyrealb_oneOf_dict[elems_key] = indices  # reset dict element
        e = elems[idx]
    return e() if callable(e) else e

# Select a random element in a list
# if the first argument is a list, selection is done within the list,
# otherwise the selection is among the arguments
# Similar to oneOf() but without taking into account previous choices
# if the chosen element is "callable" (lambda:...) , then it is applied to ()
def choice(*elems):
    if len(elems) == 1:
        if isinstance(elems[0], list):
            elems = elems[0]
    l = len(elems)
    if l==0:
        return None
    if l==1:
        e = elems[0]
    else:
        e = random.choice(elems)
    return e() if callable(e) else e

# Mix elements of a list in a random order.
# If the first argument is a list, mixing is done within the list,
# otherwise the mix is among the arguments. The original list is not modified
# if the chosen element is "callable" (lambda:...) , then it is applied to ()
def mix(*elems):
    if len(elems) == 1:
        if isinstance(elems[0], list):
            elems = elems[0].copy()
    else:
        elems = list(elems).copy()
    random.shuffle(elems)
    return [(e() if callable(e) else e) for e in elems]

# Flag for quoting out of vocabulary tokens (not yet taken into account)
# quoteOOV=False;
# def setQuoteOOV(qOOV):
#     global quoteOOV
#     quoteOOV=qOOV

# return a list of elements that are not None flattening embedded lists (used by Phrase and Dependent)
def _getElems(es):
    res = []
    for e in es:
        if e is not None:
            if isinstance(e, (list,tuple)):res.extend([e0 for e0 in _getElems(e) if e0 is not None])
            else:res.append(e)
    return res

# create expression from a JSON structure
def fromJSON(json, lang=None):
    from .Terminal import Terminal
    from .Phrase import Phrase
    from .Dependent import Dependent
    if isinstance(json, dict):
        if "lang" in json:
            if json["lang"] == "en":
                lang = "en"
            elif json["lang"] == "fr":
                lang = "fr"
            else:
                print("FromJSON: lang should be 'en' or 'fr', not " + json["lang"] + " 'en' will be used",
                      file=sys.stderr)
                lang = "en"
        lang1 = lang if lang is not None else getLanguage()
        if "phrase" in json:
            constType = json["phrase"]
            if constType in ['NP', 'AP', 'AdvP', 'VP', 'PP', 'CP', 'S', 'SP']:
                return Phrase.fromJSON(constType, json, lang1)
            else:
                print("fromJSON: unknown Phrase type:" + constType, file=sys.stderr)
        elif "dependent" in json:
            constType = json["dependent"]
            if constType in ["root", "det", "subj", "comp", "mod", "compObj", "compObl", "coord"]:
                return Dependent.fromJSON(constType, json, lang1)
            else:
                print("fromJSON: unknown Dependent type:" + constType, file=sys.stderr)
        elif "terminal" in json:
            constType = json["terminal"]
            if constType in ['N', 'A', 'Pro', 'D', 'Adv', 'V', 'P', 'C', 'DT', 'NO', 'Q']:
                return Terminal.fromJSON(constType, json, lang1)
            else:
                print("fromJSON: unknown Terminal type:" + constType, file=sys.stderr)
    else:
        print("fromJSON: object expected, but found " + type(json).__name__ + ":" + repr(json), file=sys.stderr)


# version and date information
pyrealb_version = "3.2"
pyrealb_datecreated = datetime.datetime.today()

####################################################################################
###  Factory functions for Terminals
from .TerminalEn import TerminalEn
from .TerminalFr import TerminalFr
# call language dependent constructors
def terminal(constType,lemma,lang=None):
    if lang is None:lang=getLanguage()
    if lang == "en": return TerminalEn(constType, lemma)
    return TerminalFr(constType, lemma)

# terms = ["N","A","Pro","D","Adv","V","P","C","DT","NO","Q"]
def N(lemma=None,lang=None):
    return terminal("N",lemma,lang)

def A(lemma=None,lang=None):
    return terminal("A",lemma,lang)

def Pro(lemma=None,lang=None):
    return terminal("Pro",lemma,lang)

def D(lemma=None,lang=None):
    return terminal("D",lemma,lang)

def Adv(lemma=None,lang=None):
    return terminal("Adv",lemma,lang)

def V(lemma=None,lang=None):
    return terminal("V",lemma,lang)

def P(lemma=None,lang=None):
    return terminal("P",lemma,lang)

def C(lemma=None,lang=None):
    return terminal("C",lemma,lang)

def DT(lemma=None,lang=None):
    return terminal("DT",lemma,lang)

def NO(lemma=None,lang=None):
    return terminal("NO",lemma,lang)

def Q(lemma=None,lang=None):
    return terminal("Q",lemma,lang)

### Factory function for Phrases

from .PhraseEn import PhraseEn
from .PhraseFr import PhraseFr

##  functions to call language specific constructors
def phrase(constType,elems,lang=None):
    if lang is None:lang = getLanguage()
    if lang == "en":return PhraseEn(constType, elems)
    return  PhraseFr(constType, elems)

def NP(*elems,lang=None):
    return phrase("NP",elems,lang)

def AP(*elems,lang=None):
    return phrase("AP",elems,lang)

def AdvP(*elems,lang=None):
    return phrase("AdvP",elems,lang)

def VP(*elems,lang=None):
    return phrase("VP",elems,lang)

def PP(*elems,lang=None):
    return phrase("PP",elems,lang)

def CP(*elems,lang=None):
    return phrase("CP",elems,lang)

def S(*elems,lang=None):
    return phrase("S",elems,lang)

def SP(*elems,lang=None):
    return phrase("SP",elems,lang)

### Factory methods for Dependent

from .DependentEn import DependentEn
from .DependentFr import DependentFr

## call language dependent constructors
def dep(params,deprel,lang=None):
    if lang is None: lang=getLanguage()
    if lang == "en": return DependentEn(params, deprel)
    return DependentFr(params, deprel)

def root(*params,lang=None):
    return dep(params,"root",lang)

def subj(*params,lang=None):
    return dep(params,"subj",lang)

def det(*params,lang=None):
    return dep(params,"det",lang)

def mod(*params,lang=None):
    return dep(params,"mod",lang)

def comp(*params,lang=None):
    return dep(params,"comp",lang)

def coord(*params,lang=None):
    return dep(params,"coord",lang)
