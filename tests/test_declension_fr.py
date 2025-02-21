import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..','src')))

from pyrealb import *
load("fr")

def test_declension_fr_0():
    assert (
N("abbé").g('m').n('p').realize()   
    ) == 'abbés',\
    'N("abbé").g(\'m\').n(\'p\')=>abbés'


def test_declension_fr_1():
    assert (
N("abeille").g('f').n('p').realize()   
    ) == 'abeilles',\
    'N("abeille").g(\'f\').n(\'p\')=>abeilles'


def test_declension_fr_2():
    assert (
N("abîme").g('m').n('p').realize()   
    ) == 'abîmes',\
    'N("abîme").g(\'m\').n(\'p\')=>abîmes'


def test_declension_fr_3():
    assert (
N("abondance").g('f').n('p').realize()   
    ) == 'abondances',\
    'N("abondance").g(\'f\').n(\'p\')=>abondances'


def test_declension_fr_4():
    assert (
A("abondant").n('p').realize()   
    ) == 'abondants',\
    'A("abondant").n(\'p\')=>abondants'


def test_declension_fr_5():
    assert (
N("abord").g('m').n('p').realize()   
    ) == 'abords',\
    'N("abord").g(\'m\').n(\'p\')=>abords'


def test_declension_fr_6():
    assert (
N("abri").g('m').n('p').realize()   
    ) == 'abris',\
    'N("abri").g(\'m\').n(\'p\')=>abris'


def test_declension_fr_7():
    assert (
N("absence").g('f').n('p').realize()   
    ) == 'absences',\
    'N("absence").g(\'f\').n(\'p\')=>absences'


def test_declension_fr_8():
    assert (
A("absent").n('p').realize()   
    ) == 'absents',\
    'A("absent").n(\'p\')=>absents'


def test_declension_fr_9():
    assert (
A("absolu").n('p').realize()   
    ) == 'absolus',\
    'A("absolu").n(\'p\')=>absolus'


def test_declension_fr_10():
    assert (
N("accident").g('m').n('p').realize()   
    ) == 'accidents',\
    'N("accident").g(\'m\').n(\'p\')=>accidents'


def test_declension_fr_11():
    assert (
N("acclamation").g('f').n('p').realize()   
    ) == 'acclamations',\
    'N("acclamation").g(\'f\').n(\'p\')=>acclamations'


def test_declension_fr_12():
    assert (
N("accord").g('m').n('p').realize()   
    ) == 'accords',\
    'N("accord").g(\'m\').n(\'p\')=>accords'


def test_declension_fr_13():
    assert (
N("accueil").g('m').n('p').realize()   
    ) == 'accueils',\
    'N("accueil").g(\'m\').n(\'p\')=>accueils'


def test_declension_fr_14():
    assert (
N("achat").g('m').n('p').realize()   
    ) == 'achats',\
    'N("achat").g(\'m\').n(\'p\')=>achats'


def test_declension_fr_15():
    assert (
N("acheteur").g('f').n('p').realize()   
    ) == 'acheteuses',\
    'N("acheteur").g(\'f\').n(\'p\')=>acheteuses'


def test_declension_fr_16():
    assert (
N("acide").g('m').n('p').realize()   
    ) == 'acides',\
    'N("acide").g(\'m\').n(\'p\')=>acides'


def test_declension_fr_17():
    assert (
N("acier").g('m').n('p').realize()   
    ) == 'aciers',\
    'N("acier").g(\'m\').n(\'p\')=>aciers'


def test_declension_fr_18():
    assert (
N("acte").g('m').n('p').realize()   
    ) == 'actes',\
    'N("acte").g(\'m\').n(\'p\')=>actes'


def test_declension_fr_19():
    assert (
A("actif").n('p').realize()   
    ) == 'actifs',\
    'A("actif").n(\'p\')=>actifs'


def test_declension_fr_20():
    assert (
N("action").g('f').n('p').realize()   
    ) == 'actions',\
    'N("action").g(\'f\').n(\'p\')=>actions'


def test_declension_fr_21():
    assert (
N("activité").g('f').n('p').realize()   
    ) == 'activités',\
    'N("activité").g(\'f\').n(\'p\')=>activités'


def test_declension_fr_22():
    assert (
A("actuel").n('p').realize()   
    ) == 'actuels',\
    'A("actuel").n(\'p\')=>actuels'


def test_declension_fr_23():
    assert (
N("adieu").g('m').n('p').realize()   
    ) == 'adieux',\
    'N("adieu").g(\'m\').n(\'p\')=>adieux'


def test_declension_fr_24():
    assert (
N("administration").g('f').n('p').realize()   
    ) == 'administrations',\
    'N("administration").g(\'f\').n(\'p\')=>administrations'


def test_declension_fr_25():
    assert (
A("admirable").n('p').realize()   
    ) == 'admirables',\
    'A("admirable").n(\'p\')=>admirables'


def test_declension_fr_26():
    assert (
N("admiration").g('f').n('p').realize()   
    ) == 'admirations',\
    'N("admiration").g(\'f\').n(\'p\')=>admirations'


def test_declension_fr_27():
    assert (
N("adresse").g('f').n('p').realize()   
    ) == 'adresses',\
    'N("adresse").g(\'f\').n(\'p\')=>adresses'


def test_declension_fr_28():
    assert (
A("adroit").n('p').realize()   
    ) == 'adroits',\
    'A("adroit").n(\'p\')=>adroits'


def test_declension_fr_29():
    assert (
N("adversaire").n('p').realize()   
    ) == 'adversaires',\
    'N("adversaire").n(\'p\')=>adversaires'


def test_declension_fr_30():
    assert (
N("affaire").g('f').n('p').realize()   
    ) == 'affaires',\
    'N("affaire").g(\'f\').n(\'p\')=>affaires'


def test_declension_fr_31():
    assert (
A("affairé").n('p').realize()   
    ) == 'affairés',\
    'A("affairé").n(\'p\')=>affairés'


def test_declension_fr_32():
    assert (
N("affection").g('f').n('p').realize()   
    ) == 'affections',\
    'N("affection").g(\'f\').n(\'p\')=>affections'


def test_declension_fr_33():
    assert (
A("affectueux").n('p').realize()   
    ) == 'affectueux',\
    'A("affectueux").n(\'p\')=>affectueux'


def test_declension_fr_34():
    assert (
N("affiche").g('f').n('p').realize()   
    ) == 'affiches',\
    'N("affiche").g(\'f\').n(\'p\')=>affiches'


def test_declension_fr_35():
    assert (
A("affreux").n('p').realize()   
    ) == 'affreux',\
    'A("affreux").n(\'p\')=>affreux'


def test_declension_fr_36():
    assert (
N("âge").g('m').n('p').realize()   
    ) == 'âges',\
    'N("âge").g(\'m\').n(\'p\')=>âges'


def test_declension_fr_37():
    assert (
A("âgé").n('p').realize()   
    ) == 'âgés',\
    'A("âgé").n(\'p\')=>âgés'


def test_declension_fr_38():
    assert (
N("agent").g('m').n('p').realize()   
    ) == 'agents',\
    'N("agent").g(\'m\').n(\'p\')=>agents'


def test_declension_fr_39():
    assert (
A("agile").n('p').realize()   
    ) == 'agiles',\
    'A("agile").n(\'p\')=>agiles'


def test_declension_fr_40():
    assert (
N("agitation").g('f').n('p').realize()   
    ) == 'agitations',\
    'N("agitation").g(\'f\').n(\'p\')=>agitations'


def test_declension_fr_41():
    assert (
A("agréable").n('p').realize()   
    ) == 'agréables',\
    'A("agréable").n(\'p\')=>agréables'


def test_declension_fr_42():
    assert (
N("agrément").g('m').n('p').realize()   
    ) == 'agréments',\
    'N("agrément").g(\'m\').n(\'p\')=>agréments'


def test_declension_fr_43():
    assert (
N("aide").g('f').n('p').realize()   
    ) == 'aides',\
    'N("aide").g(\'f\').n(\'p\')=>aides'


def test_declension_fr_44():
    assert (
A("aigu").n('p').realize()   
    ) == 'aigus',\
    'A("aigu").n(\'p\')=>aigus'


def test_declension_fr_45():
    assert (
N("aiguille").g('f').n('p').realize()   
    ) == 'aiguilles',\
    'N("aiguille").g(\'f\').n(\'p\')=>aiguilles'


def test_declension_fr_46():
    assert (
N("aile").g('f').n('p').realize()   
    ) == 'ailes',\
    'N("aile").g(\'f\').n(\'p\')=>ailes'


def test_declension_fr_47():
    assert (
A("aimable").n('p').realize()   
    ) == 'aimables',\
    'A("aimable").n(\'p\')=>aimables'


def test_declension_fr_48():
    assert (
A("aîné").n('p').realize()   
    ) == 'aînés',\
    'A("aîné").n(\'p\')=>aînés'


def test_declension_fr_49():
    assert (
N("air").g('m').n('p').realize()   
    ) == 'airs',\
    'N("air").g(\'m\').n(\'p\')=>airs'


def test_declension_fr_50():
    assert (
N("aire").g('f').n('p').realize()   
    ) == 'aires',\
    'N("aire").g(\'f\').n(\'p\')=>aires'


def test_declension_fr_51():
    assert (
N("aisance").g('f').n('p').realize()   
    ) == 'aisances',\
    'N("aisance").g(\'f\').n(\'p\')=>aisances'


def test_declension_fr_52():
    assert (
N("aise").g('f').n('p').realize()   
    ) == 'aises',\
    'N("aise").g(\'f\').n(\'p\')=>aises'


def test_declension_fr_53():
    assert (
A("aisé").n('p').realize()   
    ) == 'aisés',\
    'A("aisé").n(\'p\')=>aisés'


def test_declension_fr_54():
    assert (
N("alcool").g('m').n('p').realize()   
    ) == 'alcools',\
    'N("alcool").g(\'m\').n(\'p\')=>alcools'


def test_declension_fr_55():
    assert (
A("alcoolique").n('p').realize()   
    ) == 'alcooliques',\
    'A("alcoolique").n(\'p\')=>alcooliques'


def test_declension_fr_56():
    assert (
N("alentours").g('m').n('p').realize()   
    ) == 'alentours',\
    'N("alentours").g(\'m\').n(\'p\')=>alentours'


def test_declension_fr_57():
    assert (
N("alerte").g('f').n('p').realize()   
    ) == 'alertes',\
    'N("alerte").g(\'f\').n(\'p\')=>alertes'


def test_declension_fr_58():
    assert (
N("aliment").g('m').n('p').realize()   
    ) == 'aliments',\
    'N("aliment").g(\'m\').n(\'p\')=>aliments'


def test_declension_fr_59():
    assert (
N("allée").g('f').n('p').realize()   
    ) == 'allées',\
    'N("allée").g(\'f\').n(\'p\')=>allées'


def test_declension_fr_60():
    assert (
N("allégresse").g('f').n('p').realize()   
    ) == 'allégresses',\
    'N("allégresse").g(\'f\').n(\'p\')=>allégresses'


def test_declension_fr_61():
    assert (
A("allemand").n('p').realize()   
    ) == 'allemands',\
    'A("allemand").n(\'p\')=>allemands'


def test_declension_fr_62():
    assert (
N("allumette").g('f').n('p').realize()   
    ) == 'allumettes',\
    'N("allumette").g(\'f\').n(\'p\')=>allumettes'


def test_declension_fr_63():
    assert (
N("allure").g('f').n('p').realize()   
    ) == 'allures',\
    'N("allure").g(\'f\').n(\'p\')=>allures'


def test_declension_fr_64():
    assert (
N("alouette").g('f').n('p').realize()   
    ) == 'alouettes',\
    'N("alouette").g(\'f\').n(\'p\')=>alouettes'


def test_declension_fr_65():
    assert (
N("amateur").g('m').n('p').realize()   
    ) == 'amateurs',\
    'N("amateur").g(\'m\').n(\'p\')=>amateurs'


def test_declension_fr_66():
    assert (
N("ambulance").g('f').n('p').realize()   
    ) == 'ambulances',\
    'N("ambulance").g(\'f\').n(\'p\')=>ambulances'


def test_declension_fr_67():
    assert (
N("âme").g('f').n('p').realize()   
    ) == 'âmes',\
    'N("âme").g(\'f\').n(\'p\')=>âmes'


def test_declension_fr_68():
    assert (
N("amende").g('f').n('p').realize()   
    ) == 'amendes',\
    'N("amende").g(\'f\').n(\'p\')=>amendes'


def test_declension_fr_69():
    assert (
A("amer").n('p').realize()   
    ) == 'amers',\
    'A("amer").n(\'p\')=>amers'


def test_declension_fr_70():
    assert (
A("américain").n('p').realize()   
    ) == 'américains',\
    'A("américain").n(\'p\')=>américains'


def test_declension_fr_71():
    assert (
N("ami").g('m').n('p').realize()   
    ) == 'amis',\
    'N("ami").g(\'m\').n(\'p\')=>amis'


def test_declension_fr_72():
    assert (
A("amical").n('p').realize()   
    ) == 'amicaux',\
    'A("amical").n(\'p\')=>amicaux'


def test_declension_fr_73():
    assert (
N("amitié").g('f').n('p').realize()   
    ) == 'amitiés',\
    'N("amitié").g(\'f\').n(\'p\')=>amitiés'


def test_declension_fr_74():
    assert (
A("ample").n('p').realize()   
    ) == 'amples',\
    'A("ample").n(\'p\')=>amples'


def test_declension_fr_75():
    assert (
A("amusant").n('p').realize()   
    ) == 'amusants',\
    'A("amusant").n(\'p\')=>amusants'


def test_declension_fr_76():
    assert (
N("amusement").g('m').n('p').realize()   
    ) == 'amusements',\
    'N("amusement").g(\'m\').n(\'p\')=>amusements'


def test_declension_fr_77():
    assert (
A("ancien").n('p').realize()   
    ) == 'anciens',\
    'A("ancien").n(\'p\')=>anciens'


def test_declension_fr_78():
    assert (
N("âne").g('m').n('p').realize()   
    ) == 'ânes',\
    'N("âne").g(\'m\').n(\'p\')=>ânes'


def test_declension_fr_79():
    assert (
N("ange").g('m').n('p').realize()   
    ) == 'anges',\
    'N("ange").g(\'m\').n(\'p\')=>anges'


def test_declension_fr_80():
    assert (
A("anglais").n('p').realize()   
    ) == 'anglais',\
    'A("anglais").n(\'p\')=>anglais'


def test_declension_fr_81():
    assert (
N("angle").g('m').n('p').realize()   
    ) == 'angles',\
    'N("angle").g(\'m\').n(\'p\')=>angles'


def test_declension_fr_82():
    assert (
N("angoisse").g('f').n('p').realize()   
    ) == 'angoisses',\
    'N("angoisse").g(\'f\').n(\'p\')=>angoisses'


def test_declension_fr_83():
    assert (
N("animal").g('m').n('p').realize()   
    ) == 'animaux',\
    'N("animal").g(\'m\').n(\'p\')=>animaux'


def test_declension_fr_84():
    assert (
N("animation").g('f').n('p').realize()   
    ) == 'animations',\
    'N("animation").g(\'f\').n(\'p\')=>animations'


def test_declension_fr_85():
    assert (
N("anneau").g('m').n('p').realize()   
    ) == 'anneaux',\
    'N("anneau").g(\'m\').n(\'p\')=>anneaux'


def test_declension_fr_86():
    assert (
N("année").g('f').n('p').realize()   
    ) == 'années',\
    'N("année").g(\'f\').n(\'p\')=>années'


def test_declension_fr_87():
    assert (
N("anniversaire").g('m').n('p').realize()   
    ) == 'anniversaires',\
    'N("anniversaire").g(\'m\').n(\'p\')=>anniversaires'


def test_declension_fr_88():
    assert (
N("annonce").g('f').n('p').realize()   
    ) == 'annonces',\
    'N("annonce").g(\'f\').n(\'p\')=>annonces'


def test_declension_fr_89():
    assert (
A("annuel").n('p').realize()   
    ) == 'annuels',\
    'A("annuel").n(\'p\')=>annuels'


def test_declension_fr_90():
    assert (
N("anxiété").g('f').n('p').realize()   
    ) == 'anxiétés',\
    'N("anxiété").g(\'f\').n(\'p\')=>anxiétés'


def test_declension_fr_91():
    assert (
A("anxieux").n('p').realize()   
    ) == 'anxieux',\
    'A("anxieux").n(\'p\')=>anxieux'


def test_declension_fr_92():
    assert (
N("août").g('m').n('p').realize()   
    ) == 'aoûts',\
    'N("août").g(\'m\').n(\'p\')=>aoûts'


def test_declension_fr_93():
    assert (
A("apostolique").n('p').realize()   
    ) == 'apostoliques',\
    'A("apostolique").n(\'p\')=>apostoliques'


def test_declension_fr_94():
    assert (
N("apôtre").g('m').n('p').realize()   
    ) == 'apôtres',\
    'N("apôtre").g(\'m\').n(\'p\')=>apôtres'


def test_declension_fr_95():
    assert (
N("apparence").g('f').n('p').realize()   
    ) == 'apparences',\
    'N("apparence").g(\'f\').n(\'p\')=>apparences'


def test_declension_fr_96():
    assert (
N("apparition").g('f').n('p').realize()   
    ) == 'apparitions',\
    'N("apparition").g(\'f\').n(\'p\')=>apparitions'


def test_declension_fr_97():
    assert (
N("appartement").g('m').n('p').realize()   
    ) == 'appartements',\
    'N("appartement").g(\'m\').n(\'p\')=>appartements'


def test_declension_fr_98():
    assert (
N("appel").g('m').n('p').realize()   
    ) == 'appels',\
    'N("appel").g(\'m\').n(\'p\')=>appels'


def test_declension_fr_99():
    assert (
A("appétissant").n('p').realize()   
    ) == 'appétissants',\
    'A("appétissant").n(\'p\')=>appétissants'


def test_declension_fr_100():
    assert (
N("appétit").g('m').n('p').realize()   
    ) == 'appétits',\
    'N("appétit").g(\'m\').n(\'p\')=>appétits'


def test_declension_fr_101():
    assert (
N("application").g('f').n('p').realize()   
    ) == 'applications',\
    'N("application").g(\'f\').n(\'p\')=>applications'


def test_declension_fr_102():
    assert (
N("approche").g('f').n('p').realize()   
    ) == 'approches',\
    'N("approche").g(\'f\').n(\'p\')=>approches'


def test_declension_fr_103():
    assert (
N("appui").g('m').n('p').realize()   
    ) == 'appuis',\
    'N("appui").g(\'m\').n(\'p\')=>appuis'


def test_declension_fr_104():
    assert (
N("araignée").g('f').n('p').realize()   
    ) == 'araignées',\
    'N("araignée").g(\'f\').n(\'p\')=>araignées'


def test_declension_fr_105():
    assert (
N("arbitre").g('m').n('p').realize()   
    ) == 'arbitres',\
    'N("arbitre").g(\'m\').n(\'p\')=>arbitres'


def test_declension_fr_106():
    assert (
N("arbre").g('m').n('p').realize()   
    ) == 'arbres',\
    'N("arbre").g(\'m\').n(\'p\')=>arbres'


def test_declension_fr_107():
    assert (
N("arbuste").g('m').n('p').realize()   
    ) == 'arbustes',\
    'N("arbuste").g(\'m\').n(\'p\')=>arbustes'


def test_declension_fr_108():
    assert (
N("architecte").g('m').n('p').realize()   
    ) == 'architectes',\
    'N("architecte").g(\'m\').n(\'p\')=>architectes'


def test_declension_fr_109():
    assert (
A("ardent").n('p').realize()   
    ) == 'ardents',\
    'A("ardent").n(\'p\')=>ardents'


def test_declension_fr_110():
    assert (
N("ardeur").g('f').n('p').realize()   
    ) == 'ardeurs',\
    'N("ardeur").g(\'f\').n(\'p\')=>ardeurs'


def test_declension_fr_111():
    assert (
N("ardoise").g('f').n('p').realize()   
    ) == 'ardoises',\
    'N("ardoise").g(\'f\').n(\'p\')=>ardoises'


def test_declension_fr_112():
    assert (
N("argent").g('m').n('p').realize()   
    ) == 'argents',\
    'N("argent").g(\'m\').n(\'p\')=>argents'


def test_declension_fr_113():
    assert (
N("arme").g('f').n('p').realize()   
    ) == 'armes',\
    'N("arme").g(\'f\').n(\'p\')=>armes'


def test_declension_fr_114():
    assert (
N("armée").g('f').n('p').realize()   
    ) == 'armées',\
    'N("armée").g(\'f\').n(\'p\')=>armées'


def test_declension_fr_115():
    assert (
N("armoire").g('f').n('p').realize()   
    ) == 'armoires',\
    'N("armoire").g(\'f\').n(\'p\')=>armoires'


def test_declension_fr_116():
    assert (
N("arrêt").g('m').n('p').realize()   
    ) == 'arrêts',\
    'N("arrêt").g(\'m\').n(\'p\')=>arrêts'


def test_declension_fr_117():
    assert (
N("arrière").g('m').n('p').realize()   
    ) == 'arrières',\
    'N("arrière").g(\'m\').n(\'p\')=>arrières'


def test_declension_fr_118():
    assert (
N("arrivée").g('f').n('p').realize()   
    ) == 'arrivées',\
    'N("arrivée").g(\'f\').n(\'p\')=>arrivées'


def test_declension_fr_119():
    assert (
N("arrondissement").g('m').n('p').realize()   
    ) == 'arrondissements',\
    'N("arrondissement").g(\'m\').n(\'p\')=>arrondissements'


def test_declension_fr_120():
    assert (
N("art").g('m').n('p').realize()   
    ) == 'arts',\
    'N("art").g(\'m\').n(\'p\')=>arts'


def test_declension_fr_121():
    assert (
N("article").g('m').n('p').realize()   
    ) == 'articles',\
    'N("article").g(\'m\').n(\'p\')=>articles'


def test_declension_fr_122():
    assert (
N("artiste").n('p').realize()   
    ) == 'artistes',\
    'N("artiste").n(\'p\')=>artistes'


def test_declension_fr_123():
    assert (
N("assaut").g('m').n('p').realize()   
    ) == 'assauts',\
    'N("assaut").g(\'m\').n(\'p\')=>assauts'


def test_declension_fr_124():
    assert (
A("assidu").n('p').realize()   
    ) == 'assidus',\
    'A("assidu").n(\'p\')=>assidus'


def test_declension_fr_125():
    assert (
N("assiette").g('f').n('p').realize()   
    ) == 'assiettes',\
    'N("assiette").g(\'f\').n(\'p\')=>assiettes'


def test_declension_fr_126():
    assert (
N("astre").g('m').n('p').realize()   
    ) == 'astres',\
    'N("astre").g(\'m\').n(\'p\')=>astres'


def test_declension_fr_127():
    assert (
N("atelier").g('m').n('p').realize()   
    ) == 'ateliers',\
    'N("atelier").g(\'m\').n(\'p\')=>ateliers'


def test_declension_fr_128():
    assert (
N("atmosphère").g('f').n('p').realize()   
    ) == 'atmosphères',\
    'N("atmosphère").g(\'f\').n(\'p\')=>atmosphères'


def test_declension_fr_129():
    assert (
N("attachement").g('m').n('p').realize()   
    ) == 'attachements',\
    'N("attachement").g(\'m\').n(\'p\')=>attachements'


def test_declension_fr_130():
    assert (
N("attaque").g('f').n('p').realize()   
    ) == 'attaques',\
    'N("attaque").g(\'f\').n(\'p\')=>attaques'


def test_declension_fr_131():
    assert (
N("attente").g('f').n('p').realize()   
    ) == 'attentes',\
    'N("attente").g(\'f\').n(\'p\')=>attentes'


def test_declension_fr_132():
    assert (
A("attentif").n('p').realize()   
    ) == 'attentifs',\
    'A("attentif").n(\'p\')=>attentifs'


def test_declension_fr_133():
    assert (
N("attention").g('f').n('p').realize()   
    ) == 'attentions',\
    'N("attention").g(\'f\').n(\'p\')=>attentions'


def test_declension_fr_134():
    assert (
N("attrait").g('m').n('p').realize()   
    ) == 'attraits',\
    'N("attrait").g(\'m\').n(\'p\')=>attraits'


def test_declension_fr_135():
    assert (
N("aube").g('f').n('p').realize()   
    ) == 'aubes',\
    'N("aube").g(\'f\').n(\'p\')=>aubes'


def test_declension_fr_136():
    assert (
N("aubépine").g('f').n('p').realize()   
    ) == 'aubépines',\
    'N("aubépine").g(\'f\').n(\'p\')=>aubépines'


def test_declension_fr_137():
    assert (
N("auberge").g('f').n('p').realize()   
    ) == 'auberges',\
    'N("auberge").g(\'f\').n(\'p\')=>auberges'


def test_declension_fr_138():
    assert (
N("aumône").g('f').n('p').realize()   
    ) == 'aumônes',\
    'N("aumône").g(\'f\').n(\'p\')=>aumônes'


def test_declension_fr_139():
    assert (
N("aurore").g('f').n('p').realize()   
    ) == 'aurores',\
    'N("aurore").g(\'f\').n(\'p\')=>aurores'


def test_declension_fr_140():
    assert (
N("autel").g('m').n('p').realize()   
    ) == 'autels',\
    'N("autel").g(\'m\').n(\'p\')=>autels'


def test_declension_fr_141():
    assert (
N("auteur").g('m').n('p').realize()   
    ) == 'auteurs',\
    'N("auteur").g(\'m\').n(\'p\')=>auteurs'


def test_declension_fr_142():
    assert (
N("automne").g('m').n('p').realize()   
    ) == 'automnes',\
    'N("automne").g(\'m\').n(\'p\')=>automnes'


def test_declension_fr_143():
    assert (
N("automobile").g('f').n('p').realize()   
    ) == 'automobiles',\
    'N("automobile").g(\'f\').n(\'p\')=>automobiles'


def test_declension_fr_144():
    assert (
N("autorité").g('f').n('p').realize()   
    ) == 'autorités',\
    'N("autorité").g(\'f\').n(\'p\')=>autorités'


def test_declension_fr_145():
    assert (
A("autre").n('p').realize()   
    ) == 'autres',\
    'A("autre").n(\'p\')=>autres'


def test_declension_fr_146():
    assert (
N("avance").g('f').n('p').realize()   
    ) == 'avances',\
    'N("avance").g(\'f\').n(\'p\')=>avances'


def test_declension_fr_147():
    assert (
N("avantage").g('m').n('p').realize()   
    ) == 'avantages',\
    'N("avantage").g(\'m\').n(\'p\')=>avantages'


def test_declension_fr_148():
    assert (
A("avantageux").n('p').realize()   
    ) == 'avantageux',\
    'A("avantageux").n(\'p\')=>avantageux'


def test_declension_fr_149():
    assert (
N("avenir").g('m').n('p').realize()   
    ) == 'avenirs',\
    'N("avenir").g(\'m\').n(\'p\')=>avenirs'


def test_declension_fr_150():
    assert (
N("aventure").g('f').n('p').realize()   
    ) == 'aventures',\
    'N("aventure").g(\'f\').n(\'p\')=>aventures'


def test_declension_fr_151():
    assert (
N("avenue").g('f').n('p').realize()   
    ) == 'avenues',\
    'N("avenue").g(\'f\').n(\'p\')=>avenues'


def test_declension_fr_152():
    assert (
N("averse").g('f').n('p').realize()   
    ) == 'averses',\
    'N("averse").g(\'f\').n(\'p\')=>averses'


def test_declension_fr_153():
    assert (
A("aveugle").n('p').realize()   
    ) == 'aveugles',\
    'A("aveugle").n(\'p\')=>aveugles'


def test_declension_fr_154():
    assert (
N("aviateur").g('m').n('p').realize()   
    ) == 'aviateurs',\
    'N("aviateur").g(\'m\').n(\'p\')=>aviateurs'


def test_declension_fr_155():
    assert (
N("avion").g('m').n('p').realize()   
    ) == 'avions',\
    'N("avion").g(\'m\').n(\'p\')=>avions'


def test_declension_fr_156():
    assert (
N("avis").g('m').n('p').realize()   
    ) == 'avis',\
    'N("avis").g(\'m\').n(\'p\')=>avis'


def test_declension_fr_157():
    assert (
N("avoir").g('m').n('p').realize()   
    ) == 'avoirs',\
    'N("avoir").g(\'m\').n(\'p\')=>avoirs'


def test_declension_fr_158():
    assert (
N("avril").g('m').n('p').realize()   
    ) == 'avrils',\
    'N("avril").g(\'m\').n(\'p\')=>avrils'


def test_declension_fr_159():
    assert (
N("azur").g('m').n('p').realize()   
    ) == 'azurs',\
    'N("azur").g(\'m\').n(\'p\')=>azurs'


def test_declension_fr_160():
    assert (
A("azuré").n('p').realize()   
    ) == 'azurés',\
    'A("azuré").n(\'p\')=>azurés'


def test_declension_fr_161():
    assert (
N("bagage").g('m').n('p').realize()   
    ) == 'bagages',\
    'N("bagage").g(\'m\').n(\'p\')=>bagages'


def test_declension_fr_162():
    assert (
N("baguette").g('f').n('p').realize()   
    ) == 'baguettes',\
    'N("baguette").g(\'f\').n(\'p\')=>baguettes'


def test_declension_fr_163():
    assert (
N("bain").g('m').n('p').realize()   
    ) == 'bains',\
    'N("bain").g(\'m\').n(\'p\')=>bains'


def test_declension_fr_164():
    assert (
N("baiser").g('m').n('p').realize()   
    ) == 'baisers',\
    'N("baiser").g(\'m\').n(\'p\')=>baisers'


def test_declension_fr_165():
    assert (
N("bal").g('m').n('p').realize()   
    ) == 'bals',\
    'N("bal").g(\'m\').n(\'p\')=>bals'


def test_declension_fr_166():
    assert (
N("balançoire").g('f').n('p').realize()   
    ) == 'balançoires',\
    'N("balançoire").g(\'f\').n(\'p\')=>balançoires'


def test_declension_fr_167():
    assert (
N("balcon").g('m').n('p').realize()   
    ) == 'balcons',\
    'N("balcon").g(\'m\').n(\'p\')=>balcons'


def test_declension_fr_168():
    assert (
N("balle").g('f').n('p').realize()   
    ) == 'balles',\
    'N("balle").g(\'f\').n(\'p\')=>balles'


def test_declension_fr_169():
    assert (
N("ballon").g('m').n('p').realize()   
    ) == 'ballons',\
    'N("ballon").g(\'m\').n(\'p\')=>ballons'


def test_declension_fr_170():
    assert (
N("bambin").g('m').n('p').realize()   
    ) == 'bambins',\
    'N("bambin").g(\'m\').n(\'p\')=>bambins'


def test_declension_fr_171():
    assert (
N("banane").g('f').n('p').realize()   
    ) == 'bananes',\
    'N("banane").g(\'f\').n(\'p\')=>bananes'


def test_declension_fr_172():
    assert (
N("banc").g('m').n('p').realize()   
    ) == 'bancs',\
    'N("banc").g(\'m\').n(\'p\')=>bancs'


def test_declension_fr_173():
    assert (
N("bande").g('f').n('p').realize()   
    ) == 'bandes',\
    'N("bande").g(\'f\').n(\'p\')=>bandes'


def test_declension_fr_174():
    assert (
N("bandit").g('m').n('p').realize()   
    ) == 'bandits',\
    'N("bandit").g(\'m\').n(\'p\')=>bandits'


def test_declension_fr_175():
    assert (
N("banque").g('f').n('p').realize()   
    ) == 'banques',\
    'N("banque").g(\'f\').n(\'p\')=>banques'


def test_declension_fr_176():
    assert (
N("banquier").g('m').n('p').realize()   
    ) == 'banquiers',\
    'N("banquier").g(\'m\').n(\'p\')=>banquiers'


def test_declension_fr_177():
    assert (
N("baptême").g('m').n('p').realize()   
    ) == 'baptêmes',\
    'N("baptême").g(\'m\').n(\'p\')=>baptêmes'


def test_declension_fr_178():
    assert (
N("barbe").g('f').n('p').realize()   
    ) == 'barbes',\
    'N("barbe").g(\'f\').n(\'p\')=>barbes'


def test_declension_fr_179():
    assert (
N("barque").g('f').n('p').realize()   
    ) == 'barques',\
    'N("barque").g(\'f\').n(\'p\')=>barques'


def test_declension_fr_180():
    assert (
N("barquette").g('f').n('p').realize()   
    ) == 'barquettes',\
    'N("barquette").g(\'f\').n(\'p\')=>barquettes'


def test_declension_fr_181():
    assert (
N("barrage").g('m').n('p').realize()   
    ) == 'barrages',\
    'N("barrage").g(\'m\').n(\'p\')=>barrages'


def test_declension_fr_182():
    assert (
N("barre").g('f').n('p').realize()   
    ) == 'barres',\
    'N("barre").g(\'f\').n(\'p\')=>barres'


def test_declension_fr_183():
    assert (
N("barreau").g('m').n('p').realize()   
    ) == 'barreaux',\
    'N("barreau").g(\'m\').n(\'p\')=>barreaux'


def test_declension_fr_184():
    assert (
N("barrière").g('f').n('p').realize()   
    ) == 'barrières',\
    'N("barrière").g(\'f\').n(\'p\')=>barrières'


def test_declension_fr_185():
    assert (
A("bas").n('p').realize()   
    ) == 'bas',\
    'A("bas").n(\'p\')=>bas'


def test_declension_fr_186():
    assert (
N("basse").g('f').n('p').realize()   
    ) == 'basses',\
    'N("basse").g(\'f\').n(\'p\')=>basses'


def test_declension_fr_187():
    assert (
N("bassin").g('m').n('p').realize()   
    ) == 'bassins',\
    'N("bassin").g(\'m\').n(\'p\')=>bassins'


def test_declension_fr_188():
    assert (
N("bataille").g('f').n('p').realize()   
    ) == 'batailles',\
    'N("bataille").g(\'f\').n(\'p\')=>batailles'


def test_declension_fr_189():
    assert (
N("bateau").g('m').n('p').realize()   
    ) == 'bateaux',\
    'N("bateau").g(\'m\').n(\'p\')=>bateaux'


def test_declension_fr_190():
    assert (
N("bâtiment").g('m').n('p').realize()   
    ) == 'bâtiments',\
    'N("bâtiment").g(\'m\').n(\'p\')=>bâtiments'


def test_declension_fr_191():
    assert (
N("bâton").g('m').n('p').realize()   
    ) == 'bâtons',\
    'N("bâton").g(\'m\').n(\'p\')=>bâtons'


def test_declension_fr_192():
    assert (
N("bazar").g('m').n('p').realize()   
    ) == 'bazars',\
    'N("bazar").g(\'m\').n(\'p\')=>bazars'


def test_declension_fr_193():
    assert (
A("beau").n('p').realize()   
    ) == 'beaux',\
    'A("beau").n(\'p\')=>beaux'


def test_declension_fr_194():
    assert (
N("beauté").g('f').n('p').realize()   
    ) == 'beautés',\
    'N("beauté").g(\'f\').n(\'p\')=>beautés'


def test_declension_fr_195():
    assert (
N("bébé").g('m').n('p').realize()   
    ) == 'bébés',\
    'N("bébé").g(\'m\').n(\'p\')=>bébés'


def test_declension_fr_196():
    assert (
N("bec").g('m').n('p').realize()   
    ) == 'becs',\
    'N("bec").g(\'m\').n(\'p\')=>becs'


def test_declension_fr_197():
    assert (
N("bêche").g('f').n('p').realize()   
    ) == 'bêches',\
    'N("bêche").g(\'f\').n(\'p\')=>bêches'


def test_declension_fr_198():
    assert (
A("belge").n('p').realize()   
    ) == 'belges',\
    'A("belge").n(\'p\')=>belges'


def test_declension_fr_199():
    assert (
N("bénédiction").g('f').n('p').realize()   
    ) == 'bénédictions',\
    'N("bénédiction").g(\'f\').n(\'p\')=>bénédictions'


def test_declension_fr_200():
    assert (
N("berceau").g('m').n('p').realize()   
    ) == 'berceaux',\
    'N("berceau").g(\'m\').n(\'p\')=>berceaux'


def test_declension_fr_201():
    assert (
N("béret").g('m').n('p').realize()   
    ) == 'bérets',\
    'N("béret").g(\'m\').n(\'p\')=>bérets'


def test_declension_fr_202():
    assert (
N("berger").g('m').n('p').realize()   
    ) == 'bergers',\
    'N("berger").g(\'m\').n(\'p\')=>bergers'


def test_declension_fr_203():
    assert (
N("bergère").g('f').n('p').realize()   
    ) == 'bergères',\
    'N("bergère").g(\'f\').n(\'p\')=>bergères'


def test_declension_fr_204():
    assert (
N("besogne").g('f').n('p').realize()   
    ) == 'besognes',\
    'N("besogne").g(\'f\').n(\'p\')=>besognes'


def test_declension_fr_205():
    assert (
N("besoin").g('m').n('p').realize()   
    ) == 'besoins',\
    'N("besoin").g(\'m\').n(\'p\')=>besoins'


def test_declension_fr_206():
    assert (
N("bétail").g('m').n('p').realize()   
    ) == 'bétails',\
    'N("bétail").g(\'m\').n(\'p\')=>bétails'


def test_declension_fr_207():
    assert (
N("bête").g('f').n('p').realize()   
    ) == 'bêtes',\
    'N("bête").g(\'f\').n(\'p\')=>bêtes'


def test_declension_fr_208():
    assert (
N("betterave").g('f').n('p').realize()   
    ) == 'betteraves',\
    'N("betterave").g(\'f\').n(\'p\')=>betteraves'


def test_declension_fr_209():
    assert (
N("beurre").g('m').n('p').realize()   
    ) == 'beurres',\
    'N("beurre").g(\'m\').n(\'p\')=>beurres'


def test_declension_fr_210():
    assert (
N("bibelot").g('m').n('p').realize()   
    ) == 'bibelots',\
    'N("bibelot").g(\'m\').n(\'p\')=>bibelots'


def test_declension_fr_211():
    assert (
N("bibliothèque").g('f').n('p').realize()   
    ) == 'bibliothèques',\
    'N("bibliothèque").g(\'f\').n(\'p\')=>bibliothèques'


def test_declension_fr_212():
    assert (
N("bicyclette").g('f').n('p').realize()   
    ) == 'bicyclettes',\
    'N("bicyclette").g(\'f\').n(\'p\')=>bicyclettes'


def test_declension_fr_213():
    assert (
A("bienfaisant").n('p').realize()   
    ) == 'bienfaisants',\
    'A("bienfaisant").n(\'p\')=>bienfaisants'


def test_declension_fr_214():
    assert (
N("bienfait").g('m').n('p').realize()   
    ) == 'bienfaits',\
    'N("bienfait").g(\'m\').n(\'p\')=>bienfaits'


def test_declension_fr_215():
    assert (
N("bienfaiteur").g('m').n('p').realize()   
    ) == 'bienfaiteurs',\
    'N("bienfaiteur").g(\'m\').n(\'p\')=>bienfaiteurs'


def test_declension_fr_216():
    assert (
A("bienheureux").n('p').realize()   
    ) == 'bienheureux',\
    'A("bienheureux").n(\'p\')=>bienheureux'


def test_declension_fr_217():
    assert (
N("bienveillance").g('f').n('p').realize()   
    ) == 'bienveillances',\
    'N("bienveillance").g(\'f\').n(\'p\')=>bienveillances'


def test_declension_fr_218():
    assert (
A("bienveillant").n('p').realize()   
    ) == 'bienveillants',\
    'A("bienveillant").n(\'p\')=>bienveillants'


def test_declension_fr_219():
    assert (
N("bière").g('f').n('p').realize()   
    ) == 'bières',\
    'N("bière").g(\'f\').n(\'p\')=>bières'


def test_declension_fr_220():
    assert (
N("bijou").g('m').n('p').realize()   
    ) == 'bijoux',\
    'N("bijou").g(\'m\').n(\'p\')=>bijoux'


def test_declension_fr_221():
    assert (
N("bille").g('f').n('p').realize()   
    ) == 'billes',\
    'N("bille").g(\'f\').n(\'p\')=>billes'


def test_declension_fr_222():
    assert (
N("billet").g('m').n('p').realize()   
    ) == 'billets',\
    'N("billet").g(\'m\').n(\'p\')=>billets'


def test_declension_fr_223():
    assert (
A("bizarre").n('p').realize()   
    ) == 'bizarres',\
    'A("bizarre").n(\'p\')=>bizarres'


def test_declension_fr_224():
    assert (
A("blanc").n('p').realize()   
    ) == 'blancs',\
    'A("blanc").n(\'p\')=>blancs'


def test_declension_fr_225():
    assert (
N("blancheur").g('f').n('p').realize()   
    ) == 'blancheurs',\
    'N("blancheur").g(\'f\').n(\'p\')=>blancheurs'


def test_declension_fr_226():
    assert (
N("blé").g('m').n('p').realize()   
    ) == 'blés',\
    'N("blé").g(\'m\').n(\'p\')=>blés'


def test_declension_fr_227():
    assert (
N("blessure").g('f').n('p').realize()   
    ) == 'blessures',\
    'N("blessure").g(\'f\').n(\'p\')=>blessures'


def test_declension_fr_228():
    assert (
A("bleu").n('p').realize()   
    ) == 'bleus',\
    'A("bleu").n(\'p\')=>bleus'


def test_declension_fr_229():
    assert (
N("bleuet").g('m').n('p').realize()   
    ) == 'bleuets',\
    'N("bleuet").g(\'m\').n(\'p\')=>bleuets'


def test_declension_fr_230():
    assert (
N("bloc").g('m').n('p').realize()   
    ) == 'blocs',\
    'N("bloc").g(\'m\').n(\'p\')=>blocs'


def test_declension_fr_231():
    assert (
A("blond").n('p').realize()   
    ) == 'blonds',\
    'A("blond").n(\'p\')=>blonds'


def test_declension_fr_232():
    assert (
N("blouse").g('f').n('p').realize()   
    ) == 'blouses',\
    'N("blouse").g(\'f\').n(\'p\')=>blouses'


def test_declension_fr_233():
    assert (
N("bluet").g('m').n('p').realize()   
    ) == 'bluets',\
    'N("bluet").g(\'m\').n(\'p\')=>bluets'


def test_declension_fr_234():
    assert (
N("bois").g('m').n('p').realize()   
    ) == 'bois',\
    'N("bois").g(\'m\').n(\'p\')=>bois'


def test_declension_fr_235():
    assert (
N("boisson").g('f').n('p').realize()   
    ) == 'boissons',\
    'N("boisson").g(\'f\').n(\'p\')=>boissons'


def test_declension_fr_236():
    assert (
N("boîte").g('f').n('p').realize()   
    ) == 'boîtes',\
    'N("boîte").g(\'f\').n(\'p\')=>boîtes'


def test_declension_fr_237():
    assert (
A("boiteux").n('p').realize()   
    ) == 'boiteux',\
    'A("boiteux").n(\'p\')=>boiteux'


def test_declension_fr_238():
    assert (
A("bon").n('p').realize()   
    ) == 'bons',\
    'A("bon").n(\'p\')=>bons'


def test_declension_fr_239():
    assert (
N("bonbon").g('m').n('p').realize()   
    ) == 'bonbons',\
    'N("bonbon").g(\'m\').n(\'p\')=>bonbons'


def test_declension_fr_240():
    assert (
N("bond").g('m').n('p').realize()   
    ) == 'bonds',\
    'N("bond").g(\'m\').n(\'p\')=>bonds'


def test_declension_fr_241():
    assert (
N("bonheur").g('m').n('p').realize()   
    ) == 'bonheurs',\
    'N("bonheur").g(\'m\').n(\'p\')=>bonheurs'


def test_declension_fr_242():
    assert (
N("bonhomme").g('m').n('p').realize()   
    ) == 'bonshommes',\
    'N("bonhomme").g(\'m\').n(\'p\')=>bonshommes'


def test_declension_fr_243():
    assert (
N("bonjour").g('m').n('p').realize()   
    ) == 'bonjours',\
    'N("bonjour").g(\'m\').n(\'p\')=>bonjours'


def test_declension_fr_244():
    assert (
N("bonne").g('f').n('p').realize()   
    ) == 'bonnes',\
    'N("bonne").g(\'f\').n(\'p\')=>bonnes'


def test_declension_fr_245():
    assert (
N("bonnet").g('m').n('p').realize()   
    ) == 'bonnets',\
    'N("bonnet").g(\'m\').n(\'p\')=>bonnets'


def test_declension_fr_246():
    assert (
N("bonsoir").g('m').n('p').realize()   
    ) == 'bonsoirs',\
    'N("bonsoir").g(\'m\').n(\'p\')=>bonsoirs'


def test_declension_fr_247():
    assert (
N("bonté").g('f').n('p').realize()   
    ) == 'bontés',\
    'N("bonté").g(\'f\').n(\'p\')=>bontés'


def test_declension_fr_248():
    assert (
N("bord").g('m').n('p').realize()   
    ) == 'bords',\
    'N("bord").g(\'m\').n(\'p\')=>bords'


def test_declension_fr_249():
    assert (
N("bordure").g('f').n('p').realize()   
    ) == 'bordures',\
    'N("bordure").g(\'f\').n(\'p\')=>bordures'


def test_declension_fr_250():
    assert (
N("borne").g('f').n('p').realize()   
    ) == 'bornes',\
    'N("borne").g(\'f\').n(\'p\')=>bornes'


def test_declension_fr_251():
    assert (
N("bosquet").g('m').n('p').realize()   
    ) == 'bosquets',\
    'N("bosquet").g(\'m\').n(\'p\')=>bosquets'


def test_declension_fr_252():
    assert (
A("bossu").n('p').realize()   
    ) == 'bossus',\
    'A("bossu").n(\'p\')=>bossus'


def test_declension_fr_253():
    assert (
N("botte").g('f').n('p').realize()   
    ) == 'bottes',\
    'N("botte").g(\'f\').n(\'p\')=>bottes'


def test_declension_fr_254():
    assert (
N("bouche").g('f').n('p').realize()   
    ) == 'bouches',\
    'N("bouche").g(\'f\').n(\'p\')=>bouches'


def test_declension_fr_255():
    assert (
N("boucle").g('f').n('p').realize()   
    ) == 'boucles',\
    'N("boucle").g(\'f\').n(\'p\')=>boucles'


def test_declension_fr_256():
    assert (
N("boue").g('f').n('p').realize()   
    ) == 'boues',\
    'N("boue").g(\'f\').n(\'p\')=>boues'


def test_declension_fr_257():
    assert (
A("boueux").n('p').realize()   
    ) == 'boueux',\
    'A("boueux").n(\'p\')=>boueux'


def test_declension_fr_258():
    assert (
N("bougie").g('f').n('p').realize()   
    ) == 'bougies',\
    'N("bougie").g(\'f\').n(\'p\')=>bougies'


def test_declension_fr_259():
    assert (
N("boulanger").g('m').n('p').realize()   
    ) == 'boulangers',\
    'N("boulanger").g(\'m\').n(\'p\')=>boulangers'


def test_declension_fr_260():
    assert (
N("boulangerie").g('f').n('p').realize()   
    ) == 'boulangeries',\
    'N("boulangerie").g(\'f\').n(\'p\')=>boulangeries'


def test_declension_fr_261():
    assert (
N("boule").g('f').n('p').realize()   
    ) == 'boules',\
    'N("boule").g(\'f\').n(\'p\')=>boules'


def test_declension_fr_262():
    assert (
N("bouleau").g('m').n('p').realize()   
    ) == 'bouleaux',\
    'N("bouleau").g(\'m\').n(\'p\')=>bouleaux'


def test_declension_fr_263():
    assert (
N("boulevard").g('m').n('p').realize()   
    ) == 'boulevards',\
    'N("boulevard").g(\'m\').n(\'p\')=>boulevards'


def test_declension_fr_264():
    assert (
N("bouquet").g('m').n('p').realize()   
    ) == 'bouquets',\
    'N("bouquet").g(\'m\').n(\'p\')=>bouquets'


def test_declension_fr_265():
    assert (
N("bourdonnement").g('m').n('p').realize()   
    ) == 'bourdonnements',\
    'N("bourdonnement").g(\'m\').n(\'p\')=>bourdonnements'


def test_declension_fr_266():
    assert (
N("bourgeois").g('m').n('p').realize()   
    ) == 'bourgeois',\
    'N("bourgeois").g(\'m\').n(\'p\')=>bourgeois'


def test_declension_fr_267():
    assert (
N("bourgeon").g('m').n('p').realize()   
    ) == 'bourgeons',\
    'N("bourgeon").g(\'m\').n(\'p\')=>bourgeons'


def test_declension_fr_268():
    assert (
N("bourgmestre").g('m').n('p').realize()   
    ) == 'bourgmestres',\
    'N("bourgmestre").g(\'m\').n(\'p\')=>bourgmestres'


def test_declension_fr_269():
    assert (
N("bourrasque").g('f').n('p').realize()   
    ) == 'bourrasques',\
    'N("bourrasque").g(\'f\').n(\'p\')=>bourrasques'


def test_declension_fr_270():
    assert (
N("bourse").g('f').n('p').realize()   
    ) == 'bourses',\
    'N("bourse").g(\'f\').n(\'p\')=>bourses'


def test_declension_fr_271():
    assert (
N("bout").g('m').n('p').realize()   
    ) == 'bouts',\
    'N("bout").g(\'m\').n(\'p\')=>bouts'


def test_declension_fr_272():
    assert (
N("bouteille").g('f').n('p').realize()   
    ) == 'bouteilles',\
    'N("bouteille").g(\'f\').n(\'p\')=>bouteilles'


def test_declension_fr_273():
    assert (
N("boutique").g('f').n('p').realize()   
    ) == 'boutiques',\
    'N("boutique").g(\'f\').n(\'p\')=>boutiques'


def test_declension_fr_274():
    assert (
N("bouton").g('m').n('p').realize()   
    ) == 'boutons',\
    'N("bouton").g(\'m\').n(\'p\')=>boutons'


def test_declension_fr_275():
    assert (
N("branche").g('f').n('p').realize()   
    ) == 'branches',\
    'N("branche").g(\'f\').n(\'p\')=>branches'


def test_declension_fr_276():
    assert (
N("bras").g('m').n('p').realize()   
    ) == 'bras',\
    'N("bras").g(\'m\').n(\'p\')=>bras'


def test_declension_fr_277():
    assert (
A("brave").n('p').realize()   
    ) == 'braves',\
    'A("brave").n(\'p\')=>braves'


def test_declension_fr_278():
    assert (
N("bravo").g('m').n('p').realize()   
    ) == 'bravos',\
    'N("bravo").g(\'m\').n(\'p\')=>bravos'


def test_declension_fr_279():
    assert (
N("brebis").g('f').n('p').realize()   
    ) == 'brebis',\
    'N("brebis").g(\'f\').n(\'p\')=>brebis'


def test_declension_fr_280():
    assert (
N("brèche").g('f').n('p').realize()   
    ) == 'brèches',\
    'N("brèche").g(\'f\').n(\'p\')=>brèches'


def test_declension_fr_281():
    assert (
A("bref").n('p').realize()   
    ) == 'brefs',\
    'A("bref").n(\'p\')=>brefs'


def test_declension_fr_282():
    assert (
N("brigand").g('m').n('p').realize()   
    ) == 'brigands',\
    'N("brigand").g(\'m\').n(\'p\')=>brigands'


def test_declension_fr_283():
    assert (
A("brillant").n('p').realize()   
    ) == 'brillants',\
    'A("brillant").n(\'p\')=>brillants'


def test_declension_fr_284():
    assert (
N("brin").g('m').n('p').realize()   
    ) == 'brins',\
    'N("brin").g(\'m\').n(\'p\')=>brins'


def test_declension_fr_285():
    assert (
N("brindille").g('f').n('p').realize()   
    ) == 'brindilles',\
    'N("brindille").g(\'f\').n(\'p\')=>brindilles'


def test_declension_fr_286():
    assert (
N("brique").g('f').n('p').realize()   
    ) == 'briques',\
    'N("brique").g(\'f\').n(\'p\')=>briques'


def test_declension_fr_287():
    assert (
N("brise").g('f').n('p').realize()   
    ) == 'brises',\
    'N("brise").g(\'f\').n(\'p\')=>brises'


def test_declension_fr_288():
    assert (
N("brochure").g('f').n('p').realize()   
    ) == 'brochures',\
    'N("brochure").g(\'f\').n(\'p\')=>brochures'


def test_declension_fr_289():
    assert (
N("brouillard").g('m').n('p').realize()   
    ) == 'brouillards',\
    'N("brouillard").g(\'m\').n(\'p\')=>brouillards'


def test_declension_fr_290():
    assert (
N("bruit").g('m').n('p').realize()   
    ) == 'bruits',\
    'N("bruit").g(\'m\').n(\'p\')=>bruits'


def test_declension_fr_291():
    assert (
A("brûlant").n('p').realize()   
    ) == 'brûlants',\
    'A("brûlant").n(\'p\')=>brûlants'


def test_declension_fr_292():
    assert (
N("brume").g('f').n('p').realize()   
    ) == 'brumes',\
    'N("brume").g(\'f\').n(\'p\')=>brumes'


def test_declension_fr_293():
    assert (
A("brumeux").n('p').realize()   
    ) == 'brumeux',\
    'A("brumeux").n(\'p\')=>brumeux'


def test_declension_fr_294():
    assert (
A("brun").n('p').realize()   
    ) == 'bruns',\
    'A("brun").n(\'p\')=>bruns'


def test_declension_fr_295():
    assert (
A("brusque").n('p').realize()   
    ) == 'brusques',\
    'A("brusque").n(\'p\')=>brusques'


def test_declension_fr_296():
    assert (
A("brut").n('p').realize()   
    ) == 'bruts',\
    'A("brut").n(\'p\')=>bruts'


def test_declension_fr_297():
    assert (
A("brutal").n('p').realize()   
    ) == 'brutaux',\
    'A("brutal").n(\'p\')=>brutaux'


def test_declension_fr_298():
    assert (
A("bruyant").n('p').realize()   
    ) == 'bruyants',\
    'A("bruyant").n(\'p\')=>bruyants'


def test_declension_fr_299():
    assert (
N("bûcheron").g('m').n('p').realize()   
    ) == 'bûcherons',\
    'N("bûcheron").g(\'m\').n(\'p\')=>bûcherons'


def test_declension_fr_300():
    assert (
N("buis").g('m').n('p').realize()   
    ) == 'buis',\
    'N("buis").g(\'m\').n(\'p\')=>buis'


def test_declension_fr_301():
    assert (
N("buisson").g('m').n('p').realize()   
    ) == 'buissons',\
    'N("buisson").g(\'m\').n(\'p\')=>buissons'


def test_declension_fr_302():
    assert (
N("bulletin").g('m').n('p').realize()   
    ) == 'bulletins',\
    'N("bulletin").g(\'m\').n(\'p\')=>bulletins'


def test_declension_fr_303():
    assert (
N("bureau").g('m').n('p').realize()   
    ) == 'bureaux',\
    'N("bureau").g(\'m\').n(\'p\')=>bureaux'


def test_declension_fr_304():
    assert (
N("but").g('m').n('p').realize()   
    ) == 'buts',\
    'N("but").g(\'m\').n(\'p\')=>buts'


def test_declension_fr_305():
    assert (
N("cabane").g('f').n('p').realize()   
    ) == 'cabanes',\
    'N("cabane").g(\'f\').n(\'p\')=>cabanes'


def test_declension_fr_306():
    assert (
N("cabine").g('f').n('p').realize()   
    ) == 'cabines',\
    'N("cabine").g(\'f\').n(\'p\')=>cabines'


def test_declension_fr_307():
    assert (
N("cadavre").g('m').n('p').realize()   
    ) == 'cadavres',\
    'N("cadavre").g(\'m\').n(\'p\')=>cadavres'


def test_declension_fr_308():
    assert (
N("cadeau").g('m').n('p').realize()   
    ) == 'cadeaux',\
    'N("cadeau").g(\'m\').n(\'p\')=>cadeaux'


def test_declension_fr_309():
    assert (
A("cadet").n('p').realize()   
    ) == 'cadets',\
    'A("cadet").n(\'p\')=>cadets'


def test_declension_fr_310():
    assert (
N("cadran").g('m').n('p').realize()   
    ) == 'cadrans',\
    'N("cadran").g(\'m\').n(\'p\')=>cadrans'


def test_declension_fr_311():
    assert (
N("cadre").g('m').n('p').realize()   
    ) == 'cadres',\
    'N("cadre").g(\'m\').n(\'p\')=>cadres'


def test_declension_fr_312():
    assert (
N("café").g('m').n('p').realize()   
    ) == 'cafés',\
    'N("café").g(\'m\').n(\'p\')=>cafés'


def test_declension_fr_313():
    assert (
N("cage").g('f').n('p').realize()   
    ) == 'cages',\
    'N("cage").g(\'f\').n(\'p\')=>cages'


def test_declension_fr_314():
    assert (
N("cahier").g('m').n('p').realize()   
    ) == 'cahiers',\
    'N("cahier").g(\'m\').n(\'p\')=>cahiers'


def test_declension_fr_315():
    assert (
N("caillou").g('m').n('p').realize()   
    ) == 'cailloux',\
    'N("caillou").g(\'m\').n(\'p\')=>cailloux'


def test_declension_fr_316():
    assert (
N("caisse").g('f').n('p').realize()   
    ) == 'caisses',\
    'N("caisse").g(\'f\').n(\'p\')=>caisses'


def test_declension_fr_317():
    assert (
N("calcul").g('m').n('p').realize()   
    ) == 'calculs',\
    'N("calcul").g(\'m\').n(\'p\')=>calculs'


def test_declension_fr_318():
    assert (
N("calendrier").g('m').n('p').realize()   
    ) == 'calendriers',\
    'N("calendrier").g(\'m\').n(\'p\')=>calendriers'


def test_declension_fr_319():
    assert (
N("calice").g('m').n('p').realize()   
    ) == 'calices',\
    'N("calice").g(\'m\').n(\'p\')=>calices'


def test_declension_fr_320():
    assert (
A("calme").n('p').realize()   
    ) == 'calmes',\
    'A("calme").n(\'p\')=>calmes'


def test_declension_fr_321():
    assert (
N("calvaire").g('m').n('p').realize()   
    ) == 'calvaires',\
    'N("calvaire").g(\'m\').n(\'p\')=>calvaires'


def test_declension_fr_322():
    assert (
N("camarade").n('p').realize()   
    ) == 'camarades',\
    'N("camarade").n(\'p\')=>camarades'


def test_declension_fr_323():
    assert (
N("camion").g('m').n('p').realize()   
    ) == 'camions',\
    'N("camion").g(\'m\').n(\'p\')=>camions'


def test_declension_fr_324():
    assert (
N("camp").g('m').n('p').realize()   
    ) == 'camps',\
    'N("camp").g(\'m\').n(\'p\')=>camps'


def test_declension_fr_325():
    assert (
N("campagne").g('f').n('p').realize()   
    ) == 'campagnes',\
    'N("campagne").g(\'f\').n(\'p\')=>campagnes'


def test_declension_fr_326():
    assert (
N("canal").g('m').n('p').realize()   
    ) == 'canaux',\
    'N("canal").g(\'m\').n(\'p\')=>canaux'


def test_declension_fr_327():
    assert (
N("canard").g('m').n('p').realize()   
    ) == 'canards',\
    'N("canard").g(\'m\').n(\'p\')=>canards'


def test_declension_fr_328():
    assert (
N("canif").g('m').n('p').realize()   
    ) == 'canifs',\
    'N("canif").g(\'m\').n(\'p\')=>canifs'


def test_declension_fr_329():
    assert (
N("canne").g('f').n('p').realize()   
    ) == 'cannes',\
    'N("canne").g(\'f\').n(\'p\')=>cannes'


def test_declension_fr_330():
    assert (
N("canon").g('m').n('p').realize()   
    ) == 'canons',\
    'N("canon").g(\'m\').n(\'p\')=>canons'


def test_declension_fr_331():
    assert (
N("canot").g('m').n('p').realize()   
    ) == 'canots',\
    'N("canot").g(\'m\').n(\'p\')=>canots'


def test_declension_fr_332():
    assert (
N("cantique").g('m').n('p').realize()   
    ) == 'cantiques',\
    'N("cantique").g(\'m\').n(\'p\')=>cantiques'


def test_declension_fr_333():
    assert (
A("capable").n('p').realize()   
    ) == 'capables',\
    'A("capable").n(\'p\')=>capables'


def test_declension_fr_334():
    assert (
N("capitaine").g('m').n('p').realize()   
    ) == 'capitaines',\
    'N("capitaine").g(\'m\').n(\'p\')=>capitaines'


def test_declension_fr_335():
    assert (
N("capital").g('m').n('p').realize()   
    ) == 'capitaux',\
    'N("capital").g(\'m\').n(\'p\')=>capitaux'


def test_declension_fr_336():
    assert (
N("capitale").g('f').n('p').realize()   
    ) == 'capitales',\
    'N("capitale").g(\'f\').n(\'p\')=>capitales'


def test_declension_fr_337():
    assert (
N("caprice").g('m').n('p').realize()   
    ) == 'caprices',\
    'N("caprice").g(\'m\').n(\'p\')=>caprices'


def test_declension_fr_338():
    assert (
N("carabine").g('f').n('p').realize()   
    ) == 'carabines',\
    'N("carabine").g(\'f\').n(\'p\')=>carabines'


def test_declension_fr_339():
    assert (
N("caractère").g('m').n('p').realize()   
    ) == 'caractères',\
    'N("caractère").g(\'m\').n(\'p\')=>caractères'


def test_declension_fr_340():
    assert (
N("caresse").g('f').n('p').realize()   
    ) == 'caresses',\
    'N("caresse").g(\'f\').n(\'p\')=>caresses'


def test_declension_fr_341():
    assert (
N("carnet").g('m').n('p').realize()   
    ) == 'carnets',\
    'N("carnet").g(\'m\').n(\'p\')=>carnets'


def test_declension_fr_342():
    assert (
N("carotte").g('f').n('p').realize()   
    ) == 'carottes',\
    'N("carotte").g(\'f\').n(\'p\')=>carottes'


def test_declension_fr_343():
    assert (
A("carré").n('p').realize()   
    ) == 'carrés',\
    'A("carré").n(\'p\')=>carrés'


def test_declension_fr_344():
    assert (
N("carreau").g('m').n('p').realize()   
    ) == 'carreaux',\
    'N("carreau").g(\'m\').n(\'p\')=>carreaux'


def test_declension_fr_345():
    assert (
N("carrefour").g('m').n('p').realize()   
    ) == 'carrefours',\
    'N("carrefour").g(\'m\').n(\'p\')=>carrefours'


def test_declension_fr_346():
    assert (
N("carrière").g('f').n('p').realize()   
    ) == 'carrières',\
    'N("carrière").g(\'f\').n(\'p\')=>carrières'


def test_declension_fr_347():
    assert (
N("carrousel").g('m').n('p').realize()   
    ) == 'carrousels',\
    'N("carrousel").g(\'m\').n(\'p\')=>carrousels'


def test_declension_fr_348():
    assert (
N("cartable").g('m').n('p').realize()   
    ) == 'cartables',\
    'N("cartable").g(\'m\').n(\'p\')=>cartables'


def test_declension_fr_349():
    assert (
N("carte").g('f').n('p').realize()   
    ) == 'cartes',\
    'N("carte").g(\'f\').n(\'p\')=>cartes'


def test_declension_fr_350():
    assert (
N("carton").g('m').n('p').realize()   
    ) == 'cartons',\
    'N("carton").g(\'m\').n(\'p\')=>cartons'


def test_declension_fr_351():
    assert (
N("cas").g('m').n('p').realize()   
    ) == 'cas',\
    'N("cas").g(\'m\').n(\'p\')=>cas'


def test_declension_fr_352():
    assert (
N("casquette").g('f').n('p').realize()   
    ) == 'casquettes',\
    'N("casquette").g(\'f\').n(\'p\')=>casquettes'


def test_declension_fr_353():
    assert (
N("catastrophe").g('f').n('p').realize()   
    ) == 'catastrophes',\
    'N("catastrophe").g(\'f\').n(\'p\')=>catastrophes'


def test_declension_fr_354():
    assert (
N("catéchisme").g('m').n('p').realize()   
    ) == 'catéchismes',\
    'N("catéchisme").g(\'m\').n(\'p\')=>catéchismes'


def test_declension_fr_355():
    assert (
N("cathédrale").g('f').n('p').realize()   
    ) == 'cathédrales',\
    'N("cathédrale").g(\'f\').n(\'p\')=>cathédrales'


def test_declension_fr_356():
    assert (
A("catholique").n('p').realize()   
    ) == 'catholiques',\
    'A("catholique").n(\'p\')=>catholiques'


def test_declension_fr_357():
    assert (
N("cause").g('f').n('p').realize()   
    ) == 'causes',\
    'N("cause").g(\'f\').n(\'p\')=>causes'


def test_declension_fr_358():
    assert (
N("cave").g('f').n('p').realize()   
    ) == 'caves',\
    'N("cave").g(\'f\').n(\'p\')=>caves'


def test_declension_fr_359():
    assert (
N("caverne").g('f').n('p').realize()   
    ) == 'cavernes',\
    'N("caverne").g(\'f\').n(\'p\')=>cavernes'


def test_declension_fr_360():
    assert (
N("ceinture").g('f').n('p').realize()   
    ) == 'ceintures',\
    'N("ceinture").g(\'f\').n(\'p\')=>ceintures'


def test_declension_fr_361():
    assert (
A("célèbre").n('p').realize()   
    ) == 'célèbres',\
    'A("célèbre").n(\'p\')=>célèbres'


def test_declension_fr_362():
    assert (
A("céleste").n('p').realize()   
    ) == 'célestes',\
    'A("céleste").n(\'p\')=>célestes'


def test_declension_fr_363():
    assert (
N("cendre").g('f').n('p').realize()   
    ) == 'cendres',\
    'N("cendre").g(\'f\').n(\'p\')=>cendres'


def test_declension_fr_364():
    assert (
N("centaine").g('f').n('p').realize()   
    ) == 'centaines',\
    'N("centaine").g(\'f\').n(\'p\')=>centaines'


def test_declension_fr_365():
    assert (
N("centime").g('m').n('p').realize()   
    ) == 'centimes',\
    'N("centime").g(\'m\').n(\'p\')=>centimes'


def test_declension_fr_366():
    assert (
N("centimètre").g('m').n('p').realize()   
    ) == 'centimètres',\
    'N("centimètre").g(\'m\').n(\'p\')=>centimètres'


def test_declension_fr_367():
    assert (
A("central").n('p').realize()   
    ) == 'centraux',\
    'A("central").n(\'p\')=>centraux'


def test_declension_fr_368():
    assert (
N("centre").g('m').n('p').realize()   
    ) == 'centres',\
    'N("centre").g(\'m\').n(\'p\')=>centres'


def test_declension_fr_369():
    assert (
N("cercle").g('m').n('p').realize()   
    ) == 'cercles',\
    'N("cercle").g(\'m\').n(\'p\')=>cercles'


def test_declension_fr_370():
    assert (
N("cérémonie").g('f').n('p').realize()   
    ) == 'cérémonies',\
    'N("cérémonie").g(\'f\').n(\'p\')=>cérémonies'


def test_declension_fr_371():
    assert (
N("cerf").g('m').n('p').realize()   
    ) == 'cerfs',\
    'N("cerf").g(\'m\').n(\'p\')=>cerfs'


def test_declension_fr_372():
    assert (
N("cerise").g('f').n('p').realize()   
    ) == 'cerises',\
    'N("cerise").g(\'f\').n(\'p\')=>cerises'


def test_declension_fr_373():
    assert (
N("cerisier").g('m').n('p').realize()   
    ) == 'cerisiers',\
    'N("cerisier").g(\'m\').n(\'p\')=>cerisiers'


def test_declension_fr_374():
    assert (
A("certain").n('p').realize()   
    ) == 'certains',\
    'A("certain").n(\'p\')=>certains'


def test_declension_fr_375():
    assert (
N("cesse").g('f').n('p').realize()   
    ) == 'cesses',\
    'N("cesse").g(\'f\').n(\'p\')=>cesses'


def test_declension_fr_376():
    assert (
N("chagrin").g('m').n('p').realize()   
    ) == 'chagrins',\
    'N("chagrin").g(\'m\').n(\'p\')=>chagrins'


def test_declension_fr_377():
    assert (
N("chaîne").g('f').n('p').realize()   
    ) == 'chaînes',\
    'N("chaîne").g(\'f\').n(\'p\')=>chaînes'


def test_declension_fr_378():
    assert (
N("chair").g('f').n('p').realize()   
    ) == 'chairs',\
    'N("chair").g(\'f\').n(\'p\')=>chairs'


def test_declension_fr_379():
    assert (
N("chaise").g('f').n('p').realize()   
    ) == 'chaises',\
    'N("chaise").g(\'f\').n(\'p\')=>chaises'


def test_declension_fr_380():
    assert (
N("chaland").g('m').n('p').realize()   
    ) == 'chalands',\
    'N("chaland").g(\'m\').n(\'p\')=>chalands'


def test_declension_fr_381():
    assert (
N("chaleur").g('f').n('p').realize()   
    ) == 'chaleurs',\
    'N("chaleur").g(\'f\').n(\'p\')=>chaleurs'


def test_declension_fr_382():
    assert (
N("chambre").g('f').n('p').realize()   
    ) == 'chambres',\
    'N("chambre").g(\'f\').n(\'p\')=>chambres'


def test_declension_fr_383():
    assert (
N("chameau").g('m').n('p').realize()   
    ) == 'chameaux',\
    'N("chameau").g(\'m\').n(\'p\')=>chameaux'


def test_declension_fr_384():
    assert (
N("champ").g('m').n('p').realize()   
    ) == 'champs',\
    'N("champ").g(\'m\').n(\'p\')=>champs'


def test_declension_fr_385():
    assert (
N("chance").g('f').n('p').realize()   
    ) == 'chances',\
    'N("chance").g(\'f\').n(\'p\')=>chances'


def test_declension_fr_386():
    assert (
N("changement").g('m').n('p').realize()   
    ) == 'changements',\
    'N("changement").g(\'m\').n(\'p\')=>changements'


def test_declension_fr_387():
    assert (
N("chanson").g('f').n('p').realize()   
    ) == 'chansons',\
    'N("chanson").g(\'f\').n(\'p\')=>chansons'


def test_declension_fr_388():
    assert (
N("chant").g('m').n('p').realize()   
    ) == 'chants',\
    'N("chant").g(\'m\').n(\'p\')=>chants'


def test_declension_fr_389():
    assert (
N("chanteur").g('m').n('p').realize()   
    ) == 'chanteurs',\
    'N("chanteur").g(\'m\').n(\'p\')=>chanteurs'


def test_declension_fr_390():
    assert (
N("chantre").g('m').n('p').realize()   
    ) == 'chantres',\
    'N("chantre").g(\'m\').n(\'p\')=>chantres'


def test_declension_fr_391():
    assert (
N("chapeau").g('m').n('p').realize()   
    ) == 'chapeaux',\
    'N("chapeau").g(\'m\').n(\'p\')=>chapeaux'


def test_declension_fr_392():
    assert (
N("chapelet").g('m').n('p').realize()   
    ) == 'chapelets',\
    'N("chapelet").g(\'m\').n(\'p\')=>chapelets'


def test_declension_fr_393():
    assert (
N("chapelle").g('f').n('p').realize()   
    ) == 'chapelles',\
    'N("chapelle").g(\'f\').n(\'p\')=>chapelles'


def test_declension_fr_394():
    assert (
N("chapitre").g('m').n('p').realize()   
    ) == 'chapitres',\
    'N("chapitre").g(\'m\').n(\'p\')=>chapitres'


def test_declension_fr_395():
    assert (
N("charbon").g('m').n('p').realize()   
    ) == 'charbons',\
    'N("charbon").g(\'m\').n(\'p\')=>charbons'


def test_declension_fr_396():
    assert (
N("charbonnage").g('m').n('p').realize()   
    ) == 'charbonnages',\
    'N("charbonnage").g(\'m\').n(\'p\')=>charbonnages'


def test_declension_fr_397():
    assert (
N("charge").g('f').n('p').realize()   
    ) == 'charges',\
    'N("charge").g(\'f\').n(\'p\')=>charges'


def test_declension_fr_398():
    assert (
N("chariot").g('m').n('p').realize()   
    ) == 'chariots',\
    'N("chariot").g(\'m\').n(\'p\')=>chariots'


def test_declension_fr_399():
    assert (
A("charitable").n('p').realize()   
    ) == 'charitables',\
    'A("charitable").n(\'p\')=>charitables'


def test_declension_fr_400():
    assert (
N("charité").g('f').n('p').realize()   
    ) == 'charités',\
    'N("charité").g(\'f\').n(\'p\')=>charités'


def test_declension_fr_401():
    assert (
N("charlatan").g('m').n('p').realize()   
    ) == 'charlatans',\
    'N("charlatan").g(\'m\').n(\'p\')=>charlatans'


def test_declension_fr_402():
    assert (
A("charmant").n('p').realize()   
    ) == 'charmants',\
    'A("charmant").n(\'p\')=>charmants'


def test_declension_fr_403():
    assert (
N("charme").g('m').n('p').realize()   
    ) == 'charmes',\
    'N("charme").g(\'m\').n(\'p\')=>charmes'


def test_declension_fr_404():
    assert (
N("charrette").g('f').n('p').realize()   
    ) == 'charrettes',\
    'N("charrette").g(\'f\').n(\'p\')=>charrettes'


def test_declension_fr_405():
    assert (
N("charrue").g('f').n('p').realize()   
    ) == 'charrues',\
    'N("charrue").g(\'f\').n(\'p\')=>charrues'


def test_declension_fr_406():
    assert (
N("chasse").g('f').n('p').realize()   
    ) == 'chasses',\
    'N("chasse").g(\'f\').n(\'p\')=>chasses'


def test_declension_fr_407():
    assert (
N("chasseur").g('m').n('p').realize()   
    ) == 'chasseurs',\
    'N("chasseur").g(\'m\').n(\'p\')=>chasseurs'


def test_declension_fr_408():
    assert (
N("chat").g('m').n('p').realize()   
    ) == 'chats',\
    'N("chat").g(\'m\').n(\'p\')=>chats'


def test_declension_fr_409():
    assert (
N("château").g('m').n('p').realize()   
    ) == 'châteaux',\
    'N("château").g(\'m\').n(\'p\')=>châteaux'


def test_declension_fr_410():
    assert (
A("chaud").n('p').realize()   
    ) == 'chauds',\
    'A("chaud").n(\'p\')=>chauds'


def test_declension_fr_411():
    assert (
N("chauffage").g('m').n('p').realize()   
    ) == 'chauffages',\
    'N("chauffage").g(\'m\').n(\'p\')=>chauffages'


def test_declension_fr_412():
    assert (
N("chauffeur").g('m').n('p').realize()   
    ) == 'chauffeurs',\
    'N("chauffeur").g(\'m\').n(\'p\')=>chauffeurs'


def test_declension_fr_413():
    assert (
N("chauffeuse").g('f').n('p').realize()   
    ) == 'chauffeuses',\
    'N("chauffeuse").g(\'f\').n(\'p\')=>chauffeuses'


def test_declension_fr_414():
    assert (
N("chaume").g('m').n('p').realize()   
    ) == 'chaumes',\
    'N("chaume").g(\'m\').n(\'p\')=>chaumes'


def test_declension_fr_415():
    assert (
N("chaumière").g('f').n('p').realize()   
    ) == 'chaumières',\
    'N("chaumière").g(\'f\').n(\'p\')=>chaumières'


def test_declension_fr_416():
    assert (
N("chaussée").g('f').n('p').realize()   
    ) == 'chaussées',\
    'N("chaussée").g(\'f\').n(\'p\')=>chaussées'


def test_declension_fr_417():
    assert (
N("chaussure").g('f').n('p').realize()   
    ) == 'chaussures',\
    'N("chaussure").g(\'f\').n(\'p\')=>chaussures'


def test_declension_fr_418():
    assert (
N("chaux").g('f').n('p').realize()   
    ) == 'chaux',\
    'N("chaux").g(\'f\').n(\'p\')=>chaux'


def test_declension_fr_419():
    assert (
N("chef").g('m').n('p').realize()   
    ) == 'chefs',\
    'N("chef").g(\'m\').n(\'p\')=>chefs'


def test_declension_fr_420():
    assert (
N("chemin").g('m').n('p').realize()   
    ) == 'chemins',\
    'N("chemin").g(\'m\').n(\'p\')=>chemins'


def test_declension_fr_421():
    assert (
N("cheminée").g('f').n('p').realize()   
    ) == 'cheminées',\
    'N("cheminée").g(\'f\').n(\'p\')=>cheminées'


def test_declension_fr_422():
    assert (
N("chemise").g('f').n('p').realize()   
    ) == 'chemises',\
    'N("chemise").g(\'f\').n(\'p\')=>chemises'


def test_declension_fr_423():
    assert (
N("chêne").g('m').n('p').realize()   
    ) == 'chênes',\
    'N("chêne").g(\'m\').n(\'p\')=>chênes'


def test_declension_fr_424():
    assert (
A("cher").n('p').realize()   
    ) == 'chers',\
    'A("cher").n(\'p\')=>chers'


def test_declension_fr_425():
    assert (
A("chéri").n('p').realize()   
    ) == 'chéris',\
    'A("chéri").n(\'p\')=>chéris'


def test_declension_fr_426():
    assert (
N("cheval").g('m').n('p').realize()   
    ) == 'chevaux',\
    'N("cheval").g(\'m\').n(\'p\')=>chevaux'


def test_declension_fr_427():
    assert (
N("chevalier").g('m').n('p').realize()   
    ) == 'chevaliers',\
    'N("chevalier").g(\'m\').n(\'p\')=>chevaliers'


def test_declension_fr_428():
    assert (
N("chevalière").g('f').n('p').realize()   
    ) == 'chevalières',\
    'N("chevalière").g(\'f\').n(\'p\')=>chevalières'


def test_declension_fr_429():
    assert (
N("chevelure").g('f').n('p').realize()   
    ) == 'chevelures',\
    'N("chevelure").g(\'f\').n(\'p\')=>chevelures'


def test_declension_fr_430():
    assert (
N("chevet").g('m').n('p').realize()   
    ) == 'chevets',\
    'N("chevet").g(\'m\').n(\'p\')=>chevets'


def test_declension_fr_431():
    assert (
N("cheveu").g('m').n('p').realize()   
    ) == 'cheveux',\
    'N("cheveu").g(\'m\').n(\'p\')=>cheveux'


def test_declension_fr_432():
    assert (
N("chèvre").g('f').n('p').realize()   
    ) == 'chèvres',\
    'N("chèvre").g(\'f\').n(\'p\')=>chèvres'


def test_declension_fr_433():
    assert (
N("chien").g('m').n('p').realize()   
    ) == 'chiens',\
    'N("chien").g(\'m\').n(\'p\')=>chiens'


def test_declension_fr_434():
    assert (
N("chiffon").g('m').n('p').realize()   
    ) == 'chiffons',\
    'N("chiffon").g(\'m\').n(\'p\')=>chiffons'


def test_declension_fr_435():
    assert (
N("chiffre").g('m').n('p').realize()   
    ) == 'chiffres',\
    'N("chiffre").g(\'m\').n(\'p\')=>chiffres'


def test_declension_fr_436():
    assert (
N("choc").g('m').n('p').realize()   
    ) == 'chocs',\
    'N("choc").g(\'m\').n(\'p\')=>chocs'


def test_declension_fr_437():
    assert (
N("chocolat").g('m').n('p').realize()   
    ) == 'chocolats',\
    'N("chocolat").g(\'m\').n(\'p\')=>chocolats'


def test_declension_fr_438():
    assert (
N("choix").g('m').n('p').realize()   
    ) == 'choix',\
    'N("choix").g(\'m\').n(\'p\')=>choix'


def test_declension_fr_439():
    assert (
N("chose").g('f').n('p').realize()   
    ) == 'choses',\
    'N("chose").g(\'f\').n(\'p\')=>choses'


def test_declension_fr_440():
    assert (
N("chou").g('m').n('p').realize()   
    ) == 'choux',\
    'N("chou").g(\'m\').n(\'p\')=>choux'


def test_declension_fr_441():
    assert (
A("chrétien").n('p').realize()   
    ) == 'chrétiens',\
    'A("chrétien").n(\'p\')=>chrétiens'


def test_declension_fr_442():
    assert (
N("chrysanthème").g('m').n('p').realize()   
    ) == 'chrysanthèmes',\
    'N("chrysanthème").g(\'m\').n(\'p\')=>chrysanthèmes'


def test_declension_fr_443():
    assert (
N("chute").g('f').n('p').realize()   
    ) == 'chutes',\
    'N("chute").g(\'f\').n(\'p\')=>chutes'


def test_declension_fr_444():
    assert (
N("ciel").g('m').n('p').realize()   
    ) == 'cieux',\
    'N("ciel").g(\'m\').n(\'p\')=>cieux'


def test_declension_fr_445():
    assert (
N("cigarette").g('f').n('p').realize()   
    ) == 'cigarettes',\
    'N("cigarette").g(\'f\').n(\'p\')=>cigarettes'


def test_declension_fr_446():
    assert (
N("cime").g('f').n('p').realize()   
    ) == 'cimes',\
    'N("cime").g(\'f\').n(\'p\')=>cimes'


def test_declension_fr_447():
    assert (
N("cimetière").g('m').n('p').realize()   
    ) == 'cimetières',\
    'N("cimetière").g(\'m\').n(\'p\')=>cimetières'


def test_declension_fr_448():
    assert (
N("cinéma").g('m').n('p').realize()   
    ) == 'cinémas',\
    'N("cinéma").g(\'m\').n(\'p\')=>cinémas'


def test_declension_fr_449():
    assert (
N("circonstance").g('f').n('p').realize()   
    ) == 'circonstances',\
    'N("circonstance").g(\'f\').n(\'p\')=>circonstances'


def test_declension_fr_450():
    assert (
N("circulation").g('f').n('p').realize()   
    ) == 'circulations',\
    'N("circulation").g(\'f\').n(\'p\')=>circulations'


def test_declension_fr_451():
    assert (
N("cirque").g('m').n('p').realize()   
    ) == 'cirques',\
    'N("cirque").g(\'m\').n(\'p\')=>cirques'


def test_declension_fr_452():
    assert (
N("cité").g('f').n('p').realize()   
    ) == 'cités',\
    'N("cité").g(\'f\').n(\'p\')=>cités'


def test_declension_fr_453():
    assert (
N("citoyen").g('m').n('p').realize()   
    ) == 'citoyens',\
    'N("citoyen").g(\'m\').n(\'p\')=>citoyens'


def test_declension_fr_454():
    assert (
A("civil").n('p').realize()   
    ) == 'civils',\
    'A("civil").n(\'p\')=>civils'


def test_declension_fr_455():
    assert (
A("clair").n('p').realize()   
    ) == 'clairs',\
    'A("clair").n(\'p\')=>clairs'


def test_declension_fr_456():
    assert (
N("clairière").g('f').n('p').realize()   
    ) == 'clairières',\
    'N("clairière").g(\'f\').n(\'p\')=>clairières'


def test_declension_fr_457():
    assert (
N("clairon").g('m').n('p').realize()   
    ) == 'clairons',\
    'N("clairon").g(\'m\').n(\'p\')=>clairons'


def test_declension_fr_458():
    assert (
N("clarté").g('f').n('p').realize()   
    ) == 'clartés',\
    'N("clarté").g(\'f\').n(\'p\')=>clartés'


def test_declension_fr_459():
    assert (
N("classe").g('f').n('p').realize()   
    ) == 'classes',\
    'N("classe").g(\'f\').n(\'p\')=>classes'


def test_declension_fr_460():
    assert (
A("classique").n('p').realize()   
    ) == 'classiques',\
    'A("classique").n(\'p\')=>classiques'


def test_declension_fr_461():
    assert (
N("clé").g('f').n('p').realize()   
    ) == 'clés',\
    'N("clé").g(\'f\').n(\'p\')=>clés'


def test_declension_fr_462():
    assert (
N("clef").g('f').n('p').realize()   
    ) == 'clefs',\
    'N("clef").g(\'f\').n(\'p\')=>clefs'


def test_declension_fr_463():
    assert (
A("clément").n('p').realize()   
    ) == 'cléments',\
    'A("clément").n(\'p\')=>cléments'


def test_declension_fr_464():
    assert (
N("client").g('m').n('p').realize()   
    ) == 'clients',\
    'N("client").g(\'m\').n(\'p\')=>clients'


def test_declension_fr_465():
    assert (
N("climat").g('m').n('p').realize()   
    ) == 'climats',\
    'N("climat").g(\'m\').n(\'p\')=>climats'


def test_declension_fr_466():
    assert (
N("cloche").g('f').n('p').realize()   
    ) == 'cloches',\
    'N("cloche").g(\'f\').n(\'p\')=>cloches'


def test_declension_fr_467():
    assert (
N("clocher").g('m').n('p').realize()   
    ) == 'clochers',\
    'N("clocher").g(\'m\').n(\'p\')=>clochers'


def test_declension_fr_468():
    assert (
N("clochette").g('f').n('p').realize()   
    ) == 'clochettes',\
    'N("clochette").g(\'f\').n(\'p\')=>clochettes'


def test_declension_fr_469():
    assert (
A("clos").n('p').realize()   
    ) == 'clos',\
    'A("clos").n(\'p\')=>clos'


def test_declension_fr_470():
    assert (
N("clou").g('m').n('p').realize()   
    ) == 'clous',\
    'N("clou").g(\'m\').n(\'p\')=>clous'


def test_declension_fr_471():
    assert (
N("clown").g('m').n('p').realize()   
    ) == 'clowns',\
    'N("clown").g(\'m\').n(\'p\')=>clowns'


def test_declension_fr_472():
    assert (
N("cochon").g('m').n('p').realize()   
    ) == 'cochons',\
    'N("cochon").g(\'m\').n(\'p\')=>cochons'


def test_declension_fr_473():
    assert (
N("coffre").g('m').n('p').realize()   
    ) == 'coffres',\
    'N("coffre").g(\'m\').n(\'p\')=>coffres'


def test_declension_fr_474():
    assert (
N("coffret").g('m').n('p').realize()   
    ) == 'coffrets',\
    'N("coffret").g(\'m\').n(\'p\')=>coffrets'


def test_declension_fr_475():
    assert (
N("coiffure").g('f').n('p').realize()   
    ) == 'coiffures',\
    'N("coiffure").g(\'f\').n(\'p\')=>coiffures'


def test_declension_fr_476():
    assert (
N("coin").g('m').n('p').realize()   
    ) == 'coins',\
    'N("coin").g(\'m\').n(\'p\')=>coins'


def test_declension_fr_477():
    assert (
N("colère").g('f').n('p').realize()   
    ) == 'colères',\
    'N("colère").g(\'f\').n(\'p\')=>colères'


def test_declension_fr_478():
    assert (
N("colis").g('m').n('p').realize()   
    ) == 'colis',\
    'N("colis").g(\'m\').n(\'p\')=>colis'


def test_declension_fr_479():
    assert (
N("collection").g('f').n('p').realize()   
    ) == 'collections',\
    'N("collection").g(\'f\').n(\'p\')=>collections'


def test_declension_fr_480():
    assert (
N("collège").g('m').n('p').realize()   
    ) == 'collèges',\
    'N("collège").g(\'m\').n(\'p\')=>collèges'


def test_declension_fr_481():
    assert (
N("colline").g('f').n('p').realize()   
    ) == 'collines',\
    'N("colline").g(\'f\').n(\'p\')=>collines'


def test_declension_fr_482():
    assert (
N("colonel").g('m').n('p').realize()   
    ) == 'colonels',\
    'N("colonel").g(\'m\').n(\'p\')=>colonels'


def test_declension_fr_483():
    assert (
A("colonial").n('p').realize()   
    ) == 'coloniaux',\
    'A("colonial").n(\'p\')=>coloniaux'


def test_declension_fr_484():
    assert (
N("colonne").g('f').n('p').realize()   
    ) == 'colonnes',\
    'N("colonne").g(\'f\').n(\'p\')=>colonnes'


def test_declension_fr_485():
    assert (
N("combat").g('m').n('p').realize()   
    ) == 'combats',\
    'N("combat").g(\'m\').n(\'p\')=>combats'


def test_declension_fr_486():
    assert (
N("combattant").g('m').n('p').realize()   
    ) == 'combattants',\
    'N("combattant").g(\'m\').n(\'p\')=>combattants'


def test_declension_fr_487():
    assert (
N("comble").g('m').n('p').realize()   
    ) == 'combles',\
    'N("comble").g(\'m\').n(\'p\')=>combles'


def test_declension_fr_488():
    assert (
N("commandant").g('m').n('p').realize()   
    ) == 'commandants',\
    'N("commandant").g(\'m\').n(\'p\')=>commandants'


def test_declension_fr_489():
    assert (
N("commande").g('f').n('p').realize()   
    ) == 'commandes',\
    'N("commande").g(\'f\').n(\'p\')=>commandes'


def test_declension_fr_490():
    assert (
N("commandement").g('m').n('p').realize()   
    ) == 'commandements',\
    'N("commandement").g(\'m\').n(\'p\')=>commandements'


def test_declension_fr_491():
    assert (
N("commencement").g('m').n('p').realize()   
    ) == 'commencements',\
    'N("commencement").g(\'m\').n(\'p\')=>commencements'


def test_declension_fr_492():
    assert (
N("commerçant").g('m').n('p').realize()   
    ) == 'commerçants',\
    'N("commerçant").g(\'m\').n(\'p\')=>commerçants'


def test_declension_fr_493():
    assert (
N("commerce").g('m').n('p').realize()   
    ) == 'commerces',\
    'N("commerce").g(\'m\').n(\'p\')=>commerces'


def test_declension_fr_494():
    assert (
A("commercial").n('p').realize()   
    ) == 'commerciaux',\
    'A("commercial").n(\'p\')=>commerciaux'


def test_declension_fr_495():
    assert (
N("commission").g('f').n('p').realize()   
    ) == 'commissions',\
    'N("commission").g(\'f\').n(\'p\')=>commissions'


def test_declension_fr_496():
    assert (
N("commode").g('f').n('p').realize()   
    ) == 'commodes',\
    'N("commode").g(\'f\').n(\'p\')=>commodes'


def test_declension_fr_497():
    assert (
A("commun").n('p').realize()   
    ) == 'communs',\
    'A("commun").n(\'p\')=>communs'


def test_declension_fr_498():
    assert (
A("communal").n('p').realize()   
    ) == 'communaux',\
    'A("communal").n(\'p\')=>communaux'


def test_declension_fr_499():
    assert (
N("commune").g('f').n('p').realize()   
    ) == 'communes',\
    'N("commune").g(\'f\').n(\'p\')=>communes'


def test_declension_fr_500():
    assert (
N("communiant").g('m').n('p').realize()   
    ) == 'communiants',\
    'N("communiant").g(\'m\').n(\'p\')=>communiants'


def test_declension_fr_501():
    assert (
N("communication").g('f').n('p').realize()   
    ) == 'communications',\
    'N("communication").g(\'f\').n(\'p\')=>communications'


def test_declension_fr_502():
    assert (
N("communion").g('f').n('p').realize()   
    ) == 'communions',\
    'N("communion").g(\'f\').n(\'p\')=>communions'


def test_declension_fr_503():
    assert (
N("compagne").g('f').n('p').realize()   
    ) == 'compagnes',\
    'N("compagne").g(\'f\').n(\'p\')=>compagnes'


def test_declension_fr_504():
    assert (
N("compagnie").g('f').n('p').realize()   
    ) == 'compagnies',\
    'N("compagnie").g(\'f\').n(\'p\')=>compagnies'


def test_declension_fr_505():
    assert (
N("compagnon").g('m').n('p').realize()   
    ) == 'compagnons',\
    'N("compagnon").g(\'m\').n(\'p\')=>compagnons'


def test_declension_fr_506():
    assert (
N("comparaison").g('f').n('p').realize()   
    ) == 'comparaisons',\
    'N("comparaison").g(\'f\').n(\'p\')=>comparaisons'


def test_declension_fr_507():
    assert (
N("compassion").g('f').n('p').realize()   
    ) == 'compassions',\
    'N("compassion").g(\'f\').n(\'p\')=>compassions'


def test_declension_fr_508():
    assert (
A("complet").n('p').realize()   
    ) == 'complets',\
    'A("complet").n(\'p\')=>complets'


def test_declension_fr_509():
    assert (
N("compliment").g('m').n('p').realize()   
    ) == 'compliments',\
    'N("compliment").g(\'m\').n(\'p\')=>compliments'


def test_declension_fr_510():
    assert (
N("composition").g('f').n('p').realize()   
    ) == 'compositions',\
    'N("composition").g(\'f\').n(\'p\')=>compositions'


def test_declension_fr_511():
    assert (
N("compte").g('m').n('p').realize()   
    ) == 'comptes',\
    'N("compte").g(\'m\').n(\'p\')=>comptes'


def test_declension_fr_512():
    assert (
N("comte").g('m').n('p').realize()   
    ) == 'comtes',\
    'N("comte").g(\'m\').n(\'p\')=>comtes'


def test_declension_fr_513():
    assert (
N("comtesse").g('f').n('p').realize()   
    ) == 'comtesses',\
    'N("comtesse").g(\'f\').n(\'p\')=>comtesses'


def test_declension_fr_514():
    assert (
N("concert").g('m').n('p').realize()   
    ) == 'concerts',\
    'N("concert").g(\'m\').n(\'p\')=>concerts'


def test_declension_fr_515():
    assert (
N("concours").g('m').n('p').realize()   
    ) == 'concours',\
    'N("concours").g(\'m\').n(\'p\')=>concours'


def test_declension_fr_516():
    assert (
N("condisciple").n('p').realize()   
    ) == 'condisciples',\
    'N("condisciple").n(\'p\')=>condisciples'


def test_declension_fr_517():
    assert (
N("condition").g('f').n('p').realize()   
    ) == 'conditions',\
    'N("condition").g(\'f\').n(\'p\')=>conditions'


def test_declension_fr_518():
    assert (
N("conduite").g('f').n('p').realize()   
    ) == 'conduites',\
    'N("conduite").g(\'f\').n(\'p\')=>conduites'


def test_declension_fr_519():
    assert (
N("conférence").g('f').n('p').realize()   
    ) == 'conférences',\
    'N("conférence").g(\'f\').n(\'p\')=>conférences'


def test_declension_fr_520():
    assert (
N("confiance").g('f').n('p').realize()   
    ) == 'confiances',\
    'N("confiance").g(\'f\').n(\'p\')=>confiances'


def test_declension_fr_521():
    assert (
N("confiture").g('f').n('p').realize()   
    ) == 'confitures',\
    'N("confiture").g(\'f\').n(\'p\')=>confitures'


def test_declension_fr_522():
    assert (
N("confrère").g('m').n('p').realize()   
    ) == 'confrères',\
    'N("confrère").g(\'m\').n(\'p\')=>confrères'


def test_declension_fr_523():
    assert (
A("confus").n('p').realize()   
    ) == 'confus',\
    'A("confus").n(\'p\')=>confus'


def test_declension_fr_524():
    assert (
N("congé").g('m').n('p').realize()   
    ) == 'congés',\
    'N("congé").g(\'m\').n(\'p\')=>congés'


def test_declension_fr_525():
    assert (
N("congrès").g('m').n('p').realize()   
    ) == 'congrès',\
    'N("congrès").g(\'m\').n(\'p\')=>congrès'


def test_declension_fr_526():
    assert (
N("connaissance").g('f').n('p').realize()   
    ) == 'connaissances',\
    'N("connaissance").g(\'f\').n(\'p\')=>connaissances'


def test_declension_fr_527():
    assert (
N("conscience").g('f').n('p').realize()   
    ) == 'consciences',\
    'N("conscience").g(\'f\').n(\'p\')=>consciences'


def test_declension_fr_528():
    assert (
N("conseil").g('m').n('p').realize()   
    ) == 'conseils',\
    'N("conseil").g(\'m\').n(\'p\')=>conseils'


def test_declension_fr_529():
    assert (
N("consentement").g('m').n('p').realize()   
    ) == 'consentements',\
    'N("consentement").g(\'m\').n(\'p\')=>consentements'


def test_declension_fr_530():
    assert (
N("conséquence").g('f').n('p').realize()   
    ) == 'conséquences',\
    'N("conséquence").g(\'f\').n(\'p\')=>conséquences'


def test_declension_fr_531():
    assert (
A("considérable").n('p').realize()   
    ) == 'considérables',\
    'A("considérable").n(\'p\')=>considérables'


def test_declension_fr_532():
    assert (
N("consolation").g('f').n('p').realize()   
    ) == 'consolations',\
    'N("consolation").g(\'f\').n(\'p\')=>consolations'


def test_declension_fr_533():
    assert (
A("constant").n('p').realize()   
    ) == 'constants',\
    'A("constant").n(\'p\')=>constants'


def test_declension_fr_534():
    assert (
N("construction").g('f').n('p').realize()   
    ) == 'constructions',\
    'N("construction").g(\'f\').n(\'p\')=>constructions'


def test_declension_fr_535():
    assert (
N("contact").g('m').n('p').realize()   
    ) == 'contacts',\
    'N("contact").g(\'m\').n(\'p\')=>contacts'


def test_declension_fr_536():
    assert (
N("conte").g('m').n('p').realize()   
    ) == 'contes',\
    'N("conte").g(\'m\').n(\'p\')=>contes'


def test_declension_fr_537():
    assert (
A("content").n('p').realize()   
    ) == 'contents',\
    'A("content").n(\'p\')=>contents'


def test_declension_fr_538():
    assert (
N("contenu").g('m').n('p').realize()   
    ) == 'contenus',\
    'N("contenu").g(\'m\').n(\'p\')=>contenus'


def test_declension_fr_539():
    assert (
A("continuel").n('p').realize()   
    ) == 'continuels',\
    'A("continuel").n(\'p\')=>continuels'


def test_declension_fr_540():
    assert (
A("contraire").n('p').realize()   
    ) == 'contraires',\
    'A("contraire").n(\'p\')=>contraires'


def test_declension_fr_541():
    assert (
N("contrée").g('f').n('p').realize()   
    ) == 'contrées',\
    'N("contrée").g(\'f\').n(\'p\')=>contrées'


def test_declension_fr_542():
    assert (
A("convenable").n('p').realize()   
    ) == 'convenables',\
    'A("convenable").n(\'p\')=>convenables'


def test_declension_fr_543():
    assert (
N("conversation").g('f').n('p').realize()   
    ) == 'conversations',\
    'N("conversation").g(\'f\').n(\'p\')=>conversations'


def test_declension_fr_544():
    assert (
N("conviction").g('f').n('p').realize()   
    ) == 'convictions',\
    'N("conviction").g(\'f\').n(\'p\')=>convictions'


def test_declension_fr_545():
    assert (
N("coq").g('m').n('p').realize()   
    ) == 'coqs',\
    'N("coq").g(\'m\').n(\'p\')=>coqs'


def test_declension_fr_546():
    assert (
N("coquelicot").g('m').n('p').realize()   
    ) == 'coquelicots',\
    'N("coquelicot").g(\'m\').n(\'p\')=>coquelicots'


def test_declension_fr_547():
    assert (
A("coquet").n('p').realize()   
    ) == 'coquets',\
    'A("coquet").n(\'p\')=>coquets'


def test_declension_fr_548():
    assert (
N("coquille").g('f').n('p').realize()   
    ) == 'coquilles',\
    'N("coquille").g(\'f\').n(\'p\')=>coquilles'


def test_declension_fr_549():
    assert (
N("corbeau").g('m').n('p').realize()   
    ) == 'corbeaux',\
    'N("corbeau").g(\'m\').n(\'p\')=>corbeaux'


def test_declension_fr_550():
    assert (
N("corbeille").g('f').n('p').realize()   
    ) == 'corbeilles',\
    'N("corbeille").g(\'f\').n(\'p\')=>corbeilles'


def test_declension_fr_551():
    assert (
N("corde").g('f').n('p').realize()   
    ) == 'cordes',\
    'N("corde").g(\'f\').n(\'p\')=>cordes'


def test_declension_fr_552():
    assert (
N("cordial").g('m').n('p').realize()   
    ) == 'cordiaux',\
    'N("cordial").g(\'m\').n(\'p\')=>cordiaux'


def test_declension_fr_553():
    assert (
N("cordonnier").g('m').n('p').realize()   
    ) == 'cordonniers',\
    'N("cordonnier").g(\'m\').n(\'p\')=>cordonniers'


def test_declension_fr_554():
    assert (
N("corne").g('f').n('p').realize()   
    ) == 'cornes',\
    'N("corne").g(\'f\').n(\'p\')=>cornes'


def test_declension_fr_555():
    assert (
N("corniche").g('f').n('p').realize()   
    ) == 'corniches',\
    'N("corniche").g(\'f\').n(\'p\')=>corniches'


def test_declension_fr_556():
    assert (
N("corolle").g('f').n('p').realize()   
    ) == 'corolles',\
    'N("corolle").g(\'f\').n(\'p\')=>corolles'


def test_declension_fr_557():
    assert (
N("corps").g('m').n('p').realize()   
    ) == 'corps',\
    'N("corps").g(\'m\').n(\'p\')=>corps'


def test_declension_fr_558():
    assert (
N("correction").g('f').n('p').realize()   
    ) == 'corrections',\
    'N("correction").g(\'f\').n(\'p\')=>corrections'


def test_declension_fr_559():
    assert (
N("correspondance").g('f').n('p').realize()   
    ) == 'correspondances',\
    'N("correspondance").g(\'f\').n(\'p\')=>correspondances'


def test_declension_fr_560():
    assert (
N("corridor").g('m').n('p').realize()   
    ) == 'corridors',\
    'N("corridor").g(\'m\').n(\'p\')=>corridors'


def test_declension_fr_561():
    assert (
N("cortège").g('m').n('p').realize()   
    ) == 'cortèges',\
    'N("cortège").g(\'m\').n(\'p\')=>cortèges'


def test_declension_fr_562():
    assert (
N("costume").g('m').n('p').realize()   
    ) == 'costumes',\
    'N("costume").g(\'m\').n(\'p\')=>costumes'


def test_declension_fr_563():
    assert (
N("côte").g('f').n('p').realize()   
    ) == 'côtes',\
    'N("côte").g(\'f\').n(\'p\')=>côtes'


def test_declension_fr_564():
    assert (
N("côté").g('m').n('p').realize()   
    ) == 'côtés',\
    'N("côté").g(\'m\').n(\'p\')=>côtés'


def test_declension_fr_565():
    assert (
N("coton").g('m').n('p').realize()   
    ) == 'cotons',\
    'N("coton").g(\'m\').n(\'p\')=>cotons'


def test_declension_fr_566():
    assert (
N("cou").g('m').n('p').realize()   
    ) == 'cous',\
    'N("cou").g(\'m\').n(\'p\')=>cous'


def test_declension_fr_567():
    assert (
N("couche").g('f').n('p').realize()   
    ) == 'couches',\
    'N("couche").g(\'f\').n(\'p\')=>couches'


def test_declension_fr_568():
    assert (
N("coucou").g('m').n('p').realize()   
    ) == 'coucous',\
    'N("coucou").g(\'m\').n(\'p\')=>coucous'


def test_declension_fr_569():
    assert (
N("coude").g('m').n('p').realize()   
    ) == 'coudes',\
    'N("coude").g(\'m\').n(\'p\')=>coudes'


def test_declension_fr_570():
    assert (
N("couleur").g('f').n('p').realize()   
    ) == 'couleurs',\
    'N("couleur").g(\'f\').n(\'p\')=>couleurs'


def test_declension_fr_571():
    assert (
N("couloir").g('m').n('p').realize()   
    ) == 'couloirs',\
    'N("couloir").g(\'m\').n(\'p\')=>couloirs'


def test_declension_fr_572():
    assert (
N("coup").g('m').n('p').realize()   
    ) == 'coups',\
    'N("coup").g(\'m\').n(\'p\')=>coups'


def test_declension_fr_573():
    assert (
A("coupable").n('p').realize()   
    ) == 'coupables',\
    'A("coupable").n(\'p\')=>coupables'


def test_declension_fr_574():
    assert (
N("coupe").g('f').n('p').realize()   
    ) == 'coupes',\
    'N("coupe").g(\'f\').n(\'p\')=>coupes'


def test_declension_fr_575():
    assert (
N("cour").g('f').n('p').realize()   
    ) == 'cours',\
    'N("cour").g(\'f\').n(\'p\')=>cours'


def test_declension_fr_576():
    assert (
N("courage").g('m').n('p').realize()   
    ) == 'courages',\
    'N("courage").g(\'m\').n(\'p\')=>courages'


def test_declension_fr_577():
    assert (
A("courageux").n('p').realize()   
    ) == 'courageux',\
    'A("courageux").n(\'p\')=>courageux'


def test_declension_fr_578():
    assert (
A("courant").n('p').realize()   
    ) == 'courants',\
    'A("courant").n(\'p\')=>courants'


def test_declension_fr_579():
    assert (
N("coureur").g('m').n('p').realize()   
    ) == 'coureurs',\
    'N("coureur").g(\'m\').n(\'p\')=>coureurs'


def test_declension_fr_580():
    assert (
N("couronne").g('f').n('p').realize()   
    ) == 'couronnes',\
    'N("couronne").g(\'f\').n(\'p\')=>couronnes'


def test_declension_fr_581():
    assert (
N("courrier").g('m').n('p').realize()   
    ) == 'courriers',\
    'N("courrier").g(\'m\').n(\'p\')=>courriers'


def test_declension_fr_582():
    assert (
N("cours").g('m').n('p').realize()   
    ) == 'cours',\
    'N("cours").g(\'m\').n(\'p\')=>cours'


def test_declension_fr_583():
    assert (
N("course").g('f').n('p').realize()   
    ) == 'courses',\
    'N("course").g(\'f\').n(\'p\')=>courses'


def test_declension_fr_584():
    assert (
A("court").n('p').realize()   
    ) == 'courts',\
    'A("court").n(\'p\')=>courts'


def test_declension_fr_585():
    assert (
N("cousin").g('m').n('p').realize()   
    ) == 'cousins',\
    'N("cousin").g(\'m\').n(\'p\')=>cousins'


def test_declension_fr_586():
    assert (
N("coussin").g('m').n('p').realize()   
    ) == 'coussins',\
    'N("coussin").g(\'m\').n(\'p\')=>coussins'


def test_declension_fr_587():
    assert (
N("couteau").g('m').n('p').realize()   
    ) == 'couteaux',\
    'N("couteau").g(\'m\').n(\'p\')=>couteaux'


def test_declension_fr_588():
    assert (
N("coutume").g('f').n('p').realize()   
    ) == 'coutumes',\
    'N("coutume").g(\'f\').n(\'p\')=>coutumes'


def test_declension_fr_589():
    assert (
N("couture").g('f').n('p').realize()   
    ) == 'coutures',\
    'N("couture").g(\'f\').n(\'p\')=>coutures'


def test_declension_fr_590():
    assert (
N("couvercle").g('m').n('p').realize()   
    ) == 'couvercles',\
    'N("couvercle").g(\'m\').n(\'p\')=>couvercles'


def test_declension_fr_591():
    assert (
N("couvert").g('m').n('p').realize()   
    ) == 'couverts',\
    'N("couvert").g(\'m\').n(\'p\')=>couverts'


def test_declension_fr_592():
    assert (
N("couverture").g('f').n('p').realize()   
    ) == 'couvertures',\
    'N("couverture").g(\'f\').n(\'p\')=>couvertures'


def test_declension_fr_593():
    assert (
N("crainte").g('f').n('p').realize()   
    ) == 'craintes',\
    'N("crainte").g(\'f\').n(\'p\')=>craintes'


def test_declension_fr_594():
    assert (
N("craquement").g('m').n('p').realize()   
    ) == 'craquements',\
    'N("craquement").g(\'m\').n(\'p\')=>craquements'


def test_declension_fr_595():
    assert (
N("crayon").g('m').n('p').realize()   
    ) == 'crayons',\
    'N("crayon").g(\'m\').n(\'p\')=>crayons'


def test_declension_fr_596():
    assert (
N("créateur").g('m').n('p').realize()   
    ) == 'créateurs',\
    'N("créateur").g(\'m\').n(\'p\')=>créateurs'


def test_declension_fr_597():
    assert (
N("créature").g('f').n('p').realize()   
    ) == 'créatures',\
    'N("créature").g(\'f\').n(\'p\')=>créatures'


def test_declension_fr_598():
    assert (
N("crèche").g('f').n('p').realize()   
    ) == 'crèches',\
    'N("crèche").g(\'f\').n(\'p\')=>crèches'


def test_declension_fr_599():
    assert (
N("crème").g('f').n('p').realize()   
    ) == 'crèmes',\
    'N("crème").g(\'f\').n(\'p\')=>crèmes'


def test_declension_fr_600():
    assert (
N("crêpe").g('f').n('p').realize()   
    ) == 'crêpes',\
    'N("crêpe").g(\'f\').n(\'p\')=>crêpes'


def test_declension_fr_601():
    assert (
N("crépuscule").g('m').n('p').realize()   
    ) == 'crépuscules',\
    'N("crépuscule").g(\'m\').n(\'p\')=>crépuscules'


def test_declension_fr_602():
    assert (
A("creux").n('p').realize()   
    ) == 'creux',\
    'A("creux").n(\'p\')=>creux'


def test_declension_fr_603():
    assert (
N("cri").g('m').n('p').realize()   
    ) == 'cris',\
    'N("cri").g(\'m\').n(\'p\')=>cris'


def test_declension_fr_604():
    assert (
N("crime").g('m').n('p').realize()   
    ) == 'crimes',\
    'N("crime").g(\'m\').n(\'p\')=>crimes'


def test_declension_fr_605():
    assert (
N("crise").g('f').n('p').realize()   
    ) == 'crises',\
    'N("crise").g(\'f\').n(\'p\')=>crises'


def test_declension_fr_606():
    assert (
N("cristal").g('m').n('p').realize()   
    ) == 'cristaux',\
    'N("cristal").g(\'m\').n(\'p\')=>cristaux'


def test_declension_fr_607():
    assert (
N("croix").g('f').n('p').realize()   
    ) == 'croix',\
    'N("croix").g(\'f\').n(\'p\')=>croix'


def test_declension_fr_608():
    assert (
N("croûte").g('f').n('p').realize()   
    ) == 'croûtes',\
    'N("croûte").g(\'f\').n(\'p\')=>croûtes'


def test_declension_fr_609():
    assert (
N("crucifix").g('m').n('p').realize()   
    ) == 'crucifix',\
    'N("crucifix").g(\'m\').n(\'p\')=>crucifix'


def test_declension_fr_610():
    assert (
A("cruel").n('p').realize()   
    ) == 'cruels',\
    'A("cruel").n(\'p\')=>cruels'


def test_declension_fr_611():
    assert (
N("cueillette").g('f').n('p').realize()   
    ) == 'cueillettes',\
    'N("cueillette").g(\'f\').n(\'p\')=>cueillettes'


def test_declension_fr_612():
    assert (
N("cuiller").g('f').n('p').realize()   
    ) == 'cuillers',\
    'N("cuiller").g(\'f\').n(\'p\')=>cuillers'


def test_declension_fr_613():
    assert (
N("cuillère").g('f').n('p').realize()   
    ) == 'cuillères',\
    'N("cuillère").g(\'f\').n(\'p\')=>cuillères'


def test_declension_fr_614():
    assert (
N("cuir").g('m').n('p').realize()   
    ) == 'cuirs',\
    'N("cuir").g(\'m\').n(\'p\')=>cuirs'


def test_declension_fr_615():
    assert (
N("cuisine").g('f').n('p').realize()   
    ) == 'cuisines',\
    'N("cuisine").g(\'f\').n(\'p\')=>cuisines'


def test_declension_fr_616():
    assert (
N("cuisinière").g('f').n('p').realize()   
    ) == 'cuisinières',\
    'N("cuisinière").g(\'f\').n(\'p\')=>cuisinières'


def test_declension_fr_617():
    assert (
N("cuivre").g('m').n('p').realize()   
    ) == 'cuivres',\
    'N("cuivre").g(\'m\').n(\'p\')=>cuivres'


def test_declension_fr_618():
    assert (
N("culotte").g('f').n('p').realize()   
    ) == 'culottes',\
    'N("culotte").g(\'f\').n(\'p\')=>culottes'


def test_declension_fr_619():
    assert (
N("cultivateur").g('m').n('p').realize()   
    ) == 'cultivateurs',\
    'N("cultivateur").g(\'m\').n(\'p\')=>cultivateurs'


def test_declension_fr_620():
    assert (
N("culture").g('f').n('p').realize()   
    ) == 'cultures',\
    'N("culture").g(\'f\').n(\'p\')=>cultures'


def test_declension_fr_621():
    assert (
N("curé").g('m').n('p').realize()   
    ) == 'curés',\
    'N("curé").g(\'m\').n(\'p\')=>curés'


def test_declension_fr_622():
    assert (
A("curieux").n('p').realize()   
    ) == 'curieux',\
    'A("curieux").n(\'p\')=>curieux'


def test_declension_fr_623():
    assert (
N("curiosité").g('f').n('p').realize()   
    ) == 'curiosités',\
    'N("curiosité").g(\'f\').n(\'p\')=>curiosités'


def test_declension_fr_624():
    assert (
N("cycliste").n('p').realize()   
    ) == 'cyclistes',\
    'N("cycliste").n(\'p\')=>cyclistes'


def test_declension_fr_625():
    assert (
N("cygne").g('m').n('p').realize()   
    ) == 'cygnes',\
    'N("cygne").g(\'m\').n(\'p\')=>cygnes'


def test_declension_fr_626():
    assert (
N("dahlia").g('m').n('p').realize()   
    ) == 'dahlias',\
    'N("dahlia").g(\'m\').n(\'p\')=>dahlias'


def test_declension_fr_627():
    assert (
N("dame").g('f').n('p').realize()   
    ) == 'dames',\
    'N("dame").g(\'f\').n(\'p\')=>dames'


def test_declension_fr_628():
    assert (
N("danger").g('m').n('p').realize()   
    ) == 'dangers',\
    'N("danger").g(\'m\').n(\'p\')=>dangers'


def test_declension_fr_629():
    assert (
A("dangereux").n('p').realize()   
    ) == 'dangereux',\
    'A("dangereux").n(\'p\')=>dangereux'


def test_declension_fr_630():
    assert (
N("danse").g('f').n('p').realize()   
    ) == 'danses',\
    'N("danse").g(\'f\').n(\'p\')=>danses'


def test_declension_fr_631():
    assert (
N("date").g('f').n('p').realize()   
    ) == 'dates',\
    'N("date").g(\'f\').n(\'p\')=>dates'


def test_declension_fr_632():
    assert (
N("débris").g('m').n('p').realize()   
    ) == 'débris',\
    'N("débris").g(\'m\').n(\'p\')=>débris'


def test_declension_fr_633():
    assert (
N("début").g('m').n('p').realize()   
    ) == 'débuts',\
    'N("début").g(\'m\').n(\'p\')=>débuts'


def test_declension_fr_634():
    assert (
N("décembre").g('m').n('p').realize()   
    ) == 'décembres',\
    'N("décembre").g(\'m\').n(\'p\')=>décembres'


def test_declension_fr_635():
    assert (
N("déception").g('f').n('p').realize()   
    ) == 'déceptions',\
    'N("déception").g(\'f\').n(\'p\')=>déceptions'


def test_declension_fr_636():
    assert (
N("décision").g('f').n('p').realize()   
    ) == 'décisions',\
    'N("décision").g(\'f\').n(\'p\')=>décisions'


def test_declension_fr_637():
    assert (
N("découverte").g('f').n('p').realize()   
    ) == 'découvertes',\
    'N("découverte").g(\'f\').n(\'p\')=>découvertes'


def test_declension_fr_638():
    assert (
N("défaut").g('m').n('p').realize()   
    ) == 'défauts',\
    'N("défaut").g(\'m\').n(\'p\')=>défauts'


def test_declension_fr_639():
    assert (
N("défense").g('f').n('p').realize()   
    ) == 'défenses',\
    'N("défense").g(\'f\').n(\'p\')=>défenses'


def test_declension_fr_640():
    assert (
N("défenseur").g('m').n('p').realize()   
    ) == 'défenseurs',\
    'N("défenseur").g(\'m\').n(\'p\')=>défenseurs'


def test_declension_fr_641():
    assert (
N("défunt").g('m').n('p').realize()   
    ) == 'défunts',\
    'N("défunt").g(\'m\').n(\'p\')=>défunts'


def test_declension_fr_642():
    assert (
N("dégât").g('m').n('p').realize()   
    ) == 'dégâts',\
    'N("dégât").g(\'m\').n(\'p\')=>dégâts'


def test_declension_fr_643():
    assert (
N("degré").g('m').n('p').realize()   
    ) == 'degrés',\
    'N("degré").g(\'m\').n(\'p\')=>degrés'


def test_declension_fr_644():
    assert (
A("délicat").n('p').realize()   
    ) == 'délicats',\
    'A("délicat").n(\'p\')=>délicats'


def test_declension_fr_645():
    assert (
A("délicieux").n('p').realize()   
    ) == 'délicieux',\
    'A("délicieux").n(\'p\')=>délicieux'


def test_declension_fr_646():
    assert (
N("demande").g('f').n('p').realize()   
    ) == 'demandes',\
    'N("demande").g(\'f\').n(\'p\')=>demandes'


def test_declension_fr_647():
    assert (
N("démarche").g('f').n('p').realize()   
    ) == 'démarches',\
    'N("démarche").g(\'f\').n(\'p\')=>démarches'


def test_declension_fr_648():
    assert (
N("demeure").g('f').n('p').realize()   
    ) == 'demeures',\
    'N("demeure").g(\'f\').n(\'p\')=>demeures'


def test_declension_fr_649():
    assert (
N("demi").g('m').n('p').realize()   
    ) == 'demis',\
    'N("demi").g(\'m\').n(\'p\')=>demis'


def test_declension_fr_650():
    assert (
N("demoiselle").g('f').n('p').realize()   
    ) == 'demoiselles',\
    'N("demoiselle").g(\'f\').n(\'p\')=>demoiselles'


def test_declension_fr_651():
    assert (
N("dent").g('f').n('p').realize()   
    ) == 'dents',\
    'N("dent").g(\'f\').n(\'p\')=>dents'


def test_declension_fr_652():
    assert (
N("dentelle").g('f').n('p').realize()   
    ) == 'dentelles',\
    'N("dentelle").g(\'f\').n(\'p\')=>dentelles'


def test_declension_fr_653():
    assert (
A("dénudé").n('p').realize()   
    ) == 'dénudés',\
    'A("dénudé").n(\'p\')=>dénudés'


def test_declension_fr_654():
    assert (
N("départ").g('m').n('p').realize()   
    ) == 'départs',\
    'N("départ").g(\'m\').n(\'p\')=>départs'


def test_declension_fr_655():
    assert (
N("dépens").g('m').n('p').realize()   
    ) == 'dépens',\
    'N("dépens").g(\'m\').n(\'p\')=>dépens'


def test_declension_fr_656():
    assert (
N("dépôt").g('m').n('p').realize()   
    ) == 'dépôts',\
    'N("dépôt").g(\'m\').n(\'p\')=>dépôts'


def test_declension_fr_657():
    assert (
A("dernier").n('p').realize()   
    ) == 'derniers',\
    'A("dernier").n(\'p\')=>derniers'


def test_declension_fr_658():
    assert (
A("désagréable").n('p').realize()   
    ) == 'désagréables',\
    'A("désagréable").n(\'p\')=>désagréables'


def test_declension_fr_659():
    assert (
N("désastre").g('m').n('p').realize()   
    ) == 'désastres',\
    'N("désastre").g(\'m\').n(\'p\')=>désastres'


def test_declension_fr_660():
    assert (
N("descente").g('f').n('p').realize()   
    ) == 'descentes',\
    'N("descente").g(\'f\').n(\'p\')=>descentes'


def test_declension_fr_661():
    assert (
N("description").g('f').n('p').realize()   
    ) == 'descriptions',\
    'N("description").g(\'f\').n(\'p\')=>descriptions'


def test_declension_fr_662():
    assert (
A("désert").n('p').realize()   
    ) == 'déserts',\
    'A("désert").n(\'p\')=>déserts'


def test_declension_fr_663():
    assert (
N("désespoir").g('m').n('p').realize()   
    ) == 'désespoirs',\
    'N("désespoir").g(\'m\').n(\'p\')=>désespoirs'


def test_declension_fr_664():
    assert (
N("désir").g('m').n('p').realize()   
    ) == 'désirs',\
    'N("désir").g(\'m\').n(\'p\')=>désirs'


def test_declension_fr_665():
    assert (
A("désireux").n('p').realize()   
    ) == 'désireux',\
    'A("désireux").n(\'p\')=>désireux'


def test_declension_fr_666():
    assert (
N("désobéissance").g('f').n('p').realize()   
    ) == 'désobéissances',\
    'N("désobéissance").g(\'f\').n(\'p\')=>désobéissances'


def test_declension_fr_667():
    assert (
A("désobéissant").n('p').realize()   
    ) == 'désobéissants',\
    'A("désobéissant").n(\'p\')=>désobéissants'


def test_declension_fr_668():
    assert (
N("désolation").g('f').n('p').realize()   
    ) == 'désolations',\
    'N("désolation").g(\'f\').n(\'p\')=>désolations'


def test_declension_fr_669():
    assert (
N("désordre").g('m').n('p').realize()   
    ) == 'désordres',\
    'N("désordre").g(\'m\').n(\'p\')=>désordres'


def test_declension_fr_670():
    assert (
N("dessein").g('m').n('p').realize()   
    ) == 'desseins',\
    'N("dessein").g(\'m\').n(\'p\')=>desseins'


def test_declension_fr_671():
    assert (
N("dessert").g('m').n('p').realize()   
    ) == 'desserts',\
    'N("dessert").g(\'m\').n(\'p\')=>desserts'


def test_declension_fr_672():
    assert (
N("dessin").g('m').n('p').realize()   
    ) == 'dessins',\
    'N("dessin").g(\'m\').n(\'p\')=>dessins'


def test_declension_fr_673():
    assert (
N("destination").g('f').n('p').realize()   
    ) == 'destinations',\
    'N("destination").g(\'f\').n(\'p\')=>destinations'


def test_declension_fr_674():
    assert (
N("destinée").g('f').n('p').realize()   
    ) == 'destinées',\
    'N("destinée").g(\'f\').n(\'p\')=>destinées'


def test_declension_fr_675():
    assert (
N("détail").g('m').n('p').realize()   
    ) == 'détails',\
    'N("détail").g(\'m\').n(\'p\')=>détails'


def test_declension_fr_676():
    assert (
N("détour").g('m').n('p').realize()   
    ) == 'détours',\
    'N("détour").g(\'m\').n(\'p\')=>détours'


def test_declension_fr_677():
    assert (
N("dette").g('f').n('p').realize()   
    ) == 'dettes',\
    'N("dette").g(\'f\').n(\'p\')=>dettes'


def test_declension_fr_678():
    assert (
N("deuil").g('m').n('p').realize()   
    ) == 'deuils',\
    'N("deuil").g(\'m\').n(\'p\')=>deuils'


def test_declension_fr_679():
    assert (
N("dévouement").g('m').n('p').realize()   
    ) == 'dévouements',\
    'N("dévouement").g(\'m\').n(\'p\')=>dévouements'


def test_declension_fr_680():
    assert (
N("diable").g('m').n('p').realize()   
    ) == 'diables',\
    'N("diable").g(\'m\').n(\'p\')=>diables'


def test_declension_fr_681():
    assert (
N("diamant").g('m').n('p').realize()   
    ) == 'diamants',\
    'N("diamant").g(\'m\').n(\'p\')=>diamants'


def test_declension_fr_682():
    assert (
N("dictée").g('f').n('p').realize()   
    ) == 'dictées',\
    'N("dictée").g(\'f\').n(\'p\')=>dictées'


def test_declension_fr_683():
    assert (
N("dictionnaire").g('m').n('p').realize()   
    ) == 'dictionnaires',\
    'N("dictionnaire").g(\'m\').n(\'p\')=>dictionnaires'


def test_declension_fr_684():
    assert (
N("dieu").g('m').n('p').realize()   
    ) == 'dieux',\
    'N("dieu").g(\'m\').n(\'p\')=>dieux'


def test_declension_fr_685():
    assert (
N("différence").g('f').n('p').realize()   
    ) == 'différences',\
    'N("différence").g(\'f\').n(\'p\')=>différences'


def test_declension_fr_686():
    assert (
A("différent").n('p').realize()   
    ) == 'différents',\
    'A("différent").n(\'p\')=>différents'


def test_declension_fr_687():
    assert (
A("difficile").n('p').realize()   
    ) == 'difficiles',\
    'A("difficile").n(\'p\')=>difficiles'


def test_declension_fr_688():
    assert (
N("difficulté").g('f').n('p').realize()   
    ) == 'difficultés',\
    'N("difficulté").g(\'f\').n(\'p\')=>difficultés'


def test_declension_fr_689():
    assert (
A("digne").n('p').realize()   
    ) == 'dignes',\
    'A("digne").n(\'p\')=>dignes'


def test_declension_fr_690():
    assert (
N("dimanche").g('m').n('p').realize()   
    ) == 'dimanches',\
    'N("dimanche").g(\'m\').n(\'p\')=>dimanches'


def test_declension_fr_691():
    assert (
N("dimension").g('f').n('p').realize()   
    ) == 'dimensions',\
    'N("dimension").g(\'f\').n(\'p\')=>dimensions'


def test_declension_fr_692():
    assert (
N("directeur").g('m').n('p').realize()   
    ) == 'directeurs',\
    'N("directeur").g(\'m\').n(\'p\')=>directeurs'


def test_declension_fr_693():
    assert (
N("direction").g('f').n('p').realize()   
    ) == 'directions',\
    'N("direction").g(\'f\').n(\'p\')=>directions'


def test_declension_fr_694():
    assert (
N("directrice").g('f').n('p').realize()   
    ) == 'directrices',\
    'N("directrice").g(\'f\').n(\'p\')=>directrices'


def test_declension_fr_695():
    assert (
N("discours").g('m').n('p').realize()   
    ) == 'discours',\
    'N("discours").g(\'m\').n(\'p\')=>discours'


def test_declension_fr_696():
    assert (
N("discussion").g('f').n('p').realize()   
    ) == 'discussions',\
    'N("discussion").g(\'f\').n(\'p\')=>discussions'


def test_declension_fr_697():
    assert (
N("disparition").g('f').n('p').realize()   
    ) == 'disparitions',\
    'N("disparition").g(\'f\').n(\'p\')=>disparitions'


def test_declension_fr_698():
    assert (
N("disposition").g('f').n('p').realize()   
    ) == 'dispositions',\
    'N("disposition").g(\'f\').n(\'p\')=>dispositions'


def test_declension_fr_699():
    assert (
N("distance").g('f').n('p').realize()   
    ) == 'distances',\
    'N("distance").g(\'f\').n(\'p\')=>distances'


def test_declension_fr_700():
    assert (
N("distinction").g('f').n('p').realize()   
    ) == 'distinctions',\
    'N("distinction").g(\'f\').n(\'p\')=>distinctions'


def test_declension_fr_701():
    assert (
N("distraction").g('f').n('p').realize()   
    ) == 'distractions',\
    'N("distraction").g(\'f\').n(\'p\')=>distractions'


def test_declension_fr_702():
    assert (
A("distrait").n('p').realize()   
    ) == 'distraits',\
    'A("distrait").n(\'p\')=>distraits'


def test_declension_fr_703():
    assert (
N("distribution").g('f').n('p').realize()   
    ) == 'distributions',\
    'N("distribution").g(\'f\').n(\'p\')=>distributions'


def test_declension_fr_704():
    assert (
A("divin").n('p').realize()   
    ) == 'divins',\
    'A("divin").n(\'p\')=>divins'


def test_declension_fr_705():
    assert (
N("division").g('f').n('p').realize()   
    ) == 'divisions',\
    'N("division").g(\'f\').n(\'p\')=>divisions'


def test_declension_fr_706():
    assert (
N("dizaine").g('f').n('p').realize()   
    ) == 'dizaines',\
    'N("dizaine").g(\'f\').n(\'p\')=>dizaines'


def test_declension_fr_707():
    assert (
A("docile").n('p').realize()   
    ) == 'dociles',\
    'A("docile").n(\'p\')=>dociles'


def test_declension_fr_708():
    assert (
N("docteur").g('m').n('p').realize()   
    ) == 'docteurs',\
    'N("docteur").g(\'m\').n(\'p\')=>docteurs'


def test_declension_fr_709():
    assert (
N("doigt").g('m').n('p').realize()   
    ) == 'doigts',\
    'N("doigt").g(\'m\').n(\'p\')=>doigts'


def test_declension_fr_710():
    assert (
N("domaine").g('m').n('p').realize()   
    ) == 'domaines',\
    'N("domaine").g(\'m\').n(\'p\')=>domaines'


def test_declension_fr_711():
    assert (
A("domestique").n('p').realize()   
    ) == 'domestiques',\
    'A("domestique").n(\'p\')=>domestiques'


def test_declension_fr_712():
    assert (
N("domicile").g('m').n('p').realize()   
    ) == 'domiciles',\
    'N("domicile").g(\'m\').n(\'p\')=>domiciles'


def test_declension_fr_713():
    assert (
N("dommage").g('m').n('p').realize()   
    ) == 'dommages',\
    'N("dommage").g(\'m\').n(\'p\')=>dommages'


def test_declension_fr_714():
    assert (
N("dompteur").g('m').n('p').realize()   
    ) == 'dompteurs',\
    'N("dompteur").g(\'m\').n(\'p\')=>dompteurs'


def test_declension_fr_715():
    assert (
N("don").g('m').n('p').realize()   
    ) == 'dons',\
    'N("don").g(\'m\').n(\'p\')=>dons'


def test_declension_fr_716():
    assert (
N("dortoir").g('m').n('p').realize()   
    ) == 'dortoirs',\
    'N("dortoir").g(\'m\').n(\'p\')=>dortoirs'


def test_declension_fr_717():
    assert (
N("dos").g('m').n('p').realize()   
    ) == 'dos',\
    'N("dos").g(\'m\').n(\'p\')=>dos'


def test_declension_fr_718():
    assert (
N("dossier").g('m').n('p').realize()   
    ) == 'dossiers',\
    'N("dossier").g(\'m\').n(\'p\')=>dossiers'


def test_declension_fr_719():
    assert (
A("double").n('p').realize()   
    ) == 'doubles',\
    'A("double").n(\'p\')=>doubles'


def test_declension_fr_720():
    assert (
N("douceur").g('f').n('p').realize()   
    ) == 'douceurs',\
    'N("douceur").g(\'f\').n(\'p\')=>douceurs'


def test_declension_fr_721():
    assert (
N("douleur").g('f').n('p').realize()   
    ) == 'douleurs',\
    'N("douleur").g(\'f\').n(\'p\')=>douleurs'


def test_declension_fr_722():
    assert (
A("douloureux").n('p').realize()   
    ) == 'douloureux',\
    'A("douloureux").n(\'p\')=>douloureux'


def test_declension_fr_723():
    assert (
N("doute").g('m').n('p').realize()   
    ) == 'doutes',\
    'N("doute").g(\'m\').n(\'p\')=>doutes'


def test_declension_fr_724():
    assert (
A("doux").n('p').realize()   
    ) == 'doux',\
    'A("doux").n(\'p\')=>doux'


def test_declension_fr_725():
    assert (
N("douzaine").g('f').n('p').realize()   
    ) == 'douzaines',\
    'N("douzaine").g(\'f\').n(\'p\')=>douzaines'


def test_declension_fr_726():
    assert (
N("doyen").g('m').n('p').realize()   
    ) == 'doyens',\
    'N("doyen").g(\'m\').n(\'p\')=>doyens'


def test_declension_fr_727():
    assert (
N("drap").g('m').n('p').realize()   
    ) == 'draps',\
    'N("drap").g(\'m\').n(\'p\')=>draps'


def test_declension_fr_728():
    assert (
N("drapeau").g('m').n('p').realize()   
    ) == 'drapeaux',\
    'N("drapeau").g(\'m\').n(\'p\')=>drapeaux'


def test_declension_fr_729():
    assert (
A("droit").n('p').realize()   
    ) == 'droits',\
    'A("droit").n(\'p\')=>droits'


def test_declension_fr_730():
    assert (
A("drôle").n('p').realize()   
    ) == 'drôles',\
    'A("drôle").n(\'p\')=>drôles'


def test_declension_fr_731():
    assert (
N("duc").g('m').n('p').realize()   
    ) == 'ducs',\
    'N("duc").g(\'m\').n(\'p\')=>ducs'


def test_declension_fr_732():
    assert (
A("dur").n('p').realize()   
    ) == 'durs',\
    'A("dur").n(\'p\')=>durs'


def test_declension_fr_733():
    assert (
N("durée").g('f').n('p').realize()   
    ) == 'durées',\
    'N("durée").g(\'f\').n(\'p\')=>durées'


def test_declension_fr_734():
    assert (
N("duvet").g('m').n('p').realize()   
    ) == 'duvets',\
    'N("duvet").g(\'m\').n(\'p\')=>duvets'


def test_declension_fr_735():
    assert (
N("eau").g('f').n('p').realize()   
    ) == 'eaux',\
    'N("eau").g(\'f\').n(\'p\')=>eaux'


def test_declension_fr_736():
    assert (
N("échantillon").g('m').n('p').realize()   
    ) == 'échantillons',\
    'N("échantillon").g(\'m\').n(\'p\')=>échantillons'


def test_declension_fr_737():
    assert (
N("écharpe").g('f').n('p').realize()   
    ) == 'écharpes',\
    'N("écharpe").g(\'f\').n(\'p\')=>écharpes'


def test_declension_fr_738():
    assert (
N("échec").g('m').n('p').realize()   
    ) == 'échecs',\
    'N("échec").g(\'m\').n(\'p\')=>échecs'


def test_declension_fr_739():
    assert (
N("échelle").g('f').n('p').realize()   
    ) == 'échelles',\
    'N("échelle").g(\'f\').n(\'p\')=>échelles'


def test_declension_fr_740():
    assert (
N("écho").g('m').n('p').realize()   
    ) == 'échos',\
    'N("écho").g(\'m\').n(\'p\')=>échos'


def test_declension_fr_741():
    assert (
N("éclair").g('m').n('p').realize()   
    ) == 'éclairs',\
    'N("éclair").g(\'m\').n(\'p\')=>éclairs'


def test_declension_fr_742():
    assert (
N("éclat").g('m').n('p').realize()   
    ) == 'éclats',\
    'N("éclat").g(\'m\').n(\'p\')=>éclats'


def test_declension_fr_743():
    assert (
A("éclatant").n('p').realize()   
    ) == 'éclatants',\
    'A("éclatant").n(\'p\')=>éclatants'


def test_declension_fr_744():
    assert (
N("écluse").g('f').n('p').realize()   
    ) == 'écluses',\
    'N("écluse").g(\'f\').n(\'p\')=>écluses'


def test_declension_fr_745():
    assert (
N("école").g('f').n('p').realize()   
    ) == 'écoles',\
    'N("école").g(\'f\').n(\'p\')=>écoles'


def test_declension_fr_746():
    assert (
N("écolier").g('m').n('p').realize()   
    ) == 'écoliers',\
    'N("écolier").g(\'m\').n(\'p\')=>écoliers'


def test_declension_fr_747():
    assert (
N("économie").g('f').n('p').realize()   
    ) == 'économies',\
    'N("économie").g(\'f\').n(\'p\')=>économies'


def test_declension_fr_748():
    assert (
N("écorce").g('f').n('p').realize()   
    ) == 'écorces',\
    'N("écorce").g(\'f\').n(\'p\')=>écorces'


def test_declension_fr_749():
    assert (
N("écriture").g('f').n('p').realize()   
    ) == 'écritures',\
    'N("écriture").g(\'f\').n(\'p\')=>écritures'


def test_declension_fr_750():
    assert (
N("écrivain").g('m').n('p').realize()   
    ) == 'écrivains',\
    'N("écrivain").g(\'m\').n(\'p\')=>écrivains'


def test_declension_fr_751():
    assert (
N("écureuil").g('m').n('p').realize()   
    ) == 'écureuils',\
    'N("écureuil").g(\'m\').n(\'p\')=>écureuils'


def test_declension_fr_752():
    assert (
N("écurie").g('f').n('p').realize()   
    ) == 'écuries',\
    'N("écurie").g(\'f\').n(\'p\')=>écuries'


def test_declension_fr_753():
    assert (
N("éducation").g('f').n('p').realize()   
    ) == 'éducations',\
    'N("éducation").g(\'f\').n(\'p\')=>éducations'


def test_declension_fr_754():
    assert (
N("effet").g('m').n('p').realize()   
    ) == 'effets',\
    'N("effet").g(\'m\').n(\'p\')=>effets'


def test_declension_fr_755():
    assert (
N("effort").g('m').n('p').realize()   
    ) == 'efforts',\
    'N("effort").g(\'m\').n(\'p\')=>efforts'


def test_declension_fr_756():
    assert (
A("effroyable").n('p').realize()   
    ) == 'effroyables',\
    'A("effroyable").n(\'p\')=>effroyables'


def test_declension_fr_757():
    assert (
A("égal").n('p').realize()   
    ) == 'égaux',\
    'A("égal").n(\'p\')=>égaux'


def test_declension_fr_758():
    assert (
N("égard").g('m').n('p').realize()   
    ) == 'égards',\
    'N("égard").g(\'m\').n(\'p\')=>égards'


def test_declension_fr_759():
    assert (
N("église").g('f').n('p').realize()   
    ) == 'églises',\
    'N("église").g(\'f\').n(\'p\')=>églises'


def test_declension_fr_760():
    assert (
N("élan").g('m').n('p').realize()   
    ) == 'élans',\
    'N("élan").g(\'m\').n(\'p\')=>élans'


def test_declension_fr_761():
    assert (
N("électricité").g('f').n('p').realize()   
    ) == 'électricités',\
    'N("électricité").g(\'f\').n(\'p\')=>électricités'


def test_declension_fr_762():
    assert (
A("électrique").n('p').realize()   
    ) == 'électriques',\
    'A("électrique").n(\'p\')=>électriques'


def test_declension_fr_763():
    assert (
A("élégant").n('p').realize()   
    ) == 'élégants',\
    'A("élégant").n(\'p\')=>élégants'


def test_declension_fr_764():
    assert (
N("éléphant").g('m').n('p').realize()   
    ) == 'éléphants',\
    'N("éléphant").g(\'m\').n(\'p\')=>éléphants'


def test_declension_fr_765():
    assert (
N("élève").g('m').n('p').realize()   
    ) == 'élèves',\
    'N("élève").g(\'m\').n(\'p\')=>élèves'


def test_declension_fr_766():
    assert (
N("embarras").g('m').n('p').realize()   
    ) == 'embarras',\
    'N("embarras").g(\'m\').n(\'p\')=>embarras'


def test_declension_fr_767():
    assert (
N("émotion").g('f').n('p').realize()   
    ) == 'émotions',\
    'N("émotion").g(\'f\').n(\'p\')=>émotions'


def test_declension_fr_768():
    assert (
N("empereur").g('m').n('p').realize()   
    ) == 'empereurs',\
    'N("empereur").g(\'m\').n(\'p\')=>empereurs'


def test_declension_fr_769():
    assert (
N("emplacement").g('m').n('p').realize()   
    ) == 'emplacements',\
    'N("emplacement").g(\'m\').n(\'p\')=>emplacements'


def test_declension_fr_770():
    assert (
N("emploi").g('m').n('p').realize()   
    ) == 'emplois',\
    'N("emploi").g(\'m\').n(\'p\')=>emplois'


def test_declension_fr_771():
    assert (
N("employé").g('m').n('p').realize()   
    ) == 'employés',\
    'N("employé").g(\'m\').n(\'p\')=>employés'


def test_declension_fr_772():
    assert (
N("empressement").g('m').n('p').realize()   
    ) == 'empressements',\
    'N("empressement").g(\'m\').n(\'p\')=>empressements'


def test_declension_fr_773():
    assert (
A("enchanté").n('p').realize()   
    ) == 'enchantés',\
    'A("enchanté").n(\'p\')=>enchantés'


def test_declension_fr_774():
    assert (
N("encre").g('f').n('p').realize()   
    ) == 'encres',\
    'N("encre").g(\'f\').n(\'p\')=>encres'


def test_declension_fr_775():
    assert (
N("encrier").g('m').n('p').realize()   
    ) == 'encriers',\
    'N("encrier").g(\'m\').n(\'p\')=>encriers'


def test_declension_fr_776():
    assert (
N("endroit").g('m').n('p').realize()   
    ) == 'endroits',\
    'N("endroit").g(\'m\').n(\'p\')=>endroits'


def test_declension_fr_777():
    assert (
N("énergie").g('f').n('p').realize()   
    ) == 'énergies',\
    'N("énergie").g(\'f\').n(\'p\')=>énergies'


def test_declension_fr_778():
    assert (
A("énergique").n('p').realize()   
    ) == 'énergiques',\
    'A("énergique").n(\'p\')=>énergiques'


def test_declension_fr_779():
    assert (
N("enfance").g('f').n('p').realize()   
    ) == 'enfances',\
    'N("enfance").g(\'f\').n(\'p\')=>enfances'


def test_declension_fr_780():
    assert (
N("enfant").n('p').realize()   
    ) == 'enfants',\
    'N("enfant").n(\'p\')=>enfants'


def test_declension_fr_781():
    assert (
N("ennemi").g('m').n('p').realize()   
    ) == 'ennemis',\
    'N("ennemi").g(\'m\').n(\'p\')=>ennemis'


def test_declension_fr_782():
    assert (
N("ennui").g('m').n('p').realize()   
    ) == 'ennuis',\
    'N("ennui").g(\'m\').n(\'p\')=>ennuis'


def test_declension_fr_783():
    assert (
A("ennuyeux").n('p').realize()   
    ) == 'ennuyeux',\
    'A("ennuyeux").n(\'p\')=>ennuyeux'


def test_declension_fr_784():
    assert (
A("énorme").n('p').realize()   
    ) == 'énormes',\
    'A("énorme").n(\'p\')=>énormes'


def test_declension_fr_785():
    assert (
N("enquête").g('f').n('p').realize()   
    ) == 'enquêtes',\
    'N("enquête").g(\'f\').n(\'p\')=>enquêtes'


def test_declension_fr_786():
    assert (
N("enseignement").g('m').n('p').realize()   
    ) == 'enseignements',\
    'N("enseignement").g(\'m\').n(\'p\')=>enseignements'


def test_declension_fr_787():
    assert (
A("ensoleillé").n('p').realize()   
    ) == 'ensoleillés',\
    'A("ensoleillé").n(\'p\')=>ensoleillés'


def test_declension_fr_788():
    assert (
N("enterrement").g('m').n('p').realize()   
    ) == 'enterrements',\
    'N("enterrement").g(\'m\').n(\'p\')=>enterrements'


def test_declension_fr_789():
    assert (
N("enthousiasme").g('m').n('p').realize()   
    ) == 'enthousiasmes',\
    'N("enthousiasme").g(\'m\').n(\'p\')=>enthousiasmes'


def test_declension_fr_790():
    assert (
A("entier").n('p').realize()   
    ) == 'entiers',\
    'A("entier").n(\'p\')=>entiers'


def test_declension_fr_791():
    assert (
N("entrain").g('m').n('p').realize()   
    ) == 'entrains',\
    'N("entrain").g(\'m\').n(\'p\')=>entrains'


def test_declension_fr_792():
    assert (
N("entrée").g('f').n('p').realize()   
    ) == 'entrées',\
    'N("entrée").g(\'f\').n(\'p\')=>entrées'


def test_declension_fr_793():
    assert (
N("entretien").g('m').n('p').realize()   
    ) == 'entretiens',\
    'N("entretien").g(\'m\').n(\'p\')=>entretiens'


def test_declension_fr_794():
    assert (
N("enveloppe").g('f').n('p').realize()   
    ) == 'enveloppes',\
    'N("enveloppe").g(\'f\').n(\'p\')=>enveloppes'


def test_declension_fr_795():
    assert (
N("envers").g('m').n('p').realize()   
    ) == 'envers',\
    'N("envers").g(\'m\').n(\'p\')=>envers'


def test_declension_fr_796():
    assert (
N("envie").g('f').n('p').realize()   
    ) == 'envies',\
    'N("envie").g(\'f\').n(\'p\')=>envies'


def test_declension_fr_797():
    assert (
N("envoi").g('m').n('p').realize()   
    ) == 'envois',\
    'N("envoi").g(\'m\').n(\'p\')=>envois'


def test_declension_fr_798():
    assert (
A("épais").n('p').realize()   
    ) == 'épais',\
    'A("épais").n(\'p\')=>épais'


def test_declension_fr_799():
    assert (
N("épargne").g('f').n('p').realize()   
    ) == 'épargnes',\
    'N("épargne").g(\'f\').n(\'p\')=>épargnes'


def test_declension_fr_800():
    assert (
N("épaule").g('f').n('p').realize()   
    ) == 'épaules',\
    'N("épaule").g(\'f\').n(\'p\')=>épaules'


def test_declension_fr_801():
    assert (
N("épée").g('f').n('p').realize()   
    ) == 'épées',\
    'N("épée").g(\'f\').n(\'p\')=>épées'


def test_declension_fr_802():
    assert (
N("épi").g('m').n('p').realize()   
    ) == 'épis',\
    'N("épi").g(\'m\').n(\'p\')=>épis'


def test_declension_fr_803():
    assert (
N("épine").g('f').n('p').realize()   
    ) == 'épines',\
    'N("épine").g(\'f\').n(\'p\')=>épines'


def test_declension_fr_804():
    assert (
N("époque").g('f').n('p').realize()   
    ) == 'époques',\
    'N("époque").g(\'f\').n(\'p\')=>époques'


def test_declension_fr_805():
    assert (
A("épouvantable").n('p').realize()   
    ) == 'épouvantables',\
    'A("épouvantable").n(\'p\')=>épouvantables'


def test_declension_fr_806():
    assert (
N("époux").g('m').n('p').realize()   
    ) == 'époux',\
    'N("époux").g(\'m\').n(\'p\')=>époux'


def test_declension_fr_807():
    assert (
N("épreuve").g('f').n('p').realize()   
    ) == 'épreuves',\
    'N("épreuve").g(\'f\').n(\'p\')=>épreuves'


def test_declension_fr_808():
    assert (
N("équilibre").g('m').n('p').realize()   
    ) == 'équilibres',\
    'N("équilibre").g(\'m\').n(\'p\')=>équilibres'


def test_declension_fr_809():
    assert (
N("équipage").g('m').n('p').realize()   
    ) == 'équipages',\
    'N("équipage").g(\'m\').n(\'p\')=>équipages'


def test_declension_fr_810():
    assert (
N("équipe").g('f').n('p').realize()   
    ) == 'équipes',\
    'N("équipe").g(\'f\').n(\'p\')=>équipes'


def test_declension_fr_811():
    assert (
N("erreur").g('f').n('p').realize()   
    ) == 'erreurs',\
    'N("erreur").g(\'f\').n(\'p\')=>erreurs'


def test_declension_fr_812():
    assert (
N("escalier").g('m').n('p').realize()   
    ) == 'escaliers',\
    'N("escalier").g(\'m\').n(\'p\')=>escaliers'


def test_declension_fr_813():
    assert (
N("esclave").n('p').realize()   
    ) == 'esclaves',\
    'N("esclave").n(\'p\')=>esclaves'


def test_declension_fr_814():
    assert (
N("espace").g('m').n('p').realize()   
    ) == 'espaces',\
    'N("espace").g(\'m\').n(\'p\')=>espaces'


def test_declension_fr_815():
    assert (
N("espèce").g('f').n('p').realize()   
    ) == 'espèces',\
    'N("espèce").g(\'f\').n(\'p\')=>espèces'


def test_declension_fr_816():
    assert (
N("espérance").g('f').n('p').realize()   
    ) == 'espérances',\
    'N("espérance").g(\'f\').n(\'p\')=>espérances'


def test_declension_fr_817():
    assert (
A("espiègle").n('p').realize()   
    ) == 'espiègles',\
    'A("espiègle").n(\'p\')=>espiègles'


def test_declension_fr_818():
    assert (
N("espoir").g('m').n('p').realize()   
    ) == 'espoirs',\
    'N("espoir").g(\'m\').n(\'p\')=>espoirs'


def test_declension_fr_819():
    assert (
N("esprit").g('m').n('p').realize()   
    ) == 'esprits',\
    'N("esprit").g(\'m\').n(\'p\')=>esprits'


def test_declension_fr_820():
    assert (
N("essai").g('m').n('p').realize()   
    ) == 'essais',\
    'N("essai").g(\'m\').n(\'p\')=>essais'


def test_declension_fr_821():
    assert (
N("estime").g('f').n('p').realize()   
    ) == 'estimes',\
    'N("estime").g(\'f\').n(\'p\')=>estimes'


def test_declension_fr_822():
    assert (
N("estomac").g('m').n('p').realize()   
    ) == 'estomacs',\
    'N("estomac").g(\'m\').n(\'p\')=>estomacs'


def test_declension_fr_823():
    assert (
N("estrade").g('f').n('p').realize()   
    ) == 'estrades',\
    'N("estrade").g(\'f\').n(\'p\')=>estrades'


def test_declension_fr_824():
    assert (
N("étable").g('f').n('p').realize()   
    ) == 'étables',\
    'N("étable").g(\'f\').n(\'p\')=>étables'


def test_declension_fr_825():
    assert (
N("établissement").g('m').n('p').realize()   
    ) == 'établissements',\
    'N("établissement").g(\'m\').n(\'p\')=>établissements'


def test_declension_fr_826():
    assert (
N("étage").g('m').n('p').realize()   
    ) == 'étages',\
    'N("étage").g(\'m\').n(\'p\')=>étages'


def test_declension_fr_827():
    assert (
N("étagère").g('f').n('p').realize()   
    ) == 'étagères',\
    'N("étagère").g(\'f\').n(\'p\')=>étagères'


def test_declension_fr_828():
    assert (
N("étalage").g('m').n('p').realize()   
    ) == 'étalages',\
    'N("étalage").g(\'m\').n(\'p\')=>étalages'


def test_declension_fr_829():
    assert (
N("étang").g('m').n('p').realize()   
    ) == 'étangs',\
    'N("étang").g(\'m\').n(\'p\')=>étangs'


def test_declension_fr_830():
    assert (
N("état").g('m').n('p').realize()   
    ) == 'états',\
    'N("état").g(\'m\').n(\'p\')=>états'


def test_declension_fr_831():
    assert (
N("été").g('m').n('p').realize()   
    ) == 'étés',\
    'N("été").g(\'m\').n(\'p\')=>étés'


def test_declension_fr_832():
    assert (
N("étendue").g('f').n('p').realize()   
    ) == 'étendues',\
    'N("étendue").g(\'f\').n(\'p\')=>étendues'


def test_declension_fr_833():
    assert (
A("éternel").n('p').realize()   
    ) == 'éternels',\
    'A("éternel").n(\'p\')=>éternels'


def test_declension_fr_834():
    assert (
N("éternité").g('f').n('p').realize()   
    ) == 'éternités',\
    'N("éternité").g(\'f\').n(\'p\')=>éternités'


def test_declension_fr_835():
    assert (
A("étincelant").n('p').realize()   
    ) == 'étincelants',\
    'A("étincelant").n(\'p\')=>étincelants'


def test_declension_fr_836():
    assert (
N("étincelle").g('f').n('p').realize()   
    ) == 'étincelles',\
    'N("étincelle").g(\'f\').n(\'p\')=>étincelles'


def test_declension_fr_837():
    assert (
N("étoffe").g('f').n('p').realize()   
    ) == 'étoffes',\
    'N("étoffe").g(\'f\').n(\'p\')=>étoffes'


def test_declension_fr_838():
    assert (
N("étoile").g('f').n('p').realize()   
    ) == 'étoiles',\
    'N("étoile").g(\'f\').n(\'p\')=>étoiles'


def test_declension_fr_839():
    assert (
N("étonnement").g('m').n('p').realize()   
    ) == 'étonnements',\
    'N("étonnement").g(\'m\').n(\'p\')=>étonnements'


def test_declension_fr_840():
    assert (
A("étourdi").n('p').realize()   
    ) == 'étourdis',\
    'A("étourdi").n(\'p\')=>étourdis'


def test_declension_fr_841():
    assert (
A("étrange").n('p').realize()   
    ) == 'étranges',\
    'A("étrange").n(\'p\')=>étranges'


def test_declension_fr_842():
    assert (
A("étranger").n('p').realize()   
    ) == 'étrangers',\
    'A("étranger").n(\'p\')=>étrangers'


def test_declension_fr_843():
    assert (
N("être").g('m').n('p').realize()   
    ) == 'êtres',\
    'N("être").g(\'m\').n(\'p\')=>êtres'


def test_declension_fr_844():
    assert (
A("étroit").n('p').realize()   
    ) == 'étroits',\
    'A("étroit").n(\'p\')=>étroits'


def test_declension_fr_845():
    assert (
N("étude").g('f').n('p').realize()   
    ) == 'études',\
    'N("étude").g(\'f\').n(\'p\')=>études'


def test_declension_fr_846():
    assert (
N("étudiant").g('m').n('p').realize()   
    ) == 'étudiants',\
    'N("étudiant").g(\'m\').n(\'p\')=>étudiants'


def test_declension_fr_847():
    assert (
N("évangile").g('m').n('p').realize()   
    ) == 'évangiles',\
    'N("évangile").g(\'m\').n(\'p\')=>évangiles'


def test_declension_fr_848():
    assert (
N("événement").g('m').n('p').realize()   
    ) == 'événements',\
    'N("événement").g(\'m\').n(\'p\')=>événements'


def test_declension_fr_849():
    assert (
N("évêque").g('m').n('p').realize()   
    ) == 'évêques',\
    'N("évêque").g(\'m\').n(\'p\')=>évêques'


def test_declension_fr_850():
    assert (
A("exact").n('p').realize()   
    ) == 'exacts',\
    'A("exact").n(\'p\')=>exacts'


def test_declension_fr_851():
    assert (
N("exactitude").g('f').n('p').realize()   
    ) == 'exactitudes',\
    'N("exactitude").g(\'f\').n(\'p\')=>exactitudes'


def test_declension_fr_852():
    assert (
N("examen").g('m').n('p').realize()   
    ) == 'examens',\
    'N("examen").g(\'m\').n(\'p\')=>examens'


def test_declension_fr_853():
    assert (
N("excellence").g('f').n('p').realize()   
    ) == 'excellences',\
    'N("excellence").g(\'f\').n(\'p\')=>excellences'


def test_declension_fr_854():
    assert (
A("excellent").n('p').realize()   
    ) == 'excellents',\
    'A("excellent").n(\'p\')=>excellents'


def test_declension_fr_855():
    assert (
N("exclamation").g('f').n('p').realize()   
    ) == 'exclamations',\
    'N("exclamation").g(\'f\').n(\'p\')=>exclamations'


def test_declension_fr_856():
    assert (
N("excursion").g('f').n('p').realize()   
    ) == 'excursions',\
    'N("excursion").g(\'f\').n(\'p\')=>excursions'


def test_declension_fr_857():
    assert (
N("excuse").g('f').n('p').realize()   
    ) == 'excuses',\
    'N("excuse").g(\'f\').n(\'p\')=>excuses'


def test_declension_fr_858():
    assert (
N("exécution").g('f').n('p').realize()   
    ) == 'exécutions',\
    'N("exécution").g(\'f\').n(\'p\')=>exécutions'


def test_declension_fr_859():
    assert (
N("exemplaire").g('m').n('p').realize()   
    ) == 'exemplaires',\
    'N("exemplaire").g(\'m\').n(\'p\')=>exemplaires'


def test_declension_fr_860():
    assert (
N("exemple").g('m').n('p').realize()   
    ) == 'exemples',\
    'N("exemple").g(\'m\').n(\'p\')=>exemples'


def test_declension_fr_861():
    assert (
N("exercice").g('m').n('p').realize()   
    ) == 'exercices',\
    'N("exercice").g(\'m\').n(\'p\')=>exercices'


def test_declension_fr_862():
    assert (
N("existence").g('f').n('p').realize()   
    ) == 'existences',\
    'N("existence").g(\'f\').n(\'p\')=>existences'


def test_declension_fr_863():
    assert (
N("expédition").g('f').n('p').realize()   
    ) == 'expéditions',\
    'N("expédition").g(\'f\').n(\'p\')=>expéditions'


def test_declension_fr_864():
    assert (
N("expérience").g('f').n('p').realize()   
    ) == 'expériences',\
    'N("expérience").g(\'f\').n(\'p\')=>expériences'


def test_declension_fr_865():
    assert (
N("explication").g('f').n('p').realize()   
    ) == 'explications',\
    'N("explication").g(\'f\').n(\'p\')=>explications'


def test_declension_fr_866():
    assert (
N("exposition").g('f').n('p').realize()   
    ) == 'expositions',\
    'N("exposition").g(\'f\').n(\'p\')=>expositions'


def test_declension_fr_867():
    assert (
N("expression").g('f').n('p').realize()   
    ) == 'expressions',\
    'N("expression").g(\'f\').n(\'p\')=>expressions'


def test_declension_fr_868():
    assert (
A("exquis").n('p').realize()   
    ) == 'exquis',\
    'A("exquis").n(\'p\')=>exquis'


def test_declension_fr_869():
    assert (
A("extérieur").n('p').realize()   
    ) == 'extérieurs',\
    'A("extérieur").n(\'p\')=>extérieurs'


def test_declension_fr_870():
    assert (
A("extraordinaire").n('p').realize()   
    ) == 'extraordinaires',\
    'A("extraordinaire").n(\'p\')=>extraordinaires'


def test_declension_fr_871():
    assert (
A("extrême").n('p').realize()   
    ) == 'extrêmes',\
    'A("extrême").n(\'p\')=>extrêmes'


def test_declension_fr_872():
    assert (
N("extrémité").g('f').n('p').realize()   
    ) == 'extrémités',\
    'N("extrémité").g(\'f\').n(\'p\')=>extrémités'


def test_declension_fr_873():
    assert (
N("fabrication").g('f').n('p').realize()   
    ) == 'fabrications',\
    'N("fabrication").g(\'f\').n(\'p\')=>fabrications'


def test_declension_fr_874():
    assert (
N("fabrique").g('f').n('p').realize()   
    ) == 'fabriques',\
    'N("fabrique").g(\'f\').n(\'p\')=>fabriques'


def test_declension_fr_875():
    assert (
N("façade").g('f').n('p').realize()   
    ) == 'façades',\
    'N("façade").g(\'f\').n(\'p\')=>façades'


def test_declension_fr_876():
    assert (
A("fâcheux").n('p').realize()   
    ) == 'fâcheux',\
    'A("fâcheux").n(\'p\')=>fâcheux'


def test_declension_fr_877():
    assert (
A("facile").n('p').realize()   
    ) == 'faciles',\
    'A("facile").n(\'p\')=>faciles'


def test_declension_fr_878():
    assert (
N("facilité").g('f').n('p').realize()   
    ) == 'facilités',\
    'N("facilité").g(\'f\').n(\'p\')=>facilités'


def test_declension_fr_879():
    assert (
N("façon").g('f').n('p').realize()   
    ) == 'façons',\
    'N("façon").g(\'f\').n(\'p\')=>façons'


def test_declension_fr_880():
    assert (
N("facteur").g('m').n('p').realize()   
    ) == 'facteurs',\
    'N("facteur").g(\'m\').n(\'p\')=>facteurs'


def test_declension_fr_881():
    assert (
A("faible").n('p').realize()   
    ) == 'faibles',\
    'A("faible").n(\'p\')=>faibles'


def test_declension_fr_882():
    assert (
N("faiblesse").g('f').n('p').realize()   
    ) == 'faiblesses',\
    'N("faiblesse").g(\'f\').n(\'p\')=>faiblesses'


def test_declension_fr_883():
    assert (
N("faim").g('f').n('p').realize()   
    ) == 'faims',\
    'N("faim").g(\'f\').n(\'p\')=>faims'


def test_declension_fr_884():
    assert (
N("fait").g('m').n('p').realize()   
    ) == 'faits',\
    'N("fait").g(\'m\').n(\'p\')=>faits'


def test_declension_fr_885():
    assert (
A("fameux").n('p').realize()   
    ) == 'fameux',\
    'A("fameux").n(\'p\')=>fameux'


def test_declension_fr_886():
    assert (
A("familial").n('p').realize()   
    ) == 'familiaux',\
    'A("familial").n(\'p\')=>familiaux'


def test_declension_fr_887():
    assert (
A("familier").n('p').realize()   
    ) == 'familiers',\
    'A("familier").n(\'p\')=>familiers'


def test_declension_fr_888():
    assert (
N("famille").g('f').n('p').realize()   
    ) == 'familles',\
    'N("famille").g(\'f\').n(\'p\')=>familles'


def test_declension_fr_889():
    assert (
N("farce").g('f').n('p').realize()   
    ) == 'farces',\
    'N("farce").g(\'f\').n(\'p\')=>farces'


def test_declension_fr_890():
    assert (
N("farine").g('f').n('p').realize()   
    ) == 'farines',\
    'N("farine").g(\'f\').n(\'p\')=>farines'


def test_declension_fr_891():
    assert (
A("farouche").n('p').realize()   
    ) == 'farouches',\
    'A("farouche").n(\'p\')=>farouches'


def test_declension_fr_892():
    assert (
A("fatal").n('p').realize()   
    ) == 'fatals',\
    'A("fatal").n(\'p\')=>fatals'


def test_declension_fr_893():
    assert (
N("fatigue").g('f').n('p').realize()   
    ) == 'fatigues',\
    'N("fatigue").g(\'f\').n(\'p\')=>fatigues'


def test_declension_fr_894():
    assert (
N("faucheur").g('m').n('p').realize()   
    ) == 'faucheurs',\
    'N("faucheur").g(\'m\').n(\'p\')=>faucheurs'


def test_declension_fr_895():
    assert (
N("faute").g('f').n('p').realize()   
    ) == 'fautes',\
    'N("faute").g(\'f\').n(\'p\')=>fautes'


def test_declension_fr_896():
    assert (
N("fauteuil").g('m').n('p').realize()   
    ) == 'fauteuils',\
    'N("fauteuil").g(\'m\').n(\'p\')=>fauteuils'


def test_declension_fr_897():
    assert (
A("fauve").n('p').realize()   
    ) == 'fauves',\
    'A("fauve").n(\'p\')=>fauves'


def test_declension_fr_898():
    assert (
N("fauvette").g('f').n('p').realize()   
    ) == 'fauvettes',\
    'N("fauvette").g(\'f\').n(\'p\')=>fauvettes'


def test_declension_fr_899():
    assert (
A("faux").n('p').realize()   
    ) == 'faux',\
    'A("faux").n(\'p\')=>faux'


def test_declension_fr_900():
    assert (
N("faveur").g('f').n('p').realize()   
    ) == 'faveurs',\
    'N("faveur").g(\'f\').n(\'p\')=>faveurs'


def test_declension_fr_901():
    assert (
A("favorable").n('p').realize()   
    ) == 'favorables',\
    'A("favorable").n(\'p\')=>favorables'


def test_declension_fr_902():
    assert (
A("favori").n('p').realize()   
    ) == 'favoris',\
    'A("favori").n(\'p\')=>favoris'


def test_declension_fr_903():
    assert (
N("fée").g('f').n('p').realize()   
    ) == 'fées',\
    'N("fée").g(\'f\').n(\'p\')=>fées'


def test_declension_fr_904():
    assert (
N("femelle").g('f').n('p').realize()   
    ) == 'femelles',\
    'N("femelle").g(\'f\').n(\'p\')=>femelles'


def test_declension_fr_905():
    assert (
N("femme").g('f').n('p').realize()   
    ) == 'femmes',\
    'N("femme").g(\'f\').n(\'p\')=>femmes'


def test_declension_fr_906():
    assert (
N("fenêtre").g('f').n('p').realize()   
    ) == 'fenêtres',\
    'N("fenêtre").g(\'f\').n(\'p\')=>fenêtres'


def test_declension_fr_907():
    assert (
N("fer").g('m').n('p').realize()   
    ) == 'fers',\
    'N("fer").g(\'m\').n(\'p\')=>fers'


def test_declension_fr_908():
    assert (
N("ferme").g('f').n('p').realize()   
    ) == 'fermes',\
    'N("ferme").g(\'f\').n(\'p\')=>fermes'


def test_declension_fr_909():
    assert (
N("fermier").g('m').n('p').realize()   
    ) == 'fermiers',\
    'N("fermier").g(\'m\').n(\'p\')=>fermiers'


def test_declension_fr_910():
    assert (
A("féroce").n('p').realize()   
    ) == 'féroces',\
    'A("féroce").n(\'p\')=>féroces'


def test_declension_fr_911():
    assert (
N("ferraille").g('f').n('p').realize()   
    ) == 'ferrailles',\
    'N("ferraille").g(\'f\').n(\'p\')=>ferrailles'


def test_declension_fr_912():
    assert (
A("fervent").n('p').realize()   
    ) == 'fervents',\
    'A("fervent").n(\'p\')=>fervents'


def test_declension_fr_913():
    assert (
N("ferveur").g('f').n('p').realize()   
    ) == 'ferveurs',\
    'N("ferveur").g(\'f\').n(\'p\')=>ferveurs'


def test_declension_fr_914():
    assert (
N("fête").g('f').n('p').realize()   
    ) == 'fêtes',\
    'N("fête").g(\'f\').n(\'p\')=>fêtes'


def test_declension_fr_915():
    assert (
N("feu").g('m').n('p').realize()   
    ) == 'feux',\
    'N("feu").g(\'m\').n(\'p\')=>feux'


def test_declension_fr_916():
    assert (
N("feuillage").g('m').n('p').realize()   
    ) == 'feuillages',\
    'N("feuillage").g(\'m\').n(\'p\')=>feuillages'


def test_declension_fr_917():
    assert (
N("feuille").g('f').n('p').realize()   
    ) == 'feuilles',\
    'N("feuille").g(\'f\').n(\'p\')=>feuilles'


def test_declension_fr_918():
    assert (
N("février").g('m').n('p').realize()   
    ) == 'févriers',\
    'N("février").g(\'m\').n(\'p\')=>févriers'


def test_declension_fr_919():
    assert (
N("ficelle").g('f').n('p').realize()   
    ) == 'ficelles',\
    'N("ficelle").g(\'f\').n(\'p\')=>ficelles'


def test_declension_fr_920():
    assert (
A("fidèle").n('p').realize()   
    ) == 'fidèles',\
    'A("fidèle").n(\'p\')=>fidèles'


def test_declension_fr_921():
    assert (
A("fier").n('p').realize()   
    ) == 'fiers',\
    'A("fier").n(\'p\')=>fiers'


def test_declension_fr_922():
    assert (
N("fièvre").g('f').n('p').realize()   
    ) == 'fièvres',\
    'N("fièvre").g(\'f\').n(\'p\')=>fièvres'


def test_declension_fr_923():
    assert (
N("figure").g('f').n('p').realize()   
    ) == 'figures',\
    'N("figure").g(\'f\').n(\'p\')=>figures'


def test_declension_fr_924():
    assert (
N("fil").g('m').n('p').realize()   
    ) == 'fils',\
    'N("fil").g(\'m\').n(\'p\')=>fils'


def test_declension_fr_925():
    assert (
N("file").g('f').n('p').realize()   
    ) == 'files',\
    'N("file").g(\'f\').n(\'p\')=>files'


def test_declension_fr_926():
    assert (
N("filet").g('m').n('p').realize()   
    ) == 'filets',\
    'N("filet").g(\'m\').n(\'p\')=>filets'


def test_declension_fr_927():
    assert (
N("fille").g('f').n('p').realize()   
    ) == 'filles',\
    'N("fille").g(\'f\').n(\'p\')=>filles'


def test_declension_fr_928():
    assert (
N("fillette").g('f').n('p').realize()   
    ) == 'fillettes',\
    'N("fillette").g(\'f\').n(\'p\')=>fillettes'


def test_declension_fr_929():
    assert (
N("filleul").g('m').n('p').realize()   
    ) == 'filleuls',\
    'N("filleul").g(\'m\').n(\'p\')=>filleuls'


def test_declension_fr_930():
    assert (
N("fils").g('m').n('p').realize()   
    ) == 'fils',\
    'N("fils").g(\'m\').n(\'p\')=>fils'


def test_declension_fr_931():
    assert (
N("fin").g('f').n('p').realize()   
    ) == 'fins',\
    'N("fin").g(\'f\').n(\'p\')=>fins'


def test_declension_fr_932():
    assert (
N("firmament").g('m').n('p').realize()   
    ) == 'firmaments',\
    'N("firmament").g(\'m\').n(\'p\')=>firmaments'


def test_declension_fr_933():
    assert (
A("fixe").n('p').realize()   
    ) == 'fixes',\
    'A("fixe").n(\'p\')=>fixes'


def test_declension_fr_934():
    assert (
N("flacon").g('m').n('p').realize()   
    ) == 'flacons',\
    'N("flacon").g(\'m\').n(\'p\')=>flacons'


def test_declension_fr_935():
    assert (
A("flamand").n('p').realize()   
    ) == 'flamands',\
    'A("flamand").n(\'p\')=>flamands'


def test_declension_fr_936():
    assert (
N("flamme").g('f').n('p').realize()   
    ) == 'flammes',\
    'N("flamme").g(\'f\').n(\'p\')=>flammes'


def test_declension_fr_937():
    assert (
N("flanc").g('m').n('p').realize()   
    ) == 'flancs',\
    'N("flanc").g(\'m\').n(\'p\')=>flancs'


def test_declension_fr_938():
    assert (
N("flaque").g('f').n('p').realize()   
    ) == 'flaques',\
    'N("flaque").g(\'f\').n(\'p\')=>flaques'


def test_declension_fr_939():
    assert (
N("flatteur").g('m').n('p').realize()   
    ) == 'flatteurs',\
    'N("flatteur").g(\'m\').n(\'p\')=>flatteurs'


def test_declension_fr_940():
    assert (
N("fléau").g('m').n('p').realize()   
    ) == 'fléaux',\
    'N("fléau").g(\'m\').n(\'p\')=>fléaux'


def test_declension_fr_941():
    assert (
N("flèche").g('f').n('p').realize()   
    ) == 'flèches',\
    'N("flèche").g(\'f\').n(\'p\')=>flèches'


def test_declension_fr_942():
    assert (
N("fleur").g('f').n('p').realize()   
    ) == 'fleurs',\
    'N("fleur").g(\'f\').n(\'p\')=>fleurs'


def test_declension_fr_943():
    assert (
N("fleurette").g('f').n('p').realize()   
    ) == 'fleurettes',\
    'N("fleurette").g(\'f\').n(\'p\')=>fleurettes'


def test_declension_fr_944():
    assert (
N("fleuve").g('m').n('p').realize()   
    ) == 'fleuves',\
    'N("fleuve").g(\'m\').n(\'p\')=>fleuves'


def test_declension_fr_945():
    assert (
N("flocon").g('m').n('p').realize()   
    ) == 'flocons',\
    'N("flocon").g(\'m\').n(\'p\')=>flocons'


def test_declension_fr_946():
    assert (
N("flot").g('m').n('p').realize()   
    ) == 'flots',\
    'N("flot").g(\'m\').n(\'p\')=>flots'


def test_declension_fr_947():
    assert (
N("flûte").g('f').n('p').realize()   
    ) == 'flûtes',\
    'N("flûte").g(\'f\').n(\'p\')=>flûtes'


def test_declension_fr_948():
    assert (
N("foi").g('f').n('p').realize()   
    ) == 'fois',\
    'N("foi").g(\'f\').n(\'p\')=>fois'


def test_declension_fr_949():
    assert (
N("foie").g('m').n('p').realize()   
    ) == 'foies',\
    'N("foie").g(\'m\').n(\'p\')=>foies'


def test_declension_fr_950():
    assert (
N("foin").g('m').n('p').realize()   
    ) == 'foins',\
    'N("foin").g(\'m\').n(\'p\')=>foins'


def test_declension_fr_951():
    assert (
N("foire").g('f').n('p').realize()   
    ) == 'foires',\
    'N("foire").g(\'f\').n(\'p\')=>foires'


def test_declension_fr_952():
    assert (
N("fois").g('f').n('p').realize()   
    ) == 'fois',\
    'N("fois").g(\'f\').n(\'p\')=>fois'


def test_declension_fr_953():
    assert (
N("fonction").g('f').n('p').realize()   
    ) == 'fonctions',\
    'N("fonction").g(\'f\').n(\'p\')=>fonctions'


def test_declension_fr_954():
    assert (
N("fond").g('m').n('p').realize()   
    ) == 'fonds',\
    'N("fond").g(\'m\').n(\'p\')=>fonds'


def test_declension_fr_955():
    assert (
N("fonds").g('m').n('p').realize()   
    ) == 'fonds',\
    'N("fonds").g(\'m\').n(\'p\')=>fonds'


def test_declension_fr_956():
    assert (
N("fontaine").g('f').n('p').realize()   
    ) == 'fontaines',\
    'N("fontaine").g(\'f\').n(\'p\')=>fontaines'


def test_declension_fr_957():
    assert (
N("force").g('f').n('p').realize()   
    ) == 'forces',\
    'N("force").g(\'f\').n(\'p\')=>forces'


def test_declension_fr_958():
    assert (
A("forestier").n('p').realize()   
    ) == 'forestiers',\
    'A("forestier").n(\'p\')=>forestiers'


def test_declension_fr_959():
    assert (
N("forêt").g('f').n('p').realize()   
    ) == 'forêts',\
    'N("forêt").g(\'f\').n(\'p\')=>forêts'


def test_declension_fr_960():
    assert (
N("forge").g('f').n('p').realize()   
    ) == 'forges',\
    'N("forge").g(\'f\').n(\'p\')=>forges'


def test_declension_fr_961():
    assert (
N("forgeron").g('m').n('p').realize()   
    ) == 'forgerons',\
    'N("forgeron").g(\'m\').n(\'p\')=>forgerons'


def test_declension_fr_962():
    assert (
N("forme").g('f').n('p').realize()   
    ) == 'formes',\
    'N("forme").g(\'f\').n(\'p\')=>formes'


def test_declension_fr_963():
    assert (
A("formidable").n('p').realize()   
    ) == 'formidables',\
    'A("formidable").n(\'p\')=>formidables'


def test_declension_fr_964():
    assert (
A("fort").n('p').realize()   
    ) == 'forts',\
    'A("fort").n(\'p\')=>forts'


def test_declension_fr_965():
    assert (
N("fortune").g('f').n('p').realize()   
    ) == 'fortunes',\
    'N("fortune").g(\'f\').n(\'p\')=>fortunes'


def test_declension_fr_966():
    assert (
N("fossé").g('m').n('p').realize()   
    ) == 'fossés',\
    'N("fossé").g(\'m\').n(\'p\')=>fossés'


def test_declension_fr_967():
    assert (
A("fou").n('p').realize()   
    ) == 'fous',\
    'A("fou").n(\'p\')=>fous'


def test_declension_fr_968():
    assert (
N("foudre").g('f').n('p').realize()   
    ) == 'foudres',\
    'N("foudre").g(\'f\').n(\'p\')=>foudres'


def test_declension_fr_969():
    assert (
N("fouet").g('m').n('p').realize()   
    ) == 'fouets',\
    'N("fouet").g(\'m\').n(\'p\')=>fouets'


def test_declension_fr_970():
    assert (
N("fougère").g('f').n('p').realize()   
    ) == 'fougères',\
    'N("fougère").g(\'f\').n(\'p\')=>fougères'


def test_declension_fr_971():
    assert (
N("foule").g('f').n('p').realize()   
    ) == 'foules',\
    'N("foule").g(\'f\').n(\'p\')=>foules'


def test_declension_fr_972():
    assert (
N("four").g('m').n('p').realize()   
    ) == 'fours',\
    'N("four").g(\'m\').n(\'p\')=>fours'


def test_declension_fr_973():
    assert (
N("fourmi").g('f').n('p').realize()   
    ) == 'fourmis',\
    'N("fourmi").g(\'f\').n(\'p\')=>fourmis'


def test_declension_fr_974():
    assert (
N("fourneau").g('m').n('p').realize()   
    ) == 'fourneaux',\
    'N("fourneau").g(\'m\').n(\'p\')=>fourneaux'


def test_declension_fr_975():
    assert (
N("fourniture").g('f').n('p').realize()   
    ) == 'fournitures',\
    'N("fourniture").g(\'f\').n(\'p\')=>fournitures'


def test_declension_fr_976():
    assert (
N("fourrure").g('f').n('p').realize()   
    ) == 'fourrures',\
    'N("fourrure").g(\'f\').n(\'p\')=>fourrures'


def test_declension_fr_977():
    assert (
N("foyer").g('m').n('p').realize()   
    ) == 'foyers',\
    'N("foyer").g(\'m\').n(\'p\')=>foyers'


def test_declension_fr_978():
    assert (
A("fragile").n('p').realize()   
    ) == 'fragiles',\
    'A("fragile").n(\'p\')=>fragiles'


def test_declension_fr_979():
    assert (
N("fraîcheur").g('f').n('p').realize()   
    ) == 'fraîcheurs',\
    'N("fraîcheur").g(\'f\').n(\'p\')=>fraîcheurs'


def test_declension_fr_980():
    assert (
A("frais").n('p').realize()   
    ) == 'frais',\
    'A("frais").n(\'p\')=>frais'


def test_declension_fr_981():
    assert (
N("fraise").g('f').n('p').realize()   
    ) == 'fraises',\
    'N("fraise").g(\'f\').n(\'p\')=>fraises'


def test_declension_fr_982():
    assert (
A("franc").n('p').realize()   
    ) == 'francs',\
    'A("franc").n(\'p\')=>francs'


def test_declension_fr_983():
    assert (
A("français").n('p').realize()   
    ) == 'français',\
    'A("français").n(\'p\')=>français'


def test_declension_fr_984():
    assert (
N("franchise").g('f').n('p').realize()   
    ) == 'franchises',\
    'N("franchise").g(\'f\').n(\'p\')=>franchises'


def test_declension_fr_985():
    assert (
N("frayeur").g('f').n('p').realize()   
    ) == 'frayeurs',\
    'N("frayeur").g(\'f\').n(\'p\')=>frayeurs'


def test_declension_fr_986():
    assert (
A("frêle").n('p').realize()   
    ) == 'frêles',\
    'A("frêle").n(\'p\')=>frêles'


def test_declension_fr_987():
    assert (
A("fréquent").n('p').realize()   
    ) == 'fréquents',\
    'A("fréquent").n(\'p\')=>fréquents'


def test_declension_fr_988():
    assert (
N("frère").g('m').n('p').realize()   
    ) == 'frères',\
    'N("frère").g(\'m\').n(\'p\')=>frères'


def test_declension_fr_989():
    assert (
N("friandise").g('f').n('p').realize()   
    ) == 'friandises',\
    'N("friandise").g(\'f\').n(\'p\')=>friandises'


def test_declension_fr_990():
    assert (
A("froid").n('p').realize()   
    ) == 'froids',\
    'A("froid").n(\'p\')=>froids'


def test_declension_fr_991():
    assert (
N("fromage").g('m').n('p').realize()   
    ) == 'fromages',\
    'N("fromage").g(\'m\').n(\'p\')=>fromages'


def test_declension_fr_992():
    assert (
N("froment").g('m').n('p').realize()   
    ) == 'froments',\
    'N("froment").g(\'m\').n(\'p\')=>froments'


def test_declension_fr_993():
    assert (
N("front").g('m').n('p').realize()   
    ) == 'fronts',\
    'N("front").g(\'m\').n(\'p\')=>fronts'


def test_declension_fr_994():
    assert (
N("frontière").g('f').n('p').realize()   
    ) == 'frontières',\
    'N("frontière").g(\'f\').n(\'p\')=>frontières'


def test_declension_fr_995():
    assert (
N("fruit").g('m').n('p').realize()   
    ) == 'fruits',\
    'N("fruit").g(\'m\').n(\'p\')=>fruits'


def test_declension_fr_996():
    assert (
A("fruitier").n('p').realize()   
    ) == 'fruitiers',\
    'A("fruitier").n(\'p\')=>fruitiers'


def test_declension_fr_997():
    assert (
N("fuite").g('f').n('p').realize()   
    ) == 'fuites',\
    'N("fuite").g(\'f\').n(\'p\')=>fuites'


def test_declension_fr_998():
    assert (
N("fumée").g('f').n('p').realize()   
    ) == 'fumées',\
    'N("fumée").g(\'f\').n(\'p\')=>fumées'


def test_declension_fr_999():
    assert (
N("fureur").g('f').n('p').realize()   
    ) == 'fureurs',\
    'N("fureur").g(\'f\').n(\'p\')=>fureurs'


def test_declension_fr_1000():
    assert (
A("furieux").n('p').realize()   
    ) == 'furieux',\
    'A("furieux").n(\'p\')=>furieux'


def test_declension_fr_1001():
    assert (
N("fusil").g('m').n('p').realize()   
    ) == 'fusils',\
    'N("fusil").g(\'m\').n(\'p\')=>fusils'


def test_declension_fr_1002():
    assert (
A("futur").n('p').realize()   
    ) == 'futurs',\
    'A("futur").n(\'p\')=>futurs'


def test_declension_fr_1003():
    assert (
A("gai").n('p').realize()   
    ) == 'gais',\
    'A("gai").n(\'p\')=>gais'


def test_declension_fr_1004():
    assert (
N("gaieté").g('f').n('p').realize()   
    ) == 'gaietés',\
    'N("gaieté").g(\'f\').n(\'p\')=>gaietés'


def test_declension_fr_1005():
    assert (
N("galerie").g('f').n('p').realize()   
    ) == 'galeries',\
    'N("galerie").g(\'f\').n(\'p\')=>galeries'


def test_declension_fr_1006():
    assert (
N("gamin").g('m').n('p').realize()   
    ) == 'gamins',\
    'N("gamin").g(\'m\').n(\'p\')=>gamins'


def test_declension_fr_1007():
    assert (
N("gant").g('m').n('p').realize()   
    ) == 'gants',\
    'N("gant").g(\'m\').n(\'p\')=>gants'


def test_declension_fr_1008():
    assert (
N("garçon").g('m').n('p').realize()   
    ) == 'garçons',\
    'N("garçon").g(\'m\').n(\'p\')=>garçons'


def test_declension_fr_1009():
    assert (
N("garde").g('m').n('p').realize()   
    ) == 'gardes',\
    'N("garde").g(\'m\').n(\'p\')=>gardes'


def test_declension_fr_1010():
    assert (
N("gardien").g('m').n('p').realize()   
    ) == 'gardiens',\
    'N("gardien").g(\'m\').n(\'p\')=>gardiens'


def test_declension_fr_1011():
    assert (
N("gare").g('f').n('p').realize()   
    ) == 'gares',\
    'N("gare").g(\'f\').n(\'p\')=>gares'


def test_declension_fr_1012():
    assert (
N("garniture").g('f').n('p').realize()   
    ) == 'garnitures',\
    'N("garniture").g(\'f\').n(\'p\')=>garnitures'


def test_declension_fr_1013():
    assert (
N("gâteau").g('m').n('p').realize()   
    ) == 'gâteaux',\
    'N("gâteau").g(\'m\').n(\'p\')=>gâteaux'


def test_declension_fr_1014():
    assert (
A("gauche").n('p').realize()   
    ) == 'gauches',\
    'A("gauche").n(\'p\')=>gauches'


def test_declension_fr_1015():
    assert (
N("gaufre").g('f').n('p').realize()   
    ) == 'gaufres',\
    'N("gaufre").g(\'f\').n(\'p\')=>gaufres'


def test_declension_fr_1016():
    assert (
N("gaz").g('m').n('p').realize()   
    ) == 'gaz',\
    'N("gaz").g(\'m\').n(\'p\')=>gaz'


def test_declension_fr_1017():
    assert (
N("gazon").g('m').n('p').realize()   
    ) == 'gazons',\
    'N("gazon").g(\'m\').n(\'p\')=>gazons'


def test_declension_fr_1018():
    assert (
N("gazouillement").g('m').n('p').realize()   
    ) == 'gazouillements',\
    'N("gazouillement").g(\'m\').n(\'p\')=>gazouillements'


def test_declension_fr_1019():
    assert (
A("géant").n('p').realize()   
    ) == 'géants',\
    'A("géant").n(\'p\')=>géants'


def test_declension_fr_1020():
    assert (
N("gelée").g('f').n('p').realize()   
    ) == 'gelées',\
    'N("gelée").g(\'f\').n(\'p\')=>gelées'


def test_declension_fr_1021():
    assert (
N("gendarme").g('m').n('p').realize()   
    ) == 'gendarmes',\
    'N("gendarme").g(\'m\').n(\'p\')=>gendarmes'


def test_declension_fr_1022():
    assert (
A("général").n('p').realize()   
    ) == 'généraux',\
    'A("général").n(\'p\')=>généraux'


def test_declension_fr_1023():
    assert (
A("généreux").n('p').realize()   
    ) == 'généreux',\
    'A("généreux").n(\'p\')=>généreux'


def test_declension_fr_1024():
    assert (
N("générosité").g('f').n('p').realize()   
    ) == 'générosités',\
    'N("générosité").g(\'f\').n(\'p\')=>générosités'


def test_declension_fr_1025():
    assert (
N("genêt").g('m').n('p').realize()   
    ) == 'genêts',\
    'N("genêt").g(\'m\').n(\'p\')=>genêts'


def test_declension_fr_1026():
    assert (
N("genou").g('m').n('p').realize()   
    ) == 'genoux',\
    'N("genou").g(\'m\').n(\'p\')=>genoux'


def test_declension_fr_1027():
    assert (
N("genre").g('m').n('p').realize()   
    ) == 'genres',\
    'N("genre").g(\'m\').n(\'p\')=>genres'


def test_declension_fr_1028():
    assert (
N("gens").g('m').n('p').realize()   
    ) == 'gens',\
    'N("gens").g(\'m\').n(\'p\')=>gens'


def test_declension_fr_1029():
    assert (
A("gentil").n('p').realize()   
    ) == 'gentils',\
    'A("gentil").n(\'p\')=>gentils'


def test_declension_fr_1030():
    assert (
N("géographie").g('f').n('p').realize()   
    ) == 'géographies',\
    'N("géographie").g(\'f\').n(\'p\')=>géographies'


def test_declension_fr_1031():
    assert (
N("géranium").g('m').n('p').realize()   
    ) == 'géraniums',\
    'N("géranium").g(\'m\').n(\'p\')=>géraniums'


def test_declension_fr_1032():
    assert (
N("gerbe").g('f').n('p').realize()   
    ) == 'gerbes',\
    'N("gerbe").g(\'f\').n(\'p\')=>gerbes'


def test_declension_fr_1033():
    assert (
N("geste").g('m').n('p').realize()   
    ) == 'gestes',\
    'N("geste").g(\'m\').n(\'p\')=>gestes'


def test_declension_fr_1034():
    assert (
N("gibecière").g('f').n('p').realize()   
    ) == 'gibecières',\
    'N("gibecière").g(\'f\').n(\'p\')=>gibecières'


def test_declension_fr_1035():
    assert (
N("gibier").g('m').n('p').realize()   
    ) == 'gibiers',\
    'N("gibier").g(\'m\').n(\'p\')=>gibiers'


def test_declension_fr_1036():
    assert (
N("giboulée").g('f').n('p').realize()   
    ) == 'giboulées',\
    'N("giboulée").g(\'f\').n(\'p\')=>giboulées'


def test_declension_fr_1037():
    assert (
A("gigantesque").n('p').realize()   
    ) == 'gigantesques',\
    'A("gigantesque").n(\'p\')=>gigantesques'


def test_declension_fr_1038():
    assert (
N("giroflée").g('f').n('p').realize()   
    ) == 'giroflées',\
    'N("giroflée").g(\'f\').n(\'p\')=>giroflées'


def test_declension_fr_1039():
    assert (
N("gîte").g('m').n('p').realize()   
    ) == 'gîtes',\
    'N("gîte").g(\'m\').n(\'p\')=>gîtes'


def test_declension_fr_1040():
    assert (
N("givre").g('m').n('p').realize()   
    ) == 'givres',\
    'N("givre").g(\'m\').n(\'p\')=>givres'


def test_declension_fr_1041():
    assert (
N("glace").g('f').n('p').realize()   
    ) == 'glaces',\
    'N("glace").g(\'f\').n(\'p\')=>glaces'


def test_declension_fr_1042():
    assert (
N("gland").g('m').n('p').realize()   
    ) == 'glands',\
    'N("gland").g(\'m\').n(\'p\')=>glands'


def test_declension_fr_1043():
    assert (
A("glissant").n('p').realize()   
    ) == 'glissants',\
    'A("glissant").n(\'p\')=>glissants'


def test_declension_fr_1044():
    assert (
N("glissoire").g('f').n('p').realize()   
    ) == 'glissoires',\
    'N("glissoire").g(\'f\').n(\'p\')=>glissoires'


def test_declension_fr_1045():
    assert (
N("gloire").g('f').n('p').realize()   
    ) == 'gloires',\
    'N("gloire").g(\'f\').n(\'p\')=>gloires'


def test_declension_fr_1046():
    assert (
N("gorge").g('f').n('p').realize()   
    ) == 'gorges',\
    'N("gorge").g(\'f\').n(\'p\')=>gorges'


def test_declension_fr_1047():
    assert (
N("gosse").n('p').realize()   
    ) == 'gosses',\
    'N("gosse").n(\'p\')=>gosses'


def test_declension_fr_1048():
    assert (
A("gourmand").n('p').realize()   
    ) == 'gourmands',\
    'A("gourmand").n(\'p\')=>gourmands'


def test_declension_fr_1049():
    assert (
N("goût").g('m').n('p').realize()   
    ) == 'goûts',\
    'N("goût").g(\'m\').n(\'p\')=>goûts'


def test_declension_fr_1050():
    assert (
N("goutte").g('f').n('p').realize()   
    ) == 'gouttes',\
    'N("goutte").g(\'f\').n(\'p\')=>gouttes'


def test_declension_fr_1051():
    assert (
N("gouvernement").g('m').n('p').realize()   
    ) == 'gouvernements',\
    'N("gouvernement").g(\'m\').n(\'p\')=>gouvernements'


def test_declension_fr_1052():
    assert (
N("grâce").g('f').n('p').realize()   
    ) == 'grâces',\
    'N("grâce").g(\'f\').n(\'p\')=>grâces'


def test_declension_fr_1053():
    assert (
A("gracieux").n('p').realize()   
    ) == 'gracieux',\
    'A("gracieux").n(\'p\')=>gracieux'


def test_declension_fr_1054():
    assert (
N("grain").g('m').n('p').realize()   
    ) == 'grains',\
    'N("grain").g(\'m\').n(\'p\')=>grains'


def test_declension_fr_1055():
    assert (
N("graine").g('f').n('p').realize()   
    ) == 'graines',\
    'N("graine").g(\'f\').n(\'p\')=>graines'


def test_declension_fr_1056():
    assert (
N("graisse").g('f').n('p').realize()   
    ) == 'graisses',\
    'N("graisse").g(\'f\').n(\'p\')=>graisses'


def test_declension_fr_1057():
    assert (
N("grammaire").g('f').n('p').realize()   
    ) == 'grammaires',\
    'N("grammaire").g(\'f\').n(\'p\')=>grammaires'


def test_declension_fr_1058():
    assert (
A("grand").n('p').realize()   
    ) == 'grands',\
    'A("grand").n(\'p\')=>grands'


def test_declension_fr_1059():
    assert (
N("grandeur").g('f').n('p').realize()   
    ) == 'grandeurs',\
    'N("grandeur").g(\'f\').n(\'p\')=>grandeurs'


def test_declension_fr_1060():
    assert (
A("grandiose").n('p').realize()   
    ) == 'grandioses',\
    'A("grandiose").n(\'p\')=>grandioses'


def test_declension_fr_1061():
    assert (
N("grange").g('f').n('p').realize()   
    ) == 'granges',\
    'N("grange").g(\'f\').n(\'p\')=>granges'


def test_declension_fr_1062():
    assert (
N("grappe").g('f').n('p').realize()   
    ) == 'grappes',\
    'N("grappe").g(\'f\').n(\'p\')=>grappes'


def test_declension_fr_1063():
    assert (
A("gras").n('p').realize()   
    ) == 'gras',\
    'A("gras").n(\'p\')=>gras'


def test_declension_fr_1064():
    assert (
N("gratitude").g('f').n('p').realize()   
    ) == 'gratitudes',\
    'N("gratitude").g(\'f\').n(\'p\')=>gratitudes'


def test_declension_fr_1065():
    assert (
A("grave").n('p').realize()   
    ) == 'graves',\
    'A("grave").n(\'p\')=>graves'


def test_declension_fr_1066():
    assert (
N("gravure").g('f').n('p').realize()   
    ) == 'gravures',\
    'N("gravure").g(\'f\').n(\'p\')=>gravures'


def test_declension_fr_1067():
    assert (
N("grêle").g('f').n('p').realize()   
    ) == 'grêles',\
    'N("grêle").g(\'f\').n(\'p\')=>grêles'


def test_declension_fr_1068():
    assert (
N("grenier").g('m').n('p').realize()   
    ) == 'greniers',\
    'N("grenier").g(\'m\').n(\'p\')=>greniers'


def test_declension_fr_1069():
    assert (
N("grenouille").g('f').n('p').realize()   
    ) == 'grenouilles',\
    'N("grenouille").g(\'f\').n(\'p\')=>grenouilles'


def test_declension_fr_1070():
    assert (
N("grès").g('m').n('p').realize()   
    ) == 'grès',\
    'N("grès").g(\'m\').n(\'p\')=>grès'


def test_declension_fr_1071():
    assert (
N("griffe").g('f').n('p').realize()   
    ) == 'griffes',\
    'N("griffe").g(\'f\').n(\'p\')=>griffes'


def test_declension_fr_1072():
    assert (
N("grille").g('f').n('p').realize()   
    ) == 'grilles',\
    'N("grille").g(\'f\').n(\'p\')=>grilles'


def test_declension_fr_1073():
    assert (
N("grippe").g('f').n('p').realize()   
    ) == 'grippes',\
    'N("grippe").g(\'f\').n(\'p\')=>grippes'


def test_declension_fr_1074():
    assert (
A("gris").n('p').realize()   
    ) == 'gris',\
    'A("gris").n(\'p\')=>gris'


def test_declension_fr_1075():
    assert (
N("grive").g('f').n('p').realize()   
    ) == 'grives',\
    'N("grive").g(\'f\').n(\'p\')=>grives'


def test_declension_fr_1076():
    assert (
A("gros").n('p').realize()   
    ) == 'gros',\
    'A("gros").n(\'p\')=>gros'


def test_declension_fr_1077():
    assert (
N("groseillier").g('m').n('p').realize()   
    ) == 'groseilliers',\
    'N("groseillier").g(\'m\').n(\'p\')=>groseilliers'


def test_declension_fr_1078():
    assert (
A("grossier").n('p').realize()   
    ) == 'grossiers',\
    'A("grossier").n(\'p\')=>grossiers'


def test_declension_fr_1079():
    assert (
N("grotte").g('f').n('p').realize()   
    ) == 'grottes',\
    'N("grotte").g(\'f\').n(\'p\')=>grottes'


def test_declension_fr_1080():
    assert (
N("groupe").g('m').n('p').realize()   
    ) == 'groupes',\
    'N("groupe").g(\'m\').n(\'p\')=>groupes'


def test_declension_fr_1081():
    assert (
N("grue").g('f').n('p').realize()   
    ) == 'grues',\
    'N("grue").g(\'f\').n(\'p\')=>grues'


def test_declension_fr_1082():
    assert (
N("guêpe").g('f').n('p').realize()   
    ) == 'guêpes',\
    'N("guêpe").g(\'f\').n(\'p\')=>guêpes'


def test_declension_fr_1083():
    assert (
N("guérison").g('f').n('p').realize()   
    ) == 'guérisons',\
    'N("guérison").g(\'f\').n(\'p\')=>guérisons'


def test_declension_fr_1084():
    assert (
N("guerre").g('f').n('p').realize()   
    ) == 'guerres',\
    'N("guerre").g(\'f\').n(\'p\')=>guerres'


def test_declension_fr_1085():
    assert (
N("guichet").g('m').n('p').realize()   
    ) == 'guichets',\
    'N("guichet").g(\'m\').n(\'p\')=>guichets'


def test_declension_fr_1086():
    assert (
N("guide").n('p').realize()   
    ) == 'guides',\
    'N("guide").n(\'p\')=>guides'


def test_declension_fr_1087():
    assert (
N("gymnastique").g('f').n('p').realize()   
    ) == 'gymnastiques',\
    'N("gymnastique").g(\'f\').n(\'p\')=>gymnastiques'


def test_declension_fr_1088():
    assert (
A("habile").n('p').realize()   
    ) == 'habiles',\
    'A("habile").n(\'p\')=>habiles'


def test_declension_fr_1089():
    assert (
N("habileté").g('f').n('p').realize()   
    ) == 'habiletés',\
    'N("habileté").g(\'f\').n(\'p\')=>habiletés'


def test_declension_fr_1090():
    assert (
N("habit").g('m').n('p').realize()   
    ) == 'habits',\
    'N("habit").g(\'m\').n(\'p\')=>habits'


def test_declension_fr_1091():
    assert (
N("habitant").g('m').n('p').realize()   
    ) == 'habitants',\
    'N("habitant").g(\'m\').n(\'p\')=>habitants'


def test_declension_fr_1092():
    assert (
N("habitation").g('f').n('p').realize()   
    ) == 'habitations',\
    'N("habitation").g(\'f\').n(\'p\')=>habitations'


def test_declension_fr_1093():
    assert (
N("habitude").g('f').n('p').realize()   
    ) == 'habitudes',\
    'N("habitude").g(\'f\').n(\'p\')=>habitudes'


def test_declension_fr_1094():
    assert (
A("habituel").n('p').realize()   
    ) == 'habituels',\
    'A("habituel").n(\'p\')=>habituels'


def test_declension_fr_1095():
    assert (
N("hache").g('f').n('p').realize()   
    ) == 'haches',\
    'N("hache").g(\'f\').n(\'p\')=>haches'


def test_declension_fr_1096():
    assert (
N("haie").g('f').n('p').realize()   
    ) == 'haies',\
    'N("haie").g(\'f\').n(\'p\')=>haies'


def test_declension_fr_1097():
    assert (
N("haillon").g('m').n('p').realize()   
    ) == 'haillons',\
    'N("haillon").g(\'m\').n(\'p\')=>haillons'


def test_declension_fr_1098():
    assert (
N("haine").g('f').n('p').realize()   
    ) == 'haines',\
    'N("haine").g(\'f\').n(\'p\')=>haines'


def test_declension_fr_1099():
    assert (
N("haleine").g('f').n('p').realize()   
    ) == 'haleines',\
    'N("haleine").g(\'f\').n(\'p\')=>haleines'


def test_declension_fr_1100():
    assert (
N("halte").g('f').n('p').realize()   
    ) == 'haltes',\
    'N("halte").g(\'f\').n(\'p\')=>haltes'


def test_declension_fr_1101():
    assert (
N("hameau").g('m').n('p').realize()   
    ) == 'hameaux',\
    'N("hameau").g(\'m\').n(\'p\')=>hameaux'


def test_declension_fr_1102():
    assert (
N("hangar").g('m').n('p').realize()   
    ) == 'hangars',\
    'N("hangar").g(\'m\').n(\'p\')=>hangars'


def test_declension_fr_1103():
    assert (
N("hanneton").g('m').n('p').realize()   
    ) == 'hannetons',\
    'N("hanneton").g(\'m\').n(\'p\')=>hannetons'


def test_declension_fr_1104():
    assert (
A("hardi").n('p').realize()   
    ) == 'hardis',\
    'A("hardi").n(\'p\')=>hardis'


def test_declension_fr_1105():
    assert (
A("harmonieux").n('p').realize()   
    ) == 'harmonieux',\
    'A("harmonieux").n(\'p\')=>harmonieux'


def test_declension_fr_1106():
    assert (
N("hasard").g('m').n('p').realize()   
    ) == 'hasards',\
    'N("hasard").g(\'m\').n(\'p\')=>hasards'


def test_declension_fr_1107():
    assert (
N("hâte").g('f').n('p').realize()   
    ) == 'hâtes',\
    'N("hâte").g(\'f\').n(\'p\')=>hâtes'


def test_declension_fr_1108():
    assert (
A("haut").n('p').realize()   
    ) == 'hauts',\
    'A("haut").n(\'p\')=>hauts'


def test_declension_fr_1109():
    assert (
N("hauteur").g('f').n('p').realize()   
    ) == 'hauteurs',\
    'N("hauteur").g(\'f\').n(\'p\')=>hauteurs'


def test_declension_fr_1110():
    assert (
N("herbe").g('f').n('p').realize()   
    ) == 'herbes',\
    'N("herbe").g(\'f\').n(\'p\')=>herbes'


def test_declension_fr_1111():
    assert (
A("hérissé").n('p').realize()   
    ) == 'hérissés',\
    'A("hérissé").n(\'p\')=>hérissés'


def test_declension_fr_1112():
    assert (
N("hermine").g('f').n('p').realize()   
    ) == 'hermines',\
    'N("hermine").g(\'f\').n(\'p\')=>hermines'


def test_declension_fr_1113():
    assert (
A("héroïque").n('p').realize()   
    ) == 'héroïques',\
    'A("héroïque").n(\'p\')=>héroïques'


def test_declension_fr_1114():
    assert (
N("héros").g('m').n('p').realize()   
    ) == 'héros',\
    'N("héros").g(\'m\').n(\'p\')=>héros'


def test_declension_fr_1115():
    assert (
N("hêtre").g('m').n('p').realize()   
    ) == 'hêtres',\
    'N("hêtre").g(\'m\').n(\'p\')=>hêtres'


def test_declension_fr_1116():
    assert (
N("heure").g('f').n('p').realize()   
    ) == 'heures',\
    'N("heure").g(\'f\').n(\'p\')=>heures'


def test_declension_fr_1117():
    assert (
A("heureux").n('p').realize()   
    ) == 'heureux',\
    'A("heureux").n(\'p\')=>heureux'


def test_declension_fr_1118():
    assert (
N("hirondelle").g('f').n('p').realize()   
    ) == 'hirondelles',\
    'N("hirondelle").g(\'f\').n(\'p\')=>hirondelles'


def test_declension_fr_1119():
    assert (
N("histoire").g('f').n('p').realize()   
    ) == 'histoires',\
    'N("histoire").g(\'f\').n(\'p\')=>histoires'


def test_declension_fr_1120():
    assert (
N("hiver").g('m').n('p').realize()   
    ) == 'hivers',\
    'N("hiver").g(\'m\').n(\'p\')=>hivers'


def test_declension_fr_1121():
    assert (
N("hommage").g('m').n('p').realize()   
    ) == 'hommages',\
    'N("hommage").g(\'m\').n(\'p\')=>hommages'


def test_declension_fr_1122():
    assert (
N("homme").g('m').n('p').realize()   
    ) == 'hommes',\
    'N("homme").g(\'m\').n(\'p\')=>hommes'


def test_declension_fr_1123():
    assert (
A("honnête").n('p').realize()   
    ) == 'honnêtes',\
    'A("honnête").n(\'p\')=>honnêtes'


def test_declension_fr_1124():
    assert (
N("honneur").g('m').n('p').realize()   
    ) == 'honneurs',\
    'N("honneur").g(\'m\').n(\'p\')=>honneurs'


def test_declension_fr_1125():
    assert (
A("honorable").n('p').realize()   
    ) == 'honorables',\
    'A("honorable").n(\'p\')=>honorables'


def test_declension_fr_1126():
    assert (
N("honte").g('f').n('p').realize()   
    ) == 'hontes',\
    'N("honte").g(\'f\').n(\'p\')=>hontes'


def test_declension_fr_1127():
    assert (
A("honteux").n('p').realize()   
    ) == 'honteux',\
    'A("honteux").n(\'p\')=>honteux'


def test_declension_fr_1128():
    assert (
N("hôpital").g('m').n('p').realize()   
    ) == 'hôpitaux',\
    'N("hôpital").g(\'m\').n(\'p\')=>hôpitaux'


def test_declension_fr_1129():
    assert (
N("horizon").g('m').n('p').realize()   
    ) == 'horizons',\
    'N("horizon").g(\'m\').n(\'p\')=>horizons'


def test_declension_fr_1130():
    assert (
N("horloge").g('f').n('p').realize()   
    ) == 'horloges',\
    'N("horloge").g(\'f\').n(\'p\')=>horloges'


def test_declension_fr_1131():
    assert (
N("horreur").g('f').n('p').realize()   
    ) == 'horreurs',\
    'N("horreur").g(\'f\').n(\'p\')=>horreurs'


def test_declension_fr_1132():
    assert (
A("horrible").n('p').realize()   
    ) == 'horribles',\
    'A("horrible").n(\'p\')=>horribles'


def test_declension_fr_1133():
    assert (
N("hôte").g('m').n('p').realize()   
    ) == 'hôtes',\
    'N("hôte").g(\'m\').n(\'p\')=>hôtes'


def test_declension_fr_1134():
    assert (
N("hôtel").g('m').n('p').realize()   
    ) == 'hôtels',\
    'N("hôtel").g(\'m\').n(\'p\')=>hôtels'


def test_declension_fr_1135():
    assert (
N("houille").g('f').n('p').realize()   
    ) == 'houilles',\
    'N("houille").g(\'f\').n(\'p\')=>houilles'


def test_declension_fr_1136():
    assert (
N("huile").g('f').n('p').realize()   
    ) == 'huiles',\
    'N("huile").g(\'f\').n(\'p\')=>huiles'


def test_declension_fr_1137():
    assert (
A("humain").n('p').realize()   
    ) == 'humains',\
    'A("humain").n(\'p\')=>humains'


def test_declension_fr_1138():
    assert (
N("humanité").g('f').n('p').realize()   
    ) == 'humanités',\
    'N("humanité").g(\'f\').n(\'p\')=>humanités'


def test_declension_fr_1139():
    assert (
A("humble").n('p').realize()   
    ) == 'humbles',\
    'A("humble").n(\'p\')=>humbles'


def test_declension_fr_1140():
    assert (
N("humeur").g('f').n('p').realize()   
    ) == 'humeurs',\
    'N("humeur").g(\'f\').n(\'p\')=>humeurs'


def test_declension_fr_1141():
    assert (
A("humide").n('p').realize()   
    ) == 'humides',\
    'A("humide").n(\'p\')=>humides'


def test_declension_fr_1142():
    assert (
N("humidité").g('f').n('p').realize()   
    ) == 'humidités',\
    'N("humidité").g(\'f\').n(\'p\')=>humidités'


def test_declension_fr_1143():
    assert (
N("hygiène").g('f').n('p').realize()   
    ) == 'hygiènes',\
    'N("hygiène").g(\'f\').n(\'p\')=>hygiènes'


def test_declension_fr_1144():
    assert (
A("hypocrite").n('p').realize()   
    ) == 'hypocrites',\
    'A("hypocrite").n(\'p\')=>hypocrites'


def test_declension_fr_1145():
    assert (
A("idéal").n('p').realize()   
    ) == 'idéaux',\
    'A("idéal").n(\'p\')=>idéaux'


def test_declension_fr_1146():
    assert (
N("idée").g('f').n('p').realize()   
    ) == 'idées',\
    'N("idée").g(\'f\').n(\'p\')=>idées'


def test_declension_fr_1147():
    assert (
A("ignorant").n('p').realize()   
    ) == 'ignorants',\
    'A("ignorant").n(\'p\')=>ignorants'


def test_declension_fr_1148():
    assert (
N("île").g('f').n('p').realize()   
    ) == 'îles',\
    'N("île").g(\'f\').n(\'p\')=>îles'


def test_declension_fr_1149():
    assert (
N("illusion").g('f').n('p').realize()   
    ) == 'illusions',\
    'N("illusion").g(\'f\').n(\'p\')=>illusions'


def test_declension_fr_1150():
    assert (
A("illustre").n('p').realize()   
    ) == 'illustres',\
    'A("illustre").n(\'p\')=>illustres'


def test_declension_fr_1151():
    assert (
N("image").g('f').n('p').realize()   
    ) == 'images',\
    'N("image").g(\'f\').n(\'p\')=>images'


def test_declension_fr_1152():
    assert (
N("imagination").g('f').n('p').realize()   
    ) == 'imaginations',\
    'N("imagination").g(\'f\').n(\'p\')=>imaginations'


def test_declension_fr_1153():
    assert (
A("immaculé").n('p').realize()   
    ) == 'immaculés',\
    'A("immaculé").n(\'p\')=>immaculés'


def test_declension_fr_1154():
    assert (
A("immense").n('p').realize()   
    ) == 'immenses',\
    'A("immense").n(\'p\')=>immenses'


def test_declension_fr_1155():
    assert (
A("immobile").n('p').realize()   
    ) == 'immobiles',\
    'A("immobile").n(\'p\')=>immobiles'


def test_declension_fr_1156():
    assert (
N("impatience").g('f').n('p').realize()   
    ) == 'impatiences',\
    'N("impatience").g(\'f\').n(\'p\')=>impatiences'


def test_declension_fr_1157():
    assert (
A("impatient").n('p').realize()   
    ) == 'impatients',\
    'A("impatient").n(\'p\')=>impatients'


def test_declension_fr_1158():
    assert (
A("imperméable").n('p').realize()   
    ) == 'imperméables',\
    'A("imperméable").n(\'p\')=>imperméables'


def test_declension_fr_1159():
    assert (
N("importance").g('f').n('p').realize()   
    ) == 'importances',\
    'N("importance").g(\'f\').n(\'p\')=>importances'


def test_declension_fr_1160():
    assert (
A("important").n('p').realize()   
    ) == 'importants',\
    'A("important").n(\'p\')=>importants'


def test_declension_fr_1161():
    assert (
A("imposant").n('p').realize()   
    ) == 'imposants',\
    'A("imposant").n(\'p\')=>imposants'


def test_declension_fr_1162():
    assert (
N("impossibilité").g('f').n('p').realize()   
    ) == 'impossibilités',\
    'N("impossibilité").g(\'f\').n(\'p\')=>impossibilités'


def test_declension_fr_1163():
    assert (
A("impossible").n('p').realize()   
    ) == 'impossibles',\
    'A("impossible").n(\'p\')=>impossibles'


def test_declension_fr_1164():
    assert (
N("impression").g('f').n('p').realize()   
    ) == 'impressions',\
    'N("impression").g(\'f\').n(\'p\')=>impressions'


def test_declension_fr_1165():
    assert (
A("imprévu").n('p').realize()   
    ) == 'imprévus',\
    'A("imprévu").n(\'p\')=>imprévus'


def test_declension_fr_1166():
    assert (
N("imprudence").g('f').n('p').realize()   
    ) == 'imprudences',\
    'N("imprudence").g(\'f\').n(\'p\')=>imprudences'


def test_declension_fr_1167():
    assert (
A("imprudent").n('p').realize()   
    ) == 'imprudents',\
    'A("imprudent").n(\'p\')=>imprudents'


def test_declension_fr_1168():
    assert (
N("incendie").g('m').n('p').realize()   
    ) == 'incendies',\
    'N("incendie").g(\'m\').n(\'p\')=>incendies'


def test_declension_fr_1169():
    assert (
N("incident").g('m').n('p').realize()   
    ) == 'incidents',\
    'N("incident").g(\'m\').n(\'p\')=>incidents'


def test_declension_fr_1170():
    assert (
N("inconnu").g('m').n('p').realize()   
    ) == 'inconnus',\
    'N("inconnu").g(\'m\').n(\'p\')=>inconnus'


def test_declension_fr_1171():
    assert (
N("inconvénient").g('m').n('p').realize()   
    ) == 'inconvénients',\
    'N("inconvénient").g(\'m\').n(\'p\')=>inconvénients'


def test_declension_fr_1172():
    assert (
N("indication").g('f').n('p').realize()   
    ) == 'indications',\
    'N("indication").g(\'f\').n(\'p\')=>indications'


def test_declension_fr_1173():
    assert (
A("indifférent").n('p').realize()   
    ) == 'indifférents',\
    'A("indifférent").n(\'p\')=>indifférents'


def test_declension_fr_1174():
    assert (
A("indigne").n('p').realize()   
    ) == 'indignes',\
    'A("indigne").n(\'p\')=>indignes'


def test_declension_fr_1175():
    assert (
A("indispensable").n('p').realize()   
    ) == 'indispensables',\
    'A("indispensable").n(\'p\')=>indispensables'


def test_declension_fr_1176():
    assert (
N("industrie").g('f').n('p').realize()   
    ) == 'industries',\
    'N("industrie").g(\'f\').n(\'p\')=>industries'


def test_declension_fr_1177():
    assert (
A("industriel").n('p').realize()   
    ) == 'industriels',\
    'A("industriel").n(\'p\')=>industriels'


def test_declension_fr_1178():
    assert (
A("inerte").n('p').realize()   
    ) == 'inertes',\
    'A("inerte").n(\'p\')=>inertes'


def test_declension_fr_1179():
    assert (
A("inférieur").n('p').realize()   
    ) == 'inférieurs',\
    'A("inférieur").n(\'p\')=>inférieurs'


def test_declension_fr_1180():
    assert (
A("infini").n('p').realize()   
    ) == 'infinis',\
    'A("infini").n(\'p\')=>infinis'


def test_declension_fr_1181():
    assert (
A("infirme").n('p').realize()   
    ) == 'infirmes',\
    'A("infirme").n(\'p\')=>infirmes'


def test_declension_fr_1182():
    assert (
N("infirmier").g('m').n('p').realize()   
    ) == 'infirmiers',\
    'N("infirmier").g(\'m\').n(\'p\')=>infirmiers'


def test_declension_fr_1183():
    assert (
N("influence").g('f').n('p').realize()   
    ) == 'influences',\
    'N("influence").g(\'f\').n(\'p\')=>influences'


def test_declension_fr_1184():
    assert (
A("ingrat").n('p').realize()   
    ) == 'ingrats',\
    'A("ingrat").n(\'p\')=>ingrats'


def test_declension_fr_1185():
    assert (
N("ingratitude").g('f').n('p').realize()   
    ) == 'ingratitudes',\
    'N("ingratitude").g(\'f\').n(\'p\')=>ingratitudes'


def test_declension_fr_1186():
    assert (
N("injure").g('f').n('p').realize()   
    ) == 'injures',\
    'N("injure").g(\'f\').n(\'p\')=>injures'


def test_declension_fr_1187():
    assert (
A("innocent").n('p').realize()   
    ) == 'innocents',\
    'A("innocent").n(\'p\')=>innocents'


def test_declension_fr_1188():
    assert (
N("inondation").g('f').n('p').realize()   
    ) == 'inondations',\
    'N("inondation").g(\'f\').n(\'p\')=>inondations'


def test_declension_fr_1189():
    assert (
A("inquiet").n('p').realize()   
    ) == 'inquiets',\
    'A("inquiet").n(\'p\')=>inquiets'


def test_declension_fr_1190():
    assert (
N("inquiétude").g('f').n('p').realize()   
    ) == 'inquiétudes',\
    'N("inquiétude").g(\'f\').n(\'p\')=>inquiétudes'


def test_declension_fr_1191():
    assert (
N("insecte").g('m').n('p').realize()   
    ) == 'insectes',\
    'N("insecte").g(\'m\').n(\'p\')=>insectes'


def test_declension_fr_1192():
    assert (
N("insigne").g('m').n('p').realize()   
    ) == 'insignes',\
    'N("insigne").g(\'m\').n(\'p\')=>insignes'


def test_declension_fr_1193():
    assert (
N("inspecteur").g('m').n('p').realize()   
    ) == 'inspecteurs',\
    'N("inspecteur").g(\'m\').n(\'p\')=>inspecteurs'


def test_declension_fr_1194():
    assert (
N("instant").g('m').n('p').realize()   
    ) == 'instants',\
    'N("instant").g(\'m\').n(\'p\')=>instants'


def test_declension_fr_1195():
    assert (
N("institut").g('m').n('p').realize()   
    ) == 'instituts',\
    'N("institut").g(\'m\').n(\'p\')=>instituts'


def test_declension_fr_1196():
    assert (
N("instituteur").g('m').n('p').realize()   
    ) == 'instituteurs',\
    'N("instituteur").g(\'m\').n(\'p\')=>instituteurs'


def test_declension_fr_1197():
    assert (
A("instructif").n('p').realize()   
    ) == 'instructifs',\
    'A("instructif").n(\'p\')=>instructifs'


def test_declension_fr_1198():
    assert (
N("instruction").g('f').n('p').realize()   
    ) == 'instructions',\
    'N("instruction").g(\'f\').n(\'p\')=>instructions'


def test_declension_fr_1199():
    assert (
N("instrument").g('m').n('p').realize()   
    ) == 'instruments',\
    'N("instrument").g(\'m\').n(\'p\')=>instruments'


def test_declension_fr_1200():
    assert (
A("intellectuel").n('p').realize()   
    ) == 'intellectuels',\
    'A("intellectuel").n(\'p\')=>intellectuels'


def test_declension_fr_1201():
    assert (
N("intelligence").g('f').n('p').realize()   
    ) == 'intelligences',\
    'N("intelligence").g(\'f\').n(\'p\')=>intelligences'


def test_declension_fr_1202():
    assert (
A("intelligent").n('p').realize()   
    ) == 'intelligents',\
    'A("intelligent").n(\'p\')=>intelligents'


def test_declension_fr_1203():
    assert (
A("intense").n('p').realize()   
    ) == 'intenses',\
    'A("intense").n(\'p\')=>intenses'


def test_declension_fr_1204():
    assert (
N("intention").g('f').n('p').realize()   
    ) == 'intentions',\
    'N("intention").g(\'f\').n(\'p\')=>intentions'


def test_declension_fr_1205():
    assert (
A("intéressant").n('p').realize()   
    ) == 'intéressants',\
    'A("intéressant").n(\'p\')=>intéressants'


def test_declension_fr_1206():
    assert (
N("intérêt").g('m').n('p').realize()   
    ) == 'intérêts',\
    'N("intérêt").g(\'m\').n(\'p\')=>intérêts'


def test_declension_fr_1207():
    assert (
A("intérieur").n('p').realize()   
    ) == 'intérieurs',\
    'A("intérieur").n(\'p\')=>intérieurs'


def test_declension_fr_1208():
    assert (
N("interruption").g('f').n('p').realize()   
    ) == 'interruptions',\
    'N("interruption").g(\'f\').n(\'p\')=>interruptions'


def test_declension_fr_1209():
    assert (
A("intime").n('p').realize()   
    ) == 'intimes',\
    'A("intime").n(\'p\')=>intimes'


def test_declension_fr_1210():
    assert (
N("introduction").g('f').n('p').realize()   
    ) == 'introductions',\
    'N("introduction").g(\'f\').n(\'p\')=>introductions'


def test_declension_fr_1211():
    assert (
A("inutile").n('p').realize()   
    ) == 'inutiles',\
    'A("inutile").n(\'p\')=>inutiles'


def test_declension_fr_1212():
    assert (
N("invention").g('f').n('p').realize()   
    ) == 'inventions',\
    'N("invention").g(\'f\').n(\'p\')=>inventions'


def test_declension_fr_1213():
    assert (
A("invisible").n('p').realize()   
    ) == 'invisibles',\
    'A("invisible").n(\'p\')=>invisibles'


def test_declension_fr_1214():
    assert (
N("invitation").g('f').n('p').realize()   
    ) == 'invitations',\
    'N("invitation").g(\'f\').n(\'p\')=>invitations'


def test_declension_fr_1215():
    assert (
N("ivoire").g('m').n('p').realize()   
    ) == 'ivoires',\
    'N("ivoire").g(\'m\').n(\'p\')=>ivoires'


def test_declension_fr_1216():
    assert (
A("ivre").n('p').realize()   
    ) == 'ivres',\
    'A("ivre").n(\'p\')=>ivres'


def test_declension_fr_1217():
    assert (
N("ivresse").g('f').n('p').realize()   
    ) == 'ivresses',\
    'N("ivresse").g(\'f\').n(\'p\')=>ivresses'


def test_declension_fr_1218():
    assert (
N("jacinthe").g('f').n('p').realize()   
    ) == 'jacinthes',\
    'N("jacinthe").g(\'f\').n(\'p\')=>jacinthes'


def test_declension_fr_1219():
    assert (
A("jaloux").n('p').realize()   
    ) == 'jaloux',\
    'A("jaloux").n(\'p\')=>jaloux'


def test_declension_fr_1220():
    assert (
N("jambe").g('f').n('p').realize()   
    ) == 'jambes',\
    'N("jambe").g(\'f\').n(\'p\')=>jambes'


def test_declension_fr_1221():
    assert (
N("jambon").g('m').n('p').realize()   
    ) == 'jambons',\
    'N("jambon").g(\'m\').n(\'p\')=>jambons'


def test_declension_fr_1222():
    assert (
N("janvier").g('m').n('p').realize()   
    ) == 'janviers',\
    'N("janvier").g(\'m\').n(\'p\')=>janviers'


def test_declension_fr_1223():
    assert (
N("jardin").g('m').n('p').realize()   
    ) == 'jardins',\
    'N("jardin").g(\'m\').n(\'p\')=>jardins'


def test_declension_fr_1224():
    assert (
N("jardinage").g('m').n('p').realize()   
    ) == 'jardinages',\
    'N("jardinage").g(\'m\').n(\'p\')=>jardinages'


def test_declension_fr_1225():
    assert (
N("jardinier").g('m').n('p').realize()   
    ) == 'jardiniers',\
    'N("jardinier").g(\'m\').n(\'p\')=>jardiniers'


def test_declension_fr_1226():
    assert (
A("jaune").n('p').realize()   
    ) == 'jaunes',\
    'A("jaune").n(\'p\')=>jaunes'


def test_declension_fr_1227():
    assert (
N("jeu").g('m').n('p').realize()   
    ) == 'jeux',\
    'N("jeu").g(\'m\').n(\'p\')=>jeux'


def test_declension_fr_1228():
    assert (
N("jeudi").g('m').n('p').realize()   
    ) == 'jeudis',\
    'N("jeudi").g(\'m\').n(\'p\')=>jeudis'


def test_declension_fr_1229():
    assert (
A("jeune").n('p').realize()   
    ) == 'jeunes',\
    'A("jeune").n(\'p\')=>jeunes'


def test_declension_fr_1230():
    assert (
N("jeunesse").g('f').n('p').realize()   
    ) == 'jeunesses',\
    'N("jeunesse").g(\'f\').n(\'p\')=>jeunesses'


def test_declension_fr_1231():
    assert (
N("joie").g('f').n('p').realize()   
    ) == 'joies',\
    'N("joie").g(\'f\').n(\'p\')=>joies'


def test_declension_fr_1232():
    assert (
A("joli").n('p').realize()   
    ) == 'jolis',\
    'A("joli").n(\'p\')=>jolis'


def test_declension_fr_1233():
    assert (
N("jonquille").g('f').n('p').realize()   
    ) == 'jonquilles',\
    'N("jonquille").g(\'f\').n(\'p\')=>jonquilles'


def test_declension_fr_1234():
    assert (
N("joue").g('f').n('p').realize()   
    ) == 'joues',\
    'N("joue").g(\'f\').n(\'p\')=>joues'


def test_declension_fr_1235():
    assert (
N("jouet").g('m').n('p').realize()   
    ) == 'jouets',\
    'N("jouet").g(\'m\').n(\'p\')=>jouets'


def test_declension_fr_1236():
    assert (
N("joueur").g('m').n('p').realize()   
    ) == 'joueurs',\
    'N("joueur").g(\'m\').n(\'p\')=>joueurs'


def test_declension_fr_1237():
    assert (
N("joujou").g('m').n('p').realize()   
    ) == 'joujoux',\
    'N("joujou").g(\'m\').n(\'p\')=>joujoux'


def test_declension_fr_1238():
    assert (
N("jour").g('m').n('p').realize()   
    ) == 'jours',\
    'N("jour").g(\'m\').n(\'p\')=>jours'


def test_declension_fr_1239():
    assert (
N("journal").g('m').n('p').realize()   
    ) == 'journaux',\
    'N("journal").g(\'m\').n(\'p\')=>journaux'


def test_declension_fr_1240():
    assert (
A("journalier").n('p').realize()   
    ) == 'journaliers',\
    'A("journalier").n(\'p\')=>journaliers'


def test_declension_fr_1241():
    assert (
N("journée").g('f').n('p').realize()   
    ) == 'journées',\
    'N("journée").g(\'f\').n(\'p\')=>journées'


def test_declension_fr_1242():
    assert (
A("joyeux").n('p').realize()   
    ) == 'joyeux',\
    'A("joyeux").n(\'p\')=>joyeux'


def test_declension_fr_1243():
    assert (
N("juge").g('m').n('p').realize()   
    ) == 'juges',\
    'N("juge").g(\'m\').n(\'p\')=>juges'


def test_declension_fr_1244():
    assert (
N("jugement").g('m').n('p').realize()   
    ) == 'jugements',\
    'N("jugement").g(\'m\').n(\'p\')=>jugements'


def test_declension_fr_1245():
    assert (
N("juillet").g('m').n('p').realize()   
    ) == 'juillets',\
    'N("juillet").g(\'m\').n(\'p\')=>juillets'


def test_declension_fr_1246():
    assert (
N("juin").g('m').n('p').realize()   
    ) == 'juins',\
    'N("juin").g(\'m\').n(\'p\')=>juins'


def test_declension_fr_1247():
    assert (
A("juste").n('p').realize()   
    ) == 'justes',\
    'A("juste").n(\'p\')=>justes'


def test_declension_fr_1248():
    assert (
N("justice").g('f').n('p').realize()   
    ) == 'justices',\
    'N("justice").g(\'f\').n(\'p\')=>justices'


def test_declension_fr_1249():
    assert (
N("képi").g('m').n('p').realize()   
    ) == 'képis',\
    'N("képi").g(\'m\').n(\'p\')=>képis'


def test_declension_fr_1250():
    assert (
N("kermesse").g('f').n('p').realize()   
    ) == 'kermesses',\
    'N("kermesse").g(\'f\').n(\'p\')=>kermesses'


def test_declension_fr_1251():
    assert (
N("kilogramme").g('m').n('p').realize()   
    ) == 'kilogrammes',\
    'N("kilogramme").g(\'m\').n(\'p\')=>kilogrammes'


def test_declension_fr_1252():
    assert (
N("kilomètre").g('m').n('p').realize()   
    ) == 'kilomètres',\
    'N("kilomètre").g(\'m\').n(\'p\')=>kilomètres'


def test_declension_fr_1253():
    assert (
N("labeur").g('m').n('p').realize()   
    ) == 'labeurs',\
    'N("labeur").g(\'m\').n(\'p\')=>labeurs'


def test_declension_fr_1254():
    assert (
A("laborieux").n('p').realize()   
    ) == 'laborieux',\
    'A("laborieux").n(\'p\')=>laborieux'


def test_declension_fr_1255():
    assert (
N("laboureur").g('m').n('p').realize()   
    ) == 'laboureurs',\
    'N("laboureur").g(\'m\').n(\'p\')=>laboureurs'


def test_declension_fr_1256():
    assert (
N("lac").g('m').n('p').realize()   
    ) == 'lacs',\
    'N("lac").g(\'m\').n(\'p\')=>lacs'


def test_declension_fr_1257():
    assert (
A("laid").n('p').realize()   
    ) == 'laids',\
    'A("laid").n(\'p\')=>laids'


def test_declension_fr_1258():
    assert (
N("laine").g('f').n('p').realize()   
    ) == 'laines',\
    'N("laine").g(\'f\').n(\'p\')=>laines'


def test_declension_fr_1259():
    assert (
N("lait").g('m').n('p').realize()   
    ) == 'laits',\
    'N("lait").g(\'m\').n(\'p\')=>laits'


def test_declension_fr_1260():
    assert (
N("laitier").g('m').n('p').realize()   
    ) == 'laitiers',\
    'N("laitier").g(\'m\').n(\'p\')=>laitiers'


def test_declension_fr_1261():
    assert (
N("lambeau").g('m').n('p').realize()   
    ) == 'lambeaux',\
    'N("lambeau").g(\'m\').n(\'p\')=>lambeaux'


def test_declension_fr_1262():
    assert (
A("lamentable").n('p').realize()   
    ) == 'lamentables',\
    'A("lamentable").n(\'p\')=>lamentables'


def test_declension_fr_1263():
    assert (
N("lampe").g('f').n('p').realize()   
    ) == 'lampes',\
    'N("lampe").g(\'f\').n(\'p\')=>lampes'


def test_declension_fr_1264():
    assert (
N("langage").g('m').n('p').realize()   
    ) == 'langages',\
    'N("langage").g(\'m\').n(\'p\')=>langages'


def test_declension_fr_1265():
    assert (
N("langue").g('f').n('p').realize()   
    ) == 'langues',\
    'N("langue").g(\'f\').n(\'p\')=>langues'


def test_declension_fr_1266():
    assert (
N("lanterne").g('f').n('p').realize()   
    ) == 'lanternes',\
    'N("lanterne").g(\'f\').n(\'p\')=>lanternes'


def test_declension_fr_1267():
    assert (
N("lapin").g('m').n('p').realize()   
    ) == 'lapins',\
    'N("lapin").g(\'m\').n(\'p\')=>lapins'


def test_declension_fr_1268():
    assert (
A("large").n('p').realize()   
    ) == 'larges',\
    'A("large").n(\'p\')=>larges'


def test_declension_fr_1269():
    assert (
N("larme").g('f').n('p').realize()   
    ) == 'larmes',\
    'N("larme").g(\'f\').n(\'p\')=>larmes'


def test_declension_fr_1270():
    assert (
A("las").n('p').realize()   
    ) == 'las',\
    'A("las").n(\'p\')=>las'


def test_declension_fr_1271():
    assert (
N("leçon").g('f').n('p').realize()   
    ) == 'leçons',\
    'N("leçon").g(\'f\').n(\'p\')=>leçons'


def test_declension_fr_1272():
    assert (
N("lecture").g('f').n('p').realize()   
    ) == 'lectures',\
    'N("lecture").g(\'f\').n(\'p\')=>lectures'


def test_declension_fr_1273():
    assert (
A("léger").n('p').realize()   
    ) == 'légers',\
    'A("léger").n(\'p\')=>légers'


def test_declension_fr_1274():
    assert (
N("légume").n('p').realize()   
    ) == 'légumes',\
    'N("légume").n(\'p\')=>légumes'


def test_declension_fr_1275():
    assert (
N("lendemain").g('m').n('p').realize()   
    ) == 'lendemains',\
    'N("lendemain").g(\'m\').n(\'p\')=>lendemains'


def test_declension_fr_1276():
    assert (
A("lent").n('p').realize()   
    ) == 'lents',\
    'A("lent").n(\'p\')=>lents'


def test_declension_fr_1277():
    assert (
N("lenteur").g('f').n('p').realize()   
    ) == 'lenteurs',\
    'N("lenteur").g(\'f\').n(\'p\')=>lenteurs'


def test_declension_fr_1278():
    assert (
N("lettre").g('f').n('p').realize()   
    ) == 'lettres',\
    'N("lettre").g(\'f\').n(\'p\')=>lettres'


def test_declension_fr_1279():
    assert (
N("lèvre").g('f').n('p').realize()   
    ) == 'lèvres',\
    'N("lèvre").g(\'f\').n(\'p\')=>lèvres'


def test_declension_fr_1280():
    assert (
N("liberté").g('f').n('p').realize()   
    ) == 'libertés',\
    'N("liberté").g(\'f\').n(\'p\')=>libertés'


def test_declension_fr_1281():
    assert (
A("libre").n('p').realize()   
    ) == 'libres',\
    'A("libre").n(\'p\')=>libres'


def test_declension_fr_1282():
    assert (
N("lien").g('m').n('p').realize()   
    ) == 'liens',\
    'N("lien").g(\'m\').n(\'p\')=>liens'


def test_declension_fr_1283():
    assert (
N("lierre").g('m').n('p').realize()   
    ) == 'lierres',\
    'N("lierre").g(\'m\').n(\'p\')=>lierres'


def test_declension_fr_1284():
    assert (
N("lieu").g('m').n('p').realize()   
    ) == 'lieux',\
    'N("lieu").g(\'m\').n(\'p\')=>lieux'


def test_declension_fr_1285():
    assert (
N("lieue").g('f').n('p').realize()   
    ) == 'lieues',\
    'N("lieue").g(\'f\').n(\'p\')=>lieues'


def test_declension_fr_1286():
    assert (
N("lièvre").g('m').n('p').realize()   
    ) == 'lièvres',\
    'N("lièvre").g(\'m\').n(\'p\')=>lièvres'


def test_declension_fr_1287():
    assert (
N("ligne").g('f').n('p').realize()   
    ) == 'lignes',\
    'N("ligne").g(\'f\').n(\'p\')=>lignes'


def test_declension_fr_1288():
    assert (
N("ligue").g('f').n('p').realize()   
    ) == 'ligues',\
    'N("ligue").g(\'f\').n(\'p\')=>ligues'


def test_declension_fr_1289():
    assert (
N("lilas").g('m').n('p').realize()   
    ) == 'lilas',\
    'N("lilas").g(\'m\').n(\'p\')=>lilas'


def test_declension_fr_1290():
    assert (
N("limite").g('f').n('p').realize()   
    ) == 'limites',\
    'N("limite").g(\'f\').n(\'p\')=>limites'


def test_declension_fr_1291():
    assert (
A("limpide").n('p').realize()   
    ) == 'limpides',\
    'A("limpide").n(\'p\')=>limpides'


def test_declension_fr_1292():
    assert (
N("lin").g('m').n('p').realize()   
    ) == 'lins',\
    'N("lin").g(\'m\').n(\'p\')=>lins'


def test_declension_fr_1293():
    assert (
N("linge").g('m').n('p').realize()   
    ) == 'linges',\
    'N("linge").g(\'m\').n(\'p\')=>linges'


def test_declension_fr_1294():
    assert (
N("lion").g('m').n('p').realize()   
    ) == 'lions',\
    'N("lion").g(\'m\').n(\'p\')=>lions'


def test_declension_fr_1295():
    assert (
A("liquide").n('p').realize()   
    ) == 'liquides',\
    'A("liquide").n(\'p\')=>liquides'


def test_declension_fr_1296():
    assert (
N("lis").g('m').n('p').realize()   
    ) == 'lis',\
    'N("lis").g(\'m\').n(\'p\')=>lis'


def test_declension_fr_1297():
    assert (
N("lisière").g('f').n('p').realize()   
    ) == 'lisières',\
    'N("lisière").g(\'f\').n(\'p\')=>lisières'


def test_declension_fr_1298():
    assert (
A("lisse").n('p').realize()   
    ) == 'lisses',\
    'A("lisse").n(\'p\')=>lisses'


def test_declension_fr_1299():
    assert (
N("liste").g('f').n('p').realize()   
    ) == 'listes',\
    'N("liste").g(\'f\').n(\'p\')=>listes'


def test_declension_fr_1300():
    assert (
N("lit").g('m').n('p').realize()   
    ) == 'lits',\
    'N("lit").g(\'m\').n(\'p\')=>lits'


def test_declension_fr_1301():
    assert (
N("litière").g('f').n('p').realize()   
    ) == 'litières',\
    'N("litière").g(\'f\').n(\'p\')=>litières'


def test_declension_fr_1302():
    assert (
N("livre").g('m').n('p').realize()   
    ) == 'livres',\
    'N("livre").g(\'m\').n(\'p\')=>livres'


def test_declension_fr_1303():
    assert (
N("local").g('m').n('p').realize()   
    ) == 'locaux',\
    'N("local").g(\'m\').n(\'p\')=>locaux'


def test_declension_fr_1304():
    assert (
N("localité").g('f').n('p').realize()   
    ) == 'localités',\
    'N("localité").g(\'f\').n(\'p\')=>localités'


def test_declension_fr_1305():
    assert (
N("locomotive").g('f').n('p').realize()   
    ) == 'locomotives',\
    'N("locomotive").g(\'f\').n(\'p\')=>locomotives'


def test_declension_fr_1306():
    assert (
N("logis").g('m').n('p').realize()   
    ) == 'logis',\
    'N("logis").g(\'m\').n(\'p\')=>logis'


def test_declension_fr_1307():
    assert (
N("loi").g('f').n('p').realize()   
    ) == 'lois',\
    'N("loi").g(\'f\').n(\'p\')=>lois'


def test_declension_fr_1308():
    assert (
A("lointain").n('p').realize()   
    ) == 'lointains',\
    'A("lointain").n(\'p\')=>lointains'


def test_declension_fr_1309():
    assert (
N("loisir").g('m').n('p').realize()   
    ) == 'loisirs',\
    'N("loisir").g(\'m\').n(\'p\')=>loisirs'


def test_declension_fr_1310():
    assert (
A("long").n('p').realize()   
    ) == 'longs',\
    'A("long").n(\'p\')=>longs'


def test_declension_fr_1311():
    assert (
N("longueur").g('f').n('p').realize()   
    ) == 'longueurs',\
    'N("longueur").g(\'f\').n(\'p\')=>longueurs'


def test_declension_fr_1312():
    assert (
N("lot").g('m').n('p').realize()   
    ) == 'lots',\
    'N("lot").g(\'m\').n(\'p\')=>lots'


def test_declension_fr_1313():
    assert (
N("louange").g('f').n('p').realize()   
    ) == 'louanges',\
    'N("louange").g(\'f\').n(\'p\')=>louanges'


def test_declension_fr_1314():
    assert (
N("loup").g('m').n('p').realize()   
    ) == 'loups',\
    'N("loup").g(\'m\').n(\'p\')=>loups'


def test_declension_fr_1315():
    assert (
A("lourd").n('p').realize()   
    ) == 'lourds',\
    'A("lourd").n(\'p\')=>lourds'


def test_declension_fr_1316():
    assert (
N("louve").g('f').n('p').realize()   
    ) == 'louves',\
    'N("louve").g(\'f\').n(\'p\')=>louves'


def test_declension_fr_1317():
    assert (
A("loyal").n('p').realize()   
    ) == 'loyaux',\
    'A("loyal").n(\'p\')=>loyaux'


def test_declension_fr_1318():
    assert (
N("lueur").g('f').n('p').realize()   
    ) == 'lueurs',\
    'N("lueur").g(\'f\').n(\'p\')=>lueurs'


def test_declension_fr_1319():
    assert (
A("lugubre").n('p').realize()   
    ) == 'lugubres',\
    'A("lugubre").n(\'p\')=>lugubres'


def test_declension_fr_1320():
    assert (
A("luisant").n('p').realize()   
    ) == 'luisants',\
    'A("luisant").n(\'p\')=>luisants'


def test_declension_fr_1321():
    assert (
N("lumière").g('f').n('p').realize()   
    ) == 'lumières',\
    'N("lumière").g(\'f\').n(\'p\')=>lumières'


def test_declension_fr_1322():
    assert (
A("lumineux").n('p').realize()   
    ) == 'lumineux',\
    'A("lumineux").n(\'p\')=>lumineux'


def test_declension_fr_1323():
    assert (
N("lundi").g('m').n('p').realize()   
    ) == 'lundis',\
    'N("lundi").g(\'m\').n(\'p\')=>lundis'


def test_declension_fr_1324():
    assert (
N("lune").g('f').n('p').realize()   
    ) == 'lunes',\
    'N("lune").g(\'f\').n(\'p\')=>lunes'


def test_declension_fr_1325():
    assert (
N("lunette").g('f').n('p').realize()   
    ) == 'lunettes',\
    'N("lunette").g(\'f\').n(\'p\')=>lunettes'


def test_declension_fr_1326():
    assert (
N("lutin").g('m').n('p').realize()   
    ) == 'lutins',\
    'N("lutin").g(\'m\').n(\'p\')=>lutins'


def test_declension_fr_1327():
    assert (
N("lutte").g('f').n('p').realize()   
    ) == 'luttes',\
    'N("lutte").g(\'f\').n(\'p\')=>luttes'


def test_declension_fr_1328():
    assert (
N("lys").g('m').n('p').realize()   
    ) == 'lys',\
    'N("lys").g(\'m\').n(\'p\')=>lys'


def test_declension_fr_1329():
    assert (
N("machine").g('f').n('p').realize()   
    ) == 'machines',\
    'N("machine").g(\'f\').n(\'p\')=>machines'


def test_declension_fr_1330():
    assert (
N("mâchoire").g('f').n('p').realize()   
    ) == 'mâchoires',\
    'N("mâchoire").g(\'f\').n(\'p\')=>mâchoires'


def test_declension_fr_1331():
    assert (
N("madame").g('f').n('p').realize()   
    ) == 'mesdames',\
    'N("madame").g(\'f\').n(\'p\')=>mesdames'


def test_declension_fr_1332():
    assert (
N("mademoiselle").g('f').n('p').realize()   
    ) == 'mesdemoiselles',\
    'N("mademoiselle").g(\'f\').n(\'p\')=>mesdemoiselles'


def test_declension_fr_1333():
    assert (
N("magasin").g('m').n('p').realize()   
    ) == 'magasins',\
    'N("magasin").g(\'m\').n(\'p\')=>magasins'


def test_declension_fr_1334():
    assert (
A("magique").n('p').realize()   
    ) == 'magiques',\
    'A("magique").n(\'p\')=>magiques'


def test_declension_fr_1335():
    assert (
A("magnifique").n('p').realize()   
    ) == 'magnifiques',\
    'A("magnifique").n(\'p\')=>magnifiques'


def test_declension_fr_1336():
    assert (
N("mai").g('m').n('p').realize()   
    ) == 'mais',\
    'N("mai").g(\'m\').n(\'p\')=>mais'


def test_declension_fr_1337():
    assert (
A("maigre").n('p').realize()   
    ) == 'maigres',\
    'A("maigre").n(\'p\')=>maigres'


def test_declension_fr_1338():
    assert (
N("main").g('f').n('p').realize()   
    ) == 'mains',\
    'N("main").g(\'f\').n(\'p\')=>mains'


def test_declension_fr_1339():
    assert (
N("maire").g('m').n('p').realize()   
    ) == 'maires',\
    'N("maire").g(\'m\').n(\'p\')=>maires'


def test_declension_fr_1340():
    assert (
N("maison").g('f').n('p').realize()   
    ) == 'maisons',\
    'N("maison").g(\'f\').n(\'p\')=>maisons'


def test_declension_fr_1341():
    assert (
N("maître").g('m').n('p').realize()   
    ) == 'maîtres',\
    'N("maître").g(\'m\').n(\'p\')=>maîtres'


def test_declension_fr_1342():
    assert (
N("majesté").g('f').n('p').realize()   
    ) == 'majestés',\
    'N("majesté").g(\'f\').n(\'p\')=>majestés'


def test_declension_fr_1343():
    assert (
A("majestueux").n('p').realize()   
    ) == 'majestueux',\
    'A("majestueux").n(\'p\')=>majestueux'


def test_declension_fr_1344():
    assert (
A("malade").n('p').realize()   
    ) == 'malades',\
    'A("malade").n(\'p\')=>malades'


def test_declension_fr_1345():
    assert (
N("maladie").g('f').n('p').realize()   
    ) == 'maladies',\
    'N("maladie").g(\'f\').n(\'p\')=>maladies'


def test_declension_fr_1346():
    assert (
N("malheur").g('m').n('p').realize()   
    ) == 'malheurs',\
    'N("malheur").g(\'m\').n(\'p\')=>malheurs'


def test_declension_fr_1347():
    assert (
A("malheureux").n('p').realize()   
    ) == 'malheureux',\
    'A("malheureux").n(\'p\')=>malheureux'


def test_declension_fr_1348():
    assert (
A("malin").n('p').realize()   
    ) == 'malins',\
    'A("malin").n(\'p\')=>malins'


def test_declension_fr_1349():
    assert (
N("malle").g('f').n('p').realize()   
    ) == 'malles',\
    'N("malle").g(\'f\').n(\'p\')=>malles'


def test_declension_fr_1350():
    assert (
N("maman").g('f').n('p').realize()   
    ) == 'mamans',\
    'N("maman").g(\'f\').n(\'p\')=>mamans'


def test_declension_fr_1351():
    assert (
N("manche").g('f').n('p').realize()   
    ) == 'manches',\
    'N("manche").g(\'f\').n(\'p\')=>manches'


def test_declension_fr_1352():
    assert (
N("manière").g('f').n('p').realize()   
    ) == 'manières',\
    'N("manière").g(\'f\').n(\'p\')=>manières'


def test_declension_fr_1353():
    assert (
N("manoeuvre").g('m').n('p').realize()   
    ) == 'manoeuvres',\
    'N("manoeuvre").g(\'m\').n(\'p\')=>manoeuvres'


def test_declension_fr_1354():
    assert (
N("manque").g('m').n('p').realize()   
    ) == 'manques',\
    'N("manque").g(\'m\').n(\'p\')=>manques'


def test_declension_fr_1355():
    assert (
N("mansarde").g('f').n('p').realize()   
    ) == 'mansardes',\
    'N("mansarde").g(\'f\').n(\'p\')=>mansardes'


def test_declension_fr_1356():
    assert (
N("manteau").g('m').n('p').realize()   
    ) == 'manteaux',\
    'N("manteau").g(\'m\').n(\'p\')=>manteaux'


def test_declension_fr_1357():
    assert (
A("manuel").n('p').realize()   
    ) == 'manuels',\
    'A("manuel").n(\'p\')=>manuels'


def test_declension_fr_1358():
    assert (
N("marbre").g('m').n('p').realize()   
    ) == 'marbres',\
    'N("marbre").g(\'m\').n(\'p\')=>marbres'


def test_declension_fr_1359():
    assert (
N("marchand").g('m').n('p').realize()   
    ) == 'marchands',\
    'N("marchand").g(\'m\').n(\'p\')=>marchands'


def test_declension_fr_1360():
    assert (
N("marchandise").g('f').n('p').realize()   
    ) == 'marchandises',\
    'N("marchandise").g(\'f\').n(\'p\')=>marchandises'


def test_declension_fr_1361():
    assert (
N("marche").g('f').n('p').realize()   
    ) == 'marches',\
    'N("marche").g(\'f\').n(\'p\')=>marches'


def test_declension_fr_1362():
    assert (
N("marché").g('m').n('p').realize()   
    ) == 'marchés',\
    'N("marché").g(\'m\').n(\'p\')=>marchés'


def test_declension_fr_1363():
    assert (
N("mardi").g('m').n('p').realize()   
    ) == 'mardis',\
    'N("mardi").g(\'m\').n(\'p\')=>mardis'


def test_declension_fr_1364():
    assert (
N("mare").g('f').n('p').realize()   
    ) == 'mares',\
    'N("mare").g(\'f\').n(\'p\')=>mares'


def test_declension_fr_1365():
    assert (
N("marguerite").g('f').n('p').realize()   
    ) == 'marguerites',\
    'N("marguerite").g(\'f\').n(\'p\')=>marguerites'


def test_declension_fr_1366():
    assert (
N("mari").g('m').n('p').realize()   
    ) == 'maris',\
    'N("mari").g(\'m\').n(\'p\')=>maris'


def test_declension_fr_1367():
    assert (
N("mariage").g('m').n('p').realize()   
    ) == 'mariages',\
    'N("mariage").g(\'m\').n(\'p\')=>mariages'


def test_declension_fr_1368():
    assert (
N("marin").g('m').n('p').realize()   
    ) == 'marins',\
    'N("marin").g(\'m\').n(\'p\')=>marins'


def test_declension_fr_1369():
    assert (
N("marine").g('f').n('p').realize()   
    ) == 'marines',\
    'N("marine").g(\'f\').n(\'p\')=>marines'


def test_declension_fr_1370():
    assert (
N("marque").g('f').n('p').realize()   
    ) == 'marques',\
    'N("marque").g(\'f\').n(\'p\')=>marques'


def test_declension_fr_1371():
    assert (
N("marquis").g('m').n('p').realize()   
    ) == 'marquis',\
    'N("marquis").g(\'m\').n(\'p\')=>marquis'


def test_declension_fr_1372():
    assert (
N("marraine").g('f').n('p').realize()   
    ) == 'marraines',\
    'N("marraine").g(\'f\').n(\'p\')=>marraines'


def test_declension_fr_1373():
    assert (
N("marron").g('m').n('p').realize()   
    ) == 'marrons',\
    'N("marron").g(\'m\').n(\'p\')=>marrons'


def test_declension_fr_1374():
    assert (
N("marronnier").g('m').n('p').realize()   
    ) == 'marronniers',\
    'N("marronnier").g(\'m\').n(\'p\')=>marronniers'


def test_declension_fr_1375():
    assert (
N("mars").g('m').n('p').realize()   
    ) == 'mars',\
    'N("mars").g(\'m\').n(\'p\')=>mars'


def test_declension_fr_1376():
    assert (
N("marteau").g('m').n('p').realize()   
    ) == 'marteaux',\
    'N("marteau").g(\'m\').n(\'p\')=>marteaux'


def test_declension_fr_1377():
    assert (
N("masse").g('f').n('p').realize()   
    ) == 'masses',\
    'N("masse").g(\'f\').n(\'p\')=>masses'


def test_declension_fr_1378():
    assert (
A("massif").n('p').realize()   
    ) == 'massifs',\
    'A("massif").n(\'p\')=>massifs'


def test_declension_fr_1379():
    assert (
N("mât").g('m').n('p').realize()   
    ) == 'mâts',\
    'N("mât").g(\'m\').n(\'p\')=>mâts'


def test_declension_fr_1380():
    assert (
N("matériel").g('m').n('p').realize()   
    ) == 'matériels',\
    'N("matériel").g(\'m\').n(\'p\')=>matériels'


def test_declension_fr_1381():
    assert (
A("maternel").n('p').realize()   
    ) == 'maternels',\
    'A("maternel").n(\'p\')=>maternels'


def test_declension_fr_1382():
    assert (
N("matière").g('f').n('p').realize()   
    ) == 'matières',\
    'N("matière").g(\'f\').n(\'p\')=>matières'


def test_declension_fr_1383():
    assert (
N("matin").g('m').n('p').realize()   
    ) == 'matins',\
    'N("matin").g(\'m\').n(\'p\')=>matins'


def test_declension_fr_1384():
    assert (
A("matinal").n('p').realize()   
    ) == 'matinaux',\
    'A("matinal").n(\'p\')=>matinaux'


def test_declension_fr_1385():
    assert (
N("matinée").g('f').n('p').realize()   
    ) == 'matinées',\
    'N("matinée").g(\'f\').n(\'p\')=>matinées'


def test_declension_fr_1386():
    assert (
A("maussade").n('p').realize()   
    ) == 'maussades',\
    'A("maussade").n(\'p\')=>maussades'


def test_declension_fr_1387():
    assert (
A("mauvais").n('p').realize()   
    ) == 'mauvais',\
    'A("mauvais").n(\'p\')=>mauvais'


def test_declension_fr_1388():
    assert (
A("mauve").n('p').realize()   
    ) == 'mauves',\
    'A("mauve").n(\'p\')=>mauves'


def test_declension_fr_1389():
    assert (
A("mécanique").n('p').realize()   
    ) == 'mécaniques',\
    'A("mécanique").n(\'p\')=>mécaniques'


def test_declension_fr_1390():
    assert (
A("méchant").n('p').realize()   
    ) == 'méchants',\
    'A("méchant").n(\'p\')=>méchants'


def test_declension_fr_1391():
    assert (
A("mécontent").n('p').realize()   
    ) == 'mécontents',\
    'A("mécontent").n(\'p\')=>mécontents'


def test_declension_fr_1392():
    assert (
N("médaille").g('f').n('p').realize()   
    ) == 'médailles',\
    'N("médaille").g(\'f\').n(\'p\')=>médailles'


def test_declension_fr_1393():
    assert (
N("médecin").g('m').n('p').realize()   
    ) == 'médecins',\
    'N("médecin").g(\'m\').n(\'p\')=>médecins'


def test_declension_fr_1394():
    assert (
A("meilleur").n('p').realize()   
    ) == 'meilleurs',\
    'A("meilleur").n(\'p\')=>meilleurs'


def test_declension_fr_1395():
    assert (
N("mélancolie").g('f').n('p').realize()   
    ) == 'mélancolies',\
    'N("mélancolie").g(\'f\').n(\'p\')=>mélancolies'


def test_declension_fr_1396():
    assert (
A("mélancolique").n('p').realize()   
    ) == 'mélancoliques',\
    'A("mélancolique").n(\'p\')=>mélancoliques'


def test_declension_fr_1397():
    assert (
N("mélange").g('m').n('p').realize()   
    ) == 'mélanges',\
    'N("mélange").g(\'m\').n(\'p\')=>mélanges'


def test_declension_fr_1398():
    assert (
N("mélodie").g('f').n('p').realize()   
    ) == 'mélodies',\
    'N("mélodie").g(\'f\').n(\'p\')=>mélodies'


def test_declension_fr_1399():
    assert (
A("mélodieux").n('p').realize()   
    ) == 'mélodieux',\
    'A("mélodieux").n(\'p\')=>mélodieux'


def test_declension_fr_1400():
    assert (
N("membre").g('m').n('p').realize()   
    ) == 'membres',\
    'N("membre").g(\'m\').n(\'p\')=>membres'


def test_declension_fr_1401():
    assert (
N("mémoire").g('f').n('p').realize()   
    ) == 'mémoires',\
    'N("mémoire").g(\'f\').n(\'p\')=>mémoires'


def test_declension_fr_1402():
    assert (
N("ménage").g('m').n('p').realize()   
    ) == 'ménages',\
    'N("ménage").g(\'m\').n(\'p\')=>ménages'


def test_declension_fr_1403():
    assert (
N("ménagerie").g('f').n('p').realize()   
    ) == 'ménageries',\
    'N("ménagerie").g(\'f\').n(\'p\')=>ménageries'


def test_declension_fr_1404():
    assert (
N("mendiant").g('m').n('p').realize()   
    ) == 'mendiants',\
    'N("mendiant").g(\'m\').n(\'p\')=>mendiants'


def test_declension_fr_1405():
    assert (
N("mensonge").g('m').n('p').realize()   
    ) == 'mensonges',\
    'N("mensonge").g(\'m\').n(\'p\')=>mensonges'


def test_declension_fr_1406():
    assert (
N("menteur").g('m').n('p').realize()   
    ) == 'menteurs',\
    'N("menteur").g(\'m\').n(\'p\')=>menteurs'


def test_declension_fr_1407():
    assert (
N("menton").g('m').n('p').realize()   
    ) == 'mentons',\
    'N("menton").g(\'m\').n(\'p\')=>mentons'


def test_declension_fr_1408():
    assert (
N("menu").g('m').n('p').realize()   
    ) == 'menus',\
    'N("menu").g(\'m\').n(\'p\')=>menus'


def test_declension_fr_1409():
    assert (
N("menuisier").g('m').n('p').realize()   
    ) == 'menuisiers',\
    'N("menuisier").g(\'m\').n(\'p\')=>menuisiers'


def test_declension_fr_1410():
    assert (
N("mer").g('f').n('p').realize()   
    ) == 'mers',\
    'N("mer").g(\'f\').n(\'p\')=>mers'


def test_declension_fr_1411():
    assert (
N("merci").g('m').n('p').realize()   
    ) == 'mercis',\
    'N("merci").g(\'m\').n(\'p\')=>mercis'


def test_declension_fr_1412():
    assert (
N("mercredi").g('m').n('p').realize()   
    ) == 'mercredis',\
    'N("mercredi").g(\'m\').n(\'p\')=>mercredis'


def test_declension_fr_1413():
    assert (
N("mère").g('f').n('p').realize()   
    ) == 'mères',\
    'N("mère").g(\'f\').n(\'p\')=>mères'


def test_declension_fr_1414():
    assert (
N("mérite").g('m').n('p').realize()   
    ) == 'mérites',\
    'N("mérite").g(\'m\').n(\'p\')=>mérites'


def test_declension_fr_1415():
    assert (
N("merle").g('m').n('p').realize()   
    ) == 'merles',\
    'N("merle").g(\'m\').n(\'p\')=>merles'


def test_declension_fr_1416():
    assert (
N("merveille").g('f').n('p').realize()   
    ) == 'merveilles',\
    'N("merveille").g(\'f\').n(\'p\')=>merveilles'


def test_declension_fr_1417():
    assert (
A("merveilleux").n('p').realize()   
    ) == 'merveilleux',\
    'A("merveilleux").n(\'p\')=>merveilleux'


def test_declension_fr_1418():
    assert (
N("messager").g('m').n('p').realize()   
    ) == 'messagers',\
    'N("messager").g(\'m\').n(\'p\')=>messagers'


def test_declension_fr_1419():
    assert (
N("messe").g('f').n('p').realize()   
    ) == 'messes',\
    'N("messe").g(\'f\').n(\'p\')=>messes'


def test_declension_fr_1420():
    assert (
N("mesure").g('f').n('p').realize()   
    ) == 'mesures',\
    'N("mesure").g(\'f\').n(\'p\')=>mesures'


def test_declension_fr_1421():
    assert (
N("métal").g('m').n('p').realize()   
    ) == 'métaux',\
    'N("métal").g(\'m\').n(\'p\')=>métaux'


def test_declension_fr_1422():
    assert (
N("méthode").g('f').n('p').realize()   
    ) == 'méthodes',\
    'N("méthode").g(\'f\').n(\'p\')=>méthodes'


def test_declension_fr_1423():
    assert (
N("métier").g('m').n('p').realize()   
    ) == 'métiers',\
    'N("métier").g(\'m\').n(\'p\')=>métiers'


def test_declension_fr_1424():
    assert (
A("métis").g('f').n('s').realize()   
    ) == 'métisse',\
    'A("métis").g(\'f\').n(\'s\')=>métisse'


def test_declension_fr_1425():
    assert (
N("mètre").g('m').n('p').realize()   
    ) == 'mètres',\
    'N("mètre").g(\'m\').n(\'p\')=>mètres'


def test_declension_fr_1426():
    assert (
N("meuble").g('m').n('p').realize()   
    ) == 'meubles',\
    'N("meuble").g(\'m\').n(\'p\')=>meubles'


def test_declension_fr_1427():
    assert (
N("meule").g('f').n('p').realize()   
    ) == 'meules',\
    'N("meule").g(\'f\').n(\'p\')=>meules'


def test_declension_fr_1428():
    assert (
N("meunier").g('m').n('p').realize()   
    ) == 'meuniers',\
    'N("meunier").g(\'m\').n(\'p\')=>meuniers'


def test_declension_fr_1429():
    assert (
N("midi").g('m').n('p').realize()   
    ) == 'midis',\
    'N("midi").g(\'m\').n(\'p\')=>midis'


def test_declension_fr_1430():
    assert (
N("miel").g('m').n('p').realize()   
    ) == 'miels',\
    'N("miel").g(\'m\').n(\'p\')=>miels'


def test_declension_fr_1431():
    assert (
N("miette").g('f').n('p').realize()   
    ) == 'miettes',\
    'N("miette").g(\'f\').n(\'p\')=>miettes'


def test_declension_fr_1432():
    assert (
A("mignon").n('p').realize()   
    ) == 'mignons',\
    'A("mignon").n(\'p\')=>mignons'


def test_declension_fr_1433():
    assert (
A("migrateur").n('p').realize()   
    ) == 'migrateurs',\
    'A("migrateur").n(\'p\')=>migrateurs'


def test_declension_fr_1434():
    assert (
N("milieu").g('m').n('p').realize()   
    ) == 'milieux',\
    'N("milieu").g(\'m\').n(\'p\')=>milieux'


def test_declension_fr_1435():
    assert (
A("militaire").n('p').realize()   
    ) == 'militaires',\
    'A("militaire").n(\'p\')=>militaires'


def test_declension_fr_1436():
    assert (
N("millier").g('m').n('p').realize()   
    ) == 'milliers',\
    'N("millier").g(\'m\').n(\'p\')=>milliers'


def test_declension_fr_1437():
    assert (
N("million").g('m').n('p').realize()   
    ) == 'millions',\
    'N("million").g(\'m\').n(\'p\')=>millions'


def test_declension_fr_1438():
    assert (
A("mince").n('p').realize()   
    ) == 'minces',\
    'A("mince").n(\'p\')=>minces'


def test_declension_fr_1439():
    assert (
N("mine").g('f').n('p').realize()   
    ) == 'mines',\
    'N("mine").g(\'f\').n(\'p\')=>mines'


def test_declension_fr_1440():
    assert (
N("mineur").g('m').n('p').realize()   
    ) == 'mineurs',\
    'N("mineur").g(\'m\').n(\'p\')=>mineurs'


def test_declension_fr_1441():
    assert (
N("ministre").g('m').n('p').realize()   
    ) == 'ministres',\
    'N("ministre").g(\'m\').n(\'p\')=>ministres'


def test_declension_fr_1442():
    assert (
N("minuit").g('m').n('p').realize()   
    ) == 'minuits',\
    'N("minuit").g(\'m\').n(\'p\')=>minuits'


def test_declension_fr_1443():
    assert (
A("minuscule").n('p').realize()   
    ) == 'minuscules',\
    'A("minuscule").n(\'p\')=>minuscules'


def test_declension_fr_1444():
    assert (
N("minute").g('f').n('p').realize()   
    ) == 'minutes',\
    'N("minute").g(\'f\').n(\'p\')=>minutes'


def test_declension_fr_1445():
    assert (
N("miracle").g('m').n('p').realize()   
    ) == 'miracles',\
    'N("miracle").g(\'m\').n(\'p\')=>miracles'


def test_declension_fr_1446():
    assert (
N("miroir").g('m').n('p').realize()   
    ) == 'miroirs',\
    'N("miroir").g(\'m\').n(\'p\')=>miroirs'


def test_declension_fr_1447():
    assert (
A("misérable").n('p').realize()   
    ) == 'misérables',\
    'A("misérable").n(\'p\')=>misérables'


def test_declension_fr_1448():
    assert (
N("misère").g('f').n('p').realize()   
    ) == 'misères',\
    'N("misère").g(\'f\').n(\'p\')=>misères'


def test_declension_fr_1449():
    assert (
N("missel").g('m').n('p').realize()   
    ) == 'missels',\
    'N("missel").g(\'m\').n(\'p\')=>missels'


def test_declension_fr_1450():
    assert (
N("mission").g('f').n('p').realize()   
    ) == 'missions',\
    'N("mission").g(\'f\').n(\'p\')=>missions'


def test_declension_fr_1451():
    assert (
N("missionnaire").n('p').realize()   
    ) == 'missionnaires',\
    'N("missionnaire").n(\'p\')=>missionnaires'


def test_declension_fr_1452():
    assert (
A("mobile").n('p').realize()   
    ) == 'mobiles',\
    'A("mobile").n(\'p\')=>mobiles'


def test_declension_fr_1453():
    assert (
N("mobilier").g('m').n('p').realize()   
    ) == 'mobiliers',\
    'N("mobilier").g(\'m\').n(\'p\')=>mobiliers'


def test_declension_fr_1454():
    assert (
N("mode").g('f').n('p').realize()   
    ) == 'modes',\
    'N("mode").g(\'f\').n(\'p\')=>modes'


def test_declension_fr_1455():
    assert (
N("modèle").g('m').n('p').realize()   
    ) == 'modèles',\
    'N("modèle").g(\'m\').n(\'p\')=>modèles'


def test_declension_fr_1456():
    assert (
A("moderne").n('p').realize()   
    ) == 'modernes',\
    'A("moderne").n(\'p\')=>modernes'


def test_declension_fr_1457():
    assert (
A("modeste").n('p').realize()   
    ) == 'modestes',\
    'A("modeste").n(\'p\')=>modestes'


def test_declension_fr_1458():
    assert (
N("modestie").g('f').n('p').realize()   
    ) == 'modesties',\
    'N("modestie").g(\'f\').n(\'p\')=>modesties'


def test_declension_fr_1459():
    assert (
A("moelleux").n('p').realize()   
    ) == 'moelleux',\
    'A("moelleux").n(\'p\')=>moelleux'


def test_declension_fr_1460():
    assert (
A("moindre").n('p').realize()   
    ) == 'moindres',\
    'A("moindre").n(\'p\')=>moindres'


def test_declension_fr_1461():
    assert (
N("moine").g('m').n('p').realize()   
    ) == 'moines',\
    'N("moine").g(\'m\').n(\'p\')=>moines'


def test_declension_fr_1462():
    assert (
N("moineau").g('m').n('p').realize()   
    ) == 'moineaux',\
    'N("moineau").g(\'m\').n(\'p\')=>moineaux'


def test_declension_fr_1463():
    assert (
N("mois").g('m').n('p').realize()   
    ) == 'mois',\
    'N("mois").g(\'m\').n(\'p\')=>mois'


def test_declension_fr_1464():
    assert (
N("moisson").g('f').n('p').realize()   
    ) == 'moissons',\
    'N("moisson").g(\'f\').n(\'p\')=>moissons'


def test_declension_fr_1465():
    assert (
N("moissonneur").g('m').n('p').realize()   
    ) == 'moissonneurs',\
    'N("moissonneur").g(\'m\').n(\'p\')=>moissonneurs'


def test_declension_fr_1466():
    assert (
N("moitié").g('f').n('p').realize()   
    ) == 'moitiés',\
    'N("moitié").g(\'f\').n(\'p\')=>moitiés'


def test_declension_fr_1467():
    assert (
N("moment").g('m').n('p').realize()   
    ) == 'moments',\
    'N("moment").g(\'m\').n(\'p\')=>moments'


def test_declension_fr_1468():
    assert (
N("monde").g('m').n('p').realize()   
    ) == 'mondes',\
    'N("monde").g(\'m\').n(\'p\')=>mondes'


def test_declension_fr_1469():
    assert (
N("monnaie").g('f').n('p').realize()   
    ) == 'monnaies',\
    'N("monnaie").g(\'f\').n(\'p\')=>monnaies'


def test_declension_fr_1470():
    assert (
A("monotone").n('p').realize()   
    ) == 'monotones',\
    'A("monotone").n(\'p\')=>monotones'


def test_declension_fr_1471():
    assert (
N("monseigneur").g('m').n('p').realize()   
    ) == 'messeigneurs',\
    'N("monseigneur").g(\'m\').n(\'p\')=>messeigneurs'


def test_declension_fr_1472():
    assert (
N("monstre").g('m').n('p').realize()   
    ) == 'monstres',\
    'N("monstre").g(\'m\').n(\'p\')=>monstres'


def test_declension_fr_1473():
    assert (
N("mont").g('m').n('p').realize()   
    ) == 'monts',\
    'N("mont").g(\'m\').n(\'p\')=>monts'


def test_declension_fr_1474():
    assert (
N("montagne").g('f').n('p').realize()   
    ) == 'montagnes',\
    'N("montagne").g(\'f\').n(\'p\')=>montagnes'


def test_declension_fr_1475():
    assert (
N("montant").g('m').n('p').realize()   
    ) == 'montants',\
    'N("montant").g(\'m\').n(\'p\')=>montants'


def test_declension_fr_1476():
    assert (
N("montre").g('f').n('p').realize()   
    ) == 'montres',\
    'N("montre").g(\'f\').n(\'p\')=>montres'


def test_declension_fr_1477():
    assert (
N("monument").g('m').n('p').realize()   
    ) == 'monuments',\
    'N("monument").g(\'m\').n(\'p\')=>monuments'


def test_declension_fr_1478():
    assert (
A("moqueur").n('p').realize()   
    ) == 'moqueurs',\
    'A("moqueur").n(\'p\')=>moqueurs'


def test_declension_fr_1479():
    assert (
N("moral").g('m').n('p').realize()   
    ) == 'moraux',\
    'N("moral").g(\'m\').n(\'p\')=>moraux'


def test_declension_fr_1480():
    assert (
N("morale").g('f').n('p').realize()   
    ) == 'morales',\
    'N("morale").g(\'f\').n(\'p\')=>morales'


def test_declension_fr_1481():
    assert (
N("morceau").g('m').n('p').realize()   
    ) == 'morceaux',\
    'N("morceau").g(\'m\').n(\'p\')=>morceaux'


def test_declension_fr_1482():
    assert (
A("morne").n('p').realize()   
    ) == 'mornes',\
    'A("morne").n(\'p\')=>mornes'


def test_declension_fr_1483():
    assert (
A("mort").g('m').n('p').realize()   
    ) == 'morts',\
    'A("mort").g(\'m\').n(\'p\')=>morts'


def test_declension_fr_1484():
    assert (
A("mortel").n('p').realize()   
    ) == 'mortels',\
    'A("mortel").n(\'p\')=>mortels'


def test_declension_fr_1485():
    assert (
N("mot").g('m').n('p').realize()   
    ) == 'mots',\
    'N("mot").g(\'m\').n(\'p\')=>mots'


def test_declension_fr_1486():
    assert (
N("moteur").g('m').n('p').realize()   
    ) == 'moteurs',\
    'N("moteur").g(\'m\').n(\'p\')=>moteurs'


def test_declension_fr_1487():
    assert (
N("motif").g('m').n('p').realize()   
    ) == 'motifs',\
    'N("motif").g(\'m\').n(\'p\')=>motifs'


def test_declension_fr_1488():
    assert (
A("mou").n('p').realize()   
    ) == 'mous',\
    'A("mou").n(\'p\')=>mous'


def test_declension_fr_1489():
    assert (
N("mouche").g('f').n('p').realize()   
    ) == 'mouches',\
    'N("mouche").g(\'f\').n(\'p\')=>mouches'


def test_declension_fr_1490():
    assert (
N("mouchoir").g('m').n('p').realize()   
    ) == 'mouchoirs',\
    'N("mouchoir").g(\'m\').n(\'p\')=>mouchoirs'


def test_declension_fr_1491():
    assert (
N("moulin").g('m').n('p').realize()   
    ) == 'moulins',\
    'N("moulin").g(\'m\').n(\'p\')=>moulins'


def test_declension_fr_1492():
    assert (
N("mousse").g('f').n('p').realize()   
    ) == 'mousses',\
    'N("mousse").g(\'f\').n(\'p\')=>mousses'


def test_declension_fr_1493():
    assert (
N("moustache").g('f').n('p').realize()   
    ) == 'moustaches',\
    'N("moustache").g(\'f\').n(\'p\')=>moustaches'


def test_declension_fr_1494():
    assert (
N("mouton").g('m').n('p').realize()   
    ) == 'moutons',\
    'N("mouton").g(\'m\').n(\'p\')=>moutons'


def test_declension_fr_1495():
    assert (
N("mouvement").g('m').n('p').realize()   
    ) == 'mouvements',\
    'N("mouvement").g(\'m\').n(\'p\')=>mouvements'


def test_declension_fr_1496():
    assert (
A("moyen").n('p').realize()   
    ) == 'moyens',\
    'A("moyen").n(\'p\')=>moyens'


def test_declension_fr_1497():
    assert (
N("moyenne").g('f').n('p').realize()   
    ) == 'moyennes',\
    'N("moyenne").g(\'f\').n(\'p\')=>moyennes'


def test_declension_fr_1498():
    assert (
A("muet").n('p').realize()   
    ) == 'muets',\
    'A("muet").n(\'p\')=>muets'


def test_declension_fr_1499():
    assert (
N("muguet").g('m').n('p').realize()   
    ) == 'muguets',\
    'N("muguet").g(\'m\').n(\'p\')=>muguets'


def test_declension_fr_1500():
    assert (
A("multicolore").n('p').realize()   
    ) == 'multicolores',\
    'A("multicolore").n(\'p\')=>multicolores'


def test_declension_fr_1501():
    assert (
A("multiple").n('p').realize()   
    ) == 'multiples',\
    'A("multiple").n(\'p\')=>multiples'


def test_declension_fr_1502():
    assert (
N("multitude").g('f').n('p').realize()   
    ) == 'multitudes',\
    'N("multitude").g(\'f\').n(\'p\')=>multitudes'


def test_declension_fr_1503():
    assert (
N("mur").g('m').n('p').realize()   
    ) == 'murs',\
    'N("mur").g(\'m\').n(\'p\')=>murs'


def test_declension_fr_1504():
    assert (
A("mûr").n('p').realize()   
    ) == 'mûrs',\
    'A("mûr").n(\'p\')=>mûrs'


def test_declension_fr_1505():
    assert (
N("muraille").g('f').n('p').realize()   
    ) == 'murailles',\
    'N("muraille").g(\'f\').n(\'p\')=>murailles'


def test_declension_fr_1506():
    assert (
N("murmure").g('m').n('p').realize()   
    ) == 'murmures',\
    'N("murmure").g(\'m\').n(\'p\')=>murmures'


def test_declension_fr_1507():
    assert (
N("muscle").g('m').n('p').realize()   
    ) == 'muscles',\
    'N("muscle").g(\'m\').n(\'p\')=>muscles'


def test_declension_fr_1508():
    assert (
N("museau").g('m').n('p').realize()   
    ) == 'museaux',\
    'N("museau").g(\'m\').n(\'p\')=>museaux'


def test_declension_fr_1509():
    assert (
N("musée").g('m').n('p').realize()   
    ) == 'musées',\
    'N("musée").g(\'m\').n(\'p\')=>musées'


def test_declension_fr_1510():
    assert (
A("musicien").n('p').realize()   
    ) == 'musiciens',\
    'A("musicien").n(\'p\')=>musiciens'


def test_declension_fr_1511():
    assert (
N("musique").g('f').n('p').realize()   
    ) == 'musiques',\
    'N("musique").g(\'f\').n(\'p\')=>musiques'


def test_declension_fr_1512():
    assert (
N("myosotis").g('m').n('p').realize()   
    ) == 'myosotis',\
    'N("myosotis").g(\'m\').n(\'p\')=>myosotis'


def test_declension_fr_1513():
    assert (
N("mystère").g('m').n('p').realize()   
    ) == 'mystères',\
    'N("mystère").g(\'m\').n(\'p\')=>mystères'


def test_declension_fr_1514():
    assert (
A("mystérieux").n('p').realize()   
    ) == 'mystérieux',\
    'A("mystérieux").n(\'p\')=>mystérieux'


def test_declension_fr_1515():
    assert (
N("naissance").g('f').n('p').realize()   
    ) == 'naissances',\
    'N("naissance").g(\'f\').n(\'p\')=>naissances'


def test_declension_fr_1516():
    assert (
N("nappe").g('f').n('p').realize()   
    ) == 'nappes',\
    'N("nappe").g(\'f\').n(\'p\')=>nappes'


def test_declension_fr_1517():
    assert (
N("narcisse").g('m').n('p').realize()   
    ) == 'narcisses',\
    'N("narcisse").g(\'m\').n(\'p\')=>narcisses'


def test_declension_fr_1518():
    assert (
A("natal").n('p').realize()   
    ) == 'natals',\
    'A("natal").n(\'p\')=>natals'


def test_declension_fr_1519():
    assert (
N("nation").g('f').n('p').realize()   
    ) == 'nations',\
    'N("nation").g(\'f\').n(\'p\')=>nations'


def test_declension_fr_1520():
    assert (
A("national").n('p').realize()   
    ) == 'nationaux',\
    'A("national").n(\'p\')=>nationaux'


def test_declension_fr_1521():
    assert (
N("nature").g('f').n('p').realize()   
    ) == 'natures',\
    'N("nature").g(\'f\').n(\'p\')=>natures'


def test_declension_fr_1522():
    assert (
A("naturel").n('p').realize()   
    ) == 'naturels',\
    'A("naturel").n(\'p\')=>naturels'


def test_declension_fr_1523():
    assert (
N("naufrage").g('m').n('p').realize()   
    ) == 'naufrages',\
    'N("naufrage").g(\'m\').n(\'p\')=>naufrages'


def test_declension_fr_1524():
    assert (
N("navire").g('m').n('p').realize()   
    ) == 'navires',\
    'N("navire").g(\'m\').n(\'p\')=>navires'


def test_declension_fr_1525():
    assert (
A("nécessaire").n('p').realize()   
    ) == 'nécessaires',\
    'A("nécessaire").n(\'p\')=>nécessaires'


def test_declension_fr_1526():
    assert (
N("négligence").g('f').n('p').realize()   
    ) == 'négligences',\
    'N("négligence").g(\'f\').n(\'p\')=>négligences'


def test_declension_fr_1527():
    assert (
A("négligent").n('p').realize()   
    ) == 'négligents',\
    'A("négligent").n(\'p\')=>négligents'


def test_declension_fr_1528():
    assert (
N("négociant").g('m').n('p').realize()   
    ) == 'négociants',\
    'N("négociant").g(\'m\').n(\'p\')=>négociants'


def test_declension_fr_1529():
    assert (
A("nègre").n('p').realize()   
    ) == 'nègres',\
    'A("nègre").n(\'p\')=>nègres'


def test_declension_fr_1530():
    assert (
N("neige").g('f').n('p').realize()   
    ) == 'neiges',\
    'N("neige").g(\'f\').n(\'p\')=>neiges'


def test_declension_fr_1531():
    assert (
A("nerveux").n('p').realize()   
    ) == 'nerveux',\
    'A("nerveux").n(\'p\')=>nerveux'


def test_declension_fr_1532():
    assert (
A("net").n('p').realize()   
    ) == 'nets',\
    'A("net").n(\'p\')=>nets'


def test_declension_fr_1533():
    assert (
A("neuf").g('f').n('s').realize()   
    ) == 'neuve',\
    'A("neuf").g(\'f\').n(\'s\')=>neuve'


def test_declension_fr_1534():
    assert (
N("neveu").g('m').n('p').realize()   
    ) == 'neveux',\
    'N("neveu").g(\'m\').n(\'p\')=>neveux'


def test_declension_fr_1535():
    assert (
N("nez").g('m').n('p').realize()   
    ) == 'nez',\
    'N("nez").g(\'m\').n(\'p\')=>nez'


def test_declension_fr_1536():
    assert (
N("niche").g('f').n('p').realize()   
    ) == 'niches',\
    'N("niche").g(\'f\').n(\'p\')=>niches'


def test_declension_fr_1537():
    assert (
N("nid").g('m').n('p').realize()   
    ) == 'nids',\
    'N("nid").g(\'m\').n(\'p\')=>nids'


def test_declension_fr_1538():
    assert (
N("nièce").g('f').n('p').realize()   
    ) == 'nièces',\
    'N("nièce").g(\'f\').n(\'p\')=>nièces'


def test_declension_fr_1539():
    assert (
N("niveau").g('m').n('p').realize()   
    ) == 'niveaux',\
    'N("niveau").g(\'m\').n(\'p\')=>niveaux'


def test_declension_fr_1540():
    assert (
A("noble").n('p').realize()   
    ) == 'nobles',\
    'A("noble").n(\'p\')=>nobles'


def test_declension_fr_1541():
    assert (
N("noeud").g('m').n('p').realize()   
    ) == 'noeuds',\
    'N("noeud").g(\'m\').n(\'p\')=>noeuds'


def test_declension_fr_1542():
    assert (
A("noir").n('p').realize()   
    ) == 'noirs',\
    'A("noir").n(\'p\')=>noirs'


def test_declension_fr_1543():
    assert (
N("noisette").g('f').n('p').realize()   
    ) == 'noisettes',\
    'N("noisette").g(\'f\').n(\'p\')=>noisettes'


def test_declension_fr_1544():
    assert (
N("noix").g('f').n('p').realize()   
    ) == 'noix',\
    'N("noix").g(\'f\').n(\'p\')=>noix'


def test_declension_fr_1545():
    assert (
N("nom").g('m').n('p').realize()   
    ) == 'noms',\
    'N("nom").g(\'m\').n(\'p\')=>noms'


def test_declension_fr_1546():
    assert (
N("nombre").g('m').n('p').realize()   
    ) == 'nombres',\
    'N("nombre").g(\'m\').n(\'p\')=>nombres'


def test_declension_fr_1547():
    assert (
A("nombreux").n('p').realize()   
    ) == 'nombreux',\
    'A("nombreux").n(\'p\')=>nombreux'


def test_declension_fr_1548():
    assert (
A("normal").n('p').realize()   
    ) == 'normaux',\
    'A("normal").n(\'p\')=>normaux'


def test_declension_fr_1549():
    assert (
N("notaire").g('m').n('p').realize()   
    ) == 'notaires',\
    'N("notaire").g(\'m\').n(\'p\')=>notaires'


def test_declension_fr_1550():
    assert (
N("note").g('f').n('p').realize()   
    ) == 'notes',\
    'N("note").g(\'f\').n(\'p\')=>notes'


def test_declension_fr_1551():
    assert (
N("nourriture").g('f').n('p').realize()   
    ) == 'nourritures',\
    'N("nourriture").g(\'f\').n(\'p\')=>nourritures'


def test_declension_fr_1552():
    assert (
A("nouveau").n('p').realize()   
    ) == 'nouveaux',\
    'A("nouveau").n(\'p\')=>nouveaux'


def test_declension_fr_1553():
    assert (
N("novembre").g('m').n('p').realize()   
    ) == 'novembres',\
    'N("novembre").g(\'m\').n(\'p\')=>novembres'


def test_declension_fr_1554():
    assert (
A("nu").n('p').realize()   
    ) == 'nus',\
    'A("nu").n(\'p\')=>nus'


def test_declension_fr_1555():
    assert (
N("nuage").g('m').n('p').realize()   
    ) == 'nuages',\
    'N("nuage").g(\'m\').n(\'p\')=>nuages'


def test_declension_fr_1556():
    assert (
A("nuisible").n('p').realize()   
    ) == 'nuisibles',\
    'A("nuisible").n(\'p\')=>nuisibles'


def test_declension_fr_1557():
    assert (
N("nuit").g('f').n('p').realize()   
    ) == 'nuits',\
    'N("nuit").g(\'f\').n(\'p\')=>nuits'


def test_declension_fr_1558():
    assert (
N("numéro").g('m').n('p').realize()   
    ) == 'numéros',\
    'N("numéro").g(\'m\').n(\'p\')=>numéros'


def test_declension_fr_1559():
    assert (
A("obéissant").n('p').realize()   
    ) == 'obéissants',\
    'A("obéissant").n(\'p\')=>obéissants'


def test_declension_fr_1560():
    assert (
N("objet").g('m').n('p').realize()   
    ) == 'objets',\
    'N("objet").g(\'m\').n(\'p\')=>objets'


def test_declension_fr_1561():
    assert (
N("obligeance").g('f').n('p').realize()   
    ) == 'obligeances',\
    'N("obligeance").g(\'f\').n(\'p\')=>obligeances'


def test_declension_fr_1562():
    assert (
A("obscur").n('p').realize()   
    ) == 'obscurs',\
    'A("obscur").n(\'p\')=>obscurs'


def test_declension_fr_1563():
    assert (
N("obscurité").g('f').n('p').realize()   
    ) == 'obscurités',\
    'N("obscurité").g(\'f\').n(\'p\')=>obscurités'


def test_declension_fr_1564():
    assert (
N("observation").g('f').n('p').realize()   
    ) == 'observations',\
    'N("observation").g(\'f\').n(\'p\')=>observations'


def test_declension_fr_1565():
    assert (
N("obstacle").g('m').n('p').realize()   
    ) == 'obstacles',\
    'N("obstacle").g(\'m\').n(\'p\')=>obstacles'


def test_declension_fr_1566():
    assert (
N("occasion").g('f').n('p').realize()   
    ) == 'occasions',\
    'N("occasion").g(\'f\').n(\'p\')=>occasions'


def test_declension_fr_1567():
    assert (
N("occupation").g('f').n('p').realize()   
    ) == 'occupations',\
    'N("occupation").g(\'f\').n(\'p\')=>occupations'


def test_declension_fr_1568():
    assert (
N("océan").g('m').n('p').realize()   
    ) == 'océans',\
    'N("océan").g(\'m\').n(\'p\')=>océans'


def test_declension_fr_1569():
    assert (
N("octobre").g('m').n('p').realize()   
    ) == 'octobres',\
    'N("octobre").g(\'m\').n(\'p\')=>octobres'


def test_declension_fr_1570():
    assert (
N("odeur").g('f').n('p').realize()   
    ) == 'odeurs',\
    'N("odeur").g(\'f\').n(\'p\')=>odeurs'


def test_declension_fr_1571():
    assert (
A("odorant").n('p').realize()   
    ) == 'odorants',\
    'A("odorant").n(\'p\')=>odorants'


def test_declension_fr_1572():
    assert (
N("oeil").g('m').n('p').realize()   
    ) == 'yeux',\
    'N("oeil").g(\'m\').n(\'p\')=>yeux'


def test_declension_fr_1573():
    assert (
N("oeillet").g('m').n('p').realize()   
    ) == 'oeillets',\
    'N("oeillet").g(\'m\').n(\'p\')=>oeillets'


def test_declension_fr_1574():
    assert (
N("oeuf").g('m').n('p').realize()   
    ) == 'oeufs',\
    'N("oeuf").g(\'m\').n(\'p\')=>oeufs'


def test_declension_fr_1575():
    assert (
N("oeuvre").g('f').n('p').realize()   
    ) == 'oeuvres',\
    'N("oeuvre").g(\'f\').n(\'p\')=>oeuvres'


def test_declension_fr_1576():
    assert (
N("office").g('m').n('p').realize()   
    ) == 'offices',\
    'N("office").g(\'m\').n(\'p\')=>offices'


def test_declension_fr_1577():
    assert (
N("officier").g('m').n('p').realize()   
    ) == 'officiers',\
    'N("officier").g(\'m\').n(\'p\')=>officiers'


def test_declension_fr_1578():
    assert (
N("offre").g('f').n('p').realize()   
    ) == 'offres',\
    'N("offre").g(\'f\').n(\'p\')=>offres'


def test_declension_fr_1579():
    assert (
N("oie").g('f').n('p').realize()   
    ) == 'oies',\
    'N("oie").g(\'f\').n(\'p\')=>oies'


def test_declension_fr_1580():
    assert (
N("oiseau").g('m').n('p').realize()   
    ) == 'oiseaux',\
    'N("oiseau").g(\'m\').n(\'p\')=>oiseaux'


def test_declension_fr_1581():
    assert (
N("oisillon").g('m').n('p').realize()   
    ) == 'oisillons',\
    'N("oisillon").g(\'m\').n(\'p\')=>oisillons'


def test_declension_fr_1582():
    assert (
N("ombrage").g('m').n('p').realize()   
    ) == 'ombrages',\
    'N("ombrage").g(\'m\').n(\'p\')=>ombrages'


def test_declension_fr_1583():
    assert (
N("ombre").g('f').n('p').realize()   
    ) == 'ombres',\
    'N("ombre").g(\'f\').n(\'p\')=>ombres'


def test_declension_fr_1584():
    assert (
N("oncle").g('m').n('p').realize()   
    ) == 'oncles',\
    'N("oncle").g(\'m\').n(\'p\')=>oncles'


def test_declension_fr_1585():
    assert (
N("onde").g('f').n('p').realize()   
    ) == 'ondes',\
    'N("onde").g(\'f\').n(\'p\')=>ondes'


def test_declension_fr_1586():
    assert (
N("opération").g('f').n('p').realize()   
    ) == 'opérations',\
    'N("opération").g(\'f\').n(\'p\')=>opérations'


def test_declension_fr_1587():
    assert (
N("opinion").g('f').n('p').realize()   
    ) == 'opinions',\
    'N("opinion").g(\'f\').n(\'p\')=>opinions'


def test_declension_fr_1588():
    assert (
N("or").g('m').n('p').realize()   
    ) == 'ors',\
    'N("or").g(\'m\').n(\'p\')=>ors'


def test_declension_fr_1589():
    assert (
N("orage").g('m').n('p').realize()   
    ) == 'orages',\
    'N("orage").g(\'m\').n(\'p\')=>orages'


def test_declension_fr_1590():
    assert (
N("orange").g('f').n('s').realize()   
    ) == 'orange',\
    'N("orange").g(\'f\').n(\'s\')=>orange'


def test_declension_fr_1591():
    assert (
N("oranger").g('m').n('p').realize()   
    ) == 'orangers',\
    'N("oranger").g(\'m\').n(\'p\')=>orangers'


def test_declension_fr_1592():
    assert (
A("ordinaire").n('p').realize()   
    ) == 'ordinaires',\
    'A("ordinaire").n(\'p\')=>ordinaires'


def test_declension_fr_1593():
    assert (
N("ordre").g('m').n('p').realize()   
    ) == 'ordres',\
    'N("ordre").g(\'m\').n(\'p\')=>ordres'


def test_declension_fr_1594():
    assert (
N("orée").g('f').n('p').realize()   
    ) == 'orées',\
    'N("orée").g(\'f\').n(\'p\')=>orées'


def test_declension_fr_1595():
    assert (
N("oreille").g('f').n('p').realize()   
    ) == 'oreilles',\
    'N("oreille").g(\'f\').n(\'p\')=>oreilles'


def test_declension_fr_1596():
    assert (
N("orgueil").g('m').n('p').realize()   
    ) == 'orgueils',\
    'N("orgueil").g(\'m\').n(\'p\')=>orgueils'


def test_declension_fr_1597():
    assert (
A("orgueilleux").n('p').realize()   
    ) == 'orgueilleux',\
    'A("orgueilleux").n(\'p\')=>orgueilleux'


def test_declension_fr_1598():
    assert (
N("ornement").g('m').n('p').realize()   
    ) == 'ornements',\
    'N("ornement").g(\'m\').n(\'p\')=>ornements'


def test_declension_fr_1599():
    assert (
N("orphelin").g('m').n('p').realize()   
    ) == 'orphelins',\
    'N("orphelin").g(\'m\').n(\'p\')=>orphelins'


def test_declension_fr_1600():
    assert (
N("os").g('m').n('p').realize()   
    ) == 'os',\
    'N("os").g(\'m\').n(\'p\')=>os'


def test_declension_fr_1601():
    assert (
N("osier").g('m').n('p').realize()   
    ) == 'osiers',\
    'N("osier").g(\'m\').n(\'p\')=>osiers'


def test_declension_fr_1602():
    assert (
N("ouate").g('f').n('p').realize()   
    ) == 'ouates',\
    'N("ouate").g(\'f\').n(\'p\')=>ouates'


def test_declension_fr_1603():
    assert (
N("ours").g('m').n('p').realize()   
    ) == 'ours',\
    'N("ours").g(\'m\').n(\'p\')=>ours'


def test_declension_fr_1604():
    assert (
N("outil").g('m').n('p').realize()   
    ) == 'outils',\
    'N("outil").g(\'m\').n(\'p\')=>outils'


def test_declension_fr_1605():
    assert (
N("ouverture").g('f').n('p').realize()   
    ) == 'ouvertures',\
    'N("ouverture").g(\'f\').n(\'p\')=>ouvertures'


def test_declension_fr_1606():
    assert (
N("ouvrage").g('m').n('p').realize()   
    ) == 'ouvrages',\
    'N("ouvrage").g(\'m\').n(\'p\')=>ouvrages'


def test_declension_fr_1607():
    assert (
N("ouvrier").g('m').n('p').realize()   
    ) == 'ouvriers',\
    'N("ouvrier").g(\'m\').n(\'p\')=>ouvriers'


def test_declension_fr_1608():
    assert (
N("page").g('f').n('p').realize()   
    ) == 'pages',\
    'N("page").g(\'f\').n(\'p\')=>pages'


def test_declension_fr_1609():
    assert (
N("paille").g('f').n('p').realize()   
    ) == 'pailles',\
    'N("paille").g(\'f\').n(\'p\')=>pailles'


def test_declension_fr_1610():
    assert (
N("pain").g('m').n('p').realize()   
    ) == 'pains',\
    'N("pain").g(\'m\').n(\'p\')=>pains'


def test_declension_fr_1611():
    assert (
N("paire").g('f').n('p').realize()   
    ) == 'paires',\
    'N("paire").g(\'f\').n(\'p\')=>paires'


def test_declension_fr_1612():
    assert (
A("paisible").n('p').realize()   
    ) == 'paisibles',\
    'A("paisible").n(\'p\')=>paisibles'


def test_declension_fr_1613():
    assert (
N("paix").g('f').n('p').realize()   
    ) == 'paix',\
    'N("paix").g(\'f\').n(\'p\')=>paix'


def test_declension_fr_1614():
    assert (
N("palais").g('m').n('p').realize()   
    ) == 'palais',\
    'N("palais").g(\'m\').n(\'p\')=>palais'


def test_declension_fr_1615():
    assert (
A("pâle").n('p').realize()   
    ) == 'pâles',\
    'A("pâle").n(\'p\')=>pâles'


def test_declension_fr_1616():
    assert (
N("paletot").g('m').n('p').realize()   
    ) == 'paletots',\
    'N("paletot").g(\'m\').n(\'p\')=>paletots'


def test_declension_fr_1617():
    assert (
N("pan").g('m').n('p').realize()   
    ) == 'pans',\
    'N("pan").g(\'m\').n(\'p\')=>pans'


def test_declension_fr_1618():
    assert (
N("panache").g('m').n('p').realize()   
    ) == 'panaches',\
    'N("panache").g(\'m\').n(\'p\')=>panaches'


def test_declension_fr_1619():
    assert (
N("panier").g('m').n('p').realize()   
    ) == 'paniers',\
    'N("panier").g(\'m\').n(\'p\')=>paniers'


def test_declension_fr_1620():
    assert (
N("panorama").g('m').n('p').realize()   
    ) == 'panoramas',\
    'N("panorama").g(\'m\').n(\'p\')=>panoramas'


def test_declension_fr_1621():
    assert (
N("pantalon").g('m').n('p').realize()   
    ) == 'pantalons',\
    'N("pantalon").g(\'m\').n(\'p\')=>pantalons'


def test_declension_fr_1622():
    assert (
N("papa").g('m').n('p').realize()   
    ) == 'papas',\
    'N("papa").g(\'m\').n(\'p\')=>papas'


def test_declension_fr_1623():
    assert (
N("papier").g('m').n('p').realize()   
    ) == 'papiers',\
    'N("papier").g(\'m\').n(\'p\')=>papiers'


def test_declension_fr_1624():
    assert (
N("papillon").g('m').n('p').realize()   
    ) == 'papillons',\
    'N("papillon").g(\'m\').n(\'p\')=>papillons'


def test_declension_fr_1625():
    assert (
N("pâquerette").g('f').n('p').realize()   
    ) == 'pâquerettes',\
    'N("pâquerette").g(\'f\').n(\'p\')=>pâquerettes'


def test_declension_fr_1626():
    assert (
N("paquet").g('m').n('p').realize()   
    ) == 'paquets',\
    'N("paquet").g(\'m\').n(\'p\')=>paquets'


def test_declension_fr_1627():
    assert (
N("paradis").g('m').n('p').realize()   
    ) == 'paradis',\
    'N("paradis").g(\'m\').n(\'p\')=>paradis'


def test_declension_fr_1628():
    assert (
N("parapluie").g('m').n('p').realize()   
    ) == 'parapluies',\
    'N("parapluie").g(\'m\').n(\'p\')=>parapluies'


def test_declension_fr_1629():
    assert (
N("parc").g('m').n('p').realize()   
    ) == 'parcs',\
    'N("parc").g(\'m\').n(\'p\')=>parcs'


def test_declension_fr_1630():
    assert (
N("parcours").g('m').n('p').realize()   
    ) == 'parcours',\
    'N("parcours").g(\'m\').n(\'p\')=>parcours'


def test_declension_fr_1631():
    assert (
N("pardessus").g('m').n('p').realize()   
    ) == 'pardessus',\
    'N("pardessus").g(\'m\').n(\'p\')=>pardessus'


def test_declension_fr_1632():
    assert (
N("pardon").g('m').n('p').realize()   
    ) == 'pardons',\
    'N("pardon").g(\'m\').n(\'p\')=>pardons'


def test_declension_fr_1633():
    assert (
A("pareil").n('p').realize()   
    ) == 'pareils',\
    'A("pareil").n(\'p\')=>pareils'


def test_declension_fr_1634():
    assert (
N("parent").g('m').n('p').realize()   
    ) == 'parents',\
    'N("parent").g(\'m\').n(\'p\')=>parents'


def test_declension_fr_1635():
    assert (
N("paresse").g('f').n('p').realize()   
    ) == 'paresses',\
    'N("paresse").g(\'f\').n(\'p\')=>paresses'


def test_declension_fr_1636():
    assert (
A("paresseux").n('p').realize()   
    ) == 'paresseux',\
    'A("paresseux").n(\'p\')=>paresseux'


def test_declension_fr_1637():
    assert (
A("parfait").n('p').realize()   
    ) == 'parfaits',\
    'A("parfait").n(\'p\')=>parfaits'


def test_declension_fr_1638():
    assert (
N("parfum").g('m').n('p').realize()   
    ) == 'parfums',\
    'N("parfum").g(\'m\').n(\'p\')=>parfums'


def test_declension_fr_1639():
    assert (
N("paroisse").g('f').n('p').realize()   
    ) == 'paroisses',\
    'N("paroisse").g(\'f\').n(\'p\')=>paroisses'


def test_declension_fr_1640():
    assert (
N("parole").g('f').n('p').realize()   
    ) == 'paroles',\
    'N("parole").g(\'f\').n(\'p\')=>paroles'


def test_declension_fr_1641():
    assert (
N("parquet").g('m').n('p').realize()   
    ) == 'parquets',\
    'N("parquet").g(\'m\').n(\'p\')=>parquets'


def test_declension_fr_1642():
    assert (
N("parrain").g('m').n('p').realize()   
    ) == 'parrains',\
    'N("parrain").g(\'m\').n(\'p\')=>parrains'


def test_declension_fr_1643():
    assert (
N("part").g('f').n('p').realize()   
    ) == 'parts',\
    'N("part").g(\'f\').n(\'p\')=>parts'


def test_declension_fr_1644():
    assert (
N("parterre").g('m').n('p').realize()   
    ) == 'parterres',\
    'N("parterre").g(\'m\').n(\'p\')=>parterres'


def test_declension_fr_1645():
    assert (
N("parti").g('m').n('p').realize()   
    ) == 'partis',\
    'N("parti").g(\'m\').n(\'p\')=>partis'


def test_declension_fr_1646():
    assert (
A("particulier").n('p').realize()   
    ) == 'particuliers',\
    'A("particulier").n(\'p\')=>particuliers'


def test_declension_fr_1647():
    assert (
N("partie").g('f').n('p').realize()   
    ) == 'parties',\
    'N("partie").g(\'f\').n(\'p\')=>parties'


def test_declension_fr_1648():
    assert (
N("parure").g('f').n('p').realize()   
    ) == 'parures',\
    'N("parure").g(\'f\').n(\'p\')=>parures'


def test_declension_fr_1649():
    assert (
N("pas").g('m').n('p').realize()   
    ) == 'pas',\
    'N("pas").g(\'m\').n(\'p\')=>pas'


def test_declension_fr_1650():
    assert (
N("passage").g('m').n('p').realize()   
    ) == 'passages',\
    'N("passage").g(\'m\').n(\'p\')=>passages'


def test_declension_fr_1651():
    assert (
N("passager").g('m').n('p').realize()   
    ) == 'passagers',\
    'N("passager").g(\'m\').n(\'p\')=>passagers'


def test_declension_fr_1652():
    assert (
N("passant").g('m').n('p').realize()   
    ) == 'passants',\
    'N("passant").g(\'m\').n(\'p\')=>passants'


def test_declension_fr_1653():
    assert (
N("passé").g('m').n('p').realize()   
    ) == 'passés',\
    'N("passé").g(\'m\').n(\'p\')=>passés'


def test_declension_fr_1654():
    assert (
N("passion").g('f').n('p').realize()   
    ) == 'passions',\
    'N("passion").g(\'f\').n(\'p\')=>passions'


def test_declension_fr_1655():
    assert (
N("pâte").g('f').n('p').realize()   
    ) == 'pâtes',\
    'N("pâte").g(\'f\').n(\'p\')=>pâtes'


def test_declension_fr_1656():
    assert (
A("paternel").n('p').realize()   
    ) == 'paternels',\
    'A("paternel").n(\'p\')=>paternels'


def test_declension_fr_1657():
    assert (
N("patience").g('f').n('p').realize()   
    ) == 'patiences',\
    'N("patience").g(\'f\').n(\'p\')=>patiences'


def test_declension_fr_1658():
    assert (
N("patin").g('m').n('p').realize()   
    ) == 'patins',\
    'N("patin").g(\'m\').n(\'p\')=>patins'


def test_declension_fr_1659():
    assert (
N("pâtisserie").g('f').n('p').realize()   
    ) == 'pâtisseries',\
    'N("pâtisserie").g(\'f\').n(\'p\')=>pâtisseries'


def test_declension_fr_1660():
    assert (
N("pâtre").g('m').n('p').realize()   
    ) == 'pâtres',\
    'N("pâtre").g(\'m\').n(\'p\')=>pâtres'


def test_declension_fr_1661():
    assert (
N("patrie").g('f').n('p').realize()   
    ) == 'patries',\
    'N("patrie").g(\'f\').n(\'p\')=>patries'


def test_declension_fr_1662():
    assert (
N("patron").g('m').n('p').realize()   
    ) == 'patrons',\
    'N("patron").g(\'m\').n(\'p\')=>patrons'


def test_declension_fr_1663():
    assert (
N("patronage").g('m').n('p').realize()   
    ) == 'patronages',\
    'N("patronage").g(\'m\').n(\'p\')=>patronages'


def test_declension_fr_1664():
    assert (
N("patte").g('f').n('p').realize()   
    ) == 'pattes',\
    'N("patte").g(\'f\').n(\'p\')=>pattes'


def test_declension_fr_1665():
    assert (
N("pâture").g('f').n('p').realize()   
    ) == 'pâtures',\
    'N("pâture").g(\'f\').n(\'p\')=>pâtures'


def test_declension_fr_1666():
    assert (
A("pauvre").n('p').realize()   
    ) == 'pauvres',\
    'A("pauvre").n(\'p\')=>pauvres'


def test_declension_fr_1667():
    assert (
N("pavé").g('m').n('p').realize()   
    ) == 'pavés',\
    'N("pavé").g(\'m\').n(\'p\')=>pavés'


def test_declension_fr_1668():
    assert (
N("pays").g('m').n('p').realize()   
    ) == 'pays',\
    'N("pays").g(\'m\').n(\'p\')=>pays'


def test_declension_fr_1669():
    assert (
N("paysage").g('m').n('p').realize()   
    ) == 'paysages',\
    'N("paysage").g(\'m\').n(\'p\')=>paysages'


def test_declension_fr_1670():
    assert (
N("paysan").g('m').n('p').realize()   
    ) == 'paysans',\
    'N("paysan").g(\'m\').n(\'p\')=>paysans'


def test_declension_fr_1671():
    assert (
N("peau").g('f').n('p').realize()   
    ) == 'peaux',\
    'N("peau").g(\'f\').n(\'p\')=>peaux'


def test_declension_fr_1672():
    assert (
N("péché").g('m').n('p').realize()   
    ) == 'péchés',\
    'N("péché").g(\'m\').n(\'p\')=>péchés'


def test_declension_fr_1673():
    assert (
N("pêche").g('f').n('p').realize()   
    ) == 'pêches',\
    'N("pêche").g(\'f\').n(\'p\')=>pêches'


def test_declension_fr_1674():
    assert (
N("pêcheur").g('m').n('p').realize()   
    ) == 'pêcheurs',\
    'N("pêcheur").g(\'m\').n(\'p\')=>pêcheurs'


def test_declension_fr_1675():
    assert (
N("peine").g('f').n('p').realize()   
    ) == 'peines',\
    'N("peine").g(\'f\').n(\'p\')=>peines'


def test_declension_fr_1676():
    assert (
N("peintre").g('m').n('p').realize()   
    ) == 'peintres',\
    'N("peintre").g(\'m\').n(\'p\')=>peintres'


def test_declension_fr_1677():
    assert (
N("peinture").g('f').n('p').realize()   
    ) == 'peintures',\
    'N("peinture").g(\'f\').n(\'p\')=>peintures'


def test_declension_fr_1678():
    assert (
N("pelage").g('m').n('p').realize()   
    ) == 'pelages',\
    'N("pelage").g(\'m\').n(\'p\')=>pelages'


def test_declension_fr_1679():
    assert (
N("pelouse").g('f').n('p').realize()   
    ) == 'pelouses',\
    'N("pelouse").g(\'f\').n(\'p\')=>pelouses'


def test_declension_fr_1680():
    assert (
N("pendule").g('m').n('p').realize()   
    ) == 'pendules',\
    'N("pendule").g(\'m\').n(\'p\')=>pendules'


def test_declension_fr_1681():
    assert (
A("pénible").n('p').realize()   
    ) == 'pénibles',\
    'A("pénible").n(\'p\')=>pénibles'


def test_declension_fr_1682():
    assert (
N("pénitence").g('f').n('p').realize()   
    ) == 'pénitences',\
    'N("pénitence").g(\'f\').n(\'p\')=>pénitences'


def test_declension_fr_1683():
    assert (
N("pensée").g('f').n('p').realize()   
    ) == 'pensées',\
    'N("pensée").g(\'f\').n(\'p\')=>pensées'


def test_declension_fr_1684():
    assert (
N("pension").g('f').n('p').realize()   
    ) == 'pensions',\
    'N("pension").g(\'f\').n(\'p\')=>pensions'


def test_declension_fr_1685():
    assert (
N("pensionnaire").n('p').realize()   
    ) == 'pensionnaires',\
    'N("pensionnaire").n(\'p\')=>pensionnaires'


def test_declension_fr_1686():
    assert (
N("pensionnat").g('m').n('p').realize()   
    ) == 'pensionnats',\
    'N("pensionnat").g(\'m\').n(\'p\')=>pensionnats'


def test_declension_fr_1687():
    assert (
N("perche").g('f').n('p').realize()   
    ) == 'perches',\
    'N("perche").g(\'f\').n(\'p\')=>perches'


def test_declension_fr_1688():
    assert (
N("perdrix").g('f').n('p').realize()   
    ) == 'perdrix',\
    'N("perdrix").g(\'f\').n(\'p\')=>perdrix'


def test_declension_fr_1689():
    assert (
N("père").g('m').n('p').realize()   
    ) == 'pères',\
    'N("père").g(\'m\').n(\'p\')=>pères'


def test_declension_fr_1690():
    assert (
N("perfection").g('f').n('p').realize()   
    ) == 'perfections',\
    'N("perfection").g(\'f\').n(\'p\')=>perfections'


def test_declension_fr_1691():
    assert (
N("péril").g('m').n('p').realize()   
    ) == 'périls',\
    'N("péril").g(\'m\').n(\'p\')=>périls'


def test_declension_fr_1692():
    assert (
A("périlleux").n('p').realize()   
    ) == 'périlleux',\
    'A("périlleux").n(\'p\')=>périlleux'


def test_declension_fr_1693():
    assert (
N("période").g('f').n('p').realize()   
    ) == 'périodes',\
    'N("période").g(\'f\').n(\'p\')=>périodes'


def test_declension_fr_1694():
    assert (
N("perle").g('f').n('p').realize()   
    ) == 'perles',\
    'N("perle").g(\'f\').n(\'p\')=>perles'


def test_declension_fr_1695():
    assert (
N("permission").g('f').n('p').realize()   
    ) == 'permissions',\
    'N("permission").g(\'f\').n(\'p\')=>permissions'


def test_declension_fr_1696():
    assert (
A("perpétuel").n('p').realize()   
    ) == 'perpétuels',\
    'A("perpétuel").n(\'p\')=>perpétuels'


def test_declension_fr_1697():
    assert (
N("perroquet").g('m').n('p').realize()   
    ) == 'perroquets',\
    'N("perroquet").g(\'m\').n(\'p\')=>perroquets'


def test_declension_fr_1698():
    assert (
N("personnage").g('m').n('p').realize()   
    ) == 'personnages',\
    'N("personnage").g(\'m\').n(\'p\')=>personnages'


def test_declension_fr_1699():
    assert (
N("personne").g('f').n('p').realize()   
    ) == 'personnes',\
    'N("personne").g(\'f\').n(\'p\')=>personnes'


def test_declension_fr_1700():
    assert (
A("personnel").n('p').realize()   
    ) == 'personnels',\
    'A("personnel").n(\'p\')=>personnels'


def test_declension_fr_1701():
    assert (
N("perspective").g('f').n('p').realize()   
    ) == 'perspectives',\
    'N("perspective").g(\'f\').n(\'p\')=>perspectives'


def test_declension_fr_1702():
    assert (
N("perte").g('f').n('p').realize()   
    ) == 'pertes',\
    'N("perte").g(\'f\').n(\'p\')=>pertes'


def test_declension_fr_1703():
    assert (
N("pétale").g('m').n('p').realize()   
    ) == 'pétales',\
    'N("pétale").g(\'m\').n(\'p\')=>pétales'


def test_declension_fr_1704():
    assert (
A("petit").n('p').realize()   
    ) == 'petits',\
    'A("petit").n(\'p\')=>petits'


def test_declension_fr_1705():
    assert (
N("petit").g('m').n('p').realize()   
    ) == 'petits',\
    'N("petit").g(\'m\').n(\'p\')=>petits'


def test_declension_fr_1706():
    assert (
N("peuple").g('m').n('p').realize()   
    ) == 'peuples',\
    'N("peuple").g(\'m\').n(\'p\')=>peuples'


def test_declension_fr_1707():
    assert (
N("peuplier").g('m').n('p').realize()   
    ) == 'peupliers',\
    'N("peuplier").g(\'m\').n(\'p\')=>peupliers'


def test_declension_fr_1708():
    assert (
N("peur").g('f').n('p').realize()   
    ) == 'peurs',\
    'N("peur").g(\'f\').n(\'p\')=>peurs'


def test_declension_fr_1709():
    assert (
N("photographie").g('f').n('p').realize()   
    ) == 'photographies',\
    'N("photographie").g(\'f\').n(\'p\')=>photographies'


def test_declension_fr_1710():
    assert (
N("phrase").g('f').n('p').realize()   
    ) == 'phrases',\
    'N("phrase").g(\'f\').n(\'p\')=>phrases'


def test_declension_fr_1711():
    assert (
A("physique").n('p').realize()   
    ) == 'physiques',\
    'A("physique").n(\'p\')=>physiques'


def test_declension_fr_1712():
    assert (
N("piano").g('m').n('p').realize()   
    ) == 'pianos',\
    'N("piano").g(\'m\').n(\'p\')=>pianos'


def test_declension_fr_1713():
    assert (
N("pic").g('m').n('p').realize()   
    ) == 'pics',\
    'N("pic").g(\'m\').n(\'p\')=>pics'


def test_declension_fr_1714():
    assert (
N("pie").g('f').n('p').realize()   
    ) == 'pies',\
    'N("pie").g(\'f\').n(\'p\')=>pies'


def test_declension_fr_1715():
    assert (
N("pièce").g('f').n('p').realize()   
    ) == 'pièces',\
    'N("pièce").g(\'f\').n(\'p\')=>pièces'


def test_declension_fr_1716():
    assert (
N("pied").g('m').n('p').realize()   
    ) == 'pieds',\
    'N("pied").g(\'m\').n(\'p\')=>pieds'


def test_declension_fr_1717():
    assert (
N("pierre").g('f').n('p').realize()   
    ) == 'pierres',\
    'N("pierre").g(\'f\').n(\'p\')=>pierres'


def test_declension_fr_1718():
    assert (
N("piété").g('f').n('p').realize()   
    ) == 'piétés',\
    'N("piété").g(\'f\').n(\'p\')=>piétés'


def test_declension_fr_1719():
    assert (
A("pieux").n('p').realize()   
    ) == 'pieux',\
    'A("pieux").n(\'p\')=>pieux'


def test_declension_fr_1720():
    assert (
N("pigeon").g('m').n('p').realize()   
    ) == 'pigeons',\
    'N("pigeon").g(\'m\').n(\'p\')=>pigeons'


def test_declension_fr_1721():
    assert (
N("pin").g('m').n('p').realize()   
    ) == 'pins',\
    'N("pin").g(\'m\').n(\'p\')=>pins'


def test_declension_fr_1722():
    assert (
N("pinceau").g('m').n('p').realize()   
    ) == 'pinceaux',\
    'N("pinceau").g(\'m\').n(\'p\')=>pinceaux'


def test_declension_fr_1723():
    assert (
N("pinson").g('m').n('p').realize()   
    ) == 'pinsons',\
    'N("pinson").g(\'m\').n(\'p\')=>pinsons'


def test_declension_fr_1724():
    assert (
N("pipe").g('f').n('p').realize()   
    ) == 'pipes',\
    'N("pipe").g(\'f\').n(\'p\')=>pipes'


def test_declension_fr_1725():
    assert (
N("piste").g('f').n('p').realize()   
    ) == 'pistes',\
    'N("piste").g(\'f\').n(\'p\')=>pistes'


def test_declension_fr_1726():
    assert (
N("pitié").g('f').n('p').realize()   
    ) == 'pitiés',\
    'N("pitié").g(\'f\').n(\'p\')=>pitiés'


def test_declension_fr_1727():
    assert (
A("pittoresque").n('p').realize()   
    ) == 'pittoresques',\
    'A("pittoresque").n(\'p\')=>pittoresques'


def test_declension_fr_1728():
    assert (
N("place").g('f').n('p').realize()   
    ) == 'places',\
    'N("place").g(\'f\').n(\'p\')=>places'


def test_declension_fr_1729():
    assert (
N("plafond").g('m').n('p').realize()   
    ) == 'plafonds',\
    'N("plafond").g(\'m\').n(\'p\')=>plafonds'


def test_declension_fr_1730():
    assert (
N("plage").g('f').n('p').realize()   
    ) == 'plages',\
    'N("plage").g(\'f\').n(\'p\')=>plages'


def test_declension_fr_1731():
    assert (
N("plaie").g('f').n('p').realize()   
    ) == 'plaies',\
    'N("plaie").g(\'f\').n(\'p\')=>plaies'


def test_declension_fr_1732():
    assert (
N("plaine").g('f').n('p').realize()   
    ) == 'plaines',\
    'N("plaine").g(\'f\').n(\'p\')=>plaines'


def test_declension_fr_1733():
    assert (
N("plainte").g('f').n('p').realize()   
    ) == 'plaintes',\
    'N("plainte").g(\'f\').n(\'p\')=>plaintes'


def test_declension_fr_1734():
    assert (
A("plaintif").n('p').realize()   
    ) == 'plaintifs',\
    'A("plaintif").n(\'p\')=>plaintifs'


def test_declension_fr_1735():
    assert (
N("plaisir").g('m').n('p').realize()   
    ) == 'plaisirs',\
    'N("plaisir").g(\'m\').n(\'p\')=>plaisirs'


def test_declension_fr_1736():
    assert (
N("plan").g('m').n('p').realize()   
    ) == 'plans',\
    'N("plan").g(\'m\').n(\'p\')=>plans'


def test_declension_fr_1737():
    assert (
N("planche").g('f').n('p').realize()   
    ) == 'planches',\
    'N("planche").g(\'f\').n(\'p\')=>planches'


def test_declension_fr_1738():
    assert (
N("plancher").g('m').n('p').realize()   
    ) == 'planchers',\
    'N("plancher").g(\'m\').n(\'p\')=>planchers'


def test_declension_fr_1739():
    assert (
N("plane").g('f').n('p').realize()   
    ) == 'planes',\
    'N("plane").g(\'f\').n(\'p\')=>planes'


def test_declension_fr_1740():
    assert (
N("plante").g('f').n('p').realize()   
    ) == 'plantes',\
    'N("plante").g(\'f\').n(\'p\')=>plantes'


def test_declension_fr_1741():
    assert (
N("plaque").g('f').n('p').realize()   
    ) == 'plaques',\
    'N("plaque").g(\'f\').n(\'p\')=>plaques'


def test_declension_fr_1742():
    assert (
N("plat").g('m').n('p').realize()   
    ) == 'plats',\
    'N("plat").g(\'m\').n(\'p\')=>plats'


def test_declension_fr_1743():
    assert (
N("plate").g('f').n('p').realize()   
    ) == 'plates',\
    'N("plate").g(\'f\').n(\'p\')=>plates'


def test_declension_fr_1744():
    assert (
N("plateau").g('m').n('p').realize()   
    ) == 'plateaux',\
    'N("plateau").g(\'m\').n(\'p\')=>plateaux'


def test_declension_fr_1745():
    assert (
A("plein").n('p').realize()   
    ) == 'pleins',\
    'A("plein").n(\'p\')=>pleins'


def test_declension_fr_1746():
    assert (
N("pleur").g('m').n('p').realize()   
    ) == 'pleurs',\
    'N("pleur").g(\'m\').n(\'p\')=>pleurs'


def test_declension_fr_1747():
    assert (
N("pli").g('m').n('p').realize()   
    ) == 'plis',\
    'N("pli").g(\'m\').n(\'p\')=>plis'


def test_declension_fr_1748():
    assert (
N("plomb").g('m').n('p').realize()   
    ) == 'plombs',\
    'N("plomb").g(\'m\').n(\'p\')=>plombs'


def test_declension_fr_1749():
    assert (
N("pluie").g('f').n('p').realize()   
    ) == 'pluies',\
    'N("pluie").g(\'f\').n(\'p\')=>pluies'


def test_declension_fr_1750():
    assert (
N("plumage").g('m').n('p').realize()   
    ) == 'plumages',\
    'N("plumage").g(\'m\').n(\'p\')=>plumages'


def test_declension_fr_1751():
    assert (
N("plume").g('f').n('p').realize()   
    ) == 'plumes',\
    'N("plume").g(\'f\').n(\'p\')=>plumes'


def test_declension_fr_1752():
    assert (
N("plumier").g('m').n('p').realize()   
    ) == 'plumiers',\
    'N("plumier").g(\'m\').n(\'p\')=>plumiers'


def test_declension_fr_1753():
    assert (
N("poche").g('f').n('p').realize()   
    ) == 'poches',\
    'N("poche").g(\'f\').n(\'p\')=>poches'


def test_declension_fr_1754():
    assert (
N("poêle").g('f').n('p').realize()   
    ) == 'poêles',\
    'N("poêle").g(\'f\').n(\'p\')=>poêles'


def test_declension_fr_1755():
    assert (
N("poésie").g('f').n('p').realize()   
    ) == 'poésies',\
    'N("poésie").g(\'f\').n(\'p\')=>poésies'


def test_declension_fr_1756():
    assert (
N("poète").g('m').n('p').realize()   
    ) == 'poètes',\
    'N("poète").g(\'m\').n(\'p\')=>poètes'


def test_declension_fr_1757():
    assert (
N("poids").g('m').n('p').realize()   
    ) == 'poids',\
    'N("poids").g(\'m\').n(\'p\')=>poids'


def test_declension_fr_1758():
    assert (
N("poignée").g('f').n('p').realize()   
    ) == 'poignées',\
    'N("poignée").g(\'f\').n(\'p\')=>poignées'


def test_declension_fr_1759():
    assert (
N("poil").g('m').n('p').realize()   
    ) == 'poils',\
    'N("poil").g(\'m\').n(\'p\')=>poils'


def test_declension_fr_1760():
    assert (
N("poing").g('m').n('p').realize()   
    ) == 'poings',\
    'N("poing").g(\'m\').n(\'p\')=>poings'


def test_declension_fr_1761():
    assert (
N("point").g('m').n('p').realize()   
    ) == 'points',\
    'N("point").g(\'m\').n(\'p\')=>points'


def test_declension_fr_1762():
    assert (
N("pointe").g('f').n('p').realize()   
    ) == 'pointes',\
    'N("pointe").g(\'f\').n(\'p\')=>pointes'


def test_declension_fr_1763():
    assert (
A("pointu").n('p').realize()   
    ) == 'pointus',\
    'A("pointu").n(\'p\')=>pointus'


def test_declension_fr_1764():
    assert (
N("poire").g('f').n('p').realize()   
    ) == 'poires',\
    'N("poire").g(\'f\').n(\'p\')=>poires'


def test_declension_fr_1765():
    assert (
N("poireau").g('m').n('p').realize()   
    ) == 'poireaux',\
    'N("poireau").g(\'m\').n(\'p\')=>poireaux'


def test_declension_fr_1766():
    assert (
N("poirier").g('m').n('p').realize()   
    ) == 'poiriers',\
    'N("poirier").g(\'m\').n(\'p\')=>poiriers'


def test_declension_fr_1767():
    assert (
N("pois").g('m').n('p').realize()   
    ) == 'pois',\
    'N("pois").g(\'m\').n(\'p\')=>pois'


def test_declension_fr_1768():
    assert (
N("poisson").g('m').n('p').realize()   
    ) == 'poissons',\
    'N("poisson").g(\'m\').n(\'p\')=>poissons'


def test_declension_fr_1769():
    assert (
N("poitrine").g('f').n('p').realize()   
    ) == 'poitrines',\
    'N("poitrine").g(\'f\').n(\'p\')=>poitrines'


def test_declension_fr_1770():
    assert (
A("poli").n('p').realize()   
    ) == 'polis',\
    'A("poli").n(\'p\')=>polis'


def test_declension_fr_1771():
    assert (
N("police").g('f').n('p').realize()   
    ) == 'polices',\
    'N("police").g(\'f\').n(\'p\')=>polices'


def test_declension_fr_1772():
    assert (
N("politesse").g('f').n('p').realize()   
    ) == 'politesses',\
    'N("politesse").g(\'f\').n(\'p\')=>politesses'


def test_declension_fr_1773():
    assert (
N("politique").g('f').n('p').realize()   
    ) == 'politiques',\
    'N("politique").g(\'f\').n(\'p\')=>politiques'


def test_declension_fr_1774():
    assert (
N("pomme").g('f').n('p').realize()   
    ) == 'pommes',\
    'N("pomme").g(\'f\').n(\'p\')=>pommes'


def test_declension_fr_1775():
    assert (
N("pommier").g('m').n('p').realize()   
    ) == 'pommiers',\
    'N("pommier").g(\'m\').n(\'p\')=>pommiers'


def test_declension_fr_1776():
    assert (
N("pompe").g('f').n('p').realize()   
    ) == 'pompes',\
    'N("pompe").g(\'f\').n(\'p\')=>pompes'


def test_declension_fr_1777():
    assert (
N("pompier").g('m').n('p').realize()   
    ) == 'pompiers',\
    'N("pompier").g(\'m\').n(\'p\')=>pompiers'


def test_declension_fr_1778():
    assert (
N("pont").g('m').n('p').realize()   
    ) == 'ponts',\
    'N("pont").g(\'m\').n(\'p\')=>ponts'


def test_declension_fr_1779():
    assert (
N("porc").g('m').n('p').realize()   
    ) == 'porcs',\
    'N("porc").g(\'m\').n(\'p\')=>porcs'


def test_declension_fr_1780():
    assert (
N("port").g('m').n('p').realize()   
    ) == 'ports',\
    'N("port").g(\'m\').n(\'p\')=>ports'


def test_declension_fr_1781():
    assert (
N("porte").g('f').n('p').realize()   
    ) == 'portes',\
    'N("porte").g(\'f\').n(\'p\')=>portes'


def test_declension_fr_1782():
    assert (
N("portée").g('f').n('p').realize()   
    ) == 'portées',\
    'N("portée").g(\'f\').n(\'p\')=>portées'


def test_declension_fr_1783():
    assert (
N("portefeuille").g('m').n('p').realize()   
    ) == 'portefeuilles',\
    'N("portefeuille").g(\'m\').n(\'p\')=>portefeuilles'


def test_declension_fr_1784():
    assert (
N("porteur").g('m').n('p').realize()   
    ) == 'porteurs',\
    'N("porteur").g(\'m\').n(\'p\')=>porteurs'


def test_declension_fr_1785():
    assert (
N("portière").g('f').n('p').realize()   
    ) == 'portières',\
    'N("portière").g(\'f\').n(\'p\')=>portières'


def test_declension_fr_1786():
    assert (
N("portrait").g('m').n('p').realize()   
    ) == 'portraits',\
    'N("portrait").g(\'m\').n(\'p\')=>portraits'


def test_declension_fr_1787():
    assert (
N("position").g('f').n('p').realize()   
    ) == 'positions',\
    'N("position").g(\'f\').n(\'p\')=>positions'


def test_declension_fr_1788():
    assert (
N("possession").g('f').n('p').realize()   
    ) == 'possessions',\
    'N("possession").g(\'f\').n(\'p\')=>possessions'


def test_declension_fr_1789():
    assert (
A("possible").n('p').realize()   
    ) == 'possibles',\
    'A("possible").n(\'p\')=>possibles'


def test_declension_fr_1790():
    assert (
A("postal").n('p').realize()   
    ) == 'postaux',\
    'A("postal").n(\'p\')=>postaux'


def test_declension_fr_1791():
    assert (
N("poste").g('m').n('p').realize()   
    ) == 'postes',\
    'N("poste").g(\'m\').n(\'p\')=>postes'


def test_declension_fr_1792():
    assert (
N("pot").g('m').n('p').realize()   
    ) == 'pots',\
    'N("pot").g(\'m\').n(\'p\')=>pots'


def test_declension_fr_1793():
    assert (
N("potager").g('m').n('p').realize()   
    ) == 'potagers',\
    'N("potager").g(\'m\').n(\'p\')=>potagers'


def test_declension_fr_1794():
    assert (
N("poteau").g('m').n('p').realize()   
    ) == 'poteaux',\
    'N("poteau").g(\'m\').n(\'p\')=>poteaux'


def test_declension_fr_1795():
    assert (
N("poudre").g('f').n('p').realize()   
    ) == 'poudres',\
    'N("poudre").g(\'f\').n(\'p\')=>poudres'


def test_declension_fr_1796():
    assert (
N("poulailler").g('m').n('p').realize()   
    ) == 'poulaillers',\
    'N("poulailler").g(\'m\').n(\'p\')=>poulaillers'


def test_declension_fr_1797():
    assert (
N("poulain").g('m').n('p').realize()   
    ) == 'poulains',\
    'N("poulain").g(\'m\').n(\'p\')=>poulains'


def test_declension_fr_1798():
    assert (
N("poule").g('f').n('p').realize()   
    ) == 'poules',\
    'N("poule").g(\'f\').n(\'p\')=>poules'


def test_declension_fr_1799():
    assert (
N("poulet").g('m').n('p').realize()   
    ) == 'poulets',\
    'N("poulet").g(\'m\').n(\'p\')=>poulets'


def test_declension_fr_1800():
    assert (
N("poumon").g('m').n('p').realize()   
    ) == 'poumons',\
    'N("poumon").g(\'m\').n(\'p\')=>poumons'


def test_declension_fr_1801():
    assert (
N("poupée").g('f').n('p').realize()   
    ) == 'poupées',\
    'N("poupée").g(\'f\').n(\'p\')=>poupées'


def test_declension_fr_1802():
    assert (
A("pourpre").n('p').realize()   
    ) == 'pourpres',\
    'A("pourpre").n(\'p\')=>pourpres'


def test_declension_fr_1803():
    assert (
N("poursuite").g('f').n('p').realize()   
    ) == 'poursuites',\
    'N("poursuite").g(\'f\').n(\'p\')=>poursuites'


def test_declension_fr_1804():
    assert (
N("poussière").g('f').n('p').realize()   
    ) == 'poussières',\
    'N("poussière").g(\'f\').n(\'p\')=>poussières'


def test_declension_fr_1805():
    assert (
N("poussin").g('m').n('p').realize()   
    ) == 'poussins',\
    'N("poussin").g(\'m\').n(\'p\')=>poussins'


def test_declension_fr_1806():
    assert (
N("poutre").g('f').n('p').realize()   
    ) == 'poutres',\
    'N("poutre").g(\'f\').n(\'p\')=>poutres'


def test_declension_fr_1807():
    assert (
N("prairie").g('f').n('p').realize()   
    ) == 'prairies',\
    'N("prairie").g(\'f\').n(\'p\')=>prairies'


def test_declension_fr_1808():
    assert (
A("pratique").n('p').realize()   
    ) == 'pratiques',\
    'A("pratique").n(\'p\')=>pratiques'


def test_declension_fr_1809():
    assert (
N("pré").g('m').n('p').realize()   
    ) == 'prés',\
    'N("pré").g(\'m\').n(\'p\')=>prés'


def test_declension_fr_1810():
    assert (
N("préau").g('m').n('p').realize()   
    ) == 'préaux',\
    'N("préau").g(\'m\').n(\'p\')=>préaux'


def test_declension_fr_1811():
    assert (
N("précaution").g('f').n('p').realize()   
    ) == 'précautions',\
    'N("précaution").g(\'f\').n(\'p\')=>précautions'


def test_declension_fr_1812():
    assert (
A("précédent").n('p').realize()   
    ) == 'précédents',\
    'A("précédent").n(\'p\')=>précédents'


def test_declension_fr_1813():
    assert (
A("précieux").n('p').realize()   
    ) == 'précieux',\
    'A("précieux").n(\'p\')=>précieux'


def test_declension_fr_1814():
    assert (
N("préférence").g('f').n('p').realize()   
    ) == 'préférences',\
    'N("préférence").g(\'f\').n(\'p\')=>préférences'


def test_declension_fr_1815():
    assert (
A("premier").n('p').realize()   
    ) == 'premiers',\
    'A("premier").n(\'p\')=>premiers'


def test_declension_fr_1816():
    assert (
N("préparatif").g('m').n('p').realize()   
    ) == 'préparatifs',\
    'N("préparatif").g(\'m\').n(\'p\')=>préparatifs'


def test_declension_fr_1817():
    assert (
N("préparation").g('f').n('p').realize()   
    ) == 'préparations',\
    'N("préparation").g(\'f\').n(\'p\')=>préparations'


def test_declension_fr_1818():
    assert (
N("présence").g('f').n('p').realize()   
    ) == 'présences',\
    'N("présence").g(\'f\').n(\'p\')=>présences'


def test_declension_fr_1819():
    assert (
A("présent").n('p').realize()   
    ) == 'présents',\
    'A("présent").n(\'p\')=>présents'


def test_declension_fr_1820():
    assert (
N("président").g('m').n('p').realize()   
    ) == 'présidents',\
    'N("président").g(\'m\').n(\'p\')=>présidents'


def test_declension_fr_1821():
    assert (
N("présidente").g('f').n('p').realize()   
    ) == 'présidentes',\
    'N("présidente").g(\'f\').n(\'p\')=>présidentes'


def test_declension_fr_1822():
    assert (
A("prêt").n('p').realize()   
    ) == 'prêts',\
    'A("prêt").n(\'p\')=>prêts'


def test_declension_fr_1823():
    assert (
N("prêtre").g('m').n('p').realize()   
    ) == 'prêtres',\
    'N("prêtre").g(\'m\').n(\'p\')=>prêtres'


def test_declension_fr_1824():
    assert (
N("preuve").g('f').n('p').realize()   
    ) == 'preuves',\
    'N("preuve").g(\'f\').n(\'p\')=>preuves'


def test_declension_fr_1825():
    assert (
N("prière").g('f').n('p').realize()   
    ) == 'prières',\
    'N("prière").g(\'f\').n(\'p\')=>prières'


def test_declension_fr_1826():
    assert (
A("primaire").n('p').realize()   
    ) == 'primaires',\
    'A("primaire").n(\'p\')=>primaires'


def test_declension_fr_1827():
    assert (
N("prime").g('f').n('p').realize()   
    ) == 'primes',\
    'N("prime").g(\'f\').n(\'p\')=>primes'


def test_declension_fr_1828():
    assert (
N("primevère").g('f').n('p').realize()   
    ) == 'primevères',\
    'N("primevère").g(\'f\').n(\'p\')=>primevères'


def test_declension_fr_1829():
    assert (
N("prince").g('m').n('p').realize()   
    ) == 'princes',\
    'N("prince").g(\'m\').n(\'p\')=>princes'


def test_declension_fr_1830():
    assert (
N("princesse").g('f').n('p').realize()   
    ) == 'princesses',\
    'N("princesse").g(\'f\').n(\'p\')=>princesses'


def test_declension_fr_1831():
    assert (
A("principal").n('p').realize()   
    ) == 'principaux',\
    'A("principal").n(\'p\')=>principaux'


def test_declension_fr_1832():
    assert (
N("principe").g('m').n('p').realize()   
    ) == 'principes',\
    'N("principe").g(\'m\').n(\'p\')=>principes'


def test_declension_fr_1833():
    assert (
A("printanier").n('p').realize()   
    ) == 'printaniers',\
    'A("printanier").n(\'p\')=>printaniers'


def test_declension_fr_1834():
    assert (
N("printemps").g('m').n('p').realize()   
    ) == 'printemps',\
    'N("printemps").g(\'m\').n(\'p\')=>printemps'


def test_declension_fr_1835():
    assert (
N("prise").g('f').n('p').realize()   
    ) == 'prises',\
    'N("prise").g(\'f\').n(\'p\')=>prises'


def test_declension_fr_1836():
    assert (
N("prison").g('f').n('p').realize()   
    ) == 'prisons',\
    'N("prison").g(\'f\').n(\'p\')=>prisons'


def test_declension_fr_1837():
    assert (
N("prisonnier").g('m').n('p').realize()   
    ) == 'prisonniers',\
    'N("prisonnier").g(\'m\').n(\'p\')=>prisonniers'


def test_declension_fr_1838():
    assert (
N("privation").g('f').n('p').realize()   
    ) == 'privations',\
    'N("privation").g(\'f\').n(\'p\')=>privations'


def test_declension_fr_1839():
    assert (
N("prix").g('m').n('p').realize()   
    ) == 'prix',\
    'N("prix").g(\'m\').n(\'p\')=>prix'


def test_declension_fr_1840():
    assert (
N("problème").g('m').n('p').realize()   
    ) == 'problèmes',\
    'N("problème").g(\'m\').n(\'p\')=>problèmes'


def test_declension_fr_1841():
    assert (
N("procession").g('f').n('p').realize()   
    ) == 'processions',\
    'N("procession").g(\'f\').n(\'p\')=>processions'


def test_declension_fr_1842():
    assert (
A("prochain").n('p').realize()   
    ) == 'prochains',\
    'A("prochain").n(\'p\')=>prochains'


def test_declension_fr_1843():
    assert (
A("proche").n('p').realize()   
    ) == 'proches',\
    'A("proche").n(\'p\')=>proches'


def test_declension_fr_1844():
    assert (
N("procureur").g('m').n('p').realize()   
    ) == 'procureurs',\
    'N("procureur").g(\'m\').n(\'p\')=>procureurs'


def test_declension_fr_1845():
    assert (
A("prodigieux").n('p').realize()   
    ) == 'prodigieux',\
    'A("prodigieux").n(\'p\')=>prodigieux'


def test_declension_fr_1846():
    assert (
N("production").g('f').n('p').realize()   
    ) == 'productions',\
    'N("production").g(\'f\').n(\'p\')=>productions'


def test_declension_fr_1847():
    assert (
N("produit").g('m').n('p').realize()   
    ) == 'produits',\
    'N("produit").g(\'m\').n(\'p\')=>produits'


def test_declension_fr_1848():
    assert (
N("professeur").g('m').n('p').realize()   
    ) == 'professeurs',\
    'N("professeur").g(\'m\').n(\'p\')=>professeurs'


def test_declension_fr_1849():
    assert (
N("profession").g('f').n('p').realize()   
    ) == 'professions',\
    'N("profession").g(\'f\').n(\'p\')=>professions'


def test_declension_fr_1850():
    assert (
N("profit").g('m').n('p').realize()   
    ) == 'profits',\
    'N("profit").g(\'m\').n(\'p\')=>profits'


def test_declension_fr_1851():
    assert (
A("profond").n('p').realize()   
    ) == 'profonds',\
    'A("profond").n(\'p\')=>profonds'


def test_declension_fr_1852():
    assert (
N("profondeur").g('f').n('p').realize()   
    ) == 'profondeurs',\
    'N("profondeur").g(\'f\').n(\'p\')=>profondeurs'


def test_declension_fr_1853():
    assert (
N("programme").g('m').n('p').realize()   
    ) == 'programmes',\
    'N("programme").g(\'m\').n(\'p\')=>programmes'


def test_declension_fr_1854():
    assert (
N("progrès").g('m').n('p').realize()   
    ) == 'progrès',\
    'N("progrès").g(\'m\').n(\'p\')=>progrès'


def test_declension_fr_1855():
    assert (
N("proie").g('f').n('p').realize()   
    ) == 'proies',\
    'N("proie").g(\'f\').n(\'p\')=>proies'


def test_declension_fr_1856():
    assert (
N("projet").g('m').n('p').realize()   
    ) == 'projets',\
    'N("projet").g(\'m\').n(\'p\')=>projets'


def test_declension_fr_1857():
    assert (
N("promenade").g('f').n('p').realize()   
    ) == 'promenades',\
    'N("promenade").g(\'f\').n(\'p\')=>promenades'


def test_declension_fr_1858():
    assert (
N("promeneur").g('m').n('p').realize()   
    ) == 'promeneurs',\
    'N("promeneur").g(\'m\').n(\'p\')=>promeneurs'


def test_declension_fr_1859():
    assert (
N("promesse").g('f').n('p').realize()   
    ) == 'promesses',\
    'N("promesse").g(\'f\').n(\'p\')=>promesses'


def test_declension_fr_1860():
    assert (
A("prompt").n('p').realize()   
    ) == 'prompts',\
    'A("prompt").n(\'p\')=>prompts'


def test_declension_fr_1861():
    assert (
A("propice").n('p').realize()   
    ) == 'propices',\
    'A("propice").n(\'p\')=>propices'


def test_declension_fr_1862():
    assert (
N("propos").g('m').n('p').realize()   
    ) == 'propos',\
    'N("propos").g(\'m\').n(\'p\')=>propos'


def test_declension_fr_1863():
    assert (
N("proposition").g('f').n('p').realize()   
    ) == 'propositions',\
    'N("proposition").g(\'f\').n(\'p\')=>propositions'


def test_declension_fr_1864():
    assert (
A("propre").n('p').realize()   
    ) == 'propres',\
    'A("propre").n(\'p\')=>propres'


def test_declension_fr_1865():
    assert (
N("propreté").g('f').n('p').realize()   
    ) == 'propretés',\
    'N("propreté").g(\'f\').n(\'p\')=>propretés'


def test_declension_fr_1866():
    assert (
N("propriétaire").n('p').realize()   
    ) == 'propriétaires',\
    'N("propriétaire").n(\'p\')=>propriétaires'


def test_declension_fr_1867():
    assert (
N("propriété").g('f').n('p').realize()   
    ) == 'propriétés',\
    'N("propriété").g(\'f\').n(\'p\')=>propriétés'


def test_declension_fr_1868():
    assert (
N("prospérité").g('f').n('p').realize()   
    ) == 'prospérités',\
    'N("prospérité").g(\'f\').n(\'p\')=>prospérités'


def test_declension_fr_1869():
    assert (
N("protecteur").g('m').n('p').realize()   
    ) == 'protecteurs',\
    'N("protecteur").g(\'m\').n(\'p\')=>protecteurs'


def test_declension_fr_1870():
    assert (
N("protection").g('f').n('p').realize()   
    ) == 'protections',\
    'N("protection").g(\'f\').n(\'p\')=>protections'


def test_declension_fr_1871():
    assert (
N("proverbe").g('m').n('p').realize()   
    ) == 'proverbes',\
    'N("proverbe").g(\'m\').n(\'p\')=>proverbes'


def test_declension_fr_1872():
    assert (
N("providence").g('f').n('p').realize()   
    ) == 'providences',\
    'N("providence").g(\'f\').n(\'p\')=>providences'


def test_declension_fr_1873():
    assert (
N("provision").g('f').n('p').realize()   
    ) == 'provisions',\
    'N("provision").g(\'f\').n(\'p\')=>provisions'


def test_declension_fr_1874():
    assert (
N("prudence").g('f').n('p').realize()   
    ) == 'prudences',\
    'N("prudence").g(\'f\').n(\'p\')=>prudences'


def test_declension_fr_1875():
    assert (
A("prudent").n('p').realize()   
    ) == 'prudents',\
    'A("prudent").n(\'p\')=>prudents'


def test_declension_fr_1876():
    assert (
A("public").n('p').realize()   
    ) == 'publics',\
    'A("public").n(\'p\')=>publics'


def test_declension_fr_1877():
    assert (
N("puissance").g('f').n('p').realize()   
    ) == 'puissances',\
    'N("puissance").g(\'f\').n(\'p\')=>puissances'


def test_declension_fr_1878():
    assert (
A("puissant").n('p').realize()   
    ) == 'puissants',\
    'A("puissant").n(\'p\')=>puissants'


def test_declension_fr_1879():
    assert (
N("puits").g('m').n('p').realize()   
    ) == 'puits',\
    'N("puits").g(\'m\').n(\'p\')=>puits'


def test_declension_fr_1880():
    assert (
N("punition").g('f').n('p').realize()   
    ) == 'punitions',\
    'N("punition").g(\'f\').n(\'p\')=>punitions'


def test_declension_fr_1881():
    assert (
N("pupitre").g('m').n('p').realize()   
    ) == 'pupitres',\
    'N("pupitre").g(\'m\').n(\'p\')=>pupitres'


def test_declension_fr_1882():
    assert (
A("pur").n('p').realize()   
    ) == 'purs',\
    'A("pur").n(\'p\')=>purs'


def test_declension_fr_1883():
    assert (
N("quai").g('m').n('p').realize()   
    ) == 'quais',\
    'N("quai").g(\'m\').n(\'p\')=>quais'


def test_declension_fr_1884():
    assert (
N("qualité").g('f').n('p').realize()   
    ) == 'qualités',\
    'N("qualité").g(\'f\').n(\'p\')=>qualités'


def test_declension_fr_1885():
    assert (
N("quantité").g('f').n('p').realize()   
    ) == 'quantités',\
    'N("quantité").g(\'f\').n(\'p\')=>quantités'


def test_declension_fr_1886():
    assert (
N("quart").g('m').n('p').realize()   
    ) == 'quarts',\
    'N("quart").g(\'m\').n(\'p\')=>quarts'


def test_declension_fr_1887():
    assert (
N("quartier").g('m').n('p').realize()   
    ) == 'quartiers',\
    'N("quartier").g(\'m\').n(\'p\')=>quartiers'


def test_declension_fr_1888():
    assert (
A("quelconque").n('p').realize()   
    ) == 'quelconques',\
    'A("quelconque").n(\'p\')=>quelconques'


def test_declension_fr_1889():
    assert (
N("question").g('f').n('p').realize()   
    ) == 'questions',\
    'N("question").g(\'f\').n(\'p\')=>questions'


def test_declension_fr_1890():
    assert (
N("queue").g('f').n('p').realize()   
    ) == 'queues',\
    'N("queue").g(\'f\').n(\'p\')=>queues'


def test_declension_fr_1891():
    assert (
N("quinzaine").g('f').n('p').realize()   
    ) == 'quinzaines',\
    'N("quinzaine").g(\'f\').n(\'p\')=>quinzaines'


def test_declension_fr_1892():
    assert (
A("quotidien").n('p').realize()   
    ) == 'quotidiens',\
    'A("quotidien").n(\'p\')=>quotidiens'


def test_declension_fr_1893():
    assert (
N("race").g('f').n('p').realize()   
    ) == 'races',\
    'N("race").g(\'f\').n(\'p\')=>races'


def test_declension_fr_1894():
    assert (
N("racine").g('f').n('p').realize()   
    ) == 'racines',\
    'N("racine").g(\'f\').n(\'p\')=>racines'


def test_declension_fr_1895():
    assert (
A("radieux").n('p').realize()   
    ) == 'radieux',\
    'A("radieux").n(\'p\')=>radieux'


def test_declension_fr_1896():
    assert (
N("rage").g('f').n('p').realize()   
    ) == 'rages',\
    'N("rage").g(\'f\').n(\'p\')=>rages'


def test_declension_fr_1897():
    assert (
A("raide").n('p').realize()   
    ) == 'raides',\
    'A("raide").n(\'p\')=>raides'


def test_declension_fr_1898():
    assert (
N("raisin").g('m').n('p').realize()   
    ) == 'raisins',\
    'N("raisin").g(\'m\').n(\'p\')=>raisins'


def test_declension_fr_1899():
    assert (
N("raison").g('f').n('p').realize()   
    ) == 'raisons',\
    'N("raison").g(\'f\').n(\'p\')=>raisons'


def test_declension_fr_1900():
    assert (
A("raisonnable").n('p').realize()   
    ) == 'raisonnables',\
    'A("raisonnable").n(\'p\')=>raisonnables'


def test_declension_fr_1901():
    assert (
N("ramage").g('m').n('p').realize()   
    ) == 'ramages',\
    'N("ramage").g(\'m\').n(\'p\')=>ramages'


def test_declension_fr_1902():
    assert (
N("rame").g('f').n('p').realize()   
    ) == 'rames',\
    'N("rame").g(\'f\').n(\'p\')=>rames'


def test_declension_fr_1903():
    assert (
N("rameau").g('m').n('p').realize()   
    ) == 'rameaux',\
    'N("rameau").g(\'m\').n(\'p\')=>rameaux'


def test_declension_fr_1904():
    assert (
N("randonnée").g('f').n('p').realize()   
    ) == 'randonnées',\
    'N("randonnée").g(\'f\').n(\'p\')=>randonnées'


def test_declension_fr_1905():
    assert (
N("rang").g('m').n('p').realize()   
    ) == 'rangs',\
    'N("rang").g(\'m\').n(\'p\')=>rangs'


def test_declension_fr_1906():
    assert (
A("rapide").n('p').realize()   
    ) == 'rapides',\
    'A("rapide").n(\'p\')=>rapides'


def test_declension_fr_1907():
    assert (
N("rapidité").g('f').n('p').realize()   
    ) == 'rapidités',\
    'N("rapidité").g(\'f\').n(\'p\')=>rapidités'


def test_declension_fr_1908():
    assert (
N("rapport").g('m').n('p').realize()   
    ) == 'rapports',\
    'N("rapport").g(\'m\').n(\'p\')=>rapports'


def test_declension_fr_1909():
    assert (
A("rare").n('p').realize()   
    ) == 'rares',\
    'A("rare").n(\'p\')=>rares'


def test_declension_fr_1910():
    assert (
N("rat").g('m').n('p').realize()   
    ) == 'rats',\
    'N("rat").g(\'m\').n(\'p\')=>rats'


def test_declension_fr_1911():
    assert (
N("ravage").g('m').n('p').realize()   
    ) == 'ravages',\
    'N("ravage").g(\'m\').n(\'p\')=>ravages'


def test_declension_fr_1912():
    assert (
N("ravin").g('m').n('p').realize()   
    ) == 'ravins',\
    'N("ravin").g(\'m\').n(\'p\')=>ravins'


def test_declension_fr_1913():
    assert (
A("ravissant").n('p').realize()   
    ) == 'ravissants',\
    'A("ravissant").n(\'p\')=>ravissants'


def test_declension_fr_1914():
    assert (
N("rayon").g('m').n('p').realize()   
    ) == 'rayons',\
    'N("rayon").g(\'m\').n(\'p\')=>rayons'


def test_declension_fr_1915():
    assert (
N("réalité").g('f').n('p').realize()   
    ) == 'réalités',\
    'N("réalité").g(\'f\').n(\'p\')=>réalités'


def test_declension_fr_1916():
    assert (
N("réception").g('f').n('p').realize()   
    ) == 'réceptions',\
    'N("réception").g(\'f\').n(\'p\')=>réceptions'


def test_declension_fr_1917():
    assert (
N("recherche").g('f').n('p').realize()   
    ) == 'recherches',\
    'N("recherche").g(\'f\').n(\'p\')=>recherches'


def test_declension_fr_1918():
    assert (
N("récit").g('m').n('p').realize()   
    ) == 'récits',\
    'N("récit").g(\'m\').n(\'p\')=>récits'


def test_declension_fr_1919():
    assert (
N("récolte").g('f').n('p').realize()   
    ) == 'récoltes',\
    'N("récolte").g(\'f\').n(\'p\')=>récoltes'


def test_declension_fr_1920():
    assert (
N("recommandation").g('f').n('p').realize()   
    ) == 'recommandations',\
    'N("recommandation").g(\'f\').n(\'p\')=>recommandations'


def test_declension_fr_1921():
    assert (
N("récompense").g('f').n('p').realize()   
    ) == 'récompenses',\
    'N("récompense").g(\'f\').n(\'p\')=>récompenses'


def test_declension_fr_1922():
    assert (
N("reconnaissance").g('f').n('p').realize()   
    ) == 'reconnaissances',\
    'N("reconnaissance").g(\'f\').n(\'p\')=>reconnaissances'


def test_declension_fr_1923():
    assert (
A("reconnaissant").n('p').realize()   
    ) == 'reconnaissants',\
    'A("reconnaissant").n(\'p\')=>reconnaissants'


def test_declension_fr_1924():
    assert (
N("recours").g('m').n('p').realize()   
    ) == 'recours',\
    'N("recours").g(\'m\').n(\'p\')=>recours'


def test_declension_fr_1925():
    assert (
N("récréation").g('f').n('p').realize()   
    ) == 'récréations',\
    'N("récréation").g(\'f\').n(\'p\')=>récréations'


def test_declension_fr_1926():
    assert (
N("rédaction").g('f').n('p').realize()   
    ) == 'rédactions',\
    'N("rédaction").g(\'f\').n(\'p\')=>rédactions'


def test_declension_fr_1927():
    assert (
A("redoutable").n('p').realize()   
    ) == 'redoutables',\
    'A("redoutable").n(\'p\')=>redoutables'


def test_declension_fr_1928():
    assert (
A("réel").n('p').realize()   
    ) == 'réels',\
    'A("réel").n(\'p\')=>réels'


def test_declension_fr_1929():
    assert (
N("réfectoire").g('m').n('p').realize()   
    ) == 'réfectoires',\
    'N("réfectoire").g(\'m\').n(\'p\')=>réfectoires'


def test_declension_fr_1930():
    assert (
N("reflet").g('m').n('p').realize()   
    ) == 'reflets',\
    'N("reflet").g(\'m\').n(\'p\')=>reflets'


def test_declension_fr_1931():
    assert (
N("réflexion").g('f').n('p').realize()   
    ) == 'réflexions',\
    'N("réflexion").g(\'f\').n(\'p\')=>réflexions'


def test_declension_fr_1932():
    assert (
N("refrain").g('m').n('p').realize()   
    ) == 'refrains',\
    'N("refrain").g(\'m\').n(\'p\')=>refrains'


def test_declension_fr_1933():
    assert (
N("refuge").g('m').n('p').realize()   
    ) == 'refuges',\
    'N("refuge").g(\'m\').n(\'p\')=>refuges'


def test_declension_fr_1934():
    assert (
N("regard").g('m').n('p').realize()   
    ) == 'regards',\
    'N("regard").g(\'m\').n(\'p\')=>regards'


def test_declension_fr_1935():
    assert (
N("régime").g('m').n('p').realize()   
    ) == 'régimes',\
    'N("régime").g(\'m\').n(\'p\')=>régimes'


def test_declension_fr_1936():
    assert (
N("régiment").g('m').n('p').realize()   
    ) == 'régiments',\
    'N("régiment").g(\'m\').n(\'p\')=>régiments'


def test_declension_fr_1937():
    assert (
N("région").g('f').n('p').realize()   
    ) == 'régions',\
    'N("région").g(\'f\').n(\'p\')=>régions'


def test_declension_fr_1938():
    assert (
N("règle").g('f').n('p').realize()   
    ) == 'règles',\
    'N("règle").g(\'f\').n(\'p\')=>règles'


def test_declension_fr_1939():
    assert (
N("règne").g('m').n('p').realize()   
    ) == 'règnes',\
    'N("règne").g(\'m\').n(\'p\')=>règnes'


def test_declension_fr_1940():
    assert (
N("regret").g('m').n('p').realize()   
    ) == 'regrets',\
    'N("regret").g(\'m\').n(\'p\')=>regrets'


def test_declension_fr_1941():
    assert (
A("régulier").n('p').realize()   
    ) == 'réguliers',\
    'A("régulier").n(\'p\')=>réguliers'


def test_declension_fr_1942():
    assert (
N("reine").g('f').n('p').realize()   
    ) == 'reines',\
    'N("reine").g(\'f\').n(\'p\')=>reines'


def test_declension_fr_1943():
    assert (
A("relatif").n('p').realize()   
    ) == 'relatifs',\
    'A("relatif").n(\'p\')=>relatifs'


def test_declension_fr_1944():
    assert (
N("relation").g('f').n('p').realize()   
    ) == 'relations',\
    'N("relation").g(\'f\').n(\'p\')=>relations'


def test_declension_fr_1945():
    assert (
A("religieux").n('p').realize()   
    ) == 'religieux',\
    'A("religieux").n(\'p\')=>religieux'


def test_declension_fr_1946():
    assert (
N("religion").g('f').n('p').realize()   
    ) == 'religions',\
    'N("religion").g(\'f\').n(\'p\')=>religions'


def test_declension_fr_1947():
    assert (
A("remarquable").n('p').realize()   
    ) == 'remarquables',\
    'A("remarquable").n(\'p\')=>remarquables'


def test_declension_fr_1948():
    assert (
N("remarque").g('f').n('p').realize()   
    ) == 'remarques',\
    'N("remarque").g(\'f\').n(\'p\')=>remarques'


def test_declension_fr_1949():
    assert (
N("remède").g('m').n('p').realize()   
    ) == 'remèdes',\
    'N("remède").g(\'m\').n(\'p\')=>remèdes'


def test_declension_fr_1950():
    assert (
N("remerciement").g('m').n('p').realize()   
    ) == 'remerciements',\
    'N("remerciement").g(\'m\').n(\'p\')=>remerciements'


def test_declension_fr_1951():
    assert (
N("remise").g('f').n('p').realize()   
    ) == 'remises',\
    'N("remise").g(\'f\').n(\'p\')=>remises'


def test_declension_fr_1952():
    assert (
N("remords").g('m').n('p').realize()   
    ) == 'remords',\
    'N("remords").g(\'m\').n(\'p\')=>remords'


def test_declension_fr_1953():
    assert (
N("renard").g('m').n('p').realize()   
    ) == 'renards',\
    'N("renard").g(\'m\').n(\'p\')=>renards'


def test_declension_fr_1954():
    assert (
N("rencontre").g('f').n('p').realize()   
    ) == 'rencontres',\
    'N("rencontre").g(\'f\').n(\'p\')=>rencontres'


def test_declension_fr_1955():
    assert (
N("renoncule").g('f').n('p').realize()   
    ) == 'renoncules',\
    'N("renoncule").g(\'f\').n(\'p\')=>renoncules'


def test_declension_fr_1956():
    assert (
N("renouveau").g('m').n('p').realize()   
    ) == 'renouveaux',\
    'N("renouveau").g(\'m\').n(\'p\')=>renouveaux'


def test_declension_fr_1957():
    assert (
N("renouvellement").g('m').n('p').realize()   
    ) == 'renouvellements',\
    'N("renouvellement").g(\'m\').n(\'p\')=>renouvellements'


def test_declension_fr_1958():
    assert (
N("renseignement").g('m').n('p').realize()   
    ) == 'renseignements',\
    'N("renseignement").g(\'m\').n(\'p\')=>renseignements'


def test_declension_fr_1959():
    assert (
N("rentrée").g('f').n('p').realize()   
    ) == 'rentrées',\
    'N("rentrée").g(\'f\').n(\'p\')=>rentrées'


def test_declension_fr_1960():
    assert (
N("repas").g('m').n('p').realize()   
    ) == 'repas',\
    'N("repas").g(\'m\').n(\'p\')=>repas'


def test_declension_fr_1961():
    assert (
N("réponse").g('f').n('p').realize()   
    ) == 'réponses',\
    'N("réponse").g(\'f\').n(\'p\')=>réponses'


def test_declension_fr_1962():
    assert (
N("repos").g('m').n('p').realize()   
    ) == 'repos',\
    'N("repos").g(\'m\').n(\'p\')=>repos'


def test_declension_fr_1963():
    assert (
N("représentant").g('m').n('p').realize()   
    ) == 'représentants',\
    'N("représentant").g(\'m\').n(\'p\')=>représentants'


def test_declension_fr_1964():
    assert (
N("représentation").g('f').n('p').realize()   
    ) == 'représentations',\
    'N("représentation").g(\'f\').n(\'p\')=>représentations'


def test_declension_fr_1965():
    assert (
N("reprise").g('f').n('p').realize()   
    ) == 'reprises',\
    'N("reprise").g(\'f\').n(\'p\')=>reprises'


def test_declension_fr_1966():
    assert (
N("reproche").g('m').n('p').realize()   
    ) == 'reproches',\
    'N("reproche").g(\'m\').n(\'p\')=>reproches'


def test_declension_fr_1967():
    assert (
N("réserve").g('f').n('p').realize()   
    ) == 'réserves',\
    'N("réserve").g(\'f\').n(\'p\')=>réserves'


def test_declension_fr_1968():
    assert (
N("résistance").g('f').n('p').realize()   
    ) == 'résistances',\
    'N("résistance").g(\'f\').n(\'p\')=>résistances'


def test_declension_fr_1969():
    assert (
N("résolution").g('f').n('p').realize()   
    ) == 'résolutions',\
    'N("résolution").g(\'f\').n(\'p\')=>résolutions'


def test_declension_fr_1970():
    assert (
N("respect").g('m').n('p').realize()   
    ) == 'respects',\
    'N("respect").g(\'m\').n(\'p\')=>respects'


def test_declension_fr_1971():
    assert (
A("respectueux").n('p').realize()   
    ) == 'respectueux',\
    'A("respectueux").n(\'p\')=>respectueux'


def test_declension_fr_1972():
    assert (
N("respiration").g('f').n('p').realize()   
    ) == 'respirations',\
    'N("respiration").g(\'f\').n(\'p\')=>respirations'


def test_declension_fr_1973():
    assert (
N("ressort").g('m').n('p').realize()   
    ) == 'ressorts',\
    'N("ressort").g(\'m\').n(\'p\')=>ressorts'


def test_declension_fr_1974():
    assert (
N("ressource").g('f').n('p').realize()   
    ) == 'ressources',\
    'N("ressource").g(\'f\').n(\'p\')=>ressources'


def test_declension_fr_1975():
    assert (
N("reste").g('m').n('p').realize()   
    ) == 'restes',\
    'N("reste").g(\'m\').n(\'p\')=>restes'


def test_declension_fr_1976():
    assert (
N("résultat").g('m').n('p').realize()   
    ) == 'résultats',\
    'N("résultat").g(\'m\').n(\'p\')=>résultats'


def test_declension_fr_1977():
    assert (
N("retard").g('m').n('p').realize()   
    ) == 'retards',\
    'N("retard").g(\'m\').n(\'p\')=>retards'


def test_declension_fr_1978():
    assert (
N("retour").g('m').n('p').realize()   
    ) == 'retours',\
    'N("retour").g(\'m\').n(\'p\')=>retours'


def test_declension_fr_1979():
    assert (
N("retraite").g('f').n('p').realize()   
    ) == 'retraites',\
    'N("retraite").g(\'f\').n(\'p\')=>retraites'


def test_declension_fr_1980():
    assert (
N("réunion").g('f').n('p').realize()   
    ) == 'réunions',\
    'N("réunion").g(\'f\').n(\'p\')=>réunions'


def test_declension_fr_1981():
    assert (
N("rêve").g('m').n('p').realize()   
    ) == 'rêves',\
    'N("rêve").g(\'m\').n(\'p\')=>rêves'


def test_declension_fr_1982():
    assert (
N("réveil").g('m').n('p').realize()   
    ) == 'réveils',\
    'N("réveil").g(\'m\').n(\'p\')=>réveils'


def test_declension_fr_1983():
    assert (
N("revue").g('f').n('p').realize()   
    ) == 'revues',\
    'N("revue").g(\'f\').n(\'p\')=>revues'


def test_declension_fr_1984():
    assert (
N("rhume").g('m').n('p').realize()   
    ) == 'rhumes',\
    'N("rhume").g(\'m\').n(\'p\')=>rhumes'


def test_declension_fr_1985():
    assert (
A("riant").n('p').realize()   
    ) == 'riants',\
    'A("riant").n(\'p\')=>riants'


def test_declension_fr_1986():
    assert (
A("riche").n('p').realize()   
    ) == 'riches',\
    'A("riche").n(\'p\')=>riches'


def test_declension_fr_1987():
    assert (
N("richesse").g('f').n('p').realize()   
    ) == 'richesses',\
    'N("richesse").g(\'f\').n(\'p\')=>richesses'


def test_declension_fr_1988():
    assert (
N("rideau").g('m').n('p').realize()   
    ) == 'rideaux',\
    'N("rideau").g(\'m\').n(\'p\')=>rideaux'


def test_declension_fr_1989():
    assert (
N("rigole").g('f').n('p').realize()   
    ) == 'rigoles',\
    'N("rigole").g(\'f\').n(\'p\')=>rigoles'


def test_declension_fr_1990():
    assert (
A("rigoureux").n('p').realize()   
    ) == 'rigoureux',\
    'A("rigoureux").n(\'p\')=>rigoureux'


def test_declension_fr_1991():
    assert (
N("risque").g('m').n('p').realize()   
    ) == 'risques',\
    'N("risque").g(\'m\').n(\'p\')=>risques'


def test_declension_fr_1992():
    assert (
N("rive").g('f').n('p').realize()   
    ) == 'rives',\
    'N("rive").g(\'f\').n(\'p\')=>rives'


def test_declension_fr_1993():
    assert (
N("rivière").g('f').n('p').realize()   
    ) == 'rivières',\
    'N("rivière").g(\'f\').n(\'p\')=>rivières'


def test_declension_fr_1994():
    assert (
N("riz").g('m').n('p').realize()   
    ) == 'riz',\
    'N("riz").g(\'m\').n(\'p\')=>riz'


def test_declension_fr_1995():
    assert (
N("robe").g('f').n('p').realize()   
    ) == 'robes',\
    'N("robe").g(\'f\').n(\'p\')=>robes'


def test_declension_fr_1996():
    assert (
A("robuste").n('p').realize()   
    ) == 'robustes',\
    'A("robuste").n(\'p\')=>robustes'


def test_declension_fr_1997():
    assert (
N("rocher").g('m').n('p').realize()   
    ) == 'rochers',\
    'N("rocher").g(\'m\').n(\'p\')=>rochers'


def test_declension_fr_1998():
    assert (
N("roi").g('m').n('p').realize()   
    ) == 'rois',\
    'N("roi").g(\'m\').n(\'p\')=>rois'


def test_declension_fr_1999():
    assert (
N("rôle").g('m').n('p').realize()   
    ) == 'rôles',\
    'N("rôle").g(\'m\').n(\'p\')=>rôles'


def test_declension_fr_2000():
    assert (
A("romain").n('p').realize()   
    ) == 'romains',\
    'A("romain").n(\'p\')=>romains'


def test_declension_fr_2001():
    assert (
N("ronce").g('f').n('p').realize()   
    ) == 'ronces',\
    'N("ronce").g(\'f\').n(\'p\')=>ronces'


def test_declension_fr_2002():
    assert (
A("rond").n('p').realize()   
    ) == 'ronds',\
    'A("rond").n(\'p\')=>ronds'


def test_declension_fr_2003():
    assert (
N("ronde").g('f').n('p').realize()   
    ) == 'rondes',\
    'N("ronde").g(\'f\').n(\'p\')=>rondes'


def test_declension_fr_2004():
    assert (
N("rose").g('f').n('p').realize()   
    ) == 'roses',\
    'N("rose").g(\'f\').n(\'p\')=>roses'


def test_declension_fr_2005():
    assert (
N("roseau").g('m').n('p').realize()   
    ) == 'roseaux',\
    'N("roseau").g(\'m\').n(\'p\')=>roseaux'


def test_declension_fr_2006():
    assert (
N("rosée").g('f').n('p').realize()   
    ) == 'rosées',\
    'N("rosée").g(\'f\').n(\'p\')=>rosées'


def test_declension_fr_2007():
    assert (
N("rosier").g('m').n('p').realize()   
    ) == 'rosiers',\
    'N("rosier").g(\'m\').n(\'p\')=>rosiers'


def test_declension_fr_2008():
    assert (
N("rossignol").g('m').n('p').realize()   
    ) == 'rossignols',\
    'N("rossignol").g(\'m\').n(\'p\')=>rossignols'


def test_declension_fr_2009():
    assert (
N("rôti").g('m').n('p').realize()   
    ) == 'rôtis',\
    'N("rôti").g(\'m\').n(\'p\')=>rôtis'


def test_declension_fr_2010():
    assert (
N("roue").g('f').n('p').realize()   
    ) == 'roues',\
    'N("roue").g(\'f\').n(\'p\')=>roues'


def test_declension_fr_2011():
    assert (
A("rouge").n('p').realize()   
    ) == 'rouges',\
    'A("rouge").n(\'p\')=>rouges'


def test_declension_fr_2012():
    assert (
N("rouleau").g('m').n('p').realize()   
    ) == 'rouleaux',\
    'N("rouleau").g(\'m\').n(\'p\')=>rouleaux'


def test_declension_fr_2013():
    assert (
N("roulotte").g('f').n('p').realize()   
    ) == 'roulottes',\
    'N("roulotte").g(\'f\').n(\'p\')=>roulottes'


def test_declension_fr_2014():
    assert (
N("route").g('f').n('p').realize()   
    ) == 'routes',\
    'N("route").g(\'f\').n(\'p\')=>routes'


def test_declension_fr_2015():
    assert (
A("roux").n('p').realize()   
    ) == 'roux',\
    'A("roux").n(\'p\')=>roux'


def test_declension_fr_2016():
    assert (
A("royal").n('p').realize()   
    ) == 'royaux',\
    'A("royal").n(\'p\')=>royaux'


def test_declension_fr_2017():
    assert (
N("royaume").g('m').n('p').realize()   
    ) == 'royaumes',\
    'N("royaume").g(\'m\').n(\'p\')=>royaumes'


def test_declension_fr_2018():
    assert (
N("ruban").g('m').n('p').realize()   
    ) == 'rubans',\
    'N("ruban").g(\'m\').n(\'p\')=>rubans'


def test_declension_fr_2019():
    assert (
N("ruche").g('f').n('p').realize()   
    ) == 'ruches',\
    'N("ruche").g(\'f\').n(\'p\')=>ruches'


def test_declension_fr_2020():
    assert (
A("rude").n('p').realize()   
    ) == 'rudes',\
    'A("rude").n(\'p\')=>rudes'


def test_declension_fr_2021():
    assert (
N("rue").g('f').n('p').realize()   
    ) == 'rues',\
    'N("rue").g(\'f\').n(\'p\')=>rues'


def test_declension_fr_2022():
    assert (
N("ruelle").g('f').n('p').realize()   
    ) == 'ruelles',\
    'N("ruelle").g(\'f\').n(\'p\')=>ruelles'


def test_declension_fr_2023():
    assert (
N("ruisseau").g('m').n('p').realize()   
    ) == 'ruisseaux',\
    'N("ruisseau").g(\'m\').n(\'p\')=>ruisseaux'


def test_declension_fr_2024():
    assert (
N("ruisselet").g('m').n('p').realize()   
    ) == 'ruisselets',\
    'N("ruisselet").g(\'m\').n(\'p\')=>ruisselets'


def test_declension_fr_2025():
    assert (
A("rusé").n('p').realize()   
    ) == 'rusés',\
    'A("rusé").n(\'p\')=>rusés'


def test_declension_fr_2026():
    assert (
A("rustique").n('p').realize()   
    ) == 'rustiques',\
    'A("rustique").n(\'p\')=>rustiques'


def test_declension_fr_2027():
    assert (
N("sable").g('m').n('p').realize()   
    ) == 'sables',\
    'N("sable").g(\'m\').n(\'p\')=>sables'


def test_declension_fr_2028():
    assert (
N("sabot").g('m').n('p').realize()   
    ) == 'sabots',\
    'N("sabot").g(\'m\').n(\'p\')=>sabots'


def test_declension_fr_2029():
    assert (
N("sabre").g('m').n('p').realize()   
    ) == 'sabres',\
    'N("sabre").g(\'m\').n(\'p\')=>sabres'


def test_declension_fr_2030():
    assert (
N("sac").g('m').n('p').realize()   
    ) == 'sacs',\
    'N("sac").g(\'m\').n(\'p\')=>sacs'


def test_declension_fr_2031():
    assert (
N("sacoche").g('f').n('p').realize()   
    ) == 'sacoches',\
    'N("sacoche").g(\'f\').n(\'p\')=>sacoches'


def test_declension_fr_2032():
    assert (
A("sacré").n('p').realize()   
    ) == 'sacrés',\
    'A("sacré").n(\'p\')=>sacrés'


def test_declension_fr_2033():
    assert (
N("sacrement").g('m').n('p').realize()   
    ) == 'sacrements',\
    'N("sacrement").g(\'m\').n(\'p\')=>sacrements'


def test_declension_fr_2034():
    assert (
N("sacrifice").g('m').n('p').realize()   
    ) == 'sacrifices',\
    'N("sacrifice").g(\'m\').n(\'p\')=>sacrifices'


def test_declension_fr_2035():
    assert (
A("sage").n('p').realize()   
    ) == 'sages',\
    'A("sage").n(\'p\')=>sages'


def test_declension_fr_2036():
    assert (
N("sagesse").g('f').n('p').realize()   
    ) == 'sagesses',\
    'N("sagesse").g(\'f\').n(\'p\')=>sagesses'


def test_declension_fr_2037():
    assert (
A("sain").n('p').realize()   
    ) == 'sains',\
    'A("sain").n(\'p\')=>sains'


def test_declension_fr_2038():
    assert (
A("saint").n('p').realize()   
    ) == 'saints',\
    'A("saint").n(\'p\')=>saints'


def test_declension_fr_2039():
    assert (
N("saison").g('f').n('p').realize()   
    ) == 'saisons',\
    'N("saison").g(\'f\').n(\'p\')=>saisons'


def test_declension_fr_2040():
    assert (
N("salade").g('f').n('p').realize()   
    ) == 'salades',\
    'N("salade").g(\'f\').n(\'p\')=>salades'


def test_declension_fr_2041():
    assert (
N("salaire").g('m').n('p').realize()   
    ) == 'salaires',\
    'N("salaire").g(\'m\').n(\'p\')=>salaires'


def test_declension_fr_2042():
    assert (
A("sale").n('p').realize()   
    ) == 'sales',\
    'A("sale").n(\'p\')=>sales'


def test_declension_fr_2043():
    assert (
N("salle").g('f').n('p').realize()   
    ) == 'salles',\
    'N("salle").g(\'f\').n(\'p\')=>salles'


def test_declension_fr_2044():
    assert (
N("salon").g('m').n('p').realize()   
    ) == 'salons',\
    'N("salon").g(\'m\').n(\'p\')=>salons'


def test_declension_fr_2045():
    assert (
N("salut").g('m').n('p').realize()   
    ) == 'saluts',\
    'N("salut").g(\'m\').n(\'p\')=>saluts'


def test_declension_fr_2046():
    assert (
N("salutation").g('f').n('p').realize()   
    ) == 'salutations',\
    'N("salutation").g(\'f\').n(\'p\')=>salutations'


def test_declension_fr_2047():
    assert (
N("samedi").g('m').n('p').realize()   
    ) == 'samedis',\
    'N("samedi").g(\'m\').n(\'p\')=>samedis'


def test_declension_fr_2048():
    assert (
N("sang").g('m').n('p').realize()   
    ) == 'sangs',\
    'N("sang").g(\'m\').n(\'p\')=>sangs'


def test_declension_fr_2049():
    assert (
N("sanglot").g('m').n('p').realize()   
    ) == 'sanglots',\
    'N("sanglot").g(\'m\').n(\'p\')=>sanglots'


def test_declension_fr_2050():
    assert (
N("santé").g('f').n('p').realize()   
    ) == 'santés',\
    'N("santé").g(\'f\').n(\'p\')=>santés'


def test_declension_fr_2051():
    assert (
N("sapin").g('m').n('p').realize()   
    ) == 'sapins',\
    'N("sapin").g(\'m\').n(\'p\')=>sapins'


def test_declension_fr_2052():
    assert (
N("satin").g('m').n('p').realize()   
    ) == 'satins',\
    'N("satin").g(\'m\').n(\'p\')=>satins'


def test_declension_fr_2053():
    assert (
N("satisfaction").g('f').n('p').realize()   
    ) == 'satisfactions',\
    'N("satisfaction").g(\'f\').n(\'p\')=>satisfactions'


def test_declension_fr_2054():
    assert (
A("satisfait").n('p').realize()   
    ) == 'satisfaits',\
    'A("satisfait").n(\'p\')=>satisfaits'


def test_declension_fr_2055():
    assert (
N("saule").g('m').n('p').realize()   
    ) == 'saules',\
    'N("saule").g(\'m\').n(\'p\')=>saules'


def test_declension_fr_2056():
    assert (
N("saut").g('m').n('p').realize()   
    ) == 'sauts',\
    'N("saut").g(\'m\').n(\'p\')=>sauts'


def test_declension_fr_2057():
    assert (
A("sauvage").n('p').realize()   
    ) == 'sauvages',\
    'A("sauvage").n(\'p\')=>sauvages'


def test_declension_fr_2058():
    assert (
N("savant").g('m').n('p').realize()   
    ) == 'savants',\
    'N("savant").g(\'m\').n(\'p\')=>savants'


def test_declension_fr_2059():
    assert (
N("savon").g('m').n('p').realize()   
    ) == 'savons',\
    'N("savon").g(\'m\').n(\'p\')=>savons'


def test_declension_fr_2060():
    assert (
A("savoureux").n('p').realize()   
    ) == 'savoureux',\
    'A("savoureux").n(\'p\')=>savoureux'


def test_declension_fr_2061():
    assert (
N("scène").g('f').n('p').realize()   
    ) == 'scènes',\
    'N("scène").g(\'f\').n(\'p\')=>scènes'


def test_declension_fr_2062():
    assert (
N("science").g('f').n('p').realize()   
    ) == 'sciences',\
    'N("science").g(\'f\').n(\'p\')=>sciences'


def test_declension_fr_2063():
    assert (
A("scolaire").n('p').realize()   
    ) == 'scolaires',\
    'A("scolaire").n(\'p\')=>scolaires'


def test_declension_fr_2064():
    assert (
N("séance").g('f').n('p').realize()   
    ) == 'séances',\
    'N("séance").g(\'f\').n(\'p\')=>séances'


def test_declension_fr_2065():
    assert (
N("seau").g('m').n('p').realize()   
    ) == 'seaux',\
    'N("seau").g(\'m\').n(\'p\')=>seaux'


def test_declension_fr_2066():
    assert (
A("sec").n('p').realize()   
    ) == 'secs',\
    'A("sec").n(\'p\')=>secs'


def test_declension_fr_2067():
    assert (
N("seconde").g('f').n('p').realize()   
    ) == 'secondes',\
    'N("seconde").g(\'f\').n(\'p\')=>secondes'


def test_declension_fr_2068():
    assert (
N("secours").g('m').n('p').realize()   
    ) == 'secours',\
    'N("secours").g(\'m\').n(\'p\')=>secours'


def test_declension_fr_2069():
    assert (
N("secret").g('m').n('p').realize()   
    ) == 'secrets',\
    'N("secret").g(\'m\').n(\'p\')=>secrets'


def test_declension_fr_2070():
    assert (
N("sécurité").g('f').n('p').realize()   
    ) == 'sécurités',\
    'N("sécurité").g(\'f\').n(\'p\')=>sécurités'


def test_declension_fr_2071():
    assert (
N("seigneur").g('m').n('p').realize()   
    ) == 'seigneurs',\
    'N("seigneur").g(\'m\').n(\'p\')=>seigneurs'


def test_declension_fr_2072():
    assert (
N("séjour").g('m').n('p').realize()   
    ) == 'séjours',\
    'N("séjour").g(\'m\').n(\'p\')=>séjours'


def test_declension_fr_2073():
    assert (
N("sel").g('m').n('p').realize()   
    ) == 'sels',\
    'N("sel").g(\'m\').n(\'p\')=>sels'


def test_declension_fr_2074():
    assert (
N("semaine").g('f').n('p').realize()   
    ) == 'semaines',\
    'N("semaine").g(\'f\').n(\'p\')=>semaines'


def test_declension_fr_2075():
    assert (
A("semblable").n('p').realize()   
    ) == 'semblables',\
    'A("semblable").n(\'p\')=>semblables'


def test_declension_fr_2076():
    assert (
N("séminaire").g('m').n('p').realize()   
    ) == 'séminaires',\
    'N("séminaire").g(\'m\').n(\'p\')=>séminaires'


def test_declension_fr_2077():
    assert (
N("sens").g('m').n('p').realize()   
    ) == 'sens',\
    'N("sens").g(\'m\').n(\'p\')=>sens'


def test_declension_fr_2078():
    assert (
A("sensible").n('p').realize()   
    ) == 'sensibles',\
    'A("sensible").n(\'p\')=>sensibles'


def test_declension_fr_2079():
    assert (
N("sentier").g('m').n('p').realize()   
    ) == 'sentiers',\
    'N("sentier").g(\'m\').n(\'p\')=>sentiers'


def test_declension_fr_2080():
    assert (
N("sentiment").g('m').n('p').realize()   
    ) == 'sentiments',\
    'N("sentiment").g(\'m\').n(\'p\')=>sentiments'


def test_declension_fr_2081():
    assert (
N("septembre").g('m').n('p').realize()   
    ) == 'septembres',\
    'N("septembre").g(\'m\').n(\'p\')=>septembres'


def test_declension_fr_2082():
    assert (
A("serein").n('p').realize()   
    ) == 'sereins',\
    'A("serein").n(\'p\')=>sereins'


def test_declension_fr_2083():
    assert (
N("sergent").g('m').n('p').realize()   
    ) == 'sergents',\
    'N("sergent").g(\'m\').n(\'p\')=>sergents'


def test_declension_fr_2084():
    assert (
N("série").g('f').n('p').realize()   
    ) == 'séries',\
    'N("série").g(\'f\').n(\'p\')=>séries'


def test_declension_fr_2085():
    assert (
A("sérieux").n('p').realize()   
    ) == 'sérieux',\
    'A("sérieux").n(\'p\')=>sérieux'


def test_declension_fr_2086():
    assert (
N("sermon").g('m').n('p').realize()   
    ) == 'sermons',\
    'N("sermon").g(\'m\').n(\'p\')=>sermons'


def test_declension_fr_2087():
    assert (
N("serrure").g('f').n('p').realize()   
    ) == 'serrures',\
    'N("serrure").g(\'f\').n(\'p\')=>serrures'


def test_declension_fr_2088():
    assert (
N("servante").g('f').n('p').realize()   
    ) == 'servantes',\
    'N("servante").g(\'f\').n(\'p\')=>servantes'


def test_declension_fr_2089():
    assert (
A("serviable").n('p').realize()   
    ) == 'serviables',\
    'A("serviable").n(\'p\')=>serviables'


def test_declension_fr_2090():
    assert (
N("service").g('m').n('p').realize()   
    ) == 'services',\
    'N("service").g(\'m\').n(\'p\')=>services'


def test_declension_fr_2091():
    assert (
N("serviette").g('f').n('p').realize()   
    ) == 'serviettes',\
    'N("serviette").g(\'f\').n(\'p\')=>serviettes'


def test_declension_fr_2092():
    assert (
N("serviteur").g('m').n('p').realize()   
    ) == 'serviteurs',\
    'N("serviteur").g(\'m\').n(\'p\')=>serviteurs'


def test_declension_fr_2093():
    assert (
N("seuil").g('m').n('p').realize()   
    ) == 'seuils',\
    'N("seuil").g(\'m\').n(\'p\')=>seuils'


def test_declension_fr_2094():
    assert (
A("seul").n('p').realize()   
    ) == 'seuls',\
    'A("seul").n(\'p\')=>seuls'


def test_declension_fr_2095():
    assert (
N("sève").g('f').n('p').realize()   
    ) == 'sèves',\
    'N("sève").g(\'f\').n(\'p\')=>sèves'


def test_declension_fr_2096():
    assert (
A("sévère").n('p').realize()   
    ) == 'sévères',\
    'A("sévère").n(\'p\')=>sévères'


def test_declension_fr_2097():
    assert (
N("siècle").g('m').n('p').realize()   
    ) == 'siècles',\
    'N("siècle").g(\'m\').n(\'p\')=>siècles'


def test_declension_fr_2098():
    assert (
N("siège").g('m').n('p').realize()   
    ) == 'sièges',\
    'N("siège").g(\'m\').n(\'p\')=>sièges'


def test_declension_fr_2099():
    assert (
N("sifflement").g('m').n('p').realize()   
    ) == 'sifflements',\
    'N("sifflement").g(\'m\').n(\'p\')=>sifflements'


def test_declension_fr_2100():
    assert (
N("sifflet").g('m').n('p').realize()   
    ) == 'sifflets',\
    'N("sifflet").g(\'m\').n(\'p\')=>sifflets'


def test_declension_fr_2101():
    assert (
N("signal").g('m').n('p').realize()   
    ) == 'signaux',\
    'N("signal").g(\'m\').n(\'p\')=>signaux'


def test_declension_fr_2102():
    assert (
N("signature").g('f').n('p').realize()   
    ) == 'signatures',\
    'N("signature").g(\'f\').n(\'p\')=>signatures'


def test_declension_fr_2103():
    assert (
N("signe").g('m').n('p').realize()   
    ) == 'signes',\
    'N("signe").g(\'m\').n(\'p\')=>signes'


def test_declension_fr_2104():
    assert (
N("silence").g('m').n('p').realize()   
    ) == 'silences',\
    'N("silence").g(\'m\').n(\'p\')=>silences'


def test_declension_fr_2105():
    assert (
A("silencieux").n('p').realize()   
    ) == 'silencieux',\
    'A("silencieux").n(\'p\')=>silencieux'


def test_declension_fr_2106():
    assert (
N("sillon").g('m').n('p').realize()   
    ) == 'sillons',\
    'N("sillon").g(\'m\').n(\'p\')=>sillons'


def test_declension_fr_2107():
    assert (
A("simple").n('p').realize()   
    ) == 'simples',\
    'A("simple").n(\'p\')=>simples'


def test_declension_fr_2108():
    assert (
N("simplicité").g('f').n('p').realize()   
    ) == 'simplicités',\
    'N("simplicité").g(\'f\').n(\'p\')=>simplicités'


def test_declension_fr_2109():
    assert (
A("sincère").n('p').realize()   
    ) == 'sincères',\
    'A("sincère").n(\'p\')=>sincères'


def test_declension_fr_2110():
    assert (
N("sincérité").g('f').n('p').realize()   
    ) == 'sincérités',\
    'N("sincérité").g(\'f\').n(\'p\')=>sincérités'


def test_declension_fr_2111():
    assert (
N("singe").g('m').n('p').realize()   
    ) == 'singes',\
    'N("singe").g(\'m\').n(\'p\')=>singes'


def test_declension_fr_2112():
    assert (
A("singulier").n('p').realize()   
    ) == 'singuliers',\
    'A("singulier").n(\'p\')=>singuliers'


def test_declension_fr_2113():
    assert (
A("sinistre").n('p').realize()   
    ) == 'sinistres',\
    'A("sinistre").n(\'p\')=>sinistres'


def test_declension_fr_2114():
    assert (
N("sirène").g('f').n('p').realize()   
    ) == 'sirènes',\
    'N("sirène").g(\'f\').n(\'p\')=>sirènes'


def test_declension_fr_2115():
    assert (
N("situation").g('f').n('p').realize()   
    ) == 'situations',\
    'N("situation").g(\'f\').n(\'p\')=>situations'


def test_declension_fr_2116():
    assert (
A("sobre").n('p').realize()   
    ) == 'sobres',\
    'A("sobre").n(\'p\')=>sobres'


def test_declension_fr_2117():
    assert (
N("société").g('f').n('p').realize()   
    ) == 'sociétés',\
    'N("société").g(\'f\').n(\'p\')=>sociétés'


def test_declension_fr_2118():
    assert (
N("soie").g('f').n('p').realize()   
    ) == 'soies',\
    'N("soie").g(\'f\').n(\'p\')=>soies'


def test_declension_fr_2119():
    assert (
N("soif").g('f').n('p').realize()   
    ) == 'soifs',\
    'N("soif").g(\'f\').n(\'p\')=>soifs'


def test_declension_fr_2120():
    assert (
A("soigneux").n('p').realize()   
    ) == 'soigneux',\
    'A("soigneux").n(\'p\')=>soigneux'


def test_declension_fr_2121():
    assert (
N("soin").g('m').n('p').realize()   
    ) == 'soins',\
    'N("soin").g(\'m\').n(\'p\')=>soins'


def test_declension_fr_2122():
    assert (
N("soir").g('m').n('p').realize()   
    ) == 'soirs',\
    'N("soir").g(\'m\').n(\'p\')=>soirs'


def test_declension_fr_2123():
    assert (
N("soirée").g('f').n('p').realize()   
    ) == 'soirées',\
    'N("soirée").g(\'f\').n(\'p\')=>soirées'


def test_declension_fr_2124():
    assert (
N("sol").g('m').n('p').realize()   
    ) == 'sols',\
    'N("sol").g(\'m\').n(\'p\')=>sols'


def test_declension_fr_2125():
    assert (
N("soldat").g('m').n('p').realize()   
    ) == 'soldats',\
    'N("soldat").g(\'m\').n(\'p\')=>soldats'


def test_declension_fr_2126():
    assert (
N("soleil").g('m').n('p').realize()   
    ) == 'soleils',\
    'N("soleil").g(\'m\').n(\'p\')=>soleils'


def test_declension_fr_2127():
    assert (
A("solennel").n('p').realize()   
    ) == 'solennels',\
    'A("solennel").n(\'p\')=>solennels'


def test_declension_fr_2128():
    assert (
A("solide").n('p').realize()   
    ) == 'solides',\
    'A("solide").n(\'p\')=>solides'


def test_declension_fr_2129():
    assert (
A("solitaire").n('p').realize()   
    ) == 'solitaires',\
    'A("solitaire").n(\'p\')=>solitaires'


def test_declension_fr_2130():
    assert (
N("solitude").g('f').n('p').realize()   
    ) == 'solitudes',\
    'N("solitude").g(\'f\').n(\'p\')=>solitudes'


def test_declension_fr_2131():
    assert (
A("sombre").n('p').realize()   
    ) == 'sombres',\
    'A("sombre").n(\'p\')=>sombres'


def test_declension_fr_2132():
    assert (
N("somme").g('f').n('p').realize()   
    ) == 'sommes',\
    'N("somme").g(\'f\').n(\'p\')=>sommes'


def test_declension_fr_2133():
    assert (
N("sommeil").g('m').n('p').realize()   
    ) == 'sommeils',\
    'N("sommeil").g(\'m\').n(\'p\')=>sommeils'


def test_declension_fr_2134():
    assert (
N("sommet").g('m').n('p').realize()   
    ) == 'sommets',\
    'N("sommet").g(\'m\').n(\'p\')=>sommets'


def test_declension_fr_2135():
    assert (
N("son").g('m').n('p').realize()   
    ) == 'sons',\
    'N("son").g(\'m\').n(\'p\')=>sons'


def test_declension_fr_2136():
    assert (
N("sonnette").g('f').n('p').realize()   
    ) == 'sonnettes',\
    'N("sonnette").g(\'f\').n(\'p\')=>sonnettes'


def test_declension_fr_2137():
    assert (
A("sonore").n('p').realize()   
    ) == 'sonores',\
    'A("sonore").n(\'p\')=>sonores'


def test_declension_fr_2138():
    assert (
N("sort").g('m').n('p').realize()   
    ) == 'sorts',\
    'N("sort").g(\'m\').n(\'p\')=>sorts'


def test_declension_fr_2139():
    assert (
N("sorte").g('f').n('p').realize()   
    ) == 'sortes',\
    'N("sorte").g(\'f\').n(\'p\')=>sortes'


def test_declension_fr_2140():
    assert (
N("sortie").g('f').n('p').realize()   
    ) == 'sorties',\
    'N("sortie").g(\'f\').n(\'p\')=>sorties'


def test_declension_fr_2141():
    assert (
A("sot").n('p').realize()   
    ) == 'sots',\
    'A("sot").n(\'p\')=>sots'


def test_declension_fr_2142():
    assert (
N("sou").g('m').n('p').realize()   
    ) == 'sous',\
    'N("sou").g(\'m\').n(\'p\')=>sous'


def test_declension_fr_2143():
    assert (
N("souci").g('m').n('p').realize()   
    ) == 'soucis',\
    'N("souci").g(\'m\').n(\'p\')=>soucis'


def test_declension_fr_2144():
    assert (
N("souffle").g('m').n('p').realize()   
    ) == 'souffles',\
    'N("souffle").g(\'m\').n(\'p\')=>souffles'


def test_declension_fr_2145():
    assert (
N("souffrance").g('f').n('p').realize()   
    ) == 'souffrances',\
    'N("souffrance").g(\'f\').n(\'p\')=>souffrances'


def test_declension_fr_2146():
    assert (
N("souhait").g('m').n('p').realize()   
    ) == 'souhaits',\
    'N("souhait").g(\'m\').n(\'p\')=>souhaits'


def test_declension_fr_2147():
    assert (
N("soulagement").g('m').n('p').realize()   
    ) == 'soulagements',\
    'N("soulagement").g(\'m\').n(\'p\')=>soulagements'


def test_declension_fr_2148():
    assert (
N("soulier").g('m').n('p').realize()   
    ) == 'souliers',\
    'N("soulier").g(\'m\').n(\'p\')=>souliers'


def test_declension_fr_2149():
    assert (
N("soupe").g('f').n('p').realize()   
    ) == 'soupes',\
    'N("soupe").g(\'f\').n(\'p\')=>soupes'


def test_declension_fr_2150():
    assert (
N("soupir").g('m').n('p').realize()   
    ) == 'soupirs',\
    'N("soupir").g(\'m\').n(\'p\')=>soupirs'


def test_declension_fr_2151():
    assert (
A("souple").n('p').realize()   
    ) == 'souples',\
    'A("souple").n(\'p\')=>souples'


def test_declension_fr_2152():
    assert (
N("source").g('f').n('p').realize()   
    ) == 'sources',\
    'N("source").g(\'f\').n(\'p\')=>sources'


def test_declension_fr_2153():
    assert (
A("sourd").n('p').realize()   
    ) == 'sourds',\
    'A("sourd").n(\'p\')=>sourds'


def test_declension_fr_2154():
    assert (
A("souriant").n('p').realize()   
    ) == 'souriants',\
    'A("souriant").n(\'p\')=>souriants'


def test_declension_fr_2155():
    assert (
N("souris").g('f').n('p').realize()   
    ) == 'souris',\
    'N("souris").g(\'f\').n(\'p\')=>souris'


def test_declension_fr_2156():
    assert (
A("souterrain").n('p').realize()   
    ) == 'souterrains',\
    'A("souterrain").n(\'p\')=>souterrains'


def test_declension_fr_2157():
    assert (
N("soutien").g('m').n('p').realize()   
    ) == 'soutiens',\
    'N("soutien").g(\'m\').n(\'p\')=>soutiens'


def test_declension_fr_2158():
    assert (
N("souvenir").g('m').n('p').realize()   
    ) == 'souvenirs',\
    'N("souvenir").g(\'m\').n(\'p\')=>souvenirs'


def test_declension_fr_2159():
    assert (
N("souverain").g('m').n('p').realize()   
    ) == 'souverains',\
    'N("souverain").g(\'m\').n(\'p\')=>souverains'


def test_declension_fr_2160():
    assert (
A("soyeux").n('p').realize()   
    ) == 'soyeux',\
    'A("soyeux").n(\'p\')=>soyeux'


def test_declension_fr_2161():
    assert (
A("spacieux").n('p').realize()   
    ) == 'spacieux',\
    'A("spacieux").n(\'p\')=>spacieux'


def test_declension_fr_2162():
    assert (
A("spécial").n('p').realize()   
    ) == 'spéciaux',\
    'A("spécial").n(\'p\')=>spéciaux'


def test_declension_fr_2163():
    assert (
N("spectacle").g('m').n('p').realize()   
    ) == 'spectacles',\
    'N("spectacle").g(\'m\').n(\'p\')=>spectacles'


def test_declension_fr_2164():
    assert (
N("spectateur").g('m').n('p').realize()   
    ) == 'spectateurs',\
    'N("spectateur").g(\'m\').n(\'p\')=>spectateurs'


def test_declension_fr_2165():
    assert (
N("splendeur").g('f').n('p').realize()   
    ) == 'splendeurs',\
    'N("splendeur").g(\'f\').n(\'p\')=>splendeurs'


def test_declension_fr_2166():
    assert (
A("splendide").n('p').realize()   
    ) == 'splendides',\
    'A("splendide").n(\'p\')=>splendides'


def test_declension_fr_2167():
    assert (
N("sport").g('m').n('p').realize()   
    ) == 'sports',\
    'N("sport").g(\'m\').n(\'p\')=>sports'


def test_declension_fr_2168():
    assert (
N("station").g('f').n('p').realize()   
    ) == 'stations',\
    'N("station").g(\'f\').n(\'p\')=>stations'


def test_declension_fr_2169():
    assert (
N("statue").g('f').n('p').realize()   
    ) == 'statues',\
    'N("statue").g(\'f\').n(\'p\')=>statues'


def test_declension_fr_2170():
    assert (
A("studieux").n('p').realize()   
    ) == 'studieux',\
    'A("studieux").n(\'p\')=>studieux'


def test_declension_fr_2171():
    assert (
N("stupéfaction").g('f').n('p').realize()   
    ) == 'stupéfactions',\
    'N("stupéfaction").g(\'f\').n(\'p\')=>stupéfactions'


def test_declension_fr_2172():
    assert (
N("style").g('m').n('p').realize()   
    ) == 'styles',\
    'N("style").g(\'m\').n(\'p\')=>styles'


def test_declension_fr_2173():
    assert (
A("suave").n('p').realize()   
    ) == 'suaves',\
    'A("suave").n(\'p\')=>suaves'


def test_declension_fr_2174():
    assert (
A("sublime").n('p').realize()   
    ) == 'sublimes',\
    'A("sublime").n(\'p\')=>sublimes'


def test_declension_fr_2175():
    assert (
N("suc").g('m').n('p').realize()   
    ) == 'sucs',\
    'N("suc").g(\'m\').n(\'p\')=>sucs'


def test_declension_fr_2176():
    assert (
N("succès").g('m').n('p').realize()   
    ) == 'succès',\
    'N("succès").g(\'m\').n(\'p\')=>succès'


def test_declension_fr_2177():
    assert (
A("succulent").n('p').realize()   
    ) == 'succulents',\
    'A("succulent").n(\'p\')=>succulents'


def test_declension_fr_2178():
    assert (
N("sucre").g('m').n('p').realize()   
    ) == 'sucres',\
    'N("sucre").g(\'m\').n(\'p\')=>sucres'


def test_declension_fr_2179():
    assert (
N("sueur").g('f').n('p').realize()   
    ) == 'sueurs',\
    'N("sueur").g(\'f\').n(\'p\')=>sueurs'


def test_declension_fr_2180():
    assert (
A("suffisant").n('p').realize()   
    ) == 'suffisants',\
    'A("suffisant").n(\'p\')=>suffisants'


def test_declension_fr_2181():
    assert (
N("suite").g('f').n('p').realize()   
    ) == 'suites',\
    'N("suite").g(\'f\').n(\'p\')=>suites'


def test_declension_fr_2182():
    assert (
A("suivant").n('p').realize()   
    ) == 'suivants',\
    'A("suivant").n(\'p\')=>suivants'


def test_declension_fr_2183():
    assert (
N("sujet").g('m').n('p').realize()   
    ) == 'sujets',\
    'N("sujet").g(\'m\').n(\'p\')=>sujets'


def test_declension_fr_2184():
    assert (
A("superbe").n('p').realize()   
    ) == 'superbes',\
    'A("superbe").n(\'p\')=>superbes'


def test_declension_fr_2185():
    assert (
A("supérieur").n('p').realize()   
    ) == 'supérieurs',\
    'A("supérieur").n(\'p\')=>supérieurs'


def test_declension_fr_2186():
    assert (
A("suprême").n('p').realize()   
    ) == 'suprêmes',\
    'A("suprême").n(\'p\')=>suprêmes'


def test_declension_fr_2187():
    assert (
A("sûr").n('p').realize()   
    ) == 'sûrs',\
    'A("sûr").n(\'p\')=>sûrs'


def test_declension_fr_2188():
    assert (
N("surface").g('f').n('p').realize()   
    ) == 'surfaces',\
    'N("surface").g(\'f\').n(\'p\')=>surfaces'


def test_declension_fr_2189():
    assert (
N("surprise").g('f').n('p').realize()   
    ) == 'surprises',\
    'N("surprise").g(\'f\').n(\'p\')=>surprises'


def test_declension_fr_2190():
    assert (
N("sursaut").g('m').n('p').realize()   
    ) == 'sursauts',\
    'N("sursaut").g(\'m\').n(\'p\')=>sursauts'


def test_declension_fr_2191():
    assert (
N("symbole").g('m').n('p').realize()   
    ) == 'symboles',\
    'N("symbole").g(\'m\').n(\'p\')=>symboles'


def test_declension_fr_2192():
    assert (
N("sympathie").g('f').n('p').realize()   
    ) == 'sympathies',\
    'N("sympathie").g(\'f\').n(\'p\')=>sympathies'


def test_declension_fr_2193():
    assert (
N("tabac").g('m').n('p').realize()   
    ) == 'tabacs',\
    'N("tabac").g(\'m\').n(\'p\')=>tabacs'


def test_declension_fr_2194():
    assert (
N("table").g('f').n('p').realize()   
    ) == 'tables',\
    'N("table").g(\'f\').n(\'p\')=>tables'


def test_declension_fr_2195():
    assert (
N("tableau").g('m').n('p').realize()   
    ) == 'tableaux',\
    'N("tableau").g(\'m\').n(\'p\')=>tableaux'


def test_declension_fr_2196():
    assert (
N("tablier").g('m').n('p').realize()   
    ) == 'tabliers',\
    'N("tablier").g(\'m\').n(\'p\')=>tabliers'


def test_declension_fr_2197():
    assert (
N("tache").g('f').n('p').realize()   
    ) == 'taches',\
    'N("tache").g(\'f\').n(\'p\')=>taches'


def test_declension_fr_2198():
    assert (
N("tâche").g('f').n('p').realize()   
    ) == 'tâches',\
    'N("tâche").g(\'f\').n(\'p\')=>tâches'


def test_declension_fr_2199():
    assert (
N("taille").g('f').n('p').realize()   
    ) == 'tailles',\
    'N("taille").g(\'f\').n(\'p\')=>tailles'


def test_declension_fr_2200():
    assert (
N("tailleur").g('m').n('p').realize()   
    ) == 'tailleurs',\
    'N("tailleur").g(\'m\').n(\'p\')=>tailleurs'


def test_declension_fr_2201():
    assert (
N("taillis").g('m').n('p').realize()   
    ) == 'taillis',\
    'N("taillis").g(\'m\').n(\'p\')=>taillis'


def test_declension_fr_2202():
    assert (
N("talent").g('m').n('p').realize()   
    ) == 'talents',\
    'N("talent").g(\'m\').n(\'p\')=>talents'


def test_declension_fr_2203():
    assert (
N("talus").g('m').n('p').realize()   
    ) == 'talus',\
    'N("talus").g(\'m\').n(\'p\')=>talus'


def test_declension_fr_2204():
    assert (
N("tambour").g('m').n('p').realize()   
    ) == 'tambours',\
    'N("tambour").g(\'m\').n(\'p\')=>tambours'


def test_declension_fr_2205():
    assert (
N("tante").g('f').n('p').realize()   
    ) == 'tantes',\
    'N("tante").g(\'f\').n(\'p\')=>tantes'


def test_declension_fr_2206():
    assert (
N("tapage").g('m').n('p').realize()   
    ) == 'tapages',\
    'N("tapage").g(\'m\').n(\'p\')=>tapages'


def test_declension_fr_2207():
    assert (
N("tapis").g('m').n('p').realize()   
    ) == 'tapis',\
    'N("tapis").g(\'m\').n(\'p\')=>tapis'


def test_declension_fr_2208():
    assert (
N("tarte").g('f').n('p').realize()   
    ) == 'tartes',\
    'N("tarte").g(\'f\').n(\'p\')=>tartes'


def test_declension_fr_2209():
    assert (
N("tartine").g('f').n('p').realize()   
    ) == 'tartines',\
    'N("tartine").g(\'f\').n(\'p\')=>tartines'


def test_declension_fr_2210():
    assert (
N("tas").g('m').n('p').realize()   
    ) == 'tas',\
    'N("tas").g(\'m\').n(\'p\')=>tas'


def test_declension_fr_2211():
    assert (
N("tasse").g('f').n('p').realize()   
    ) == 'tasses',\
    'N("tasse").g(\'f\').n(\'p\')=>tasses'


def test_declension_fr_2212():
    assert (
N("teinte").g('f').n('p').realize()   
    ) == 'teintes',\
    'N("teinte").g(\'f\').n(\'p\')=>teintes'


def test_declension_fr_2213():
    assert (
N("télégramme").g('m').n('p').realize()   
    ) == 'télégrammes',\
    'N("télégramme").g(\'m\').n(\'p\')=>télégrammes'


def test_declension_fr_2214():
    assert (
N("téléphone").g('m').n('p').realize()   
    ) == 'téléphones',\
    'N("téléphone").g(\'m\').n(\'p\')=>téléphones'


def test_declension_fr_2215():
    assert (
N("témoignage").g('m').n('p').realize()   
    ) == 'témoignages',\
    'N("témoignage").g(\'m\').n(\'p\')=>témoignages'


def test_declension_fr_2216():
    assert (
N("témoin").g('m').n('p').realize()   
    ) == 'témoins',\
    'N("témoin").g(\'m\').n(\'p\')=>témoins'


def test_declension_fr_2217():
    assert (
N("température").g('f').n('p').realize()   
    ) == 'températures',\
    'N("température").g(\'f\').n(\'p\')=>températures'


def test_declension_fr_2218():
    assert (
N("tempête").g('f').n('p').realize()   
    ) == 'tempêtes',\
    'N("tempête").g(\'f\').n(\'p\')=>tempêtes'


def test_declension_fr_2219():
    assert (
N("temps").g('m').n('p').realize()   
    ) == 'temps',\
    'N("temps").g(\'m\').n(\'p\')=>temps'


def test_declension_fr_2220():
    assert (
A("tendre").n('p').realize()   
    ) == 'tendres',\
    'A("tendre").n(\'p\')=>tendres'


def test_declension_fr_2221():
    assert (
N("tendresse").g('f').n('p').realize()   
    ) == 'tendresses',\
    'N("tendresse").g(\'f\').n(\'p\')=>tendresses'


def test_declension_fr_2222():
    assert (
N("ténèbres").g('f').n('p').realize()   
    ) == 'ténèbres',\
    'N("ténèbres").g(\'f\').n(\'p\')=>ténèbres'


def test_declension_fr_2223():
    assert (
N("tentation").g('f').n('p').realize()   
    ) == 'tentations',\
    'N("tentation").g(\'f\').n(\'p\')=>tentations'


def test_declension_fr_2224():
    assert (
N("tente").g('f').n('p').realize()   
    ) == 'tentes',\
    'N("tente").g(\'f\').n(\'p\')=>tentes'


def test_declension_fr_2225():
    assert (
N("tenue").g('f').n('p').realize()   
    ) == 'tenues',\
    'N("tenue").g(\'f\').n(\'p\')=>tenues'


def test_declension_fr_2226():
    assert (
N("terme").g('m').n('p').realize()   
    ) == 'termes',\
    'N("terme").g(\'m\').n(\'p\')=>termes'


def test_declension_fr_2227():
    assert (
N("terrain").g('m').n('p').realize()   
    ) == 'terrains',\
    'N("terrain").g(\'m\').n(\'p\')=>terrains'


def test_declension_fr_2228():
    assert (
N("terrasse").g('f').n('p').realize()   
    ) == 'terrasses',\
    'N("terrasse").g(\'f\').n(\'p\')=>terrasses'


def test_declension_fr_2229():
    assert (
N("terre").g('f').n('p').realize()   
    ) == 'terres',\
    'N("terre").g(\'f\').n(\'p\')=>terres'


def test_declension_fr_2230():
    assert (
A("terrestre").n('p').realize()   
    ) == 'terrestres',\
    'A("terrestre").n(\'p\')=>terrestres'


def test_declension_fr_2231():
    assert (
N("terreur").g('f').n('p').realize()   
    ) == 'terreurs',\
    'N("terreur").g(\'f\').n(\'p\')=>terreurs'


def test_declension_fr_2232():
    assert (
A("terrible").n('p').realize()   
    ) == 'terribles',\
    'A("terrible").n(\'p\')=>terribles'


def test_declension_fr_2233():
    assert (
N("terrier").g('m').n('p').realize()   
    ) == 'terriers',\
    'N("terrier").g(\'m\').n(\'p\')=>terriers'


def test_declension_fr_2234():
    assert (
N("tête").g('f').n('p').realize()   
    ) == 'têtes',\
    'N("tête").g(\'f\').n(\'p\')=>têtes'


def test_declension_fr_2235():
    assert (
N("thé").g('m').n('p').realize()   
    ) == 'thés',\
    'N("thé").g(\'m\').n(\'p\')=>thés'


def test_declension_fr_2236():
    assert (
N("théâtre").g('m').n('p').realize()   
    ) == 'théâtres',\
    'N("théâtre").g(\'m\').n(\'p\')=>théâtres'


def test_declension_fr_2237():
    assert (
A("tiède").n('p').realize()   
    ) == 'tièdes',\
    'A("tiède").n(\'p\')=>tièdes'


def test_declension_fr_2238():
    assert (
N("tige").g('f').n('p').realize()   
    ) == 'tiges',\
    'N("tige").g(\'f\').n(\'p\')=>tiges'


def test_declension_fr_2239():
    assert (
N("tigre").g('m').n('p').realize()   
    ) == 'tigres',\
    'N("tigre").g(\'m\').n(\'p\')=>tigres'


def test_declension_fr_2240():
    assert (
N("tilleul").g('m').n('p').realize()   
    ) == 'tilleuls',\
    'N("tilleul").g(\'m\').n(\'p\')=>tilleuls'


def test_declension_fr_2241():
    assert (
N("timbre").g('m').n('p').realize()   
    ) == 'timbres',\
    'N("timbre").g(\'m\').n(\'p\')=>timbres'


def test_declension_fr_2242():
    assert (
A("timide").n('p').realize()   
    ) == 'timides',\
    'A("timide").n(\'p\')=>timides'


def test_declension_fr_2243():
    assert (
N("tirelire").g('f').n('p').realize()   
    ) == 'tirelires',\
    'N("tirelire").g(\'f\').n(\'p\')=>tirelires'


def test_declension_fr_2244():
    assert (
N("tiroir").g('m').n('p').realize()   
    ) == 'tiroirs',\
    'N("tiroir").g(\'m\').n(\'p\')=>tiroirs'


def test_declension_fr_2245():
    assert (
N("tissu").g('m').n('p').realize()   
    ) == 'tissus',\
    'N("tissu").g(\'m\').n(\'p\')=>tissus'


def test_declension_fr_2246():
    assert (
N("titre").g('m').n('p').realize()   
    ) == 'titres',\
    'N("titre").g(\'m\').n(\'p\')=>titres'


def test_declension_fr_2247():
    assert (
N("toile").g('f').n('p').realize()   
    ) == 'toiles',\
    'N("toile").g(\'f\').n(\'p\')=>toiles'


def test_declension_fr_2248():
    assert (
N("toilette").g('f').n('p').realize()   
    ) == 'toilettes',\
    'N("toilette").g(\'f\').n(\'p\')=>toilettes'


def test_declension_fr_2249():
    assert (
N("toit").g('m').n('p').realize()   
    ) == 'toits',\
    'N("toit").g(\'m\').n(\'p\')=>toits'


def test_declension_fr_2250():
    assert (
N("tombe").g('f').n('p').realize()   
    ) == 'tombes',\
    'N("tombe").g(\'f\').n(\'p\')=>tombes'


def test_declension_fr_2251():
    assert (
N("tombeau").g('m').n('p').realize()   
    ) == 'tombeaux',\
    'N("tombeau").g(\'m\').n(\'p\')=>tombeaux'


def test_declension_fr_2252():
    assert (
N("ton").g('m').n('p').realize()   
    ) == 'tons',\
    'N("ton").g(\'m\').n(\'p\')=>tons'


def test_declension_fr_2253():
    assert (
N("tonneau").g('m').n('p').realize()   
    ) == 'tonneaux',\
    'N("tonneau").g(\'m\').n(\'p\')=>tonneaux'


def test_declension_fr_2254():
    assert (
N("tonnerre").g('m').n('p').realize()   
    ) == 'tonnerres',\
    'N("tonnerre").g(\'m\').n(\'p\')=>tonnerres'


def test_declension_fr_2255():
    assert (
N("torrent").g('m').n('p').realize()   
    ) == 'torrents',\
    'N("torrent").g(\'m\').n(\'p\')=>torrents'


def test_declension_fr_2256():
    assert (
N("tort").g('m').n('p').realize()   
    ) == 'torts',\
    'N("tort").g(\'m\').n(\'p\')=>torts'


def test_declension_fr_2257():
    assert (
N("tortue").g('f').n('p').realize()   
    ) == 'tortues',\
    'N("tortue").g(\'f\').n(\'p\')=>tortues'


def test_declension_fr_2258():
    assert (
N("touffe").g('f').n('p').realize()   
    ) == 'touffes',\
    'N("touffe").g(\'f\').n(\'p\')=>touffes'


def test_declension_fr_2259():
    assert (
A("touffu").n('p').realize()   
    ) == 'touffus',\
    'A("touffu").n(\'p\')=>touffus'


def test_declension_fr_2260():
    assert (
N("tour").g('m').n('p').realize()   
    ) == 'tours',\
    'N("tour").g(\'m\').n(\'p\')=>tours'


def test_declension_fr_2261():
    assert (
N("tourbillon").g('m').n('p').realize()   
    ) == 'tourbillons',\
    'N("tourbillon").g(\'m\').n(\'p\')=>tourbillons'


def test_declension_fr_2262():
    assert (
N("tourment").g('m').n('p').realize()   
    ) == 'tourments',\
    'N("tourment").g(\'m\').n(\'p\')=>tourments'


def test_declension_fr_2263():
    assert (
N("tournant").g('m').n('p').realize()   
    ) == 'tournants',\
    'N("tournant").g(\'m\').n(\'p\')=>tournants'


def test_declension_fr_2264():
    assert (
N("tournée").g('f').n('p').realize()   
    ) == 'tournées',\
    'N("tournée").g(\'f\').n(\'p\')=>tournées'


def test_declension_fr_2265():
    assert (
N("toux").g('f').n('p').realize()   
    ) == 'toux',\
    'N("toux").g(\'f\').n(\'p\')=>toux'


def test_declension_fr_2266():
    assert (
N("trace").g('f').n('p').realize()   
    ) == 'traces',\
    'N("trace").g(\'f\').n(\'p\')=>traces'


def test_declension_fr_2267():
    assert (
N("train").g('m').n('p').realize()   
    ) == 'trains',\
    'N("train").g(\'m\').n(\'p\')=>trains'


def test_declension_fr_2268():
    assert (
N("traîneau").g('m').n('p').realize()   
    ) == 'traîneaux',\
    'N("traîneau").g(\'m\').n(\'p\')=>traîneaux'


def test_declension_fr_2269():
    assert (
N("trait").g('m').n('p').realize()   
    ) == 'traits',\
    'N("trait").g(\'m\').n(\'p\')=>traits'


def test_declension_fr_2270():
    assert (
N("traitement").g('m').n('p').realize()   
    ) == 'traitements',\
    'N("traitement").g(\'m\').n(\'p\')=>traitements'


def test_declension_fr_2271():
    assert (
N("trajet").g('m').n('p').realize()   
    ) == 'trajets',\
    'N("trajet").g(\'m\').n(\'p\')=>trajets'


def test_declension_fr_2272():
    assert (
N("tram").g('m').n('p').realize()   
    ) == 'trams',\
    'N("tram").g(\'m\').n(\'p\')=>trams'


def test_declension_fr_2273():
    assert (
N("tramway").g('m').n('p').realize()   
    ) == 'tramways',\
    'N("tramway").g(\'m\').n(\'p\')=>tramways'


def test_declension_fr_2274():
    assert (
N("tranche").g('f').n('p').realize()   
    ) == 'tranches',\
    'N("tranche").g(\'f\').n(\'p\')=>tranches'


def test_declension_fr_2275():
    assert (
A("tranquille").n('p').realize()   
    ) == 'tranquilles',\
    'A("tranquille").n(\'p\')=>tranquilles'


def test_declension_fr_2276():
    assert (
N("transformation").g('f').n('p').realize()   
    ) == 'transformations',\
    'N("transformation").g(\'f\').n(\'p\')=>transformations'


def test_declension_fr_2277():
    assert (
A("transparent").n('p').realize()   
    ) == 'transparents',\
    'A("transparent").n(\'p\')=>transparents'


def test_declension_fr_2278():
    assert (
N("transport").g('m').n('p').realize()   
    ) == 'transports',\
    'N("transport").g(\'m\').n(\'p\')=>transports'


def test_declension_fr_2279():
    assert (
N("travail").g('m').n('p').realize()   
    ) == 'travaux',\
    'N("travail").g(\'m\').n(\'p\')=>travaux'


def test_declension_fr_2280():
    assert (
N("travailleur").g('m').n('p').realize()   
    ) == 'travailleurs',\
    'N("travailleur").g(\'m\').n(\'p\')=>travailleurs'


def test_declension_fr_2281():
    assert (
N("travailleuse").g('f').n('p').realize()   
    ) == 'travailleuses',\
    'N("travailleuse").g(\'f\').n(\'p\')=>travailleuses'


def test_declension_fr_2282():
    assert (
N("travers").g('m').n('p').realize()   
    ) == 'travers',\
    'N("travers").g(\'m\').n(\'p\')=>travers'


def test_declension_fr_2283():
    assert (
N("trésor").g('m').n('p').realize()   
    ) == 'trésors',\
    'N("trésor").g(\'m\').n(\'p\')=>trésors'


def test_declension_fr_2284():
    assert (
N("tribunal").g('m').n('p').realize()   
    ) == 'tribunaux',\
    'N("tribunal").g(\'m\').n(\'p\')=>tribunaux'


def test_declension_fr_2285():
    assert (
A("tricolore").n('p').realize()   
    ) == 'tricolores',\
    'A("tricolore").n(\'p\')=>tricolores'


def test_declension_fr_2286():
    assert (
N("tricot").g('m').n('p').realize()   
    ) == 'tricots',\
    'N("tricot").g(\'m\').n(\'p\')=>tricots'


def test_declension_fr_2287():
    assert (
N("trimestre").g('m').n('p').realize()   
    ) == 'trimestres',\
    'N("trimestre").g(\'m\').n(\'p\')=>trimestres'


def test_declension_fr_2288():
    assert (
N("triomphe").g('m').n('p').realize()   
    ) == 'triomphes',\
    'N("triomphe").g(\'m\').n(\'p\')=>triomphes'


def test_declension_fr_2289():
    assert (
A("triste").n('p').realize()   
    ) == 'tristes',\
    'A("triste").n(\'p\')=>tristes'


def test_declension_fr_2290():
    assert (
N("tristesse").g('f').n('p').realize()   
    ) == 'tristesses',\
    'N("tristesse").g(\'f\').n(\'p\')=>tristesses'


def test_declension_fr_2291():
    assert (
N("trompette").g('f').n('p').realize()   
    ) == 'trompettes',\
    'N("trompette").g(\'f\').n(\'p\')=>trompettes'


def test_declension_fr_2292():
    assert (
N("tronc").g('m').n('p').realize()   
    ) == 'troncs',\
    'N("tronc").g(\'m\').n(\'p\')=>troncs'


def test_declension_fr_2293():
    assert (
N("trottoir").g('m').n('p').realize()   
    ) == 'trottoirs',\
    'N("trottoir").g(\'m\').n(\'p\')=>trottoirs'


def test_declension_fr_2294():
    assert (
N("trou").g('m').n('p').realize()   
    ) == 'trous',\
    'N("trou").g(\'m\').n(\'p\')=>trous'


def test_declension_fr_2295():
    assert (
N("trouble").g('m').n('p').realize()   
    ) == 'troubles',\
    'N("trouble").g(\'m\').n(\'p\')=>troubles'


def test_declension_fr_2296():
    assert (
N("troupe").g('f').n('p').realize()   
    ) == 'troupes',\
    'N("troupe").g(\'f\').n(\'p\')=>troupes'


def test_declension_fr_2297():
    assert (
N("troupeau").g('m').n('p').realize()   
    ) == 'troupeaux',\
    'N("troupeau").g(\'m\').n(\'p\')=>troupeaux'


def test_declension_fr_2298():
    assert (
N("tuile").g('f').n('p').realize()   
    ) == 'tuiles',\
    'N("tuile").g(\'f\').n(\'p\')=>tuiles'


def test_declension_fr_2299():
    assert (
N("tulipe").g('f').n('p').realize()   
    ) == 'tulipes',\
    'N("tulipe").g(\'f\').n(\'p\')=>tulipes'


def test_declension_fr_2300():
    assert (
N("tunnel").g('m').n('p').realize()   
    ) == 'tunnels',\
    'N("tunnel").g(\'m\').n(\'p\')=>tunnels'


def test_declension_fr_2301():
    assert (
A("turbulent").n('p').realize()   
    ) == 'turbulents',\
    'A("turbulent").n(\'p\')=>turbulents'


def test_declension_fr_2302():
    assert (
N("tuyau").g('m').n('p').realize()   
    ) == 'tuyaux',\
    'N("tuyau").g(\'m\').n(\'p\')=>tuyaux'


def test_declension_fr_2303():
    assert (
N("type").g('m').n('p').realize()   
    ) == 'types',\
    'N("type").g(\'m\').n(\'p\')=>types'


def test_declension_fr_2304():
    assert (
N("union").g('f').n('p').realize()   
    ) == 'unions',\
    'N("union").g(\'f\').n(\'p\')=>unions'


def test_declension_fr_2305():
    assert (
A("unique").n('p').realize()   
    ) == 'uniques',\
    'A("unique").n(\'p\')=>uniques'


def test_declension_fr_2306():
    assert (
N("univers").g('m').n('p').realize()   
    ) == 'univers',\
    'N("univers").g(\'m\').n(\'p\')=>univers'


def test_declension_fr_2307():
    assert (
A("universel").n('p').realize()   
    ) == 'universels',\
    'A("universel").n(\'p\')=>universels'


def test_declension_fr_2308():
    assert (
A("urgent").n('p').realize()   
    ) == 'urgents',\
    'A("urgent").n(\'p\')=>urgents'


def test_declension_fr_2309():
    assert (
N("usage").g('m').n('p').realize()   
    ) == 'usages',\
    'N("usage").g(\'m\').n(\'p\')=>usages'


def test_declension_fr_2310():
    assert (
N("usine").g('f').n('p').realize()   
    ) == 'usines',\
    'N("usine").g(\'f\').n(\'p\')=>usines'


def test_declension_fr_2311():
    assert (
A("utile").n('p').realize()   
    ) == 'utiles',\
    'A("utile").n(\'p\')=>utiles'


def test_declension_fr_2312():
    assert (
N("utilité").g('f').n('p').realize()   
    ) == 'utilités',\
    'N("utilité").g(\'f\').n(\'p\')=>utilités'


def test_declension_fr_2313():
    assert (
N("vache").g('f').n('p').realize()   
    ) == 'vaches',\
    'N("vache").g(\'f\').n(\'p\')=>vaches'


def test_declension_fr_2314():
    assert (
A("vagabond").n('p').realize()   
    ) == 'vagabonds',\
    'A("vagabond").n(\'p\')=>vagabonds'


def test_declension_fr_2315():
    assert (
N("vague").g('f').n('p').realize()   
    ) == 'vagues',\
    'N("vague").g(\'f\').n(\'p\')=>vagues'


def test_declension_fr_2316():
    assert (
A("vaillant").n('p').realize()   
    ) == 'vaillants',\
    'A("vaillant").n(\'p\')=>vaillants'


def test_declension_fr_2317():
    assert (
A("vain").n('p').realize()   
    ) == 'vains',\
    'A("vain").n(\'p\')=>vains'


def test_declension_fr_2318():
    assert (
N("vainqueur").g('m').n('p').realize()   
    ) == 'vainqueurs',\
    'N("vainqueur").g(\'m\').n(\'p\')=>vainqueurs'


def test_declension_fr_2319():
    assert (
N("vaisseau").n('p').realize()   
    ) == 'vaisseaux',\
    'N("vaisseau").n(\'p\')=>vaisseaux'


def test_declension_fr_2320():
    assert (
N("vaisselle").g('f').n('p').realize()   
    ) == 'vaisselles',\
    'N("vaisselle").g(\'f\').n(\'p\')=>vaisselles'


def test_declension_fr_2321():
    assert (
N("valet").g('m').n('p').realize()   
    ) == 'valets',\
    'N("valet").g(\'m\').n(\'p\')=>valets'


def test_declension_fr_2322():
    assert (
N("valeur").g('f').n('p').realize()   
    ) == 'valeurs',\
    'N("valeur").g(\'f\').n(\'p\')=>valeurs'


def test_declension_fr_2323():
    assert (
N("valise").g('f').n('p').realize()   
    ) == 'valises',\
    'N("valise").g(\'f\').n(\'p\')=>valises'


def test_declension_fr_2324():
    assert (
N("vallée").g('f').n('p').realize()   
    ) == 'vallées',\
    'N("vallée").g(\'f\').n(\'p\')=>vallées'


def test_declension_fr_2325():
    assert (
N("vapeur").g('f').n('p').realize()   
    ) == 'vapeurs',\
    'N("vapeur").g(\'f\').n(\'p\')=>vapeurs'


def test_declension_fr_2326():
    assert (
N("vase").g('m').n('p').realize()   
    ) == 'vases',\
    'N("vase").g(\'m\').n(\'p\')=>vases'


def test_declension_fr_2327():
    assert (
A("vaste").n('p').realize()   
    ) == 'vastes',\
    'A("vaste").n(\'p\')=>vastes'


def test_declension_fr_2328():
    assert (
N("veau").g('m').n('p').realize()   
    ) == 'veaux',\
    'N("veau").g(\'m\').n(\'p\')=>veaux'


def test_declension_fr_2329():
    assert (
A("végétal").n('p').realize()   
    ) == 'végétaux',\
    'A("végétal").n(\'p\')=>végétaux'


def test_declension_fr_2330():
    assert (
N("végétation").g('f').n('p').realize()   
    ) == 'végétations',\
    'N("végétation").g(\'f\').n(\'p\')=>végétations'


def test_declension_fr_2331():
    assert (
N("véhicule").g('m').n('p').realize()   
    ) == 'véhicules',\
    'N("véhicule").g(\'m\').n(\'p\')=>véhicules'


def test_declension_fr_2332():
    assert (
N("veille").g('f').n('p').realize()   
    ) == 'veilles',\
    'N("veille").g(\'f\').n(\'p\')=>veilles'


def test_declension_fr_2333():
    assert (
N("veine").g('f').n('p').realize()   
    ) == 'veines',\
    'N("veine").g(\'f\').n(\'p\')=>veines'


def test_declension_fr_2334():
    assert (
N("vélo").g('m').n('p').realize()   
    ) == 'vélos',\
    'N("vélo").g(\'m\').n(\'p\')=>vélos'


def test_declension_fr_2335():
    assert (
N("velours").g('m').n('p').realize()   
    ) == 'velours',\
    'N("velours").g(\'m\').n(\'p\')=>velours'


def test_declension_fr_2336():
    assert (
A("velouté").n('p').realize()   
    ) == 'veloutés',\
    'A("velouté").n(\'p\')=>veloutés'


def test_declension_fr_2337():
    assert (
N("vendeur").g('m').n('p').realize()   
    ) == 'vendeurs',\
    'N("vendeur").g(\'m\').n(\'p\')=>vendeurs'


def test_declension_fr_2338():
    assert (
N("vendredi").g('m').n('p').realize()   
    ) == 'vendredis',\
    'N("vendredi").g(\'m\').n(\'p\')=>vendredis'


def test_declension_fr_2339():
    assert (
N("vent").g('m').n('p').realize()   
    ) == 'vents',\
    'N("vent").g(\'m\').n(\'p\')=>vents'


def test_declension_fr_2340():
    assert (
N("vente").g('f').n('p').realize()   
    ) == 'ventes',\
    'N("vente").g(\'f\').n(\'p\')=>ventes'


def test_declension_fr_2341():
    assert (
N("ventre").g('m').n('p').realize()   
    ) == 'ventres',\
    'N("ventre").g(\'m\').n(\'p\')=>ventres'


def test_declension_fr_2342():
    assert (
N("vêpres").g('f').n('p').realize()   
    ) == 'vêpres',\
    'N("vêpres").g(\'f\').n(\'p\')=>vêpres'


def test_declension_fr_2343():
    assert (
N("ver").g('m').n('p').realize()   
    ) == 'vers',\
    'N("ver").g(\'m\').n(\'p\')=>vers'


def test_declension_fr_2344():
    assert (
A("verdâtre").n('p').realize()   
    ) == 'verdâtres',\
    'A("verdâtre").n(\'p\')=>verdâtres'


def test_declension_fr_2345():
    assert (
A("verdoyant").n('p').realize()   
    ) == 'verdoyants',\
    'A("verdoyant").n(\'p\')=>verdoyants'


def test_declension_fr_2346():
    assert (
N("verdure").g('f').n('p').realize()   
    ) == 'verdures',\
    'N("verdure").g(\'f\').n(\'p\')=>verdures'


def test_declension_fr_2347():
    assert (
N("verger").g('m').n('p').realize()   
    ) == 'vergers',\
    'N("verger").g(\'m\').n(\'p\')=>vergers'


def test_declension_fr_2348():
    assert (
A("véritable").n('p').realize()   
    ) == 'véritables',\
    'A("véritable").n(\'p\')=>véritables'


def test_declension_fr_2349():
    assert (
N("vérité").g('f').n('p').realize()   
    ) == 'vérités',\
    'N("vérité").g(\'f\').n(\'p\')=>vérités'


def test_declension_fr_2350():
    assert (
N("vermeil").g('m').n('p').realize()   
    ) == 'vermeils',\
    'N("vermeil").g(\'m\').n(\'p\')=>vermeils'


def test_declension_fr_2351():
    assert (
N("verre").g('m').n('p').realize()   
    ) == 'verres',\
    'N("verre").g(\'m\').n(\'p\')=>verres'


def test_declension_fr_2352():
    assert (
A("vert").n('p').realize()   
    ) == 'verts',\
    'A("vert").n(\'p\')=>verts'


def test_declension_fr_2353():
    assert (
N("vertu").g('f').n('p').realize()   
    ) == 'vertus',\
    'N("vertu").g(\'f\').n(\'p\')=>vertus'


def test_declension_fr_2354():
    assert (
N("veston").g('m').n('p').realize()   
    ) == 'vestons',\
    'N("veston").g(\'m\').n(\'p\')=>vestons'


def test_declension_fr_2355():
    assert (
N("vêtement").g('m').n('p').realize()   
    ) == 'vêtements',\
    'N("vêtement").g(\'m\').n(\'p\')=>vêtements'


def test_declension_fr_2356():
    assert (
A("veuf").n('p').realize()   
    ) == 'veufs',\
    'A("veuf").n(\'p\')=>veufs'


def test_declension_fr_2357():
    assert (
N("viande").g('f').n('p').realize()   
    ) == 'viandes',\
    'N("viande").g(\'f\').n(\'p\')=>viandes'


def test_declension_fr_2358():
    assert (
N("vicaire").g('m').n('p').realize()   
    ) == 'vicaires',\
    'N("vicaire").g(\'m\').n(\'p\')=>vicaires'


def test_declension_fr_2359():
    assert (
N("vice").g('m').n('p').realize()   
    ) == 'vices',\
    'N("vice").g(\'m\').n(\'p\')=>vices'


def test_declension_fr_2360():
    assert (
N("victime").g('f').n('p').realize()   
    ) == 'victimes',\
    'N("victime").g(\'f\').n(\'p\')=>victimes'


def test_declension_fr_2361():
    assert (
N("victoire").g('f').n('p').realize()   
    ) == 'victoires',\
    'N("victoire").g(\'f\').n(\'p\')=>victoires'


def test_declension_fr_2362():
    assert (
A("vide").n('p').realize()   
    ) == 'vides',\
    'A("vide").n(\'p\')=>vides'


def test_declension_fr_2363():
    assert (
N("vie").g('f').n('p').realize()   
    ) == 'vies',\
    'N("vie").g(\'f\').n(\'p\')=>vies'


def test_declension_fr_2364():
    assert (
N("vieillard").g('m').n('p').realize()   
    ) == 'vieillards',\
    'N("vieillard").g(\'m\').n(\'p\')=>vieillards'


def test_declension_fr_2365():
    assert (
N("vieillesse").g('f').n('p').realize()   
    ) == 'vieillesses',\
    'N("vieillesse").g(\'f\').n(\'p\')=>vieillesses'


def test_declension_fr_2366():
    assert (
A("vierge").n('p').realize()   
    ) == 'vierges',\
    'A("vierge").n(\'p\')=>vierges'


def test_declension_fr_2367():
    assert (
A("vieux").n('p').realize()   
    ) == 'vieux',\
    'A("vieux").n(\'p\')=>vieux'


def test_declension_fr_2368():
    assert (
A("vif").n('p').realize()   
    ) == 'vifs',\
    'A("vif").n(\'p\')=>vifs'


def test_declension_fr_2369():
    assert (
N("vigne").g('f').n('p').realize()   
    ) == 'vignes',\
    'N("vigne").g(\'f\').n(\'p\')=>vignes'


def test_declension_fr_2370():
    assert (
A("vigoureux").n('p').realize()   
    ) == 'vigoureux',\
    'A("vigoureux").n(\'p\')=>vigoureux'


def test_declension_fr_2371():
    assert (
N("vigueur").g('f').n('p').realize()   
    ) == 'vigueurs',\
    'N("vigueur").g(\'f\').n(\'p\')=>vigueurs'


def test_declension_fr_2372():
    assert (
A("vilain").n('p').realize()   
    ) == 'vilains',\
    'A("vilain").n(\'p\')=>vilains'


def test_declension_fr_2373():
    assert (
N("villa").g('f').n('p').realize()   
    ) == 'villas',\
    'N("villa").g(\'f\').n(\'p\')=>villas'


def test_declension_fr_2374():
    assert (
N("village").g('m').n('p').realize()   
    ) == 'villages',\
    'N("village").g(\'m\').n(\'p\')=>villages'


def test_declension_fr_2375():
    assert (
N("villageois").g('m').n('p').realize()   
    ) == 'villageois',\
    'N("villageois").g(\'m\').n(\'p\')=>villageois'


def test_declension_fr_2376():
    assert (
N("ville").g('f').n('p').realize()   
    ) == 'villes',\
    'N("ville").g(\'f\').n(\'p\')=>villes'


def test_declension_fr_2377():
    assert (
N("vin").g('m').n('p').realize()   
    ) == 'vins',\
    'N("vin").g(\'m\').n(\'p\')=>vins'


def test_declension_fr_2378():
    assert (
N("violence").g('f').n('p').realize()   
    ) == 'violences',\
    'N("violence").g(\'f\').n(\'p\')=>violences'


def test_declension_fr_2379():
    assert (
A("violent").n('p').realize()   
    ) == 'violents',\
    'A("violent").n(\'p\')=>violents'


def test_declension_fr_2380():
    assert (
A("violet").n('p').realize()   
    ) == 'violets',\
    'A("violet").n(\'p\')=>violets'


def test_declension_fr_2381():
    assert (
N("violette").g('f').n('p').realize()   
    ) == 'violettes',\
    'N("violette").g(\'f\').n(\'p\')=>violettes'


def test_declension_fr_2382():
    assert (
N("visage").g('m').n('p').realize()   
    ) == 'visages',\
    'N("visage").g(\'m\').n(\'p\')=>visages'


def test_declension_fr_2383():
    assert (
A("visible").n('p').realize()   
    ) == 'visibles',\
    'A("visible").n(\'p\')=>visibles'


def test_declension_fr_2384():
    assert (
N("visite").g('f').n('p').realize()   
    ) == 'visites',\
    'N("visite").g(\'f\').n(\'p\')=>visites'


def test_declension_fr_2385():
    assert (
N("visiteur").g('m').n('p').realize()   
    ) == 'visiteurs',\
    'N("visiteur").g(\'m\').n(\'p\')=>visiteurs'


def test_declension_fr_2386():
    assert (
N("vitesse").g('f').n('p').realize()   
    ) == 'vitesses',\
    'N("vitesse").g(\'f\').n(\'p\')=>vitesses'


def test_declension_fr_2387():
    assert (
N("vitre").g('f').n('p').realize()   
    ) == 'vitres',\
    'N("vitre").g(\'f\').n(\'p\')=>vitres'


def test_declension_fr_2388():
    assert (
N("vitrine").g('f').n('p').realize()   
    ) == 'vitrines',\
    'N("vitrine").g(\'f\').n(\'p\')=>vitrines'


def test_declension_fr_2389():
    assert (
A("vivant").n('p').realize()   
    ) == 'vivants',\
    'A("vivant").n(\'p\')=>vivants'


def test_declension_fr_2390():
    assert (
N("voie").g('f').n('p').realize()   
    ) == 'voies',\
    'N("voie").g(\'f\').n(\'p\')=>voies'


def test_declension_fr_2391():
    assert (
N("voile").g('f').n('p').realize()   
    ) == 'voiles',\
    'N("voile").g(\'f\').n(\'p\')=>voiles'


def test_declension_fr_2392():
    assert (
N("voisin").g('m').n('p').realize()   
    ) == 'voisins',\
    'N("voisin").g(\'m\').n(\'p\')=>voisins'


def test_declension_fr_2393():
    assert (
N("voisinage").g('m').n('p').realize()   
    ) == 'voisinages',\
    'N("voisinage").g(\'m\').n(\'p\')=>voisinages'


def test_declension_fr_2394():
    assert (
N("voiture").g('f').n('p').realize()   
    ) == 'voitures',\
    'N("voiture").g(\'f\').n(\'p\')=>voitures'


def test_declension_fr_2395():
    assert (
N("voix").g('f').n('p').realize()   
    ) == 'voix',\
    'N("voix").g(\'f\').n(\'p\')=>voix'


def test_declension_fr_2396():
    assert (
N("vol").g('m').n('p').realize()   
    ) == 'vols',\
    'N("vol").g(\'m\').n(\'p\')=>vols'


def test_declension_fr_2397():
    assert (
N("volaille").g('f').n('p').realize()   
    ) == 'volailles',\
    'N("volaille").g(\'f\').n(\'p\')=>volailles'


def test_declension_fr_2398():
    assert (
N("volée").g('f').n('p').realize()   
    ) == 'volées',\
    'N("volée").g(\'f\').n(\'p\')=>volées'


def test_declension_fr_2399():
    assert (
N("volet").g('m').n('p').realize()   
    ) == 'volets',\
    'N("volet").g(\'m\').n(\'p\')=>volets'


def test_declension_fr_2400():
    assert (
N("voleur").g('m').n('p').realize()   
    ) == 'voleurs',\
    'N("voleur").g(\'m\').n(\'p\')=>voleurs'


def test_declension_fr_2401():
    assert (
N("volonté").g('f').n('p').realize()   
    ) == 'volontés',\
    'N("volonté").g(\'f\').n(\'p\')=>volontés'


def test_declension_fr_2402():
    assert (
N("volume").g('m').n('p').realize()   
    ) == 'volumes',\
    'N("volume").g(\'m\').n(\'p\')=>volumes'


def test_declension_fr_2403():
    assert (
N("voûte").g('f').n('p').realize()   
    ) == 'voûtes',\
    'N("voûte").g(\'f\').n(\'p\')=>voûtes'


def test_declension_fr_2404():
    assert (
N("voyage").g('m').n('p').realize()   
    ) == 'voyages',\
    'N("voyage").g(\'m\').n(\'p\')=>voyages'


def test_declension_fr_2405():
    assert (
N("voyageur").g('m').n('p').realize()   
    ) == 'voyageurs',\
    'N("voyageur").g(\'m\').n(\'p\')=>voyageurs'


def test_declension_fr_2406():
    assert (
A("vrai").n('p').realize()   
    ) == 'vrais',\
    'A("vrai").n(\'p\')=>vrais'


def test_declension_fr_2407():
    assert (
N("vue").g('f').n('p').realize()   
    ) == 'vues',\
    'N("vue").g(\'f\').n(\'p\')=>vues'


def test_declension_fr_2408():
    assert (
A("vulgaire").n('p').realize()   
    ) == 'vulgaires',\
    'A("vulgaire").n(\'p\')=>vulgaires'


def test_declension_fr_2409():
    assert (
N("wagon").g('m').n('p').realize()   
    ) == 'wagons',\
    'N("wagon").g(\'m\').n(\'p\')=>wagons'


def test_declension_fr_2410():
    assert (
N("zèle").g('m').n('p').realize()   
    ) == 'zèles',\
    'N("zèle").g(\'m\').n(\'p\')=>zèles'


def test_declension_fr_2411():
    assert (
Pro("je").g('m').n('s').pe(2).realize()   
    ) == 'tu',\
    'Pro("je").g(\'m\').n(\'s\').pe(2)=>tu'


def test_declension_fr_2412():
    assert (
Pro("je").g('m').n('p').pe(3).realize()   
    ) == 'ils',\
    'Pro("je").g(\'m\').n(\'p\').pe(3)=>ils'


def test_declension_fr_2413():
    assert (
Pro("je").g('f').n('s').pe(3).realize()   
    ) == 'elle',\
    'Pro("je").g(\'f\').n(\'s\').pe(3)=>elle'


def test_declension_fr_2414():
    assert (
Pro("moi").g('m').n('s').pe(2).realize()   
    ) == 'toi',\
    'Pro("moi").g(\'m\').n(\'s\').pe(2)=>toi'


def test_declension_fr_2415():
    assert (
Pro("moi").g('m').n('p').pe(3).realize()   
    ) == 'eux',\
    'Pro("moi").g(\'m\').n(\'p\').pe(3)=>eux'


def test_declension_fr_2416():
    assert (
Pro("moi").g('f').n('s').pe(3).realize()   
    ) == 'elle',\
    'Pro("moi").g(\'f\').n(\'s\').pe(3)=>elle'


def test_declension_fr_2417():
    assert (
Pro("lequel").g('m').n('s').pe(2).realize()   
    ) == 'lequel',\
    'Pro("lequel").g(\'m\').n(\'s\').pe(2)=>lequel'


def test_declension_fr_2418():
    assert (
Pro("lequel").g('m').n('p').pe(3).realize()   
    ) == 'lesquels',\
    'Pro("lequel").g(\'m\').n(\'p\').pe(3)=>lesquels'


def test_declension_fr_2419():
    assert (
Pro("lequel").g('f').n('s').pe(3).realize()   
    ) == 'laquelle',\
    'Pro("lequel").g(\'f\').n(\'s\').pe(3)=>laquelle'


def test_declension_fr_2420():
    assert (
Pro("celui-ci").g('m').n('s').pe(3).realize()   
    ) == 'celui-ci',\
    'Pro("celui-ci").g(\'m\').n(\'s\').pe(3)=>celui-ci'


def test_declension_fr_2421():
    assert (
Pro("celui-ci").g('m').n('p').pe(3).realize()   
    ) == 'ceux-ci',\
    'Pro("celui-ci").g(\'m\').n(\'p\').pe(3)=>ceux-ci'


def test_declension_fr_2422():
    assert (
Pro("celui-ci").g('f').n('s').pe(3).realize()   
    ) == 'celle-ci',\
    'Pro("celui-ci").g(\'f\').n(\'s\').pe(3)=>celle-ci'


def test_declension_fr_2423():
    assert (
Pro("qui").g('m').n('s').pe(2).realize()   
    ) == 'qui',\
    'Pro("qui").g(\'m\').n(\'s\').pe(2)=>qui'


def test_declension_fr_2424():
    assert (
Pro("qui").g('m').n('p').pe(3).realize()   
    ) == 'qui',\
    'Pro("qui").g(\'m\').n(\'p\').pe(3)=>qui'


def test_declension_fr_2425():
    assert (
Pro("qui").g('f').n('s').pe(3).realize()   
    ) == 'qui',\
    'Pro("qui").g(\'f\').n(\'s\').pe(3)=>qui'


def test_declension_fr_2426():
    assert (
Pro("quoi").g('m').n('s').pe(2).realize()   
    ) == 'quoi',\
    'Pro("quoi").g(\'m\').n(\'s\').pe(2)=>quoi'


def test_declension_fr_2427():
    assert (
Pro("quoi").g('m').n('p').pe(3).realize()   
    ) == 'quoi',\
    'Pro("quoi").g(\'m\').n(\'p\').pe(3)=>quoi'


def test_declension_fr_2428():
    assert (
Pro("quoi").g('f').n('s').pe(3).realize()   
    ) == 'quoi',\
    'Pro("quoi").g(\'f\').n(\'s\').pe(3)=>quoi'


def test_declension_fr_2429():
    assert (
Pro("où").g('m').n('s').pe(2).realize()   
    ) == 'où',\
    'Pro("où").g(\'m\').n(\'s\').pe(2)=>où'


def test_declension_fr_2430():
    assert (
Pro("où").g('m').n('p').pe(3).realize()   
    ) == 'où',\
    'Pro("où").g(\'m\').n(\'p\').pe(3)=>où'


def test_declension_fr_2431():
    assert (
Pro("où").g('f').n('s').pe(3).realize()   
    ) == 'où',\
    'Pro("où").g(\'f\').n(\'s\').pe(3)=>où'


def test_declension_fr_2432():
    assert (
Pro("ce").g('m').n('s').pe(2).realize()   
    ) == 'ce',\
    'Pro("ce").g(\'m\').n(\'s\').pe(2)=>ce'


def test_declension_fr_2433():
    assert (
Pro("ce").g('m').n('p').pe(3).realize()   
    ) == 'ce',\
    'Pro("ce").g(\'m\').n(\'p\').pe(3)=>ce'


def test_declension_fr_2434():
    assert (
Pro("ce").g('f').n('s').pe(3).realize()   
    ) == 'ce',\
    'Pro("ce").g(\'f\').n(\'s\').pe(3)=>ce'


def test_declension_fr_2435():
    assert (
Pro("que").g('m').n('s').pe(2).realize()   
    ) == 'que',\
    'Pro("que").g(\'m\').n(\'s\').pe(2)=>que'


def test_declension_fr_2436():
    assert (
Pro("que").g('m').n('p').pe(3).realize()   
    ) == 'que',\
    'Pro("que").g(\'m\').n(\'p\').pe(3)=>que'


def test_declension_fr_2437():
    assert (
Pro("que").g('f').n('s').pe(3).realize()   
    ) == 'que',\
    'Pro("que").g(\'f\').n(\'s\').pe(3)=>que'

