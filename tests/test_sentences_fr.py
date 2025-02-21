import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..','src')))

from pyrealb import *
load("fr")

addToLexicon({"John":{"N":{"g":"m","tab":"n4"}}})
addToLexicon({"Mary":{"N":{"g":"f","tab":"n16"}}})

def test_sentences_fr_1():
    assert (
S(NP(D("le"),
     N("souris"),
     SP(Pro("que"),
        NP(D("le"),
           N("chat").n('p')),
        VP(V("manger").t('pc')))),
  VP(V("être").t('p'),
     AP(A("gris")))).realize()   
    ) == 'La souris que les chats ont mangée est grise. ',\
    'Phrase avec attribut, de plus le passé composé avec avoir est accordé correctement...'


def test_sentences_fr_2():
    assert (
S(N("cadeau").n('p')).cap(False).realize()   
    ) == 'cadeaux',\
    'Phrase sans capitale'


def test_sentences_fr_3():
    assert (
S(NP(A("beau"),
     N("cadeau").n('p'))).realize()   
    ) == 'Beaux cadeaux. ',\
    'Accord adjectif'


def test_sentences_fr_4():
    assert (
NP(D("le"),
   N("gens").n('p'),
   A("vulgaire").pos('pre')).realize()   
    ) == 'les vulgaires gens',\
    'Adjectif pré-posé'


def test_sentences_fr_5():
    assert (
S(NP(D("le"),
     N("père"),
     PP(P("de"),
        NP(D("mon").pe(1),
           N("fille"))))).realize()   
    ) == 'Le père de ma fille. ',\
    'Accord adjectif'


def test_sentences_fr_6():
    assert (
S(Pro("je").pe(1).n('p'),
  VP(V("agir").t('pc'),
     AdvP(Adv("conformément"),
          PP(P("à"),
             NP(D("le"),
                N("loi")))))).typ({'neg': True}).realize()   
    ) == "Nous n'avons pas agi conformément à la loi. ",\
    'Phrase négative avec accord du verbe'


def test_sentences_fr_7():
    assert (
S(Pro("je").pe(2),
  VP(V("travailler").t('pc'),
     AdvP(Adv("bien")))).typ({'mod': 'nece'}).realize()   
    ) == 'Tu as dû bien travailler. ',\
    'Phrase au passé avec modalité de nécessité'


def test_sentences_fr_8():
    assert (
S(CP(C("et"),
     NP(D("le"),
        N("garçon")),
     NP(D("le"),
        N("fille"))),
  VP(V("être").t('p'),
     A("gentil"))).realize()   
    ) == 'Le garçon et la fille sont gentils. ',\
    'Coordination'


def test_sentences_fr_9():
    assert (
S(CP(C("et"),
     NP(D("le"),
        N("boulanger").g('f')),
     NP(D("le"),
        N("client").g('f'))),
  VP(V("parler").t('p'))).typ({'int': 'yon'}).realize()   
    ) == 'La boulangère et la cliente parlent-elles? ',\
    'Coordination et interrogation'


def test_sentences_fr_10():
    assert (
S(CP(C("et"),
     NP(D("le"),
        N("boulanger").g('f')),
     NP(D("le"),
        N("vendeur")),
     NP(D("le"),
        N("client").g('f'))),
  VP(V("parler").t('p'))).realize()   
    ) == 'La boulangère, le vendeur et la cliente parlent. ',\
    'Coordination'


def test_sentences_fr_11():
    assert (
S(NP(D("le"),
     N("enfant").n('p')),
  VP(V("manger"),
     NP(D("le"),
        N("gâteau")))).typ({'pas': True}).realize()   
    ) == 'Le gâteau est mangé par les enfants. ',\
    'Passif avec élision'


def test_sentences_fr_12():
    assert (
S(NP(D("le"),
     N("enfant").n('p')).pro(True),
  VP(V("manger"),
     NP(D("le"),
        N("gâteau")))).realize()   
    ) == 'Ils mangent le gâteau. ',\
    'Pronominalisation du sujet'


def test_sentences_fr_13():
    assert (
S(NP(D("le"),
     N("enfant").n('p')),
  VP(V("manger"),
     NP(D("le"),
        N("gâteau")).pro(True))).realize()   
    ) == 'Les enfants le mangent. ',\
    'Pronominalisation du complément'


