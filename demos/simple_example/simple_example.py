from context import pyrealb
from pyrealb import *
import datetime, sys

## some examples that were used during development

def english():
    # a few examples generates warnings shown here as comments
    loadEn()
    exp=S(CP(C("and"),NP(D("the"),N("apple"))),        # 13
          VP(V("be"),A("good")))
    print(exp.toDependent().toSource(0))
    print(exp.toDependent())
    # sys.exit(0)
    exp=S(Pro("him").c("nom"),
       VP(V("eat"),                                 # 11
          NP(D("a"),N("apple").n("p"))
          .add(A("red")))).add(Adv("now").a(","),0)
    print(exp.toDependent().toSource(0))
    print(exp.toDependent())
    print(root(V("eat")).add(Adv("now").a(','),0))
    print(root(V("eat"),
               comp(N("apple").n('p'),
                    det(D("a")),
                    mod(A("red")).pos('pre')).add(A("red")),
               subj(Pro("him").c('nom')),
               mod(Adv("now").a(','))).add(Adv("now").a(','),0))
    print(S(Pro("him").c("nom"),                      # 20
         VP(V("eat"),
            NP(D("a"), N("apple").tag("a", {"href":"https:#en.wikipedia.org/wiki/Apple"})))).clone(globals()))
    print(S(CP(C("and"), NP(D("the"), N("apple"))), VP(V("be"), A("good"))))
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
    print(S(Pro("him").c("nom"),
         VP(V("eat"),
            NP(D("a"),N("apple").n("p")).tag("em")
       )).typ({"int":"tag"}).realize())
    print(S(Pro("him").c("nom"),
         VP(V("eat"),
            NP(D("a"),N("apple").n("p")).tag("em")
       )).typ({"int":"tag","neg":True}).realize())
    print(S(Pro("him").c("nom"),
         VP(V("eat").t("f"),
            NP(D("a"),N("apple").n("p")).tag("em")
       )).typ({"int":"tag"}).realize())

def francais():
    loadFr()
    exp=S(Pro("je"),
        VP(V('manger').t("pc"),
           NP(D('le'),
              N('fromage')))).typ({"int":"tag"})
    print(exp.realize())
    print(S(Pro("moi").pe(1),VP(V("aimer"))).typ({"pas":True}).realize())
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

def dependent_fr():
    loadFr()
    pommeS = subj(N("pomme"),det(D("le")))
    gars = subj(N("garçon").n("p"),det(D("le")))
    addToLexicon({"John":{"N":{"g":"m","tab":"n4"}}})
    addToLexicon({"Mary":{"N":{"g":"f","tab":"n16"}}})

    print(root(N("test")))
    print(V("repentir").t('p').pe(1).n('s').realize())
    print(root(V("manger").t("pc"),
                  subj(N("souris"),
                       det(D("le"))),
                  comp(N("fromage"),
                       det(D("le")))).typ({"int": "wad", "pas": true}).realize())
    print(root(V("manger").t("pc"),
                  subj(N("souris"),
                       det(D("le"))),
                  comp(N("fromage"),
                       det(D("le")))).typ({"int": "tag"}).realize())
    print(root(V('demander').t("pc"),
                  comp(N('adresse'),
                       det(D('mon'))).pro(),
                  comp(P('à'),
                       mod(N('parent').n("p"),
                           det(D('mon')))).pro(),
                  subj(Pro('je').pe(2))).realize())
    print(root(V("manger").t("f"),
               subj(N("chat"),
                    det(D("le"))).n("p"),
               comp(N("souris"),
                    det(D("un")))).typ({"neg":True}).realize())
    print(root(V('être').t("p"),
               comp(A('gris')),
               subj(N('souris'),
                    det(D('le')),
                    mod(V('manger').t("pc"),
                        comp(Pro('que')).pos("pre"),
                        subj(N('chat').n("p"),
                             det(D('le')))))))
    print(root(N('cadeau').n("p"),
                 mod(A('beau'))))
    print(root(N('gens').n("p"),
                 det(D('le')),
                 mod(A('vulgaire').pos("pre"))).cap(false))
    print(root(N('père'),
                 det(D('le')),
                 mod(P('de'),
                     mod(N('fille'),
                         det(D('mon').pe(1))))))
    print(root(V('manger'),
                 comp(N('gâteau'),
                      det(D('le'))),
                 subj(N('enfant').n("p"),
                      det(D('le'))).pro()))
    print(root(V('manger'),
                 comp(N('gâteau'),
                      det(D('le'))).pro(),
                 subj(N('enfant').n("p"),
                      det(D('le')))))
    print(root(V('manger'),
                 comp(N('gâteau'),
                      det(D('le'))),
                 subj(N('enfant').n("p"),
                      det(D('le')))).typ({"pas":True}))
    print(root(V('venir').t("pc"),
             comp(Adv('hier')),
             coord(C('et'),
                   subj(N('fruit'),
                        det(D('le')))).add(pommeS).add(gars)))

