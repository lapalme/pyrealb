import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..','src')))

from pyrealb import *
load("fr")

def test_elision_fr_1():
    assert (
Q("&").realize()   
    ) == '&',\
    'elision dans &'


def test_elision_fr_2():
    assert (
N("bonjour").realize()   
    ) == 'bonjour',\
    'elision dans bonjour'


def test_elision_fr_3():
    assert (
N("bonjour").tag('i').tag('p').realize()   
    ) == '<p><i>bonjour</i></p>',\
    'elision dans <p><i>bonjour</i></p>'


def test_elision_fr_4():
    assert (
NP(D("le"),
   N("enfant")).realize()   
    ) == "l'enfant",\
    "elision dans l'enfant"


def test_elision_fr_5():
    assert (
NP(D("le"),
   A("beau"),
   N("homme")).realize()   
    ) == 'le bel homme',\
    'elision dans le bel homme'


def test_elision_fr_6():
    assert (
NP(D("le"),
   A("vieux").f('co'),
   N("homme")).realize()   
    ) == 'le plus vieil homme',\
    'elision dans le plus vieil homme'


def test_elision_fr_7():
    assert (
NP(A("beau").f('su'),
   N("homme")).realize()   
    ) == 'le plus bel homme',\
    'elision dans le plus bel homme'


def test_elision_fr_8():
    assert (
NP(D("le"),
   A("beau").f('su').pos('post'),
   N("homme")).realize()   
    ) == "l'homme le plus beau",\
    "elision dans l'homme le plus beau"


def test_elision_fr_9():
    assert (
NP(D("le"),
   A("beau").f('co'),
   N("homme").n('p')).realize()   
    ) == 'les plus beaux hommes',\
    'elision dans les plus beaux hommes'


def test_elision_fr_10():
    assert (
S(NP(D("le"),
     N("écolier")),
  VP(Pro("me*refl").pe(3),
     V("élever"),
     PP(P("dans"),
        NP(D("le"),
           N("haut"))))).realize()   
    ) == "L'écolier s'élève dans le haut. ",\
    "elision dans L'écolier s'élève dans le haut. "


def test_elision_fr_11():
    assert (
NP(D("le"),
   N("élève").cap(True)).realize()   
    ) == "l'Élève",\
    "elision dans l'Élève"


def test_elision_fr_12():
    assert (
NP(D("le"),
   N("avocat"),
   SP(Pro("que"),
      Adv("aujourd'hui"),
      Pro("je").pe(1),
      VP(V("accepter"),
         PP(P("pour"),
            NP(D("mon").pe(1),
               N("ami").g('f')))))).realize()   
    ) == "l'avocat qu'aujourd'hui j'accepte pour mon amie",\
    "elision dans l'avocat qu'aujourd'hui j'accepte pour mon amie"


def test_elision_fr_13():
    assert (
CP(NP(D("le"),
      N("hameçon").cap(True)),
   NP(D("le"),
      N("héros")),
   NP(D("mon"),
      N("habitude"))).realize()   
    ) == "l'Hameçon, le héros, son habitude",\
    "elision dans l'Hameçon, le héros, son habitude"


def test_elision_fr_14():
    assert (
CP(PP(P("de"),
      NP(D("le"),
         N("chapeau").tag('b'))),
   PP(P("à"),
      NP(D("le"),
         N("ami").n('p'))).tag('i'),
   NP(D("mon").pe(1),
      NP(N("ami"),
         A("beau").tag('b'))),
   NP(D("mon").pe(1),
      NP(N("étudiant"),
         A("vieux")).tag('i'))).realize()   
    ) == 'du <b>chapeau</b>, <i>aux amis</i>, mon <b>bel</b> ami, mon <i>vieil étudiant</i>',\
    'elision dans du <b>chapeau</b>, <i>aux amis</i>, mon <b>bel</b> ami, mon <i>vieil étudiant</i>'


def test_elision_fr_15():
    assert (
CP(PP(P("jusque"),
      PP(P("à"),
         NP(D("le"),
            N("bord")).n('p'))),
   PP(P("jusque"),
      PP(P("à"),
         NP(D("un"),
            N("bord")).n('p')))).realize()   
    ) == "jusqu'aux bords, jusqu'à des bords",\
    "elision dans jusqu'aux bords, jusqu'à des bords"