def test_sentences_fr_14():
    assert (
S(NP(D("le"),
     N("enfant").n('p')),
  VP(V("manger"),
     NP(D("le"),
        N("gâteau")).pro(True))).typ({'pas': True}).realize()   
    ) == 'Il est mangé par les enfants. ',\
    'Pronominalisation du complément au passif'


def test_sentences_fr_15():
    assert (
S(NP(D("le"),
     N("chat").g('f').n('p')),
  VP(V("manger"),
     NP(D("le"),
        N("souris")))).realize()   
    ) == 'Les chattes mangent la souris. ',\
    'Phrase affirmative'


def test_sentences_fr_16():
    assert (
S(NP(D("le"),
     Q("super"),
     N("chat").g('f').n('p').tag('b').tag('i')),
  VP(V("dévorer").t('pc'),
     NP(D("le"),
        N("souris"),
        A("gris"),
        Q("Wow!")).tag("a",{'href': 'http:#wikipedia.org/cat', 'target': '_blank'}))).typ({'neg': True}).realize()   
    ) == 'Les super <i><b>chattes</b></i> n\'ont pas dévoré <a href="http:#wikipedia.org/cat" target="_blank">la souris grise Wow!</a>',\
    'Phrase avec tag HTML'


def test_sentences_fr_17():
    assert (
S(NP(D("le"),
     N("souris").n('p')),
  VP(V("être").t('p'),
     AP(A("gris")))).typ({'neg': True}).realize()   
    ) == 'Les souris ne sont pas grises. ',\
    'Accord avec être'


def test_sentences_fr_18():
    assert (
S(Pro("je").n('p').pe(2),
  VP(V("avoir").t('cp'),
     NP(NO("2"),
        A("beau"),
        N("ami").g('f')))).typ({'neg': 'plus'}).realize()   
    ) == "Vous n'auriez plus eu 2 belles amies. ",\
    'Négation avec adjectif au pluriel'


def test_sentences_fr_19():
    assert (
S(NP(N("John")),
  VP(V("évanouir").t('pc'),
     DT("1979-05-21T12:00:00").dOpt({'hour': False, 'minute': False, 'second': False}))).typ({'neg': True}).realize()   
    ) == "John ne s'est pas évanoui le lundi 21 mai 1979. ",\
    'Phrase avec une date et un ajout au dictionnaire'


def test_sentences_fr_20():
    assert (
S(CP(C("et"),
     NP(N("John")),
     NP(N("Mary"))),
  VP(V("évanouir").t('pc'),
     PP(DT("1979-05-21T12:00:00").dOpt({'hour': False, 'minute': False, 'second': False})))).typ({'neg': True, 'refl': True}).realize()   
    ) == 'John et Mary ne se sont pas évanouis le lundi 21 mai 1979. ',\
    'Phrase avec coordination ou et date. '


def test_sentences_fr_21():
    assert (
S(VP().add(V("aimer")).add(NP(D("le"),N("pomme")))).add(NP(D("le"),N("garçon").n('p')),0).realize()   
    ) == 'Les garçons aiment la pomme. ',\
    'Phrase construite par morceaux'


def test_sentences_fr_22():
    assert (
S(CP(C("et"),
     NP(D("le"),
        N("fruit"))).add(NP(D("le"),N("pomme"))).add(NP(D("le"),N("garçon").n('p'))),
  VP(V("venir").t('pc'),
     Adv("hier"))).realize()   
    ) == 'Le fruit, la pomme et les garçons sont venus hier. ',\
    'Coordination construite par morceaux'


def test_sentences_fr_23():
    assert (
S(CP(C("et"),
     NP(D("le"),
        N("orange"))).add(NP(D("le"),N("pomme"))),
  VP(V("arriver").t('pc'),
     Adv("hier"))).realize()   
    ) == "L'orange et la pomme sont arrivées hier. ",\
    'Coordination avec attribut au pluriel'


def test_sentences_fr_24():
    assert (
S(Pro("je"),
  VP(V("manger").t('pc'),
     NP(D("le"),
        N("pomme")))).realize()   
    ) == 'Il a mangé la pomme. ',\
    'Phrase de base'


