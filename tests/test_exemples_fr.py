import os, sys,datetime
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..','src')))

from pyrealb import *
load("fr")

addToLexicon({"John":{"N":{"g":"m","tab":"n4"}}})
addToLexicon({"Mary":{"N":{"g":"f","tab":"n16"}}})
pomme = NP(D("le"),N("pomme"));
gars = NP(D("le"),N("garçon").n("p"));

def test_exemples_fr_1():
    assert (
N("chat").realize()   
    ) == 'chat',\
    'Phrase complète:  chat'


def test_exemples_fr_2():
    assert (
Pro("moi").c('acc').realize()   
    ) == 'me',\
    'Phrase complète:  me'


def test_exemples_fr_3():
    assert (
Pro("moi").tn('').realize()   
    ) == 'moi',\
    'Phrase complète:  moi'


def test_exemples_fr_4():
    assert (
NP(D("le"),
   N("chat")).realize()   
    ) == 'le chat',\
    'Phrase complète:  le chat'


def test_exemples_fr_5():
    assert (
S(NP(D("le"),
     N("chat").n('p'))).realize()   
    ) == 'Les chats. ',\
    'Phrase complète:  Les chats. '


def test_exemples_fr_6():
    assert (
V("aller").t('ps').pe(2).n('p').realize()   
    ) == 'allâtes',\
    'Phrase complète:  allâtes'


def test_exemples_fr_7():
    assert (
V("aller").t('pc').pe(3).n('s').realize()   
    ) == 'est allé',\
    'Phrase complète:  est allé'


def test_exemples_fr_8():
    assert (
VP(V("aller").t('f').pe(1).n('p')).typ({'neg': True}).realize()   
    ) == "n'irons pas",\
    "Phrase complète:  n'irons pas"


def test_exemples_fr_9():
    assert (
VP(V("aller").t('pq').pe(2).n('s')).typ({'neg': True}).realize()   
    ) == "n'étais pas allé",\
    "Phrase complète:  n'étais pas allé"


def test_exemples_fr_10():
    assert (
S(NP(D("le"),
     N("chat").g('f').n('p')),
  VP(V("manger"),
     NP(D("le"),
        N("souris")))).realize()   
    ) == 'Les chattes mangent la souris. ',\
    'Phrase complète:  Les chattes mangent la souris. '


def test_exemples_fr_11():
    assert (
S(NP(D("le"),
     N("chat").g('f').n('p')),
  VP(V("manger"),
     NP(D("le"),
        N("souris")))).typ({'pas': True}).realize()   
    ) == 'La souris est mangée par les chattes. ',\
    'Phrase complète:  La souris est mangée par les chattes. '


def test_exemples_fr_12():
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
    'Phrase complète:  Les super <i><b>chattes</b></i> n\'ont pas dévoré <a href="http:#wikipedia.org/cat" target="_blank">la souris grise Wow!</a>'


def test_exemples_fr_13():
    assert (
S(NP(D("le"),
     N("souris").n('p')),
  VP(V("être"),
     AP(A("gris")))).typ({'neg': True}).realize()   
    ) == 'Les souris ne sont pas grises. ',\
    'Phrase complète:  Les souris ne sont pas grises. '


def test_exemples_fr_14():
    assert (
S(Pro("je").n('p').pe(2),
  VP(V("avoir").t('cp'),
     NP(NO("2"),
        A("beau"),
        N("ami").g('f')))).typ({'neg': 'plus'}).realize()   
    ) == "Vous n'auriez plus eu 2 belles amies. ",\
    "Phrase complète:  Vous n'auriez plus eu 2 belles amies. "


def test_exemples_fr_15():
    assert (
S(NP(N("John")),
  VP(V("évanouir").aux('êt').t('pc')),
  PP(P("à"),
     DT("1979-05-21T10:05:00"))).typ({'neg': True}).realize()   
    ) == "John ne s'est pas évanoui au lundi 21 mai 1979 à 10 h 5. ",\
    "Phrase complète:  John ne s'est pas évanoui au lundi 21 mai 1979 à 10 h 5. "


def test_exemples_fr_16():
    assert (
S(CP(C("et"),
     NP(N("John")),
     NP(N("Mary"))),
  VP(V("évanouir").t('pc')),
  PP(P("à"),
     DT("1979-05-21T10:05:00"))).typ({'neg': True}).realize()   
    ) == 'John et Mary ne se sont pas évanouis au lundi 21 mai 1979 à 10 h 5. ',\
    'Phrase complète:  John et Mary ne se sont pas évanouis au lundi 21 mai 1979 à 10 h 5. '


def test_exemples_fr_17():
    assert (
S(VP().add(V("aimer")).add(NP(D("le"),N("pomme")))).add(NP(D("le"),N("garçon").n('p')),0).realize()   
    ) == 'Les garçons aiment la pomme. ',\
    'Phrase complète:  Les garçons aiment la pomme. '


def test_exemples_fr_18():
    assert (
S(CP(C("et"),
     NP(D("le"),
        N("fruit"))).add(NP(D("le"),N("pomme"))).add(NP(D("le"),N("garçon").n('p'))),
  VP(V("venir").t('pc'),
     Adv("hier"))).realize()   
    ) == 'Le fruit, la pomme et les garçons sont venus hier. ',\
    'Phrase complète:  Le fruit, la pomme et les garçons sont venus hier. '


def test_exemples_fr_19():
    assert (
S(CP(C("et"),
     NP(D("le"),
        N("orange"))).add(NP(D("le"),N("pomme"))),
  VP(V("arriver").t('pc'),
     Adv("hier"))).realize()   
    ) == "L'orange et la pomme sont arrivées hier. ",\
    "Phrase complète:  L'orange et la pomme sont arrivées hier. "


