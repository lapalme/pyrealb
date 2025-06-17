from pyrealb import *

class English_lang:
    def __init__(self):
        self.code = "en"
        load(self.code)
        # vocabulary
        self.conj = lambda:C("and")
        self.individual = lambda:N("person")

    def attend(self,meeting):
        return VP(V("attend"),meeting)

    def meeting(self,noun):
        return NP(D("the"),N(noun))
