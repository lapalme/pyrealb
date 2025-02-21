import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..','src')))

from pyrealb import *
load("en")

def test_declension_en_0():
    assert (
N("activity").n('p').realize()   
    ) == 'activities',\
    'N("activity").n(\'p\')=>activities'


def test_declension_en_1():
    assert (
Adv("all").f('co').realize()   
    ) == 'all',\
    'Adv("all").f(\'co\')=>all'


def test_declension_en_2():
    assert (
N("analysis").n('p').realize()   
    ) == 'analyses',\
    'N("analysis").n(\'p\')=>analyses'


def test_declension_en_3():
    assert (
N("audience").n('p').realize()   
    ) == 'audiences',\
    'N("audience").n(\'p\')=>audiences'


def test_declension_en_4():
    assert (
N("avocado").n('p').realize()   
    ) == 'avocados',\
    'N("avocado").n(\'p\')=>avocados'


def test_declension_en_5():
    assert (
A("bad").f('co').realize()   
    ) == 'worse',\
    'A("bad").f(\'co\')=>worse'


def test_declension_en_6():
    assert (
A("bad").f('su').realize()   
    ) == 'worst',\
    'A("bad").f(\'su\')=>worst'


def test_declension_en_7():
    assert (
Adv("badly").f('co').realize()   
    ) == 'worse',\
    'Adv("badly").f(\'co\')=>worse'


def test_declension_en_8():
    assert (
N("basis").n('p').realize()   
    ) == 'bases',\
    'N("basis").n(\'p\')=>bases'


def test_declension_en_9():
    assert (
N("batch").n('p').realize()   
    ) == 'batches',\
    'N("batch").n(\'p\')=>batches'


def test_declension_en_10():
    assert (
N("berry").n('p').realize()   
    ) == 'berries',\
    'N("berry").n(\'p\')=>berries'


def test_declension_en_11():
    assert (
A("big").f('co').realize()   
    ) == 'bigger',\
    'A("big").f(\'co\')=>bigger'


def test_declension_en_12():
    assert (
A("big").f('su').realize()   
    ) == 'biggest',\
    'A("big").f(\'su\')=>biggest'


def test_declension_en_13():
    assert (
N("box").n('p').realize()   
    ) == 'boxes',\
    'N("box").n(\'p\')=>boxes'


def test_declension_en_14():
    assert (
N("boy").n('p').realize()   
    ) == 'boys',\
    'N("boy").n(\'p\')=>boys'


def test_declension_en_15():
    assert (
N("bunch").n('p').realize()   
    ) == 'bunches',\
    'N("bunch").n(\'p\')=>bunches'


def test_declension_en_16():
    assert (
N("bus").n('p').realize()   
    ) == 'buses',\
    'N("bus").n(\'p\')=>buses'


def test_declension_en_17():
    assert (
N("businessman").n('p').realize()   
    ) == 'businessmen',\
    'N("businessman").n(\'p\')=>businessmen'


def test_declension_en_18():
    assert (
N("calf").n('p').realize()   
    ) == 'calves',\
    'N("calf").n(\'p\')=>calves'


def test_declension_en_19():
    assert (
N("car").n('p').realize()   
    ) == 'cars',\
    'N("car").n(\'p\')=>cars'


def test_declension_en_20():
    assert (
N("cargo").n('p').realize()   
    ) == 'cargoes',\
    'N("cargo").n(\'p\')=>cargoes'


def test_declension_en_21():
    assert (
N("cattle").n('p').realize()   
    ) == 'cattle',\
    'N("cattle").n(\'p\')=>cattle'


def test_declension_en_22():
    assert (
N("chairman").n('p').realize()   
    ) == 'chairmen',\
    'N("chairman").n(\'p\')=>chairmen'


def test_declension_en_23():
    assert (
N("chief").n('p').realize()   
    ) == 'chiefs',\
    'N("chief").n(\'p\')=>chiefs'


def test_declension_en_24():
    assert (
N("child").n('p').realize()   
    ) == 'children',\
    'N("child").n(\'p\')=>children'