def test_exemples_fr_20():
    assert (
S(Pro("je"),
  VP(V("manger").t('pc'),
     NP(D("le"),
        N("pomme")))).realize()   
    ) == 'Il a mangé la pomme. ',\
    'Phrase complète:  Il a mangé la pomme. '


def test_exemples_fr_21():
    assert (
S(Pro("je"),
  VP(V("manger").t('pc'),
     NP(D("le"),
        N("pomme")).tag('i').pro(True))).realize()   
    ) == "Il <i>l'</i> a mangée. ",\
    "Phrase complète:  Il <i>l'</i> a mangée. "


def test_exemples_fr_22():
    assert (
S(NP(D("le"),
     N("pomme").tag('i'),
     SP(Pro("qui"),
        VP(V("manger").aux('êt').t('pc'))))).realize()   
    ) == 'La <i>pomme</i> qui est mangée. ',\
    'Phrase complète:  La <i>pomme</i> qui est mangée. '


def test_exemples_fr_23():
    assert (
NP(D("le"),
   N("pomme").tag('i'),
   SP(Pro("que"),
      Pro("je"),
      VP(V("manger").t('pc')))).realize()   
    ) == "la <i>pomme</i> qu'il a mangée",\
    "Phrase complète:  la <i>pomme</i> qu'il a mangée"


def test_exemples_fr_24():
    assert (
S(NP(D("le"),
     N("pomme").tag('i'),
     SP(Pro("que"),
        Pro("je"),
        VP(V("manger").t('pc')))).pro(True)).realize()   
    ) == 'Elle. ',\
    'Phrase complète:  Elle. '


def test_exemples_fr_25():
    assert (
S(NP(D("le"),
     N("enfant").n('p')),
  VP(V("manger"),
     NP(D("le"),
        N("gâteau")))).typ({'pas': True}).realize()   
    ) == 'Le gâteau est mangé par les enfants. ',\
    'Phrase complète:  Le gâteau est mangé par les enfants. '


def test_exemples_fr_26():
    assert (
S(Pro("je").pe(1).n('p'),
  VP(V("agir").t('pc'),
     AdvP(Adv("conformément"),
          PP(P("à"),
             NP(D("le"),
                N("loi")))))).typ({'neg': True}).realize()   
    ) == "Nous n'avons pas agi conformément à la loi. ",\
    "Phrase complète:  Nous n'avons pas agi conformément à la loi. "


def test_exemples_fr_27():
    assert (
S(NP(D("le"),
     N("souris"),
     SP(Pro("que"),
        NP(D("le"),
           N("chat").n('p')),
        VP(V("manger").t('pc')))),
  VP(V("être"),
     AP(A("gris")))).realize()   
    ) == 'La souris que les chats ont mangée est grise. ',\
    'Phrase complète:  La souris que les chats ont mangée est grise. '


def test_exemples_fr_28():
    assert (
DT("2025-02-18 10:38:28.887096").realize()
    ) == 'le mardi 18 février 2025 à 10 h 38 min 28 s',\
    'Phrase complète:  None'


def test_exemples_fr_29():
    assert (
DT("2025-02-18 10:38:28.887132").nat(False).realize()
    ) == 'mardi 18/2/2025 10:38:28',\
    'Phrase complète:  None'


def test_exemples_fr_30():
    assert (
DT(datetime.datetime.today()).dOpt({'rtime': True, 'hour': False, "minute": False, 'second':False}).realize()
    ) == "aujourd'hui",\
    'Phrase complète:  None'


def test_exemples_fr_31():
    assert (
NO("1.847584").dOpt({'mprecision': 0}).realize()   
    ) == '2',\
    'Phrase complète:  2'


def test_exemples_fr_32():
    assert (
NO("1.847584").dOpt({'mprecision': 4}).realize()   
    ) == '1,8476',\
    'Phrase complète:  1,8476'


def test_exemples_fr_33():
    assert (
NO("1.847584").dOpt({'raw': False}).realize()   
    ) == '1,85',\
    'Phrase complète:  1,85'


def test_exemples_fr_34():
    assert (
NO("1.847584").dOpt({'raw': True}).realize()   
    ) == '1.847584',\
    'Phrase complète:  1.847584'


def test_exemples_fr_35():
    assert (
NO("125").dOpt({'nat': True}).realize()   
    ) == 'cent vingt-cinq',\
    'Phrase complète:  cent vingt-cinq'


def test_exemples_fr_36():
    assert (
NO("10").dOpt({'ord': True}).realize()   
    ) == 'dixième',\
    'Phrase complète:  dixième'


def test_exemples_fr_37():
    assert (
NP(NO("0"),
   N("avion")).realize()   
    ) == '0 avion',\
    'Phrase complète:  0 avion'


def test_exemples_fr_38():
    assert (
NP(NO("2"),
   N("avion")).realize()   
    ) == '2 avions',\
    'Phrase complète:  2 avions'


def test_exemples_fr_39():
    assert (
NP(NO("1.5").dOpt({'mprecision': 1}),
   N("livre")).realize()   
    ) == '1,5 livre',\
    'Phrase complète:  1,5 livre'


def test_exemples_fr_40():
    assert (
NP(NO("2.4").dOpt({'mprecision': 1}),
   N("livre")).realize()   
    ) == '2,4 livres',\
    'Phrase complète:  2,4 livres'


def test_exemples_fr_41():
    assert (
NP(NO("2"),
   A("rouge"),
   N("avion")).realize()   
    ) == '2 avions rouges',\
    'Phrase complète:  2 avions rouges'


