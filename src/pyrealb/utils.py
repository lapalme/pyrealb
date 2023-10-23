## Python version of jsRealB
##   the organization parallels the one of JavaScript version (version 4.0)
##   in fact, the JavaScript version was sometimes revised in order to make it
##   similar
## Guy Lapalme, December 2021

import datetime
import random
import sys

from .Lexicon import currentLanguage
from .Terminal import Terminal
from .Phrase import Phrase
from .Dependent import Dependent

pyrealb_oneOf_dict = {}  # internal Map for keeping track of calls to specific oneOf call

# Select a random element in a list useful to have some variety in the generated text
# if the first argument is a list, selection is done within the list,
# otherwise the selection is among the arguments
# Implements the "mode:once" of RosaeNLG
#    (https://rosaenlg.org/rosaenlg/4.3.0/mixins_ref/synonyms.html#_choose_randomly_but_try_not_to_repeat)
# Select an alternative randomly, but tries not to repeat the same alternative.
# When all alternatives have been triggered, it will reset, but will try not run the last triggered alternative
# as the first new one, avoiding repetitions.
def oneOf(*elems):
    if len(elems) == 1:
        if isinstance(elems[0], list):
            elems = elems[0]
    l = len(elems)
    if l==1:
        e = elems[0]
    else:
        elems_key = repr(elems)  # HACK: create key from the array
        if elems_key in pyrealb_oneOf_dict :
            past_indices = pyrealb_oneOf_dict[elems_key] # // a list of past indices
            if len(past_indices)<l:
                indices = [i for i in range(l) if i not in past_indices]
            else: # reset the list but avoid last index
                last_idx = past_indices[-1]
                indices = [i for i in range(l) if i != last_idx]
                past_indices.clear()
            idx = random.choice(indices)
            past_indices.append(idx)
        else:  # first call
            indices = list(range(l))
            idx = random.choice(indices)
            pyrealb_oneOf_dict[elems_key]=[idx] # initialise dict element
        e = elems[idx]
    return e() if callable(e) else e

# Mix elements of a list in a random order.
# If the first argument is a list, mixing is done within the list,
# otherwise the mix is among the arguments. The original list is not modified
def mix(*elems):
    if len(elems) == 1:
        if isinstance(elems[0], list):
            elems = elems[0].copy()
    else:
        elems = list(elems).copy()
    random.shuffle(elems)
    return [e() if callable(e) else e for e in elems]

# Flag for quoting out of vocabulary tokens (not yet taken into account)
# quoteOOV=False;
# def setQuoteOOV(qOOV):
#     global quoteOOV
#     quoteOOV=qOOV

# create expression from a JSON structure
def fromJSON(json, lang=None):
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
        lang1 = lang if lang is not None else currentLanguage()
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


# useful variables for using expressions written originally for the javascript version
false = False
true = True
null = None

# version and date informations
pyrealb_version = "2.3.8"
pyrealb_datecreated = datetime.datetime.today()