def test_declension_en_25():
    assert (
N("choir").n('p').realize()   
    ) == 'choirs',\
    'N("choir").n(\'p\')=>choirs'


def test_declension_en_26():
    assert (
N("church").n('p').realize()   
    ) == 'churches',\
    'N("church").n(\'p\')=>churches'


def test_declension_en_27():
    assert (
N("city").n('p').realize()   
    ) == 'cities',\
    'N("city").n(\'p\')=>cities'


def test_declension_en_28():
    assert (
A("civil").f('co').realize()   
    ) == 'civiller',\
    'A("civil").f(\'co\')=>civiller'


def test_declension_en_29():
    assert (
A("civil").f('su').realize()   
    ) == 'civillest',\
    'A("civil").f(\'su\')=>civillest'


def test_declension_en_30():
    assert (
N("clergy").n('p').realize()   
    ) == 'clergies',\
    'N("clergy").n(\'p\')=>clergies'


def test_declension_en_31():
    assert (
N("clothes").n('p').realize()   
    ) == 'clothes',\
    'N("clothes").n(\'p\')=>clothes'


def test_declension_en_32():
    assert (
N("coalition").n('p').realize()   
    ) == 'coalitions',\
    'N("coalition").n(\'p\')=>coalitions'


def test_declension_en_33():
    assert (
N("collection").n('p').realize()   
    ) == 'collections',\
    'N("collection").n(\'p\')=>collections'


def test_declension_en_34():
    assert (
N("committee").n('p').realize()   
    ) == 'committees',\
    'N("committee").n(\'p\')=>committees'


def test_declension_en_35():
    assert (
N("commons").n('p').realize()   
    ) == 'commons',\
    'N("commons").n(\'p\')=>commons'


def test_declension_en_36():
    assert (
N("constituency").n('p').realize()   
    ) == 'constituencies',\
    'N("constituency").n(\'p\')=>constituencies'


def test_declension_en_37():
    assert (
N("corps").n('p').realize()   
    ) == 'corps',\
    'N("corps").n(\'p\')=>corps'


def test_declension_en_38():
    assert (
N("council").n('p').realize()   
    ) == 'councils',\
    'N("council").n(\'p\')=>councils'


def test_declension_en_39():
    assert (
N("craftsman").n('p').realize()   
    ) == 'craftsmen',\
    'N("craftsman").n(\'p\')=>craftsmen'


def test_declension_en_40():
    assert (
N("crew").n('p').realize()   
    ) == 'crews',\
    'N("crew").n(\'p\')=>crews'


def test_declension_en_41():
    assert (
N("crisis").n('p').realize()   
    ) == 'crises',\
    'N("crisis").n(\'p\')=>crises'


def test_declension_en_42():
    assert (
N("day").n('p').realize()   
    ) == 'days',\
    'N("day").n(\'p\')=>days'


def test_declension_en_43():
    assert (
N("diagnosis").n('p').realize()   
    ) == 'diagnoses',\
    'N("diagnosis").n(\'p\')=>diagnoses'


def test_declension_en_44():
    assert (
N("elite").n('p').realize()   
    ) == 'elites',\
    'N("elite").n(\'p\')=>elites'


def test_declension_en_45():
    assert (
N("emphasis").n('p').realize()   
    ) == 'emphases',\
    'N("emphasis").n(\'p\')=>emphases'


def test_declension_en_46():
    assert (
N("establishment").n('p').realize()   
    ) == 'establishments',\
    'N("establishment").n(\'p\')=>establishments'


def test_declension_en_47():
    assert (
A("far").f('co').realize()   
    ) == 'farther',\
    'A("far").f(\'co\')=>farther'


def test_declension_en_48():
    assert (
A("far").f('su').realize()   
    ) == 'farthest',\
    'A("far").f(\'su\')=>farthest'


def test_declension_en_49():
    assert (
A("fat").f('co').realize()   
    ) == 'fatter',\
    'A("fat").f(\'co\')=>fatter'


def test_declension_en_50():
    assert (
A("fat").f('su').realize()   
    ) == 'fattest',\
    'A("fat").f(\'su\')=>fattest'


