from context import pyrealb
from datetime import datetime,timedelta
from pyrealb import *

# add names to the English and French lexica
for loadF in [loadEn,loadFr]:
    loadF()
    addToLexicon({"Alice":{ "N": { "g": "f", "pe": 3, "tab": "nI" } }})
    addToLexicon({"Bob":{ "N": { "g": "m", "pe": 3, "tab": "nI" } }})
    addToLexicon({"Eve":{ "N": { "g": "f", "pe": 3, "tab": "nI" } }})
# text parameterization
today    = datetime.today()
participants = ["Alice", "Eve", "Bob"]
conj      = {"en":"and",    "fr":"et"}
copula    = {"en":"be",     "fr":"être"}
attribute = {"en":"present","fr":"présent"}
dateOptions = {"minute":False,"second":False}

def report(names, date,lang):
    if lang=="en":
        loadEn(); meet = PP(P("at"), NP(D("the"),Q("jsRealB"),N("meeting")))
    else:
        loadFr(); meet = PP(P("à"),NP(D("le"),N("réunion"),Q("jsRealB")))
    t = "p" if date == today else ("f" if date > today else "ps") #determine tense
    print(S(CP(*[C(conj[lang]),
                 *[N(name) for name in names]]),
             VP(V(copula[lang]),
                A(attribute[lang]),meet),
                DT(date).dOpt(dateOptions)).t(t))

loadEn();print(DT(today).dOpt(dateOptions),"\n")
for (i,day) in zip(range(1,len(participants)+1),
                   [today-timedelta(days=1),today,today+timedelta(days=1)]):
    report(participants[:i], day,"en")
    report(participants[:i], day,"fr")
    print()

'''  output:
on Monday, May 9, 2022 at 11 a.m. 

Alice was present at the jsRealB meeting on Sunday, May 8, 2022 at 11 a.m.
Alice fut présente à la réunion jsRealB le dimanche 8 mai 2022 à 11 h.

Alice and Eve are present at the jsRealB meeting on Monday, May 9, 2022 at 11 a.m.
Alice et Eve sont présentes à la réunion jsRealB le lundi 9 mai 2022 à 11 h.

Alice, Eve and Bob will be present at the jsRealB meeting on Tuesday, May 10, 2022 at 11 a.m.
Alice, Eve et Bob seront présents à la réunion jsRealB le mardi 10 mai 2022 à 11 h.
'''