def test_sentences_fr_25():
    assert (
S(Pro("je"),
  VP(V("manger").t('pc'),
     NP(D("le"),
        N("pomme")).tag('i').pro(True))).realize()   
    ) == "Il <i>l'</i> a mangée. ",\
    'Pronominalisation combinée avec tag HTML'


def test_sentences_fr_26():
    assert (
S(NP(D("le"),
     N("pomme").tag('i'),
     SP(Pro("qui"),
        VP(V("manger").aux('êt').t('pc'))))).realize()   
    ) == 'La <i>pomme</i> qui est mangée. ',\
    'Phrase avec attribut'


def test_sentences_fr_27():
    assert (
NP(D("le"),
   N("pomme").tag('i'),
   SP(Pro("que"),
      Pro("je"),
      VP(V("manger").t('pc')))).realize()   
    ) == "la <i>pomme</i> qu'il a mangée",\
    'NP avec relative'


def test_sentences_fr_28():
    assert (
S(NP(D("le"),
     N("pomme").tag('i'),
     SP(Pro("que"),
        Pro("je"),
        VP(V("manger").t('pc')))).pro(True)).realize()   
    ) == 'Elle. ',\
    'Pronominalisation qui couvre toute la phrase...'


def test_sentences_fr_29():
    assert (
S(NP(D("le"),
     N("enfant").n('p')),
  VP(V("manger"),
     NP(D("le"),
        N("gâteau")))).typ({'pas': True}).realize()   
    ) == 'Le gâteau est mangé par les enfants. ',\
    'Passive'


def test_sentences_fr_30():
    assert (
S(Pro("je").pe(1).n('p'),
  VP(V("agir").t('c'),
     AdvP(Adv("conformément"),
          PP(P("à"),
             NP(D("le"),
                N("loi")))))).typ({'mod': 'nece'}).realize()   
    ) == 'Nous devrions agir conformément à la loi. ',\
    'avec PP'


def test_sentences_fr_31():
    assert (
S(NP(D("le"),
     N("chat").n('p')),
  CP(C("et"),
     VP(V("courir")),
     VP(V("sauter")),
     VP(V("manger"),
        NP(D("le"),
           N("souris"))))).realize()   
    ) == 'Les chats courent, sautent et mangent la souris. ',\
    "Sujet d'une coordination de verbes"


def test_sentences_fr_32():
    assert (
S(Pro("ce"),
  VP(V("être"),
     PP(P("de"),
        NP(D("le"),
           N("exercice"),
           AP(A("aisé"),
              PP(P("à"),
                 VP(V("réussir").t('b'),
                    PP(P("de"),
                       NP(D("le"),
                          A("premier"),
                          N("coup")))))))))).typ({'neg': True}).realize()   
    ) == "Ce n'est pas de l'exercice aisé à réussir du premier coup. ",\
    'Multiples élisions'


def test_sentences_fr_33():
    assert (
S(CP(C("et"),
     NP(D("mon").pe(1),
        N("ami").g('f')),
     NP(D("le"),
        A("vieux"),
        N("étudiant").g('f'))),
  SP(Pro("que"),
     NP(D("ce"),
        N("homme")),
     VP(V("recevoir").t('pc')))).realize()   
    ) == 'Mon amie et la vieille étudiante que cet homme a reçues. ',\
    'Élisions, euphonies et cod coordonné placé avant le verbe'


def test_sentences_fr_34():
    assert (
S(NP(D("le").tag('i'),
     N("chat").tag('b'))).realize()   
    ) == '<i>Le</i> <b>chat</b>. ',\
    'Top level,capitalization with HTML tags. '


def test_sentences_fr_35():
    assert (
S(Pro("je").pe(2),
  VP(V("demander").t('pc'),
     NP(D("mon"),
        N("adresse")).pro(True),
     PP(P("à"),
        NP(D("mon"),
           N("parent").n('p'))).pro(True))).realize()   
    ) == 'Tu la leur as demandée. ',\
    "Pronominalisation de l'objet direct et de l'objet indirect (datif)"