def test_declension_en_51():
    assert (
N("fisherman").n('p').realize()   
    ) == 'fishermen',\
    'N("fisherman").n(\'p\')=>fishermen'


def test_declension_en_52():
    assert (
A("fit").f('co').realize()   
    ) == 'fitter',\
    'A("fit").f(\'co\')=>fitter'


def test_declension_en_53():
    assert (
A("fit").f('su').realize()   
    ) == 'fittest',\
    'A("fit").f(\'su\')=>fittest'


def test_declension_en_54():
    assert (
A("flat").f('co').realize()   
    ) == 'flatter',\
    'A("flat").f(\'co\')=>flatter'


def test_declension_en_55():
    assert (
A("flat").f('su').realize()   
    ) == 'flattest',\
    'A("flat").f(\'su\')=>flattest'


def test_declension_en_56():
    assert (
N("fleet").n('p').realize()   
    ) == 'fleets',\
    'N("fleet").n(\'p\')=>fleets'


def test_declension_en_57():
    assert (
N("foot").n('p').realize()   
    ) == 'feet',\
    'N("foot").n(\'p\')=>feet'


def test_declension_en_58():
    assert (
N("formula").n('p').realize()   
    ) == 'formulas',\
    'N("formula").n(\'p\')=>formulas'


def test_declension_en_59():
    assert (
N("gang").n('p').realize()   
    ) == 'gangs',\
    'N("gang").n(\'p\')=>gangs'


def test_declension_en_60():
    assert (
N("gentleman").n('p').realize()   
    ) == 'gentlemen',\
    'N("gentleman").n(\'p\')=>gentlemen'


def test_declension_en_61():
    assert (
A("glad").f('co').realize()   
    ) == 'gladder',\
    'A("glad").f(\'co\')=>gladder'


def test_declension_en_62():
    assert (
A("glad").f('su').realize()   
    ) == 'gladdest',\
    'A("glad").f(\'su\')=>gladdest'


def test_declension_en_63():
    assert (
N("go").n('p').realize()   
    ) == 'goes',\
    'N("go").n(\'p\')=>goes'


def test_declension_en_64():
    assert (
A("good").f('co').realize()   
    ) == 'better',\
    'A("good").f(\'co\')=>better'


def test_declension_en_65():
    assert (
A("good").f('su').realize()   
    ) == 'best',\
    'A("good").f(\'su\')=>best'


def test_declension_en_66():
    assert (
N("government").n('p').realize()   
    ) == 'governments',\
    'N("government").n(\'p\')=>governments'


def test_declension_en_67():
    assert (
A("grim").f('co').realize()   
    ) == 'grimmer',\
    'A("grim").f(\'co\')=>grimmer'


def test_declension_en_68():
    assert (
A("grim").f('su').realize()   
    ) == 'grimmest',\
    'A("grim").f(\'su\')=>grimmest'


def test_declension_en_69():
    assert (
N("half").n('p').realize()   
    ) == 'halves',\
    'N("half").n(\'p\')=>halves'


def test_declension_en_70():
    assert (
N("handful").n('p').realize()   
    ) == 'handfuls',\
    'N("handful").n(\'p\')=>handfuls'


def test_declension_en_71():
    assert (
N("headquarters").n('p').realize()   
    ) == 'headquarters',\
    'N("headquarters").n(\'p\')=>headquarters'


def test_declension_en_72():
    assert (
N("herd").n('p').realize()   
    ) == 'herds',\
    'N("herd").n(\'p\')=>herds'


def test_declension_en_73():
    assert (
N("hero").n('p').realize()   
    ) == 'heroes',\
    'N("hero").n(\'p\')=>heroes'


def test_declension_en_74():
    assert (
A("hot").f('co').realize()   
    ) == 'hotter',\
    'A("hot").f(\'co\')=>hotter'


def test_declension_en_75():
    assert (
A("hot").f('su').realize()   
    ) == 'hottest',\
    'A("hot").f(\'su\')=>hottest'


def test_declension_en_76():
    assert (
N("household").n('p').realize()   
    ) == 'households',\
    'N("household").n(\'p\')=>households'


