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
    addToLexicon({"pyrealb":{"A":{ "tab":"nI"}}})

# text parameterization with words dictionaries indexed by language
today    = datetime.today()
participants = ["Alice", "Eve", "Bob"]
conj      = {"en":"and",    "fr":"et"}
prep      = {"en":"at", "fr":"à"}
det       = {"en":"the", "fr":"le"}
meet      = {"en":"meeting", "fr":"réunion"}
copula    = {"en":"be",     "fr":"être"}
attribute = {"en":"present","fr":"présent"}
dateOptions = {"minute":False,"second":False}

# compare day of date with the day of the reference
def tense(date, reference):
    o = date.toordinal()
    ref_o = reference.toordinal()
    return "p" if o == ref_o else "f" if o > ref_o else "ps"

def report(names, date,lang):
    loadEn() if lang=="en" else loadFr()
    meeting = PP(P(prep[lang]), NP(D(det[lang]),A("pyrealb"),N(meet[lang])))
    print(S(CP(C(conj[lang]),[N(name) for name in names]),
             VP(V(copula[lang]),
                A(attribute[lang]),
                meeting,
                DT(date).dOpt(dateOptions)).t(tense(date,today))))

if __name__ == "__main__":
    loadEn();print(DT(today).dOpt(dateOptions),"\n")
    for (i,day) in zip(range(1,len(participants)+1),
                       [today-timedelta(days=1),today,today+timedelta(days=1)]):
        report(participants[:i], day,"en")
        report(participants[:i], day,"fr")
        print("--")
        # use Realizer subclasses on the reversed lists
        English().report(participants[::-1][:i],day)
        Francais().report(participants[::-1][:i], day)
        print("====")


'''  output:
on Monday, September 18, 2023 at 2 p.m. 

Alice was present at the pyrealb meeting on Sunday, September 17, 2023 at 2 p.m.
Alice fut présente à la réunion pyrealb le dimanche 17 septembre 2023 à 14 h. 
--
Bob attended the pyrealb meeting on Sunday, September 17, 2023 at 2 p.m.
Bob fut présent à la réunion pyrealb le dimanche 17 septembre 2023 à 14 h. 
====
Alice and Eve are present at the pyrealb meeting on Monday, September 18, 2023 at 2 p.m.
Alice et Eve sont présentes à la réunion pyrealb le lundi 18 septembre 2023 à 14 h. 
--
Bob and Eve attend the pyrealb meeting on Monday, September 18, 2023 at 2 p.m.
Bob et Eve sont présents à la réunion pyrealb le lundi 18 septembre 2023 à 14 h. 
====
Alice, Eve and Bob will be present at the pyrealb meeting on Tuesday, September 19, 2023 at 2 p.m.
Alice, Eve et Bob seront présents à la réunion pyrealb le mardi 19 septembre 2023 à 14 h. 
--
Bob, Eve and Alice will attend the pyrealb meeting on Tuesday, September 19, 2023 at 2 p.m.
Bob, Eve et Alice seront présents à la réunion pyrealb le mardi 19 septembre 2023 à 14 h. 
====
'''