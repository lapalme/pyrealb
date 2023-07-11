from pyrealb import NO, NP, N, DT, Q, currentLanguage
class Realizer:
    # output number in letters if 12 or less
    def no(self,val):
        return NO(val).dOpt({"nat": val < 13})

    def nb(self,val,n):
        return NP(self.no(val),N(n) if isinstance(n,str) else n)

    def on_day(self,date):
        return DT(date).dOpt({"nat":   True, "hour": False, "minute": False, "second": False,
                              "month": False, "date": False, "year": False,
                              "det": currentLanguage()=="en"})

    def pts(self,val1,val2,postfix=None):
        return NP(NO(val1).lier(),NO(val2),Q(postfix) if postfix is not None else None)