def test_declension_en_77():
    assert (
N("housewife").n('p').realize()   
    ) == 'housewives',\
    'N("housewife").n(\'p\')=>housewives'


def test_declension_en_78():
    assert (
N("hypothesis").n('p').realize()   
    ) == 'hypotheses',\
    'N("hypothesis").n(\'p\')=>hypotheses'


def test_declension_en_79():
    assert (
N("jeans").n('p').realize()   
    ) == 'jeans',\
    'N("jeans").n(\'p\')=>jeans'


def test_declension_en_80():
    assert (
N("knife").n('p').realize()   
    ) == 'knives',\
    'N("knife").n(\'p\')=>knives'


def test_declension_en_81():
    assert (
N("lab").n('p').realize()   
    ) == 'labs',\
    'N("lab").n(\'p\')=>labs'


def test_declension_en_82():
    assert (
N("life").n('p').realize()   
    ) == 'lives',\
    'N("life").n(\'p\')=>lives'


def test_declension_en_83():
    assert (
Adv("little").f('co').realize()   
    ) == 'less',\
    'Adv("little").f(\'co\')=>less'


def test_declension_en_84():
    assert (
A("loyal").f('co').realize()   
    ) == 'loyaller',\
    'A("loyal").f(\'co\')=>loyaller'


def test_declension_en_85():
    assert (
A("loyal").f('su').realize()   
    ) == 'loyallest',\
    'A("loyal").f(\'su\')=>loyallest'


def test_declension_en_86():
    assert (
A("mad").f('co').realize()   
    ) == 'madder',\
    'A("mad").f(\'co\')=>madder'


def test_declension_en_87():
    assert (
A("mad").f('su').realize()   
    ) == 'maddest',\
    'A("mad").f(\'su\')=>maddest'


def test_declension_en_88():
    assert (
N("man").n('p').realize()   
    ) == 'men',\
    'N("man").n(\'p\')=>men'


def test_declension_en_89():
    assert (
N("management").n('p').realize()   
    ) == 'managements',\
    'N("management").n(\'p\')=>managements'


def test_declension_en_90():
    assert (
N("monarch").n('p').realize()   
    ) == 'monarchs',\
    'N("monarch").n(\'p\')=>monarchs'


def test_declension_en_91():
    assert (
N("mouse").n('p').realize()   
    ) == 'mice',\
    'N("mouse").n(\'p\')=>mice'


def test_declension_en_92():
    assert (
N("navy").n('p').realize()   
    ) == 'navies',\
    'N("navy").n(\'p\')=>navies'


def test_declension_en_93():
    assert (
N("neighbourhood").n('p').realize()   
    ) == 'neighbourhoods',\
    'N("neighbourhood").n(\'p\')=>neighbourhoods'


def test_declension_en_94():
    assert (
N("number").n('p').realize()   
    ) == 'numbers',\
    'N("number").n(\'p\')=>numbers'


def test_declension_en_95():
    assert (
N("orchestra").n('p').realize()   
    ) == 'orchestras',\
    'N("orchestra").n(\'p\')=>orchestras'


def test_declension_en_96():
    assert (
N("pair").n('p').realize()   
    ) == 'pairs',\
    'N("pair").n(\'p\')=>pairs'


def test_declension_en_97():
    assert (
N("person").n('p').realize()   
    ) == 'people',\
    'N("person").n(\'p\')=>people'


def test_declension_en_98():
    assert (
N("personnel").n('p').realize()   
    ) == 'personnels',\
    'N("personnel").n(\'p\')=>personnels'


def test_declension_en_99():
    assert (
N("police").n('p').realize()   
    ) == 'police',\
    'N("police").n(\'p\')=>police'


def test_declension_en_100():
    assert (
N("policeman").n('p').realize()   
    ) == 'policemen',\
    'N("policeman").n(\'p\')=>policemen'


def test_declension_en_101():
    assert (
N("potato").n('p').realize()   
    ) == 'potatoes',\
    'N("potato").n(\'p\')=>potatoes'


def test_declension_en_102():
    assert (
N("quantum").n('p').realize()   
    ) == 'quanta',\
    'N("quantum").n(\'p\')=>quanta'


