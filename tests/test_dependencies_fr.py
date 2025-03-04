import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..','src')))

from pyrealb import *
load("fr")

pomme = comp(N("pomme"), det(D("le")))
pommeS = subj(N("pomme"), det(D("le")))
gars = subj(N("garçon").n("p"), det(D("le")))
addToLexicon({"John": {"N": {"g": "m", "tab": "n4"}}})
addToLexicon({"Mary": {"N": {"g": "f", "tab": "n16"}}})

def test_dependencies_fr_1():
    assert (
root(V("être").t('p'),
     comp(A("gris")),
     subj(N("souris"),
          det(D("le")),
          mod(V("manger").t('pc'),
              comp(Pro("que")).pos('pre'),
              subj(N("chat").n('p'),
                   det(D("le")))))).realize()   
    ) == 'La souris que les chats ont mangée est grise. ',\
    'Phrase avec attribut, de plus le passé composé avec avoir est accordé correctement... '


def test_dependencies_fr_2():
    assert (
root(N("cadeau").n('p')).cap(False).realize()   
    ) == 'cadeaux',\
    'Phrase sans capitale'


def test_dependencies_fr_3():
    assert (
root(N("cadeau").n('p'),
     mod(A("beau"))).realize()   
    ) == 'Beaux cadeaux. ',\
    'Accord adjectif'


def test_dependencies_fr_4():
    assert (
root(N("gens").n('p'),
     det(D("le")),
     mod(A("vulgaire").pos('pre'))).cap(False).realize()   
    ) == 'les vulgaires gens',\
    'Adjectif pré-posé'


def test_dependencies_fr_5():
    assert (
root(N("père"),
     det(D("le")),
     mod(P("de"),
         mod(N("fille"),
             det(D("mon").pe(1))))).realize()   
    ) == 'Le père de ma fille. ',\
    'Complément du nom'


def test_dependencies_fr_6():
    assert (
root(V("agir").t('pc'),
     comp(Adv("conformément"),
          mod(P("à"),
              mod(N("loi"),
                  det(D("le"))))),
     subj(Pro("je").pe(1).n('p'))).typ({'neg': True}).realize()   
    ) == "Nous n'avons pas agi conformément à la loi. ",\
    'Phrase négative avec accord du verbe'


def test_dependencies_fr_7():
    assert (
root(V("travailler").t('pc'),
     comp(Adv("bien")),
     subj(Pro("je").pe(2))).typ({'mod': 'nece'}).realize()   
    ) == 'Tu as dû bien travailler. ',\
    'Phrase au passé avec modalité de nécessité'


def test_dependencies_fr_8():
    assert (
root(V("être").t('p'),
     coord(C("et"),
           subj(N("garçon"),
                det(D("le"))),
           subj(N("fille"),
                det(D("le")))),
     comp(A("gentil"))).realize()   
    ) == 'Le garçon et la fille sont gentils. ',\
    'Coordination'


def test_dependencies_fr_9():
    assert (
root(V("parler").t('p'),
     coord(C("et"),
           subj(N("boulanger").g('f'),
                det(D("le"))),
           subj(N("client").g('f'),
                det(D("le"))))).typ({'int': 'yon'}).realize()   
    ) == 'La boulangère et la cliente parlent-elles? ',\
    'Coordination et interrogation'


def test_dependencies_fr_10():
    assert (
root(V("parler").t('p'),
     coord(C("et"),
           subj(N("boulanger").g('f'),
                det(D("le"))),
           subj(N("vendeur"),
                det(D("le"))),
           subj(N("client").g('f'),
                det(D("le"))))).realize()   
    ) == 'La boulangère, le vendeur et la cliente parlent. ',\
    'Coordination'


def test_dependencies_fr_11():
    assert (
root(V("manger"),
     comp(N("gâteau"),
          det(D("le"))),
     subj(N("enfant").n('p'),
          det(D("le")))).typ({'pas': True}).realize()   
    ) == 'Le gâteau est mangé par les enfants. ',\
    'Passif avec élision'


def test_dependencies_fr_12():
    assert (
root(V("manger"),
     comp(N("gâteau"),
          det(D("le"))),
     subj(N("enfant").n('p'),
          det(D("le"))).pro(True)).realize()   
    ) == 'Ils mangent le gâteau. ',\
    'Pronominalisation du sujet'