def test_sentences_fr_36():
    assert (
S(Pro("je"),
  VP(V("parler").t('pc'),
     PP(P("à"),
        NP(D("mon"),
           N("ami").g('f'))).pro(True),
     PP(P("de"),
        NP(D("mon"),
           N("problème"))).pro(True))).realize()   
    ) == 'Il lui en a parlé. ',\
    'Pronominalisation de deux objets indirects'


def test_sentences_fr_37():
    assert (
S(Pro("je"),
  VP(V("aller").t('pc'),
     Adv("hier"),
     PP(P("à"),
        NP(D("le"),
           N("maison"))))).typ({'neg': True}).realize()   
    ) == "Il n'est pas allé hier à la maison. ",\
    "Position de l'adverbe dans une négation"


def test_sentences_fr_38():
    assert (
S(Pro("je"),
  VP(V("aller").t('pc'),
     Adv("souvent"),
     PP(P("à"),
        NP(D("le"),
           N("maison"))),
     Adv("sûrement"))).typ({'neg': True}).realize()   
    ) == "Il n'est pas souvent allé à la maison sûrement. ",\
    "Position d'adverbes séparés"


def test_sentences_fr_39():
    assert (
S(Pro("je"),
  VP(V("aller").t('pc'),
     Adv("souvent").pos('post'),
     PP(P("à"),
        NP(D("le"),
           N("maison"))))).typ({'neg': True}).realize()   
    ) == "Il n'est pas allé souvent à la maison. ",\
    "Position d'un adverbe avec .pos()"


def test_sentences_fr_40():
    assert (
S(NP(D("le"),
     N("chat")),
  VP(V("manger"),
     Adv("bien"),
     Adv("souvent"),
     NP(D("le"),
        N("souris")))).typ({'pas': True}).realize()   
    ) == 'La souris est bien souvent mangée par le chat. ',\
    "Position d'adverbes contigus"


def test_sentences_fr_41():
    assert (
S(S(VP(V("trouver").t('b'),
       NP(D("un"),
          N("livre"),
          SP(Pro("dont"),
             Pro("on"),
             VP(V("dire").t('s'),
                SP(Pro("que"),
                   VP(V("traduire").t('pc'),
                      Pro("lui").c('acc')).typ({'neg': True, 'pas': True}))).typ({'mod': 'poss'}))))),
  VP(V("être"),
     A("difficile"))).typ({'pas': True, 'neg': True}).realize()   
    ) == "Il n'a pas été difficile de trouver un livre dont on puisse dire qu'il n'a pas été traduit. ",\
    'Subordonnées modifiées imbriquées'


def test_sentences_fr_42():
    assert (
S(S(VP(V("trouver").t('b'),
       NP(D("un"),
          N("livre"),
          SP(Pro("que"),
             Pro("lui").c('nom'),
             VP(V("traduire").t('pc')).typ({'neg': True, 'pas': False}))))),
  VP(V("être"),
     A("difficile"))).typ({'pas': True, 'neg': True}).realize()   
    ) == "Il n'a pas été difficile de trouver un livre qu'il n'a pas traduit. ",\
    'Subordonnées modifiées imbriquées - bis'


def test_sentences_fr_43():
    assert (
CP(C("et"),
   NP(D("de"),
      A("multiple").pos('pre'),
      N("tâche")),
   N("démarche")).n('p').realize()   
    ) == 'de multiples tâches et démarches',\
    "propagation d'option dans un CP"


def test_sentences_fr_44():
    assert (
S(Pro("lui").c('nom'),
  VP(V("indiquer").t('c'),
     SP(C("si"),
        Pro("lui").c('nom'),
        VP(V("plaider"),
           AP(A("coupable"),
              PP(P("de"),
                 NP(D("le"),
                    N("fait").n('p'),
                    SP(Pro("qui"),
                       VP(V("être"),
                          V("reprocher").t('pp'),
                          Pro("lui").c('dat')))))))))).typ({'mod': 'nece'}).realize()   
    ) == "Il devrait indiquer s'il plaide coupable des faits qui lui sont reprochés. ",\
    'NP avec une relative contenant un attribut'


