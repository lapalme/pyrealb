# from pyrealb import *
from pyrealb import Constituent, Terminal,N,A,Pro,D,Adv,V,P,C,DT,NO,Q, Phrase,NP,AP,VP,AdvP,PP,CP,S,SP,\
    loadEn,loadFr,addToLexicon, getLemma,\
    oneOf, fromJSON, pyRealB_version, true, false, null

from Realization.common import realize, jsrDayPeriod

sky_condition_terminology = { ## types of sky conditions
    "c1":{"en":(lambda:AP(A("sunny")),lambda:AP(A("clear"))),
          "fr":(lambda:AP(A("ensoleillé")),lambda:AP(A("dégagé")))},
    "c2":{"en":(lambda:AP(Adv("mainly"),A("sunny")),lambda:NP(Q("a"),D("few"),N("cloud").n("p"))),
          "fr":(lambda:AP(Adv("généralement"),A("ensoleillé")),lambda:NP(D("quelque"),N("nuage").n("p")))},
    "c3":{"en":(lambda:NP(D("a"),N("mix"),PP(P("of"),CP(C("and"),N("sun"),N("cloud").n("p")))),
                lambda:AP(Adv("partly"),A("cloudy"))),
          "fr":(lambda:NP(N("alternance"),CP(C("et"),PP(P("de"),N("soleil")),PP(P("de"),N("nuage").n("p")))),
                lambda:AP(Adv("partiellement"),A("couvert")))},
    "c4":{"en":(lambda:AP(Adv("mainly"),A("cloudy")),),
          "fr":(lambda:AP(Adv("généralement"),A("nuageux")),)},
    "c5":{"en":(lambda:AP(A("cloudy")),),
          "fr":(lambda:AP(A("nuageux")),)},
    "c6":{"en":(lambda:AP(A("overcast")),),
          "fr":(lambda:AP(A("couvert")),)},
    "c7":{"en":(lambda:NP(V("increase").t("pr"),N("cloudiness")),),
          "fr":(lambda:NP(N("ennuagement")),)},
    "c8":{"en":(lambda:NP(N("clearing")),),
          "fr":(lambda:NP(N("dégagement")),)},
}

def sky_condition(mc,period,lang):
    previous_conditions=[]
    jsrExprs=[]

    def addNoRepeat(c,dn,period=None): # avoid generating same sentence twice
        if c not in previous_conditions:
            if len(sky_condition_terminology[c][lang])==1:dn=0
            jsrExpr=sky_condition_terminology[c][lang][dn]()
            if period!=None:jsrExpr.add(period)
            jsrExprs.append(jsrExpr)
            previous_conditions.append(c)
            
    sc_terms=mc.get_sky_cover(period)
    if sc_terms is None: return None
    for sc_term in sc_terms:
        valStart=sc_term.infos[0]
        valEnd  =sc_term.infos[1]
        dayNight = 0 if period in ["today","tomorrow"] else 1
        if valStart==valEnd:
            if valStart in [0,1]:
                addNoRepeat("c1",dayNight)
            if valStart in [2,3]:
                addNoRepeat("c2",dayNight)
            if valStart in [4,5,6]:
                addNoRepeat("c3",dayNight)
            if valStart in [7,8]:
                addNoRepeat("c4",dayNight)
            if valStart in [9]:
                addNoRepeat("c5",dayNight)
            if valStart in [10]:
                addNoRepeat("c6",dayNight)
        elif valStart in [0,1,2,3] and valEnd in [7,8,9,10]:
            addNoRepeat("c7",dayNight,jsrDayPeriod(sc_term.start,lang))
        elif (valStart in [7,8,9,10] and valEnd in [0,1,2,3]) or \
             (valStart in [5,6]      and valEnd in [0,1]):
            addNoRepeat("c8",dayNight,jsrDayPeriod(sc_term.start,lang))
    return " ".join(realize(jsrExpr,lang) for jsrExpr in jsrExprs)


if __name__ == '__main__':
    ## exercise all sky_condition_terminology expressions
    for c in sky_condition_terminology:
        for lang in ["en","fr"]:
            {"en":loadEn,"fr":loadFr}[lang]()
            jsrExprs=sky_condition_terminology[c][lang]
            for jsrExpr in jsrExprs:
                print(realize(jsrExpr(),lang))
