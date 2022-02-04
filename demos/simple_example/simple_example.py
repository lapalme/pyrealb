from context import pyrealb

from pyrealb.Lexicon import *
from pyrealb.Terminal import *
from pyrealb.Phrase import *
from pyrealb.utils import *


def english():
    # a few examples generates warnings shown here as comments
    loadEn()
    print(V("reserve").t(""))  # V('reserve'):: : this bad value for option t is ignored.
    print(N())  # N(None):: the parameter should be string, not NoneType.
    print(DT())
    print(DT(datetime.datetime.today()).dOpt({'rtime': True}))
    print(DT(None).dOpt({"det": False}))
    s = lambda: S(Pro("I").pe(1),
                  VP(V("say").t("ps"),
                     NP(N("hello"),
                        PP(P("to"), NP(D("the"), N("world").n("p")))))).typ({"pas": False, "neg": True})
    print(S(NP(D("a"), N("cat").n("p"))))
    print(s())
    sJson = s().toJSON()
    import json
    json.dump(sJson, sys.stdout, indent=3)
    print()
    s1 = fromJSON(s().toJSON())
    print(s1)


def francais():
    loadFr()
    print(S(NP(D("le"), N("chat")).n("p"), VP(V("asseoir"))).typ({"refl": True}).realize())
    addToLexicon({"John": {"N": {"g": "m", "tab": "n35"}}})
    addToLexicon({"Mary": {"N": {"g": "f", "tab": "n36"}}})

    print(S(NP(D("le"), N("chat")),
            VP(V("manger"),
               NP(D("le"), N("souris")))).typ({'int': 'yon', 'neg': true}).realize()
          )
    print(S(Pro("lui").c('nom').pe(3).g('m').n('s'),
            VP(V("donner").t('pc'), NP(D("un"), N("pomme")).pro(),
               PP(P("à"), NP(D("le"), N("fille"))).pro())
            ).typ({'neg': False, 'pas': True}).realize())
    print(VP(V("aller").t("pc").pe(2).n("p")).typ(1))
    print(S(Pro("moi").c("nom").pe(3).n("p"), VP(Pro("eux").c('refl'), V("évanouir").t('pc'))).typ({"neg": True}))
    print(S(CP(C("et"), NP(N("John")), NP(N("Mary"))), VP(V("évanouir").t('pc'))).typ({"neg": True, "refl": True}))
    print(S(Pro("je").pe(1).n('p'),
            VP(V("agir").t('p'),
               AdvP(Adv("conformément"),
                    PP(P("à"), NP(D("le"), N("loi"))))).typ({'neg': True})))
    print(S(Pro("lui").c("nom"),
            VP(V("parler").t("pc"),
               PP(P("à"), NP(D("mon"), N("ami"))).pro(),
               PP(P("de"), NP(D("mon"), N("problème"))).pro())))
    print(S(NP(D("un"), N("garçon").g("f")),
            VP(V("travailler"),
               PP(P("sur"), N("internet")))).typ({"neg": True}))
    # print(V("cliquer").t("pc").pe(1))
    print(V("repentir").t('p').pe(2).n('s').lier())
    print(V("repentir").t('ip').pe(2).n('s').lier())
    # print(PP(P("sur"),N("internet")))
    print(S(NP(D("un"), N("garçon").g("f")),
            # erreur de morphologie : genre différent de celui du lexique N('garçon') :{'g': 'f', 'lexique': 'm'}.
            VP(V("travailler"),
               PP(P("sur"), N("internet")))))
    print(S(NP(D("le"), N("élève").g('f')),
            VP(Pro("moi").pe(1).c('dat'), V("dire"),
               PP(P("de"), VP(V("interroger").t('b'),
                              NP(D("le"), N("élève").g('f')).pro(None))
                  .typ({'neg': True})))).realize())
    print(VP(V("aimer").t("ip").pe(2).n("s")).typ({"refl": True}).realize())
    print(S(Pro("je").pe(2), VP(V("enfuir"))).realize())
    print(S(Pro("je").pe(2).n("p"), VP(V("laver").t("pc"))).typ({"refl": True}).realize())
    print(S(Pro("je").pe(2), VP(V("savoir"))).typ({"pas": True}).realize())
    print(S(NP(D("le"), N("chat")), VP(V("manger"))).typ({"pas": True}))
    print(oneOf([lambda: N("amour"), lambda: N("amitié")]))
    print(oneOf([lambda: N("amour"), lambda: N("amitié")]))
    print(oneOf(lambda: N("amitié")))
    print(oneOf(lambda: N("amour"), lambda: N("amitié")))
    print(NO(4).nat())
    print(NO(4).dOpt({"nat": True}))
    print(D("un", "B"))  # D('un'):: langage devrait être  "en" ou  "fr" , ce sera fr.
    c = lambda: NP(D("un"), N("chat"))
    print(c())

    s = CP(C("et"), NP(NO("1").nat(True), N("consultation")), NP(NO("2").nat(True), N("atelier")))
    print(s.toSource())
    print(s)
    print(DT(None))
    print(DT("").dOpt({"det": False}))
    print(S(NP(D("le"),
               N("rat").n("p"),
               SP(Pro("que"),
                  NP(D("le"),
                     N("chat").g("f").n('p')),
                  VP(V("manger").t('pc')))),
            VP(V("être").t('p'),
               AP(A("gris")))))


english()
francais()
