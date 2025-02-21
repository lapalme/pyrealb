import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..','src')))

from pyrealb import *
load("fr")

def test_bonfante_fr_ex_1():
    assert (
S(NP(D("le"),
     N("conférence"),
     A("intergouvernemental")),
  VP(V("tenter"),
     PP(P("de"),
        VP(V("répondre").t('b'),
           Adv("précisément"),
           PP(P("à"),
              NP(D("ce"),
                 N("question"))))))).realize()   
    ) == 'La conférence intergouvernementale tente de répondre précisément à cette question. ',\
    " Figure 2.1 p 45 / REM: NP,AP et VP sont 'condensés'"


def test_bonfante_fr_ex_2():
    assert (
root(V("tenter"),
     subj(N("conférence"),
          det(D("le")),
          mod(A("intergouvernemental"))),
     comp(P("de"),
          comp(V("répondre").t('b'),
               mod(Adv("précisément")),
               comp(P("à"),
                    mod(N("question"),
                        det(D("ce"))))))).realize()   
    ) == 'La conférence intergouvernementale tente de répondre précisément à cette question. ',\
    'Figure 2.2 p 46'


def test_bonfante_fr_ex_3():
    assert (
coord(C("et"),
      root(V("convoquer"),
           subj(N("directeur"),
                det(D("le"))),
           comp(N("conseil"),
                det(D("le")))),
      root(V("proposer"),
           comp(N("plan"),
                det(D("un"))),
           comp(P("à"),
                comp(N("conseil"),
                     det(D("un")))).pro(True))).t('f').realize()   
    ) == 'Le directeur convoquera le conseil et lui proposera un plan. ',\
    ' Exercice 2.4 p 48'


def test_bonfante_fr_ex_4():
    assert (
root(V("être").t('f'),
     coord(C("et"),
           subj(N("curé"),
                det(D("le"))),
           subj(N("maire"),
                det(D("le")),
                comp(P("de"),
                     mod(N("village"),
                         det(D("le")))))).a(','),
     mod(Adv("demain")).a(',').pos('pre'),
     mod(A("présent"),
         comp(P("à"),
              comp(N("cérémonie"),
                   det(D("le")))))).realize()   
    ) == 'Le curé et le maire du village, demain, seront présents à la cérémonie. ',\
    ' Exercice 2.6 p 48'


def test_bonfante_fr_ex_5():
    assert (
root(V("demander").t('pc').aux('êt'),
     subj(Pro("lui").c('nom')),
     mod(Pro("vous").c('dat')),
     comp(P("de"),
          comp(V("régler").t('b'),
               comp(N("problème"),
                    det(D("le")))))).realize()   
    ) == 'Il vous est demandé de régler le problème. ',\
    ' Figure 2.11 p 49'


def test_bonfante_fr_ex_6():
    assert (
root(V("désoler"),
     subj(Pro("lui").c('nom')),
     comp(Pro("que"),
          comp(V("être").t('s'),
               subj(Pro("elle").c('nom')),
               mod(A("furieux"),
                   comp(P("contre"),
                        comp(N("frère"),
                             det(D("son")))))))).typ({'refl': True}).realize()   
    ) == "Il se désole qu'elle soit furieuse contre son frère. ",\
    ' Figure 2.14 p 53'


def test_bonfante_fr_ex_7():
    assert (
root(V("tomber"),
     subj(N("garçon").n('p'),
          det(D("le")),
          comp(V("courir"),
               subj(Pro("qui"))))).realize()   
    ) == 'Les garçons qui courent tombent. ',\
    'p 54 (au pluriel et passé composé)'


def test_bonfante_fr_ex_8():
    assert (
root(V("être").t('ps'),
     subj(N("sorcier").g('f'),
          det(D("le"))),
     coord(C("et"),
           mod(V("condamner").t('pp'),
               comp(P("à"),
                    mod(N("mort")))),
           mod(V("torturer").t('pp')),
           mod(V("brûler").t('pp')))).realize()   
    ) == 'La sorcière fut condamnée à mort, torturée et brûlée. ',\
    ' Figure 2.19 p 58 / REM: sujet féminin pour vérifier les accords dans un coord'


def test_bonfante_fr_ex_9():
    assert (
root(V("être").t('pc'),
     subj(N("français").cap(True).n('p'),
          det(NO("2").nat(True)),
          mod(A("autre"))),
     coord(C("et"),
           mod(V("enlever").t('pp')),
           mod(V("libérer").t('pp'))).n('p'),
     comp(P("à"),
          comp(Q("Beyrouth")))).realize()   
    ) == 'Deux autres Français ont été enlevés et libérés à Beyrouth. ',\
    "p 59 - 2.22 / dépendances assez différentes... et on doit forcer l'accord des PP"


def test_bonfante_fr_ex_10():
    assert (
root(V("enlever").t('pc'),
     comp(N("français").cap(True),
          det(NO("2").nat(True)),
          mod(A("autre"))),
     comp(P("à"),
          comp(Q("Beyrouth")))).typ({'pas': True}).realize()   
    ) == 'Deux autres Français ont été enlevés à Beyrouth. ',\
    'p 59 - p 2.22 / variante sans coordination'