def test_sentences_fr_45():
    assert (
NP(D("un"),
   N("personne"),
   AP(Adv("très"),
      A("beau"))).realize()   
    ) == 'une personne très belle',\
    'accord dans un AP'


def test_sentences_fr_46():
    assert (
NP(D("un"),
   AP(Adv("très"),
      A("beau")),
   N("personne")).realize()   
    ) == 'une très belle personne',\
    'accord dans un AP'


def test_sentences_fr_47():
    assert (
S(NP(Pro("je")).pe(2),
  VP(V("être"),
     AP(A("intelligent")))).g('f').realize()   
    ) == 'Tu es intelligente. ',\
    '1. VP'


def test_sentences_fr_48():
    assert (
S(NP(Pro("je")).pe(2),
  VP(V("travailler"),
     AdvP(Adv("bien")))).realize()   
    ) == 'Tu travailles bien. ',\
    '2. VP'


def test_sentences_fr_49():
    assert (
S(NP(D("le"),
     N("visiteur")),
  VP(V("dormir")).t('i'),
  NP(D("le"),
     N("matin"))).realize()   
    ) == 'Le visiteur dormait le matin. ',\
    '3. VP'


def test_sentences_fr_50():
    assert (
S(NP(Pro("je")).pe(3).g('f'),
  VP(V("manger"),
     NP(D("un"),
        N("gâteau")).n('p')).t('i')).realize()   
    ) == 'Elle mangeait des gâteaux. ',\
    '4. VP'


def test_sentences_fr_51():
    assert (
S(NP(D("ce"),
     N("gâteau")),
  VP(V("être")),
  AP(A("excellent"))).realize()   
    ) == 'Ce gâteau est excellent. ',\
    '5. VP'


def test_sentences_fr_52():
    assert (
S(NP(Pro("je").pe(1).n('p')),
  VP(V("mettre"),
     NP(D("le"),
        N("courrier"),
        PP(P("sur"),
           NP(D("le"),
              N("table")))))).realize()   
    ) == 'Nous mettons le courrier sur la table. ',\
    '6. VP'


def test_sentences_fr_53():
    assert (
S(NP(Pro("je").pe(1)),
  VP(V("parler"),
     PP(P("à"),
        NP(D("un"),
           N("fille"))))).realize()   
    ) == 'Je parle à une fille. ',\
    '7. VP'


def test_sentences_fr_54():
    assert (
S(NP(Pro("je").pe(3).n('p')),
  VP(V("arrêter"),
     AdvP(Adv("rapidement")),
     NP(D("le"),
        N("discussion"))).t('ps')).realize()   
    ) == 'Ils arrêtèrent rapidement la discussion. ',\
    '8. VP'


def test_sentences_fr_55():
    assert (
S(NP(D("le"),
     N("petit")).g('f'),
  VP(V("garder"),
     NP(D("le"),
        N("montre")))).realize()   
    ) == 'La petite garde la montre. ',\
    '9. VP'


def test_sentences_fr_56():
    assert (
S(NP(Pro("je")).pe(3),
  VP(V("refuser")).t('f')).realize()   
    ) == 'Il refusera. ',\
    '10. VP'


def test_sentences_fr_57():
    assert (
S(Pro("je"),
  VP(V("manger"),
     NP(D("un"),
        N("pomme"),
        V("laisser").t('pp'),
        PP(P("par"),
           N("terre"))))).realize()   
    ) == 'Il mange une pomme laissée par terre. ',\
    '11.VP + NP(avec pp accordé seul) + PP'


def test_sentences_fr_58():
    assert (
NP(D("le"),
   N("fenêtre").n('p'),
   V("ouvrir").t('pp')).realize()   
    ) == 'les fenêtres ouvertes',\
    '12. NP(avec pp accordé seul)'


def test_sentences_fr_59():
    assert (
AP(A("grand").g('f')).realize()   
    ) == 'grande',\
    '1. AP'


def test_sentences_fr_60():
    assert (
AP(A("content").g('f')).realize()   
    ) == 'contente',\
    '2. AP'


def test_sentences_fr_61():
    assert (
AP(AdvP(Adv("très")),
   A("grand").g('f')).realize()   
    ) == 'très grande',\
    '3. AP'


