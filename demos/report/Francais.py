from Realizer import Realizer
from pyrealb import *

class Francais(Realizer):
    def __init__(self):
        loadFr()
        self.and_conj = C("et")
        super().__init__()

    def report(self, event, persons, date):
        loadFr()
        super().report(event, persons, date)

    def attend(self,meeting):
        return VP(V("être"),A("présent"),PP(P("à"),meeting))

    def individual(self):
        return N("individu")

    def meeting(self,noun):
        return NP(D("le"), N(noun))