def test_exemples_fr_42():
    assert (
N("pomme").realize()   
    ) == 'pomme',\
    'Phrase complète:  pomme'


def test_exemples_fr_43():
    assert (
S(Pro("lui").c('nom'),
  VP(V("donner").t('pc'),
     NP(D("un"),
        N("pomme")).pro(True),
     PP(P("à"),
        NP(D("le"),
           A("jeune"),
           N("femme"))))).realize()   
    ) == "Il l'a donnée à la jeune femme. ",\
    "Phrase complète:  Il l'a donnée à la jeune femme. "


def test_exemples_fr_44():
    assert (
S(Pro("lui").c('nom'),
  VP(V("donner").t('pc'),
     NP(D("un"),
        N("pomme")).pro(True),
     PP(P("à"),
        NP(D("le"),
           A("jeune"),
           N("femme"))).pro(True))).realize()   
    ) == 'Il la lui a donnée. ',\
    'Phrase complète:  Il la lui a donnée. '


def test_exemples_fr_45():
    assert (
S(Pro("je").pe(1),
  VP(V("mettre").t('pc'),
     NP(D("le"),
        N("lettre")),
     PP(P("sur"),
        NP(D("le"),
           N("table"))).pro(True))).realize()   
    ) == "J'y ai mis la lettre. ",\
    "Phrase complète:  J'y ai mis la lettre. "


def test_exemples_fr_46():
    assert (
S(Pro("je").pe(1),
  VP(V("mettre").t('pc'),
     NP(D("le"),
        N("lettre")).pro(True),
     PP(P("sur"),
        NP(D("le"),
           N("table"))).pro(True))).typ({'neg': True}).realize()   
    ) == "Je ne l'y ai pas mise. ",\
    "Phrase complète:  Je ne l'y ai pas mise. "


def test_exemples_fr_47():
    assert (
S(Pro("lui").c('nom'),
  VP(V("donner").t('pc'),
     NP(D("un"),
        N("pomme")).pro(True))).realize()   
    ) == "Il l'a donnée. ",\
    "Phrase complète:  Il l'a donnée. "


def test_exemples_fr_48():
    assert (
S(Pro("lui").c('nom'),
  VP(V("donner").t('pc'),
     NP(D("un"),
        N("pomme")).pro(True))).typ({'neg': True}).realize()   
    ) == "Il ne l'a pas donnée. ",\
    "Phrase complète:  Il ne l'a pas donnée. "


def test_exemples_fr_49():
    assert (
S(Pro("lui").c('nom'),
  VP(V("donner").t('pc'),
     NP(D("un"),
        N("pomme")).pro(True),
     PP(P("à"),
        NP(D("le"),
           N("fille"))))).typ({'neg': True}).realize()   
    ) == "Il ne l'a pas donnée à la fille. ",\
    "Phrase complète:  Il ne l'a pas donnée à la fille. "


def test_exemples_fr_50():
    assert (
S(Pro("lui").c('nom'),
  VP(V("donner").t('pc'),
     NP(D("un"),
        N("pomme")).pro(True),
     PP(P("à"),
        NP(D("le"),
           N("fille"))).pro(True))).typ({'neg': True}).realize()   
    ) == 'Il ne la lui a pas donnée. ',\
    'Phrase complète:  Il ne la lui a pas donnée. '


def test_exemples_fr_51():
    assert (
S(Pro("lui").c('nom'),
  VP(V("donner").t('pc'),
     NP(D("un"),
        N("pomme")).pro(True),
     PP(P("à"),
        NP(D("le"),
           N("fille"))).pro(True))).typ({'neg': True, 'pas': True}).realize()   
    ) == 'Elle ne lui a pas été donnée par lui. ',\
    'Phrase complète:  Elle ne lui a pas été donnée par lui. '


def test_exemples_fr_52():
    assert (
S(Pro("lui").c('nom'),
  VP(V("donner").t('pc'),
     NP(D("un"),
        N("chat")).pro(True),
     Pro("elle").c('dat'))).realize()   
    ) == 'Il le lui a donné. ',\
    'Phrase complète:  Il le lui a donné. '


def test_exemples_fr_53():
    assert (
S(NP(D("le"),
     N("chat").g('f')),
  VP(V("manger"),
     NP(D("le"),
        N("souris")))).t('f').realize()   
    ) == 'La chatte mangera la souris. ',\
    'Phrase complète:  La chatte mangera la souris. '


def test_exemples_fr_54():
    assert (
S(CP(C("et"),
     Pro("elle").tn(''),
     Pro("moi").tn('')),
  VP(V("aller"),
     PP(P("à"),
        NP(D("le"),
           N("plage"))))).t('pc').realize()   
    ) == 'Elle et moi sommes allés à la plage. ',\
    'Phrase complète:  Elle et moi sommes allés à la plage. '


def test_exemples_fr_55():
    assert (
S(NP(D("notre").pe(2),
     N("chef")),
  VP(V("aller"))).realize()   
    ) == 'Votre chef va. ',\
    'Phrase complète:  Votre chef va. '


def test_exemples_fr_56():
    assert (
S(NP(D("le"),
     N("chat")),
  VP(V("manger"),
     NP(D("le"),
        N("souris")))).typ({'int': 'yon'}).realize()   
    ) == 'Le chat mange-t-il la souris? ',\
    'Phrase complète:  Le chat mange-t-il la souris? '


def test_exemples_fr_57():
    assert (
S(NP(D("le"),
     N("chat")),
  VP(V("manger"),
     NP(D("le"),
        N("souris")))).typ({'int': 'yon', 'neg': True}).realize()   
    ) == 'Le chat ne mange-t-il pas la souris? ',\
    'Phrase complète:  Le chat ne mange-t-il pas la souris? '


