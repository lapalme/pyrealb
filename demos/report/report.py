#  simple demonstration of using pyrealb for generating English and French texts
#  from a single structure
#  This is a simplistic approach, but it illustrates some bilingual features of pyrealb
#  Two methods are used
#    - with word dictionaries indexed by language for cases where
#      the phrase structure are strictly parallel
#    - with a basic realizer and two language specific subclasses
#      which allows different phrase structure in both languages

from datetime import datetime,timedelta
from pyrealb import *

from English import English
from Francais import Francais

# add names to the English and French lexica
for loadF in [loadEn,loadFr]:
    loadF()
    addToLexicon({"Alice":{ "N": { "g": "f", "tab": "nI" } }})
    addToLexicon({"Bob":{ "N": { "g": "m", "tab": "nI" } }})
    addToLexicon({"Eve":{ "N": { "g": "f", "tab": "nI" } }})

# text parameterization with words dictionaries indexed by language
participants = ["Alice", "Eve", "Bob"]
conj         = {"en":"and",     "fr":"et"}
prep         = {"en":"at",      "fr":"à"}
det          = {"en":"a",       "fr":"un"}
copula       = {"en":"be",       "fr":"être"}
attribute    = {"en":"present",  "fr":"présent"}
individual   = {"en":"person",   "fr":"personne"}
dateOptions  = {"minute":False,"second":False}

# compare day of date with the day of the reference
def tense(date, reference):
    o = date.toordinal()
    ref_o = reference.toordinal()
    return "p" if o == ref_o else "f" if o > ref_o else "ps"

def report(event, persons, date, lang):
    loadEn() if lang=="en" else loadFr()
    meeting = PP(P(prep[lang]), NP(D(det[lang]),N(event)))
    return S(CP(C(conj[lang]), [N(person) for person in persons]),
             NP(NO(len(persons)).nat(), N(individual[lang])).ba("("),  # show number of persons
             VP(V(copula[lang]),
                A(attribute[lang]),
                meeting,
                DT(date).dOpt(dateOptions)).t(tense(date,today)))

if __name__ == "__main__":
    today = datetime.today()
    loadEn(); print(DT(today).dOpt(dateOptions).realize(),end="")
    loadFr();print("-",DT(today,"fr").dOpt(dateOptions).realize(),"\n")
    english = English()
    francais = Francais()
    for (i,day) in zip(range(1,len(participants)+1),
                       [today-timedelta(days=1),today,today+timedelta(days=1)]):
        print(report("assembly",participants[:i], day,"en").realize())
        print(report("réunion",participants[:i], day,"fr").realize())
        print("--")
        # use Realizer subclasses
        english.report("assembly",participants[:i],day)
        francais.report("réunion",participants[:i], day)
        print("====")


'''  output:
on Monday, October 23, 2023 at 2 p.m.- le lundi 23 octobre 2023 à 14 h 

Alice (one person) was present at an assembly on Sunday, October 22, 2023 at 2 p.m.
Alice (une personne) fut présente à une réunion le dimanche 22 octobre 2023 à 14 h. 
--
Alice (one person) attended the assembly on Sunday, October 22, 2023 at 2 p.m.
Alice (un individu) fut présente à la réunion le dimanche 22 octobre 2023 à 14 h. 
====
Alice and Eve (two persons) are present at an assembly on Monday, October 23, 2023 at 2 p.m.
Alice et Eve (deux personnes) sont présentes à une réunion le lundi 23 octobre 2023 à 14 h. 
--
Alice and Eve (two persons) attend the assembly on Monday, October 23, 2023 at 2 p.m.
Alice et Eve (deux individus) sont présentes à la réunion le lundi 23 octobre 2023 à 14 h. 
====
Alice, Eve and Bob (three persons) will be present at an assembly on Tuesday, October 24, 2023 at 2 p.m.
Alice, Eve et Bob (trois personnes) seront présents à une réunion le mardi 24 octobre 2023 à 14 h. 
--
Alice, Eve and Bob (three persons) will attend the assembly on Tuesday, October 24, 2023 at 2 p.m.
Alice, Eve et Bob (trois individus) seront présents à la réunion le mardi 24 octobre 2023 à 14 h. 
====
'''