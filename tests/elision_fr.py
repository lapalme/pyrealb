from context import pyrealb
from pyrealb import *
from test import test


def elision_fr():
    loadFr();
    elisionTestsFr=[
        [Q("&"),"&"],
        [N("bonjour"),"bonjour"],
        [N("bonjour").tag("i").tag("p"),"<p><i>bonjour</i></p>"],
        [NP(D("le"),N("enfant")),"l'enfant"],
        [S(NP(D("le"),N("écolier")),VP(Pro("me*refl").pe(3),V("élever"),PP(P("dans"),NP(D("le"),N("haut"))))),
         "L'écolier s'élève dans le haut."],
        [NP(D("le"),N("élève").cap()),"l'Élève"],
        [NP(D("le"),N("avocat"),
            SP(Pro("que"),Adv("aujourd'hui"),Pro("je").pe(1),
               VP(V("accepter"),
                  PP(P("pour"),NP(D("mon").pe(1),N("ami").g("f")))))),
         "l'avocat qu'aujourd'hui j'accepte pour mon amie"],
        [CP(NP(D("le"),N("hameçon").cap()),
            NP(D("le"),N("héros")),
            NP(D("mon"),N("habitude"))),
         "l'Hameçon, le héros, son habitude"],
        [CP(PP(P("de"),NP(D("le"),N("chapeau").tag("b"))),
            PP(P("à"),NP(D("le"),N("ami").n("p"))).tag("i"),
            NP(D("mon").pe(1),NP(N("ami"),A("beau").tag("b"))),
            NP(D("mon").pe(1),NP(N("étudiant"),A("vieux")).tag("i"))),
         "du <b>chapeau</b>, <i>aux amis, </i> mon <b>bel</b> ami, mon <i>vieil étudiant</i>"],
        [CP(PP(P("jusque"),PP(P("à"),NP(D("le"),N("bord")).n("p"))),
            PP(P("jusque"),PP(P("à"),NP(D("un"),N("bord")).n("p")))),
         "jusqu'aux bords, jusqu'à des bords"],
        [S(NP(D('le'),N("élève"),A("aimable")),
           VP(V("écrire"),
              PP(P("sur"),NP(D("le"),N("ardoise"))))),
         "L'élève aimable écrit sur l'ardoise."],
        [S(Pro("je").pe(1),
           VP(Pro("me*refl").pe(2),
              V("aimer"),
              PP(P("pour"),NP(D("le"),N("éternité"))))),
         "Je t'aime pour l'éternité."],
        [S(D("ce"),VP(V("être"),
             NP(D("un"),N("test"),
                PP(P("de"),N("élision"))),
             AP(A("facile"),
                PP(P("à"),V("faire").t("b"),
                   PP(P("de"),NP(D("le"),A("premier"),N("coup"))))))).typ({"neg":True}),
         "Ce n'est pas un test d'élision facile à faire du premier coup."],
        [S(Pro("je").pe(1),
           VP(V("aimer"),
              NP(D("ce"),N("exercice")),
              PP(P("avec"),
                 NP(D("un"),A("autre"),N("chien")).n("p")))),
        "J'aime cet exercice avec d'autres chiens."],
        [S(Adv("que"),Pro("je").pe(3),
           VP(V("aimer"),V("avoir").t("b"),
              PP(P("de"),NP(D("le"),N("exercice"))))),
        "Qu'il aime avoir de l'exercice."],
        [CP(NP(D("le"),N("église")),
            NP(D("le"),N("ami").g("f")),
            NP(D("mon").pe(3),N("ami").g("f"))),
        "l'église, l'amie, son amie" ],
        [SP(C("quoique"),
            Pro("je"),VP(V("faire").t("s"),A("beau"))),
         "quoiqu'il fasse beau"],
        [S(NP(D("le"),N("élève").g("f")),
           VP(Pro("moi").pe(1).c("dat"),
              V("dire"),
              PP(P("de"),
                 VP(V("interroger").t("b"),
                    NP(D("le"),N("élève").g("f")).pro()).typ({"neg":True})))),
        "L'élève me dit de ne pas l'interroger."],
        [S(CP(C("et"),
           SP(NP(D("le"),N("histoire")),
              VP(V("être"),
                 NP(D("le"),N("épreuve"),
                    PP(P("de"),N("examen"))))),
           SP(NP(D("le"),N("homme")),
              VP(V("respecter"),
                 NP(D("le"),N("nature")))).typ({"neg":True}))),
         "L'histoire est l'épreuve d'examen et l'homme ne respecte pas la nature."],
        [S(CP(C("et"),NP(D("mon").pe(1),N("ami")),
                      NP(D("ce"),A("honnête").pos("pre"),N("homme"))),
           VP(V("entrer").t("pc"),
              PP(P("avec"),NP(D("le"),N("armoire"))))),
        "Mon ami et cet honnête homme sont entrés avec l'armoire."],
        [S(CP(C("et"),NP(D("mon").pe(1),N("ami").g("f")),
              NP(D("ce"),A("honnête").pos("pre"),N("femme"))),
           VP(V("entrer").t("pc"),
              PP(P("avec"),NP(D("le"),N("armoire"))))),
         "Mon amie et cette honnête femme sont entrées avec l'armoire."],
        [S(Pro("ce"),
           VP(V("être"),
              PP(P("de"),
                 NP(D("le"),N("affection")),
                 SP(Pro("dont"),
                    NP(D("ce"),N("enfant")),
                       VP(V("avoir"),N("besoin")))))),
        "C'est de l'affection dont cet enfant a besoin."],
        [S(NP(D("un"),N("possibilité"),
           PP(P("de"),N("erreur"),
              Adv("lors"),P("de"),
              NP(D("un"),N("contraction"),
                 A("suivi"),
                 PP(P("de"),NP(D("un"),N("élision")))),
              SP(Pro("où"),Pro("je"),
                 VP(V("falloir"),
                    V("élider").t("b"),
                    PP(P("à"),NP(D("le"),A("premier"),N("abord")))))))),
        "Une possibilité d'erreur lors d'une contraction suivie d'une élision où il faut élider au premier abord."],
        [S(PP(P("à"),D("ce")).tag("b"),N("homme")),
        "<b>À cet</b> homme."],
        [S(Pro("je"),
           VP(Pro("me*refl"),
              V("adresser").t("ps"),
              PP(P("à"),NP(D("le"),N("homme").en("*")),
                 PP(P("à"),NP(D("le"),N("porte")),
                    PP(P("de"),NP(D("ce"),A("ancien").pos("pre"),N("château"))))))),
        "Il s'adressa à l' *homme* à la porte de cet ancien château."],
        [S(Pro("ça"),
           VP(V("être").t("pp"),
              AP(Adv("très"),A("difficile"),
                 CP(C("et"),PP(P("de"),V("approcher").t("b")),
                            PP(P("de"),Pro("le"),V("approcher").t("b")).en("*"))))),
         "Ça été très difficile d'approcher et  *de l'approcher* ."],
        [S(NP(D("le"),N("hirondelle")),
           CP(C("mais"),
              VP(Pro("me*refl").pe(1),V("honorer")),
              VP(Pro("me*refl").pe(1),
                 V("amener"),
                 CP(C("et"),
                    PP(P("à"),D("le"),N("hôpital")).en("*"),
                    PP(P("à"),D("le"),N("hibou")))))),
        "L'hirondelle m'honore mais m'amène  *à l'hôpital* et au hibou."]
    ];
    
    tests=[{}]
    for exp,expected in elisionTestsFr:
        tests.append({
            "expression":exp,
            "expected":expected,
            "message":f"elision dans {expected}"
        })
    return tests
    
if __name__ == '__main__':
    test("English dates","en",elision_fr)