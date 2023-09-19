from Realizer import Realizer
from pyrealb import *

class Francais(Realizer):
    def __init__(self):
        loadFr()
        addToLexicon({"Alice":{ "N": { "g": "f", "tab": "nI" } }})
        addToLexicon({"Bob":{ "N": { "g": "m", "tab": "nI" } }})
        addToLexicon({"Eve":{ "N": { "g": "f", "tab": "nI" } }})
        addToLexicon({"pyrealb":{"A":{ "tab":"nI"}}})

    def conjunction(self,elems):
        return CP(C("et"),elems)

    def attend(self,meeting):
        return VP(V("être"),A("présent"),
                  PP(P("à"),meeting))

    def meeting(self):
        return NP(D("le"), A("pyrealb"), N("réunion"))