def test_dependencies_fr_13():
    assert (
root(V("manger"),
     comp(N("gâteau"),
          det(D("le"))).pro(True),
     subj(N("enfant").n('p'),
          det(D("le")))).realize()   
    ) == 'Les enfants le mangent. ',\
    'Pronominalisation du complément'


def test_dependencies_fr_14():
    assert (
root(V("manger"),
     comp(N("gâteau"),
          det(D("le"))).pro(True),
     subj(N("enfant").n('p'),
          det(D("le")))).typ({'pas': True}).realize()   
    ) == 'Il est mangé par les enfants. ',\
    'Pronominalisation du complément au passif'


def test_dependencies_fr_15():
    assert (
root(V("manger"),
     comp(N("souris"),
          det(D("le"))),
     subj(N("chat").g('f').n('p'),
          det(D("le")))).realize()   
    ) == 'Les chattes mangent la souris. ',\
    'Phrase affirmative'


def test_dependencies_fr_16():
    assert (
root(V("dévorer").t('pc'),
     comp(N("souris"),
          det(D("le")),
          mod(A("gris")),
          mod(Q("Wow!"))).tag("a",{'href': 'http: #  wikipedia.org/cat', 'target': '_blank'}),
     subj(N("chat").g('f').n('p').tag('b').tag('i'),
          det(D("le")),
          mod(Q("super")))).typ({'neg': True}).realize()   
    ) == 'Les <i><b>chattes</b></i> super n\'ont pas dévoré <a href="http: #  wikipedia.org/cat" target="_blank">la souris grise Wow!</a>',\
    'Phrase avec tag HTML'


def test_dependencies_fr_17():
    assert (
root(V("être").t('p'),
     comp(A("gris")),
     subj(N("souris").n('p'),
          det(D("le")))).typ({'neg': True}).realize()   
    ) == 'Les souris ne sont pas grises. ',\
    'Accord avec être'


def test_dependencies_fr_18():
    assert (
root(V("avoir").t('cp'),
     comp(N("ami").g('f'),
          det(NO("2")),
          mod(A("beau"))),
     subj(Pro("je").n('p').pe(2))).typ({'neg': 'plus'}).realize()   
    ) == "Vous n'auriez plus eu 2 belles amies. ",\
    'Négation avec adjectif au pluriel'


def test_dependencies_fr_19():
    assert (
root(V("évanouir").t('pc'),
     comp(P("à"),
          mod(DT("1979-05-21T12:00:00").dOpt({'hour': False, 'minute': False, 'second': False}))),
     subj(N("John"))).typ({'neg': True}).realize()   
    ) == "John ne s'est pas évanoui au lundi 21 mai 1979. ",\
    'Phrase avec une date et un ajout au dictionnaire'


def test_dependencies_fr_20():
    assert (
root(V("évanouir").t('pc'),
     comp(P("à"),
          mod(DT("1979-05-21T12:00:00").dOpt({'hour': False, 'minute': False, 'second': False}))),
     coord(C("et"),
           subj(N("John")),
           subj(N("Mary")))).typ({'neg': True}).realize()   
    ) == 'John et Mary ne se sont pas évanouis au lundi 21 mai 1979. ',\
    'Phrase avec coordination ou et date.'


def test_dependencies_fr_21():
    assert (
root(V("aimer")).add(comp(N("pomme"),det(D("le")))).add(subj(N("garçon").n('p'),det(D("le"))),0).realize()   
    ) == 'Les garçons aiment la pomme. ',\
    'Phrase construite par morceaux'


def test_dependencies_fr_22():
    assert (
root(V("venir").t('pc'),
     comp(Adv("hier")),
     coord(C("et"),
           subj(N("fruit"),
                det(D("le")))).add(subj(N("pomme"),det(D("le")))).add(subj(N("garçon").n('p'),det(D("le"))))).realize()   
    ) == 'Le fruit, la pomme et les garçons sont venus hier. ',\
    'Coordination construite par morceaux'


