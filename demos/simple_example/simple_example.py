from context import pyrealb
from pyrealb import *
import datetime, sys

def show(exp):
    print(exp.realize())

## some examples that were used during development

def english():
    # a few examples generates warnings shown here as comments
    loadEn()
    exp=S(CP(C("and"),NP(D("the"),N("apple"))),        # 13
          VP(V("be"),A("good")))
    print(exp.toDependent().toSource(0))
    show(exp.toDependent())
    # sys.exit(0)
    exp=S(Pro("him").c("nom"),
       VP(V("eat"),                                 # 11
          NP(D("a"),N("apple").n("p"))
          .add(A("red")))).add(Adv("now").a(","),0)
    print(exp.toDependent().toSource(0))
    show(exp.toDependent())
    show(root(V("eat"),subj(Pro("him").c("nom"))).add(comp(Adv("now")).a(',').pos("pre")))
    show(root(V("eat"),
               comp(N("apple").n('p'),
                    det(D("a"))).add(mod(A("red"))),
               subj(Pro("him").c('nom'))).add(comp(Adv("now")).a(',').pos("pre")))
    show(S(Pro("him").c("nom"),                      # 20
         VP(V("eat"),
            NP(D("a"), N("apple").tag("a", {"href":"https:#en.wikipedia.org/wiki/Apple"})))).clone())
    show(S(CP(C("and"), NP(D("the"), N("apple"))), VP(V("be"), A("good"))))
    show(V("reserve").t(""))  # V('reserve'):: : this bad value for option t is ignored.
    show(N())  # N(None):: the parameter should be string, not NoneType.
    show(DT())
    show(DT(datetime.datetime.today()).dOpt({'rtime': True}))
    show(DT("2021-09-01").dOpt({"rtime": "2021-08-27","hour":false,"minute":false,"second":false}))
    show(DT().dOpt({'rtime': datetime.datetime.today()-datetime.timedelta(days=4)}))
    show(DT(datetime.datetime.today()-datetime.timedelta(days=5)).dOpt({'rtime': True}))
    show(DT(None).dOpt({"det": False}))
    s = lambda: S(Pro("I").pe(1),
                  VP(V("say").t("ps"),
                     NP(N("hello"),
                        PP(P("to"), NP(D("the"), N("world").n("p")))))).typ({"pas": False, "neg": True})
    show(S(NP(D("a"), N("cat").n("p"))))
    show(s())
    sJson = s().toJSON()
    import json
    json.dump(sJson, sys.stdout, indent=3)
    print()
    s1 = fromJSON(s().toJSON())
    show(s1)
    show(S(Pro("him").c("nom"),
         VP(V("eat"),
            NP(D("a"),N("apple").n("p")).tag("em")
       )).typ({"int":"tag"}))
    show(S(Pro("him").c("nom"),
         VP(V("eat"),
            NP(D("a"),N("apple").n("p")).tag("em")
       )).typ({"int":"tag","neg":True}))
    show(S(Pro("him").c("nom"),
         VP(V("eat").t("c"),
            NP(D("a"),N("apple").n("p")).tag("em")
       )).typ({"int":"tag"}))