def test_declension_en_103():
    assert (
A("red").f('co').realize()   
    ) == 'redder',\
    'A("red").f(\'co\')=>redder'


def test_declension_en_104():
    assert (
A("red").f('su').realize()   
    ) == 'reddest',\
    'A("red").f(\'su\')=>reddest'


def test_declension_en_105():
    assert (
N("regiment").n('p').realize()   
    ) == 'regiments',\
    'N("regiment").n(\'p\')=>regiments'


def test_declension_en_106():
    assert (
N("roof").n('p').realize()   
    ) == 'roofs',\
    'N("roof").n(\'p\')=>roofs'


def test_declension_en_107():
    assert (
A("sad").f('co').realize()   
    ) == 'sadder',\
    'A("sad").f(\'co\')=>sadder'


def test_declension_en_108():
    assert (
A("sad").f('su').realize()   
    ) == 'saddest',\
    'A("sad").f(\'su\')=>saddest'


def test_declension_en_109():
    assert (
N("self").n('p').realize()   
    ) == 'selves',\
    'N("self").n(\'p\')=>selves'


def test_declension_en_110():
    assert (
N("senate").n('p').realize()   
    ) == 'senates',\
    'N("senate").n(\'p\')=>senates'


def test_declension_en_111():
    assert (
N("series").n('p').realize()   
    ) == 'series',\
    'N("series").n(\'p\')=>series'


def test_declension_en_112():
    assert (
N("sheep").n('p').realize()   
    ) == 'sheep',\
    'N("sheep").n(\'p\')=>sheep'


def test_declension_en_113():
    assert (
N("shelf").n('p').realize()   
    ) == 'shelves',\
    'N("shelf").n(\'p\')=>shelves'


def test_declension_en_114():
    assert (
A("shy").f('co').realize()   
    ) == 'shyer',\
    'A("shy").f(\'co\')=>shyer'


def test_declension_en_115():
    assert (
A("shy").f('su').realize()   
    ) == 'shyest',\
    'A("shy").f(\'su\')=>shyest'


def test_declension_en_116():
    assert (
A("slim").f('co').realize()   
    ) == 'slimmer',\
    'A("slim").f(\'co\')=>slimmer'


def test_declension_en_117():
    assert (
A("slim").f('su').realize()   
    ) == 'slimmest',\
    'A("slim").f(\'su\')=>slimmest'


def test_declension_en_118():
    assert (
N("solo").n('p').realize()   
    ) == 'solos',\
    'N("solo").n(\'p\')=>solos'


def test_declension_en_119():
    assert (
N("species").n('p').realize()   
    ) == 'species',\
    'N("species").n(\'p\')=>species'


def test_declension_en_120():
    assert (
N("spokesman").n('p').realize()   
    ) == 'spokesmen',\
    'N("spokesman").n(\'p\')=>spokesmen'


def test_declension_en_121():
    assert (
N("stimulus").n('p').realize()   
    ) == 'stimuli',\
    'N("stimulus").n(\'p\')=>stimuli'


def test_declension_en_122():
    assert (
N("stomach").n('p').realize()   
    ) == 'stomachs',\
    'N("stomach").n(\'p\')=>stomachs'


def test_declension_en_123():
    assert (
N("synthesis").n('p').realize()   
    ) == 'syntheses',\
    'N("synthesis").n(\'p\')=>syntheses'


def test_declension_en_124():
    assert (
N("team").n('p').realize()   
    ) == 'teams',\
    'N("team").n(\'p\')=>teams'


def test_declension_en_125():
    assert (
N("thesis").n('p').realize()   
    ) == 'theses',\
    'N("thesis").n(\'p\')=>theses'


def test_declension_en_126():
    assert (
N("thief").n('p').realize()   
    ) == 'thieves',\
    'N("thief").n(\'p\')=>thieves'


def test_declension_en_127():
    assert (
A("thin").f('co').realize()   
    ) == 'thinner',\
    'A("thin").f(\'co\')=>thinner'


def test_declension_en_128():
    assert (
A("thin").f('su').realize()   
    ) == 'thinnest',\
    'A("thin").f(\'su\')=>thinnest'


