from context import pyrealb
from datetime import datetime,timedelta
from pyrealb import *

# add names to the English and French lexica
for loadF in [loadEn,loadFr]:
    loadF()
    addToLexicon({"Alice":{ "N": { "g": "f", "tab": "nI" } }})
    addToLexicon({"Bob":{ "N": { "g": "m", "tab": "nI" } }})
    addToLexicon({"Eve":{ "N": { "g": "f", "tab": "nI" } }})
    addToLexicon({"pyrealb":{"A":{ "tab":"nI"}}})

# text parameterization
today    = datetime.today()
participants = ["Alice", "Eve", "Bob"]
conj      = {"en":"and",    "fr":"et"}
prep      = {"en":"at", "fr":"à"}
det       = {"en":"the", "fr":"le"}
meet      = {"en":"meeting", "fr":"réunion"}
copula    = {"en":"be",     "fr":"être"}
attribute = {"en":"present","fr":"présent"}
dateOptions = {"minute":False,"second":False}

def report(names, date,lang):
    loadEn() if lang=="en" else loadFr()
    meeting = PP(P(prep[lang]), NP(D(det[lang]),A("pyrealb"),N(meet[lang])))
    t = "p" if date == today else ("f" if date > today else "ps") #determine tense
    print(S(CP(C(conj[lang]),[N(name) for name in names]),
             VP(V(copula[lang]),
                A(attribute[lang]),
                meeting,
                DT(date).dOpt(dateOptions)).t(t)))

loadEn();print(DT(today).dOpt(dateOptions),"\n")
for (i,day) in zip(range(1,len(participants)+1),
                   [today-timedelta(days=1),today,today+timedelta(days=1)]):
    report(participants[:i], day,"en")
    report(participants[:i], day,"fr")
    print()

'''  output:
on Sunday, February 5, 2023 at 2 p.m. 

Alice was present at the pyrealb meeting on Saturday, February 4, 2023 at 2 p.m.
Alice fut présente à la réunion pyrealb le samedi 4 février 2023 à 14 h. 

Alice and Eve are present at the pyrealb meeting on Sunday, February 5, 2023 at 2 p.m.
Alice et Eve sont présentes à la réunion pyrealb le dimanche 5 février 2023 à 14 h. 

Alice, Eve and Bob will be present at the pyrealb meeting on Monday, February 6, 2023 at 2 p.m.
Alice, Eve et Bob seront présents à la réunion pyrealb le lundi 6 février 2023 à 14 h. 
'''