def dependent_en():
    loadEn()
    # print(root(V("run"),subj(N("cat"),det(D("the"))).pro()).realize())
    print(root(V("play").t("f"),
                           subj(N("cat"),det(D("a"))),
                           comp(N("piano"))).typ({"neg":true}).realize())
    print(root(V("sit").t("ps"),
              subj(N("cat"),det(D("the"))),
              comp(P("on"),mod(N("couch"),det(D("the"))))))
    print(root(V("sit").t("ps"),
              subj(N("cat"),det(D("the"))),
              comp(P("on"),mod(N("couch"),det(D("the"))))).typ({"int":"tag"}).realize())
    print(root(V("sit").t("ps"),
              subj(N("cat"),det(D("the"))),
              comp(P("on"),mod(N("couch"),det(D("the"))))).typ({"int":"tag","perf":true}).realize())
    print(root(V("like").t("pr"),
               subj(N("dog").n("p"),mod(A("nice"))),
               comp(N("cat"),
                    det(D("a"))).n("p")))
    print(root(V('love'),
                 comp(N('woman'),
                      det(D('a'))).pro(),
                 subj(Pro('I').g("m"))))
    s = lambda: root(V("say").t("ps"),
                     subj(Pro("I").pe(1)),
                     comp(N("bye")),
                     comp(P("to"),
                          mod(N("world"),
                              det(D("the"))))).typ({"pas": False, "neg": True})
    print(s())
    sJson = s().toJSON()
    import json
    json.dump(sJson, sys.stdout, indent=3)
    print()
    s1 = fromJSON(s().toJSON())
    print(s1)

def dependentTransformation():
    s = lambda: S(Pro("I").pe(1),
                  VP(V("say").t("ps"),
                     NP(N("hello"),
                        PP(P("to"), NP(D("the"), N("world").n("p")))))).typ({"pas": False, "neg": True})
    print(s().toDependent().toSource(0))
    print(s().toDependent())

## test a single expression (useful for launching the debugger on a given expression
def test(exp,lang):
    loadEn() if lang=="en" else loadFr()
    print(exp.toSource(0))
    print(exp.realize())

# test_warnings()

# print("** English **")
# english()
# print("======")
# print("** Français **")
# francais()
# print("======")
# print("** Dépendances françaises **")
# dependent_fr()
# print("======")
# print("** English dependencies **")
# dependent_en()
# print("======")
# dependentTransformation()

# check list of list of parameters for Phrase
test(S(NP(D("the"),[N("cat"),A("white")],VP([V("sit"),[PP(P("on"),[NP(D("the"),N("mat"))])]]))),
     "en")

test(root(V("be").t("p"),
         subj(Pro("I").n("s").pe(1)),
            comp(P("on"),mod(N("couch"),det(D("the"))))).typ({"int":"yon","perf":False}),
     "en")
test(S(Pro("I").pe(1),VP(V("be"),PP(P("on"),NP(D("the"),N("couch"))))).typ({"int":"yon"}),"en")