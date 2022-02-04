from context import pyrealb
from pyrealb.all import *

max=6

def kmsapied(n):
    return NP(NO(n).dOpt({"nat": True}), N('kilomètre'),
              PP(P("à"), NP(N("pied"))))

def refrain():
    print(S(NP(D("le"),N("peinture"),
                        PP(P("à"),D("le"),N("huile"))).a(","),
                     S(Pro("ce"), VP(V("être").t("p"),Adv("bien"),A("difficile")))))
    print(S('mais',
                     Pro("ce"),
                     VP(V("être").t("p"),
					    AdvP(Adv("bien"),A("beau").f("co")),
                        SP(Pro("que"),
                           NP(D("le"),N("peinture"),
                           PP(P("à"),D("le"),N("eau")) ) ) )
                       ))

def couplet(i):
    ca_use=lambda:SP(Pro("ça"),V("user"))
    souliers=S(ca_use(),NP(D("le"),N("soulier").n("p")))
    kmap=kmsapied(i).a(",")
    print(S(kmap,ca_use().a(","),ca_use()))
    print(S(CP(kmap,souliers)))
    refrain()
    print()

if __name__ == '__main__':
    loadFr()
    for i in range(1,max):
        couplet(i)