def test_sentences_fr_62():
    assert (
AdvP(Adv("évidemment")).realize()   
    ) == 'évidemment',\
    '1. AdvP'


def test_sentences_fr_63():
    assert (
AdvP(Adv("fort")).realize()   
    ) == 'fort',\
    '2. AdvP'


def test_sentences_fr_64():
    assert (
AdvP(Adv("rapidement")).realize()   
    ) == 'rapidement',\
    '3. AdvP'


def test_sentences_fr_65():
    assert (
PP(P("dans"),
   NP(D("le"),
      N("ville"))).realize()   
    ) == 'dans la ville',\
    '1. PP'


def test_sentences_fr_66():
    assert (
PP(P("de"),
   NP(D("ce"),
      N("femme"))).realize()   
    ) == 'de cette femme',\
    '2. PP'


def test_sentences_fr_67():
    assert (
PP(P("à"),
   NP(D("le"),
      N("maison"))).realize()   
    ) == 'à la maison',\
    '3. PP'


def test_sentences_fr_68():
    assert (
PP(P("par"),
   NP(D("le"),
      N("fenêtre")).n('p')).realize()   
    ) == 'par les fenêtres',\
    '4. PP'


def test_sentences_fr_69():
    assert (
PP(P("avec"),
   NP(D("mon"),
      N("femme"))).realize()   
    ) == 'avec sa femme',\
    '5. PP'


def test_sentences_fr_70():
    assert (
CP(C("ou"),
   Pro("moi").pe(2),
   Pro("je").pe(3).g('f')).realize()   
    ) == 'toi ou elle',\
    '0. CP'


def test_sentences_fr_71():
    assert (
CP(C("ou"),
   Pro("moi").pe(1),
   Pro("moi").pe(2),
   Pro("je").pe(3).g('f')).realize()   
    ) == 'moi, toi ou elle',\
    '1. CP'


def test_sentences_fr_72():
    assert (
NP(N("jeu").n('p').a(';'),
   N("jouet").n('p').a(';'),
   N("cadeau").n('p')).realize()   
    ) == 'jeux ; jouets ; cadeaux',\
    '3. CP'


def test_sentences_fr_73():
    assert (
NP(D("le"),
   N("vaisseau").n('p').lier(True),
   N("mère").n('p')).realize()   
    ) == 'les vaisseaux-mères',\
    '4. CP'


def test_sentences_fr_74():
    assert (
NP(D("un"),
   N("mur"),
   A("rouge").lier(True),
   A("orange")).realize()   
    ) == 'un mur rouge-orange',\
    '5. CP'


def test_sentences_fr_75():
    assert (
CP(NP(D("le"),
      N("garçon")),
   NP(D("le"),
      N("fille")),
   C("et")).realize()   
    ) == 'le garçon et la fille',\
    '6. CP'


def test_sentences_fr_76():
    assert (
CP(NP(D("le"),
      N("garçon")),
   C("et"),
   NP(D("le"),
      N("fille"))).realize()   
    ) == 'le garçon et la fille',\
    '7. CP'


def test_sentences_fr_77():
    assert (
CP(C("et"),
   NP(D("le"),
      N("garçon")),
   NP(D("le"),
      N("fille"))).realize()   
    ) == 'le garçon et la fille',\
    '8. CP'


def test_sentences_fr_78():
    assert (
NP(D("le"),
   N("chose"),
   SP(Pro("que"),
      NP(Pro("je").pe(2)),
      VP(V("dire").t('pc')))).realize()   
    ) == 'la chose que tu as dite',\
    '1. SP'


def test_sentences_fr_79():
    assert (
NP(D("le"),
   N("souris"),
   SP(Pro("que"),
      NP(D("le"),
         N("chat")),
      VP(V("manger")))).realize()   
    ) == 'la souris que le chat mange',\
    '2. SP'


def test_sentences_fr_80():
    assert (
NP(Pro("ce"),
   SP(Pro("dont"),
      NP(Pro("je").pe(2)),
      VP(V("parler")))).realize()   
    ) == 'ce dont tu parles',\
    '3. SP'