def test_elision_fr_16():
    assert (
S(NP(D("le"),
     N("élève"),
     A("aimable")),
  VP(V("écrire"),
     PP(P("sur"),
        NP(D("le"),
           N("ardoise"))))).realize()   
    ) == "L'élève aimable écrit sur l'ardoise. ",\
    "elision dans L'élève aimable écrit sur l'ardoise. "


def test_elision_fr_17():
    assert (
S(Pro("je").pe(1),
  VP(Pro("me*refl").pe(2),
     V("aimer"),
     PP(P("pour"),
        NP(D("le"),
           N("éternité"))))).realize()   
    ) == "Je t'aime pour l'éternité. ",\
    "elision dans Je t'aime pour l'éternité. "


def test_elision_fr_18():
    assert (
S(D("ce"),
  VP(V("être"),
     NP(D("un"),
        N("test"),
        PP(P("de"),
           N("élision"))),
     AP(A("facile"),
        PP(P("à"),
           V("faire").t('b'),
           PP(P("de"),
              NP(D("le"),
                 A("premier"),
                 N("coup"))))))).typ({'neg': True}).realize()   
    ) == "Ce n'est pas un test d'élision facile à faire du premier coup. ",\
    "elision dans Ce n'est pas un test d'élision facile à faire du premier coup. "


def test_elision_fr_19():
    assert (
S(Pro("je").pe(1),
  VP(V("aimer"),
     NP(D("ce"),
        N("exercice")),
     PP(P("avec"),
        NP(D("un"),
           A("autre"),
           N("chien")).n('p')))).realize()   
    ) == "J'aime cet exercice avec d'autres chiens. ",\
    "elision dans J'aime cet exercice avec d'autres chiens. "


def test_elision_fr_20():
    assert (
S(Adv("que"),
  Pro("je").pe(3),
  VP(V("aimer"),
     V("avoir").t('b'),
     PP(P("de"),
        NP(D("le"),
           N("exercice"))))).realize()   
    ) == "Qu'il aime avoir de l'exercice. ",\
    "elision dans Qu'il aime avoir de l'exercice. "


def test_elision_fr_21():
    assert (
CP(NP(D("le"),
      N("église")),
   NP(D("le"),
      N("ami").g('f')),
   NP(D("mon").pe(3),
      N("ami").g('f'))).realize()   
    ) == "l'église, l'amie, son amie",\
    "elision dans l'église, l'amie, son amie"


def test_elision_fr_22():
    assert (
SP(C("quoique"),
   Pro("je"),
   VP(V("faire").t('s'),
      A("beau"))).realize()   
    ) == "quoiqu'il fasse beau",\
    "elision dans quoiqu'il fasse beau"


def test_elision_fr_23():
    assert (
S(NP(D("le"),
     N("élève").g('f')),
  VP(Pro("moi").pe(1).c('dat'),
     V("dire"),
     PP(P("de"),
        VP(V("interroger").t('b'),
           NP(D("le"),
              N("élève").g('f')).pro(True)).typ({'neg': True})))).realize()   
    ) == "L'élève me dit de ne pas l'interroger. ",\
    "elision dans L'élève me dit de ne pas l'interroger. "


def test_elision_fr_24():
    assert (
S(CP(C("et"),
     SP(NP(D("le"),
           N("histoire")),
        VP(V("être"),
           NP(D("le"),
              N("épreuve"),
              PP(P("de"),
                 N("examen"))))),
     SP(NP(D("le"),
           N("homme")),
        VP(V("respecter"),
           NP(D("le"),
              N("nature")))).typ({'neg': True}))).realize()   
    ) == "L'histoire est l'épreuve d'examen et l'homme ne respecte pas la nature. ",\
    "elision dans L'histoire est l'épreuve d'examen et l'homme ne respecte pas la nature. "