def test_bonfante_fr_ex_11():
    assert (
S(VP(V("enlever").t('pc'),
     NP(NO("2").nat(True),
        A("autre"),
        N("français").cap(True).n('p')),
     PP(P("à"),
        Q("Beyrouth")))).typ({'pas': True}).realize()   
    ) == 'Deux autres Français ont été enlevés à Beyrouth. ',\
    'p 59 - p 2.22 / variante sans coordination en constituants'


def test_bonfante_fr_ex_12():
    assert (
root(V("permettre").t('ip').n('p').pe(2).lier(True),
     comp(Pro("moi").pe(1).tn('')),
     comp(P("de"),
          comp(V("dire").t('b'),
               comp(Pro("vous").c('dat')),
               comp(Pro("que"),
                    comp(V("être").t('pc'),
                         subj(Pro("nous").c('nom')),
                         mod(A("sensible"),
                             mod(Adv("très"))),
                         comp(P("à"),
                              comp(N("évocation"),
                                   det(D("ce"))))))))).realize()   
    ) == 'Permettez-moi de vous dire que nous avons été très sensibles à cette évocation. ',\
    ' Figure 2.23 p 60'


def test_bonfante_fr_ex_13():
    assert (
root(V("faire").t('pc'),
     subj(N("conteur"),
          det(D("le"))),
     comp(V("jouer").t('b'),
          comp(N("enfant").n('p'),
               det(D("le"))))).realize()   
    ) == 'Le conteur a fait jouer les enfants. ',\
    ' Figure 2.25 p 61'


def test_bonfante_fr_ex_14():
    assert (
root(V("demander").t('pc').aux('êt'),
     subj(Pro("lui").c('nom')),
     comp(Pro("vous").c('dat')),
     comp(P("de"),
          comp(V("régler").t('b'),
               comp(N("problème"),
                    det(D("le")))))).realize()   
    ) == 'Il vous est demandé de régler le problème. ',\
    ' Figure 2.31 p 64'


def test_bonfante_fr_ex_15():
    assert (
coord(C("et"),
      root(V("soutenir"),
           subj(Pro("nous").c('nom')),
           comp(Pro("vous").c('acc')),
           mod(Adv("pleinement"))),
      root(V("être").pe(1).n('p'),
           mod(A("méfiant"))).typ({'neg': 'aucunement'})).realize()   
    ) == 'Nous vous soutenons pleinement et ne sommes aucunement méfiants. ',\
    '2.32 p 65'


def test_bonfante_fr_ex_16():
    assert (
root(V("mener"),
     subj(N("cabinet"),
          det(D("le")),
          mod(Q("Cadel"))),
     comp(N("conduite"),
          det(D("le")),
          comp(P("de"),
               comp(N("travail").n('p'),
                    det(D("le")))))).typ({'pas': True}).realize()   
    ) == 'La conduite des travaux est menée par le cabinet Cadel. ',\
    ' Figure 2.33 p 66 / REM: structure spécifiée à la forme active'


def test_bonfante_fr_ex_17():
    assert (
root(V("expliquer").t('c'),
     det(Pro("lui").c('nom')),
     comp(P("par"),
          comp(N("présence"),
               det(D("le")),
               comp(P("de"),
                    comp(Q("CRS"),
                         det(D("le").n('p'))))))).typ({'refl': True, 'mod': 'poss'}).cap(False).realize()   
    ) == "il pourrait s'expliquer par la présence des CRS",\
    ' Figure 2.34 p 66-67 / REM: utilise la modalité et réflexivité'


def test_bonfante_fr_ex_18():
    assert (
root(V("faire").t('pc'),
     subj(Pro("eux").c('nom')),
     comp(V("subir").t('b'),
          comp(N("choc"),
               det(D("un")),
               mod(A("électrique"))).n('p'),
          comp(Pro("lui").c('dat')))).realize()   
    ) == 'Ils lui ont fait subir des chocs électriques. ',\
    " 2.36 p 67 / la racine devrait être 'subir' avec auxiliaire faire..."


def test_bonfante_fr_ex_19():
    assert (
root(V("être"),
     subj(Q("ASE"),
          det(D("le"))).a(','),
     subj(Pro("ce")),
     comp(N("chose"),
          mod(A("autre")))).realize()   
    ) == "L'ASE, c'est autre chose. ",\
    ' Figure 2.37 p 68 '


def test_bonfante_fr_ex_20():
    assert (
root(V("être"),
     subj(Pro("ce")),
     comp(N("lieu"),
          det(D("un")),
          mod(A("commun")),
          comp(P("de"),
               comp(V("dire").t('b'))))).realize()   
    ) == "C'est un lieu commun de dire. ",\
    ' Figure 2.38 p 68'


