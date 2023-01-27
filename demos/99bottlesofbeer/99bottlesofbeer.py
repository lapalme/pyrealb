from context import pyrealb
from pyrealb import *

max = 99

def nbb(n): # (n  no more) bottle(s) of beer
    b=N("bottle")
    ob=PP(P("of"),N("beer"))
    if n==0:
        return NP("no more", b.n("p"), ob)
    return NP(NO(n).nat(true), b, ob)

def nbbW(n): # n bottles of beer on the wall
    return NP(nbb(n),PP(P("on"),D("the"),N("wall")))

def verse(n):
    print(S(CP(nbbW(n),nbb(n))))
    if n>0:
        print(S(CP(C("and"),
                   VP(V("take").pe(2).t("ip"),NO(1).nat(true),P("down")),
                   VP(V("pass").pe(2),Pro("I").g("n").pe(3),P("around")).a(","),
                   nbbW(n-1))))
    else:
        print(S(CP(C("and"),
                   VP(V("go").pe(2),PP(P("to"),D("a"),N("store"))),
                   VP(V("buy").pe(2),"some more"),
                   nbbW(max))))

if __name__ == '__main__':
    loadEn()
    Constituent.debug = False
    for n in range(max,-1,-1):
        verse(n)
        print()
