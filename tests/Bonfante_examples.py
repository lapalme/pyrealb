from context import pyrealb
from pyrealb import *
from test import test

# exemples tirées du livre "Application de la réécriture de graphes au traitement automatique des langues"
#                           Guillaume Bonfante, Bruno Guillaume, Guy Perrier, ISTE éditions 2018

def bonfante_fr_ex():
    loadFr()
    return [
        {},  # dummy 0
        # 1
        {"expression":
             S(NP(D("le"),
                  N("conférence"),
                  A("intergouvernemental")),
               VP(V("tenter"),
                  PP(P("de"),
                     VP(V("répondre").t("b"),
                        Adv("précisément"),
                        PP(P("à"),
                           NP(D("ce"),
                              N("question")))))))            ,
         "expected":"La conférence intergouvernementale tente de répondre précisément à cette question. ",
         "message":" Figure 2.1 p 45 / REM: NP,AP et VP sont 'condensés'"},
        # 1
        {"expression":
             root(V("tenter"),
                  subj(N("conférence"),
                       det(D("le")),
                       mod(A("intergouvernemental"))),
                  comp(P("de"),
                       comp(V("répondre").t('b'),
                            mod(Adv("précisément")),
                            comp(P("à"),
                                 mod(N("question"),
                                     det(D("ce"))))))),
         "expected":"La conférence intergouvernementale tente de répondre précisément à cette question. ",
         "message":"Figure 2.2 p 46"},
        # 1
        {"expression":
             root(V("désoler"),
                  subj(Pro("lui").c("nom")),
                  comp(Pro("que"),
                       comp(V("être").t("s"),
                            subj(Pro("elle").c("nom")),
                            mod(A("furieux"),
                                comp(P("contre"),
                                     comp(N("frère"),
                                          det(D("son")))))))).typ({"refl":True}),
         "expected":"Il se désole qu'elle soit furieuse contre son frère. ",
         "message":" Figure 2.14 p 53"},
        # 1
        {"expression":
             root(V("tomber"),
                  subj(N("garçon").n("p"),
                       det(D("le")),
                       comp(V("courir"),
                            subj(Pro("qui"))))),
         "expected":"Les garçons qui courent tombent. ",
         "message":"p 54 (au pluriel et passé composé)"},
        # 1
        {"expression":
             root(V("être").t("pc"),
                  subj(N("français").cap().n("p"),
                       det(NO(2).nat()),
                       mod(A("autre"))),
                  coord(C("et"),
                        mod(V("enlever").t("pp")),
                        mod(V("libérer").t("pp"))).n("p"),
                  comp(P("à"),
                       comp(Q("Beyrouth")))
                  ),
         "expected":"Deux autres Français ont été enlevés et libérés à Beyrouth. ",
         "message":"p 59 - 2.22 / dépendances assez différentes... et on doit forcer l'accord des PP"},
        # 1
        {"expression":
             root(V("enlever").t("pc"),
                  comp(N("français").cap(),
                       det(NO(2).nat()),
                       mod(A("autre"))),
                  comp(P("à"),
                       comp(Q("Beyrouth")))
                  ).typ({"pas":True}),
         "expected":"Deux autres Français ont été enlevés à Beyrouth. ",
         "message":"p 59 - p 2.22 / variante sans coordination"},
        # 1
        {"expression":
             S(VP(V("enlever").t("pc"),
                  NP(NO(2).nat(), A("autre"), N("français").cap().n("p")),
                  PP(P("à"), "Beyrouth"))).typ({"pas": True}),
         "expected":"Deux autres Français ont été enlevés à Beyrouth. ",
         "message":"p 59 - p 2.22 / variante sans coordination en constituants"},
        # 1
        {"expression":
             coord(C("et"),
                   root(V("soutenir"),
                        subj(Pro("nous").c("nom")),
                        comp(Pro("vous").c("acc")),
                        mod(Adv("pleinement"))),
                   root(V("être").pe(1).n("p"),
                        mod(A("méfiant"))).typ({"neg": "aucunement"}))            ,
         "expected":"Nous vous soutenons pleinement et ne sommes aucunement méfiants. ",
         "message":"2.32 p 65"},
        # 1
        {"expression":
             root(V("faire").t("pc"),
                  subj(Pro("eux").c("nom")),
                  comp(V("subir").t("b"),
                       comp(N("choc"),
                            det(D("un")),
                            mod(A("électrique"))).n("p"),
                       comp(Pro("lui").c("dat")))),
         "expected":"Ils lui ont fait subir des chocs électriques. ",
         "message":" 2.36 p 67 / la racine devrait être 'subir' avec auxiliaire faire..."},
        # 1
        {"expression":
             root(V("être").n("p"),
                  subj(Pro("ce")),
                  mod(N("type").n("p"),
                      det(D("le")),
                      mod(A("différent")).pos("pre"),
                      comp(N("mafia").n("p"),
                           det(P("de")))),
                  mod(V("organiser").n("p"),
                      subj(Pro("qui")),
                      comp(Pro("lui").c("acc")))),
         "expected":"Ce sont les différents types de mafias qui l'organisent. ",
         "message":"2.39 p 69"},
        # # 1
        # {"expression":S( NP(D("the"), N("cat")), VP(V("sit").t("ps"), PP(P("on"), NP(D("the"), N("couch"))))),
        #  "expected":"The cat sat on the couch. ",
        #  "message":"Full sentence"},
        # # 1
        # {"expression":S( NP(D("the"), N("cat")), VP(V("sit").t("ps"), PP(P("on"), NP(D("the"), N("couch"))))),
        #  "expected":"The cat sat on the couch. ",
        #  "message":"Full sentence"},
    ]