def test_bonfante_fr_ex_21():
    assert (
root(V("être").n('p'),
     subj(Pro("ce")),
     mod(N("type").n('p'),
         det(D("le")),
         mod(A("différent")).pos('pre'),
         comp(N("mafia").n('p'),
              det(D("de")))),
     mod(V("organiser").n('p'),
         subj(Pro("qui")),
         comp(Pro("lui").c('acc')))).realize()   
    ) == "Ce sont les différents types de mafias qui l'organisent. ",\
    '2.39 p 69'


def test_bonfante_fr_ex_22():
    assert (
root(V("tomber"),
     subj(N("garçon"),
          det(D("le")),
          mod(V("courir"),
              subj(Pro("qui"))))).realize()   
    ) == 'Le garçon qui court tombe. ',\
    ' Figure 2.39 p 70 '


def test_bonfante_fr_ex_23():
    assert (
root(N("tour").a(','),
     det(NO("3").nat(True)),
     comp(Pro("dont"),
          mod(A("prochain"),
              det(D("le"))),
          mod(V("avoir").t('f'),
              comp(N("lieu")),
              comp(P("à"),
                   comp(Q("Faulx")))))).realize()   
    ) == 'Trois tours, dont le prochain aura lieu à Faulx. ',\
    ' Figure 2.40 p 70'


def test_bonfante_fr_ex_24():
    assert (
root(V("toucher").t('p'),
     coord(C("et"),
           subj(N("tâche"),
                det(D("de")),
                mod(A("multiple")).pos('pre')),
           subj(N("démarche"))).n('p'),
     comp(P("à"),
          comp(N("bâtiment"),
               det(D("le")),
               mod(A("paroissial"))).n('p'))).realize()   
    ) == 'De multiples tâches et démarches touchent aux bâtiments paroissiaux. ',\
    "Figure 2.41 p 71 / REM: verbe au présent pour voir l'accord du sujet de la coordonnée"


def test_bonfante_fr_ex_25():
    assert (
root(A("âgé"),
     coord(C("et"),
           subj(N("fille"),
                det(D("un"))),
           subj(N("garçon"),
                det(NO("2").nat(True)))),
     mod(Adv("respectivement")),
     comp(P("de"),
          comp(N("an"),
               coord(C("et"),
                     det(NO("23")),
                     det(NO("24")),
                     det(NO("14")))))).realize()   
    ) == 'Une fille et deux garçons âgés respectivement de 23, 24 et 14 ans. ',\
    'Figure 2.42 p 71'


def test_bonfante_fr_ex_26():
    assert (
root(V("arriver"),
     subj(Pro("elle").c('nom')),
     comp(P("à"),
          comp(Q("Paris"))),
     coord(C("mais"),
           mod(A("confiant")),
           mod(V("connaître").t('b'),
               mod(P("sans")).pos('pre'),
               comp(N("ville"),
                    det(D("le")))))).realize()   
    ) == 'Elle arrive à Paris confiante mais sans connaître la ville. ',\
    ' Exercice 2.49 p 72'


def test_bonfante_fr_ex_27():
    assert (
root(V("être"),
     comp(A("difficile")),
     subj(V("trouver").t('b'),
          comp(N("livre"),
               det(D("un")),
               comp(Pro("dont"),
                    comp(V("dire").t('s'),
                         subj(Pro("on")),
                         comp(Pro("que"),
                              comp(V("traduire").t('pc'),
                                   comp(Pro("lui").c('acc'))).typ({'neg': True, 'pas': True}))).typ({'mod': 'poss'}))))).typ({'pas': True, 'neg': False}).realize()   
    ) == "Il a été difficile de trouver un livre dont on puisse dire qu'il n'a pas été traduit. ",\
    'Exercice 2.51 p 72'


def test_bonfante_fr_ex_28():
    assert (
coord(C("et"),
      root(V("perdre"),
           subj(N("automobile"),
                det(D("le"))),
           comp(N("roue"),
                det(D("son")),
                mod(A("gauche")))),
      root(V("décoller"),
           comp(P("pour"),
                coord(C("et"),
                      comp(V("retourner").t('b')).typ({'refl': True}),
                      comp(V("terminer").t('b'),
                           comp(N("course"),
                                det(D("son"))),
                           comp(P("sur"),
                                comp(N("toit"),
                                     det(D("le"))))))))).t('pc').realize()   
    ) == "L'automobile a perdu sa roue gauche et a décollé pour se retourner et terminer sa course sur le toit. ",\
    ' Figure 3.4 p 86'


def test_bonfante_fr_ex_29():
    assert (
root(V("indiquer").t('c'),
     subj(Pro("lui").c('nom')),
     comp(C("si"),
          comp(V("plaider"),
               subj(Pro("lui").c('nom')),
               mod(A("coupable"),
                   comp(P("de"),
                        comp(N("fait").n('p'),
                             det(D("le")),
                             comp(Pro("qui"),
                                  comp(V("être"),
                                       comp(V("reprocher").t('pp'),
                                            comp(Pro("lui").c('dat'))))))))))).typ({'mod': 'nece'}).realize()   
    ) == "Il devrait indiquer s'il plaide coupable des faits qui lui sont reprochés. ",\
    ' Exemple 3.1 p 82 / REM: relative avec attributs'