def test_sentences_fr_81():
    assert (
S(NP(D("le"),
     N("personne").n('p'),
     SP(Pro("que"),
        Pro("je").pe('1').n('p'),
        VP(V("rencontrer").t('pc'))))).realize()   
    ) == 'Les personnes que nous avons rencontrées. ',\
    '4. SP + pp(avoir)'


def test_sentences_fr_82():
    assert (
S(NP(D("le"),
     N("fleur").n('p'),
     SP(Pro("que"),
        NP(D("le"),
           N("garçon").n('p')),
        VP(Pro("je").pe(1).n('p'),
           V("offrir").t('pc')))),
  VP(V("être").t('pc'),
     A("joli"))).realize()   
    ) == 'Les fleurs que les garçons nous ont offertes ont été jolies. ',\
    '5. SP + pp(avoir) + pp(être)'


def test_sentences_fr_83():
    assert (
S(NP(N("pierre").n('p'),
     SP(Pro("qui"),
        VP(V("rouler")))),
  VP(V("amasser"),
     NP(N("mousse")))).typ({'neg': True}).realize()   
    ) == "Pierres qui roulent n'amassent pas mousse. ",\
    '6. SP(qui)'


def test_sentences_fr_84():
    assert (
S(NP(D("le"),
     N("dame").n('p'),
     SP(P("à"),
        Pro("qui"),
        Pro("je").pe(1).n('s'),
        VP(V("parler").t('pc')))),
  VP(V("être").t('pc'),
     A("joli"))).realize()   
    ) == "Les dames à qui j'ai parlé ont été jolies. ",\
    '7. SP(à qui)'


def test_sentences_fr_85():
    assert (
NP(D("le"),
   A("petit"),
   N("chien").g('f'),
   A("blanc"),
   PP(P("de"),
      NP(D("mon").pe(1),
         N("voisin").g('f').n('p')))).realize()   
    ) == 'la petite chienne blanche de mes voisines',\
    '1. NP + PP'


def test_sentences_fr_86():
    assert (
NP(D("le"),
   N("père"),
   PP(P("de"),
      NP(D("mon").pe(1),
         N("fille")))).realize()   
    ) == 'le père de ma fille',\
    '2. NP + PP'


def test_sentences_fr_87():
    assert (
AP(AdvP(Adv("très")),
   A("fier"),
   PP(P("de"),
      NP(D("mon").pe(3),
         N("famille")))).realize()   
    ) == 'très fier de sa famille',\
    '3. AP + AdvP + PP + NP'


def test_sentences_fr_88():
    assert (
AdvP(Adv("conformément"),
     PP(P("à"),
        NP(D("le"),
           N("loi")))).realize()   
    ) == 'conformément à la loi',\
    '4. AdvP + PP + NP'


def test_sentences_fr_89():
    assert (
S(NP(D("le"),
     N("peintre")),
  VP(V("réparer"),
     NP(D("le"),
        N("mur"))),
  PP(P("dans"),
     NP(D("le"),
        N("cour")))).realize()   
    ) == 'Le peintre répare le mur dans la cour. ',\
    '5. S + NP + VP + PP'


def test_sentences_fr_90():
    assert (
S(NP(D("le"),
     N("pomme").n('p')),
  VP(V("être"),
     A("beau"))).realize()   
    ) == 'Les pommes sont belles. ',\
    'Les pommes sont belles.'


def test_sentences_fr_91():
    assert (
S(NP(D("le"),
     N("pomme")),
  VP(V("être"),
     CP(C("et"),
        A("beau"),
        A("joli")))).realize()   
    ) == 'La pomme est belle et jolie. ',\
    'La pomme est belle et jolie'


def test_sentences_fr_92():
    assert (
S(NP(D("le"),
     N("fleur").n('p'),
     SP(Pro("que"),
        NP(D("le"),
           N("garçon").n('p')),
        VP(V("offrir").t('pc'),
           PP(P("à"),
              NP(D("le"),
                 N("fille"),
                 A("jeune")).n('p')).pro(True)))),
  VP(V("être").t('pc'),
     A("joli"))).realize()   
    ) == 'Les fleurs que les garçons leur ont offertes ont été jolies. ',\
    "Pronominalisation d'un PP"