def test_dependencies_fr_23():
    assert (
root(V("arriver").t('pc'),
     comp(Adv("hier")),
     coord(C("et"),
           subj(N("orange"),
                det(D("le")))).add(subj(N("pomme"),det(D("le"))))).realize()   
    ) == "L'orange et la pomme sont arrivées hier. ",\
    'Coordination avec attribut au pluriel'


def test_dependencies_fr_24():
    assert (
root(V("manger").t('pc'),
     comp(N("pomme"),
          det(D("le"))),
     subj(Pro("je"))).realize()   
    ) == 'Il a mangé la pomme. ',\
    'Phrase de base'


def test_dependencies_fr_25():
    assert (
root(V("manger").t('pc'),
     comp(N("pomme"),
          det(D("le"))).tag('i').pro(True),
     subj(Pro("je"))).realize()   
    ) == "Il <i>l'</i> a mangée. ",\
    'Pronominalisation combinée avec tag HTML'


def test_dependencies_fr_26():
    assert (
root(N("pomme").tag('i'),
     det(D("le")),
     mod(V("manger").aux('êt').t('pc'),
         subj(Pro("qui")))).realize()   
    ) == 'La <i>pomme</i> qui est mangée. ',\
    'Phrase avec attribut'


def test_dependencies_fr_27():
    assert (
root(N("pomme").tag('i'),
     det(D("le")),
     mod(V("manger").t('pc'),
         comp(Pro("que")).pos('pre'),
         subj(Pro("je")))).cap(False).realize()   
    ) == "la <i>pomme</i> qu'il a mangée",\
    'NP avec relative'


def test_dependencies_fr_28():
    assert (
S(NP(D("le"),
     N("pomme").tag('i'),
     SP(Pro("que"),
        Pro("je"),
        VP(V("manger").t('pc'))))).realize()   
    ) == "La <i>pomme</i> qu'il a mangée. ",\
    'Pronominalisation qui couvre toute la phrase... (non implanté en dépendences)'


def test_dependencies_fr_29():
    assert (
root(V("manger"),
     comp(N("gâteau"),
          det(D("le"))),
     subj(N("enfant").n('p'),
          det(D("le")))).typ({'pas': True}).realize()   
    ) == 'Le gâteau est mangé par les enfants. ',\
    'Passive'


def test_dependencies_fr_30():
    assert (
root(V("agir").t('c'),
     comp(Adv("conformément"),
          mod(P("à"),
              mod(N("loi"),
                  det(D("le"))))),
     subj(Pro("je").pe(1).n('p'))).typ({'mod': 'nece'}).realize()   
    ) == 'Nous devrions agir conformément à la loi. ',\
    'avec PP'


def test_dependencies_fr_31():
    assert (
root(N("chat").n('p'),
     det(D("le")),
     coord(C("et"),
           mod(V("courir")),
           mod(V("sauter")),
           mod(V("manger"))),
     comp(N("souris"),
          det(D("le")))).realize()   
    ) == 'Les chats courent, sautent et mangent la souris. ',\
    "Sujet d'une coordination de verbes"


def test_dependencies_fr_32():
    assert (
root(V("être"),
     comp(P("de"),
          mod(N("exercice"),
              det(D("le")),
              mod(A("aisé"),
                  mod(P("à"),
                      mod(V("réussir").t('b'),
                          comp(P("de"),
                               mod(N("coup"),
                                   det(D("le")),
                                   mod(A("premier"))))))))),
     subj(Pro("ce"))).typ({'neg': True}).realize()   
    ) == "Ce n'est pas de l'exercice aisé à réussir du premier coup. ",\
    'Multiples élisions'


def test_dependencies_fr_33():
    assert (
root(Q(""),
     coord(C("et"),
           subj(N("ami").g('f'),
                det(D("mon").pe(1))),
           subj(N("étudiant").g('f'),
                det(D("le")),
                mod(A("vieux")))),
     mod(V("recevoir").t('pc'),
         comp(Pro("que")).pos('pre'),
         subj(N("homme"),
              det(D("ce"))))).realize()   
    ) == 'Mon amie et la vieille étudiante que cet homme a reçues. ',\
    'Élisions, euphonies et cod coordonné placé avant le verbe'


