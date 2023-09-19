from Realizer import Realizer
from pyrealb import *

class English(Realizer):
    def __init__(self):
        loadEn()
        addToLexicon({"Alice":{ "N": { "g": "f", "tab": "nI" } }})
        addToLexicon({"Bob":{ "N": { "g": "m", "tab": "nI" } }})
        addToLexicon({"Eve":{ "N": { "g": "f", "tab": "nI" } }})
        addToLexicon({"pyrealb":{"A":{ "tab":"nI"}}})

        self.prep = "at"
        self.det  = "the"
        self.meet = "meeting"
        self.copula = "be"
        self.attribute = "present"

    def conjunction(self,elems):
        return CP(C("and"),elems)

    def attend(self,meeting):
        return VP(V("attend"),meeting)

    def meeting(self):
        return NP(D("the"), A("pyrealb"), N("meeting"))