def test_exemples_fr_58():
    assert (
S(NP(D("le"),
     N("chat")),
  VP(V("manger"),
     NP(D("le"),
        N("souris")))).typ({'int': 'yon', 'pas': True}).realize()   
    ) == 'La souris est-elle mangée par le chat? ',\
    'Phrase complète:  La souris est-elle mangée par le chat? '


def test_exemples_fr_59():
    assert (
S(Pro("je"),
  VP(V("manger"),
     NP(D("le"),
        N("fromage")))).typ({'int': 'yon'}).realize()   
    ) == 'Mange-t-il le fromage? ',\
    'Phrase complète:  Mange-t-il le fromage? '


def test_exemples_fr_60():
    assert (
S(Pro("je"),
  VP(V("manger").t('pc'),
     NP(D("le"),
        N("fromage")))).typ({'int': 'yon'}).realize()   
    ) == 'A-t-il mangé le fromage? ',\
    'Phrase complète:  A-t-il mangé le fromage? '


def test_exemples_fr_61():
    assert (
S(Pro("je"),
  VP(V("manger").t('pc'),
     NP(D("le"),
        N("fromage")))).typ({'neg': True, 'int': 'yon'}).realize()   
    ) == "N'a-t-il pas mangé le fromage? ",\
    "Phrase complète:  N'a-t-il pas mangé le fromage? "


def test_exemples_fr_62():
    assert (
S(Pro("je"),
  VP(V("manger").t('pc'),
     NP(D("le"),
        N("fromage")))).typ({'neg': True, 'int': 'tag'}).realize()   
    ) == "Il n'a pas mangé le fromage, n'est-ce pas? ",\
    "Phrase complète:  Il n'a pas mangé le fromage, n'est-ce pas? "


def test_exemples_fr_63():
    assert (
S(Pro("je").pe(2),
  VP(V("travailler").t('pc'),
     Adv("bien"))).typ({'mod': 'nece'}).realize()   
    ) == 'Tu as dû bien travailler. ',\
    'Phrase complète:  Tu as dû bien travailler. '


def test_exemples_fr_64():
    assert (
S(Pro("je"),
  VP(V("aller").t('pc'),
     Adv("hier"),
     PP(P("à"),
        NP(D("le"),
           N("maison"))))).typ({'neg': True}).realize()   
    ) == "Il n'est pas allé hier à la maison. ",\
    "Phrase complète:  Il n'est pas allé hier à la maison. "


def test_exemples_fr_65():
    assert (
S(Pro("je"),
  VP(V("aller").t('pc'),
     Adv("souvent"),
     PP(P("à"),
        NP(D("le"),
           N("maison"))),
     Adv("sûrement"))).typ({'neg': True}).realize()   
    ) == "Il n'est pas souvent allé à la maison sûrement. ",\
    "Phrase complète:  Il n'est pas souvent allé à la maison sûrement. "


def test_exemples_fr_66():
    assert (
S(Pro("je"),
  VP(V("aller").t('pc'),
     Adv("souvent").pos('post'),
     PP(P("à"),
        NP(D("le"),
           N("maison"))))).typ({'neg': True}).realize()   
    ) == "Il n'est pas allé souvent à la maison. ",\
    "Phrase complète:  Il n'est pas allé souvent à la maison. "


def test_exemples_fr_67():
    assert (
S(NP(D("le"),
     N("chat")),
  VP(V("manger"),
     Adv("bien"),
     Adv("souvent"),
     NP(D("le"),
        N("souris")))).typ({'pas': True}).realize()   
    ) == 'La souris est bien souvent mangée par le chat. ',\
    'Phrase complète:  La souris est bien souvent mangée par le chat. '


def test_exemples_fr_68():
    assert (
S(Pro("tout"),
  VP(V("sembler").t('pa'),
     V("fonctionner").t('bp'))).realize()   
    ) == 'Tout eut semblé avoir fonctionné. ',\
    'Phrase complète:  Tout eut semblé avoir fonctionné. '


def test_exemples_fr_69():
    assert (
S(Pro("lui"),
  VP(V("manger"),
     NP(D("le"),
        N("fromage")))).typ({'pas': True}).realize()   
    ) == 'Le fromage est mangé par lui. ',\
    'Phrase complète:  Le fromage est mangé par lui. '


def test_exemples_fr_70():
    assert (
NP(NO("2"),
   N("fille"),
   CP(C("et"),
      A("joli"),
      A("vieux"))).realize()   
    ) == '2 filles jolies et vieilles',\
    'Phrase complète:  2 filles jolies et vieilles'


def test_exemples_fr_71():
    assert (
NP(CP(C("ou"),
      NO("2"),
      NO("3")),
   N("fille"),
   CP(C("et"),
      A("jeune"),
      A("joli"))).realize()   
    ) == '2 ou 3 filles jeunes et jolies',\
    'Phrase complète:  2 ou 3 filles jeunes et jolies'


def test_exemples_fr_72():
    assert (
root(N("chat")).cap(False).realize()   
    ) == 'chat',\
    'Phrase complète:  chat'


def test_exemples_fr_73():
    assert (
root(Pro("moi").c('acc')).cap(False).realize()   
    ) == 'me',\
    'Phrase complète:  me'


def test_exemples_fr_74():
    assert (
root(Pro("moi").tn('')).cap(False).realize()   
    ) == 'moi',\
    'Phrase complète:  moi'


def test_exemples_fr_75():
    assert (
root(N("chat"),
     det(D("le"))).cap(False).realize()   
    ) == 'le chat',\
    'Phrase complète:  le chat'