def test_dependencies_fr_34():
    assert (
root(N("chat").tag('b'),
     det(D("le").tag('i'))).realize()   
    ) == '<i>Le</i> <b>chat</b>. ',\
    'Top level,capitalization with HTML tags.'


def test_dependencies_fr_35():
    assert (
root(V("demander").t('pc'),
     comp(N("adresse"),
          det(D("mon"))).pro(True),
     comp(P("à"),
          mod(N("parent").n('p'),
              det(D("mon")))).pro(True),
     subj(Pro("je").pe(2))).realize()   
    ) == 'Tu la leur as demandée. ',\
    "Pronominalisation de l'objet direct et de l'objet indirect (datif)"


def test_dependencies_fr_36():
    assert (
root(V("parler").t('pc'),
     comp(P("à"),
          mod(N("ami").g('f'),
              det(D("mon")))).pro(True),
     comp(P("de"),
          mod(N("problème"),
              det(D("mon")))).pro(True),
     subj(Pro("je"))).realize()   
    ) == 'Il lui en a parlé. ',\
    'Pronominalisation de deux objets indirects'


def test_dependencies_fr_37():
    assert (
root(V("manger").t('pc'),
     subj(N("souris"),
          det(D("le"))),
     comp(N("fromage"),
          det(D("le")))).typ({'int': 'wad', 'pas': True}).realize()   
    ) == 'Par quoi est-ce que le fromage a été mangé? ',\
    'Question au passif avec verbe au passé composé'


def test_dependencies_fr_38():
    assert (
root(V("manger"),
     comp(N("fromage"),
          det(D("le"))),
     subj(Pro("elles"))).typ({'pas': True}).realize()   
    ) == 'Le fromage est mangé par elles. ',\
    'Question au passif avec verbe avec pronom'


def test_dependencies_fr_39():
    assert (
root(N("fille"),
     coord(C("ou"),
           det(NO("2")),
           det(NO("3"))),
     coord(C("et"),
           mod(A("jeune")),
           mod(A("joli"))).pos('pre')).realize()   
    ) == '2 ou 3 jeunes et jolies filles. ',\
    'Accord avec des nombres et adjectifs coordonnés'


def test_dependencies_fr_40():
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
    'Deux coordinations complexes'


def test_dependencies_fr_41():
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
                                   comp(Pro("lui").c('acc'))).typ({'neg': True, 'pas': True}))).typ({'mod': 'poss'}))))).typ({'pas': True, 'neg': True}).realize()   
    ) == "Il n'a pas été difficile de trouver un livre dont on puisse dire qu'il n'a pas été traduit. ",\
    'Subordonnées modifiées imbriquées'


def test_dependencies_fr_42():
    assert (
root(V("être"),
     comp(A("difficile")),
     subj(V("trouver").t('b'),
          comp(N("livre"),
               det(D("un")),
               comp(Pro("que"),
                    comp(V("traduire").t('pc'),
                         subj(Pro("lui").c('nom'))).typ({'neg': True, 'pas': False}))))).typ({'pas': True, 'neg': True}).realize()   
    ) == "Il n'a pas été difficile de trouver un livre qu'il n'a pas traduit. ",\
    'Subordonnées modifiées imbriquées - bis'


def test_dependencies_fr_43():
    assert (
root(V("toucher").t('pr'),
     coord(C("et"),
           subj(N("tâche"),
                det(D("de")),
                mod(A("multiple")).pos('pre')),
           subj(N("démarche"))).n('p'),
     comp(P("à"),
          comp(N("bâtiment"),
               det(D("le")),
               mod(A("paroissial"))).n('p'))).realize()   
    ) == 'De multiples tâches et démarches touchant aux bâtiments paroissiaux. ',\
    "Propagation d'option dans un coord"