def francais():
    loadFr()
    exp=S(Pro("je"),
        VP(V('manger').t("pc"),
           NP(D('le'),
              N('fromage')))).typ({"int":"tag"})
    show(exp)
    show(S(Pro("moi").pe(1),VP(V("aimer"))).typ({"pas":True}))
    show(S(NP(D("le"), N("chat")).n("p"), VP(V("asseoir"))).typ({"refl": True}))
    addToLexicon({"John": {"N": {"g": "m", "tab": "n35"}}})
    addToLexicon({"Mary": {"N": {"g": "f", "tab": "n36"}}})

    show(S(NP(D("le"), N("chat")),
            VP(V("manger"),
               NP(D("le"), N("souris")))).typ({'int': 'yon', 'neg': true})
          )
    show(S(Pro("lui").c('nom').pe(3).g('m').n('s'),
            VP(V("donner").t('pc'), NP(D("un"), N("pomme")).pro(),
               PP(P("à"), NP(D("le"), N("fille"))).pro())
            ).typ({'neg': False, 'pas': True}))
    show(VP(V("aller").t("pc").pe(2).n("p")).typ(1)) # VP(V('aller')):: int:1 : cette mauvaise valeur pour l'option .typ est ignorée
    show(S(Pro("moi").c("nom").pe(3).n("p"), VP(Pro("eux").c('refl'), V("évanouir").t('pc'))).typ({"neg": True}))
    show(S(CP(C("et"), NP(N("John")), NP(N("Mary"))), VP(V("évanouir").t('pc'))).typ({"neg": True, "refl": True}))
    show(S(Pro("je").pe(1).n('p'),
            VP(V("agir").t('p'),
               AdvP(Adv("conformément"),
                    PP(P("à"), NP(D("le"), N("loi"))))).typ({'neg': True})))
    show(S(Pro("lui").c("nom"),
            VP(V("parler").t("pc"),
               PP(P("à"), NP(D("mon"), N("ami"))).pro(),
               PP(P("de"), NP(D("mon"), N("problème"))).pro())))
    show(S(NP(D("un"), N("garçon").g("f")), #N('garçon'):: erreur de morphologie : genre différent de celui du lexique N('garçon') :{'g': 'f', 'lexique': 'm'}
            VP(V("travailler"),
               PP(P("sur"), N("internet")))).typ({"neg": True}))
    # show(V("cliquer").t("pc").pe(1))
    show(V("repentir").t('p').pe(2).n('s'))
    show(V("repentir").t('ip').pe(2).n('s').lier())
    # show(PP(P("sur"),N("internet")))
    show(S(NP(D("un"), N("garçon").g("f")),
            # erreur de morphologie : genre différent de celui du lexique N('garçon') :{'g': 'f', 'lexique': 'm'}.
            VP(V("travailler"),
               PP(P("sur"), N("internet")))))
    show(S(NP(D("le"), N("élève").g('f')),
            VP(Pro("moi").pe(1).c('dat'), V("dire"),
               PP(P("de"), VP(V("interroger").t('b'),
                              NP(D("le"), N("élève").g('f')).pro(None))
                  .typ({'neg': True})))))
    show(VP(V("aimer").t("ip").pe(2).n("s")).typ({"refl": True}))
    show(S(Pro("je").pe(2), VP(V("enfuir"))))
    show(S(Pro("je").pe(2).n("p"), VP(V("laver").t("pc"))).typ({"refl": True}))
    show(S(Pro("je").pe(2), VP(V("savoir"))).typ({"pas": True}))
    show(S(NP(D("le"), N("chat")), VP(V("manger"))).typ({"pas": True}))
    show(oneOf([lambda: N("amour"), lambda: N("amitié")]))
    show(oneOf([lambda: N("amour"), lambda: N("amitié")]))
    show(oneOf(lambda: N("amitié")))
    show(oneOf(lambda: N("amour"), lambda: N("amitié")))
    show(NO(4).nat())
    show(NO(4).dOpt({"nat": True}))
    show(D("un", "B"))  # D('un'):: langage devrait être  "en" ou  "fr" , ce sera fr.
    c = lambda: NP(D("un"), N("chat"))
    show(c())

    s = CP(C("et"), NP(NO("1").nat(True), N("consultation")), NP(NO("2").nat(True), N("atelier")))
    print(s.toSource())
    show(s)
    show(DT(None))
    show(DT("").dOpt({"det": False}))
    show(S(NP(D("le"),
               N("chat").n("p"),
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

    show(root(N("test")))
    show(V("repentir").t('p').pe(1).n('s'))
    show(root(V("manger").t("pc"),
                  subj(N("souris"),
                       det(D("le"))),
                  comp(N("fromage"),
                       det(D("le")))).typ({"int": "wad", "pas": true}))
    show(root(V("manger").t("pc"),
                  subj(N("souris"),
                       det(D("le"))),
                  comp(N("fromage"),
                       det(D("le")))).typ({"int": "tag"}))
    show(root(V('demander').t("pc"),
                  comp(N('adresse'),
                       det(D('mon'))).pro(),
                  comp(P('à'),
                       mod(N('parent').n("p"),
                           det(D('mon')))).pro(),
                  subj(Pro('je').pe(2))))
    show(root(V("manger").t("f"),
               subj(N("chat"),
                    det(D("le"))).n("p"),
               comp(N("souris"),
                    det(D("un")))).typ({"neg":True}))
    show(root(V('être').t("p"),
               comp(A('gris')),
               subj(N('souris'),
                    det(D('le')),
                    mod(V('manger').t("pc"),
                        comp(Pro('que')).pos("pre"),
                        subj(N('chat').n("p"),
                             det(D('le')))))))
    show(root(N('cadeau').n("p"),
                 mod(A('beau'))))
    show(root(N('gens').n("p"),
                 det(D('le')),
                 mod(A('vulgaire').pos("pre"))).cap(false))
    show(root(N('père'),
                 det(D('le')),
                 mod(P('de'),
                     mod(N('fille'),
                         det(D('mon').pe(1))))))
    show(root(V('manger'),
                 comp(N('gâteau'),
                      det(D('le'))),
                 subj(N('enfant').n("p"),
                      det(D('le'))).pro()))
    show(root(V('manger'),
                 comp(N('gâteau'),
                      det(D('le'))).pro(),
                 subj(N('enfant').n("p"),
                      det(D('le')))))
    show(root(V('manger'),
                 comp(N('gâteau'),
                      det(D('le'))),
                 subj(N('enfant').n("p"),
                      det(D('le')))).typ({"pas":True}))
    show(root(V('venir').t("pc"),
             comp(Adv('hier')),
             coord(C('et'),
                   subj(N('fruit'),
                        det(D('le')))).add(pommeS).add(gars)))

def dependent_en():
    loadEn()
    # show(root(V("run"),subj(N("cat"),det(D("the"))).pro()))
    show(root(V("play").t("f"),
                           subj(N("cat"),det(D("a"))),
                           comp(N("piano"))).typ({"neg":true}))
    show(root(V("sit").t("ps"),
              subj(N("cat"),det(D("the"))),
              comp(P("on"),mod(N("couch"),det(D("the"))))))
    show(root(V("sit").t("ps"),
              subj(N("cat"),det(D("the"))),
              comp(P("on"),mod(N("couch"),det(D("the"))))).typ({"int":"tag"}))
    show(root(V("sit").t("ps"),
              subj(N("cat"),det(D("the"))),
              comp(P("on"),mod(N("couch"),det(D("the"))))).typ({"int":"tag","perf":true}))
    show(root(V("like").t("pr"),
               subj(N("dog").n("p"),mod(A("nice"))),
               comp(N("cat"),
                    det(D("a"))).n("p")))
    show(root(V('love'),
                 comp(N('woman'),
                      det(D('a'))).pro(),
                 subj(Pro('I').g("m"))))
    s = lambda: root(V("say").t("ps"),
                     subj(Pro("I").pe(1)),
                     comp(N("bye")),
                     comp(P("to"),
                          mod(N("world"),
                              det(D("the"))))).typ({"pas": False, "neg": True})
    show(s())
    sJson = s().toJSON()
    import json
    json.dump(sJson, sys.stdout, indent=3)
    print()
    s1 = fromJSON(s().toJSON())
    show(s1)

def dependentTransformation():
    s = lambda: S(Pro("I").pe(1),
                  VP(V("say").t("ps"),
                     NP(N("hello"),
                        PP(P("to"), NP(D("the"), N("world").n("p")))))).typ({"pas": False, "neg": True})
    print(s().toDependent().toSource(0))
    show(s().toDependent())

## test a single expression (useful for launching the debugger on a given expression
## proper language must be chosen before calling... because the parameter is evaluated before the function call
def test(exp):
    print(exp.toSource(0))
    print(exp.realize())

# test_warnings()

def testPrevious():
    print("** English **")
    english()
    print("======")
    print("** Français **")
    francais()
    print("======")
    print("** Dépendances françaises **")
    dependent_fr()
    print("======")
    print("** English dependencies **")
    dependent_en()
    print("======")
    dependentTransformation()

    # check list of list of parameters for Phrase
    loadEn()
    test(S(NP(D("the"),[N("cat"),A("white")],VP([V("sit"),[PP(P("on"),[NP(D("the"),N("mat"))])]]))))
    # check position of an adjective
    test(NP(oneOf(N("family").lier(),N("kid")),A("friendly").pos("post")))

    loadFr()
    test(NP(N("chat"),A("blanc").pos("pre")))
    test(NP(N("chat"),A("petit")))
    test(NP(N("chat"),A("noir")))

    loadEn()
    test(root(V("be").t("p"),
             subj(Pro("I").n("s").pe(1)),
                comp(P("on"),mod(N("couch"),det(D("the"))))).typ({"int":"tag","perf":True}))
    test(S(Pro("I").pe(1),VP(V("be"),PP(P("on"),NP(D("the"),N("couch"))))).typ({"int":"tag"}))

    test(S(VP(V("go").t("b"))).typ({"neg":True}))
    test(S(VP(V("go").t("b-to"))).typ({"neg":True}))
    test(V("love").t("ip").pe(1).n("p"))
    test(S(Pro("I").n("p"),VP(V("answer").t("c"))))

    addToLexicon("John", {"N": {"tab": "nI", "g": "m"}})
    addToLexicon("Mary", {"N": {"tab": "nI", "g": "f"}})
    addToLexicon("Fred", {"N": {"tab": "nI", "g": "m"}})
    addToLexicon("Maria-Luz", {"N": {"tab": "nI", "g": "f"}})
    addToLexicon("firefighter", getLemma("fighter"))
    # test(root(V("like"),comp(N("John")),subj(N("Mary"))).typ({'int': 'wod'}))

    test(coord(C("but"),root(V("laugh").t('ps'),subj(N("John"))),
                        root(V("smack").t('ps'),subj(N("Mary")),
                             coord(C("and"),comp(N("butler"),det(D("the"))),
                                   comp(N("maid"),det(D("the")))))))
    loadFr()
    test(PP(P("de"),NO(8).nat()))
    test(V("asseoir").t("pp").n("p"))

    loadFr()
    test(S(NP(D("le"), N("chat")).n("p"),
             VP(V("asseoir").t("pc"),
                PP(P("sur"),
                   NP(D("le"), N("tapis"))))).typ({"int": "tag", "neg": True, "refl": True}))
    test(V("asseoir").t("pc").pe(3).n("p").tag("em"))

    loadEn()
    en1 = NP(D("the"), N("cat").n("p"))
    en2 = NP(D("a"), N("mat")).n("p")
    loadFr()
    test(S(en1,
             VP(V("asseoir").t("pc").tag("em"),
                PP(P("sur").tag("em"),
                   en2))).typ({"refl": true, "int": "tag"}))

    test(S(Pro("ce"),V("être").t("pc")))

    loadEn()
    test(S(V("show").t("ip"),
                     NP(D("a"),N("airline").n("p"),
                        SP(Pro("that"),
                           VP(V(oneOf("fly","go")))))))

if __name__ == '__main__':
    testPrevious()
    # insert here a single example for debugging perhaps commenting the line above