def test_exemples_fr_76():
    assert (
S(NP(D("le"),
     N("chat").n('p'))).realize()   
    ) == 'Les chats. ',\
    'Phrase complète:  Les chats. '


def test_exemples_fr_77():
    assert (
root(V("aller").t('ps').pe(2).n('p')).cap(False).realize()   
    ) == 'allâtes',\
    'Phrase complète:  allâtes'


def test_exemples_fr_78():
    assert (
root(V("aller").t('pc').pe(3).n('s')).cap(False).realize()   
    ) == 'est allé',\
    'Phrase complète:  est allé'


def test_exemples_fr_79():
    assert (
root(V("aller").t('f').pe(1).n('p')).typ({'neg': True}).cap(False).realize()   
    ) == "n'irons pas",\
    "Phrase complète:  n'irons pas"


def test_exemples_fr_80():
    assert (
root(V("aller").t('pq').pe(2).n('s')).typ({'neg': True}).cap(False).realize()   
    ) == "n'étais pas allé",\
    "Phrase complète:  n'étais pas allé"


def test_exemples_fr_81():
    assert (
root(V("manger"),
     comp(N("souris"),
          det(D("le"))),
     subj(N("chat").g('f').n('p'),
          det(D("le")))).realize()   
    ) == 'Les chattes mangent la souris. ',\
    'Phrase complète:  Les chattes mangent la souris. '


def test_exemples_fr_82():
    assert (
root(V("manger"),
     comp(N("souris"),
          det(D("le"))),
     subj(N("chat").g('f').n('p'),
          det(D("le")))).typ({'pas': True}).realize()   
    ) == 'La souris est mangée par les chattes. ',\
    'Phrase complète:  La souris est mangée par les chattes. '


def test_exemples_fr_83():
    assert (
root(V("dévorer").t('pc'),
     comp(N("souris"),
          det(D("le")),
          mod(A("gris")),
          mod(Q("Wow!"))).tag("a",{'href': 'http:#wikipedia.org/cat', 'target': '_blank'}),
     subj(N("chat").g('f').n('p').tag('b').tag('i'),
          det(D("le")),
          mod(Q("super")).pos('pre'))).typ({'neg': True}).realize()   
    ) == 'Les super <i><b>chattes</b></i> n\'ont pas dévoré <a href="http:#wikipedia.org/cat" target="_blank">la souris grise Wow!</a>',\
    'Phrase complète:  Les super <i><b>chattes</b></i> n\'ont pas dévoré <a href="http:#wikipedia.org/cat" target="_blank">la souris grise Wow!</a>'


def test_exemples_fr_84():
    assert (
root(V("être"),
     comp(A("gris")),
     subj(N("souris").n('p'),
          det(D("le")))).typ({'neg': True}).realize()   
    ) == 'Les souris ne sont pas grises. ',\
    'Phrase complète:  Les souris ne sont pas grises. '


def test_exemples_fr_85():
    assert (
root(V("avoir").t('cp'),
     comp(N("ami").g('f'),
          det(NO("2")),
          mod(A("beau")).pos('pre')),
     subj(Pro("je").n('p').pe(2))).typ({'neg': 'plus'}).realize()   
    ) == "Vous n'auriez plus eu 2 belles amies. ",\
    "Phrase complète:  Vous n'auriez plus eu 2 belles amies. "


def test_exemples_fr_86():
    assert (
root(V("évanouir").aux('êt').t('pc'),
     subj(N("John")),
     mod(P("à"),
         mod(DT("1979-05-21T10:05:00")))).typ({'neg': True}).realize()   
    ) == "John ne s'est pas évanoui au lundi 21 mai 1979 à 10 h 5. ",\
    "Phrase complète:  John ne s'est pas évanoui au lundi 21 mai 1979 à 10 h 5. "


def test_exemples_fr_87():
    assert (
root(V("évanouir").t('pc'),
     coord(C("et"),
           subj(N("John")),
           subj(N("Mary"))),
     mod(P("à"),
         mod(DT("1979-05-21T10:05:00")))).typ({'neg': True}).realize()   
    ) == 'John et Mary ne se sont pas évanouis au lundi 21 mai 1979 à 10 h 5. ',\
    'Phrase complète:  John et Mary ne se sont pas évanouis au lundi 21 mai 1979 à 10 h 5. '


def test_exemples_fr_88():
    assert (
root(V("aimer"),
     comp(N("pomme"),
          det(D("le"))),
     subj(N("garçon").n('p'),
          det(D("le")))).realize()   
    ) == 'Les garçons aiment la pomme. ',\
    'Phrase complète:  Les garçons aiment la pomme. '


def test_exemples_fr_89():
    assert (
root(V("venir").t('pc'),
     comp(Adv("hier")),
     coord(C("et"),
           subj(N("fruit"),
                det(D("le"))),
           subj(N("pomme"),
                det(D("le"))),
           subj(N("garçon").n('p'),
                det(D("le"))))).realize()   
    ) == 'Le fruit, la pomme et les garçons sont venus hier. ',\
    'Phrase complète:  Le fruit, la pomme et les garçons sont venus hier. '


def test_exemples_fr_90():
    assert (
root(V("arriver").t('pc'),
     comp(Adv("hier")),
     coord(C("et"),
           subj(N("orange"),
                det(D("le"))),
           subj(N("pomme"),
                det(D("le"))))).realize()   
    ) == "L'orange et la pomme sont arrivées hier. ",\
    "Phrase complète:  L'orange et la pomme sont arrivées hier. "