def test_declension_en_129():
    assert (
N("tomato").n('p').realize()   
    ) == 'tomatoes',\
    'N("tomato").n(\'p\')=>tomatoes'


def test_declension_en_130():
    assert (
N("tooth").n('p').realize()   
    ) == 'teeth',\
    'N("tooth").n(\'p\')=>teeth'


def test_declension_en_131():
    assert (
A("well").f('co').realize()   
    ) == 'better',\
    'A("well").f(\'co\')=>better'


def test_declension_en_132():
    assert (
A("well").f('su').realize()   
    ) == 'best',\
    'A("well").f(\'su\')=>best'


def test_declension_en_133():
    assert (
A("wet").f('co').realize()   
    ) == 'wetter',\
    'A("wet").f(\'co\')=>wetter'


def test_declension_en_134():
    assert (
A("wet").f('su').realize()   
    ) == 'wettest',\
    'A("wet").f(\'su\')=>wettest'


def test_declension_en_135():
    assert (
N("wife").n('p').realize()   
    ) == 'wives',\
    'N("wife").n(\'p\')=>wives'


def test_declension_en_136():
    assert (
N("wolf").n('p').realize()   
    ) == 'wolves',\
    'N("wolf").n(\'p\')=>wolves'


def test_declension_en_137():
    assert (
N("woman").n('p').realize()   
    ) == 'women',\
    'N("woman").n(\'p\')=>women'


def test_declension_en_138():
    assert (
A("wrong").f('co').realize()   
    ) == 'wronger',\
    'A("wrong").f(\'co\')=>wronger'


def test_declension_en_139():
    assert (
A("wrong").f('su').realize()   
    ) == 'wrongest',\
    'A("wrong").f(\'su\')=>wrongest'


def test_declension_en_140():
    assert (
N("zero").n('p').realize()   
    ) == 'zeros',\
    'N("zero").n(\'p\')=>zeros'


def test_declension_en_141():
    assert (
N("zoo").n('p').realize()   
    ) == 'zoos',\
    'N("zoo").n(\'p\')=>zoos'


def test_declension_en_142():
    assert (
Pro("I").n('s').g('m').pe(1).ow('s').realize()   
    ) == 'I',\
    'Pro("I").n(\'s\').g(\'m\').pe(1).ow(\'s\')=>I'


def test_declension_en_143():
    assert (
Pro("me").n('s').g('m').pe(1).ow('s').realize()   
    ) == 'me',\
    'Pro("me").n(\'s\').g(\'m\').pe(1).ow(\'s\')=>me'


def test_declension_en_144():
    assert (
Pro("mine").n('s').g('m').pe(1).ow('s').realize()   
    ) == 'mine',\
    'Pro("mine").n(\'s\').g(\'m\').pe(1).ow(\'s\')=>mine'


def test_declension_en_145():
    assert (
Pro("myself").n('s').g('m').pe(1).ow('s').realize()   
    ) == 'myself',\
    'Pro("myself").n(\'s\').g(\'m\').pe(1).ow(\'s\')=>myself'


def test_declension_en_146():
    assert (
Pro("I").n('s').g('m').pe(2).ow('s').realize()   
    ) == 'you',\
    'Pro("I").n(\'s\').g(\'m\').pe(2).ow(\'s\')=>you'


def test_declension_en_147():
    assert (
Pro("me").n('s').g('m').pe(2).ow('s').realize()   
    ) == 'you',\
    'Pro("me").n(\'s\').g(\'m\').pe(2).ow(\'s\')=>you'


def test_declension_en_148():
    assert (
Pro("mine").n('s').g('m').pe(2).ow('s').realize()   
    ) == 'yours',\
    'Pro("mine").n(\'s\').g(\'m\').pe(2).ow(\'s\')=>yours'


def test_declension_en_149():
    assert (
Pro("myself").n('s').g('m').pe(2).ow('s').realize()   
    ) == 'yourself',\
    'Pro("myself").n(\'s\').g(\'m\').pe(2).ow(\'s\')=>yourself'


