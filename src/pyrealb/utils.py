## Python version of jsRealB
##   the organization parallels the one of JavaScript version (version 3.9)
##   in fact, the JavaScript version was sometimes revised in order to make it
##   similar
## Guy Lapalme, December 2021

# select a random element in a list useful to have some variety in the generated text
#  if the first argument is a list, selection is done within the list
#  otherwise the selection is among the arguments
#   (if the selected element is a function, evaluate it with no parameter)
import datetime
import random
import sys

from .Lexicon import currentLanguage
from .Terminal import Terminal
from .Phrase import Phrase


def oneOf(*elems):
    if len(elems) == 1:
        if isinstance(elems[0], list):
            e = random.choice(elems[0])
        else:
            e = elems[0]
    else:
        e = random.choice(elems)
    return e() if callable(e) else e


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
                lang = "fr";
            else:
                print("FromJSON: lang should be 'en' or 'fr', not " + json["lang"] + " 'en' will be used",
                      file=sys.stderr);
                lang = "en";
        lang1 = lang if lang != None else currentLanguage()
        if "phrase" in json:
            constType = json["phrase"];
            if constType in ['NP', 'AP', 'AdvP', 'VP', 'PP', 'CP', 'S', 'SP']:
                return Phrase.fromJSON(constType, json, lang1)
            else:
                print("fromJSON: unknown Phrase type:" + constType, file=sys.stderr)
        elif "terminal" in json:
            constType = json["terminal"];
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
pyRealB_version = "1.1"
pyRealB_dateCreated = datetime.datetime.today()