def test_exemples_fr_91():
    assert (
root(V("manger").t('pc'),
     comp(N("pomme"),
          det(D("le"))),
     subj(Pro("je"))).realize()   
    ) == 'Il a mangé la pomme. ',\
    'Phrase complète:  Il a mangé la pomme. '


def test_exemples_fr_92():
    assert (
root(V("manger").t('pc'),
     comp(N("pomme"),
          det(D("le"))).tag('i').pro(True),
     subj(Pro("je"))).realize()   
    ) == "Il <i>l'</i> a mangée. ",\
    "Phrase complète:  Il <i>l'</i> a mangée. "


def test_exemples_fr_93():
    assert (
S(NP(D("le"),
     N("pomme").tag('i'),
     SP(Pro("qui"),
        VP(V("manger").aux('êt').t('pc'))))).realize()   
    ) == 'La <i>pomme</i> qui est mangée. ',\
    'Phrase complète:  La <i>pomme</i> qui est mangée. '


def test_exemples_fr_94():
    assert (
root(N("pomme").tag('i'),
     det(D("le")),
     mod(V("manger").t('pc'),
         comp(Pro("que")).pos('pre'),
         mod(Pro("je")).pos('pre'))).cap(False).realize()   
    ) == "la <i>pomme</i> qu'il a mangée",\
    "Phrase complète:  la <i>pomme</i> qu'il a mangée"


def test_exemples_fr_95():
    assert (
S(NP(D("le"),
     N("pomme").tag('i'),
     SP(Pro("que"),
        Pro("je"),
        VP(V("manger").t('pc')))).pro(True)).realize()   
    ) == 'Elle. ',\
    'Phrase complète:  Elle. '


def test_exemples_fr_96():
    assert (
root(V("manger"),
     comp(N("gâteau"),
          det(D("le"))),
     subj(N("enfant").n('p'),
          det(D("le")))).typ({'pas': True}).realize()   
    ) == 'Le gâteau est mangé par les enfants. ',\
    'Phrase complète:  Le gâteau est mangé par les enfants. '


def test_exemples_fr_97():
    assert (
root(V("agir").t('pc'),
     comp(Adv("conformément"),
          mod(P("à"),
              mod(N("loi"),
                  det(D("le"))))),
     subj(Pro("je").pe(1).n('p'))).typ({'neg': True}).realize()   
    ) == "Nous n'avons pas agi conformément à la loi. ",\
    "Phrase complète:  Nous n'avons pas agi conformément à la loi. "


def test_exemples_fr_98():
    assert (
root(V("être"),
     comp(A("gris")),
     subj(N("souris"),
          det(D("le")),
          mod(V("manger").t('pc'),
              comp(Pro("que")).pos('pre'),
              subj(N("chat").n('p'),
                  det(D("le")))))).realize()
    ) == 'La souris que les chats ont mangée est grise. ',\
    'Phrase complète:  La souris que les chats ont mangée est grise. '


def test_exemples_fr_99():
    assert (
root(DT("2025-02-18 10:38:28.887096")).cap(False).realize()   
    ) == 'le mardi 18 février 2025 à 10 h 38 min 28 s',\
    'Phrase complète:  None'


def test_exemples_fr_100():
    assert (
root(DT("2025-02-18 10:38:28.887132").nat(False)).cap(False).realize()   
    ) == 'mardi 18/2/2025 10:38:28',\
    'Phrase complète:  None'


def test_exemples_fr_101():
    assert (
root(DT(datetime.datetime.today()).dOpt({'rtime': True, 'hour': False, "minute": False, 'second':False})).cap(False).realize()
    ) == "aujourd'hui",\
    'Phrase complète:  None'


def test_exemples_fr_102():
    assert (
det(NO("1.847584").dOpt({'mprecision': 0})).cap(False).realize()   
    ) == '2',\
    'Phrase complète:  2'


def test_exemples_fr_103():
    assert (
det(NO("1.847584").dOpt({'mprecision': 4})).cap(False).realize()   
    ) == '1,8476',\
    'Phrase complète:  1,8476'


def test_exemples_fr_104():
    assert (
det(NO("1.847584").dOpt({'raw': False})).cap(False).realize()   
    ) == '1,85',\
    'Phrase complète:  1,85'


def test_exemples_fr_105():
    assert (
det(NO("1.847584").dOpt({'raw': True})).cap(False).realize()   
    ) == '1.847584',\
    'Phrase complète:  1.847584'


def test_exemples_fr_106():
    assert (
det(NO("125").dOpt({'nat': True})).cap(False).realize()   
    ) == 'cent vingt-cinq',\
    'Phrase complète:  cent vingt-cinq'


def test_exemples_fr_107():
    assert (
det(NO("10").dOpt({'ord': True})).cap(False).realize()   
    ) == 'dixième',\
    'Phrase complète:  dixième'


def test_exemples_fr_108():
    assert (
root(N("avion"),
     det(NO("0"))).cap(False).realize()   
    ) == '0 avion',\
    'Phrase complète:  0 avion'


def test_exemples_fr_109():
    assert (
root(N("avion"),
     det(NO("2"))).cap(False).realize()   
    ) == '2 avions',\
    'Phrase complète:  2 avions'


def test_exemples_fr_110():
    assert (
root(N("livre"),
     det(NO("1.5").dOpt({'mprecision': 1}))).cap(False).realize()   
    ) == '1,5 livre',\
    'Phrase complète:  1,5 livre'


def test_exemples_fr_111():
    assert (
root(N("livre"),
     det(NO("2.4").dOpt({'mprecision': 1}))).cap(False).realize()   
    ) == '2,4 livres',\
    'Phrase complète:  2,4 livres'


