from pyrealb import *

class Francais_lang:
    def __init__(self):
        self.code = "fr"
        load(self.code)
        # vocabulary
        self.conj = lambda:C("et")
        self.individual = lambda:N("individu")

    def attend(self, meeting):
        return VP(V("être"), A("présent"), PP(P("à"), meeting))

    def meeting(self,noun):
        return NP(D("le"), N(noun))

