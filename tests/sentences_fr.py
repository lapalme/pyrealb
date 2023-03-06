from context import pyrealb
from pyrealb import *
from test import test

def sentences_fr():
    loadFr()
    addToLexicon({"John":{"N":{"g":"m","tab":"n4"}}})
    addToLexicon({"Mary":{"N":{"g":"f","tab":"n16"}}})
    return [
        {}, # dummy 0
        # 1
        {"expression":S(
                    NP( D('le'),
                        N('souris'),
                        SP(Pro('que'),
                            NP(D('le'),
                                N('chat').n("p")),
                            VP(V('manger').t('pc')))),
                    VP( V('être').t('p'),
                        AP(A('gris')))
                ),
         "expected":"La souris que les chats ont mangée est grise. ",
         "message":"Phrase avec attribut, de plus le passé composé avec avoir est accordé correctement..."},
        # 2
        {"expression":S(N("cadeau").n("p")).cap(False),
         "expected":"cadeaux",
         "message":"Phrase sans capitale"},
        # 3
        {"expression":S(NP(A("beau"), N("cadeau").n("p"))),
         "expected":"Beaux cadeaux. ",
         "message":"Accord adjectif"},
        # 4
        {"expression":NP(D("le"),N("gens").n("p"),A("vulgaire").pos("pre")),
         "expected":"les vulgaires gens",
         "message":"Adjectif pré-posé"},
        # 5
        {"expression":S( NP(D("le"), N("père"), PP(P("de"), NP(D("mon").pe(1), N("fille")) ) )),
         "expected":"Le père de ma fille. ",
         "message":"Accord adjectif"},
        # 6
        {"expression":S(Pro("je").pe(1).n("p"), VP(V("agir").t("pc"), AdvP(Adv("conformément"), 
                      PP(P("à"), NP(D("le"), N("loi")))))).typ({"neg":True}),
         "expected":"Nous n'avons pas agi conformément à la loi. ",
         "message":"Phrase négative avec accord du verbe"},
        # 7
        {"expression":S(Pro("je").pe(2), VP(V("travailler").t("pc"),
                      AdvP(Adv("bien")))).typ({"mod":"nece"}),
         "expected":"Tu as dû bien travailler. ",
         "message":"Phrase au passé avec modalité de nécessité"},
        # 8
        {"expression":S(CP(C("et"), NP(D("le"), N("garçon")), NP(D("le"), N("fille"))), 
                      VP(V("être").t("p"),A("gentil"))),
         "expected":"Le garçon et la fille sont gentils. ",
         "message": "Coordination"},
        # 9
        {"expression":S(CP(C("et"), NP(D("le"), N("boulanger").g("f")), 
                      NP(D("le"), N("client").g("f"))), VP(V("parler").t("p"))).typ({"int":"yon"}),
         "expected":"La boulangère et la cliente parlent-elles? ",
         "message":"Coordination et interrogation"},
        # 10
        {"expression":S(CP(C("et"), NP(D("le"), N("boulanger").g("f")), NP(D("le"), N("vendeur")), 
                      NP(D("le"), N("client").g("f"))), VP(V("parler").t("p"))),
         "expected":"La boulangère, le vendeur et la cliente parlent. ",
         "message":"Coordination"},
        # 11
        {"expression":S(NP(D("le"),N("enfant").n("p")),VP(V("manger"),NP(D("le"),N("gâteau")))).typ({"pas":True}),
         "expected":"Le gâteau est mangé par les enfants. ",
         "message":"Passif avec élision"},
        # 12
        {"expression":S(NP(D("le"),N("enfant").n("p")).pro(),VP(V("manger"),NP(D("le"),N("gâteau")))),
         "expected":"Ils mangent le gâteau. ",
         "message":"Pronominalisation du sujet"},
        # 13
        {"expression":S(NP(D("le"),N("enfant").n("p")),VP(V("manger"),NP(D("le"),N("gâteau")).pro())),
         "expected":"Les enfants le mangent. ",
         "message":"Pronominalisation du complément"},
        # 14
        {"expression":S(NP(D("le"),N("enfant").n("p")),VP(V("manger"),NP(D("le"),N("gâteau")).pro())).typ({"pas":True}),
         "expected":"Il est mangé par les enfants. ",
         "message":"Pronominalisation du complément au passif"},
        # 15
        {"expression":S(NP(D("le"),N("chat").g("f").n("p")),
                  VP(V("manger"),
                     NP(D("le"),N("souris")))),
         "expected":"Les chattes mangent la souris. ",
         "message":"Phrase affirmative"},
        # 16
        {"expression":S(NP(D('le'),Q("super"),
                     N('chat').g("f").n("p").tag("b").tag("i")),
                  VP(V('dévorer').t('pc'),
                     NP(D('le'),
                        N('souris'),
                        A("gris"),"Wow!").tag("a",{"href":"http:#wikipedia.org/cat","target":"_blank"}))
                    ).typ({"neg":True}),
         "expected":'Les super <i><b>chattes</b></i> n\'ont pas dévoré <a href="http:#wikipedia.org/cat" target="_blank">la souris grise Wow!</a>',
         "message":"Phrase avec tag HTML"},
        # 17
        {"expression":S(NP(D('le'),
                         N('souris').n("p")),
                      VP(V('être').t('p'),
                            AP(A('gris')))).typ({"neg":True}),
         "expected":"Les souris ne sont pas grises. ",
         "message":"Accord avec être"},
        # 18
        {"expression":S(Pro("je").n("p").pe(2),
                  VP(V("avoir").t("cp"),
                     NP(NO(2),A("beau"),N("ami").g("f")))).typ({"neg":"plus"}),
         "expected":"Vous n'auriez plus eu 2 belles amies. ",
         "message":"Négation avec adjectif au pluriel"},
        # 19
        {"expression":S(NP(N("John")),
                      VP(V("évanouir").t("pc"),
                          DT("1979-05-21T12:00:00")
                                     .dOpt({"hour":False,"minute":False,"second":False})))
                     .typ({"neg":True}),
         "expected":"John ne s'est pas évanoui le lundi 21 mai 1979. ",
         "message":"Phrase avec une date et un ajout au dictionnaire"},
        # 20
        {"expression":S(CP(C("et"),NP(N("John")),NP(N("Mary"))),
                      VP(V("évanouir").t("pc"),
                         PP(DT("1979-05-21T12:00:00")
                             .dOpt({"hour":False,"minute":False,"second":False})))
                      ).typ({"neg":True,"refl":True}),
         "expected":"John et Mary ne se sont pas évanouis le lundi 21 mai 1979. ",
         "message":"Phrase avec coordination ou et date. "},
        # 21
        {"expression":S(VP().add(V("aimer")).add(NP(D("le"),N("pomme")))).add(NP(D("le"),N("garçon").n("p")),0),
         "expected":"Les garçons aiment la pomme. ",
         "message":"Phrase construite par morceaux"},
        # 22
        {"expression":S(CP(C("et"),NP(D("le"),N("fruit"))).add(NP(D("le"),N("pomme"))).add(NP(D("le"),N("garçon").n("p"))),
                          VP(V("venir").t("pc"),
                             Adv("hier"))),
         "expected":"Le fruit, la pomme et les garçons sont venus hier. ",
         "message":"Coordination construite par morceaux"},
        # 23
        {"expression":S(CP(C("et"),NP(D("le"),N("orange"))).add(NP(D("le"),N("pomme"))),
                          VP(V("arriver").t("pc"),
                             Adv("hier"))),
         "expected":"L'orange et la pomme sont arrivées hier. ",
         "message":"Coordination avec attribut au pluriel"},
        # 24
        {"expression":S(Pro("je"),
                          VP(V("manger").t("pc"),
                             NP(D("le"),N("pomme")))),
         "expected":"Il a mangé la pomme. ",
         "message":"Phrase de base"},
        # 25
        {"expression":S(Pro("je"),
                          VP(V("manger").t("pc"),
                             NP(D("le"),N("pomme")).tag("i").pro())),
         "expected":"Il <i>l'</i> a mangée. ",
         "message":"Pronominalisation combinée avec tag HTML"},
        # 26
        {"expression":S(NP(D("le"),N("pomme").tag("i"),
                          SP(Pro("qui"),
                             VP(V("manger").aux("êt").t("pc"))))),
         "expected":"La <i>pomme</i> qui est mangée. ",
         "message":"Phrase avec attribut"},
        # 27
        {"expression":NP(D("le"),N("pomme").tag("i"),
                             SP(Pro("que"),
                                Pro("je"),
                                VP(V("manger").t("pc")))),
         "expected":"la <i>pomme</i> qu'il a mangée",
         "message":"NP avec relative"},
        # 28
        {"expression":S(NP(D("le"),N("pomme").tag("i"),
                             SP(Pro("que"),
                                Pro("je"),
                                VP(V("manger").t("pc")))).pro()),
         "expected":"Elle. ",
         "message":"Pronominalisation qui couvre toute la phrase..."},
        # 29
        {"expression":S(NP(D("le"),N("enfant").n("p")),VP(V("manger"),NP(D("le"),N("gâteau")))).typ({"pas":True}),
         "expected":"Le gâteau est mangé par les enfants. ",
         "message":"Passive"},
        # 30
        {"expression":S(Pro("je").pe(1).n("p"), VP(V("agir").t("c"), AdvP(Adv("conformément"),
                                  PP(P("à"), NP(D("le"), N("loi")))))).typ({"mod":"nece"}),
         "expected":"Nous devrions agir conformément à la loi. ",
         "message":"avec PP"},
        # 31
        {"expression":S(NP(D("le"),N("chat").n("p")),
                      CP(C("et"),VP(V("courir")),
                                 VP(V("sauter")),
                                 VP(V("manger"),NP(D("le"),N("souris"))))),
         "expected":"Les chats courent, sautent et mangent la souris. ",
         "message":"Sujet d'une coordination de verbes"},
        # 32
        {"expression":S(Pro("ce"),
                      VP(V("être"),
                         PP(P('de'),
                            NP(D("le"),
                               N("exercice"),
                               AP(A("aisé"),
                                  PP(P("à"),
                                     VP(V("réussir").t("b"),
                                        PP(P("de"),
                                           NP(D("le"),
                                              A("premier"),
                                              N("coup")))))))))
                       ).typ({"neg":True}),
         "expected":"Ce n'est pas de l'exercice aisé à réussir du premier coup. ",
         "message":"Multiples élisions"},
        # 33
        {"expression":S(CP(C("et"),
                         NP(D("mon").pe(1),N("ami").g("f")),
                         NP(D("le"),A("vieux"),N("étudiant").g("f"))),
                       SP(Pro("que"),
                          NP(D("ce"),N("homme")),
                          VP(V("recevoir").t("pc")))),
         "expected":"Mon amie et la vieille étudiante que cet homme a reçues. ",
         "message":"Élisions, euphonies et cod coordonné placé avant le verbe"},
        # 34
        {"expression": S(NP(D("le").tag("i"),N("chat").tag("b"))),
         "expected":"<i>Le</i> <b>chat</b>. ",
         "message":"Top level,capitalization with HTML tags. "},
        # 35
        {"expression":S(Pro("je").pe(2),
                      VP(V("demander").t("pc"),
                         NP(D("mon"),N("adresse")).pro(),
                         PP(P("à"),NP(D("mon"),N("parent").n("p"))).pro())),
         "expected":"Tu la leur as demandée. ",
         "message":"Pronominalisation de l'objet direct et de l'objet indirect (datif)"},
        # 36
        {"expression":S(Pro("je"),
                      VP(V("parler").t("pc"),
                         PP(P("à"),NP(D("mon"),N("ami").g("f"))).pro(),
                         PP(P("de"),NP(D("mon"),N("problème"))).pro())),
         "expected":"Il lui en a parlé. ",
         "message":"Pronominalisation de deux objets indirects"},
        # 37
        {"expression":S(Pro('je').pe(2),
                        VP(V('travailler').t("pc"),
                           Adv('bien'))).typ({"mod":"nece"}),
         "expected":"Tu as dû bien travailler. ",
         "message":"Position de l'adverbe"},
        # 38
        {"expression":S(Pro('je'),
                        VP(V('aller').t("pc"),
                           Adv('hier'),
                           PP(P('à'),
                              NP(D('le'),
                                 N('maison'))))).typ({"neg":True}),
         "expected":"Il n'est pas allé hier à la maison. ",
         "message":"Position de l'adverbe dans une négation"},
        # 39
        {"expression":S(Pro('je'),
                        VP(V('aller').t("pc"),
                           Adv('souvent'),
                           PP(P('à'),
                              NP(D('le'),
                                 N('maison'))),
                           Adv('sûrement'))).typ({"neg":True}),
         "expected":"Il n'est pas souvent allé à la maison sûrement. ",
         "message":"Position d'adverbes séparés"},
        # 40
        {"expression":S(Pro('je'),
                        VP(V('aller').t("pc"),
                           Adv('souvent').pos("post"),
                           PP(P('à'),
                              NP(D('le'),
                                 N('maison'))))).typ({"neg":True}),
         "expected":"Il n'est pas allé souvent à la maison. ",
         "message":"Position d'un adverbe avec .pos()"},
        # 41
        {"expression":S(NP(D('le'),
                          N('chat')),
                       VP(V('manger'),
                          Adv('bien'),
                          Adv('souvent'),
                          NP(D('le'),
                             N('souris')))).typ({"pas":True}),
         "expected":"La souris est bien souvent mangée par le chat. ",
         "message":"Position d'adverbes contigus"},
        #   42 version en constituant de Bonfante et al. Exercice 2.51 p 72
          {"expression":S(S(VP(V("trouver").t("b"),
                               NP(D("un"),N("livre"),
                                  SP(Pro("dont"),
                                     Pro("on"),
                                     VP(V("dire").t("s"),
                                        SP(Pro("que"),
                                            VP(V("traduire").t("pc"),Pro("lui").c("acc")).typ({'neg':True,"pas":True}))
                                        ).typ({"mod":"poss"}))))),
                          VP(V("être"),A("difficile"))).typ({"pas":True,"neg":True}),
          "expected": "Il n'a pas été difficile de trouver un livre dont on puisse dire qu'il n'a pas été traduit. ",
          "message": "Subordonnées modifiées imbriquées"},
        #   43 version simplifiée en constituant de Bonfante et al. Exercice 2.51 p 72
        {"expression":S(S(VP(V("trouver").t("b"),
                             NP(D("un"),N("livre"),
                                SP(Pro("que"),
                                   Pro("lui").c("nom"),
                                   VP(V("traduire").t("pc")).typ({'neg':True,"pas":False}))))),
                        VP(V("être"),A("difficile"))).typ({"pas":True,"neg":True}),
          "expected": "Il n'a pas été difficile de trouver un livre qu'il n'a pas traduit. ",
          "message": "Subordonnées modifiées imbriquées - bis"},
        #   44
        {"expression":CP(C("et"),
                         NP(D("de"),
                            A("multiple").pos('pre'),
                            N("tâche")),
                         N("démarche")).n('p'),
          "expected": "de multiples tâches et démarches",
          "message": "propagation d'option dans un CP"},
        #   45 - version cosntituant de Bonfante et al. Figure 2.19 p 58
        {"expression":
             S(NP(D("le"), N("sorcier")).g("f"),
               VP(V("être").t("ps"),
                  CP(C("et"),
                     VP(V("condamner"),
                        PP(P("à"), N("mort"))),
                     VP(V("torturer")),
                     VP(V("brûler"))).t("pp"))),
          "expected": "La sorcière fut condamnée à mort, torturée et brûlée. ",
          "message": "attributs coordonnés"},
        #   46 - version en constituants de Bonfante et al. Exemple 3.1 p 82
          {"expression":
               S(Pro("lui").c("nom"),
                 VP(V("indiquer").t("c"),
                    SP(C("si"),
                       Pro("lui").c("nom"),
                       VP(V("plaider"),
                          AP(A("coupable"),
                             PP(P("de"),
                                NP(D("le"),
                                   N("fait").n("p"),
                                   SP(Pro("qui"),
                                      VP(V("être"),
                                         V("reprocher").t("pp"),
                                         Pro("lui").c("dat")))))))))).typ({"mod": "nece"}),
          "expected": "Il devrait indiquer s'il plaide coupable des faits qui lui sont reprochés. ",
          "message": "NP avec une relative contenant un attribut"},
        #   39
        #   {"expression":,
        #   "expected": "",
        #   "message": ""},
        #   39
        #   {"expression":,
        #   "expected": "",
        #   "message": ""},

    ];

if __name__ == '__main__':
    test("Phrases françaises","fr",sentences_fr,badOnly=True)
    