def test_declension_en_150():
    assert (
Pro("I").n('s').g('m').pe(3).ow('s').realize()   
    ) == 'he',\
    'Pro("I").n(\'s\').g(\'m\').pe(3).ow(\'s\')=>he'


def test_declension_en_151():
    assert (
Pro("me").n('s').g('m').pe(3).ow('s').realize()   
    ) == 'him',\
    'Pro("me").n(\'s\').g(\'m\').pe(3).ow(\'s\')=>him'


def test_declension_en_152():
    assert (
Pro("mine").n('s').g('m').pe(3).ow('s').realize()   
    ) == 'his',\
    'Pro("mine").n(\'s\').g(\'m\').pe(3).ow(\'s\')=>his'


def test_declension_en_153():
    assert (
Pro("myself").n('s').g('m').pe(3).ow('s').realize()   
    ) == 'himself',\
    'Pro("myself").n(\'s\').g(\'m\').pe(3).ow(\'s\')=>himself'


def test_declension_en_154():
    assert (
Pro("I").n('s').g('f').pe(3).ow('s').realize()   
    ) == 'she',\
    'Pro("I").n(\'s\').g(\'f\').pe(3).ow(\'s\')=>she'


def test_declension_en_155():
    assert (
Pro("me").n('s').g('f').pe(3).ow('s').realize()   
    ) == 'her',\
    'Pro("me").n(\'s\').g(\'f\').pe(3).ow(\'s\')=>her'


def test_declension_en_156():
    assert (
Pro("mine").n('s').g('f').pe(3).ow('s').realize()   
    ) == 'hers',\
    'Pro("mine").n(\'s\').g(\'f\').pe(3).ow(\'s\')=>hers'


def test_declension_en_157():
    assert (
Pro("myself").n('s').g('f').pe(3).ow('s').realize()   
    ) == 'herself',\
    'Pro("myself").n(\'s\').g(\'f\').pe(3).ow(\'s\')=>herself'


def test_declension_en_158():
    assert (
Pro("I").n('s').g('n').pe(3).ow('s').realize()   
    ) == 'it',\
    'Pro("I").n(\'s\').g(\'n\').pe(3).ow(\'s\')=>it'


def test_declension_en_159():
    assert (
Pro("me").n('s').g('n').pe(3).ow('s').realize()   
    ) == 'it',\
    'Pro("me").n(\'s\').g(\'n\').pe(3).ow(\'s\')=>it'


def test_declension_en_160():
    assert (
Pro("mine").n('s').g('n').pe(3).ow('s').realize()   
    ) == 'its',\
    'Pro("mine").n(\'s\').g(\'n\').pe(3).ow(\'s\')=>its'


def test_declension_en_161():
    assert (
Pro("myself").n('s').g('n').pe(3).ow('s').realize()   
    ) == 'itself',\
    'Pro("myself").n(\'s\').g(\'n\').pe(3).ow(\'s\')=>itself'


def test_declension_en_162():
    assert (
Pro("I").n('p').g('m').pe(1).ow('p').realize()   
    ) == 'we',\
    'Pro("I").n(\'p\').g(\'m\').pe(1).ow(\'p\')=>we'


def test_declension_en_163():
    assert (
Pro("me").n('p').g('m').pe(1).ow('p').realize()   
    ) == 'us',\
    'Pro("me").n(\'p\').g(\'m\').pe(1).ow(\'p\')=>us'


def test_declension_en_164():
    assert (
Pro("mine").n('p').g('m').pe(1).ow('p').realize()   
    ) == 'ours',\
    'Pro("mine").n(\'p\').g(\'m\').pe(1).ow(\'p\')=>ours'


def test_declension_en_165():
    assert (
Pro("myself").n('p').g('m').pe(1).ow('p').realize()   
    ) == 'ourselves',\
    'Pro("myself").n(\'p\').g(\'m\').pe(1).ow(\'p\')=>ourselves'


def test_declension_en_166():
    assert (
Pro("I").n('p').g('m').pe(2).ow('p').realize()   
    ) == 'you',\
    'Pro("I").n(\'p\').g(\'m\').pe(2).ow(\'p\')=>you'


