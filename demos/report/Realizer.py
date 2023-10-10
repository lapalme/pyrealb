from datetime import datetime
from pyrealb import *

# language independent realization algorithm
class Realizer:
    def __init__(self): # called by __init__() in subclasses after setting the language
        addToLexicon({"Alice":{ "N": { "g": "f", "tab": "nI" } }})
        addToLexicon({"Bob":{ "N": { "g": "m", "tab": "nI" } }})
        addToLexicon({"Eve":{ "N": { "g": "f", "tab": "nI" } }})

    today    = datetime.today()
    dateOptions = {"minute": False, "second": False}

    # compare day of date with the day of the reference
    def tense(self,date, reference):
        o = date.toordinal()
        ref_o = reference.toordinal()
        return "p" if o == ref_o else "f" if o > ref_o else "ps"

    def report(self,event,persons,date):
        print(S(CP(self.and_conj,[N(person) for person in persons]),
                NP(NO(len(persons)).nat(), self.individual()).ba("("),
                self.attend(self.meeting(event)),
                DT(date).dOpt(Realizer.dateOptions))
                    .t(self.tense(date,Realizer.today)))