def test_dependencies_fr_44():
    assert (
root(V("adresser"),
     subj(N("place").n('p'),
          det(D("le")),
          comp(P("de"),
               comp(N("accueil")))),
     comp(P("en"),
          comp(N("priorité"))),
     comp(P("à"),
          comp(N("parent").n('p'),
               det(D("le")),
               comp(Pro("qui"),
                    coord(C("et"),
                          comp(V("travailler")),
                          comp(V("avoir"),
                               comp(N("possibilité"),
                                    det(D("de")),
                                    comp(P("de"),
                                         comp(N("garde"),
                                              comp(P("pour"),
                                                   comp(N("enfant"),
                                                        det(D("leur")))))))).typ({'neg': True})))))).typ({'refl': True}).realize()   
    ) == "Les places d'accueil s'adressent en priorité aux parents qui travaillent et n'ont pas de possibilité de garde pour leur enfant. ",\
    "Sujet d'une relative avec coordination de verbes"

def test_dependencies_fr_45():
    # exemple de https://www.lacheret.com/Xinha/UPLOAD/syntaxe-cours-4-2016.pdf (p 12)
    assert(
root(V("avoir"),
     subj(N("jeune").n("p"),
          det(D("un")),
          coord(C("et"),
                mod(A("masqué")),
                mod(A("armé")))),
     coord(C("et"),
           comp(V("piller").t("pc"),
                comp(N("magasin").n("p"),
                     det(D("un")))),
           comp(V("brûler").t("pp").n("s"),
                coord(C("et"),
                      comp(N("pneu").n("p"),
                           det(D("un"))),
                      comp(N("voiture").n("p"),
                           det(D("un"))))))).realize()
    ) == "Des jeunes masqués et armés ont ont pillé des magasins et brûlé des pneus et des voitures. ",\
    "Multiples coordinations"

    # exemples tirés  de
    # Conversion et améliorations de corpus du français annotés en Universal Dependencies
    # B. Guillaume, M.-C. de Marneffe, and G. Perrier, {Revue TAL}, 60(2):71-95, 2019

def test_dependencies_fr_46():
    assert(
  root(V('être'),
       subj(N('poids'),
            det(D('le'))),
       comp(A('égal'),
            mod(P('à'),
                comp(N('poids'),
                     det(D('le')),
                     mod(P('de'),
                         comp(N('fluide'),
                              det(D('le')),
                              mod(V('déplacer').t("pp")))))))).realize()
          ) == "Le poids est égal au poids du fluide déplacé. ",\
    "Figure 1 Guillaume et al."

def test_dependencies_fr_47():
    assert(
  root(V("être"),
       subj(N("problème"),
            det(D("le")),
            mod(A("seul")).pos("pre")),
       comp(Pro("que"),
            comp(V("avoir"),
                 subj(Pro("lui").c("nom")),
                 comp(N("pouvoir").n("p"),
                      det(Q("de")),
                      mod(A("super").pos("pre").lier()))
                 ).typ({"neg": True}))).realize()
          ) == "Le seul problème est qu'il n'a pas de super-pouvoirs. ",\
    "Figure 2 Guillaume et al."

def test_dependencies_fr_48():
    assert(
  root(V('créer').t("pa").aux("êt"),
       subj(Pro('eux').c("nom")),
       comp(N('temps'),
            mod(P("en")).pos("pre"),
            mod(A('même')).pos("pre"),
            comp(C('que'),
                 mod(N('tribun').n("p"),
                     det(D("le")),
                     mod(P('de'),
                         mod(N('plèbe'),
                             det(D('le')))))))).realize()
    ) == "Ils furent créés en même temps que les tribuns de la plèbe. ",\
    "Figure 3 Guillaume et al."

def test_dependencies_fr_49():
    assert(
  root(Pro("elle").c("nom"),
      coord(C("et"),
           comp(V("fonctionner").t("pc")),
           comp(V("continuer"),
                comp(P("à"),
                     mod(V("fonctionner").t("b"))))),
      comp(P("sur"),
           mod(N("base"),
                det(D("le")),
                mod(P("de"),
                     mod(N("équilibre"),
                          det(D("un"))))))).realize()
    ) == "Elle a fonctionné et continue à fonctionner sur la base d'un équilibre. ",\
    "Figure 8 Guillaume et al."

def test_dependencies_fr_50():
    assert(
      root(V("voir"),
           subj(Pro("moi").c("nom")),
           comp(V("être"),
                mod(C("que")).pos("pre"),
                subj(Pro("toi").c("nom")),
                mod(A("malade")))).realize()
    ) == "Je vois que tu es malade. ",\
    "Figure 10 Guillaume et al."