def test_declension_en_167():
    assert (
Pro("me").n('p').g('m').pe(2).ow('p').realize()   
    ) == 'you',\
    'Pro("me").n(\'p\').g(\'m\').pe(2).ow(\'p\')=>you'


def test_declension_en_168():
    assert (
Pro("mine").n('p').g('m').pe(2).ow('p').realize()   
    ) == 'yours',\
    'Pro("mine").n(\'p\').g(\'m\').pe(2).ow(\'p\')=>yours'


def test_declension_en_169():
    assert (
Pro("myself").n('p').g('m').pe(2).ow('p').realize()   
    ) == 'yourselves',\
    'Pro("myself").n(\'p\').g(\'m\').pe(2).ow(\'p\')=>yourselves'


def test_declension_en_170():
    assert (
Pro("I").n('p').g('m').pe(3).ow('p').realize()   
    ) == 'they',\
    'Pro("I").n(\'p\').g(\'m\').pe(3).ow(\'p\')=>they'


def test_declension_en_171():
    assert (
Pro("me").n('p').g('m').pe(3).ow('p').realize()   
    ) == 'them',\
    'Pro("me").n(\'p\').g(\'m\').pe(3).ow(\'p\')=>them'


def test_declension_en_172():
    assert (
Pro("mine").n('p').g('m').pe(3).ow('p').realize()   
    ) == 'theirs',\
    'Pro("mine").n(\'p\').g(\'m\').pe(3).ow(\'p\')=>theirs'


def test_declension_en_173():
    assert (
Pro("myself").n('p').g('m').pe(3).ow('p').realize()   
    ) == 'themselves',\
    'Pro("myself").n(\'p\').g(\'m\').pe(3).ow(\'p\')=>themselves'


def test_declension_en_174():
    assert (
Pro("why").n('p').g('m').pe(1).realize()   
    ) == 'why',\
    'Pro("why").n(\'p\').g(\'m\').pe(1)=>why'


def test_declension_en_175():
    assert (
Pro("who").n('p').g('m').pe(1).realize()   
    ) == 'who',\
    'Pro("who").n(\'p\').g(\'m\').pe(1)=>who'


def test_declension_en_176():
    assert (
Pro("where").n('p').g('m').pe(1).realize()   
    ) == 'where',\
    'Pro("where").n(\'p\').g(\'m\').pe(1)=>where'


def test_declension_en_177():
    assert (
Pro("this").n('p').g('m').pe(3).realize()   
    ) == 'these',\
    'Pro("this").n(\'p\').g(\'m\').pe(3)=>these'


def test_declension_en_178():
    assert (
Pro("that").n('p').g('m').pe(3).realize()   
    ) == 'those',\
    'Pro("that").n(\'p\').g(\'m\').pe(3)=>those'


def test_declension_en_179():
    assert (
D("a").n('p').g('m').pe(1).ow('p').realize()   
    ) == '',\
    'D("a").n(\'p\').g(\'m\').pe(1).ow(\'p\')=>'


def test_declension_en_180():
    assert (
D("my").n('p').g('m').pe(1).ow('p').realize()   
    ) == 'our',\
    'D("my").n(\'p\').g(\'m\').pe(1).ow(\'p\')=>our'


def test_declension_en_181():
    assert (
D("that").n('p').g('m').pe(1).ow('p').realize()   
    ) == 'those',\
    'D("that").n(\'p\').g(\'m\').pe(1).ow(\'p\')=>those'


def test_declension_en_182():
    assert (
D("what").n('p').g('m').pe(1).ow('p').realize()   
    ) == 'what',\
    'D("what").n(\'p\').g(\'m\').pe(1).ow(\'p\')=>what'


def test_declension_en_183():
    assert (
D("which").n('p').g('m').pe(1).ow('p').realize()   
    ) == 'which',\
    'D("which").n(\'p\').g(\'m\').pe(1).ow(\'p\')=>which'


def test_declension_en_184():
    assert (
D("whose").n('p').g('m').pe(1).ow('p').realize()   
    ) == 'whose',\
    'D("whose").n(\'p\').g(\'m\').pe(1).ow(\'p\')=>whose'

