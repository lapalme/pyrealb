from Realizer import Realizer
from pyrealb import *

class English(Realizer):
    def __init__(self):
        loadEn()
        self.and_conj = C("and")
        super().__init__()

    def report(self, event, persons, date):
        loadEn()
        super().report(event, persons, date)

    def attend(self,meeting):
        return VP(V("attend"),meeting)

    def individual(self):
        return N("person")

    def meeting(self,noun):
        return NP(D("the"), N(noun))