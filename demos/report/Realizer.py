from datetime import datetime
from pyrealb import *

# language independent realization algorithm
class Realizer:
    today    = datetime.today()
    dateOptions = {"minute": False, "second": False}

    # compare day of date with the day of the reference
    def tense(self,date, reference):
        o = date.toordinal()
        ref_o = reference.toordinal()
        return "p" if o == ref_o else "f" if o > ref_o else "ps"

    def report(self,names,date):
        print(S(self.conjunction([N(name) for name in names]),
                self.attend(self.meeting()),
                DT(date).dOpt(Realizer.dateOptions))
                    .t(self.tense(date,Realizer.today)))
