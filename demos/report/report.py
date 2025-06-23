#  simple demonstration of using pyrealb for generating English and French texts
#  from a single structure
#  This is a simplistic approach, but it illustrates some bilingual features of pyrealb
#  Three organisations are illustrated
#    - with word dictionaries indexed by language for cases where
#      the phrase structure are strictly parallel
#    - with a basic realizer and two language specific subclasses
#      which allows different phrase structure in both languages
#    - with a language class each keeping the words as attributes
#      and using language dependent methods

from datetime import datetime,timedelta
from pyrealb import *

from English import English
from Francais import Francais
from English_lang import English_lang
from Francais_lang import Francais_lang

today = datetime.today()
# add names to the English and French lexica
for lang in ["en","fr"]:
    load(lang)
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
individual   = {"en":"person",   "fr":"individu"}
dateOptions  = {"minute":False,"second":False}

# compare day of date with the day of the reference
def tense(date, reference):
    o = date.toordinal()
    ref_o = reference.toordinal()
    # return present if the same day, future if after else past
    return "p" if o == ref_o else "f" if o > ref_o else "ps"

# using the bilingual dictionary table
def report(event, persons, date, lang):
    load(lang)
    meeting = PP(P(prep[lang]), NP(D(det[lang]),N(event)))
    print(S(CP(C(conj[lang]), [N(person) for person in persons]),
             NP(NO(len(persons)).nat(), N(individual[lang])).ba("("),  # show number of persons
             VP(V(copula[lang]),
                A(attribute[lang]),
                meeting,
                DT(date).dOpt(dateOptions).dOpt({"rtime":True})) # show relative time
            .t(tense(date,today))).realize())

# using the _lang classes
def report_lang(event, persons, date, lang):
    load(lang.code)
    print(S(CP(lang.conj(),[N(person) for person in persons]),
            NP(NO(len(persons)).nat(), lang.individual()).ba("("),
            lang.attend(lang.meeting(event)),
            DT(date).dOpt(dateOptions))
                .t(tense(date,today)).realize())


if __name__ == "__main__":
    dates = []
    for lang in ["en","fr"]:
        load(lang)
        dates.append(DT(today).dOpt(dateOptions).cap(True).realize())
    print(" - ".join(dates),"\n")
    english = English()
    francais = Francais()
    en = English_lang()
    fr = Francais_lang()
    for (i,day) in enumerate([today-timedelta(days=1),today,today+timedelta(days=1)],
                             start=1):
        report("assembly",participants[:i], day,"en")
        report("réunion",participants[:i], day,"fr")
        print("--")
        # use Realizer subclasses
        english.report("assembly",participants[:i],day)
        francais.report("réunion",participants[:i],day)
        # use _lang classes
        print("--")
        report_lang("assembly", participants[:i], day, en)
        report_lang("réunion", participants[:i], day, fr)
        # print("--")
        print("====")


'''  output:
On monday, june 16, 2025 at 11 a.m. - Le lundi 16 juin 2025 à 11 h 

Alice (one person) was present at an assembly yesterday at 11 a.m.
Alice (un individu) fut présente à une réunion hier à 11 h. 
--
Alice (one person) attended the assembly on Sunday, June 15, 2025 at 11 a.m.
Alice (un individu) fut présente à la réunion le dimanche 15 juin 2025 à 11 h. 
--
Alice (one person) was present at an assembly yesterday at 11 a.m.
Alice (un individu) fut présente à une réunion hier à 11 h. 
====
Alice and Eve (two people) are present at an assembly today at 11 a.m.
Alice et Eve (deux individus) sont présentes à une réunion aujourd'hui à 11 h. 
--
Alice and Eve (two people) attend the assembly on Monday, June 16, 2025 at 11 a.m.
Alice et Eve (deux individus) sont présentes à la réunion le lundi 16 juin 2025 à 11 h. 
--
Alice and Eve (two people) are present at an assembly today at 11 a.m.
Alice et Eve (deux individus) sont présentes à une réunion aujourd'hui à 11 h. 
====
Alice, Eve and Bob (three people) will be present at an assembly tomorrow at 11 a.m.
Alice, Eve et Bob (trois individus) seront présents à une réunion demain à 11 h. 
--
Alice, Eve and Bob (three people) will attend the assembly on Tuesday, June 17, 2025 at 11 a.m.
Alice, Eve et Bob (trois individus) seront présents à la réunion le mardi 17 juin 2025 à 11 h. 
--
Alice, Eve and Bob (three people) will be present at an assembly tomorrow at 11 a.m.
Alice, Eve et Bob (trois individus) seront présents à une réunion demain à 11 h. 
===='''