def test_sentences_fr_93():
    assert (
S(NP(D("un"),
     N("poule")).n('p'),
  VP(V("mordre").t('p'))).realize()   
    ) == 'Des poules mordent. ',\
    'Sans pronominalisation'


def test_sentences_fr_94():
    assert (
S(NP(D("un"),
     N("poule")).n('p').pro(True),
  VP(V("mordre").t('p'))).realize()   
    ) == 'Elles mordent. ',\
    'Pronominalisation sujet'


def test_sentences_fr_95():
    assert (
S(NP(D("un"),
     N("poule")).n('p'),
  VP(V("mordre").t('p'),
     NP(D("un"),
        N("enfant")))).realize()   
    ) == 'Des poules mordent un enfant. ',\
    'Sans pronominalisation (avec cd)'


def test_sentences_fr_96():
    assert (
S(NP(D("un"),
     N("poule")).n('p'),
  VP(V("mordre").t('p'),
     NP(D("un"),
        N("enfant")).pro(True))).realize()   
    ) == 'Des poules le mordent. ',\
    'Pronominalisation cd'


def test_sentences_fr_97():
    assert (
S(NP(D("un"),
     N("poule")).n('p').pro(True),
  VP(V("mordre").t('p'),
     NP(D("un"),
        N("enfant")).pro(True))).realize()   
    ) == 'Elles le mordent. ',\
    'Pronominalisation sujet+cd'


def test_sentences_fr_98():
    assert (
S(NP(D("un"),
     N("poule")).n('p'),
  VP(V("mordre").t('p'),
     NP(D("un"),
        N("enfant")),
     PP(P("dans"),
        NP(D("un"),
           N("maison"))))).realize()   
    ) == 'Des poules mordent un enfant dans une maison. ',\
    'Sans pronominalisation (avec cd+ci)'


def test_sentences_fr_99():
    assert (
S(NP(D("un"),
     N("poule")).n('p'),
  VP(V("mordre").t('p'),
     NP(D("un"),
        N("enfant")),
     PP(P("dans"),
        NP(D("un"),
           N("maison")).pro(True)))).realize()   
    ) == 'Des poules mordent un enfant dans elle. ',\
    'Pronominalisation ci'


def test_sentences_fr_100():
    assert (
S(NP(D("un"),
     N("poule")).n('p').pro(True),
  VP(V("mordre").t('p'),
     NP(D("un"),
        N("enfant")).pro(True),
     PP(P("dans"),
        NP(D("un"),
           N("maison")).pro(True)))).realize()   
    ) == 'Elles le mordent dans elle. ',\
    'Pronominalisation sujet+cd+ci'


def test_sentences_fr_101():
    assert (
S(NP(D("le"),
     N("soldat").n('p')),
  VP(V("trouver").t('pc'),
     NP(D("le"),
        N("fille")))).realize()   
    ) == 'Les soldats ont trouvé la fille. ',\
    'Phrase simple'


def test_sentences_fr_102():
    assert (
S(NP(D("le"),
     N("soldat").n('p')),
  VP(V("trouver").t('pc'),
     NP(D("le"),
        N("fille")))).typ({'pas': True}).realize()   
    ) == 'La fille a été trouvée par les soldats. ',\
    'Phrase passive avec sujet et cd'


def test_sentences_fr_103():
    assert (
S(NP(D("le"),
     N("soldat").n('p')),
  VP(V("trouver").t('pc'))).typ({'pas': True}).realize()   
    ) == 'Il a été trouvé par les soldats. ',\
    'Phrase passive avec sujet, sans cd'


def test_sentences_fr_104():
    assert (
S(VP(V("trouver").t('pc'),
     NP(D("le"),
        N("fille")))).typ({'pas': True}).realize()   
    ) == 'La fille a été trouvée. ',\
    'Phrase passive avec cd, sans sujet'


def test_sentences_fr_105():
    assert (
S(NP(D("le"),
     N("sorcier")).g('f'),
  VP(V("être").t('ps'),
     CP(C("et"),
        VP(V("condamner"),
           PP(P("à"),
              N("mort"))),
        VP(V("torturer")),
        VP(V("brûler"))).t('pp'))).realize()   
    ) == 'La sorcière fut condamnée à mort, torturée et brûlée. ',\
    'attributs coordonnés'