def bonfante_en_ex():
    loadEn()
    return [
        {}, # dummy 0
        # 1
        {"expression":
             root(V("follow"),
                  subj(Pro("me").pe(1).c("nom")),
                  comp(N("link").n("p"),
                       mod(V("indicate"),
                           subj(Pro("that")),
                           mod(Adv("strongly")).pos("pre")))).typ({"perf": True, "prog": True}),
         "expected":"I have been following links that strongly indicate. ",
         "message":"p 47 2.2"},
        # 1
        {"expression":
             root(V("say").t("ps"),
                  subj(Pro("them").c("nom")),
                  comp(V("give"),
                       subj(Pro("them").c("nom")),
                       comp(Pro("me").pe(1).c("dat")),
                       comp(N("detail").n("p"),
                            det(D("that"))),
                       comp(P("over"),
                            comp(N("phone"),
                                 det(D("the"))))).typ({"neg": True, "mod": "poss", "contr": True})),
         "expected":"They said they can't give me those details over the phone. ",
         "message":"p 56 2.16"},
        # 1
        {"expression":
             coord(C("and"),
                   root(V("finance").n("p"),
                        subj(Pro("who"),
                             mod(N("people"),
                                 det(D("the")),
                                 det(D("same"))).pos("pre")),
                        comp(N("arm").n("p"))),
                   root(V("dispatch").n("p"),
                        comp(N("murderer").n("p"),
                             mod(N("suicide")).pos("pre"))))
            ,
         "expected":"The same people who finance arms and dispatch suicide murderers. ",
         "message":"p 58"},
        # # 1
        # {"expression":S( NP(D("the"), N("cat")), VP(V("sit").t("ps"), PP(P("on"), NP(D("the"), N("couch"))))),
        #  "expected":"The cat sat on the couch. ",
        #  "message":"Full sentence"},
        # # 1
        # {"expression":S( NP(D("the"), N("cat")), VP(V("sit").t("ps"), PP(P("on"), NP(D("the"), N("couch"))))),
        #  "expected":"The cat sat on the couch. ",
        #  "message":"Full sentence"},
        # # 1
        # {"expression":S( NP(D("the"), N("cat")), VP(V("sit").t("ps"), PP(P("on"), NP(D("the"), N("couch"))))),
        #  "expected":"The cat sat on the couch. ",
        #  "message":"Full sentence"},
        # # 1
        # {"expression":S( NP(D("the"), N("cat")), VP(V("sit").t("ps"), PP(P("on"), NP(D("the"), N("couch"))))),
        #  "expected":"The cat sat on the couch. ",
        #  "message":"Full sentence"},
        # # 1
        # {"expression":S( NP(D("the"), N("cat")), VP(V("sit").t("ps"), PP(P("on"), NP(D("the"), N("couch"))))),
        #  "expected":"The cat sat on the couch. ",
        #  "message":"Full sentence"},
        # # 1
        # {"expression":S( NP(D("the"), N("cat")), VP(V("sit").t("ps"), PP(P("on"), NP(D("the"), N("couch"))))),
        #  "expected":"The cat sat on the couch. ",
        #  "message":"Full sentence"},
        # # 1
        # {"expression":S( NP(D("the"), N("cat")), VP(V("sit").t("ps"), PP(P("on"), NP(D("the"), N("couch"))))),
        #  "expected":"The cat sat on the couch. ",
        #  "message":"Full sentence"},
        # # 1
        # {"expression":S( NP(D("the"), N("cat")), VP(V("sit").t("ps"), PP(P("on"), NP(D("the"), N("couch"))))),
        #  "expected":"The cat sat on the couch. ",
        #  "message":"Full sentence"},
        # # 1
        # {"expression":S( NP(D("the"), N("cat")), VP(V("sit").t("ps"), PP(P("on"), NP(D("the"), N("couch"))))),
        #  "expected":"The cat sat on the couch. ",
        #  "message":"Full sentence"},
        # # 1
        # {"expression":S( NP(D("the"), N("cat")), VP(V("sit").t("ps"), PP(P("on"), NP(D("the"), N("couch"))))),
        #  "expected":"The cat sat on the couch. ",
        #  "message":"Full sentence"},
        # # 1
        # {"expression":S( NP(D("the"), N("cat")), VP(V("sit").t("ps"), PP(P("on"), NP(D("the"), N("couch"))))),
        #  "expected":"The cat sat on the couch. ",
        #  "message":"Full sentence"},
    ]

if __name__ == '__main__':
    test("Exemples de Bonfante et al. en français","fr",bonfante_fr_ex,badOnly=False)
    test("Bonfante et al. examples in English","en",bonfante_en_ex,badOnly=False)