def test_exemples_fr_112():
    assert (
root(N("avion"),
     det(NO("2")),
     mod(A("rouge"))).cap(False).realize()   
    ) == '2 avions rouges',\
    'Phrase complète:  2 avions rouges'


def test_exemples_fr_113():
    assert (
root(N("pomme")).cap(False).realize()   
    ) == 'pomme',\
    'Phrase complète:  pomme'


def test_exemples_fr_114():
    assert (
root(V("donner").t('pc'),
     comp(N("pomme"),
          det(D("un"))).pro(True),
     comp(P("à"),
          mod(N("femme"),
              det(D("le")),
              mod(A("jeune")).pos('pre'))),
     subj(Pro("lui").c('nom'))).realize()   
    ) == "Il l'a donnée à la jeune femme. ",\
    "Phrase complète:  Il l'a donnée à la jeune femme. "


def test_exemples_fr_115():
    assert (
root(V("donner").t('pc'),
     comp(N("pomme"),
          det(D("un"))).pro(True),
     comp(P("à"),
          mod(N("femme"),
              det(D("le")),
              mod(A("jeune")).pos('pre'))).pro(True),
     subj(Pro("lui").c('nom'))).realize()   
    ) == 'Il la lui a donnée. ',\
    'Phrase complète:  Il la lui a donnée. '


def test_exemples_fr_116():
    assert (
root(V("mettre").t('pc'),
     comp(N("lettre"),
          det(D("le"))),
     comp(P("sur"),
          mod(N("table"),
              det(D("le")))).pro(True),
     subj(Pro("je").pe(1))).realize()   
    ) == "J'y ai mis la lettre. ",\
    "Phrase complète:  J'y ai mis la lettre. "


def test_exemples_fr_117():
    assert (
root(V("mettre").t('pc'),
     comp(N("lettre"),
          det(D("le"))).pro(True),
     comp(P("sur"),
          mod(N("table"),
              det(D("le")))).pro(True),
     subj(Pro("je").pe(1))).typ({'neg': True}).realize()   
    ) == "Je ne l'y ai pas mise. ",\
    "Phrase complète:  Je ne l'y ai pas mise. "


def test_exemples_fr_118():
    assert (
root(V("donner").t('pc'),
     comp(N("pomme"),
          det(D("un"))).pro(True),
     subj(Pro("lui").c('nom'))).realize()   
    ) == "Il l'a donnée. ",\
    "Phrase complète:  Il l'a donnée. "


def test_exemples_fr_119():
    assert (
root(V("donner").t('pc'),
     comp(N("pomme"),
          det(D("un"))).pro(True),
     subj(Pro("lui").c('nom'))).typ({'neg': True}).realize()   
    ) == "Il ne l'a pas donnée. ",\
    "Phrase complète:  Il ne l'a pas donnée. "


def test_exemples_fr_120():
    assert (
root(V("donner").t('pc'),
     comp(N("pomme"),
          det(D("un"))).pro(True),
     comp(P("à"),
          mod(N("fille"),
              det(D("le")))),
     subj(Pro("lui").c('nom'))).typ({'neg': True}).realize()   
    ) == "Il ne l'a pas donnée à la fille. ",\
    "Phrase complète:  Il ne l'a pas donnée à la fille. "


def test_exemples_fr_121():
    assert (
root(V("donner").t('pc'),
     comp(N("pomme"),
          det(D("un"))).pro(True),
     comp(P("à"),
          mod(N("fille"),
              det(D("le")))).pro(True),
     subj(Pro("lui").c('nom'))).typ({'neg': True}).realize()   
    ) == 'Il ne la lui a pas donnée. ',\
    'Phrase complète:  Il ne la lui a pas donnée. '


def test_exemples_fr_122():
    assert (
root(V("donner").t('pc'),
     comp(N("pomme"),
          det(D("un"))).pro(True),
     comp(P("à"),
          mod(N("fille"),
              det(D("le")))).pro(True),
     subj(Pro("lui").c('nom'))).typ({'neg': True, 'pas': True}).realize()   
    ) == 'Elle ne lui a pas été donnée par lui. ',\
    'Phrase complète:  Elle ne lui a pas été donnée par lui. '


def test_exemples_fr_123():
    assert (
root(V("donner").t('pc'),
     comp(N("chat"),
          det(D("un"))).pro(True),
     comp(Pro("elle").c('dat')),
     subj(Pro("lui").c('nom'))).realize()   
    ) == 'Il le lui a donné. ',\
    'Phrase complète:  Il le lui a donné. '


def test_exemples_fr_124():
    assert (
root(V("manger"),
     comp(N("souris"),
          det(D("le"))),
     subj(N("chat").g('f'),
          det(D("le")))).t('f').realize()   
    ) == 'La chatte mangera la souris. ',\
    'Phrase complète:  La chatte mangera la souris. '


def test_exemples_fr_125():
    assert (
root(V("aller"),
     comp(P("à"),
          mod(N("plage"),
              det(D("le")))),
     coord(C("et"),
           subj(Pro("elle").tn('')),
           subj(Pro("moi").tn('')))).t('pc').realize()   
    ) == 'Elle et moi sommes allés à la plage. ',\
    'Phrase complète:  Elle et moi sommes allés à la plage. '


def test_exemples_fr_126():
    assert (
root(V("aller"),
     subj(N("chef"),
          det(D("notre").pe(2)))).realize()   
    ) == 'Votre chef va. ',\
    'Phrase complète:  Votre chef va. '


def test_exemples_fr_127():
    assert (
root(V("manger"),
     comp(N("souris"),
          det(D("le"))),
     subj(N("chat"),
          det(D("le")))).typ({'int': 'yon'}).realize()   
    ) == 'Le chat mange-t-il la souris? ',\
    'Phrase complète:  Le chat mange-t-il la souris? '