def test_elision_fr_25():
    assert (
S(CP(C("et"),
     NP(D("mon").pe(1),
        N("ami")),
     NP(D("ce"),
        A("honnête").pos('pre'),
        N("homme"))),
  VP(V("entrer").t('pc'),
     PP(P("avec"),
        NP(D("le"),
           N("armoire"))))).realize()   
    ) == "Mon ami et cet honnête homme sont entrés avec l'armoire. ",\
    "elision dans Mon ami et cet honnête homme sont entrés avec l'armoire. "


def test_elision_fr_26():
    assert (
S(CP(C("et"),
     NP(D("mon").pe(1),
        N("ami").g('f')),
     NP(D("ce"),
        A("honnête").pos('pre'),
        N("femme"))),
  VP(V("entrer").t('pc'),
     PP(P("avec"),
        NP(D("le"),
           N("armoire"))))).realize()   
    ) == "Mon amie et cette honnête femme sont entrées avec l'armoire. ",\
    "elision dans Mon amie et cette honnête femme sont entrées avec l'armoire. "


def test_elision_fr_27():
    assert (
S(Pro("ce"),
  VP(V("être"),
     PP(P("de"),
        NP(D("le"),
           N("affection")),
        SP(Pro("dont"),
           NP(D("ce"),
              N("enfant")),
           VP(V("avoir"),
              N("besoin")))))).realize()   
    ) == "C'est de l'affection dont cet enfant a besoin. ",\
    "elision dans C'est de l'affection dont cet enfant a besoin. "


def test_elision_fr_28():
    assert (
S(NP(D("un"),
     N("possibilité"),
     PP(P("de"),
        N("erreur"),
        Adv("lors"),
        P("de"),
        NP(D("un"),
           N("contraction"),
           A("suivi"),
           PP(P("de"),
              NP(D("un"),
                 N("élision")))),
        SP(Pro("où"),
           Pro("je"),
           VP(V("falloir"),
              V("élider").t('b'),
              PP(P("à"),
                 NP(D("le"),
                    A("premier"),
                    N("abord")))))))).realize()   
    ) == "Une possibilité d'erreur lors d'une contraction suivie d'une élision où il faut élider au premier abord. ",\
    "elision dans Une possibilité d'erreur lors d'une contraction suivie d'une élision où il faut élider au premier abord. "


def test_elision_fr_29():
    assert (
S(PP(P("à"),
     D("ce")).tag('b'),
  N("homme")).realize()   
    ) == '<b>À cet</b> homme. ',\
    'elision dans <b>À cet</b> homme. '


def test_elision_fr_30():
    assert (
S(Pro("je"),
  VP(Pro("me*refl"),
     V("adresser").t('ps'),
     PP(P("à"),
        NP(D("le"),
           N("homme").en('*')),
        PP(P("à"),
           NP(D("le"),
              N("porte")),
           PP(P("de"),
              NP(D("ce"),
                 A("ancien").pos('pre'),
                 N("château"))))))).realize()   
    ) == "Il s'adressa à l'*homme* à la porte de cet ancien château. ",\
    "elision dans Il s'adressa à l'*homme* à la porte de cet ancien château. "


def test_elision_fr_31():
    assert (
S(Pro("ça"),
  VP(V("être").t('pp'),
     AP(Adv("très"),
        A("difficile"),
        CP(C("et"),
           PP(P("de"),
              V("approcher").t('b')),
           PP(P("de"),
              Pro("le"),
              V("approcher").t('b')).en('*'))))).realize()   
    ) == "Ça été très difficile d'approcher et *de l'approcher* . ",\
    "elision dans Ça été très difficile d'approcher et *de l'approcher* . "


def test_elision_fr_32():
    assert (
S(NP(D("le"),
     N("hirondelle")),
  CP(C("mais"),
     VP(Pro("me*refl").pe(1),
        V("honorer")),
     VP(Pro("me*refl").pe(1),
        V("amener"),
        CP(C("et"),
           PP(P("à"),
              D("le"),
              N("hôpital")).en('*'),
           PP(P("à"),
              D("le"),
              N("hibou")))))).realize()   
    ) == "L'hirondelle m'honore mais m'amène *à l'hôpital* et au hibou. ",\
    "elision dans L'hirondelle m'honore mais m'amène *à l'hôpital* et au hibou. "