def test_exemples_fr_128():
    assert (
root(V("manger"),
     comp(N("souris"),
          det(D("le"))),
     subj(N("chat"),
          det(D("le")))).typ({'int': 'yon', 'neg': True}).realize()   
    ) == 'Le chat ne mange-t-il pas la souris? ',\
    'Phrase complète:  Le chat ne mange-t-il pas la souris? '


def test_exemples_fr_129():
    assert (
root(V("manger"),
     comp(N("souris"),
          det(D("le"))),
     subj(N("chat"),
          det(D("le")))).typ({'int': 'yon', 'pas': True}).realize()   
    ) == 'La souris est-elle mangée par le chat? ',\
    'Phrase complète:  La souris est-elle mangée par le chat? '


def test_exemples_fr_130():
    assert (
root(V("manger"),
     comp(N("fromage"),
          det(D("le"))),
     subj(Pro("je"))).typ({'int': 'yon'}).realize()   
    ) == 'Mange-t-il le fromage? ',\
    'Phrase complète:  Mange-t-il le fromage? '


def test_exemples_fr_131():
    assert (
root(V("manger").t('pc'),
     comp(N("fromage"),
          det(D("le"))),
     subj(Pro("je"))).typ({'int': 'yon'}).realize()   
    ) == 'A-t-il mangé le fromage? ',\
    'Phrase complète:  A-t-il mangé le fromage? '


def test_exemples_fr_132():
    assert (
root(V("manger").t('pc'),
     comp(N("fromage"),
          det(D("le"))),
     subj(Pro("je"))).typ({'neg': True, 'int': 'yon'}).realize()   
    ) == "N'a-t-il pas mangé le fromage? ",\
    "Phrase complète:  N'a-t-il pas mangé le fromage? "


def test_exemples_fr_133():
    assert (
root(V("manger").t('pc'),
     comp(N("fromage"),
          det(D("le"))),
     subj(Pro("je"))).typ({'neg': True, 'int': 'tag'}).realize()   
    ) == "Il n'a pas mangé le fromage, n'est-ce pas? ",\
    "Phrase complète:  Il n'a pas mangé le fromage, n'est-ce pas? "


def test_exemples_fr_134():
    assert (
root(V("travailler").t('pc'),
     comp(Adv("bien")),
     subj(Pro("je").pe(2))).typ({'mod': 'nece'}).realize()   
    ) == 'Tu as dû bien travailler. ',\
    'Phrase complète:  Tu as dû bien travailler. '


def test_exemples_fr_135():
    assert (
root(V("aller").t('pc'),
     comp(Adv("hier")),
     comp(P("à"),
          mod(N("maison"),
              det(D("le")))),
     subj(Pro("je"))).typ({'neg': True}).realize()   
    ) == "Il n'est pas allé hier à la maison. ",\
    "Phrase complète:  Il n'est pas allé hier à la maison. "


def test_exemples_fr_136():
    assert (
root(V("aller").t('pc'),
     comp(Adv("souvent")),
     comp(P("à"),
          mod(N("maison"),
              det(D("le")))),
     comp(Adv("sûrement")),
     subj(Pro("je"))).typ({'neg': True}).realize()   
    ) == "Il n'est pas souvent allé à la maison sûrement. ",\
    "Phrase complète:  Il n'est pas souvent allé à la maison sûrement. "


def test_exemples_fr_137():
    assert (
root(V("aller").t('pc'),
     comp(Adv("souvent").pos('post')),
     comp(P("à"),
          mod(N("maison"),
              det(D("le")))),
     subj(Pro("je"))).typ({'neg': True}).realize()   
    ) == "Il n'est pas allé souvent à la maison. ",\
    "Phrase complète:  Il n'est pas allé souvent à la maison. "


def test_exemples_fr_138():
    assert (
root(V("manger"),
     comp(Adv("bien")),
     comp(Adv("souvent")),
     comp(N("souris"),
          det(D("le"))),
     subj(N("chat"),
          det(D("le")))).typ({'pas': True}).realize()   
    ) == 'La souris est bien souvent mangée par le chat. ',\
    'Phrase complète:  La souris est bien souvent mangée par le chat. '


def test_exemples_fr_139():
    assert (
root(V("sembler").t('pa'),
     comp(V("fonctionner").t('bp')),
     subj(Pro("tout"))).realize()   
    ) == 'Tout eut semblé avoir fonctionné. ',\
    'Phrase complète:  Tout eut semblé avoir fonctionné. '


def test_exemples_fr_140():
    assert (
root(V("manger"),
     comp(N("fromage"),
          det(D("le"))),
     subj(Pro("lui"))).typ({'pas': True}).realize()   
    ) == 'Le fromage est mangé par lui. ',\
    'Phrase complète:  Le fromage est mangé par lui. '


def test_exemples_fr_141():
    assert (
root(N("fille"),
     det(NO(2)),
     coord(C("et"),
           mod(A("joli")),
           mod(A("vieux")))).cap(False).realize()
    ) == '2 filles jolies et vieilles',\
    'Phrase complète:  2 filles jolies et vieilles'


def test_exemples_fr_142():
    assert (
root(N("fille"),
     coord(C("ou"),
           det(NO("2")),
           det(NO("3"))),
     coord(C("et"),
           mod(A("jeune")),
           mod(A("joli")))).cap(False).realize()   
    ) == '2 ou 3 filles jeunes et jolies',\
    'Phrase complète:  2 ou 3 filles jeunes et jolies'

