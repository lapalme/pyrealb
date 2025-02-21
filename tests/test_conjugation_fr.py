import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..','src')))

from pyrealb import *
load("fr")

def test_conjugation_fr_0():
    assert (
V("être").t('p').pe(1).n('s').realize()   
    ) == 'suis',\
    'être:p1'


def test_conjugation_fr_1():
    assert (
V("être").t('p').pe(2).n('s').realize()   
    ) == 'es',\
    'être:p2'


def test_conjugation_fr_2():
    assert (
V("être").t('p').pe(3).n('s').realize()   
    ) == 'est',\
    'être:p3'


def test_conjugation_fr_3():
    assert (
V("être").t('p').pe(1).n('p').realize()   
    ) == 'sommes',\
    'être:p4'


def test_conjugation_fr_4():
    assert (
V("être").t('p').pe(2).n('p').realize()   
    ) == 'êtes',\
    'être:p5'


def test_conjugation_fr_5():
    assert (
V("être").t('p').pe(3).n('p').realize()   
    ) == 'sont',\
    'être:p6'


def test_conjugation_fr_6():
    assert (
V("être").t('ip').pe(2).n('s').realize()   
    ) == 'sois',\
    'être:ip2'


def test_conjugation_fr_7():
    assert (
V("être").t('ip').pe(1).n('p').realize()   
    ) == 'soyons',\
    'être:ip4'


def test_conjugation_fr_8():
    assert (
V("être").t('ip').pe(2).n('p').realize()   
    ) == 'soyez',\
    'être:ip5'


def test_conjugation_fr_9():
    assert (
V("être").t('pp').realize()   
    ) == 'été',\
    'être:pp'


def test_conjugation_fr_10():
    assert (
V("être").t('pr').realize()   
    ) == 'étant',\
    'être:pr'


def test_conjugation_fr_11():
    assert (
V("être").t('s').pe(1).n('s').realize()   
    ) == 'sois',\
    'être:s1'


def test_conjugation_fr_12():
    assert (
V("être").t('s').pe(2).n('s').realize()   
    ) == 'sois',\
    'être:s2'


def test_conjugation_fr_13():
    assert (
V("être").t('s').pe(3).n('s').realize()   
    ) == 'soit',\
    'être:s3'


def test_conjugation_fr_14():
    assert (
V("être").t('s').pe(1).n('p').realize()   
    ) == 'soyons',\
    'être:s4'


def test_conjugation_fr_15():
    assert (
V("être").t('s').pe(2).n('p').realize()   
    ) == 'soyez',\
    'être:s5'


def test_conjugation_fr_16():
    assert (
V("être").t('s').pe(3).n('p').realize()   
    ) == 'soient',\
    'être:s6'


def test_conjugation_fr_17():
    assert (
V("être").t('ps').pe(1).n('s').realize()   
    ) == 'fus',\
    'être:ps1'


def test_conjugation_fr_18():
    assert (
V("être").t('ps').pe(2).n('s').realize()   
    ) == 'fus',\
    'être:ps2'


def test_conjugation_fr_19():
    assert (
V("être").t('ps').pe(3).n('s').realize()   
    ) == 'fut',\
    'être:ps3'


def test_conjugation_fr_20():
    assert (
V("être").t('ps').pe(1).n('p').realize()   
    ) == 'fûmes',\
    'être:ps4'


def test_conjugation_fr_21():
    assert (
V("être").t('ps').pe(2).n('p').realize()   
    ) == 'fûtes',\
    'être:ps5'


def test_conjugation_fr_22():
    assert (
V("être").t('ps').pe(3).n('p').realize()   
    ) == 'furent',\
    'être:ps6'


def test_conjugation_fr_23():
    assert (
V("avoir").t('p').pe(1).n('s').realize()   
    ) == 'ai',\
    'avoir:p1'


def test_conjugation_fr_24():
    assert (
V("avoir").t('p').pe(2).n('s').realize()   
    ) == 'as',\
    'avoir:p2'


def test_conjugation_fr_25():
    assert (
V("avoir").t('p').pe(3).n('s').realize()   
    ) == 'a',\
    'avoir:p3'


def test_conjugation_fr_26():
    assert (
V("avoir").t('p').pe(1).n('p').realize()   
    ) == 'avons',\
    'avoir:p4'


def test_conjugation_fr_27():
    assert (
V("avoir").t('p').pe(2).n('p').realize()   
    ) == 'avez',\
    'avoir:p5'


def test_conjugation_fr_28():
    assert (
V("avoir").t('p').pe(3).n('p').realize()   
    ) == 'ont',\
    'avoir:p6'


def test_conjugation_fr_29():
    assert (
V("avoir").t('ip').pe(2).n('s').realize()   
    ) == 'aie',\
    'avoir:ip2'


def test_conjugation_fr_30():
    assert (
V("avoir").t('ip').pe(1).n('p').realize()   
    ) == 'ayons',\
    'avoir:ip4'


def test_conjugation_fr_31():
    assert (
V("avoir").t('ip').pe(2).n('p').realize()   
    ) == 'ayez',\
    'avoir:ip5'


def test_conjugation_fr_32():
    assert (
V("avoir").t('pp').realize()   
    ) == 'eu',\
    'avoir:pp'


def test_conjugation_fr_33():
    assert (
V("avoir").t('pr').realize()   
    ) == 'ayant',\
    'avoir:pr'


def test_conjugation_fr_34():
    assert (
V("avoir").t('s').pe(1).n('s').realize()   
    ) == 'aie',\
    'avoir:s1'


def test_conjugation_fr_35():
    assert (
V("avoir").t('s').pe(2).n('s').realize()   
    ) == 'aies',\
    'avoir:s2'


def test_conjugation_fr_36():
    assert (
V("avoir").t('s').pe(3).n('s').realize()   
    ) == 'ait',\
    'avoir:s3'


def test_conjugation_fr_37():
    assert (
V("avoir").t('s').pe(1).n('p').realize()   
    ) == 'ayons',\
    'avoir:s4'


def test_conjugation_fr_38():
    assert (
V("avoir").t('s').pe(2).n('p').realize()   
    ) == 'ayez',\
    'avoir:s5'


def test_conjugation_fr_39():
    assert (
V("avoir").t('s').pe(3).n('p').realize()   
    ) == 'aient',\
    'avoir:s6'


def test_conjugation_fr_40():
    assert (
V("abattre").t('p').pe(3).n('s').realize()   
    ) == 'abat',\
    'abattre:p3'


def test_conjugation_fr_41():
    assert (
V("abattre").t('p').pe(1).n('s').realize()   
    ) == 'abats',\
    'abattre:p1'


def test_conjugation_fr_42():
    assert (
V("abattre").t('p').pe(2).n('s').realize()   
    ) == 'abats',\
    'abattre:p2'


def test_conjugation_fr_43():
    assert (
V("abattre").t('ip').pe(2).n('s').realize()   
    ) == 'abats',\
    'abattre:ip2'


def test_conjugation_fr_44():
    assert (
V("abattre").t('pr').realize()   
    ) == 'abattant',\
    'abattre:pr'


def test_conjugation_fr_45():
    assert (
V("abattre").t('p').pe(3).n('p').realize()   
    ) == 'abattent',\
    'abattre:p6'


def test_conjugation_fr_46():
    assert (
V("abattre").t('p').pe(2).n('p').realize()   
    ) == 'abattez',\
    'abattre:p5'


def test_conjugation_fr_47():
    assert (
V("abattre").t('ip').pe(2).n('p').realize()   
    ) == 'abattez',\
    'abattre:ip5'


def test_conjugation_fr_48():
    assert (
V("abattre").t('p').pe(1).n('p').realize()   
    ) == 'abattons',\
    'abattre:p4'


def test_conjugation_fr_49():
    assert (
V("abattre").t('ip').pe(1).n('p').realize()   
    ) == 'abattons',\
    'abattre:ip4'


def test_conjugation_fr_50():
    assert (
V("abattre").t('pp').realize()   
    ) == 'abattu',\
    'abattre:pp'


def test_conjugation_fr_51():
    assert (
V("abattre").t('s').pe(1).n('s').realize()   
    ) == 'abatte',\
    'abattre:s1'


def test_conjugation_fr_52():
    assert (
V("abattre").t('s').pe(2).n('s').realize()   
    ) == 'abattes',\
    'abattre:s2'


def test_conjugation_fr_53():
    assert (
V("abattre").t('s').pe(3).n('s').realize()   
    ) == 'abatte',\
    'abattre:s3'


def test_conjugation_fr_54():
    assert (
V("abattre").t('s').pe(1).n('p').realize()   
    ) == 'abattions',\
    'abattre:s4'


def test_conjugation_fr_55():
    assert (
V("abattre").t('s').pe(2).n('p').realize()   
    ) == 'abattiez',\
    'abattre:s5'


def test_conjugation_fr_56():
    assert (
V("abattre").t('s').pe(3).n('p').realize()   
    ) == 'abattent',\
    'abattre:s6'


def test_conjugation_fr_57():
    assert (
V("accourir").t('pr').realize()   
    ) == 'accourant',\
    'accourir:pr'


def test_conjugation_fr_58():
    assert (
V("accourir").t('p').pe(3).n('p').realize()   
    ) == 'accourent',\
    'accourir:p6'


def test_conjugation_fr_59():
    assert (
V("accourir").t('p').pe(2).n('p').realize()   
    ) == 'accourez',\
    'accourir:p5'


def test_conjugation_fr_60():
    assert (
V("accourir").t('ip').pe(2).n('p').realize()   
    ) == 'accourez',\
    'accourir:ip5'


def test_conjugation_fr_61():
    assert (
V("accourir").t('p').pe(1).n('p').realize()   
    ) == 'accourons',\
    'accourir:p4'


def test_conjugation_fr_62():
    assert (
V("accourir").t('ip').pe(1).n('p').realize()   
    ) == 'accourons',\
    'accourir:ip4'


def test_conjugation_fr_63():
    assert (
V("accourir").t('p').pe(1).n('s').realize()   
    ) == 'accours',\
    'accourir:p1'


def test_conjugation_fr_64():
    assert (
V("accourir").t('p').pe(2).n('s').realize()   
    ) == 'accours',\
    'accourir:p2'


def test_conjugation_fr_65():
    assert (
V("accourir").t('ip').pe(2).n('s').realize()   
    ) == 'accours',\
    'accourir:ip2'


def test_conjugation_fr_66():
    assert (
V("accourir").t('p').pe(3).n('s').realize()   
    ) == 'accourt',\
    'accourir:p3'


def test_conjugation_fr_67():
    assert (
V("accourir").t('pp').realize()   
    ) == 'accouru',\
    'accourir:pp'


def test_conjugation_fr_68():
    assert (
V("accourir").t('s').pe(1).n('s').realize()   
    ) == 'accoure',\
    'accourir:s1'


def test_conjugation_fr_69():
    assert (
V("accourir").t('s').pe(2).n('s').realize()   
    ) == 'accoures',\
    'accourir:s2'


def test_conjugation_fr_70():
    assert (
V("accourir").t('s').pe(3).n('s').realize()   
    ) == 'accoure',\
    'accourir:s3'


def test_conjugation_fr_71():
    assert (
V("accourir").t('s').pe(1).n('p').realize()   
    ) == 'accourions',\
    'accourir:s4'


def test_conjugation_fr_72():
    assert (
V("accourir").t('s').pe(2).n('p').realize()   
    ) == 'accouriez',\
    'accourir:s5'


def test_conjugation_fr_73():
    assert (
V("accourir").t('s').pe(3).n('p').realize()   
    ) == 'accourent',\
    'accourir:s6'


def test_conjugation_fr_74():
    assert (
V("accueillir").t('pr').realize()   
    ) == 'accueillant',\
    'accueillir:pr'


def test_conjugation_fr_75():
    assert (
V("accueillir").t('p').pe(1).n('s').realize()   
    ) == 'accueille',\
    'accueillir:p1'


def test_conjugation_fr_76():
    assert (
V("accueillir").t('p').pe(3).n('s').realize()   
    ) == 'accueille',\
    'accueillir:p3'


def test_conjugation_fr_77():
    assert (
V("accueillir").t('ip').pe(2).n('s').realize()   
    ) == 'accueille',\
    'accueillir:ip2'


def test_conjugation_fr_78():
    assert (
V("accueillir").t('p').pe(3).n('p').realize()   
    ) == 'accueillent',\
    'accueillir:p6'


def test_conjugation_fr_79():
    assert (
V("accueillir").t('p').pe(2).n('s').realize()   
    ) == 'accueilles',\
    'accueillir:p2'


def test_conjugation_fr_80():
    assert (
V("accueillir").t('p').pe(2).n('p').realize()   
    ) == 'accueillez',\
    'accueillir:p5'


def test_conjugation_fr_81():
    assert (
V("accueillir").t('ip').pe(2).n('p').realize()   
    ) == 'accueillez',\
    'accueillir:ip5'


def test_conjugation_fr_82():
    assert (
V("accueillir").t('p').pe(1).n('p').realize()   
    ) == 'accueillons',\
    'accueillir:p4'


def test_conjugation_fr_83():
    assert (
V("accueillir").t('ip').pe(1).n('p').realize()   
    ) == 'accueillons',\
    'accueillir:ip4'


def test_conjugation_fr_84():
    assert (
V("accueillir").t('pp').realize()   
    ) == 'accueilli',\
    'accueillir:pp'


def test_conjugation_fr_85():
    assert (
V("accueillir").t('s').pe(1).n('s').realize()   
    ) == 'accueille',\
    'accueillir:s1'


def test_conjugation_fr_86():
    assert (
V("accueillir").t('s').pe(2).n('s').realize()   
    ) == 'accueilles',\
    'accueillir:s2'


def test_conjugation_fr_87():
    assert (
V("accueillir").t('s').pe(3).n('s').realize()   
    ) == 'accueille',\
    'accueillir:s3'


def test_conjugation_fr_88():
    assert (
V("accueillir").t('s').pe(1).n('p').realize()   
    ) == 'accueillions',\
    'accueillir:s4'


def test_conjugation_fr_89():
    assert (
V("accueillir").t('s').pe(2).n('p').realize()   
    ) == 'accueilliez',\
    'accueillir:s5'


def test_conjugation_fr_90():
    assert (
V("accueillir").t('s').pe(3).n('p').realize()   
    ) == 'accueillent',\
    'accueillir:s6'


def test_conjugation_fr_91():
    assert (
V("acquérir").t('p').pe(1).n('s').realize()   
    ) == 'acquiers',\
    'acquérir:p1'


def test_conjugation_fr_92():
    assert (
V("acquérir").t('p').pe(2).n('s').realize()   
    ) == 'acquiers',\
    'acquérir:p2'


def test_conjugation_fr_93():
    assert (
V("acquérir").t('ip').pe(2).n('s').realize()   
    ) == 'acquiers',\
    'acquérir:ip2'


def test_conjugation_fr_94():
    assert (
V("acquérir").t('p').pe(3).n('s').realize()   
    ) == 'acquiert',\
    'acquérir:p3'


def test_conjugation_fr_95():
    assert (
V("acquérir").t('p').pe(3).n('p').realize()   
    ) == 'acquièrent',\
    'acquérir:p6'


def test_conjugation_fr_96():
    assert (
V("acquérir").t('pr').realize()   
    ) == 'acquérant',\
    'acquérir:pr'


def test_conjugation_fr_97():
    assert (
V("acquérir").t('p').pe(2).n('p').realize()   
    ) == 'acquérez',\
    'acquérir:p5'


def test_conjugation_fr_98():
    assert (
V("acquérir").t('ip').pe(2).n('p').realize()   
    ) == 'acquérez',\
    'acquérir:ip5'


def test_conjugation_fr_99():
    assert (
V("acquérir").t('p').pe(1).n('p').realize()   
    ) == 'acquérons',\
    'acquérir:p4'


def test_conjugation_fr_100():
    assert (
V("acquérir").t('ip').pe(1).n('p').realize()   
    ) == 'acquérons',\
    'acquérir:ip4'


def test_conjugation_fr_101():
    assert (
V("acquérir").t('pp').realize()   
    ) == 'acquis',\
    'acquérir:pp'


def test_conjugation_fr_102():
    assert (
V("acquérir").t('s').pe(1).n('s').realize()   
    ) == 'acquière',\
    'acquérir:s1'


def test_conjugation_fr_103():
    assert (
V("acquérir").t('s').pe(2).n('s').realize()   
    ) == 'acquières',\
    'acquérir:s2'


def test_conjugation_fr_104():
    assert (
V("acquérir").t('s').pe(3).n('s').realize()   
    ) == 'acquière',\
    'acquérir:s3'


def test_conjugation_fr_105():
    assert (
V("acquérir").t('s').pe(1).n('p').realize()   
    ) == 'acquérions',\
    'acquérir:s4'


def test_conjugation_fr_106():
    assert (
V("acquérir").t('s').pe(2).n('p').realize()   
    ) == 'acquériez',\
    'acquérir:s5'


def test_conjugation_fr_107():
    assert (
V("acquérir").t('s').pe(3).n('p').realize()   
    ) == 'acquièrent',\
    'acquérir:s6'


def test_conjugation_fr_108():
    assert (
V("admettre").t('p').pe(3).n('s').realize()   
    ) == 'admet',\
    'admettre:p3'


def test_conjugation_fr_109():
    assert (
V("admettre").t('p').pe(1).n('s').realize()   
    ) == 'admets',\
    'admettre:p1'


def test_conjugation_fr_110():
    assert (
V("admettre").t('p').pe(2).n('s').realize()   
    ) == 'admets',\
    'admettre:p2'


def test_conjugation_fr_111():
    assert (
V("admettre").t('ip').pe(2).n('s').realize()   
    ) == 'admets',\
    'admettre:ip2'


def test_conjugation_fr_112():
    assert (
V("admettre").t('pr').realize()   
    ) == 'admettant',\
    'admettre:pr'


def test_conjugation_fr_113():
    assert (
V("admettre").t('p').pe(3).n('p').realize()   
    ) == 'admettent',\
    'admettre:p6'


def test_conjugation_fr_114():
    assert (
V("admettre").t('p').pe(2).n('p').realize()   
    ) == 'admettez',\
    'admettre:p5'


def test_conjugation_fr_115():
    assert (
V("admettre").t('ip').pe(2).n('p').realize()   
    ) == 'admettez',\
    'admettre:ip5'


def test_conjugation_fr_116():
    assert (
V("admettre").t('p').pe(1).n('p').realize()   
    ) == 'admettons',\
    'admettre:p4'


def test_conjugation_fr_117():
    assert (
V("admettre").t('ip').pe(1).n('p').realize()   
    ) == 'admettons',\
    'admettre:ip4'


def test_conjugation_fr_118():
    assert (
V("admettre").t('pp').realize()   
    ) == 'admis',\
    'admettre:pp'


def test_conjugation_fr_119():
    assert (
V("admettre").t('s').pe(1).n('s').realize()   
    ) == 'admette',\
    'admettre:s1'


def test_conjugation_fr_120():
    assert (
V("admettre").t('s').pe(2).n('s').realize()   
    ) == 'admettes',\
    'admettre:s2'


def test_conjugation_fr_121():
    assert (
V("admettre").t('s').pe(3).n('s').realize()   
    ) == 'admette',\
    'admettre:s3'


def test_conjugation_fr_122():
    assert (
V("admettre").t('s').pe(1).n('p').realize()   
    ) == 'admettions',\
    'admettre:s4'


def test_conjugation_fr_123():
    assert (
V("admettre").t('s').pe(2).n('p').realize()   
    ) == 'admettiez',\
    'admettre:s5'


def test_conjugation_fr_124():
    assert (
V("admettre").t('s').pe(3).n('p').realize()   
    ) == 'admettent',\
    'admettre:s6'


def test_conjugation_fr_125():
    assert (
V("aller").t('pr').realize()   
    ) == 'allant',\
    'aller:pr'


def test_conjugation_fr_126():
    assert (
V("aller").t('p').pe(2).n('p').realize()   
    ) == 'allez',\
    'aller:p5'


def test_conjugation_fr_127():
    assert (
V("aller").t('ip').pe(2).n('p').realize()   
    ) == 'allez',\
    'aller:ip5'


def test_conjugation_fr_128():
    assert (
V("aller").t('p').pe(1).n('p').realize()   
    ) == 'allons',\
    'aller:p4'


def test_conjugation_fr_129():
    assert (
V("aller").t('ip').pe(1).n('p').realize()   
    ) == 'allons',\
    'aller:ip4'


def test_conjugation_fr_130():
    assert (
V("aller").t('p').pe(3).n('s').realize()   
    ) == 'va',\
    'aller:p3'


def test_conjugation_fr_131():
    assert (
V("aller").t('p').pe(1).n('s').realize()   
    ) == 'vais',\
    'aller:p1'


def test_conjugation_fr_132():
    assert (
V("aller").t('p').pe(2).n('s').realize()   
    ) == 'vas',\
    'aller:p2'


def test_conjugation_fr_133():
    assert (
V("aller").t('p').pe(3).n('p').realize()   
    ) == 'vont',\
    'aller:p6'


def test_conjugation_fr_134():
    assert (
V("aller").t('pp').realize()   
    ) == 'allé',\
    'aller:pp'


def test_conjugation_fr_135():
    assert (
V("aller").t('s').pe(1).n('s').realize()   
    ) == 'aille',\
    'aller:s1'


def test_conjugation_fr_136():
    assert (
V("aller").t('s').pe(2).n('s').realize()   
    ) == 'ailles',\
    'aller:s2'


def test_conjugation_fr_137():
    assert (
V("aller").t('s').pe(3).n('s').realize()   
    ) == 'aille',\
    'aller:s3'


def test_conjugation_fr_138():
    assert (
V("aller").t('s').pe(1).n('p').realize()   
    ) == 'allions',\
    'aller:s4'


def test_conjugation_fr_139():
    assert (
V("aller").t('s').pe(2).n('p').realize()   
    ) == 'alliez',\
    'aller:s5'


def test_conjugation_fr_140():
    assert (
V("aller").t('s').pe(3).n('p').realize()   
    ) == 'aillent',\
    'aller:s6'


def test_conjugation_fr_141():
    assert (
V("aller").t('ip').pe(2).n('s').realize()   
    ) == 'va',\
    'aller:ip2'


def test_conjugation_fr_142():
    assert (
V("apercevoir").t('pr').realize()   
    ) == 'apercevant',\
    'apercevoir:pr'


def test_conjugation_fr_143():
    assert (
V("apercevoir").t('p').pe(2).n('p').realize()   
    ) == 'apercevez',\
    'apercevoir:p5'


def test_conjugation_fr_144():
    assert (
V("apercevoir").t('ip').pe(2).n('p').realize()   
    ) == 'apercevez',\
    'apercevoir:ip5'


def test_conjugation_fr_145():
    assert (
V("apercevoir").t('p').pe(1).n('p').realize()   
    ) == 'apercevons',\
    'apercevoir:p4'


def test_conjugation_fr_146():
    assert (
V("apercevoir").t('ip').pe(1).n('p').realize()   
    ) == 'apercevons',\
    'apercevoir:ip4'


def test_conjugation_fr_147():
    assert (
V("apercevoir").t('p').pe(1).n('s').realize()   
    ) == 'aperçois',\
    'apercevoir:p1'


def test_conjugation_fr_148():
    assert (
V("apercevoir").t('p').pe(2).n('s').realize()   
    ) == 'aperçois',\
    'apercevoir:p2'


def test_conjugation_fr_149():
    assert (
V("apercevoir").t('ip').pe(2).n('s').realize()   
    ) == 'aperçois',\
    'apercevoir:ip2'


def test_conjugation_fr_150():
    assert (
V("apercevoir").t('p').pe(3).n('s').realize()   
    ) == 'aperçoit',\
    'apercevoir:p3'


def test_conjugation_fr_151():
    assert (
V("apercevoir").t('p').pe(3).n('p').realize()   
    ) == 'aperçoivent',\
    'apercevoir:p6'


def test_conjugation_fr_152():
    assert (
V("apercevoir").t('pp').realize()   
    ) == 'aperçu',\
    'apercevoir:pp'


def test_conjugation_fr_153():
    assert (
V("apercevoir").t('s').pe(1).n('s').realize()   
    ) == 'aperçoive',\
    'apercevoir:s1'


def test_conjugation_fr_154():
    assert (
V("apercevoir").t('s').pe(2).n('s').realize()   
    ) == 'aperçoives',\
    'apercevoir:s2'


def test_conjugation_fr_155():
    assert (
V("apercevoir").t('s').pe(3).n('s').realize()   
    ) == 'aperçoive',\
    'apercevoir:s3'


def test_conjugation_fr_156():
    assert (
V("apercevoir").t('s').pe(1).n('p').realize()   
    ) == 'apercevions',\
    'apercevoir:s4'


def test_conjugation_fr_157():
    assert (
V("apercevoir").t('s').pe(2).n('p').realize()   
    ) == 'aperceviez',\
    'apercevoir:s5'


def test_conjugation_fr_158():
    assert (
V("apercevoir").t('s').pe(3).n('p').realize()   
    ) == 'aperçoivent',\
    'apercevoir:s6'


def test_conjugation_fr_159():
    assert (
V("apparaître").t('p').pe(1).n('s').realize()   
    ) == 'apparais',\
    'apparaître:p1'


def test_conjugation_fr_160():
    assert (
V("apparaître").t('p').pe(2).n('s').realize()   
    ) == 'apparais',\
    'apparaître:p2'


def test_conjugation_fr_161():
    assert (
V("apparaître").t('ip').pe(2).n('s').realize()   
    ) == 'apparais',\
    'apparaître:ip2'


def test_conjugation_fr_162():
    assert (
V("apparaître").t('pr').realize()   
    ) == 'apparaissant',\
    'apparaître:pr'


def test_conjugation_fr_163():
    assert (
V("apparaître").t('p').pe(3).n('p').realize()   
    ) == 'apparaissent',\
    'apparaître:p6'


def test_conjugation_fr_164():
    assert (
V("apparaître").t('p').pe(2).n('p').realize()   
    ) == 'apparaissez',\
    'apparaître:p5'


def test_conjugation_fr_165():
    assert (
V("apparaître").t('ip').pe(2).n('p').realize()   
    ) == 'apparaissez',\
    'apparaître:ip5'


def test_conjugation_fr_166():
    assert (
V("apparaître").t('p').pe(1).n('p').realize()   
    ) == 'apparaissons',\
    'apparaître:p4'


def test_conjugation_fr_167():
    assert (
V("apparaître").t('ip').pe(1).n('p').realize()   
    ) == 'apparaissons',\
    'apparaître:ip4'


def test_conjugation_fr_168():
    assert (
V("apparaître").t('p').pe(3).n('s').realize()   
    ) == 'apparaît',\
    'apparaître:p3'


def test_conjugation_fr_169():
    assert (
V("apparaître").t('pp').realize()   
    ) == 'apparu',\
    'apparaître:pp'


def test_conjugation_fr_170():
    assert (
V("apparaître").t('s').pe(1).n('s').realize()   
    ) == 'apparaisse',\
    'apparaître:s1'


def test_conjugation_fr_171():
    assert (
V("apparaître").t('s').pe(2).n('s').realize()   
    ) == 'apparaisses',\
    'apparaître:s2'


def test_conjugation_fr_172():
    assert (
V("apparaître").t('s').pe(3).n('s').realize()   
    ) == 'apparaisse',\
    'apparaître:s3'


def test_conjugation_fr_173():
    assert (
V("apparaître").t('s').pe(1).n('p').realize()   
    ) == 'apparaissions',\
    'apparaître:s4'


def test_conjugation_fr_174():
    assert (
V("apparaître").t('s').pe(2).n('p').realize()   
    ) == 'apparaissiez',\
    'apparaître:s5'


def test_conjugation_fr_175():
    assert (
V("apparaître").t('s').pe(3).n('p').realize()   
    ) == 'apparaissent',\
    'apparaître:s6'


def test_conjugation_fr_176():
    assert (
V("appartenir").t('pr').realize()   
    ) == 'appartenant',\
    'appartenir:pr'


def test_conjugation_fr_177():
    assert (
V("appartenir").t('p').pe(2).n('p').realize()   
    ) == 'appartenez',\
    'appartenir:p5'


def test_conjugation_fr_178():
    assert (
V("appartenir").t('ip').pe(2).n('p').realize()   
    ) == 'appartenez',\
    'appartenir:ip5'


def test_conjugation_fr_179():
    assert (
V("appartenir").t('p').pe(1).n('p').realize()   
    ) == 'appartenons',\
    'appartenir:p4'


def test_conjugation_fr_180():
    assert (
V("appartenir").t('ip').pe(1).n('p').realize()   
    ) == 'appartenons',\
    'appartenir:ip4'


def test_conjugation_fr_181():
    assert (
V("appartenir").t('p').pe(3).n('p').realize()   
    ) == 'appartiennent',\
    'appartenir:p6'


def test_conjugation_fr_182():
    assert (
V("appartenir").t('p').pe(1).n('s').realize()   
    ) == 'appartiens',\
    'appartenir:p1'


def test_conjugation_fr_183():
    assert (
V("appartenir").t('p').pe(2).n('s').realize()   
    ) == 'appartiens',\
    'appartenir:p2'


def test_conjugation_fr_184():
    assert (
V("appartenir").t('ip').pe(2).n('s').realize()   
    ) == 'appartiens',\
    'appartenir:ip2'


def test_conjugation_fr_185():
    assert (
V("appartenir").t('p').pe(3).n('s').realize()   
    ) == 'appartient',\
    'appartenir:p3'


def test_conjugation_fr_186():
    assert (
V("appartenir").t('pp').realize()   
    ) == 'appartenu',\
    'appartenir:pp'


def test_conjugation_fr_187():
    assert (
V("appartenir").t('s').pe(1).n('s').realize()   
    ) == 'appartienne',\
    'appartenir:s1'


def test_conjugation_fr_188():
    assert (
V("appartenir").t('s').pe(2).n('s').realize()   
    ) == 'appartiennes',\
    'appartenir:s2'


def test_conjugation_fr_189():
    assert (
V("appartenir").t('s').pe(3).n('s').realize()   
    ) == 'appartienne',\
    'appartenir:s3'


def test_conjugation_fr_190():
    assert (
V("appartenir").t('s').pe(1).n('p').realize()   
    ) == 'appartenions',\
    'appartenir:s4'


def test_conjugation_fr_191():
    assert (
V("appartenir").t('s').pe(2).n('p').realize()   
    ) == 'apparteniez',\
    'appartenir:s5'


def test_conjugation_fr_192():
    assert (
V("appartenir").t('s').pe(3).n('p').realize()   
    ) == 'appartiennent',\
    'appartenir:s6'


def test_conjugation_fr_193():
    assert (
V("appeler").t('p').pe(1).n('s').realize()   
    ) == 'appelle',\
    'appeler:p1'


def test_conjugation_fr_194():
    assert (
V("appeler").t('p').pe(2).n('s').realize()   
    ) == 'appelles',\
    'appeler:p2'


def test_conjugation_fr_195():
    assert (
V("appeler").t('p').pe(3).n('s').realize()   
    ) == 'appelle',\
    'appeler:p3'


def test_conjugation_fr_196():
    assert (
V("appeler").t('p').pe(3).n('p').realize()   
    ) == 'appellent',\
    'appeler:p6'


def test_conjugation_fr_197():
    assert (
V("appeler").t('s').pe(1).n('s').realize()   
    ) == 'appelle',\
    'appeler:s1'


def test_conjugation_fr_198():
    assert (
V("appeler").t('s').pe(2).n('s').realize()   
    ) == 'appelles',\
    'appeler:s2'


def test_conjugation_fr_199():
    assert (
V("appeler").t('s').pe(3).n('s').realize()   
    ) == 'appelle',\
    'appeler:s3'


def test_conjugation_fr_200():
    assert (
V("appeler").t('s').pe(1).n('p').realize()   
    ) == 'appelions',\
    'appeler:s4'


def test_conjugation_fr_201():
    assert (
V("appeler").t('s').pe(2).n('p').realize()   
    ) == 'appeliez',\
    'appeler:s5'


def test_conjugation_fr_202():
    assert (
V("appeler").t('s').pe(3).n('p').realize()   
    ) == 'appellent',\
    'appeler:s6'


def test_conjugation_fr_203():
    assert (
V("apprendre").t('pr').realize()   
    ) == 'apprenant',\
    'apprendre:pr'


def test_conjugation_fr_204():
    assert (
V("apprendre").t('p').pe(3).n('s').realize()   
    ) == 'apprend',\
    'apprendre:p3'


def test_conjugation_fr_205():
    assert (
V("apprendre").t('p').pe(1).n('s').realize()   
    ) == 'apprends',\
    'apprendre:p1'


def test_conjugation_fr_206():
    assert (
V("apprendre").t('p').pe(2).n('s').realize()   
    ) == 'apprends',\
    'apprendre:p2'


def test_conjugation_fr_207():
    assert (
V("apprendre").t('ip').pe(2).n('s').realize()   
    ) == 'apprends',\
    'apprendre:ip2'


def test_conjugation_fr_208():
    assert (
V("apprendre").t('p').pe(2).n('p').realize()   
    ) == 'apprenez',\
    'apprendre:p5'


def test_conjugation_fr_209():
    assert (
V("apprendre").t('ip').pe(2).n('p').realize()   
    ) == 'apprenez',\
    'apprendre:ip5'


def test_conjugation_fr_210():
    assert (
V("apprendre").t('p').pe(3).n('p').realize()   
    ) == 'apprennent',\
    'apprendre:p6'


def test_conjugation_fr_211():
    assert (
V("apprendre").t('p').pe(1).n('p').realize()   
    ) == 'apprenons',\
    'apprendre:p4'


def test_conjugation_fr_212():
    assert (
V("apprendre").t('ip').pe(1).n('p').realize()   
    ) == 'apprenons',\
    'apprendre:ip4'


def test_conjugation_fr_213():
    assert (
V("apprendre").t('pp').realize()   
    ) == 'appris',\
    'apprendre:pp'


def test_conjugation_fr_214():
    assert (
V("apprendre").t('s').pe(1).n('s').realize()   
    ) == 'apprenne',\
    'apprendre:s1'


def test_conjugation_fr_215():
    assert (
V("apprendre").t('s').pe(2).n('s').realize()   
    ) == 'apprennes',\
    'apprendre:s2'


def test_conjugation_fr_216():
    assert (
V("apprendre").t('s').pe(3).n('s').realize()   
    ) == 'apprenne',\
    'apprendre:s3'


def test_conjugation_fr_217():
    assert (
V("apprendre").t('s').pe(1).n('p').realize()   
    ) == 'apprenions',\
    'apprendre:s4'


def test_conjugation_fr_218():
    assert (
V("apprendre").t('s').pe(2).n('p').realize()   
    ) == 'appreniez',\
    'apprendre:s5'


def test_conjugation_fr_219():
    assert (
V("apprendre").t('s').pe(3).n('p').realize()   
    ) == 'apprennent',\
    'apprendre:s6'


def test_conjugation_fr_220():
    assert (
V("asseoir").t('pr').realize()   
    ) == 'assoyant',\
    'asseoir:pr'


def test_conjugation_fr_221():
    assert (
V("asseoir").t('p').pe(3).n('p').realize()   
    ) == 'assoient',\
    'asseoir:p6'


def test_conjugation_fr_222():
    assert (
V("asseoir").t('p').pe(2).n('p').realize()   
    ) == 'assoyez',\
    'asseoir:p5'


def test_conjugation_fr_223():
    assert (
V("asseoir").t('ip').pe(2).n('p').realize()   
    ) == 'assoyez',\
    'asseoir:ip5'


def test_conjugation_fr_224():
    assert (
V("asseoir").t('p').pe(1).n('p').realize()   
    ) == 'assoyons',\
    'asseoir:p4'


def test_conjugation_fr_225():
    assert (
V("asseoir").t('ip').pe(1).n('p').realize()   
    ) == 'assoyons',\
    'asseoir:ip4'


def test_conjugation_fr_226():
    assert (
V("asseoir").t('p').pe(3).n('s').realize()   
    ) == 'assoit',\
    'asseoir:p3'


def test_conjugation_fr_227():
    assert (
V("asseoir").t('p').pe(1).n('s').realize()   
    ) == 'assois',\
    'asseoir:p1'


def test_conjugation_fr_228():
    assert (
V("asseoir").t('p').pe(2).n('s').realize()   
    ) == 'assois',\
    'asseoir:p2'


def test_conjugation_fr_229():
    assert (
V("asseoir").t('ip').pe(2).n('s').realize()   
    ) == 'assois',\
    'asseoir:ip2'


def test_conjugation_fr_230():
    assert (
V("asseoir").t('pp').realize()   
    ) == 'assis',\
    'asseoir:pp'


def test_conjugation_fr_231():
    assert (
V("asseoir").t('s').pe(1).n('s').realize()   
    ) == 'assoie',\
    'asseoir:s1'


def test_conjugation_fr_232():
    assert (
V("asseoir").t('s').pe(2).n('s').realize()   
    ) == 'assoies',\
    'asseoir:s2'


def test_conjugation_fr_233():
    assert (
V("asseoir").t('s').pe(3).n('s').realize()   
    ) == 'assoie',\
    'asseoir:s3'


def test_conjugation_fr_234():
    assert (
V("asseoir").t('s').pe(1).n('p').realize()   
    ) == 'assoyions',\
    'asseoir:s4'


def test_conjugation_fr_235():
    assert (
V("asseoir").t('s').pe(2).n('p').realize()   
    ) == 'assoyiez',\
    'asseoir:s5'


def test_conjugation_fr_236():
    assert (
V("asseoir").t('s').pe(3).n('p').realize()   
    ) == 'assoient',\
    'asseoir:s6'


def test_conjugation_fr_237():
    assert (
V("atteindre").t('pr').realize()   
    ) == 'atteignant',\
    'atteindre:pr'


def test_conjugation_fr_238():
    assert (
V("atteindre").t('p').pe(3).n('p').realize()   
    ) == 'atteignent',\
    'atteindre:p6'


def test_conjugation_fr_239():
    assert (
V("atteindre").t('p').pe(2).n('p').realize()   
    ) == 'atteignez',\
    'atteindre:p5'


def test_conjugation_fr_240():
    assert (
V("atteindre").t('ip').pe(2).n('p').realize()   
    ) == 'atteignez',\
    'atteindre:ip5'


def test_conjugation_fr_241():
    assert (
V("atteindre").t('p').pe(1).n('p').realize()   
    ) == 'atteignons',\
    'atteindre:p4'


def test_conjugation_fr_242():
    assert (
V("atteindre").t('ip').pe(1).n('p').realize()   
    ) == 'atteignons',\
    'atteindre:ip4'


def test_conjugation_fr_243():
    assert (
V("atteindre").t('p').pe(1).n('s').realize()   
    ) == 'atteins',\
    'atteindre:p1'


def test_conjugation_fr_244():
    assert (
V("atteindre").t('p').pe(2).n('s').realize()   
    ) == 'atteins',\
    'atteindre:p2'


def test_conjugation_fr_245():
    assert (
V("atteindre").t('ip').pe(2).n('s').realize()   
    ) == 'atteins',\
    'atteindre:ip2'


def test_conjugation_fr_246():
    assert (
V("atteindre").t('p').pe(3).n('s').realize()   
    ) == 'atteint',\
    'atteindre:p3'


def test_conjugation_fr_247():
    assert (
V("atteindre").t('pp').realize()   
    ) == 'atteint',\
    'atteindre:pp'


def test_conjugation_fr_248():
    assert (
V("atteindre").t('s').pe(1).n('s').realize()   
    ) == 'atteigne',\
    'atteindre:s1'


def test_conjugation_fr_249():
    assert (
V("atteindre").t('s').pe(2).n('s').realize()   
    ) == 'atteignes',\
    'atteindre:s2'


def test_conjugation_fr_250():
    assert (
V("atteindre").t('s').pe(3).n('s').realize()   
    ) == 'atteigne',\
    'atteindre:s3'


def test_conjugation_fr_251():
    assert (
V("atteindre").t('s').pe(1).n('p').realize()   
    ) == 'atteignions',\
    'atteindre:s4'


def test_conjugation_fr_252():
    assert (
V("atteindre").t('s').pe(2).n('p').realize()   
    ) == 'atteigniez',\
    'atteindre:s5'


def test_conjugation_fr_253():
    assert (
V("atteindre").t('s').pe(3).n('p').realize()   
    ) == 'atteignent',\
    'atteindre:s6'


def test_conjugation_fr_254():
    assert (
V("attendre").t('p').pe(3).n('s').realize()   
    ) == 'attend',\
    'attendre:p3'


def test_conjugation_fr_255():
    assert (
V("attendre").t('pr').realize()   
    ) == 'attendant',\
    'attendre:pr'


def test_conjugation_fr_256():
    assert (
V("attendre").t('p').pe(3).n('p').realize()   
    ) == 'attendent',\
    'attendre:p6'


def test_conjugation_fr_257():
    assert (
V("attendre").t('p').pe(2).n('p').realize()   
    ) == 'attendez',\
    'attendre:p5'


def test_conjugation_fr_258():
    assert (
V("attendre").t('ip').pe(2).n('p').realize()   
    ) == 'attendez',\
    'attendre:ip5'


def test_conjugation_fr_259():
    assert (
V("attendre").t('p').pe(1).n('p').realize()   
    ) == 'attendons',\
    'attendre:p4'


def test_conjugation_fr_260():
    assert (
V("attendre").t('ip').pe(1).n('p').realize()   
    ) == 'attendons',\
    'attendre:ip4'


def test_conjugation_fr_261():
    assert (
V("attendre").t('p').pe(1).n('s').realize()   
    ) == 'attends',\
    'attendre:p1'


def test_conjugation_fr_262():
    assert (
V("attendre").t('p').pe(2).n('s').realize()   
    ) == 'attends',\
    'attendre:p2'


def test_conjugation_fr_263():
    assert (
V("attendre").t('ip').pe(2).n('s').realize()   
    ) == 'attends',\
    'attendre:ip2'


def test_conjugation_fr_264():
    assert (
V("attendre").t('pp').realize()   
    ) == 'attendu',\
    'attendre:pp'


def test_conjugation_fr_265():
    assert (
V("attendre").t('s').pe(1).n('s').realize()   
    ) == 'attende',\
    'attendre:s1'


def test_conjugation_fr_266():
    assert (
V("attendre").t('s').pe(2).n('s').realize()   
    ) == 'attendes',\
    'attendre:s2'


def test_conjugation_fr_267():
    assert (
V("attendre").t('s').pe(3).n('s').realize()   
    ) == 'attende',\
    'attendre:s3'


def test_conjugation_fr_268():
    assert (
V("attendre").t('s').pe(1).n('p').realize()   
    ) == 'attendions',\
    'attendre:s4'


def test_conjugation_fr_269():
    assert (
V("attendre").t('s').pe(2).n('p').realize()   
    ) == 'attendiez',\
    'attendre:s5'


def test_conjugation_fr_270():
    assert (
V("attendre").t('s').pe(3).n('p').realize()   
    ) == 'attendent',\
    'attendre:s6'


def test_conjugation_fr_271():
    assert (
V("battre").t('p').pe(3).n('s').realize()   
    ) == 'bat',\
    'battre:p3'


def test_conjugation_fr_272():
    assert (
V("battre").t('p').pe(1).n('s').realize()   
    ) == 'bats',\
    'battre:p1'


def test_conjugation_fr_273():
    assert (
V("battre").t('p').pe(2).n('s').realize()   
    ) == 'bats',\
    'battre:p2'


def test_conjugation_fr_274():
    assert (
V("battre").t('ip').pe(2).n('s').realize()   
    ) == 'bats',\
    'battre:ip2'


def test_conjugation_fr_275():
    assert (
V("battre").t('pr').realize()   
    ) == 'battant',\
    'battre:pr'


def test_conjugation_fr_276():
    assert (
V("battre").t('p').pe(3).n('p').realize()   
    ) == 'battent',\
    'battre:p6'


def test_conjugation_fr_277():
    assert (
V("battre").t('p').pe(2).n('p').realize()   
    ) == 'battez',\
    'battre:p5'


def test_conjugation_fr_278():
    assert (
V("battre").t('ip').pe(2).n('p').realize()   
    ) == 'battez',\
    'battre:ip5'


def test_conjugation_fr_279():
    assert (
V("battre").t('p').pe(1).n('p').realize()   
    ) == 'battons',\
    'battre:p4'


def test_conjugation_fr_280():
    assert (
V("battre").t('ip').pe(1).n('p').realize()   
    ) == 'battons',\
    'battre:ip4'


def test_conjugation_fr_281():
    assert (
V("battre").t('pp').realize()   
    ) == 'battu',\
    'battre:pp'


def test_conjugation_fr_282():
    assert (
V("battre").t('s').pe(1).n('s').realize()   
    ) == 'batte',\
    'battre:s1'


def test_conjugation_fr_283():
    assert (
V("battre").t('s').pe(2).n('s').realize()   
    ) == 'battes',\
    'battre:s2'


def test_conjugation_fr_284():
    assert (
V("battre").t('s').pe(3).n('s').realize()   
    ) == 'batte',\
    'battre:s3'


def test_conjugation_fr_285():
    assert (
V("battre").t('s').pe(1).n('p').realize()   
    ) == 'battions',\
    'battre:s4'


def test_conjugation_fr_286():
    assert (
V("battre").t('s').pe(2).n('p').realize()   
    ) == 'battiez',\
    'battre:s5'


def test_conjugation_fr_287():
    assert (
V("battre").t('s').pe(3).n('p').realize()   
    ) == 'battent',\
    'battre:s6'


def test_conjugation_fr_288():
    assert (
V("boire").t('p').pe(1).n('s').realize()   
    ) == 'bois',\
    'boire:p1'


def test_conjugation_fr_289():
    assert (
V("boire").t('p').pe(2).n('s').realize()   
    ) == 'bois',\
    'boire:p2'


def test_conjugation_fr_290():
    assert (
V("boire").t('ip').pe(2).n('s').realize()   
    ) == 'bois',\
    'boire:ip2'


def test_conjugation_fr_291():
    assert (
V("boire").t('p').pe(3).n('s').realize()   
    ) == 'boit',\
    'boire:p3'


def test_conjugation_fr_292():
    assert (
V("boire").t('p').pe(3).n('p').realize()   
    ) == 'boivent',\
    'boire:p6'


def test_conjugation_fr_293():
    assert (
V("boire").t('pr').realize()   
    ) == 'buvant',\
    'boire:pr'


def test_conjugation_fr_294():
    assert (
V("boire").t('p').pe(2).n('p').realize()   
    ) == 'buvez',\
    'boire:p5'


def test_conjugation_fr_295():
    assert (
V("boire").t('ip').pe(2).n('p').realize()   
    ) == 'buvez',\
    'boire:ip5'


def test_conjugation_fr_296():
    assert (
V("boire").t('p').pe(1).n('p').realize()   
    ) == 'buvons',\
    'boire:p4'


def test_conjugation_fr_297():
    assert (
V("boire").t('ip').pe(1).n('p').realize()   
    ) == 'buvons',\
    'boire:ip4'


def test_conjugation_fr_298():
    assert (
V("boire").t('pp').realize()   
    ) == 'bu',\
    'boire:pp'


def test_conjugation_fr_299():
    assert (
V("boire").t('s').pe(1).n('s').realize()   
    ) == 'boive',\
    'boire:s1'


def test_conjugation_fr_300():
    assert (
V("boire").t('s').pe(2).n('s').realize()   
    ) == 'boives',\
    'boire:s2'


def test_conjugation_fr_301():
    assert (
V("boire").t('s').pe(3).n('s').realize()   
    ) == 'boive',\
    'boire:s3'


def test_conjugation_fr_302():
    assert (
V("boire").t('s').pe(1).n('p').realize()   
    ) == 'buvions',\
    'boire:s4'


def test_conjugation_fr_303():
    assert (
V("boire").t('s').pe(2).n('p').realize()   
    ) == 'buviez',\
    'boire:s5'


def test_conjugation_fr_304():
    assert (
V("boire").t('s').pe(3).n('p').realize()   
    ) == 'boivent',\
    'boire:s6'


def test_conjugation_fr_305():
    assert (
V("combattre").t('p').pe(3).n('s').realize()   
    ) == 'combat',\
    'combattre:p3'


def test_conjugation_fr_306():
    assert (
V("combattre").t('p').pe(1).n('s').realize()   
    ) == 'combats',\
    'combattre:p1'


def test_conjugation_fr_307():
    assert (
V("combattre").t('p').pe(2).n('s').realize()   
    ) == 'combats',\
    'combattre:p2'


def test_conjugation_fr_308():
    assert (
V("combattre").t('ip').pe(2).n('s').realize()   
    ) == 'combats',\
    'combattre:ip2'


def test_conjugation_fr_309():
    assert (
V("combattre").t('pr').realize()   
    ) == 'combattant',\
    'combattre:pr'


def test_conjugation_fr_310():
    assert (
V("combattre").t('p').pe(3).n('p').realize()   
    ) == 'combattent',\
    'combattre:p6'


def test_conjugation_fr_311():
    assert (
V("combattre").t('p').pe(2).n('p').realize()   
    ) == 'combattez',\
    'combattre:p5'


def test_conjugation_fr_312():
    assert (
V("combattre").t('ip').pe(2).n('p').realize()   
    ) == 'combattez',\
    'combattre:ip5'


def test_conjugation_fr_313():
    assert (
V("combattre").t('p').pe(1).n('p').realize()   
    ) == 'combattons',\
    'combattre:p4'


def test_conjugation_fr_314():
    assert (
V("combattre").t('ip').pe(1).n('p').realize()   
    ) == 'combattons',\
    'combattre:ip4'


def test_conjugation_fr_315():
    assert (
V("combattre").t('pp').realize()   
    ) == 'combattu',\
    'combattre:pp'


def test_conjugation_fr_316():
    assert (
V("combattre").t('s').pe(1).n('s').realize()   
    ) == 'combatte',\
    'combattre:s1'


def test_conjugation_fr_317():
    assert (
V("combattre").t('s').pe(2).n('s').realize()   
    ) == 'combattes',\
    'combattre:s2'


def test_conjugation_fr_318():
    assert (
V("combattre").t('s').pe(3).n('s').realize()   
    ) == 'combatte',\
    'combattre:s3'


def test_conjugation_fr_319():
    assert (
V("combattre").t('s').pe(1).n('p').realize()   
    ) == 'combattions',\
    'combattre:s4'


def test_conjugation_fr_320():
    assert (
V("combattre").t('s').pe(2).n('p').realize()   
    ) == 'combattiez',\
    'combattre:s5'


def test_conjugation_fr_321():
    assert (
V("combattre").t('s').pe(3).n('p').realize()   
    ) == 'combattent',\
    'combattre:s6'


def test_conjugation_fr_322():
    assert (
V("commettre").t('p').pe(3).n('s').realize()   
    ) == 'commet',\
    'commettre:p3'


def test_conjugation_fr_323():
    assert (
V("commettre").t('p').pe(1).n('s').realize()   
    ) == 'commets',\
    'commettre:p1'


def test_conjugation_fr_324():
    assert (
V("commettre").t('p').pe(2).n('s').realize()   
    ) == 'commets',\
    'commettre:p2'


def test_conjugation_fr_325():
    assert (
V("commettre").t('ip').pe(2).n('s').realize()   
    ) == 'commets',\
    'commettre:ip2'


def test_conjugation_fr_326():
    assert (
V("commettre").t('pr').realize()   
    ) == 'commettant',\
    'commettre:pr'


def test_conjugation_fr_327():
    assert (
V("commettre").t('p').pe(3).n('p').realize()   
    ) == 'commettent',\
    'commettre:p6'


def test_conjugation_fr_328():
    assert (
V("commettre").t('p').pe(2).n('p').realize()   
    ) == 'commettez',\
    'commettre:p5'


def test_conjugation_fr_329():
    assert (
V("commettre").t('ip').pe(2).n('p').realize()   
    ) == 'commettez',\
    'commettre:ip5'


def test_conjugation_fr_330():
    assert (
V("commettre").t('p').pe(1).n('p').realize()   
    ) == 'commettons',\
    'commettre:p4'


def test_conjugation_fr_331():
    assert (
V("commettre").t('ip').pe(1).n('p').realize()   
    ) == 'commettons',\
    'commettre:ip4'


def test_conjugation_fr_332():
    assert (
V("commettre").t('pp').realize()   
    ) == 'commis',\
    'commettre:pp'


def test_conjugation_fr_333():
    assert (
V("commettre").t('s').pe(1).n('s').realize()   
    ) == 'commette',\
    'commettre:s1'


def test_conjugation_fr_334():
    assert (
V("commettre").t('s').pe(2).n('s').realize()   
    ) == 'commettes',\
    'commettre:s2'


def test_conjugation_fr_335():
    assert (
V("commettre").t('s').pe(3).n('s').realize()   
    ) == 'commette',\
    'commettre:s3'


def test_conjugation_fr_336():
    assert (
V("commettre").t('s').pe(1).n('p').realize()   
    ) == 'commettions',\
    'commettre:s4'


def test_conjugation_fr_337():
    assert (
V("commettre").t('s').pe(2).n('p').realize()   
    ) == 'commettiez',\
    'commettre:s5'


def test_conjugation_fr_338():
    assert (
V("commettre").t('s').pe(3).n('p').realize()   
    ) == 'commettent',\
    'commettre:s6'


def test_conjugation_fr_339():
    assert (
V("comprendre").t('pr').realize()   
    ) == 'comprenant',\
    'comprendre:pr'


def test_conjugation_fr_340():
    assert (
V("comprendre").t('p').pe(3).n('s').realize()   
    ) == 'comprend',\
    'comprendre:p3'


def test_conjugation_fr_341():
    assert (
V("comprendre").t('p').pe(1).n('s').realize()   
    ) == 'comprends',\
    'comprendre:p1'


def test_conjugation_fr_342():
    assert (
V("comprendre").t('p').pe(2).n('s').realize()   
    ) == 'comprends',\
    'comprendre:p2'


def test_conjugation_fr_343():
    assert (
V("comprendre").t('ip').pe(2).n('s').realize()   
    ) == 'comprends',\
    'comprendre:ip2'


def test_conjugation_fr_344():
    assert (
V("comprendre").t('p').pe(2).n('p').realize()   
    ) == 'comprenez',\
    'comprendre:p5'


def test_conjugation_fr_345():
    assert (
V("comprendre").t('ip').pe(2).n('p').realize()   
    ) == 'comprenez',\
    'comprendre:ip5'


def test_conjugation_fr_346():
    assert (
V("comprendre").t('p').pe(3).n('p').realize()   
    ) == 'comprennent',\
    'comprendre:p6'


def test_conjugation_fr_347():
    assert (
V("comprendre").t('p').pe(1).n('p').realize()   
    ) == 'comprenons',\
    'comprendre:p4'


def test_conjugation_fr_348():
    assert (
V("comprendre").t('ip').pe(1).n('p').realize()   
    ) == 'comprenons',\
    'comprendre:ip4'


def test_conjugation_fr_349():
    assert (
V("comprendre").t('pp').realize()   
    ) == 'compris',\
    'comprendre:pp'


def test_conjugation_fr_350():
    assert (
V("comprendre").t('s').pe(1).n('s').realize()   
    ) == 'comprenne',\
    'comprendre:s1'


def test_conjugation_fr_351():
    assert (
V("comprendre").t('s').pe(2).n('s').realize()   
    ) == 'comprennes',\
    'comprendre:s2'


def test_conjugation_fr_352():
    assert (
V("comprendre").t('s').pe(3).n('s').realize()   
    ) == 'comprenne',\
    'comprendre:s3'


def test_conjugation_fr_353():
    assert (
V("comprendre").t('s').pe(1).n('p').realize()   
    ) == 'comprenions',\
    'comprendre:s4'


def test_conjugation_fr_354():
    assert (
V("comprendre").t('s').pe(2).n('p').realize()   
    ) == 'compreniez',\
    'comprendre:s5'


def test_conjugation_fr_355():
    assert (
V("comprendre").t('s').pe(3).n('p').realize()   
    ) == 'comprennent',\
    'comprendre:s6'


def test_conjugation_fr_356():
    assert (
V("conclure").t('pr').realize()   
    ) == 'concluant',\
    'conclure:pr'


def test_conjugation_fr_357():
    assert (
V("conclure").t('p').pe(3).n('p').realize()   
    ) == 'concluent',\
    'conclure:p6'


def test_conjugation_fr_358():
    assert (
V("conclure").t('p').pe(2).n('p').realize()   
    ) == 'concluez',\
    'conclure:p5'


def test_conjugation_fr_359():
    assert (
V("conclure").t('ip').pe(2).n('p').realize()   
    ) == 'concluez',\
    'conclure:ip5'


def test_conjugation_fr_360():
    assert (
V("conclure").t('p').pe(1).n('p').realize()   
    ) == 'concluons',\
    'conclure:p4'


def test_conjugation_fr_361():
    assert (
V("conclure").t('ip').pe(1).n('p').realize()   
    ) == 'concluons',\
    'conclure:ip4'


def test_conjugation_fr_362():
    assert (
V("conclure").t('p').pe(1).n('s').realize()   
    ) == 'conclus',\
    'conclure:p1'


def test_conjugation_fr_363():
    assert (
V("conclure").t('p').pe(2).n('s').realize()   
    ) == 'conclus',\
    'conclure:p2'


def test_conjugation_fr_364():
    assert (
V("conclure").t('ip').pe(2).n('s').realize()   
    ) == 'conclus',\
    'conclure:ip2'


def test_conjugation_fr_365():
    assert (
V("conclure").t('p').pe(3).n('s').realize()   
    ) == 'conclut',\
    'conclure:p3'


def test_conjugation_fr_366():
    assert (
V("conclure").t('pp').realize()   
    ) == 'conclu',\
    'conclure:pp'


def test_conjugation_fr_367():
    assert (
V("conclure").t('s').pe(1).n('s').realize()   
    ) == 'conclue',\
    'conclure:s1'


def test_conjugation_fr_368():
    assert (
V("conclure").t('s').pe(2).n('s').realize()   
    ) == 'conclues',\
    'conclure:s2'


def test_conjugation_fr_369():
    assert (
V("conclure").t('s').pe(3).n('s').realize()   
    ) == 'conclue',\
    'conclure:s3'


def test_conjugation_fr_370():
    assert (
V("conclure").t('s').pe(1).n('p').realize()   
    ) == 'concluions',\
    'conclure:s4'


def test_conjugation_fr_371():
    assert (
V("conclure").t('s').pe(2).n('p').realize()   
    ) == 'concluiez',\
    'conclure:s5'


def test_conjugation_fr_372():
    assert (
V("conclure").t('s').pe(3).n('p').realize()   
    ) == 'concluent',\
    'conclure:s6'


def test_conjugation_fr_373():
    assert (
V("conduire").t('p').pe(1).n('s').realize()   
    ) == 'conduis',\
    'conduire:p1'


def test_conjugation_fr_374():
    assert (
V("conduire").t('p').pe(2).n('s').realize()   
    ) == 'conduis',\
    'conduire:p2'


def test_conjugation_fr_375():
    assert (
V("conduire").t('ip').pe(2).n('s').realize()   
    ) == 'conduis',\
    'conduire:ip2'


def test_conjugation_fr_376():
    assert (
V("conduire").t('pr').realize()   
    ) == 'conduisant',\
    'conduire:pr'


def test_conjugation_fr_377():
    assert (
V("conduire").t('p').pe(3).n('p').realize()   
    ) == 'conduisent',\
    'conduire:p6'


def test_conjugation_fr_378():
    assert (
V("conduire").t('p').pe(2).n('p').realize()   
    ) == 'conduisez',\
    'conduire:p5'


def test_conjugation_fr_379():
    assert (
V("conduire").t('ip').pe(2).n('p').realize()   
    ) == 'conduisez',\
    'conduire:ip5'


def test_conjugation_fr_380():
    assert (
V("conduire").t('p').pe(1).n('p').realize()   
    ) == 'conduisons',\
    'conduire:p4'


def test_conjugation_fr_381():
    assert (
V("conduire").t('ip').pe(1).n('p').realize()   
    ) == 'conduisons',\
    'conduire:ip4'


def test_conjugation_fr_382():
    assert (
V("conduire").t('p').pe(3).n('s').realize()   
    ) == 'conduit',\
    'conduire:p3'


def test_conjugation_fr_383():
    assert (
V("conduire").t('pp').realize()   
    ) == 'conduit',\
    'conduire:pp'


def test_conjugation_fr_384():
    assert (
V("conduire").t('s').pe(1).n('s').realize()   
    ) == 'conduise',\
    'conduire:s1'


def test_conjugation_fr_385():
    assert (
V("conduire").t('s').pe(2).n('s').realize()   
    ) == 'conduises',\
    'conduire:s2'


def test_conjugation_fr_386():
    assert (
V("conduire").t('s').pe(3).n('s').realize()   
    ) == 'conduise',\
    'conduire:s3'


def test_conjugation_fr_387():
    assert (
V("conduire").t('s').pe(1).n('p').realize()   
    ) == 'conduisions',\
    'conduire:s4'


def test_conjugation_fr_388():
    assert (
V("conduire").t('s').pe(2).n('p').realize()   
    ) == 'conduisiez',\
    'conduire:s5'


def test_conjugation_fr_389():
    assert (
V("conduire").t('s').pe(3).n('p').realize()   
    ) == 'conduisent',\
    'conduire:s6'


def test_conjugation_fr_390():
    assert (
V("confondre").t('p').pe(3).n('s').realize()   
    ) == 'confond',\
    'confondre:p3'


def test_conjugation_fr_391():
    assert (
V("confondre").t('pr').realize()   
    ) == 'confondant',\
    'confondre:pr'


def test_conjugation_fr_392():
    assert (
V("confondre").t('p').pe(3).n('p').realize()   
    ) == 'confondent',\
    'confondre:p6'


def test_conjugation_fr_393():
    assert (
V("confondre").t('p').pe(2).n('p').realize()   
    ) == 'confondez',\
    'confondre:p5'


def test_conjugation_fr_394():
    assert (
V("confondre").t('ip').pe(2).n('p').realize()   
    ) == 'confondez',\
    'confondre:ip5'


def test_conjugation_fr_395():
    assert (
V("confondre").t('p').pe(1).n('p').realize()   
    ) == 'confondons',\
    'confondre:p4'


def test_conjugation_fr_396():
    assert (
V("confondre").t('ip').pe(1).n('p').realize()   
    ) == 'confondons',\
    'confondre:ip4'


def test_conjugation_fr_397():
    assert (
V("confondre").t('p').pe(1).n('s').realize()   
    ) == 'confonds',\
    'confondre:p1'


def test_conjugation_fr_398():
    assert (
V("confondre").t('p').pe(2).n('s').realize()   
    ) == 'confonds',\
    'confondre:p2'


def test_conjugation_fr_399():
    assert (
V("confondre").t('ip').pe(2).n('s').realize()   
    ) == 'confonds',\
    'confondre:ip2'


def test_conjugation_fr_400():
    assert (
V("confondre").t('pp').realize()   
    ) == 'confondu',\
    'confondre:pp'


def test_conjugation_fr_401():
    assert (
V("confondre").t('s').pe(1).n('s').realize()   
    ) == 'confonde',\
    'confondre:s1'


def test_conjugation_fr_402():
    assert (
V("confondre").t('s').pe(2).n('s').realize()   
    ) == 'confondes',\
    'confondre:s2'


def test_conjugation_fr_403():
    assert (
V("confondre").t('s').pe(3).n('s').realize()   
    ) == 'confonde',\
    'confondre:s3'


def test_conjugation_fr_404():
    assert (
V("confondre").t('s').pe(1).n('p').realize()   
    ) == 'confondions',\
    'confondre:s4'


def test_conjugation_fr_405():
    assert (
V("confondre").t('s').pe(2).n('p').realize()   
    ) == 'confondiez',\
    'confondre:s5'


def test_conjugation_fr_406():
    assert (
V("confondre").t('s').pe(3).n('p').realize()   
    ) == 'confondent',\
    'confondre:s6'


def test_conjugation_fr_407():
    assert (
V("connaître").t('p').pe(1).n('s').realize()   
    ) == 'connais',\
    'connaître:p1'


def test_conjugation_fr_408():
    assert (
V("connaître").t('p').pe(2).n('s').realize()   
    ) == 'connais',\
    'connaître:p2'


def test_conjugation_fr_409():
    assert (
V("connaître").t('ip').pe(2).n('s').realize()   
    ) == 'connais',\
    'connaître:ip2'


def test_conjugation_fr_410():
    assert (
V("connaître").t('pr').realize()   
    ) == 'connaissant',\
    'connaître:pr'


def test_conjugation_fr_411():
    assert (
V("connaître").t('p').pe(3).n('p').realize()   
    ) == 'connaissent',\
    'connaître:p6'


def test_conjugation_fr_412():
    assert (
V("connaître").t('p').pe(2).n('p').realize()   
    ) == 'connaissez',\
    'connaître:p5'


def test_conjugation_fr_413():
    assert (
V("connaître").t('ip').pe(2).n('p').realize()   
    ) == 'connaissez',\
    'connaître:ip5'


def test_conjugation_fr_414():
    assert (
V("connaître").t('p').pe(1).n('p').realize()   
    ) == 'connaissons',\
    'connaître:p4'


def test_conjugation_fr_415():
    assert (
V("connaître").t('ip').pe(1).n('p').realize()   
    ) == 'connaissons',\
    'connaître:ip4'


def test_conjugation_fr_416():
    assert (
V("connaître").t('p').pe(3).n('s').realize()   
    ) == 'connaît',\
    'connaître:p3'


def test_conjugation_fr_417():
    assert (
V("connaître").t('pp').realize()   
    ) == 'connu',\
    'connaître:pp'


def test_conjugation_fr_418():
    assert (
V("connaître").t('s').pe(1).n('s').realize()   
    ) == 'connaisse',\
    'connaître:s1'


def test_conjugation_fr_419():
    assert (
V("connaître").t('s').pe(2).n('s').realize()   
    ) == 'connaisses',\
    'connaître:s2'


def test_conjugation_fr_420():
    assert (
V("connaître").t('s').pe(3).n('s').realize()   
    ) == 'connaisse',\
    'connaître:s3'


def test_conjugation_fr_421():
    assert (
V("connaître").t('s').pe(1).n('p').realize()   
    ) == 'connaissions',\
    'connaître:s4'


def test_conjugation_fr_422():
    assert (
V("connaître").t('s').pe(2).n('p').realize()   
    ) == 'connaissiez',\
    'connaître:s5'


def test_conjugation_fr_423():
    assert (
V("connaître").t('s').pe(3).n('p').realize()   
    ) == 'connaissent',\
    'connaître:s6'


def test_conjugation_fr_424():
    assert (
V("conquérir").t('p').pe(1).n('s').realize()   
    ) == 'conquiers',\
    'conquérir:p1'


def test_conjugation_fr_425():
    assert (
V("conquérir").t('p').pe(2).n('s').realize()   
    ) == 'conquiers',\
    'conquérir:p2'


def test_conjugation_fr_426():
    assert (
V("conquérir").t('ip').pe(2).n('s').realize()   
    ) == 'conquiers',\
    'conquérir:ip2'


def test_conjugation_fr_427():
    assert (
V("conquérir").t('p').pe(3).n('s').realize()   
    ) == 'conquiert',\
    'conquérir:p3'


def test_conjugation_fr_428():
    assert (
V("conquérir").t('p').pe(3).n('p').realize()   
    ) == 'conquièrent',\
    'conquérir:p6'


def test_conjugation_fr_429():
    assert (
V("conquérir").t('pr').realize()   
    ) == 'conquérant',\
    'conquérir:pr'


def test_conjugation_fr_430():
    assert (
V("conquérir").t('p').pe(2).n('p').realize()   
    ) == 'conquérez',\
    'conquérir:p5'


def test_conjugation_fr_431():
    assert (
V("conquérir").t('ip').pe(2).n('p').realize()   
    ) == 'conquérez',\
    'conquérir:ip5'


def test_conjugation_fr_432():
    assert (
V("conquérir").t('p').pe(1).n('p').realize()   
    ) == 'conquérons',\
    'conquérir:p4'


def test_conjugation_fr_433():
    assert (
V("conquérir").t('ip').pe(1).n('p').realize()   
    ) == 'conquérons',\
    'conquérir:ip4'


def test_conjugation_fr_434():
    assert (
V("conquérir").t('pp').realize()   
    ) == 'conquis',\
    'conquérir:pp'


def test_conjugation_fr_435():
    assert (
V("conquérir").t('s').pe(1).n('s').realize()   
    ) == 'conquière',\
    'conquérir:s1'


def test_conjugation_fr_436():
    assert (
V("conquérir").t('s').pe(2).n('s').realize()   
    ) == 'conquières',\
    'conquérir:s2'


def test_conjugation_fr_437():
    assert (
V("conquérir").t('s').pe(3).n('s').realize()   
    ) == 'conquière',\
    'conquérir:s3'


def test_conjugation_fr_438():
    assert (
V("conquérir").t('s').pe(1).n('p').realize()   
    ) == 'conquérions',\
    'conquérir:s4'


def test_conjugation_fr_439():
    assert (
V("conquérir").t('s').pe(2).n('p').realize()   
    ) == 'conquériez',\
    'conquérir:s5'


def test_conjugation_fr_440():
    assert (
V("conquérir").t('s').pe(3).n('p').realize()   
    ) == 'conquièrent',\
    'conquérir:s6'


def test_conjugation_fr_441():
    assert (
V("consentir").t('p').pe(1).n('s').realize()   
    ) == 'consens',\
    'consentir:p1'


def test_conjugation_fr_442():
    assert (
V("consentir").t('p').pe(2).n('s').realize()   
    ) == 'consens',\
    'consentir:p2'


def test_conjugation_fr_443():
    assert (
V("consentir").t('ip').pe(2).n('s').realize()   
    ) == 'consens',\
    'consentir:ip2'


def test_conjugation_fr_444():
    assert (
V("consentir").t('p').pe(3).n('s').realize()   
    ) == 'consent',\
    'consentir:p3'


def test_conjugation_fr_445():
    assert (
V("consentir").t('pr').realize()   
    ) == 'consentant',\
    'consentir:pr'


def test_conjugation_fr_446():
    assert (
V("consentir").t('p').pe(3).n('p').realize()   
    ) == 'consentent',\
    'consentir:p6'


def test_conjugation_fr_447():
    assert (
V("consentir").t('p').pe(2).n('p').realize()   
    ) == 'consentez',\
    'consentir:p5'


def test_conjugation_fr_448():
    assert (
V("consentir").t('ip').pe(2).n('p').realize()   
    ) == 'consentez',\
    'consentir:ip5'


def test_conjugation_fr_449():
    assert (
V("consentir").t('p').pe(1).n('p').realize()   
    ) == 'consentons',\
    'consentir:p4'


def test_conjugation_fr_450():
    assert (
V("consentir").t('ip').pe(1).n('p').realize()   
    ) == 'consentons',\
    'consentir:ip4'


def test_conjugation_fr_451():
    assert (
V("consentir").t('pp').realize()   
    ) == 'consenti',\
    'consentir:pp'


def test_conjugation_fr_452():
    assert (
V("consentir").t('s').pe(1).n('s').realize()   
    ) == 'consente',\
    'consentir:s1'


def test_conjugation_fr_453():
    assert (
V("consentir").t('s').pe(2).n('s').realize()   
    ) == 'consentes',\
    'consentir:s2'


def test_conjugation_fr_454():
    assert (
V("consentir").t('s').pe(3).n('s').realize()   
    ) == 'consente',\
    'consentir:s3'


def test_conjugation_fr_455():
    assert (
V("consentir").t('s').pe(1).n('p').realize()   
    ) == 'consentions',\
    'consentir:s4'


def test_conjugation_fr_456():
    assert (
V("consentir").t('s').pe(2).n('p').realize()   
    ) == 'consentiez',\
    'consentir:s5'


def test_conjugation_fr_457():
    assert (
V("consentir").t('s').pe(3).n('p').realize()   
    ) == 'consentent',\
    'consentir:s6'


def test_conjugation_fr_458():
    assert (
V("construire").t('p').pe(1).n('s').realize()   
    ) == 'construis',\
    'construire:p1'


def test_conjugation_fr_459():
    assert (
V("construire").t('p').pe(2).n('s').realize()   
    ) == 'construis',\
    'construire:p2'


def test_conjugation_fr_460():
    assert (
V("construire").t('ip').pe(2).n('s').realize()   
    ) == 'construis',\
    'construire:ip2'


def test_conjugation_fr_461():
    assert (
V("construire").t('pr').realize()   
    ) == 'construisant',\
    'construire:pr'


def test_conjugation_fr_462():
    assert (
V("construire").t('p').pe(3).n('p').realize()   
    ) == 'construisent',\
    'construire:p6'


def test_conjugation_fr_463():
    assert (
V("construire").t('p').pe(2).n('p').realize()   
    ) == 'construisez',\
    'construire:p5'


def test_conjugation_fr_464():
    assert (
V("construire").t('ip').pe(2).n('p').realize()   
    ) == 'construisez',\
    'construire:ip5'


def test_conjugation_fr_465():
    assert (
V("construire").t('p').pe(1).n('p').realize()   
    ) == 'construisons',\
    'construire:p4'


def test_conjugation_fr_466():
    assert (
V("construire").t('ip').pe(1).n('p').realize()   
    ) == 'construisons',\
    'construire:ip4'


def test_conjugation_fr_467():
    assert (
V("construire").t('p').pe(3).n('s').realize()   
    ) == 'construit',\
    'construire:p3'


def test_conjugation_fr_468():
    assert (
V("construire").t('pp').realize()   
    ) == 'construit',\
    'construire:pp'


def test_conjugation_fr_469():
    assert (
V("construire").t('s').pe(1).n('s').realize()   
    ) == 'construise',\
    'construire:s1'


def test_conjugation_fr_470():
    assert (
V("construire").t('s').pe(2).n('s').realize()   
    ) == 'construises',\
    'construire:s2'


def test_conjugation_fr_471():
    assert (
V("construire").t('s').pe(3).n('s').realize()   
    ) == 'construise',\
    'construire:s3'


def test_conjugation_fr_472():
    assert (
V("construire").t('s').pe(1).n('p').realize()   
    ) == 'construisions',\
    'construire:s4'


def test_conjugation_fr_473():
    assert (
V("construire").t('s').pe(2).n('p').realize()   
    ) == 'construisiez',\
    'construire:s5'


def test_conjugation_fr_474():
    assert (
V("construire").t('s').pe(3).n('p').realize()   
    ) == 'construisent',\
    'construire:s6'


def test_conjugation_fr_475():
    assert (
V("contenir").t('pr').realize()   
    ) == 'contenant',\
    'contenir:pr'


def test_conjugation_fr_476():
    assert (
V("contenir").t('p').pe(2).n('p').realize()   
    ) == 'contenez',\
    'contenir:p5'


def test_conjugation_fr_477():
    assert (
V("contenir").t('ip').pe(2).n('p').realize()   
    ) == 'contenez',\
    'contenir:ip5'


def test_conjugation_fr_478():
    assert (
V("contenir").t('p').pe(1).n('p').realize()   
    ) == 'contenons',\
    'contenir:p4'


def test_conjugation_fr_479():
    assert (
V("contenir").t('ip').pe(1).n('p').realize()   
    ) == 'contenons',\
    'contenir:ip4'


def test_conjugation_fr_480():
    assert (
V("contenir").t('p').pe(3).n('p').realize()   
    ) == 'contiennent',\
    'contenir:p6'


def test_conjugation_fr_481():
    assert (
V("contenir").t('p').pe(1).n('s').realize()   
    ) == 'contiens',\
    'contenir:p1'


def test_conjugation_fr_482():
    assert (
V("contenir").t('p').pe(2).n('s').realize()   
    ) == 'contiens',\
    'contenir:p2'


def test_conjugation_fr_483():
    assert (
V("contenir").t('ip').pe(2).n('s').realize()   
    ) == 'contiens',\
    'contenir:ip2'


def test_conjugation_fr_484():
    assert (
V("contenir").t('p').pe(3).n('s').realize()   
    ) == 'contient',\
    'contenir:p3'


def test_conjugation_fr_485():
    assert (
V("contenir").t('pp').realize()   
    ) == 'contenu',\
    'contenir:pp'


def test_conjugation_fr_486():
    assert (
V("contenir").t('s').pe(1).n('s').realize()   
    ) == 'contienne',\
    'contenir:s1'


def test_conjugation_fr_487():
    assert (
V("contenir").t('s').pe(2).n('s').realize()   
    ) == 'contiennes',\
    'contenir:s2'


def test_conjugation_fr_488():
    assert (
V("contenir").t('s').pe(3).n('s').realize()   
    ) == 'contienne',\
    'contenir:s3'


def test_conjugation_fr_489():
    assert (
V("contenir").t('s').pe(1).n('p').realize()   
    ) == 'contenions',\
    'contenir:s4'


def test_conjugation_fr_490():
    assert (
V("contenir").t('s').pe(2).n('p').realize()   
    ) == 'conteniez',\
    'contenir:s5'


def test_conjugation_fr_491():
    assert (
V("contenir").t('s').pe(3).n('p').realize()   
    ) == 'contiennent',\
    'contenir:s6'


def test_conjugation_fr_492():
    assert (
V("convaincre").t('p').pe(3).n('s').realize()   
    ) == 'convainc',\
    'convaincre:p3'


def test_conjugation_fr_493():
    assert (
V("convaincre").t('p').pe(1).n('s').realize()   
    ) == 'convaincs',\
    'convaincre:p1'


def test_conjugation_fr_494():
    assert (
V("convaincre").t('p').pe(2).n('s').realize()   
    ) == 'convaincs',\
    'convaincre:p2'


def test_conjugation_fr_495():
    assert (
V("convaincre").t('ip').pe(2).n('s').realize()   
    ) == 'convaincs',\
    'convaincre:ip2'


def test_conjugation_fr_496():
    assert (
V("convaincre").t('pr').realize()   
    ) == 'convainquant',\
    'convaincre:pr'


def test_conjugation_fr_497():
    assert (
V("convaincre").t('p').pe(3).n('p').realize()   
    ) == 'convainquent',\
    'convaincre:p6'


def test_conjugation_fr_498():
    assert (
V("convaincre").t('p').pe(2).n('p').realize()   
    ) == 'convainquez',\
    'convaincre:p5'


def test_conjugation_fr_499():
    assert (
V("convaincre").t('ip').pe(2).n('p').realize()   
    ) == 'convainquez',\
    'convaincre:ip5'


def test_conjugation_fr_500():
    assert (
V("convaincre").t('p').pe(1).n('p').realize()   
    ) == 'convainquons',\
    'convaincre:p4'


def test_conjugation_fr_501():
    assert (
V("convaincre").t('ip').pe(1).n('p').realize()   
    ) == 'convainquons',\
    'convaincre:ip4'


def test_conjugation_fr_502():
    assert (
V("convaincre").t('pp').realize()   
    ) == 'convaincu',\
    'convaincre:pp'


def test_conjugation_fr_503():
    assert (
V("convaincre").t('s').pe(1).n('s').realize()   
    ) == 'convainque',\
    'convaincre:s1'


def test_conjugation_fr_504():
    assert (
V("convaincre").t('s').pe(2).n('s').realize()   
    ) == 'convainques',\
    'convaincre:s2'


def test_conjugation_fr_505():
    assert (
V("convaincre").t('s').pe(3).n('s').realize()   
    ) == 'convainque',\
    'convaincre:s3'


def test_conjugation_fr_506():
    assert (
V("convaincre").t('s').pe(1).n('p').realize()   
    ) == 'convainquions',\
    'convaincre:s4'


def test_conjugation_fr_507():
    assert (
V("convaincre").t('s').pe(2).n('p').realize()   
    ) == 'convainquiez',\
    'convaincre:s5'


def test_conjugation_fr_508():
    assert (
V("convaincre").t('s').pe(3).n('p').realize()   
    ) == 'convainquent',\
    'convaincre:s6'


def test_conjugation_fr_509():
    assert (
V("convenir").t('pr').realize()   
    ) == 'convenant',\
    'convenir:pr'


def test_conjugation_fr_510():
    assert (
V("convenir").t('p').pe(2).n('p').realize()   
    ) == 'convenez',\
    'convenir:p5'


def test_conjugation_fr_511():
    assert (
V("convenir").t('ip').pe(2).n('p').realize()   
    ) == 'convenez',\
    'convenir:ip5'


def test_conjugation_fr_512():
    assert (
V("convenir").t('p').pe(1).n('p').realize()   
    ) == 'convenons',\
    'convenir:p4'


def test_conjugation_fr_513():
    assert (
V("convenir").t('ip').pe(1).n('p').realize()   
    ) == 'convenons',\
    'convenir:ip4'


def test_conjugation_fr_514():
    assert (
V("convenir").t('p').pe(3).n('p').realize()   
    ) == 'conviennent',\
    'convenir:p6'


def test_conjugation_fr_515():
    assert (
V("convenir").t('p').pe(1).n('s').realize()   
    ) == 'conviens',\
    'convenir:p1'


def test_conjugation_fr_516():
    assert (
V("convenir").t('p').pe(2).n('s').realize()   
    ) == 'conviens',\
    'convenir:p2'


def test_conjugation_fr_517():
    assert (
V("convenir").t('ip').pe(2).n('s').realize()   
    ) == 'conviens',\
    'convenir:ip2'


def test_conjugation_fr_518():
    assert (
V("convenir").t('p').pe(3).n('s').realize()   
    ) == 'convient',\
    'convenir:p3'


def test_conjugation_fr_519():
    assert (
V("convenir").t('pp').realize()   
    ) == 'convenu',\
    'convenir:pp'


def test_conjugation_fr_520():
    assert (
V("convenir").t('s').pe(1).n('s').realize()   
    ) == 'convienne',\
    'convenir:s1'


def test_conjugation_fr_521():
    assert (
V("convenir").t('s').pe(2).n('s').realize()   
    ) == 'conviennes',\
    'convenir:s2'


def test_conjugation_fr_522():
    assert (
V("convenir").t('s').pe(3).n('s').realize()   
    ) == 'convienne',\
    'convenir:s3'


def test_conjugation_fr_523():
    assert (
V("convenir").t('s').pe(1).n('p').realize()   
    ) == 'convenions',\
    'convenir:s4'


def test_conjugation_fr_524():
    assert (
V("convenir").t('s').pe(2).n('p').realize()   
    ) == 'conveniez',\
    'convenir:s5'


def test_conjugation_fr_525():
    assert (
V("convenir").t('s').pe(3).n('p').realize()   
    ) == 'conviennent',\
    'convenir:s6'


def test_conjugation_fr_526():
    assert (
V("coudre").t('p').pe(3).n('s').realize()   
    ) == 'coud',\
    'coudre:p3'


def test_conjugation_fr_527():
    assert (
V("coudre").t('p').pe(1).n('s').realize()   
    ) == 'couds',\
    'coudre:p1'


def test_conjugation_fr_528():
    assert (
V("coudre").t('p').pe(2).n('s').realize()   
    ) == 'couds',\
    'coudre:p2'


def test_conjugation_fr_529():
    assert (
V("coudre").t('ip').pe(2).n('s').realize()   
    ) == 'couds',\
    'coudre:ip2'


def test_conjugation_fr_530():
    assert (
V("coudre").t('pr').realize()   
    ) == 'cousant',\
    'coudre:pr'


def test_conjugation_fr_531():
    assert (
V("coudre").t('p').pe(3).n('p').realize()   
    ) == 'cousent',\
    'coudre:p6'


def test_conjugation_fr_532():
    assert (
V("coudre").t('p').pe(2).n('p').realize()   
    ) == 'cousez',\
    'coudre:p5'


def test_conjugation_fr_533():
    assert (
V("coudre").t('ip').pe(2).n('p').realize()   
    ) == 'cousez',\
    'coudre:ip5'


def test_conjugation_fr_534():
    assert (
V("coudre").t('p').pe(1).n('p').realize()   
    ) == 'cousons',\
    'coudre:p4'


def test_conjugation_fr_535():
    assert (
V("coudre").t('ip').pe(1).n('p').realize()   
    ) == 'cousons',\
    'coudre:ip4'


def test_conjugation_fr_536():
    assert (
V("coudre").t('pp').realize()   
    ) == 'cousu',\
    'coudre:pp'


def test_conjugation_fr_537():
    assert (
V("coudre").t('s').pe(1).n('s').realize()   
    ) == 'couse',\
    'coudre:s1'


def test_conjugation_fr_538():
    assert (
V("coudre").t('s').pe(2).n('s').realize()   
    ) == 'couses',\
    'coudre:s2'


def test_conjugation_fr_539():
    assert (
V("coudre").t('s').pe(3).n('s').realize()   
    ) == 'couse',\
    'coudre:s3'


def test_conjugation_fr_540():
    assert (
V("coudre").t('s').pe(1).n('p').realize()   
    ) == 'cousions',\
    'coudre:s4'


def test_conjugation_fr_541():
    assert (
V("coudre").t('s').pe(2).n('p').realize()   
    ) == 'cousiez',\
    'coudre:s5'


def test_conjugation_fr_542():
    assert (
V("coudre").t('s').pe(3).n('p').realize()   
    ) == 'cousent',\
    'coudre:s6'


def test_conjugation_fr_543():
    assert (
V("courir").t('pr').realize()   
    ) == 'courant',\
    'courir:pr'


def test_conjugation_fr_544():
    assert (
V("courir").t('p').pe(3).n('p').realize()   
    ) == 'courent',\
    'courir:p6'


def test_conjugation_fr_545():
    assert (
V("courir").t('p').pe(2).n('p').realize()   
    ) == 'courez',\
    'courir:p5'


def test_conjugation_fr_546():
    assert (
V("courir").t('ip').pe(2).n('p').realize()   
    ) == 'courez',\
    'courir:ip5'


def test_conjugation_fr_547():
    assert (
V("courir").t('p').pe(1).n('p').realize()   
    ) == 'courons',\
    'courir:p4'


def test_conjugation_fr_548():
    assert (
V("courir").t('ip').pe(1).n('p').realize()   
    ) == 'courons',\
    'courir:ip4'


def test_conjugation_fr_549():
    assert (
V("courir").t('p').pe(1).n('s').realize()   
    ) == 'cours',\
    'courir:p1'


def test_conjugation_fr_550():
    assert (
V("courir").t('p').pe(2).n('s').realize()   
    ) == 'cours',\
    'courir:p2'


def test_conjugation_fr_551():
    assert (
V("courir").t('ip').pe(2).n('s').realize()   
    ) == 'cours',\
    'courir:ip2'


def test_conjugation_fr_552():
    assert (
V("courir").t('p').pe(3).n('s').realize()   
    ) == 'court',\
    'courir:p3'


def test_conjugation_fr_553():
    assert (
V("courir").t('pp').realize()   
    ) == 'couru',\
    'courir:pp'


def test_conjugation_fr_554():
    assert (
V("courir").t('s').pe(1).n('s').realize()   
    ) == 'coure',\
    'courir:s1'


def test_conjugation_fr_555():
    assert (
V("courir").t('s').pe(2).n('s').realize()   
    ) == 'coures',\
    'courir:s2'


def test_conjugation_fr_556():
    assert (
V("courir").t('s').pe(3).n('s').realize()   
    ) == 'coure',\
    'courir:s3'


def test_conjugation_fr_557():
    assert (
V("courir").t('s').pe(1).n('p').realize()   
    ) == 'courions',\
    'courir:s4'


def test_conjugation_fr_558():
    assert (
V("courir").t('s').pe(2).n('p').realize()   
    ) == 'couriez',\
    'courir:s5'


def test_conjugation_fr_559():
    assert (
V("courir").t('s').pe(3).n('p').realize()   
    ) == 'courent',\
    'courir:s6'


def test_conjugation_fr_560():
    assert (
V("couvrir").t('pr').realize()   
    ) == 'couvrant',\
    'couvrir:pr'


def test_conjugation_fr_561():
    assert (
V("couvrir").t('p').pe(1).n('s').realize()   
    ) == 'couvre',\
    'couvrir:p1'


def test_conjugation_fr_562():
    assert (
V("couvrir").t('p').pe(3).n('s').realize()   
    ) == 'couvre',\
    'couvrir:p3'


def test_conjugation_fr_563():
    assert (
V("couvrir").t('ip').pe(2).n('s').realize()   
    ) == 'couvre',\
    'couvrir:ip2'


def test_conjugation_fr_564():
    assert (
V("couvrir").t('p').pe(3).n('p').realize()   
    ) == 'couvrent',\
    'couvrir:p6'


def test_conjugation_fr_565():
    assert (
V("couvrir").t('p').pe(2).n('s').realize()   
    ) == 'couvres',\
    'couvrir:p2'


def test_conjugation_fr_566():
    assert (
V("couvrir").t('p').pe(2).n('p').realize()   
    ) == 'couvrez',\
    'couvrir:p5'


def test_conjugation_fr_567():
    assert (
V("couvrir").t('ip').pe(2).n('p').realize()   
    ) == 'couvrez',\
    'couvrir:ip5'


def test_conjugation_fr_568():
    assert (
V("couvrir").t('p').pe(1).n('p').realize()   
    ) == 'couvrons',\
    'couvrir:p4'


def test_conjugation_fr_569():
    assert (
V("couvrir").t('ip').pe(1).n('p').realize()   
    ) == 'couvrons',\
    'couvrir:ip4'


def test_conjugation_fr_570():
    assert (
V("couvrir").t('pp').realize()   
    ) == 'couvert',\
    'couvrir:pp'


def test_conjugation_fr_571():
    assert (
V("couvrir").t('s').pe(1).n('s').realize()   
    ) == 'couvre',\
    'couvrir:s1'


def test_conjugation_fr_572():
    assert (
V("couvrir").t('s').pe(2).n('s').realize()   
    ) == 'couvres',\
    'couvrir:s2'


def test_conjugation_fr_573():
    assert (
V("couvrir").t('s').pe(3).n('s').realize()   
    ) == 'couvre',\
    'couvrir:s3'


def test_conjugation_fr_574():
    assert (
V("couvrir").t('s').pe(1).n('p').realize()   
    ) == 'couvrions',\
    'couvrir:s4'


def test_conjugation_fr_575():
    assert (
V("couvrir").t('s').pe(2).n('p').realize()   
    ) == 'couvriez',\
    'couvrir:s5'


def test_conjugation_fr_576():
    assert (
V("couvrir").t('s').pe(3).n('p').realize()   
    ) == 'couvrent',\
    'couvrir:s6'


def test_conjugation_fr_577():
    assert (
V("craindre").t('pr').realize()   
    ) == 'craignant',\
    'craindre:pr'


def test_conjugation_fr_578():
    assert (
V("craindre").t('p').pe(3).n('p').realize()   
    ) == 'craignent',\
    'craindre:p6'


def test_conjugation_fr_579():
    assert (
V("craindre").t('p').pe(2).n('p').realize()   
    ) == 'craignez',\
    'craindre:p5'


def test_conjugation_fr_580():
    assert (
V("craindre").t('ip').pe(2).n('p').realize()   
    ) == 'craignez',\
    'craindre:ip5'


def test_conjugation_fr_581():
    assert (
V("craindre").t('p').pe(1).n('p').realize()   
    ) == 'craignons',\
    'craindre:p4'


def test_conjugation_fr_582():
    assert (
V("craindre").t('ip').pe(1).n('p').realize()   
    ) == 'craignons',\
    'craindre:ip4'


def test_conjugation_fr_583():
    assert (
V("craindre").t('p').pe(1).n('s').realize()   
    ) == 'crains',\
    'craindre:p1'


def test_conjugation_fr_584():
    assert (
V("craindre").t('p').pe(2).n('s').realize()   
    ) == 'crains',\
    'craindre:p2'


def test_conjugation_fr_585():
    assert (
V("craindre").t('ip').pe(2).n('s').realize()   
    ) == 'crains',\
    'craindre:ip2'


def test_conjugation_fr_586():
    assert (
V("craindre").t('p').pe(3).n('s').realize()   
    ) == 'craint',\
    'craindre:p3'


def test_conjugation_fr_587():
    assert (
V("craindre").t('pp').realize()   
    ) == 'craint',\
    'craindre:pp'


def test_conjugation_fr_588():
    assert (
V("craindre").t('s').pe(1).n('s').realize()   
    ) == 'craigne',\
    'craindre:s1'


def test_conjugation_fr_589():
    assert (
V("craindre").t('s').pe(2).n('s').realize()   
    ) == 'craignes',\
    'craindre:s2'


def test_conjugation_fr_590():
    assert (
V("craindre").t('s').pe(3).n('s').realize()   
    ) == 'craigne',\
    'craindre:s3'


def test_conjugation_fr_591():
    assert (
V("craindre").t('s').pe(1).n('p').realize()   
    ) == 'craignions',\
    'craindre:s4'


def test_conjugation_fr_592():
    assert (
V("craindre").t('s').pe(2).n('p').realize()   
    ) == 'craigniez',\
    'craindre:s5'


def test_conjugation_fr_593():
    assert (
V("craindre").t('s').pe(3).n('p').realize()   
    ) == 'craignent',\
    'craindre:s6'


def test_conjugation_fr_594():
    assert (
V("croire").t('p').pe(3).n('p').realize()   
    ) == 'croient',\
    'croire:p6'


def test_conjugation_fr_595():
    assert (
V("croire").t('p').pe(1).n('s').realize()   
    ) == 'crois',\
    'croire:p1'


def test_conjugation_fr_596():
    assert (
V("croire").t('p').pe(2).n('s').realize()   
    ) == 'crois',\
    'croire:p2'


def test_conjugation_fr_597():
    assert (
V("croire").t('ip').pe(2).n('s').realize()   
    ) == 'crois',\
    'croire:ip2'


def test_conjugation_fr_598():
    assert (
V("croire").t('p').pe(3).n('s').realize()   
    ) == 'croit',\
    'croire:p3'


def test_conjugation_fr_599():
    assert (
V("croire").t('pr').realize()   
    ) == 'croyant',\
    'croire:pr'


def test_conjugation_fr_600():
    assert (
V("croire").t('p').pe(2).n('p').realize()   
    ) == 'croyez',\
    'croire:p5'


def test_conjugation_fr_601():
    assert (
V("croire").t('ip').pe(2).n('p').realize()   
    ) == 'croyez',\
    'croire:ip5'


def test_conjugation_fr_602():
    assert (
V("croire").t('p').pe(1).n('p').realize()   
    ) == 'croyons',\
    'croire:p4'


def test_conjugation_fr_603():
    assert (
V("croire").t('ip').pe(1).n('p').realize()   
    ) == 'croyons',\
    'croire:ip4'


def test_conjugation_fr_604():
    assert (
V("croire").t('pp').realize()   
    ) == 'cru',\
    'croire:pp'


def test_conjugation_fr_605():
    assert (
V("croire").t('s').pe(1).n('s').realize()   
    ) == 'croie',\
    'croire:s1'


def test_conjugation_fr_606():
    assert (
V("croire").t('s').pe(2).n('s').realize()   
    ) == 'croies',\
    'croire:s2'


def test_conjugation_fr_607():
    assert (
V("croire").t('s').pe(3).n('s').realize()   
    ) == 'croie',\
    'croire:s3'


def test_conjugation_fr_608():
    assert (
V("croire").t('s').pe(1).n('p').realize()   
    ) == 'croyions',\
    'croire:s4'


def test_conjugation_fr_609():
    assert (
V("croire").t('s').pe(2).n('p').realize()   
    ) == 'croyiez',\
    'croire:s5'


def test_conjugation_fr_610():
    assert (
V("croire").t('s').pe(3).n('p').realize()   
    ) == 'croient',\
    'croire:s6'


def test_conjugation_fr_611():
    assert (
V("croître").t('pr').realize()   
    ) == 'croissant',\
    'croître:pr'


def test_conjugation_fr_612():
    assert (
V("croître").t('p').pe(3).n('p').realize()   
    ) == 'croissent',\
    'croître:p6'


def test_conjugation_fr_613():
    assert (
V("croître").t('p').pe(2).n('p').realize()   
    ) == 'croissez',\
    'croître:p5'


def test_conjugation_fr_614():
    assert (
V("croître").t('ip').pe(2).n('p').realize()   
    ) == 'croissez',\
    'croître:ip5'


def test_conjugation_fr_615():
    assert (
V("croître").t('p').pe(1).n('p').realize()   
    ) == 'croissons',\
    'croître:p4'


def test_conjugation_fr_616():
    assert (
V("croître").t('ip').pe(1).n('p').realize()   
    ) == 'croissons',\
    'croître:ip4'


def test_conjugation_fr_617():
    assert (
V("croître").t('p').pe(1).n('s').realize()   
    ) == 'croîs',\
    'croître:p1'


def test_conjugation_fr_618():
    assert (
V("croître").t('p').pe(2).n('s').realize()   
    ) == 'croîs',\
    'croître:p2'


def test_conjugation_fr_619():
    assert (
V("croître").t('ip').pe(2).n('s').realize()   
    ) == 'croîs',\
    'croître:ip2'


def test_conjugation_fr_620():
    assert (
V("croître").t('p').pe(3).n('s').realize()   
    ) == 'croît',\
    'croître:p3'


def test_conjugation_fr_621():
    assert (
V("croître").t('pp').realize()   
    ) == 'crû',\
    'croître:pp'


def test_conjugation_fr_622():
    assert (
V("croître").t('s').pe(1).n('s').realize()   
    ) == 'croisse',\
    'croître:s1'


def test_conjugation_fr_623():
    assert (
V("croître").t('s').pe(2).n('s').realize()   
    ) == 'croisses',\
    'croître:s2'


def test_conjugation_fr_624():
    assert (
V("croître").t('s').pe(3).n('s').realize()   
    ) == 'croisse',\
    'croître:s3'


def test_conjugation_fr_625():
    assert (
V("croître").t('s').pe(1).n('p').realize()   
    ) == 'croissions',\
    'croître:s4'


def test_conjugation_fr_626():
    assert (
V("croître").t('s').pe(2).n('p').realize()   
    ) == 'croissiez',\
    'croître:s5'


def test_conjugation_fr_627():
    assert (
V("croître").t('s').pe(3).n('p').realize()   
    ) == 'croissent',\
    'croître:s6'


def test_conjugation_fr_628():
    assert (
V("cueillir").t('pr').realize()   
    ) == 'cueillant',\
    'cueillir:pr'


def test_conjugation_fr_629():
    assert (
V("cueillir").t('p').pe(1).n('s').realize()   
    ) == 'cueille',\
    'cueillir:p1'


def test_conjugation_fr_630():
    assert (
V("cueillir").t('p').pe(3).n('s').realize()   
    ) == 'cueille',\
    'cueillir:p3'


def test_conjugation_fr_631():
    assert (
V("cueillir").t('ip').pe(2).n('s').realize()   
    ) == 'cueille',\
    'cueillir:ip2'


def test_conjugation_fr_632():
    assert (
V("cueillir").t('p').pe(3).n('p').realize()   
    ) == 'cueillent',\
    'cueillir:p6'


def test_conjugation_fr_633():
    assert (
V("cueillir").t('p').pe(2).n('s').realize()   
    ) == 'cueilles',\
    'cueillir:p2'


def test_conjugation_fr_634():
    assert (
V("cueillir").t('p').pe(2).n('p').realize()   
    ) == 'cueillez',\
    'cueillir:p5'


def test_conjugation_fr_635():
    assert (
V("cueillir").t('ip').pe(2).n('p').realize()   
    ) == 'cueillez',\
    'cueillir:ip5'


def test_conjugation_fr_636():
    assert (
V("cueillir").t('p').pe(1).n('p').realize()   
    ) == 'cueillons',\
    'cueillir:p4'


def test_conjugation_fr_637():
    assert (
V("cueillir").t('ip').pe(1).n('p').realize()   
    ) == 'cueillons',\
    'cueillir:ip4'


def test_conjugation_fr_638():
    assert (
V("cueillir").t('pp').realize()   
    ) == 'cueilli',\
    'cueillir:pp'


def test_conjugation_fr_639():
    assert (
V("cueillir").t('s').pe(1).n('s').realize()   
    ) == 'cueille',\
    'cueillir:s1'


def test_conjugation_fr_640():
    assert (
V("cueillir").t('s').pe(2).n('s').realize()   
    ) == 'cueilles',\
    'cueillir:s2'


def test_conjugation_fr_641():
    assert (
V("cueillir").t('s').pe(3).n('s').realize()   
    ) == 'cueille',\
    'cueillir:s3'


def test_conjugation_fr_642():
    assert (
V("cueillir").t('s').pe(1).n('p').realize()   
    ) == 'cueillions',\
    'cueillir:s4'


def test_conjugation_fr_643():
    assert (
V("cueillir").t('s').pe(2).n('p').realize()   
    ) == 'cueilliez',\
    'cueillir:s5'


def test_conjugation_fr_644():
    assert (
V("cueillir").t('s').pe(3).n('p').realize()   
    ) == 'cueillent',\
    'cueillir:s6'


def test_conjugation_fr_645():
    assert (
V("cuire").t('p').pe(1).n('s').realize()   
    ) == 'cuis',\
    'cuire:p1'


def test_conjugation_fr_646():
    assert (
V("cuire").t('p').pe(2).n('s').realize()   
    ) == 'cuis',\
    'cuire:p2'


def test_conjugation_fr_647():
    assert (
V("cuire").t('ip').pe(2).n('s').realize()   
    ) == 'cuis',\
    'cuire:ip2'


def test_conjugation_fr_648():
    assert (
V("cuire").t('pr').realize()   
    ) == 'cuisant',\
    'cuire:pr'


def test_conjugation_fr_649():
    assert (
V("cuire").t('p').pe(3).n('p').realize()   
    ) == 'cuisent',\
    'cuire:p6'


def test_conjugation_fr_650():
    assert (
V("cuire").t('p').pe(2).n('p').realize()   
    ) == 'cuisez',\
    'cuire:p5'


def test_conjugation_fr_651():
    assert (
V("cuire").t('ip').pe(2).n('p').realize()   
    ) == 'cuisez',\
    'cuire:ip5'


def test_conjugation_fr_652():
    assert (
V("cuire").t('p').pe(1).n('p').realize()   
    ) == 'cuisons',\
    'cuire:p4'


def test_conjugation_fr_653():
    assert (
V("cuire").t('ip').pe(1).n('p').realize()   
    ) == 'cuisons',\
    'cuire:ip4'


def test_conjugation_fr_654():
    assert (
V("cuire").t('p').pe(3).n('s').realize()   
    ) == 'cuit',\
    'cuire:p3'


def test_conjugation_fr_655():
    assert (
V("cuire").t('pp').realize()   
    ) == 'cuit',\
    'cuire:pp'


def test_conjugation_fr_656():
    assert (
V("cuire").t('s').pe(1).n('s').realize()   
    ) == 'cuise',\
    'cuire:s1'


def test_conjugation_fr_657():
    assert (
V("cuire").t('s').pe(2).n('s').realize()   
    ) == 'cuises',\
    'cuire:s2'


def test_conjugation_fr_658():
    assert (
V("cuire").t('s').pe(3).n('s').realize()   
    ) == 'cuise',\
    'cuire:s3'


def test_conjugation_fr_659():
    assert (
V("cuire").t('s').pe(1).n('p').realize()   
    ) == 'cuisions',\
    'cuire:s4'


def test_conjugation_fr_660():
    assert (
V("cuire").t('s').pe(2).n('p').realize()   
    ) == 'cuisiez',\
    'cuire:s5'


def test_conjugation_fr_661():
    assert (
V("cuire").t('s').pe(3).n('p').realize()   
    ) == 'cuisent',\
    'cuire:s6'


def test_conjugation_fr_662():
    assert (
V("débattre").t('p').pe(3).n('s').realize()   
    ) == 'débat',\
    'débattre:p3'


def test_conjugation_fr_663():
    assert (
V("débattre").t('p').pe(1).n('s').realize()   
    ) == 'débats',\
    'débattre:p1'


def test_conjugation_fr_664():
    assert (
V("débattre").t('p').pe(2).n('s').realize()   
    ) == 'débats',\
    'débattre:p2'


def test_conjugation_fr_665():
    assert (
V("débattre").t('ip').pe(2).n('s').realize()   
    ) == 'débats',\
    'débattre:ip2'


def test_conjugation_fr_666():
    assert (
V("débattre").t('pr').realize()   
    ) == 'débattant',\
    'débattre:pr'


def test_conjugation_fr_667():
    assert (
V("débattre").t('p').pe(3).n('p').realize()   
    ) == 'débattent',\
    'débattre:p6'


def test_conjugation_fr_668():
    assert (
V("débattre").t('p').pe(2).n('p').realize()   
    ) == 'débattez',\
    'débattre:p5'


def test_conjugation_fr_669():
    assert (
V("débattre").t('ip').pe(2).n('p').realize()   
    ) == 'débattez',\
    'débattre:ip5'


def test_conjugation_fr_670():
    assert (
V("débattre").t('p').pe(1).n('p').realize()   
    ) == 'débattons',\
    'débattre:p4'


def test_conjugation_fr_671():
    assert (
V("débattre").t('ip').pe(1).n('p').realize()   
    ) == 'débattons',\
    'débattre:ip4'


def test_conjugation_fr_672():
    assert (
V("débattre").t('pp').realize()   
    ) == 'débattu',\
    'débattre:pp'


def test_conjugation_fr_673():
    assert (
V("débattre").t('s').pe(1).n('s').realize()   
    ) == 'débatte',\
    'débattre:s1'


def test_conjugation_fr_674():
    assert (
V("débattre").t('s').pe(2).n('s').realize()   
    ) == 'débattes',\
    'débattre:s2'


def test_conjugation_fr_675():
    assert (
V("débattre").t('s').pe(3).n('s').realize()   
    ) == 'débatte',\
    'débattre:s3'


def test_conjugation_fr_676():
    assert (
V("débattre").t('s').pe(1).n('p').realize()   
    ) == 'débattions',\
    'débattre:s4'


def test_conjugation_fr_677():
    assert (
V("débattre").t('s').pe(2).n('p').realize()   
    ) == 'débattiez',\
    'débattre:s5'


def test_conjugation_fr_678():
    assert (
V("débattre").t('s').pe(3).n('p').realize()   
    ) == 'débattent',\
    'débattre:s6'


def test_conjugation_fr_679():
    assert (
V("découvrir").t('pr').realize()   
    ) == 'découvrant',\
    'découvrir:pr'


def test_conjugation_fr_680():
    assert (
V("découvrir").t('p').pe(1).n('s').realize()   
    ) == 'découvre',\
    'découvrir:p1'


def test_conjugation_fr_681():
    assert (
V("découvrir").t('p').pe(3).n('s').realize()   
    ) == 'découvre',\
    'découvrir:p3'


def test_conjugation_fr_682():
    assert (
V("découvrir").t('ip').pe(2).n('s').realize()   
    ) == 'découvre',\
    'découvrir:ip2'


def test_conjugation_fr_683():
    assert (
V("découvrir").t('p').pe(3).n('p').realize()   
    ) == 'découvrent',\
    'découvrir:p6'


def test_conjugation_fr_684():
    assert (
V("découvrir").t('p').pe(2).n('s').realize()   
    ) == 'découvres',\
    'découvrir:p2'


def test_conjugation_fr_685():
    assert (
V("découvrir").t('p').pe(2).n('p').realize()   
    ) == 'découvrez',\
    'découvrir:p5'


def test_conjugation_fr_686():
    assert (
V("découvrir").t('ip').pe(2).n('p').realize()   
    ) == 'découvrez',\
    'découvrir:ip5'


def test_conjugation_fr_687():
    assert (
V("découvrir").t('p').pe(1).n('p').realize()   
    ) == 'découvrons',\
    'découvrir:p4'


def test_conjugation_fr_688():
    assert (
V("découvrir").t('ip').pe(1).n('p').realize()   
    ) == 'découvrons',\
    'découvrir:ip4'


def test_conjugation_fr_689():
    assert (
V("découvrir").t('pp').realize()   
    ) == 'découvert',\
    'découvrir:pp'


def test_conjugation_fr_690():
    assert (
V("découvrir").t('s').pe(1).n('s').realize()   
    ) == 'découvre',\
    'découvrir:s1'


def test_conjugation_fr_691():
    assert (
V("découvrir").t('s').pe(2).n('s').realize()   
    ) == 'découvres',\
    'découvrir:s2'


def test_conjugation_fr_692():
    assert (
V("découvrir").t('s').pe(3).n('s').realize()   
    ) == 'découvre',\
    'découvrir:s3'


def test_conjugation_fr_693():
    assert (
V("découvrir").t('s').pe(1).n('p').realize()   
    ) == 'découvrions',\
    'découvrir:s4'


def test_conjugation_fr_694():
    assert (
V("découvrir").t('s').pe(2).n('p').realize()   
    ) == 'découvriez',\
    'découvrir:s5'


def test_conjugation_fr_695():
    assert (
V("découvrir").t('s').pe(3).n('p').realize()   
    ) == 'découvrent',\
    'découvrir:s6'


def test_conjugation_fr_696():
    assert (
V("décrire").t('p').pe(1).n('s').realize()   
    ) == 'décris',\
    'décrire:p1'


def test_conjugation_fr_697():
    assert (
V("décrire").t('p').pe(2).n('s').realize()   
    ) == 'décris',\
    'décrire:p2'


def test_conjugation_fr_698():
    assert (
V("décrire").t('ip').pe(2).n('s').realize()   
    ) == 'décris',\
    'décrire:ip2'


def test_conjugation_fr_699():
    assert (
V("décrire").t('p').pe(3).n('s').realize()   
    ) == 'décrit',\
    'décrire:p3'


def test_conjugation_fr_700():
    assert (
V("décrire").t('pr').realize()   
    ) == 'décrivant',\
    'décrire:pr'


def test_conjugation_fr_701():
    assert (
V("décrire").t('p').pe(3).n('p').realize()   
    ) == 'décrivent',\
    'décrire:p6'


def test_conjugation_fr_702():
    assert (
V("décrire").t('p').pe(2).n('p').realize()   
    ) == 'décrivez',\
    'décrire:p5'


def test_conjugation_fr_703():
    assert (
V("décrire").t('ip').pe(2).n('p').realize()   
    ) == 'décrivez',\
    'décrire:ip5'


def test_conjugation_fr_704():
    assert (
V("décrire").t('p').pe(1).n('p').realize()   
    ) == 'décrivons',\
    'décrire:p4'


def test_conjugation_fr_705():
    assert (
V("décrire").t('ip').pe(1).n('p').realize()   
    ) == 'décrivons',\
    'décrire:ip4'


def test_conjugation_fr_706():
    assert (
V("décrire").t('pp').realize()   
    ) == 'décrit',\
    'décrire:pp'


def test_conjugation_fr_707():
    assert (
V("décrire").t('s').pe(1).n('s').realize()   
    ) == 'décrive',\
    'décrire:s1'


def test_conjugation_fr_708():
    assert (
V("décrire").t('s').pe(2).n('s').realize()   
    ) == 'décrives',\
    'décrire:s2'


def test_conjugation_fr_709():
    assert (
V("décrire").t('s').pe(3).n('s').realize()   
    ) == 'décrive',\
    'décrire:s3'


def test_conjugation_fr_710():
    assert (
V("décrire").t('s').pe(1).n('p').realize()   
    ) == 'décrivions',\
    'décrire:s4'


def test_conjugation_fr_711():
    assert (
V("décrire").t('s').pe(2).n('p').realize()   
    ) == 'décriviez',\
    'décrire:s5'


def test_conjugation_fr_712():
    assert (
V("décrire").t('s').pe(3).n('p').realize()   
    ) == 'décrivent',\
    'décrire:s6'


def test_conjugation_fr_713():
    assert (
V("défaire").t('p').pe(1).n('s').realize()   
    ) == 'défais',\
    'défaire:p1'


def test_conjugation_fr_714():
    assert (
V("défaire").t('p').pe(2).n('s').realize()   
    ) == 'défais',\
    'défaire:p2'


def test_conjugation_fr_715():
    assert (
V("défaire").t('ip').pe(2).n('s').realize()   
    ) == 'défais',\
    'défaire:ip2'


def test_conjugation_fr_716():
    assert (
V("défaire").t('pr').realize()   
    ) == 'défaisant',\
    'défaire:pr'


def test_conjugation_fr_717():
    assert (
V("défaire").t('p').pe(1).n('p').realize()   
    ) == 'défaisons',\
    'défaire:p4'


def test_conjugation_fr_718():
    assert (
V("défaire").t('ip').pe(1).n('p').realize()   
    ) == 'défaisons',\
    'défaire:ip4'


def test_conjugation_fr_719():
    assert (
V("défaire").t('p').pe(3).n('s').realize()   
    ) == 'défait',\
    'défaire:p3'


def test_conjugation_fr_720():
    assert (
V("défaire").t('p').pe(2).n('p').realize()   
    ) == 'défaites',\
    'défaire:p5'


def test_conjugation_fr_721():
    assert (
V("défaire").t('ip').pe(2).n('p').realize()   
    ) == 'défaites',\
    'défaire:ip5'


def test_conjugation_fr_722():
    assert (
V("défaire").t('p').pe(3).n('p').realize()   
    ) == 'défont',\
    'défaire:p6'


def test_conjugation_fr_723():
    assert (
V("défaire").t('pp').realize()   
    ) == 'défait',\
    'défaire:pp'


def test_conjugation_fr_724():
    assert (
V("défaire").t('s').pe(1).n('s').realize()   
    ) == 'défasse',\
    'défaire:s1'


def test_conjugation_fr_725():
    assert (
V("défaire").t('s').pe(2).n('s').realize()   
    ) == 'défasses',\
    'défaire:s2'


def test_conjugation_fr_726():
    assert (
V("défaire").t('s').pe(3).n('s').realize()   
    ) == 'défasse',\
    'défaire:s3'


def test_conjugation_fr_727():
    assert (
V("défaire").t('s').pe(1).n('p').realize()   
    ) == 'défassions',\
    'défaire:s4'


def test_conjugation_fr_728():
    assert (
V("défaire").t('s').pe(2).n('p').realize()   
    ) == 'défassiez',\
    'défaire:s5'


def test_conjugation_fr_729():
    assert (
V("défaire").t('s').pe(3).n('p').realize()   
    ) == 'défassent',\
    'défaire:s6'


def test_conjugation_fr_730():
    assert (
V("défendre").t('p').pe(3).n('s').realize()   
    ) == 'défend',\
    'défendre:p3'


def test_conjugation_fr_731():
    assert (
V("défendre").t('pr').realize()   
    ) == 'défendant',\
    'défendre:pr'


def test_conjugation_fr_732():
    assert (
V("défendre").t('p').pe(3).n('p').realize()   
    ) == 'défendent',\
    'défendre:p6'


def test_conjugation_fr_733():
    assert (
V("défendre").t('p').pe(2).n('p').realize()   
    ) == 'défendez',\
    'défendre:p5'


def test_conjugation_fr_734():
    assert (
V("défendre").t('ip').pe(2).n('p').realize()   
    ) == 'défendez',\
    'défendre:ip5'


def test_conjugation_fr_735():
    assert (
V("défendre").t('p').pe(1).n('p').realize()   
    ) == 'défendons',\
    'défendre:p4'


def test_conjugation_fr_736():
    assert (
V("défendre").t('ip').pe(1).n('p').realize()   
    ) == 'défendons',\
    'défendre:ip4'


def test_conjugation_fr_737():
    assert (
V("défendre").t('p').pe(1).n('s').realize()   
    ) == 'défends',\
    'défendre:p1'


def test_conjugation_fr_738():
    assert (
V("défendre").t('p').pe(2).n('s').realize()   
    ) == 'défends',\
    'défendre:p2'


def test_conjugation_fr_739():
    assert (
V("défendre").t('ip').pe(2).n('s').realize()   
    ) == 'défends',\
    'défendre:ip2'


def test_conjugation_fr_740():
    assert (
V("défendre").t('pp').realize()   
    ) == 'défendu',\
    'défendre:pp'


def test_conjugation_fr_741():
    assert (
V("défendre").t('s').pe(1).n('s').realize()   
    ) == 'défende',\
    'défendre:s1'


def test_conjugation_fr_742():
    assert (
V("défendre").t('s').pe(2).n('s').realize()   
    ) == 'défendes',\
    'défendre:s2'


def test_conjugation_fr_743():
    assert (
V("défendre").t('s').pe(3).n('s').realize()   
    ) == 'défende',\
    'défendre:s3'


def test_conjugation_fr_744():
    assert (
V("défendre").t('s').pe(1).n('p').realize()   
    ) == 'défendions',\
    'défendre:s4'


def test_conjugation_fr_745():
    assert (
V("défendre").t('s').pe(2).n('p').realize()   
    ) == 'défendiez',\
    'défendre:s5'


def test_conjugation_fr_746():
    assert (
V("défendre").t('s').pe(3).n('p').realize()   
    ) == 'défendent',\
    'défendre:s6'


def test_conjugation_fr_747():
    assert (
V("dépendre").t('p').pe(3).n('s').realize()   
    ) == 'dépend',\
    'dépendre:p3'


def test_conjugation_fr_748():
    assert (
V("dépendre").t('pr').realize()   
    ) == 'dépendant',\
    'dépendre:pr'


def test_conjugation_fr_749():
    assert (
V("dépendre").t('p').pe(3).n('p').realize()   
    ) == 'dépendent',\
    'dépendre:p6'


def test_conjugation_fr_750():
    assert (
V("dépendre").t('p').pe(2).n('p').realize()   
    ) == 'dépendez',\
    'dépendre:p5'


def test_conjugation_fr_751():
    assert (
V("dépendre").t('ip').pe(2).n('p').realize()   
    ) == 'dépendez',\
    'dépendre:ip5'


def test_conjugation_fr_752():
    assert (
V("dépendre").t('p').pe(1).n('p').realize()   
    ) == 'dépendons',\
    'dépendre:p4'


def test_conjugation_fr_753():
    assert (
V("dépendre").t('ip').pe(1).n('p').realize()   
    ) == 'dépendons',\
    'dépendre:ip4'


def test_conjugation_fr_754():
    assert (
V("dépendre").t('p').pe(1).n('s').realize()   
    ) == 'dépends',\
    'dépendre:p1'


def test_conjugation_fr_755():
    assert (
V("dépendre").t('p').pe(2).n('s').realize()   
    ) == 'dépends',\
    'dépendre:p2'


def test_conjugation_fr_756():
    assert (
V("dépendre").t('ip').pe(2).n('s').realize()   
    ) == 'dépends',\
    'dépendre:ip2'


def test_conjugation_fr_757():
    assert (
V("dépendre").t('pp').realize()   
    ) == 'dépendu',\
    'dépendre:pp'


def test_conjugation_fr_758():
    assert (
V("dépendre").t('s').pe(1).n('s').realize()   
    ) == 'dépende',\
    'dépendre:s1'


def test_conjugation_fr_759():
    assert (
V("dépendre").t('s').pe(2).n('s').realize()   
    ) == 'dépendes',\
    'dépendre:s2'


def test_conjugation_fr_760():
    assert (
V("dépendre").t('s').pe(3).n('s').realize()   
    ) == 'dépende',\
    'dépendre:s3'


def test_conjugation_fr_761():
    assert (
V("dépendre").t('s').pe(1).n('p').realize()   
    ) == 'dépendions',\
    'dépendre:s4'


def test_conjugation_fr_762():
    assert (
V("dépendre").t('s').pe(2).n('p').realize()   
    ) == 'dépendiez',\
    'dépendre:s5'


def test_conjugation_fr_763():
    assert (
V("dépendre").t('s').pe(3).n('p').realize()   
    ) == 'dépendent',\
    'dépendre:s6'


def test_conjugation_fr_764():
    assert (
V("déplaire").t('p').pe(1).n('s').realize()   
    ) == 'déplais',\
    'déplaire:p1'


def test_conjugation_fr_765():
    assert (
V("déplaire").t('p').pe(2).n('s').realize()   
    ) == 'déplais',\
    'déplaire:p2'


def test_conjugation_fr_766():
    assert (
V("déplaire").t('ip').pe(2).n('s').realize()   
    ) == 'déplais',\
    'déplaire:ip2'


def test_conjugation_fr_767():
    assert (
V("déplaire").t('pr').realize()   
    ) == 'déplaisant',\
    'déplaire:pr'


def test_conjugation_fr_768():
    assert (
V("déplaire").t('p').pe(3).n('p').realize()   
    ) == 'déplaisent',\
    'déplaire:p6'


def test_conjugation_fr_769():
    assert (
V("déplaire").t('p').pe(2).n('p').realize()   
    ) == 'déplaisez',\
    'déplaire:p5'


def test_conjugation_fr_770():
    assert (
V("déplaire").t('ip').pe(2).n('p').realize()   
    ) == 'déplaisez',\
    'déplaire:ip5'


def test_conjugation_fr_771():
    assert (
V("déplaire").t('p').pe(1).n('p').realize()   
    ) == 'déplaisons',\
    'déplaire:p4'


def test_conjugation_fr_772():
    assert (
V("déplaire").t('ip').pe(1).n('p').realize()   
    ) == 'déplaisons',\
    'déplaire:ip4'


def test_conjugation_fr_773():
    assert (
V("déplaire").t('p').pe(3).n('s').realize()   
    ) == 'déplaît',\
    'déplaire:p3'


def test_conjugation_fr_774():
    assert (
V("déplaire").t('s').pe(1).n('s').realize()   
    ) == 'déplaise',\
    'déplaire:s1'


def test_conjugation_fr_775():
    assert (
V("déplaire").t('s').pe(2).n('s').realize()   
    ) == 'déplaises',\
    'déplaire:s2'


def test_conjugation_fr_776():
    assert (
V("déplaire").t('s').pe(3).n('s').realize()   
    ) == 'déplaise',\
    'déplaire:s3'


def test_conjugation_fr_777():
    assert (
V("déplaire").t('s').pe(1).n('p').realize()   
    ) == 'déplaisions',\
    'déplaire:s4'


def test_conjugation_fr_778():
    assert (
V("déplaire").t('s').pe(2).n('p').realize()   
    ) == 'déplaisiez',\
    'déplaire:s5'


def test_conjugation_fr_779():
    assert (
V("déplaire").t('s').pe(3).n('p').realize()   
    ) == 'déplaisent',\
    'déplaire:s6'


def test_conjugation_fr_780():
    assert (
V("descendre").t('p').pe(3).n('s').realize()   
    ) == 'descend',\
    'descendre:p3'


def test_conjugation_fr_781():
    assert (
V("descendre").t('pr').realize()   
    ) == 'descendant',\
    'descendre:pr'


def test_conjugation_fr_782():
    assert (
V("descendre").t('p').pe(3).n('p').realize()   
    ) == 'descendent',\
    'descendre:p6'


def test_conjugation_fr_783():
    assert (
V("descendre").t('p').pe(2).n('p').realize()   
    ) == 'descendez',\
    'descendre:p5'


def test_conjugation_fr_784():
    assert (
V("descendre").t('ip').pe(2).n('p').realize()   
    ) == 'descendez',\
    'descendre:ip5'


def test_conjugation_fr_785():
    assert (
V("descendre").t('p').pe(1).n('p').realize()   
    ) == 'descendons',\
    'descendre:p4'


def test_conjugation_fr_786():
    assert (
V("descendre").t('ip').pe(1).n('p').realize()   
    ) == 'descendons',\
    'descendre:ip4'


def test_conjugation_fr_787():
    assert (
V("descendre").t('p').pe(1).n('s').realize()   
    ) == 'descends',\
    'descendre:p1'


def test_conjugation_fr_788():
    assert (
V("descendre").t('p').pe(2).n('s').realize()   
    ) == 'descends',\
    'descendre:p2'


def test_conjugation_fr_789():
    assert (
V("descendre").t('ip').pe(2).n('s').realize()   
    ) == 'descends',\
    'descendre:ip2'


def test_conjugation_fr_790():
    assert (
V("descendre").t('pp').realize()   
    ) == 'descendu',\
    'descendre:pp'


def test_conjugation_fr_791():
    assert (
V("descendre").t('s').pe(1).n('s').realize()   
    ) == 'descende',\
    'descendre:s1'


def test_conjugation_fr_792():
    assert (
V("descendre").t('s').pe(2).n('s').realize()   
    ) == 'descendes',\
    'descendre:s2'


def test_conjugation_fr_793():
    assert (
V("descendre").t('s').pe(3).n('s').realize()   
    ) == 'descende',\
    'descendre:s3'


def test_conjugation_fr_794():
    assert (
V("descendre").t('s').pe(1).n('p').realize()   
    ) == 'descendions',\
    'descendre:s4'


def test_conjugation_fr_795():
    assert (
V("descendre").t('s').pe(2).n('p').realize()   
    ) == 'descendiez',\
    'descendre:s5'


def test_conjugation_fr_796():
    assert (
V("descendre").t('s').pe(3).n('p').realize()   
    ) == 'descendent',\
    'descendre:s6'


def test_conjugation_fr_797():
    assert (
V("détruire").t('p').pe(1).n('s').realize()   
    ) == 'détruis',\
    'détruire:p1'


def test_conjugation_fr_798():
    assert (
V("détruire").t('p').pe(2).n('s').realize()   
    ) == 'détruis',\
    'détruire:p2'


def test_conjugation_fr_799():
    assert (
V("détruire").t('ip').pe(2).n('s').realize()   
    ) == 'détruis',\
    'détruire:ip2'


def test_conjugation_fr_800():
    assert (
V("détruire").t('pr').realize()   
    ) == 'détruisant',\
    'détruire:pr'


def test_conjugation_fr_801():
    assert (
V("détruire").t('p').pe(3).n('p').realize()   
    ) == 'détruisent',\
    'détruire:p6'


def test_conjugation_fr_802():
    assert (
V("détruire").t('p').pe(2).n('p').realize()   
    ) == 'détruisez',\
    'détruire:p5'


def test_conjugation_fr_803():
    assert (
V("détruire").t('ip').pe(2).n('p').realize()   
    ) == 'détruisez',\
    'détruire:ip5'


def test_conjugation_fr_804():
    assert (
V("détruire").t('p').pe(1).n('p').realize()   
    ) == 'détruisons',\
    'détruire:p4'


def test_conjugation_fr_805():
    assert (
V("détruire").t('ip').pe(1).n('p').realize()   
    ) == 'détruisons',\
    'détruire:ip4'


def test_conjugation_fr_806():
    assert (
V("détruire").t('p').pe(3).n('s').realize()   
    ) == 'détruit',\
    'détruire:p3'


def test_conjugation_fr_807():
    assert (
V("détruire").t('pp').realize()   
    ) == 'détruit',\
    'détruire:pp'


def test_conjugation_fr_808():
    assert (
V("détruire").t('s').pe(1).n('s').realize()   
    ) == 'détruise',\
    'détruire:s1'


def test_conjugation_fr_809():
    assert (
V("détruire").t('s').pe(2).n('s').realize()   
    ) == 'détruises',\
    'détruire:s2'


def test_conjugation_fr_810():
    assert (
V("détruire").t('s').pe(3).n('s').realize()   
    ) == 'détruise',\
    'détruire:s3'


def test_conjugation_fr_811():
    assert (
V("détruire").t('s').pe(1).n('p').realize()   
    ) == 'détruisions',\
    'détruire:s4'


def test_conjugation_fr_812():
    assert (
V("détruire").t('s').pe(2).n('p').realize()   
    ) == 'détruisiez',\
    'détruire:s5'


def test_conjugation_fr_813():
    assert (
V("détruire").t('s').pe(3).n('p').realize()   
    ) == 'détruisent',\
    'détruire:s6'


def test_conjugation_fr_814():
    assert (
V("devenir").t('pr').realize()   
    ) == 'devenant',\
    'devenir:pr'


def test_conjugation_fr_815():
    assert (
V("devenir").t('p').pe(2).n('p').realize()   
    ) == 'devenez',\
    'devenir:p5'


def test_conjugation_fr_816():
    assert (
V("devenir").t('ip').pe(2).n('p').realize()   
    ) == 'devenez',\
    'devenir:ip5'


def test_conjugation_fr_817():
    assert (
V("devenir").t('p').pe(1).n('p').realize()   
    ) == 'devenons',\
    'devenir:p4'


def test_conjugation_fr_818():
    assert (
V("devenir").t('ip').pe(1).n('p').realize()   
    ) == 'devenons',\
    'devenir:ip4'


def test_conjugation_fr_819():
    assert (
V("devenir").t('p').pe(3).n('p').realize()   
    ) == 'deviennent',\
    'devenir:p6'


def test_conjugation_fr_820():
    assert (
V("devenir").t('p').pe(1).n('s').realize()   
    ) == 'deviens',\
    'devenir:p1'


def test_conjugation_fr_821():
    assert (
V("devenir").t('p').pe(2).n('s').realize()   
    ) == 'deviens',\
    'devenir:p2'


def test_conjugation_fr_822():
    assert (
V("devenir").t('ip').pe(2).n('s').realize()   
    ) == 'deviens',\
    'devenir:ip2'


def test_conjugation_fr_823():
    assert (
V("devenir").t('p').pe(3).n('s').realize()   
    ) == 'devient',\
    'devenir:p3'


def test_conjugation_fr_824():
    assert (
V("devenir").t('pp').realize()   
    ) == 'devenu',\
    'devenir:pp'


def test_conjugation_fr_825():
    assert (
V("devenir").t('s').pe(1).n('s').realize()   
    ) == 'devienne',\
    'devenir:s1'


def test_conjugation_fr_826():
    assert (
V("devenir").t('s').pe(2).n('s').realize()   
    ) == 'deviennes',\
    'devenir:s2'


def test_conjugation_fr_827():
    assert (
V("devenir").t('s').pe(3).n('s').realize()   
    ) == 'devienne',\
    'devenir:s3'


def test_conjugation_fr_828():
    assert (
V("devenir").t('s').pe(1).n('p').realize()   
    ) == 'devenions',\
    'devenir:s4'


def test_conjugation_fr_829():
    assert (
V("devenir").t('s').pe(2).n('p').realize()   
    ) == 'deveniez',\
    'devenir:s5'


def test_conjugation_fr_830():
    assert (
V("devenir").t('s').pe(3).n('p').realize()   
    ) == 'deviennent',\
    'devenir:s6'


def test_conjugation_fr_831():
    assert (
V("devoir").t('pr').realize()   
    ) == 'devant',\
    'devoir:pr'


def test_conjugation_fr_832():
    assert (
V("devoir").t('p').pe(2).n('p').realize()   
    ) == 'devez',\
    'devoir:p5'


def test_conjugation_fr_833():
    assert (
V("devoir").t('ip').pe(2).n('p').realize()   
    ) == 'devez',\
    'devoir:ip5'


def test_conjugation_fr_834():
    assert (
V("devoir").t('p').pe(1).n('p').realize()   
    ) == 'devons',\
    'devoir:p4'


def test_conjugation_fr_835():
    assert (
V("devoir").t('ip').pe(1).n('p').realize()   
    ) == 'devons',\
    'devoir:ip4'


def test_conjugation_fr_836():
    assert (
V("devoir").t('p').pe(1).n('s').realize()   
    ) == 'dois',\
    'devoir:p1'


def test_conjugation_fr_837():
    assert (
V("devoir").t('p').pe(2).n('s').realize()   
    ) == 'dois',\
    'devoir:p2'


def test_conjugation_fr_838():
    assert (
V("devoir").t('ip').pe(2).n('s').realize()   
    ) == 'dois',\
    'devoir:ip2'


def test_conjugation_fr_839():
    assert (
V("devoir").t('p').pe(3).n('s').realize()   
    ) == 'doit',\
    'devoir:p3'


def test_conjugation_fr_840():
    assert (
V("devoir").t('p').pe(3).n('p').realize()   
    ) == 'doivent',\
    'devoir:p6'


def test_conjugation_fr_841():
    assert (
V("devoir").t('pp').realize()   
    ) == 'dû',\
    'devoir:pp'


def test_conjugation_fr_842():
    assert (
V("devoir").t('s').pe(1).n('s').realize()   
    ) == 'doive',\
    'devoir:s1'


def test_conjugation_fr_843():
    assert (
V("devoir").t('s').pe(2).n('s').realize()   
    ) == 'doives',\
    'devoir:s2'


def test_conjugation_fr_844():
    assert (
V("devoir").t('s').pe(3).n('s').realize()   
    ) == 'doive',\
    'devoir:s3'


def test_conjugation_fr_845():
    assert (
V("devoir").t('s').pe(1).n('p').realize()   
    ) == 'devions',\
    'devoir:s4'


def test_conjugation_fr_846():
    assert (
V("devoir").t('s').pe(2).n('p').realize()   
    ) == 'deviez',\
    'devoir:s5'


def test_conjugation_fr_847():
    assert (
V("devoir").t('s').pe(3).n('p').realize()   
    ) == 'doivent',\
    'devoir:s6'


def test_conjugation_fr_848():
    assert (
V("dire").t('p').pe(1).n('s').realize()   
    ) == 'dis',\
    'dire:p1'


def test_conjugation_fr_849():
    assert (
V("dire").t('p').pe(2).n('s').realize()   
    ) == 'dis',\
    'dire:p2'


def test_conjugation_fr_850():
    assert (
V("dire").t('ip').pe(2).n('s').realize()   
    ) == 'dis',\
    'dire:ip2'


def test_conjugation_fr_851():
    assert (
V("dire").t('pr').realize()   
    ) == 'disant',\
    'dire:pr'


def test_conjugation_fr_852():
    assert (
V("dire").t('p').pe(3).n('p').realize()   
    ) == 'disent',\
    'dire:p6'


def test_conjugation_fr_853():
    assert (
V("dire").t('p').pe(1).n('p').realize()   
    ) == 'disons',\
    'dire:p4'


def test_conjugation_fr_854():
    assert (
V("dire").t('ip').pe(1).n('p').realize()   
    ) == 'disons',\
    'dire:ip4'


def test_conjugation_fr_855():
    assert (
V("dire").t('p').pe(3).n('s').realize()   
    ) == 'dit',\
    'dire:p3'


def test_conjugation_fr_856():
    assert (
V("dire").t('p').pe(2).n('p').realize()   
    ) == 'dites',\
    'dire:p5'


def test_conjugation_fr_857():
    assert (
V("dire").t('ip').pe(2).n('p').realize()   
    ) == 'dites',\
    'dire:ip5'


def test_conjugation_fr_858():
    assert (
V("dire").t('pp').realize()   
    ) == 'dit',\
    'dire:pp'


def test_conjugation_fr_859():
    assert (
V("dire").t('s').pe(1).n('s').realize()   
    ) == 'dise',\
    'dire:s1'


def test_conjugation_fr_860():
    assert (
V("dire").t('s').pe(2).n('s').realize()   
    ) == 'dises',\
    'dire:s2'


def test_conjugation_fr_861():
    assert (
V("dire").t('s').pe(3).n('s').realize()   
    ) == 'dise',\
    'dire:s3'


def test_conjugation_fr_862():
    assert (
V("dire").t('s').pe(1).n('p').realize()   
    ) == 'disions',\
    'dire:s4'


def test_conjugation_fr_863():
    assert (
V("dire").t('s').pe(2).n('p').realize()   
    ) == 'disiez',\
    'dire:s5'


def test_conjugation_fr_864():
    assert (
V("dire").t('s').pe(3).n('p').realize()   
    ) == 'disent',\
    'dire:s6'


def test_conjugation_fr_865():
    assert (
V("disparaître").t('p').pe(1).n('s').realize()   
    ) == 'disparais',\
    'disparaître:p1'


def test_conjugation_fr_866():
    assert (
V("disparaître").t('p').pe(2).n('s').realize()   
    ) == 'disparais',\
    'disparaître:p2'


def test_conjugation_fr_867():
    assert (
V("disparaître").t('ip').pe(2).n('s').realize()   
    ) == 'disparais',\
    'disparaître:ip2'


def test_conjugation_fr_868():
    assert (
V("disparaître").t('pr').realize()   
    ) == 'disparaissant',\
    'disparaître:pr'


def test_conjugation_fr_869():
    assert (
V("disparaître").t('p').pe(3).n('p').realize()   
    ) == 'disparaissent',\
    'disparaître:p6'


def test_conjugation_fr_870():
    assert (
V("disparaître").t('p').pe(2).n('p').realize()   
    ) == 'disparaissez',\
    'disparaître:p5'


def test_conjugation_fr_871():
    assert (
V("disparaître").t('ip').pe(2).n('p').realize()   
    ) == 'disparaissez',\
    'disparaître:ip5'


def test_conjugation_fr_872():
    assert (
V("disparaître").t('p').pe(1).n('p').realize()   
    ) == 'disparaissons',\
    'disparaître:p4'


def test_conjugation_fr_873():
    assert (
V("disparaître").t('ip').pe(1).n('p').realize()   
    ) == 'disparaissons',\
    'disparaître:ip4'


def test_conjugation_fr_874():
    assert (
V("disparaître").t('p').pe(3).n('s').realize()   
    ) == 'disparaît',\
    'disparaître:p3'


def test_conjugation_fr_875():
    assert (
V("disparaître").t('pp').realize()   
    ) == 'disparu',\
    'disparaître:pp'


def test_conjugation_fr_876():
    assert (
V("disparaître").t('s').pe(1).n('s').realize()   
    ) == 'disparaisse',\
    'disparaître:s1'


def test_conjugation_fr_877():
    assert (
V("disparaître").t('s').pe(2).n('s').realize()   
    ) == 'disparaisses',\
    'disparaître:s2'


def test_conjugation_fr_878():
    assert (
V("disparaître").t('s').pe(3).n('s').realize()   
    ) == 'disparaisse',\
    'disparaître:s3'


def test_conjugation_fr_879():
    assert (
V("disparaître").t('s').pe(1).n('p').realize()   
    ) == 'disparaissions',\
    'disparaître:s4'


def test_conjugation_fr_880():
    assert (
V("disparaître").t('s').pe(2).n('p').realize()   
    ) == 'disparaissiez',\
    'disparaître:s5'


def test_conjugation_fr_881():
    assert (
V("disparaître").t('s').pe(3).n('p').realize()   
    ) == 'disparaissent',\
    'disparaître:s6'


def test_conjugation_fr_882():
    assert (
V("distraire").t('p').pe(3).n('p').realize()   
    ) == 'distraient',\
    'distraire:p6'


def test_conjugation_fr_883():
    assert (
V("distraire").t('p').pe(1).n('s').realize()   
    ) == 'distrais',\
    'distraire:p1'


def test_conjugation_fr_884():
    assert (
V("distraire").t('p').pe(2).n('s').realize()   
    ) == 'distrais',\
    'distraire:p2'


def test_conjugation_fr_885():
    assert (
V("distraire").t('ip').pe(2).n('s').realize()   
    ) == 'distrais',\
    'distraire:ip2'


def test_conjugation_fr_886():
    assert (
V("distraire").t('p').pe(3).n('s').realize()   
    ) == 'distrait',\
    'distraire:p3'


def test_conjugation_fr_887():
    assert (
V("distraire").t('pr').realize()   
    ) == 'distrayant',\
    'distraire:pr'


def test_conjugation_fr_888():
    assert (
V("distraire").t('p').pe(2).n('p').realize()   
    ) == 'distrayez',\
    'distraire:p5'


def test_conjugation_fr_889():
    assert (
V("distraire").t('ip').pe(2).n('p').realize()   
    ) == 'distrayez',\
    'distraire:ip5'


def test_conjugation_fr_890():
    assert (
V("distraire").t('p').pe(1).n('p').realize()   
    ) == 'distrayons',\
    'distraire:p4'


def test_conjugation_fr_891():
    assert (
V("distraire").t('ip').pe(1).n('p').realize()   
    ) == 'distrayons',\
    'distraire:ip4'


def test_conjugation_fr_892():
    assert (
V("distraire").t('pp').realize()   
    ) == 'distrait',\
    'distraire:pp'


def test_conjugation_fr_893():
    assert (
V("distraire").t('s').pe(1).n('s').realize()   
    ) == 'distraie',\
    'distraire:s1'


def test_conjugation_fr_894():
    assert (
V("distraire").t('s').pe(2).n('s').realize()   
    ) == 'distraies',\
    'distraire:s2'


def test_conjugation_fr_895():
    assert (
V("distraire").t('s').pe(3).n('s').realize()   
    ) == 'distraie',\
    'distraire:s3'


def test_conjugation_fr_896():
    assert (
V("distraire").t('s').pe(1).n('p').realize()   
    ) == 'distrayions',\
    'distraire:s4'


def test_conjugation_fr_897():
    assert (
V("distraire").t('s').pe(2).n('p').realize()   
    ) == 'distrayiez',\
    'distraire:s5'


def test_conjugation_fr_898():
    assert (
V("distraire").t('s').pe(3).n('p').realize()   
    ) == 'distraient',\
    'distraire:s6'


def test_conjugation_fr_899():
    assert (
V("dormir").t('pr').realize()   
    ) == 'dormant',\
    'dormir:pr'


def test_conjugation_fr_900():
    assert (
V("dormir").t('p').pe(3).n('p').realize()   
    ) == 'dorment',\
    'dormir:p6'


def test_conjugation_fr_901():
    assert (
V("dormir").t('p').pe(2).n('p').realize()   
    ) == 'dormez',\
    'dormir:p5'


def test_conjugation_fr_902():
    assert (
V("dormir").t('ip').pe(2).n('p').realize()   
    ) == 'dormez',\
    'dormir:ip5'


def test_conjugation_fr_903():
    assert (
V("dormir").t('p').pe(1).n('p').realize()   
    ) == 'dormons',\
    'dormir:p4'


def test_conjugation_fr_904():
    assert (
V("dormir").t('ip').pe(1).n('p').realize()   
    ) == 'dormons',\
    'dormir:ip4'


def test_conjugation_fr_905():
    assert (
V("dormir").t('p').pe(1).n('s').realize()   
    ) == 'dors',\
    'dormir:p1'


def test_conjugation_fr_906():
    assert (
V("dormir").t('p').pe(2).n('s').realize()   
    ) == 'dors',\
    'dormir:p2'


def test_conjugation_fr_907():
    assert (
V("dormir").t('ip').pe(2).n('s').realize()   
    ) == 'dors',\
    'dormir:ip2'


def test_conjugation_fr_908():
    assert (
V("dormir").t('p').pe(3).n('s').realize()   
    ) == 'dort',\
    'dormir:p3'


def test_conjugation_fr_909():
    assert (
V("dormir").t('pp').realize()   
    ) == 'dormi',\
    'dormir:pp'


def test_conjugation_fr_910():
    assert (
V("dormir").t('s').pe(1).n('s').realize()   
    ) == 'dorme',\
    'dormir:s1'


def test_conjugation_fr_911():
    assert (
V("dormir").t('s').pe(2).n('s').realize()   
    ) == 'dormes',\
    'dormir:s2'


def test_conjugation_fr_912():
    assert (
V("dormir").t('s').pe(3).n('s').realize()   
    ) == 'dorme',\
    'dormir:s3'


def test_conjugation_fr_913():
    assert (
V("dormir").t('s').pe(1).n('p').realize()   
    ) == 'dormions',\
    'dormir:s4'


def test_conjugation_fr_914():
    assert (
V("dormir").t('s').pe(2).n('p').realize()   
    ) == 'dormiez',\
    'dormir:s5'


def test_conjugation_fr_915():
    assert (
V("dormir").t('s').pe(3).n('p').realize()   
    ) == 'dorment',\
    'dormir:s6'


def test_conjugation_fr_916():
    assert (
V("éclore").t('pr').realize()   
    ) == 'éclosant',\
    'éclore:pr'


def test_conjugation_fr_917():
    assert (
V("éclore").t('p').pe(3).n('p').realize()   
    ) == 'éclosent',\
    'éclore:p6'


def test_conjugation_fr_918():
    assert (
V("éclore").t('p').pe(3).n('s').realize()   
    ) == 'éclôt',\
    'éclore:p3'


def test_conjugation_fr_919():
    assert (
V("éclore").t('pp').realize()   
    ) == 'éclos',\
    'éclore:pp'


def test_conjugation_fr_920():
    assert (
V("éclore").t('s').pe(1).n('s').realize()   
    ) == 'éclose',\
    'éclore:s1'


def test_conjugation_fr_921():
    assert (
V("éclore").t('s').pe(2).n('s').realize()   
    ) == 'écloses',\
    'éclore:s2'


def test_conjugation_fr_922():
    assert (
V("éclore").t('s').pe(3).n('s').realize()   
    ) == 'éclose',\
    'éclore:s3'


def test_conjugation_fr_923():
    assert (
V("éclore").t('s').pe(1).n('p').realize()   
    ) == 'éclosions',\
    'éclore:s4'


def test_conjugation_fr_924():
    assert (
V("éclore").t('s').pe(2).n('p').realize()   
    ) == 'éclosiez',\
    'éclore:s5'


def test_conjugation_fr_925():
    assert (
V("éclore").t('s').pe(3).n('p').realize()   
    ) == 'éclosent',\
    'éclore:s6'


def test_conjugation_fr_926():
    assert (
V("écrire").t('p').pe(1).n('s').realize()   
    ) == 'écris',\
    'écrire:p1'


def test_conjugation_fr_927():
    assert (
V("écrire").t('p').pe(2).n('s').realize()   
    ) == 'écris',\
    'écrire:p2'


def test_conjugation_fr_928():
    assert (
V("écrire").t('ip').pe(2).n('s').realize()   
    ) == 'écris',\
    'écrire:ip2'


def test_conjugation_fr_929():
    assert (
V("écrire").t('p').pe(3).n('s').realize()   
    ) == 'écrit',\
    'écrire:p3'


def test_conjugation_fr_930():
    assert (
V("écrire").t('pr').realize()   
    ) == 'écrivant',\
    'écrire:pr'


def test_conjugation_fr_931():
    assert (
V("écrire").t('p').pe(3).n('p').realize()   
    ) == 'écrivent',\
    'écrire:p6'


def test_conjugation_fr_932():
    assert (
V("écrire").t('p').pe(2).n('p').realize()   
    ) == 'écrivez',\
    'écrire:p5'


def test_conjugation_fr_933():
    assert (
V("écrire").t('ip').pe(2).n('p').realize()   
    ) == 'écrivez',\
    'écrire:ip5'


def test_conjugation_fr_934():
    assert (
V("écrire").t('p').pe(1).n('p').realize()   
    ) == 'écrivons',\
    'écrire:p4'


def test_conjugation_fr_935():
    assert (
V("écrire").t('ip').pe(1).n('p').realize()   
    ) == 'écrivons',\
    'écrire:ip4'


def test_conjugation_fr_936():
    assert (
V("écrire").t('pp').realize()   
    ) == 'écrit',\
    'écrire:pp'


def test_conjugation_fr_937():
    assert (
V("écrire").t('s').pe(1).n('s').realize()   
    ) == 'écrive',\
    'écrire:s1'


def test_conjugation_fr_938():
    assert (
V("écrire").t('s').pe(2).n('s').realize()   
    ) == 'écrives',\
    'écrire:s2'


def test_conjugation_fr_939():
    assert (
V("écrire").t('s').pe(3).n('s').realize()   
    ) == 'écrive',\
    'écrire:s3'


def test_conjugation_fr_940():
    assert (
V("écrire").t('s').pe(1).n('p').realize()   
    ) == 'écrivions',\
    'écrire:s4'


def test_conjugation_fr_941():
    assert (
V("écrire").t('s').pe(2).n('p').realize()   
    ) == 'écriviez',\
    'écrire:s5'


def test_conjugation_fr_942():
    assert (
V("écrire").t('s').pe(3).n('p').realize()   
    ) == 'écrivent',\
    'écrire:s6'


def test_conjugation_fr_943():
    assert (
V("émouvoir").t('p').pe(1).n('s').realize()   
    ) == 'émeus',\
    'émouvoir:p1'


def test_conjugation_fr_944():
    assert (
V("émouvoir").t('p').pe(2).n('s').realize()   
    ) == 'émeus',\
    'émouvoir:p2'


def test_conjugation_fr_945():
    assert (
V("émouvoir").t('ip').pe(2).n('s').realize()   
    ) == 'émeus',\
    'émouvoir:ip2'


def test_conjugation_fr_946():
    assert (
V("émouvoir").t('p').pe(3).n('s').realize()   
    ) == 'émeut',\
    'émouvoir:p3'


def test_conjugation_fr_947():
    assert (
V("émouvoir").t('p').pe(3).n('p').realize()   
    ) == 'émeuvent',\
    'émouvoir:p6'


def test_conjugation_fr_948():
    assert (
V("émouvoir").t('pr').realize()   
    ) == 'émouvant',\
    'émouvoir:pr'


def test_conjugation_fr_949():
    assert (
V("émouvoir").t('p').pe(2).n('p').realize()   
    ) == 'émouvez',\
    'émouvoir:p5'


def test_conjugation_fr_950():
    assert (
V("émouvoir").t('ip').pe(2).n('p').realize()   
    ) == 'émouvez',\
    'émouvoir:ip5'


def test_conjugation_fr_951():
    assert (
V("émouvoir").t('p').pe(1).n('p').realize()   
    ) == 'émouvons',\
    'émouvoir:p4'


def test_conjugation_fr_952():
    assert (
V("émouvoir").t('ip').pe(1).n('p').realize()   
    ) == 'émouvons',\
    'émouvoir:ip4'


def test_conjugation_fr_953():
    assert (
V("émouvoir").t('pp').realize()   
    ) == 'ému',\
    'émouvoir:pp'


def test_conjugation_fr_954():
    assert (
V("émouvoir").t('s').pe(1).n('s').realize()   
    ) == 'émeuve',\
    'émouvoir:s1'


def test_conjugation_fr_955():
    assert (
V("émouvoir").t('s').pe(2).n('s').realize()   
    ) == 'émeuves',\
    'émouvoir:s2'


def test_conjugation_fr_956():
    assert (
V("émouvoir").t('s').pe(3).n('s').realize()   
    ) == 'émeuve',\
    'émouvoir:s3'


def test_conjugation_fr_957():
    assert (
V("émouvoir").t('s').pe(1).n('p').realize()   
    ) == 'émouvions',\
    'émouvoir:s4'


def test_conjugation_fr_958():
    assert (
V("émouvoir").t('s').pe(2).n('p').realize()   
    ) == 'émouviez',\
    'émouvoir:s5'


def test_conjugation_fr_959():
    assert (
V("émouvoir").t('s').pe(3).n('p').realize()   
    ) == 'émeuvent',\
    'émouvoir:s6'


def test_conjugation_fr_960():
    assert (
V("encourir").t('p').pe(1).n('s').realize()   
    ) == 'encours',\
    'encourir:p1'


def test_conjugation_fr_961():
    assert (
V("encourir").t('p').pe(2).n('s').realize()   
    ) == 'encours',\
    'encourir:p2'


def test_conjugation_fr_962():
    assert (
V("encourir").t('p').pe(3).n('s').realize()   
    ) == 'encourt',\
    'encourir:p3'


def test_conjugation_fr_963():
    assert (
V("encourir").t('p').pe(1).n('p').realize()   
    ) == 'encourons',\
    'encourir:p4'


def test_conjugation_fr_964():
    assert (
V("encourir").t('p').pe(2).n('p').realize()   
    ) == 'encourez',\
    'encourir:p5'


def test_conjugation_fr_965():
    assert (
V("encourir").t('p').pe(3).n('p').realize()   
    ) == 'encourent',\
    'encourir:p6'


def test_conjugation_fr_966():
    assert (
V("encourir").t('ip').pe(2).n('s').realize()   
    ) == 'encours',\
    'encourir:ip2'


def test_conjugation_fr_967():
    assert (
V("encourir").t('ip').pe(1).n('p').realize()   
    ) == 'encourons',\
    'encourir:ip4'


def test_conjugation_fr_968():
    assert (
V("encourir").t('ip').pe(2).n('p').realize()   
    ) == 'encourez',\
    'encourir:ip5'


def test_conjugation_fr_969():
    assert (
V("encourir").t('pr').realize()   
    ) == 'encourant',\
    'encourir:pr'


def test_conjugation_fr_970():
    assert (
V("encourir").t('pp').realize()   
    ) == 'encouru',\
    'encourir:pp'


def test_conjugation_fr_971():
    assert (
V("encourir").t('s').pe(1).n('s').realize()   
    ) == 'encoure',\
    'encourir:s1'


def test_conjugation_fr_972():
    assert (
V("encourir").t('s').pe(2).n('s').realize()   
    ) == 'encoures',\
    'encourir:s2'


def test_conjugation_fr_973():
    assert (
V("encourir").t('s').pe(3).n('s').realize()   
    ) == 'encoure',\
    'encourir:s3'


def test_conjugation_fr_974():
    assert (
V("encourir").t('s').pe(1).n('p').realize()   
    ) == 'encourions',\
    'encourir:s4'


def test_conjugation_fr_975():
    assert (
V("encourir").t('s').pe(2).n('p').realize()   
    ) == 'encouriez',\
    'encourir:s5'


def test_conjugation_fr_976():
    assert (
V("encourir").t('s').pe(3).n('p').realize()   
    ) == 'encourent',\
    'encourir:s6'


def test_conjugation_fr_977():
    assert (
V("endormir").t('p').pe(1).n('s').realize()   
    ) == 'endors',\
    'endormir:p1'


def test_conjugation_fr_978():
    assert (
V("endormir").t('p').pe(2).n('s').realize()   
    ) == 'endors',\
    'endormir:p2'


def test_conjugation_fr_979():
    assert (
V("endormir").t('p').pe(3).n('s').realize()   
    ) == 'endort',\
    'endormir:p3'


def test_conjugation_fr_980():
    assert (
V("endormir").t('p').pe(1).n('p').realize()   
    ) == 'endormons',\
    'endormir:p4'


def test_conjugation_fr_981():
    assert (
V("endormir").t('p').pe(2).n('p').realize()   
    ) == 'endormez',\
    'endormir:p5'


def test_conjugation_fr_982():
    assert (
V("endormir").t('p').pe(3).n('p').realize()   
    ) == 'endorment',\
    'endormir:p6'


def test_conjugation_fr_983():
    assert (
V("endormir").t('ip').pe(2).n('s').realize()   
    ) == 'endors',\
    'endormir:ip2'


def test_conjugation_fr_984():
    assert (
V("endormir").t('ip').pe(1).n('p').realize()   
    ) == 'endormons',\
    'endormir:ip4'


def test_conjugation_fr_985():
    assert (
V("endormir").t('ip').pe(2).n('p').realize()   
    ) == 'endormez',\
    'endormir:ip5'


def test_conjugation_fr_986():
    assert (
V("endormir").t('pr').realize()   
    ) == 'endormant',\
    'endormir:pr'


def test_conjugation_fr_987():
    assert (
V("endormir").t('pp').realize()   
    ) == 'endormi',\
    'endormir:pp'


def test_conjugation_fr_988():
    assert (
V("endormir").t('s').pe(1).n('s').realize()   
    ) == 'endorme',\
    'endormir:s1'


def test_conjugation_fr_989():
    assert (
V("endormir").t('s').pe(2).n('s').realize()   
    ) == 'endormes',\
    'endormir:s2'


def test_conjugation_fr_990():
    assert (
V("endormir").t('s').pe(3).n('s').realize()   
    ) == 'endorme',\
    'endormir:s3'


def test_conjugation_fr_991():
    assert (
V("endormir").t('s').pe(1).n('p').realize()   
    ) == 'endormions',\
    'endormir:s4'


def test_conjugation_fr_992():
    assert (
V("endormir").t('s').pe(2).n('p').realize()   
    ) == 'endormiez',\
    'endormir:s5'


def test_conjugation_fr_993():
    assert (
V("endormir").t('s').pe(3).n('p').realize()   
    ) == 'endorment',\
    'endormir:s6'


def test_conjugation_fr_994():
    assert (
V("entendre").t('p').pe(3).n('s').realize()   
    ) == 'entend',\
    'entendre:p3'


def test_conjugation_fr_995():
    assert (
V("entendre").t('pr').realize()   
    ) == 'entendant',\
    'entendre:pr'


def test_conjugation_fr_996():
    assert (
V("entendre").t('p').pe(3).n('p').realize()   
    ) == 'entendent',\
    'entendre:p6'


def test_conjugation_fr_997():
    assert (
V("entendre").t('p').pe(2).n('p').realize()   
    ) == 'entendez',\
    'entendre:p5'


def test_conjugation_fr_998():
    assert (
V("entendre").t('ip').pe(2).n('p').realize()   
    ) == 'entendez',\
    'entendre:ip5'


def test_conjugation_fr_999():
    assert (
V("entendre").t('p').pe(1).n('p').realize()   
    ) == 'entendons',\
    'entendre:p4'


def test_conjugation_fr_1000():
    assert (
V("entendre").t('ip').pe(1).n('p').realize()   
    ) == 'entendons',\
    'entendre:ip4'


def test_conjugation_fr_1001():
    assert (
V("entendre").t('p').pe(1).n('s').realize()   
    ) == 'entends',\
    'entendre:p1'


def test_conjugation_fr_1002():
    assert (
V("entendre").t('p').pe(2).n('s').realize()   
    ) == 'entends',\
    'entendre:p2'


def test_conjugation_fr_1003():
    assert (
V("entendre").t('ip').pe(2).n('s').realize()   
    ) == 'entends',\
    'entendre:ip2'


def test_conjugation_fr_1004():
    assert (
V("entendre").t('pp').realize()   
    ) == 'entendu',\
    'entendre:pp'


def test_conjugation_fr_1005():
    assert (
V("entendre").t('s').pe(1).n('s').realize()   
    ) == 'entende',\
    'entendre:s1'


def test_conjugation_fr_1006():
    assert (
V("entendre").t('s').pe(2).n('s').realize()   
    ) == 'entendes',\
    'entendre:s2'


def test_conjugation_fr_1007():
    assert (
V("entendre").t('s').pe(3).n('s').realize()   
    ) == 'entende',\
    'entendre:s3'


def test_conjugation_fr_1008():
    assert (
V("entendre").t('s').pe(1).n('p').realize()   
    ) == 'entendions',\
    'entendre:s4'


def test_conjugation_fr_1009():
    assert (
V("entendre").t('s').pe(2).n('p').realize()   
    ) == 'entendiez',\
    'entendre:s5'


def test_conjugation_fr_1010():
    assert (
V("entendre").t('s').pe(3).n('p').realize()   
    ) == 'entendent',\
    'entendre:s6'


def test_conjugation_fr_1011():
    assert (
V("entreprendre").t('pr').realize()   
    ) == 'entreprenant',\
    'entreprendre:pr'


def test_conjugation_fr_1012():
    assert (
V("entreprendre").t('p').pe(3).n('s').realize()   
    ) == 'entreprend',\
    'entreprendre:p3'


def test_conjugation_fr_1013():
    assert (
V("entreprendre").t('p').pe(1).n('s').realize()   
    ) == 'entreprends',\
    'entreprendre:p1'


def test_conjugation_fr_1014():
    assert (
V("entreprendre").t('p').pe(2).n('s').realize()   
    ) == 'entreprends',\
    'entreprendre:p2'


def test_conjugation_fr_1015():
    assert (
V("entreprendre").t('ip').pe(2).n('s').realize()   
    ) == 'entreprends',\
    'entreprendre:ip2'


def test_conjugation_fr_1016():
    assert (
V("entreprendre").t('p').pe(2).n('p').realize()   
    ) == 'entreprenez',\
    'entreprendre:p5'


def test_conjugation_fr_1017():
    assert (
V("entreprendre").t('ip').pe(2).n('p').realize()   
    ) == 'entreprenez',\
    'entreprendre:ip5'


def test_conjugation_fr_1018():
    assert (
V("entreprendre").t('p').pe(3).n('p').realize()   
    ) == 'entreprennent',\
    'entreprendre:p6'


def test_conjugation_fr_1019():
    assert (
V("entreprendre").t('p').pe(1).n('p').realize()   
    ) == 'entreprenons',\
    'entreprendre:p4'


def test_conjugation_fr_1020():
    assert (
V("entreprendre").t('ip').pe(1).n('p').realize()   
    ) == 'entreprenons',\
    'entreprendre:ip4'


def test_conjugation_fr_1021():
    assert (
V("entreprendre").t('pp').realize()   
    ) == 'entrepris',\
    'entreprendre:pp'


def test_conjugation_fr_1022():
    assert (
V("entreprendre").t('s').pe(1).n('s').realize()   
    ) == 'entreprenne',\
    'entreprendre:s1'


def test_conjugation_fr_1023():
    assert (
V("entreprendre").t('s').pe(2).n('s').realize()   
    ) == 'entreprennes',\
    'entreprendre:s2'


def test_conjugation_fr_1024():
    assert (
V("entreprendre").t('s').pe(3).n('s').realize()   
    ) == 'entreprenne',\
    'entreprendre:s3'


def test_conjugation_fr_1025():
    assert (
V("entreprendre").t('s').pe(1).n('p').realize()   
    ) == 'entreprenions',\
    'entreprendre:s4'


def test_conjugation_fr_1026():
    assert (
V("entreprendre").t('s').pe(2).n('p').realize()   
    ) == 'entrepreniez',\
    'entreprendre:s5'


def test_conjugation_fr_1027():
    assert (
V("entreprendre").t('s').pe(3).n('p').realize()   
    ) == 'entreprennent',\
    'entreprendre:s6'


def test_conjugation_fr_1028():
    assert (
V("entretenir").t('pr').realize()   
    ) == 'entretenant',\
    'entretenir:pr'


def test_conjugation_fr_1029():
    assert (
V("entretenir").t('p').pe(2).n('p').realize()   
    ) == 'entretenez',\
    'entretenir:p5'


def test_conjugation_fr_1030():
    assert (
V("entretenir").t('ip').pe(2).n('p').realize()   
    ) == 'entretenez',\
    'entretenir:ip5'


def test_conjugation_fr_1031():
    assert (
V("entretenir").t('p').pe(1).n('p').realize()   
    ) == 'entretenons',\
    'entretenir:p4'


def test_conjugation_fr_1032():
    assert (
V("entretenir").t('ip').pe(1).n('p').realize()   
    ) == 'entretenons',\
    'entretenir:ip4'


def test_conjugation_fr_1033():
    assert (
V("entretenir").t('p').pe(3).n('p').realize()   
    ) == 'entretiennent',\
    'entretenir:p6'


def test_conjugation_fr_1034():
    assert (
V("entretenir").t('p').pe(1).n('s').realize()   
    ) == 'entretiens',\
    'entretenir:p1'


def test_conjugation_fr_1035():
    assert (
V("entretenir").t('p').pe(2).n('s').realize()   
    ) == 'entretiens',\
    'entretenir:p2'


def test_conjugation_fr_1036():
    assert (
V("entretenir").t('ip').pe(2).n('s').realize()   
    ) == 'entretiens',\
    'entretenir:ip2'


def test_conjugation_fr_1037():
    assert (
V("entretenir").t('p').pe(3).n('s').realize()   
    ) == 'entretient',\
    'entretenir:p3'


def test_conjugation_fr_1038():
    assert (
V("entretenir").t('pp').realize()   
    ) == 'entretenu',\
    'entretenir:pp'


def test_conjugation_fr_1039():
    assert (
V("entretenir").t('s').pe(1).n('s').realize()   
    ) == 'entretienne',\
    'entretenir:s1'


def test_conjugation_fr_1040():
    assert (
V("entretenir").t('s').pe(2).n('s').realize()   
    ) == 'entretiennes',\
    'entretenir:s2'


def test_conjugation_fr_1041():
    assert (
V("entretenir").t('s').pe(3).n('s').realize()   
    ) == 'entretienne',\
    'entretenir:s3'


def test_conjugation_fr_1042():
    assert (
V("entretenir").t('s').pe(1).n('p').realize()   
    ) == 'entretenions',\
    'entretenir:s4'


def test_conjugation_fr_1043():
    assert (
V("entretenir").t('s').pe(2).n('p').realize()   
    ) == 'entreteniez',\
    'entretenir:s5'


def test_conjugation_fr_1044():
    assert (
V("entretenir").t('s').pe(3).n('p').realize()   
    ) == 'entretiennent',\
    'entretenir:s6'


def test_conjugation_fr_1045():
    assert (
V("entrevoir").t('p').pe(3).n('p').realize()   
    ) == 'entrevoient',\
    'entrevoir:p6'


def test_conjugation_fr_1046():
    assert (
V("entrevoir").t('p').pe(1).n('s').realize()   
    ) == 'entrevois',\
    'entrevoir:p1'


def test_conjugation_fr_1047():
    assert (
V("entrevoir").t('p').pe(2).n('s').realize()   
    ) == 'entrevois',\
    'entrevoir:p2'


def test_conjugation_fr_1048():
    assert (
V("entrevoir").t('ip').pe(2).n('s').realize()   
    ) == 'entrevois',\
    'entrevoir:ip2'


def test_conjugation_fr_1049():
    assert (
V("entrevoir").t('p').pe(3).n('s').realize()   
    ) == 'entrevoit',\
    'entrevoir:p3'


def test_conjugation_fr_1050():
    assert (
V("entrevoir").t('pr').realize()   
    ) == 'entrevoyant',\
    'entrevoir:pr'


def test_conjugation_fr_1051():
    assert (
V("entrevoir").t('p').pe(2).n('p').realize()   
    ) == 'entrevoyez',\
    'entrevoir:p5'


def test_conjugation_fr_1052():
    assert (
V("entrevoir").t('ip').pe(2).n('p').realize()   
    ) == 'entrevoyez',\
    'entrevoir:ip5'


def test_conjugation_fr_1053():
    assert (
V("entrevoir").t('p').pe(1).n('p').realize()   
    ) == 'entrevoyons',\
    'entrevoir:p4'


def test_conjugation_fr_1054():
    assert (
V("entrevoir").t('ip').pe(1).n('p').realize()   
    ) == 'entrevoyons',\
    'entrevoir:ip4'


def test_conjugation_fr_1055():
    assert (
V("entrevoir").t('pp').realize()   
    ) == 'entrevu',\
    'entrevoir:pp'


def test_conjugation_fr_1056():
    assert (
V("entrevoir").t('s').pe(1).n('s').realize()   
    ) == 'entrevoie',\
    'entrevoir:s1'


def test_conjugation_fr_1057():
    assert (
V("entrevoir").t('s').pe(2).n('s').realize()   
    ) == 'entrevoies',\
    'entrevoir:s2'


def test_conjugation_fr_1058():
    assert (
V("entrevoir").t('s').pe(3).n('s').realize()   
    ) == 'entrevoie',\
    'entrevoir:s3'


def test_conjugation_fr_1059():
    assert (
V("entrevoir").t('s').pe(1).n('p').realize()   
    ) == 'entrevoyions',\
    'entrevoir:s4'


def test_conjugation_fr_1060():
    assert (
V("entrevoir").t('s').pe(2).n('p').realize()   
    ) == 'entrevoyiez',\
    'entrevoir:s5'


def test_conjugation_fr_1061():
    assert (
V("entrevoir").t('s').pe(3).n('p').realize()   
    ) == 'entrevoient',\
    'entrevoir:s6'


def test_conjugation_fr_1062():
    assert (
V("entrouvrir").t('pr').realize()   
    ) == 'entrouvrant',\
    'entrouvrir:pr'


def test_conjugation_fr_1063():
    assert (
V("entrouvrir").t('p').pe(1).n('s').realize()   
    ) == 'entrouvre',\
    'entrouvrir:p1'


def test_conjugation_fr_1064():
    assert (
V("entrouvrir").t('p').pe(3).n('s').realize()   
    ) == 'entrouvre',\
    'entrouvrir:p3'


def test_conjugation_fr_1065():
    assert (
V("entrouvrir").t('ip').pe(2).n('s').realize()   
    ) == 'entrouvre',\
    'entrouvrir:ip2'


def test_conjugation_fr_1066():
    assert (
V("entrouvrir").t('p').pe(3).n('p').realize()   
    ) == 'entrouvrent',\
    'entrouvrir:p6'


def test_conjugation_fr_1067():
    assert (
V("entrouvrir").t('p').pe(2).n('s').realize()   
    ) == 'entrouvres',\
    'entrouvrir:p2'


def test_conjugation_fr_1068():
    assert (
V("entrouvrir").t('p').pe(2).n('p').realize()   
    ) == 'entrouvrez',\
    'entrouvrir:p5'


def test_conjugation_fr_1069():
    assert (
V("entrouvrir").t('ip').pe(2).n('p').realize()   
    ) == 'entrouvrez',\
    'entrouvrir:ip5'


def test_conjugation_fr_1070():
    assert (
V("entrouvrir").t('p').pe(1).n('p').realize()   
    ) == 'entrouvrons',\
    'entrouvrir:p4'


def test_conjugation_fr_1071():
    assert (
V("entrouvrir").t('ip').pe(1).n('p').realize()   
    ) == 'entrouvrons',\
    'entrouvrir:ip4'


def test_conjugation_fr_1072():
    assert (
V("entrouvrir").t('pp').realize()   
    ) == 'entrouvert',\
    'entrouvrir:pp'


def test_conjugation_fr_1073():
    assert (
V("entrouvrir").t('s').pe(1).n('s').realize()   
    ) == 'entrouvre',\
    'entrouvrir:s1'


def test_conjugation_fr_1074():
    assert (
V("entrouvrir").t('s').pe(2).n('s').realize()   
    ) == 'entrouvres',\
    'entrouvrir:s2'


def test_conjugation_fr_1075():
    assert (
V("entrouvrir").t('s').pe(3).n('s').realize()   
    ) == 'entrouvre',\
    'entrouvrir:s3'


def test_conjugation_fr_1076():
    assert (
V("entrouvrir").t('s').pe(1).n('p').realize()   
    ) == 'entrouvrions',\
    'entrouvrir:s4'


def test_conjugation_fr_1077():
    assert (
V("entrouvrir").t('s').pe(2).n('p').realize()   
    ) == 'entrouvriez',\
    'entrouvrir:s5'


def test_conjugation_fr_1078():
    assert (
V("entrouvrir").t('s').pe(3).n('p').realize()   
    ) == 'entrouvrent',\
    'entrouvrir:s6'


def test_conjugation_fr_1079():
    assert (
V("éteindre").t('pr').realize()   
    ) == 'éteignant',\
    'éteindre:pr'


def test_conjugation_fr_1080():
    assert (
V("éteindre").t('p').pe(3).n('p').realize()   
    ) == 'éteignent',\
    'éteindre:p6'


def test_conjugation_fr_1081():
    assert (
V("éteindre").t('p').pe(2).n('p').realize()   
    ) == 'éteignez',\
    'éteindre:p5'


def test_conjugation_fr_1082():
    assert (
V("éteindre").t('ip').pe(2).n('p').realize()   
    ) == 'éteignez',\
    'éteindre:ip5'


def test_conjugation_fr_1083():
    assert (
V("éteindre").t('p').pe(1).n('p').realize()   
    ) == 'éteignons',\
    'éteindre:p4'


def test_conjugation_fr_1084():
    assert (
V("éteindre").t('ip').pe(1).n('p').realize()   
    ) == 'éteignons',\
    'éteindre:ip4'


def test_conjugation_fr_1085():
    assert (
V("éteindre").t('p').pe(1).n('s').realize()   
    ) == 'éteins',\
    'éteindre:p1'


def test_conjugation_fr_1086():
    assert (
V("éteindre").t('p').pe(2).n('s').realize()   
    ) == 'éteins',\
    'éteindre:p2'


def test_conjugation_fr_1087():
    assert (
V("éteindre").t('ip').pe(2).n('s').realize()   
    ) == 'éteins',\
    'éteindre:ip2'


def test_conjugation_fr_1088():
    assert (
V("éteindre").t('p').pe(3).n('s').realize()   
    ) == 'éteint',\
    'éteindre:p3'


def test_conjugation_fr_1089():
    assert (
V("éteindre").t('pp').realize()   
    ) == 'éteint',\
    'éteindre:pp'


def test_conjugation_fr_1090():
    assert (
V("éteindre").t('s').pe(1).n('s').realize()   
    ) == 'éteigne',\
    'éteindre:s1'


def test_conjugation_fr_1091():
    assert (
V("éteindre").t('s').pe(2).n('s').realize()   
    ) == 'éteignes',\
    'éteindre:s2'


def test_conjugation_fr_1092():
    assert (
V("éteindre").t('s').pe(3).n('s').realize()   
    ) == 'éteigne',\
    'éteindre:s3'


def test_conjugation_fr_1093():
    assert (
V("éteindre").t('s').pe(1).n('p').realize()   
    ) == 'éteignions',\
    'éteindre:s4'


def test_conjugation_fr_1094():
    assert (
V("éteindre").t('s').pe(2).n('p').realize()   
    ) == 'éteigniez',\
    'éteindre:s5'


def test_conjugation_fr_1095():
    assert (
V("éteindre").t('s').pe(3).n('p').realize()   
    ) == 'éteignent',\
    'éteindre:s6'


def test_conjugation_fr_1096():
    assert (
V("étendre").t('p').pe(3).n('s').realize()   
    ) == 'étend',\
    'étendre:p3'


def test_conjugation_fr_1097():
    assert (
V("étendre").t('pr').realize()   
    ) == 'étendant',\
    'étendre:pr'


def test_conjugation_fr_1098():
    assert (
V("étendre").t('p').pe(3).n('p').realize()   
    ) == 'étendent',\
    'étendre:p6'


def test_conjugation_fr_1099():
    assert (
V("étendre").t('p').pe(2).n('p').realize()   
    ) == 'étendez',\
    'étendre:p5'


def test_conjugation_fr_1100():
    assert (
V("étendre").t('ip').pe(2).n('p').realize()   
    ) == 'étendez',\
    'étendre:ip5'


def test_conjugation_fr_1101():
    assert (
V("étendre").t('p').pe(1).n('p').realize()   
    ) == 'étendons',\
    'étendre:p4'


def test_conjugation_fr_1102():
    assert (
V("étendre").t('ip').pe(1).n('p').realize()   
    ) == 'étendons',\
    'étendre:ip4'


def test_conjugation_fr_1103():
    assert (
V("étendre").t('p').pe(1).n('s').realize()   
    ) == 'étends',\
    'étendre:p1'


def test_conjugation_fr_1104():
    assert (
V("étendre").t('p').pe(2).n('s').realize()   
    ) == 'étends',\
    'étendre:p2'


def test_conjugation_fr_1105():
    assert (
V("étendre").t('ip').pe(2).n('s').realize()   
    ) == 'étends',\
    'étendre:ip2'


def test_conjugation_fr_1106():
    assert (
V("étendre").t('pp').realize()   
    ) == 'étendu',\
    'étendre:pp'


def test_conjugation_fr_1107():
    assert (
V("étendre").t('s').pe(1).n('s').realize()   
    ) == 'étende',\
    'étendre:s1'


def test_conjugation_fr_1108():
    assert (
V("étendre").t('s').pe(2).n('s').realize()   
    ) == 'étendes',\
    'étendre:s2'


def test_conjugation_fr_1109():
    assert (
V("étendre").t('s').pe(3).n('s').realize()   
    ) == 'étende',\
    'étendre:s3'


def test_conjugation_fr_1110():
    assert (
V("étendre").t('s').pe(1).n('p').realize()   
    ) == 'étendions',\
    'étendre:s4'


def test_conjugation_fr_1111():
    assert (
V("étendre").t('s').pe(2).n('p').realize()   
    ) == 'étendiez',\
    'étendre:s5'


def test_conjugation_fr_1112():
    assert (
V("étendre").t('s').pe(3).n('p').realize()   
    ) == 'étendent',\
    'étendre:s6'


def test_conjugation_fr_1113():
    assert (
V("extraire").t('p').pe(3).n('p').realize()   
    ) == 'extraient',\
    'extraire:p6'


def test_conjugation_fr_1114():
    assert (
V("extraire").t('p').pe(1).n('s').realize()   
    ) == 'extrais',\
    'extraire:p1'


def test_conjugation_fr_1115():
    assert (
V("extraire").t('p').pe(2).n('s').realize()   
    ) == 'extrais',\
    'extraire:p2'


def test_conjugation_fr_1116():
    assert (
V("extraire").t('ip').pe(2).n('s').realize()   
    ) == 'extrais',\
    'extraire:ip2'


def test_conjugation_fr_1117():
    assert (
V("extraire").t('p').pe(3).n('s').realize()   
    ) == 'extrait',\
    'extraire:p3'


def test_conjugation_fr_1118():
    assert (
V("extraire").t('pr').realize()   
    ) == 'extrayant',\
    'extraire:pr'


def test_conjugation_fr_1119():
    assert (
V("extraire").t('p').pe(2).n('p').realize()   
    ) == 'extrayez',\
    'extraire:p5'


def test_conjugation_fr_1120():
    assert (
V("extraire").t('ip').pe(2).n('p').realize()   
    ) == 'extrayez',\
    'extraire:ip5'


def test_conjugation_fr_1121():
    assert (
V("extraire").t('p').pe(1).n('p').realize()   
    ) == 'extrayons',\
    'extraire:p4'


def test_conjugation_fr_1122():
    assert (
V("extraire").t('ip').pe(1).n('p').realize()   
    ) == 'extrayons',\
    'extraire:ip4'


def test_conjugation_fr_1123():
    assert (
V("extraire").t('pp').realize()   
    ) == 'extrait',\
    'extraire:pp'


def test_conjugation_fr_1124():
    assert (
V("extraire").t('s').pe(1).n('s').realize()   
    ) == 'extraie',\
    'extraire:s1'


def test_conjugation_fr_1125():
    assert (
V("extraire").t('s').pe(2).n('s').realize()   
    ) == 'extraies',\
    'extraire:s2'


def test_conjugation_fr_1126():
    assert (
V("extraire").t('s').pe(3).n('s').realize()   
    ) == 'extraie',\
    'extraire:s3'


def test_conjugation_fr_1127():
    assert (
V("extraire").t('s').pe(1).n('p').realize()   
    ) == 'extrayions',\
    'extraire:s4'


def test_conjugation_fr_1128():
    assert (
V("extraire").t('s').pe(2).n('p').realize()   
    ) == 'extrayiez',\
    'extraire:s5'


def test_conjugation_fr_1129():
    assert (
V("extraire").t('s').pe(3).n('p').realize()   
    ) == 'extraient',\
    'extraire:s6'


def test_conjugation_fr_1130():
    assert (
V("faire").t('p').pe(1).n('s').realize()   
    ) == 'fais',\
    'faire:p1'


def test_conjugation_fr_1131():
    assert (
V("faire").t('p').pe(2).n('s').realize()   
    ) == 'fais',\
    'faire:p2'


def test_conjugation_fr_1132():
    assert (
V("faire").t('ip').pe(2).n('s').realize()   
    ) == 'fais',\
    'faire:ip2'


def test_conjugation_fr_1133():
    assert (
V("faire").t('pr').realize()   
    ) == 'faisant',\
    'faire:pr'


def test_conjugation_fr_1134():
    assert (
V("faire").t('p').pe(1).n('p').realize()   
    ) == 'faisons',\
    'faire:p4'


def test_conjugation_fr_1135():
    assert (
V("faire").t('ip').pe(1).n('p').realize()   
    ) == 'faisons',\
    'faire:ip4'


def test_conjugation_fr_1136():
    assert (
V("faire").t('p').pe(3).n('s').realize()   
    ) == 'fait',\
    'faire:p3'


def test_conjugation_fr_1137():
    assert (
V("faire").t('p').pe(2).n('p').realize()   
    ) == 'faites',\
    'faire:p5'


def test_conjugation_fr_1138():
    assert (
V("faire").t('ip').pe(2).n('p').realize()   
    ) == 'faites',\
    'faire:ip5'


def test_conjugation_fr_1139():
    assert (
V("faire").t('p').pe(3).n('p').realize()   
    ) == 'font',\
    'faire:p6'


def test_conjugation_fr_1140():
    assert (
V("faire").t('pp').realize()   
    ) == 'fait',\
    'faire:pp'


def test_conjugation_fr_1141():
    assert (
V("faire").t('s').pe(1).n('s').realize()   
    ) == 'fasse',\
    'faire:s1'


def test_conjugation_fr_1142():
    assert (
V("faire").t('s').pe(2).n('s').realize()   
    ) == 'fasses',\
    'faire:s2'


def test_conjugation_fr_1143():
    assert (
V("faire").t('s').pe(3).n('s').realize()   
    ) == 'fasse',\
    'faire:s3'


def test_conjugation_fr_1144():
    assert (
V("faire").t('s').pe(1).n('p').realize()   
    ) == 'fassions',\
    'faire:s4'


def test_conjugation_fr_1145():
    assert (
V("faire").t('s').pe(2).n('p').realize()   
    ) == 'fassiez',\
    'faire:s5'


def test_conjugation_fr_1146():
    assert (
V("faire").t('s').pe(3).n('p').realize()   
    ) == 'fassent',\
    'faire:s6'


def test_conjugation_fr_1147():
    assert (
V("falloir").t('p').pe(3).n('s').realize()   
    ) == 'faut',\
    'falloir:p3'


def test_conjugation_fr_1148():
    assert (
V("falloir").t('s').pe(3).n('s').realize()   
    ) == 'faille',\
    'falloir:s3'


def test_conjugation_fr_1149():
    assert (
V("fendre").t('p').pe(3).n('s').realize()   
    ) == 'fend',\
    'fendre:p3'


def test_conjugation_fr_1150():
    assert (
V("fendre").t('pr').realize()   
    ) == 'fendant',\
    'fendre:pr'


def test_conjugation_fr_1151():
    assert (
V("fendre").t('p').pe(3).n('p').realize()   
    ) == 'fendent',\
    'fendre:p6'


def test_conjugation_fr_1152():
    assert (
V("fendre").t('p').pe(2).n('p').realize()   
    ) == 'fendez',\
    'fendre:p5'


def test_conjugation_fr_1153():
    assert (
V("fendre").t('ip').pe(2).n('p').realize()   
    ) == 'fendez',\
    'fendre:ip5'


def test_conjugation_fr_1154():
    assert (
V("fendre").t('p').pe(1).n('p').realize()   
    ) == 'fendons',\
    'fendre:p4'


def test_conjugation_fr_1155():
    assert (
V("fendre").t('ip').pe(1).n('p').realize()   
    ) == 'fendons',\
    'fendre:ip4'


def test_conjugation_fr_1156():
    assert (
V("fendre").t('p').pe(1).n('s').realize()   
    ) == 'fends',\
    'fendre:p1'


def test_conjugation_fr_1157():
    assert (
V("fendre").t('p').pe(2).n('s').realize()   
    ) == 'fends',\
    'fendre:p2'


def test_conjugation_fr_1158():
    assert (
V("fendre").t('ip').pe(2).n('s').realize()   
    ) == 'fends',\
    'fendre:ip2'


def test_conjugation_fr_1159():
    assert (
V("fendre").t('pp').realize()   
    ) == 'fendu',\
    'fendre:pp'


def test_conjugation_fr_1160():
    assert (
V("fendre").t('s').pe(1).n('s').realize()   
    ) == 'fende',\
    'fendre:s1'


def test_conjugation_fr_1161():
    assert (
V("fendre").t('s').pe(2).n('s').realize()   
    ) == 'fendes',\
    'fendre:s2'


def test_conjugation_fr_1162():
    assert (
V("fendre").t('s').pe(3).n('s').realize()   
    ) == 'fende',\
    'fendre:s3'


def test_conjugation_fr_1163():
    assert (
V("fendre").t('s').pe(1).n('p').realize()   
    ) == 'fendions',\
    'fendre:s4'


def test_conjugation_fr_1164():
    assert (
V("fendre").t('s').pe(2).n('p').realize()   
    ) == 'fendiez',\
    'fendre:s5'


def test_conjugation_fr_1165():
    assert (
V("fendre").t('s').pe(3).n('p').realize()   
    ) == 'fendent',\
    'fendre:s6'


def test_conjugation_fr_1166():
    assert (
V("fondre").t('p').pe(3).n('s').realize()   
    ) == 'fond',\
    'fondre:p3'


def test_conjugation_fr_1167():
    assert (
V("fondre").t('pr').realize()   
    ) == 'fondant',\
    'fondre:pr'


def test_conjugation_fr_1168():
    assert (
V("fondre").t('p').pe(3).n('p').realize()   
    ) == 'fondent',\
    'fondre:p6'


def test_conjugation_fr_1169():
    assert (
V("fondre").t('p').pe(2).n('p').realize()   
    ) == 'fondez',\
    'fondre:p5'


def test_conjugation_fr_1170():
    assert (
V("fondre").t('ip').pe(2).n('p').realize()   
    ) == 'fondez',\
    'fondre:ip5'


def test_conjugation_fr_1171():
    assert (
V("fondre").t('p').pe(1).n('p').realize()   
    ) == 'fondons',\
    'fondre:p4'


def test_conjugation_fr_1172():
    assert (
V("fondre").t('ip').pe(1).n('p').realize()   
    ) == 'fondons',\
    'fondre:ip4'


def test_conjugation_fr_1173():
    assert (
V("fondre").t('p').pe(1).n('s').realize()   
    ) == 'fonds',\
    'fondre:p1'


def test_conjugation_fr_1174():
    assert (
V("fondre").t('p').pe(2).n('s').realize()   
    ) == 'fonds',\
    'fondre:p2'


def test_conjugation_fr_1175():
    assert (
V("fondre").t('ip').pe(2).n('s').realize()   
    ) == 'fonds',\
    'fondre:ip2'


def test_conjugation_fr_1176():
    assert (
V("fondre").t('pp').realize()   
    ) == 'fondu',\
    'fondre:pp'


def test_conjugation_fr_1177():
    assert (
V("fondre").t('s').pe(1).n('s').realize()   
    ) == 'fonde',\
    'fondre:s1'


def test_conjugation_fr_1178():
    assert (
V("fondre").t('s').pe(2).n('s').realize()   
    ) == 'fondes',\
    'fondre:s2'


def test_conjugation_fr_1179():
    assert (
V("fondre").t('s').pe(3).n('s').realize()   
    ) == 'fonde',\
    'fondre:s3'


def test_conjugation_fr_1180():
    assert (
V("fondre").t('s').pe(1).n('p').realize()   
    ) == 'fondions',\
    'fondre:s4'


def test_conjugation_fr_1181():
    assert (
V("fondre").t('s').pe(2).n('p').realize()   
    ) == 'fondiez',\
    'fondre:s5'


def test_conjugation_fr_1182():
    assert (
V("fondre").t('s').pe(3).n('p').realize()   
    ) == 'fondent',\
    'fondre:s6'


def test_conjugation_fr_1183():
    assert (
V("fuir").t('p').pe(3).n('p').realize()   
    ) == 'fuient',\
    'fuir:p6'


def test_conjugation_fr_1184():
    assert (
V("fuir").t('p').pe(1).n('s').realize()   
    ) == 'fuis',\
    'fuir:p1'


def test_conjugation_fr_1185():
    assert (
V("fuir").t('p').pe(2).n('s').realize()   
    ) == 'fuis',\
    'fuir:p2'


def test_conjugation_fr_1186():
    assert (
V("fuir").t('ip').pe(2).n('s').realize()   
    ) == 'fuis',\
    'fuir:ip2'


def test_conjugation_fr_1187():
    assert (
V("fuir").t('p').pe(3).n('s').realize()   
    ) == 'fuit',\
    'fuir:p3'


def test_conjugation_fr_1188():
    assert (
V("fuir").t('pr').realize()   
    ) == 'fuyant',\
    'fuir:pr'


def test_conjugation_fr_1189():
    assert (
V("fuir").t('p').pe(2).n('p').realize()   
    ) == 'fuyez',\
    'fuir:p5'


def test_conjugation_fr_1190():
    assert (
V("fuir").t('ip').pe(2).n('p').realize()   
    ) == 'fuyez',\
    'fuir:ip5'


def test_conjugation_fr_1191():
    assert (
V("fuir").t('p').pe(1).n('p').realize()   
    ) == 'fuyons',\
    'fuir:p4'


def test_conjugation_fr_1192():
    assert (
V("fuir").t('ip').pe(1).n('p').realize()   
    ) == 'fuyons',\
    'fuir:ip4'


def test_conjugation_fr_1193():
    assert (
V("fuir").t('pp').realize()   
    ) == 'fui',\
    'fuir:pp'


def test_conjugation_fr_1194():
    assert (
V("fuir").t('s').pe(1).n('s').realize()   
    ) == 'fuie',\
    'fuir:s1'


def test_conjugation_fr_1195():
    assert (
V("fuir").t('s').pe(2).n('s').realize()   
    ) == 'fuies',\
    'fuir:s2'


def test_conjugation_fr_1196():
    assert (
V("fuir").t('s').pe(3).n('s').realize()   
    ) == 'fuie',\
    'fuir:s3'


def test_conjugation_fr_1197():
    assert (
V("fuir").t('s').pe(1).n('p').realize()   
    ) == 'fuyions',\
    'fuir:s4'


def test_conjugation_fr_1198():
    assert (
V("fuir").t('s').pe(2).n('p').realize()   
    ) == 'fuyiez',\
    'fuir:s5'


def test_conjugation_fr_1199():
    assert (
V("fuir").t('s').pe(3).n('p').realize()   
    ) == 'fuient',\
    'fuir:s6'


def test_conjugation_fr_1200():
    assert (
V("inscrire").t('p').pe(1).n('s').realize()   
    ) == 'inscris',\
    'inscrire:p1'


def test_conjugation_fr_1201():
    assert (
V("inscrire").t('p').pe(2).n('s').realize()   
    ) == 'inscris',\
    'inscrire:p2'


def test_conjugation_fr_1202():
    assert (
V("inscrire").t('ip').pe(2).n('s').realize()   
    ) == 'inscris',\
    'inscrire:ip2'


def test_conjugation_fr_1203():
    assert (
V("inscrire").t('p').pe(3).n('s').realize()   
    ) == 'inscrit',\
    'inscrire:p3'


def test_conjugation_fr_1204():
    assert (
V("inscrire").t('pr').realize()   
    ) == 'inscrivant',\
    'inscrire:pr'


def test_conjugation_fr_1205():
    assert (
V("inscrire").t('p').pe(3).n('p').realize()   
    ) == 'inscrivent',\
    'inscrire:p6'


def test_conjugation_fr_1206():
    assert (
V("inscrire").t('p').pe(2).n('p').realize()   
    ) == 'inscrivez',\
    'inscrire:p5'


def test_conjugation_fr_1207():
    assert (
V("inscrire").t('ip').pe(2).n('p').realize()   
    ) == 'inscrivez',\
    'inscrire:ip5'


def test_conjugation_fr_1208():
    assert (
V("inscrire").t('p').pe(1).n('p').realize()   
    ) == 'inscrivons',\
    'inscrire:p4'


def test_conjugation_fr_1209():
    assert (
V("inscrire").t('ip').pe(1).n('p').realize()   
    ) == 'inscrivons',\
    'inscrire:ip4'


def test_conjugation_fr_1210():
    assert (
V("inscrire").t('pp').realize()   
    ) == 'inscrit',\
    'inscrire:pp'


def test_conjugation_fr_1211():
    assert (
V("inscrire").t('s').pe(1).n('s').realize()   
    ) == 'inscrive',\
    'inscrire:s1'


def test_conjugation_fr_1212():
    assert (
V("inscrire").t('s').pe(2).n('s').realize()   
    ) == 'inscrives',\
    'inscrire:s2'


def test_conjugation_fr_1213():
    assert (
V("inscrire").t('s').pe(3).n('s').realize()   
    ) == 'inscrive',\
    'inscrire:s3'


def test_conjugation_fr_1214():
    assert (
V("inscrire").t('s').pe(1).n('p').realize()   
    ) == 'inscrivions',\
    'inscrire:s4'


def test_conjugation_fr_1215():
    assert (
V("inscrire").t('s').pe(2).n('p').realize()   
    ) == 'inscriviez',\
    'inscrire:s5'


def test_conjugation_fr_1216():
    assert (
V("inscrire").t('s').pe(3).n('p').realize()   
    ) == 'inscrivent',\
    'inscrire:s6'


def test_conjugation_fr_1217():
    assert (
V("instruire").t('p').pe(1).n('s').realize()   
    ) == 'instruis',\
    'instruire:p1'


def test_conjugation_fr_1218():
    assert (
V("instruire").t('p').pe(2).n('s').realize()   
    ) == 'instruis',\
    'instruire:p2'


def test_conjugation_fr_1219():
    assert (
V("instruire").t('ip').pe(2).n('s').realize()   
    ) == 'instruis',\
    'instruire:ip2'


def test_conjugation_fr_1220():
    assert (
V("instruire").t('pr').realize()   
    ) == 'instruisant',\
    'instruire:pr'


def test_conjugation_fr_1221():
    assert (
V("instruire").t('p').pe(3).n('p').realize()   
    ) == 'instruisent',\
    'instruire:p6'


def test_conjugation_fr_1222():
    assert (
V("instruire").t('p').pe(2).n('p').realize()   
    ) == 'instruisez',\
    'instruire:p5'


def test_conjugation_fr_1223():
    assert (
V("instruire").t('ip').pe(2).n('p').realize()   
    ) == 'instruisez',\
    'instruire:ip5'


def test_conjugation_fr_1224():
    assert (
V("instruire").t('p').pe(1).n('p').realize()   
    ) == 'instruisons',\
    'instruire:p4'


def test_conjugation_fr_1225():
    assert (
V("instruire").t('ip').pe(1).n('p').realize()   
    ) == 'instruisons',\
    'instruire:ip4'


def test_conjugation_fr_1226():
    assert (
V("instruire").t('p').pe(3).n('s').realize()   
    ) == 'instruit',\
    'instruire:p3'


def test_conjugation_fr_1227():
    assert (
V("instruire").t('pp').realize()   
    ) == 'instruit',\
    'instruire:pp'


def test_conjugation_fr_1228():
    assert (
V("instruire").t('s').pe(1).n('s').realize()   
    ) == 'instruise',\
    'instruire:s1'


def test_conjugation_fr_1229():
    assert (
V("instruire").t('s').pe(2).n('s').realize()   
    ) == 'instruises',\
    'instruire:s2'


def test_conjugation_fr_1230():
    assert (
V("instruire").t('s').pe(3).n('s').realize()   
    ) == 'instruise',\
    'instruire:s3'


def test_conjugation_fr_1231():
    assert (
V("instruire").t('s').pe(1).n('p').realize()   
    ) == 'instruisions',\
    'instruire:s4'


def test_conjugation_fr_1232():
    assert (
V("instruire").t('s').pe(2).n('p').realize()   
    ) == 'instruisiez',\
    'instruire:s5'


def test_conjugation_fr_1233():
    assert (
V("instruire").t('s').pe(3).n('p').realize()   
    ) == 'instruisent',\
    'instruire:s6'


def test_conjugation_fr_1234():
    assert (
V("interdire").t('p').pe(1).n('s').realize()   
    ) == 'interdis',\
    'interdire:p1'


def test_conjugation_fr_1235():
    assert (
V("interdire").t('p').pe(2).n('s').realize()   
    ) == 'interdis',\
    'interdire:p2'


def test_conjugation_fr_1236():
    assert (
V("interdire").t('ip').pe(2).n('s').realize()   
    ) == 'interdis',\
    'interdire:ip2'


def test_conjugation_fr_1237():
    assert (
V("interdire").t('pr').realize()   
    ) == 'interdisant',\
    'interdire:pr'


def test_conjugation_fr_1238():
    assert (
V("interdire").t('p').pe(3).n('p').realize()   
    ) == 'interdisent',\
    'interdire:p6'


def test_conjugation_fr_1239():
    assert (
V("interdire").t('p').pe(2).n('p').realize()   
    ) == 'interdisez',\
    'interdire:p5'


def test_conjugation_fr_1240():
    assert (
V("interdire").t('ip').pe(2).n('p').realize()   
    ) == 'interdisez',\
    'interdire:ip5'


def test_conjugation_fr_1241():
    assert (
V("interdire").t('p').pe(1).n('p').realize()   
    ) == 'interdisons',\
    'interdire:p4'


def test_conjugation_fr_1242():
    assert (
V("interdire").t('ip').pe(1).n('p').realize()   
    ) == 'interdisons',\
    'interdire:ip4'


def test_conjugation_fr_1243():
    assert (
V("interdire").t('p').pe(3).n('s').realize()   
    ) == 'interdit',\
    'interdire:p3'


def test_conjugation_fr_1244():
    assert (
V("interdire").t('pp').realize()   
    ) == 'interdit',\
    'interdire:pp'


def test_conjugation_fr_1245():
    assert (
V("interdire").t('s').pe(1).n('s').realize()   
    ) == 'interdise',\
    'interdire:s1'


def test_conjugation_fr_1246():
    assert (
V("interdire").t('s').pe(2).n('s').realize()   
    ) == 'interdises',\
    'interdire:s2'


def test_conjugation_fr_1247():
    assert (
V("interdire").t('s').pe(3).n('s').realize()   
    ) == 'interdise',\
    'interdire:s3'


def test_conjugation_fr_1248():
    assert (
V("interdire").t('s').pe(1).n('p').realize()   
    ) == 'interdisions',\
    'interdire:s4'


def test_conjugation_fr_1249():
    assert (
V("interdire").t('s').pe(2).n('p').realize()   
    ) == 'interdisiez',\
    'interdire:s5'


def test_conjugation_fr_1250():
    assert (
V("interdire").t('s').pe(3).n('p').realize()   
    ) == 'interdisent',\
    'interdire:s6'


def test_conjugation_fr_1251():
    assert (
V("interrompre").t('pr').realize()   
    ) == 'interrompant',\
    'interrompre:pr'


def test_conjugation_fr_1252():
    assert (
V("interrompre").t('p').pe(3).n('p').realize()   
    ) == 'interrompent',\
    'interrompre:p6'


def test_conjugation_fr_1253():
    assert (
V("interrompre").t('p').pe(2).n('p').realize()   
    ) == 'interrompez',\
    'interrompre:p5'


def test_conjugation_fr_1254():
    assert (
V("interrompre").t('ip').pe(2).n('p').realize()   
    ) == 'interrompez',\
    'interrompre:ip5'


def test_conjugation_fr_1255():
    assert (
V("interrompre").t('p').pe(1).n('p').realize()   
    ) == 'interrompons',\
    'interrompre:p4'


def test_conjugation_fr_1256():
    assert (
V("interrompre").t('ip').pe(1).n('p').realize()   
    ) == 'interrompons',\
    'interrompre:ip4'


def test_conjugation_fr_1257():
    assert (
V("interrompre").t('p').pe(1).n('s').realize()   
    ) == 'interromps',\
    'interrompre:p1'


def test_conjugation_fr_1258():
    assert (
V("interrompre").t('p').pe(2).n('s').realize()   
    ) == 'interromps',\
    'interrompre:p2'


def test_conjugation_fr_1259():
    assert (
V("interrompre").t('ip').pe(2).n('s').realize()   
    ) == 'interromps',\
    'interrompre:ip2'


def test_conjugation_fr_1260():
    assert (
V("interrompre").t('p').pe(3).n('s').realize()   
    ) == 'interrompt',\
    'interrompre:p3'


def test_conjugation_fr_1261():
    assert (
V("interrompre").t('pp').realize()   
    ) == 'interrompu',\
    'interrompre:pp'


def test_conjugation_fr_1262():
    assert (
V("interrompre").t('s').pe(1).n('s').realize()   
    ) == 'interrompe',\
    'interrompre:s1'


def test_conjugation_fr_1263():
    assert (
V("interrompre").t('s').pe(2).n('s').realize()   
    ) == 'interrompes',\
    'interrompre:s2'


def test_conjugation_fr_1264():
    assert (
V("interrompre").t('s').pe(3).n('s').realize()   
    ) == 'interrompe',\
    'interrompre:s3'


def test_conjugation_fr_1265():
    assert (
V("interrompre").t('s').pe(1).n('p').realize()   
    ) == 'interrompions',\
    'interrompre:s4'


def test_conjugation_fr_1266():
    assert (
V("interrompre").t('s').pe(2).n('p').realize()   
    ) == 'interrompiez',\
    'interrompre:s5'


def test_conjugation_fr_1267():
    assert (
V("interrompre").t('s').pe(3).n('p').realize()   
    ) == 'interrompent',\
    'interrompre:s6'


def test_conjugation_fr_1268():
    assert (
V("intervenir").t('pr').realize()   
    ) == 'intervenant',\
    'intervenir:pr'


def test_conjugation_fr_1269():
    assert (
V("intervenir").t('p').pe(2).n('p').realize()   
    ) == 'intervenez',\
    'intervenir:p5'


def test_conjugation_fr_1270():
    assert (
V("intervenir").t('ip').pe(2).n('p').realize()   
    ) == 'intervenez',\
    'intervenir:ip5'


def test_conjugation_fr_1271():
    assert (
V("intervenir").t('p').pe(1).n('p').realize()   
    ) == 'intervenons',\
    'intervenir:p4'


def test_conjugation_fr_1272():
    assert (
V("intervenir").t('ip').pe(1).n('p').realize()   
    ) == 'intervenons',\
    'intervenir:ip4'


def test_conjugation_fr_1273():
    assert (
V("intervenir").t('p').pe(3).n('p').realize()   
    ) == 'interviennent',\
    'intervenir:p6'


def test_conjugation_fr_1274():
    assert (
V("intervenir").t('p').pe(1).n('s').realize()   
    ) == 'interviens',\
    'intervenir:p1'


def test_conjugation_fr_1275():
    assert (
V("intervenir").t('p').pe(2).n('s').realize()   
    ) == 'interviens',\
    'intervenir:p2'


def test_conjugation_fr_1276():
    assert (
V("intervenir").t('ip').pe(2).n('s').realize()   
    ) == 'interviens',\
    'intervenir:ip2'


def test_conjugation_fr_1277():
    assert (
V("intervenir").t('p').pe(3).n('s').realize()   
    ) == 'intervient',\
    'intervenir:p3'


def test_conjugation_fr_1278():
    assert (
V("intervenir").t('pp').realize()   
    ) == 'intervenu',\
    'intervenir:pp'


def test_conjugation_fr_1279():
    assert (
V("intervenir").t('s').pe(1).n('s').realize()   
    ) == 'intervienne',\
    'intervenir:s1'


def test_conjugation_fr_1280():
    assert (
V("intervenir").t('s').pe(2).n('s').realize()   
    ) == 'interviennes',\
    'intervenir:s2'


def test_conjugation_fr_1281():
    assert (
V("intervenir").t('s').pe(3).n('s').realize()   
    ) == 'intervienne',\
    'intervenir:s3'


def test_conjugation_fr_1282():
    assert (
V("intervenir").t('s').pe(1).n('p').realize()   
    ) == 'intervenions',\
    'intervenir:s4'


def test_conjugation_fr_1283():
    assert (
V("intervenir").t('s').pe(2).n('p').realize()   
    ) == 'interveniez',\
    'intervenir:s5'


def test_conjugation_fr_1284():
    assert (
V("intervenir").t('s').pe(3).n('p').realize()   
    ) == 'interviennent',\
    'intervenir:s6'


def test_conjugation_fr_1285():
    assert (
V("introduire").t('p').pe(1).n('s').realize()   
    ) == 'introduis',\
    'introduire:p1'


def test_conjugation_fr_1286():
    assert (
V("introduire").t('p').pe(2).n('s').realize()   
    ) == 'introduis',\
    'introduire:p2'


def test_conjugation_fr_1287():
    assert (
V("introduire").t('ip').pe(2).n('s').realize()   
    ) == 'introduis',\
    'introduire:ip2'


def test_conjugation_fr_1288():
    assert (
V("introduire").t('pr').realize()   
    ) == 'introduisant',\
    'introduire:pr'


def test_conjugation_fr_1289():
    assert (
V("introduire").t('p').pe(3).n('p').realize()   
    ) == 'introduisent',\
    'introduire:p6'


def test_conjugation_fr_1290():
    assert (
V("introduire").t('p').pe(2).n('p').realize()   
    ) == 'introduisez',\
    'introduire:p5'


def test_conjugation_fr_1291():
    assert (
V("introduire").t('ip').pe(2).n('p').realize()   
    ) == 'introduisez',\
    'introduire:ip5'


def test_conjugation_fr_1292():
    assert (
V("introduire").t('p').pe(1).n('p').realize()   
    ) == 'introduisons',\
    'introduire:p4'


def test_conjugation_fr_1293():
    assert (
V("introduire").t('ip').pe(1).n('p').realize()   
    ) == 'introduisons',\
    'introduire:ip4'


def test_conjugation_fr_1294():
    assert (
V("introduire").t('p').pe(3).n('s').realize()   
    ) == 'introduit',\
    'introduire:p3'


def test_conjugation_fr_1295():
    assert (
V("introduire").t('pp').realize()   
    ) == 'introduit',\
    'introduire:pp'


def test_conjugation_fr_1296():
    assert (
V("introduire").t('s').pe(1).n('s').realize()   
    ) == 'introduise',\
    'introduire:s1'


def test_conjugation_fr_1297():
    assert (
V("introduire").t('s').pe(2).n('s').realize()   
    ) == 'introduises',\
    'introduire:s2'


def test_conjugation_fr_1298():
    assert (
V("introduire").t('s').pe(3).n('s').realize()   
    ) == 'introduise',\
    'introduire:s3'


def test_conjugation_fr_1299():
    assert (
V("introduire").t('s').pe(1).n('p').realize()   
    ) == 'introduisions',\
    'introduire:s4'


def test_conjugation_fr_1300():
    assert (
V("introduire").t('s').pe(2).n('p').realize()   
    ) == 'introduisiez',\
    'introduire:s5'


def test_conjugation_fr_1301():
    assert (
V("introduire").t('s').pe(3).n('p').realize()   
    ) == 'introduisent',\
    'introduire:s6'


def test_conjugation_fr_1302():
    assert (
V("jeter").t('p').pe(1).n('s').realize()   
    ) == 'jette',\
    'jeter:p1'


def test_conjugation_fr_1303():
    assert (
V("jeter").t('p').pe(2).n('s').realize()   
    ) == 'jettes',\
    'jeter:p2'


def test_conjugation_fr_1304():
    assert (
V("jeter").t('p').pe(3).n('s').realize()   
    ) == 'jette',\
    'jeter:p3'


def test_conjugation_fr_1305():
    assert (
V("jeter").t('p').pe(3).n('p').realize()   
    ) == 'jettent',\
    'jeter:p6'


def test_conjugation_fr_1306():
    assert (
V("jeter").t('s').pe(1).n('s').realize()   
    ) == 'jette',\
    'jeter:s1'


def test_conjugation_fr_1307():
    assert (
V("jeter").t('s').pe(2).n('s').realize()   
    ) == 'jettes',\
    'jeter:s2'


def test_conjugation_fr_1308():
    assert (
V("jeter").t('s').pe(3).n('s').realize()   
    ) == 'jette',\
    'jeter:s3'


def test_conjugation_fr_1309():
    assert (
V("jeter").t('s').pe(1).n('p').realize()   
    ) == 'jetions',\
    'jeter:s4'


def test_conjugation_fr_1310():
    assert (
V("jeter").t('s').pe(2).n('p').realize()   
    ) == 'jetiez',\
    'jeter:s5'


def test_conjugation_fr_1311():
    assert (
V("jeter").t('s').pe(3).n('p').realize()   
    ) == 'jettent',\
    'jeter:s6'


def test_conjugation_fr_1312():
    assert (
V("joindre").t('pr').realize()   
    ) == 'joignant',\
    'joindre:pr'


def test_conjugation_fr_1313():
    assert (
V("joindre").t('p').pe(3).n('p').realize()   
    ) == 'joignent',\
    'joindre:p6'


def test_conjugation_fr_1314():
    assert (
V("joindre").t('p').pe(2).n('p').realize()   
    ) == 'joignez',\
    'joindre:p5'


def test_conjugation_fr_1315():
    assert (
V("joindre").t('ip').pe(2).n('p').realize()   
    ) == 'joignez',\
    'joindre:ip5'


def test_conjugation_fr_1316():
    assert (
V("joindre").t('p').pe(1).n('p').realize()   
    ) == 'joignons',\
    'joindre:p4'


def test_conjugation_fr_1317():
    assert (
V("joindre").t('ip').pe(1).n('p').realize()   
    ) == 'joignons',\
    'joindre:ip4'


def test_conjugation_fr_1318():
    assert (
V("joindre").t('p').pe(1).n('s').realize()   
    ) == 'joins',\
    'joindre:p1'


def test_conjugation_fr_1319():
    assert (
V("joindre").t('p').pe(2).n('s').realize()   
    ) == 'joins',\
    'joindre:p2'


def test_conjugation_fr_1320():
    assert (
V("joindre").t('ip').pe(2).n('s').realize()   
    ) == 'joins',\
    'joindre:ip2'


def test_conjugation_fr_1321():
    assert (
V("joindre").t('p').pe(3).n('s').realize()   
    ) == 'joint',\
    'joindre:p3'


def test_conjugation_fr_1322():
    assert (
V("joindre").t('pp').realize()   
    ) == 'joint',\
    'joindre:pp'


def test_conjugation_fr_1323():
    assert (
V("joindre").t('s').pe(1).n('s').realize()   
    ) == 'joigne',\
    'joindre:s1'


def test_conjugation_fr_1324():
    assert (
V("joindre").t('s').pe(2).n('s').realize()   
    ) == 'joignes',\
    'joindre:s2'


def test_conjugation_fr_1325():
    assert (
V("joindre").t('s').pe(3).n('s').realize()   
    ) == 'joigne',\
    'joindre:s3'


def test_conjugation_fr_1326():
    assert (
V("joindre").t('s').pe(1).n('p').realize()   
    ) == 'joignions',\
    'joindre:s4'


def test_conjugation_fr_1327():
    assert (
V("joindre").t('s').pe(2).n('p').realize()   
    ) == 'joigniez',\
    'joindre:s5'


def test_conjugation_fr_1328():
    assert (
V("joindre").t('s').pe(3).n('p').realize()   
    ) == 'joignent',\
    'joindre:s6'


def test_conjugation_fr_1329():
    assert (
V("lire").t('p').pe(1).n('s').realize()   
    ) == 'lis',\
    'lire:p1'


def test_conjugation_fr_1330():
    assert (
V("lire").t('p').pe(2).n('s').realize()   
    ) == 'lis',\
    'lire:p2'


def test_conjugation_fr_1331():
    assert (
V("lire").t('ip').pe(2).n('s').realize()   
    ) == 'lis',\
    'lire:ip2'


def test_conjugation_fr_1332():
    assert (
V("lire").t('pr').realize()   
    ) == 'lisant',\
    'lire:pr'


def test_conjugation_fr_1333():
    assert (
V("lire").t('p').pe(3).n('p').realize()   
    ) == 'lisent',\
    'lire:p6'


def test_conjugation_fr_1334():
    assert (
V("lire").t('p').pe(2).n('p').realize()   
    ) == 'lisez',\
    'lire:p5'


def test_conjugation_fr_1335():
    assert (
V("lire").t('ip').pe(2).n('p').realize()   
    ) == 'lisez',\
    'lire:ip5'


def test_conjugation_fr_1336():
    assert (
V("lire").t('p').pe(1).n('p').realize()   
    ) == 'lisons',\
    'lire:p4'


def test_conjugation_fr_1337():
    assert (
V("lire").t('ip').pe(1).n('p').realize()   
    ) == 'lisons',\
    'lire:ip4'


def test_conjugation_fr_1338():
    assert (
V("lire").t('p').pe(3).n('s').realize()   
    ) == 'lit',\
    'lire:p3'


def test_conjugation_fr_1339():
    assert (
V("lire").t('pp').realize()   
    ) == 'lu',\
    'lire:pp'


def test_conjugation_fr_1340():
    assert (
V("lire").t('s').pe(1).n('s').realize()   
    ) == 'lise',\
    'lire:s1'


def test_conjugation_fr_1341():
    assert (
V("lire").t('s').pe(2).n('s').realize()   
    ) == 'lises',\
    'lire:s2'


def test_conjugation_fr_1342():
    assert (
V("lire").t('s').pe(3).n('s').realize()   
    ) == 'lise',\
    'lire:s3'


def test_conjugation_fr_1343():
    assert (
V("lire").t('s').pe(1).n('p').realize()   
    ) == 'lisions',\
    'lire:s4'


def test_conjugation_fr_1344():
    assert (
V("lire").t('s').pe(2).n('p').realize()   
    ) == 'lisiez',\
    'lire:s5'


def test_conjugation_fr_1345():
    assert (
V("lire").t('s').pe(3).n('p').realize()   
    ) == 'lisent',\
    'lire:s6'


def test_conjugation_fr_1346():
    assert (
V("luire").t('p').pe(1).n('s').realize()   
    ) == 'luis',\
    'luire:p1'


def test_conjugation_fr_1347():
    assert (
V("luire").t('p').pe(2).n('s').realize()   
    ) == 'luis',\
    'luire:p2'


def test_conjugation_fr_1348():
    assert (
V("luire").t('ip').pe(2).n('s').realize()   
    ) == 'luis',\
    'luire:ip2'


def test_conjugation_fr_1349():
    assert (
V("luire").t('pr').realize()   
    ) == 'luisant',\
    'luire:pr'


def test_conjugation_fr_1350():
    assert (
V("luire").t('p').pe(3).n('p').realize()   
    ) == 'luisent',\
    'luire:p6'


def test_conjugation_fr_1351():
    assert (
V("luire").t('p').pe(2).n('p').realize()   
    ) == 'luisez',\
    'luire:p5'


def test_conjugation_fr_1352():
    assert (
V("luire").t('ip').pe(2).n('p').realize()   
    ) == 'luisez',\
    'luire:ip5'


def test_conjugation_fr_1353():
    assert (
V("luire").t('p').pe(1).n('p').realize()   
    ) == 'luisons',\
    'luire:p4'


def test_conjugation_fr_1354():
    assert (
V("luire").t('ip').pe(1).n('p').realize()   
    ) == 'luisons',\
    'luire:ip4'


def test_conjugation_fr_1355():
    assert (
V("luire").t('p').pe(3).n('s').realize()   
    ) == 'luit',\
    'luire:p3'


def test_conjugation_fr_1356():
    assert (
V("luire").t('s').pe(1).n('s').realize()   
    ) == 'luise',\
    'luire:s1'


def test_conjugation_fr_1357():
    assert (
V("luire").t('s').pe(2).n('s').realize()   
    ) == 'luises',\
    'luire:s2'


def test_conjugation_fr_1358():
    assert (
V("luire").t('s').pe(3).n('s').realize()   
    ) == 'luise',\
    'luire:s3'


def test_conjugation_fr_1359():
    assert (
V("luire").t('s').pe(1).n('p').realize()   
    ) == 'luisions',\
    'luire:s4'


def test_conjugation_fr_1360():
    assert (
V("luire").t('s').pe(2).n('p').realize()   
    ) == 'luisiez',\
    'luire:s5'


def test_conjugation_fr_1361():
    assert (
V("luire").t('s').pe(3).n('p').realize()   
    ) == 'luisent',\
    'luire:s6'


def test_conjugation_fr_1362():
    assert (
V("maintenir").t('pr').realize()   
    ) == 'maintenant',\
    'maintenir:pr'


def test_conjugation_fr_1363():
    assert (
V("maintenir").t('p').pe(2).n('p').realize()   
    ) == 'maintenez',\
    'maintenir:p5'


def test_conjugation_fr_1364():
    assert (
V("maintenir").t('ip').pe(2).n('p').realize()   
    ) == 'maintenez',\
    'maintenir:ip5'


def test_conjugation_fr_1365():
    assert (
V("maintenir").t('p').pe(1).n('p').realize()   
    ) == 'maintenons',\
    'maintenir:p4'


def test_conjugation_fr_1366():
    assert (
V("maintenir").t('ip').pe(1).n('p').realize()   
    ) == 'maintenons',\
    'maintenir:ip4'


def test_conjugation_fr_1367():
    assert (
V("maintenir").t('p').pe(3).n('p').realize()   
    ) == 'maintiennent',\
    'maintenir:p6'


def test_conjugation_fr_1368():
    assert (
V("maintenir").t('p').pe(1).n('s').realize()   
    ) == 'maintiens',\
    'maintenir:p1'


def test_conjugation_fr_1369():
    assert (
V("maintenir").t('p').pe(2).n('s').realize()   
    ) == 'maintiens',\
    'maintenir:p2'


def test_conjugation_fr_1370():
    assert (
V("maintenir").t('ip').pe(2).n('s').realize()   
    ) == 'maintiens',\
    'maintenir:ip2'


def test_conjugation_fr_1371():
    assert (
V("maintenir").t('p').pe(3).n('s').realize()   
    ) == 'maintient',\
    'maintenir:p3'


def test_conjugation_fr_1372():
    assert (
V("maintenir").t('pp').realize()   
    ) == 'maintenu',\
    'maintenir:pp'


def test_conjugation_fr_1373():
    assert (
V("maintenir").t('s').pe(1).n('s').realize()   
    ) == 'maintienne',\
    'maintenir:s1'


def test_conjugation_fr_1374():
    assert (
V("maintenir").t('s').pe(2).n('s').realize()   
    ) == 'maintiennes',\
    'maintenir:s2'


def test_conjugation_fr_1375():
    assert (
V("maintenir").t('s').pe(3).n('s').realize()   
    ) == 'maintienne',\
    'maintenir:s3'


def test_conjugation_fr_1376():
    assert (
V("maintenir").t('s').pe(1).n('p').realize()   
    ) == 'maintenions',\
    'maintenir:s4'


def test_conjugation_fr_1377():
    assert (
V("maintenir").t('s').pe(2).n('p').realize()   
    ) == 'mainteniez',\
    'maintenir:s5'


def test_conjugation_fr_1378():
    assert (
V("maintenir").t('s').pe(3).n('p').realize()   
    ) == 'maintiennent',\
    'maintenir:s6'


def test_conjugation_fr_1379():
    assert (
V("maudire").t('p').pe(1).n('s').realize()   
    ) == 'maudis',\
    'maudire:p1'


def test_conjugation_fr_1380():
    assert (
V("maudire").t('p').pe(2).n('s').realize()   
    ) == 'maudis',\
    'maudire:p2'


def test_conjugation_fr_1381():
    assert (
V("maudire").t('ip').pe(2).n('s').realize()   
    ) == 'maudis',\
    'maudire:ip2'


def test_conjugation_fr_1382():
    assert (
V("maudire").t('pr').realize()   
    ) == 'maudissant',\
    'maudire:pr'


def test_conjugation_fr_1383():
    assert (
V("maudire").t('p').pe(3).n('p').realize()   
    ) == 'maudissent',\
    'maudire:p6'


def test_conjugation_fr_1384():
    assert (
V("maudire").t('p').pe(2).n('p').realize()   
    ) == 'maudissez',\
    'maudire:p5'


def test_conjugation_fr_1385():
    assert (
V("maudire").t('ip').pe(2).n('p').realize()   
    ) == 'maudissez',\
    'maudire:ip5'


def test_conjugation_fr_1386():
    assert (
V("maudire").t('p').pe(1).n('p').realize()   
    ) == 'maudissons',\
    'maudire:p4'


def test_conjugation_fr_1387():
    assert (
V("maudire").t('ip').pe(1).n('p').realize()   
    ) == 'maudissons',\
    'maudire:ip4'


def test_conjugation_fr_1388():
    assert (
V("maudire").t('p').pe(3).n('s').realize()   
    ) == 'maudit',\
    'maudire:p3'


def test_conjugation_fr_1389():
    assert (
V("maudire").t('pp').realize()   
    ) == 'maudit',\
    'maudire:pp'


def test_conjugation_fr_1390():
    assert (
V("maudire").t('s').pe(1).n('s').realize()   
    ) == 'maudisse',\
    'maudire:s1'


def test_conjugation_fr_1391():
    assert (
V("maudire").t('s').pe(2).n('s').realize()   
    ) == 'maudisses',\
    'maudire:s2'


def test_conjugation_fr_1392():
    assert (
V("maudire").t('s').pe(3).n('s').realize()   
    ) == 'maudisse',\
    'maudire:s3'


def test_conjugation_fr_1393():
    assert (
V("maudire").t('s').pe(1).n('p').realize()   
    ) == 'maudissions',\
    'maudire:s4'


def test_conjugation_fr_1394():
    assert (
V("maudire").t('s').pe(2).n('p').realize()   
    ) == 'maudissiez',\
    'maudire:s5'


def test_conjugation_fr_1395():
    assert (
V("maudire").t('s').pe(3).n('p').realize()   
    ) == 'maudissent',\
    'maudire:s6'


def test_conjugation_fr_1396():
    assert (
V("mentir").t('p').pe(1).n('s').realize()   
    ) == 'mens',\
    'mentir:p1'


def test_conjugation_fr_1397():
    assert (
V("mentir").t('p').pe(2).n('s').realize()   
    ) == 'mens',\
    'mentir:p2'


def test_conjugation_fr_1398():
    assert (
V("mentir").t('ip').pe(2).n('s').realize()   
    ) == 'mens',\
    'mentir:ip2'


def test_conjugation_fr_1399():
    assert (
V("mentir").t('p').pe(3).n('s').realize()   
    ) == 'ment',\
    'mentir:p3'


def test_conjugation_fr_1400():
    assert (
V("mentir").t('pr').realize()   
    ) == 'mentant',\
    'mentir:pr'


def test_conjugation_fr_1401():
    assert (
V("mentir").t('p').pe(3).n('p').realize()   
    ) == 'mentent',\
    'mentir:p6'


def test_conjugation_fr_1402():
    assert (
V("mentir").t('p').pe(2).n('p').realize()   
    ) == 'mentez',\
    'mentir:p5'


def test_conjugation_fr_1403():
    assert (
V("mentir").t('ip').pe(2).n('p').realize()   
    ) == 'mentez',\
    'mentir:ip5'


def test_conjugation_fr_1404():
    assert (
V("mentir").t('p').pe(1).n('p').realize()   
    ) == 'mentons',\
    'mentir:p4'


def test_conjugation_fr_1405():
    assert (
V("mentir").t('ip').pe(1).n('p').realize()   
    ) == 'mentons',\
    'mentir:ip4'


def test_conjugation_fr_1406():
    assert (
V("mentir").t('pp').realize()   
    ) == 'menti',\
    'mentir:pp'


def test_conjugation_fr_1407():
    assert (
V("mentir").t('s').pe(1).n('s').realize()   
    ) == 'mente',\
    'mentir:s1'


def test_conjugation_fr_1408():
    assert (
V("mentir").t('s').pe(2).n('s').realize()   
    ) == 'mentes',\
    'mentir:s2'


def test_conjugation_fr_1409():
    assert (
V("mentir").t('s').pe(3).n('s').realize()   
    ) == 'mente',\
    'mentir:s3'


def test_conjugation_fr_1410():
    assert (
V("mentir").t('s').pe(1).n('p').realize()   
    ) == 'mentions',\
    'mentir:s4'


def test_conjugation_fr_1411():
    assert (
V("mentir").t('s').pe(2).n('p').realize()   
    ) == 'mentiez',\
    'mentir:s5'


def test_conjugation_fr_1412():
    assert (
V("mentir").t('s').pe(3).n('p').realize()   
    ) == 'mentent',\
    'mentir:s6'


def test_conjugation_fr_1413():
    assert (
V("mettre").t('p').pe(3).n('s').realize()   
    ) == 'met',\
    'mettre:p3'


def test_conjugation_fr_1414():
    assert (
V("mettre").t('p').pe(1).n('s').realize()   
    ) == 'mets',\
    'mettre:p1'


def test_conjugation_fr_1415():
    assert (
V("mettre").t('p').pe(2).n('s').realize()   
    ) == 'mets',\
    'mettre:p2'


def test_conjugation_fr_1416():
    assert (
V("mettre").t('ip').pe(2).n('s').realize()   
    ) == 'mets',\
    'mettre:ip2'


def test_conjugation_fr_1417():
    assert (
V("mettre").t('pr').realize()   
    ) == 'mettant',\
    'mettre:pr'


def test_conjugation_fr_1418():
    assert (
V("mettre").t('p').pe(3).n('p').realize()   
    ) == 'mettent',\
    'mettre:p6'


def test_conjugation_fr_1419():
    assert (
V("mettre").t('p').pe(2).n('p').realize()   
    ) == 'mettez',\
    'mettre:p5'


def test_conjugation_fr_1420():
    assert (
V("mettre").t('ip').pe(2).n('p').realize()   
    ) == 'mettez',\
    'mettre:ip5'


def test_conjugation_fr_1421():
    assert (
V("mettre").t('p').pe(1).n('p').realize()   
    ) == 'mettons',\
    'mettre:p4'


def test_conjugation_fr_1422():
    assert (
V("mettre").t('ip').pe(1).n('p').realize()   
    ) == 'mettons',\
    'mettre:ip4'


def test_conjugation_fr_1423():
    assert (
V("mettre").t('pp').realize()   
    ) == 'mis',\
    'mettre:pp'


def test_conjugation_fr_1424():
    assert (
V("mettre").t('s').pe(1).n('s').realize()   
    ) == 'mette',\
    'mettre:s1'


def test_conjugation_fr_1425():
    assert (
V("mettre").t('s').pe(2).n('s').realize()   
    ) == 'mettes',\
    'mettre:s2'


def test_conjugation_fr_1426():
    assert (
V("mettre").t('s').pe(3).n('s').realize()   
    ) == 'mette',\
    'mettre:s3'


def test_conjugation_fr_1427():
    assert (
V("mettre").t('s').pe(1).n('p').realize()   
    ) == 'mettions',\
    'mettre:s4'


def test_conjugation_fr_1428():
    assert (
V("mettre").t('s').pe(2).n('p').realize()   
    ) == 'mettiez',\
    'mettre:s5'


def test_conjugation_fr_1429():
    assert (
V("mettre").t('s').pe(3).n('p').realize()   
    ) == 'mettent',\
    'mettre:s6'


def test_conjugation_fr_1430():
    assert (
V("mordre").t('p').pe(3).n('s').realize()   
    ) == 'mord',\
    'mordre:p3'


def test_conjugation_fr_1431():
    assert (
V("mordre").t('pr').realize()   
    ) == 'mordant',\
    'mordre:pr'


def test_conjugation_fr_1432():
    assert (
V("mordre").t('p').pe(3).n('p').realize()   
    ) == 'mordent',\
    'mordre:p6'


def test_conjugation_fr_1433():
    assert (
V("mordre").t('p').pe(2).n('p').realize()   
    ) == 'mordez',\
    'mordre:p5'


def test_conjugation_fr_1434():
    assert (
V("mordre").t('ip').pe(2).n('p').realize()   
    ) == 'mordez',\
    'mordre:ip5'


def test_conjugation_fr_1435():
    assert (
V("mordre").t('p').pe(1).n('p').realize()   
    ) == 'mordons',\
    'mordre:p4'


def test_conjugation_fr_1436():
    assert (
V("mordre").t('ip').pe(1).n('p').realize()   
    ) == 'mordons',\
    'mordre:ip4'


def test_conjugation_fr_1437():
    assert (
V("mordre").t('p').pe(1).n('s').realize()   
    ) == 'mords',\
    'mordre:p1'


def test_conjugation_fr_1438():
    assert (
V("mordre").t('p').pe(2).n('s').realize()   
    ) == 'mords',\
    'mordre:p2'


def test_conjugation_fr_1439():
    assert (
V("mordre").t('ip').pe(2).n('s').realize()   
    ) == 'mords',\
    'mordre:ip2'


def test_conjugation_fr_1440():
    assert (
V("mordre").t('pp').realize()   
    ) == 'mordu',\
    'mordre:pp'


def test_conjugation_fr_1441():
    assert (
V("mordre").t('s').pe(1).n('s').realize()   
    ) == 'morde',\
    'mordre:s1'


def test_conjugation_fr_1442():
    assert (
V("mordre").t('s').pe(2).n('s').realize()   
    ) == 'mordes',\
    'mordre:s2'


def test_conjugation_fr_1443():
    assert (
V("mordre").t('s').pe(3).n('s').realize()   
    ) == 'morde',\
    'mordre:s3'


def test_conjugation_fr_1444():
    assert (
V("mordre").t('s').pe(1).n('p').realize()   
    ) == 'mordions',\
    'mordre:s4'


def test_conjugation_fr_1445():
    assert (
V("mordre").t('s').pe(2).n('p').realize()   
    ) == 'mordiez',\
    'mordre:s5'


def test_conjugation_fr_1446():
    assert (
V("mordre").t('s').pe(3).n('p').realize()   
    ) == 'mordent',\
    'mordre:s6'


def test_conjugation_fr_1447():
    assert (
V("moudre").t('p').pe(3).n('s').realize()   
    ) == 'moud',\
    'moudre:p3'


def test_conjugation_fr_1448():
    assert (
V("moudre").t('p').pe(1).n('s').realize()   
    ) == 'mouds',\
    'moudre:p1'


def test_conjugation_fr_1449():
    assert (
V("moudre").t('p').pe(2).n('s').realize()   
    ) == 'mouds',\
    'moudre:p2'


def test_conjugation_fr_1450():
    assert (
V("moudre").t('ip').pe(2).n('s').realize()   
    ) == 'mouds',\
    'moudre:ip2'


def test_conjugation_fr_1451():
    assert (
V("moudre").t('pr').realize()   
    ) == 'moulant',\
    'moudre:pr'


def test_conjugation_fr_1452():
    assert (
V("moudre").t('p').pe(3).n('p').realize()   
    ) == 'moulent',\
    'moudre:p6'


def test_conjugation_fr_1453():
    assert (
V("moudre").t('p').pe(2).n('p').realize()   
    ) == 'moulez',\
    'moudre:p5'


def test_conjugation_fr_1454():
    assert (
V("moudre").t('ip').pe(2).n('p').realize()   
    ) == 'moulez',\
    'moudre:ip5'


def test_conjugation_fr_1455():
    assert (
V("moudre").t('p').pe(1).n('p').realize()   
    ) == 'moulons',\
    'moudre:p4'


def test_conjugation_fr_1456():
    assert (
V("moudre").t('ip').pe(1).n('p').realize()   
    ) == 'moulons',\
    'moudre:ip4'


def test_conjugation_fr_1457():
    assert (
V("moudre").t('pp').realize()   
    ) == 'moulu',\
    'moudre:pp'


def test_conjugation_fr_1458():
    assert (
V("moudre").t('s').pe(1).n('s').realize()   
    ) == 'moule',\
    'moudre:s1'


def test_conjugation_fr_1459():
    assert (
V("moudre").t('s').pe(2).n('s').realize()   
    ) == 'moules',\
    'moudre:s2'


def test_conjugation_fr_1460():
    assert (
V("moudre").t('s').pe(3).n('s').realize()   
    ) == 'moule',\
    'moudre:s3'


def test_conjugation_fr_1461():
    assert (
V("moudre").t('s').pe(1).n('p').realize()   
    ) == 'moulions',\
    'moudre:s4'


def test_conjugation_fr_1462():
    assert (
V("moudre").t('s').pe(2).n('p').realize()   
    ) == 'mouliez',\
    'moudre:s5'


def test_conjugation_fr_1463():
    assert (
V("moudre").t('s').pe(3).n('p').realize()   
    ) == 'moulent',\
    'moudre:s6'


def test_conjugation_fr_1464():
    assert (
V("mourir").t('p').pe(3).n('p').realize()   
    ) == 'meurent',\
    'mourir:p6'


def test_conjugation_fr_1465():
    assert (
V("mourir").t('p').pe(1).n('s').realize()   
    ) == 'meurs',\
    'mourir:p1'


def test_conjugation_fr_1466():
    assert (
V("mourir").t('p').pe(2).n('s').realize()   
    ) == 'meurs',\
    'mourir:p2'


def test_conjugation_fr_1467():
    assert (
V("mourir").t('ip').pe(2).n('s').realize()   
    ) == 'meurs',\
    'mourir:ip2'


def test_conjugation_fr_1468():
    assert (
V("mourir").t('p').pe(3).n('s').realize()   
    ) == 'meurt',\
    'mourir:p3'


def test_conjugation_fr_1469():
    assert (
V("mourir").t('pr').realize()   
    ) == 'mourant',\
    'mourir:pr'


def test_conjugation_fr_1470():
    assert (
V("mourir").t('p').pe(2).n('p').realize()   
    ) == 'mourez',\
    'mourir:p5'


def test_conjugation_fr_1471():
    assert (
V("mourir").t('ip').pe(2).n('p').realize()   
    ) == 'mourez',\
    'mourir:ip5'


def test_conjugation_fr_1472():
    assert (
V("mourir").t('p').pe(1).n('p').realize()   
    ) == 'mourons',\
    'mourir:p4'


def test_conjugation_fr_1473():
    assert (
V("mourir").t('ip').pe(1).n('p').realize()   
    ) == 'mourons',\
    'mourir:ip4'


def test_conjugation_fr_1474():
    assert (
V("mourir").t('pp').realize()   
    ) == 'mort',\
    'mourir:pp'


def test_conjugation_fr_1475():
    assert (
V("mourir").t('s').pe(1).n('s').realize()   
    ) == 'meure',\
    'mourir:s1'


def test_conjugation_fr_1476():
    assert (
V("mourir").t('s').pe(2).n('s').realize()   
    ) == 'meures',\
    'mourir:s2'


def test_conjugation_fr_1477():
    assert (
V("mourir").t('s').pe(3).n('s').realize()   
    ) == 'meure',\
    'mourir:s3'


def test_conjugation_fr_1478():
    assert (
V("mourir").t('s').pe(1).n('p').realize()   
    ) == 'mourions',\
    'mourir:s4'


def test_conjugation_fr_1479():
    assert (
V("mourir").t('s').pe(2).n('p').realize()   
    ) == 'mouriez',\
    'mourir:s5'


def test_conjugation_fr_1480():
    assert (
V("mourir").t('s').pe(3).n('p').realize()   
    ) == 'meurent',\
    'mourir:s6'


def test_conjugation_fr_1481():
    assert (
V("mouvoir").t('p').pe(1).n('s').realize()   
    ) == 'meus',\
    'mouvoir:p1'


def test_conjugation_fr_1482():
    assert (
V("mouvoir").t('p').pe(2).n('s').realize()   
    ) == 'meus',\
    'mouvoir:p2'


def test_conjugation_fr_1483():
    assert (
V("mouvoir").t('ip').pe(2).n('s').realize()   
    ) == 'meus',\
    'mouvoir:ip2'


def test_conjugation_fr_1484():
    assert (
V("mouvoir").t('p').pe(3).n('s').realize()   
    ) == 'meut',\
    'mouvoir:p3'


def test_conjugation_fr_1485():
    assert (
V("mouvoir").t('p').pe(3).n('p').realize()   
    ) == 'meuvent',\
    'mouvoir:p6'


def test_conjugation_fr_1486():
    assert (
V("mouvoir").t('pr').realize()   
    ) == 'mouvant',\
    'mouvoir:pr'


def test_conjugation_fr_1487():
    assert (
V("mouvoir").t('p').pe(2).n('p').realize()   
    ) == 'mouvez',\
    'mouvoir:p5'


def test_conjugation_fr_1488():
    assert (
V("mouvoir").t('ip').pe(2).n('p').realize()   
    ) == 'mouvez',\
    'mouvoir:ip5'


def test_conjugation_fr_1489():
    assert (
V("mouvoir").t('p').pe(1).n('p').realize()   
    ) == 'mouvons',\
    'mouvoir:p4'


def test_conjugation_fr_1490():
    assert (
V("mouvoir").t('ip').pe(1).n('p').realize()   
    ) == 'mouvons',\
    'mouvoir:ip4'


def test_conjugation_fr_1491():
    assert (
V("mouvoir").t('pp').realize()   
    ) == 'mu',\
    'mouvoir:pp'


def test_conjugation_fr_1492():
    assert (
V("mouvoir").t('s').pe(1).n('s').realize()   
    ) == 'meuve',\
    'mouvoir:s1'


def test_conjugation_fr_1493():
    assert (
V("mouvoir").t('s').pe(2).n('s').realize()   
    ) == 'meuves',\
    'mouvoir:s2'


def test_conjugation_fr_1494():
    assert (
V("mouvoir").t('s').pe(3).n('s').realize()   
    ) == 'meuve',\
    'mouvoir:s3'


def test_conjugation_fr_1495():
    assert (
V("mouvoir").t('s').pe(1).n('p').realize()   
    ) == 'mouvions',\
    'mouvoir:s4'


def test_conjugation_fr_1496():
    assert (
V("mouvoir").t('s').pe(2).n('p').realize()   
    ) == 'mouviez',\
    'mouvoir:s5'


def test_conjugation_fr_1497():
    assert (
V("mouvoir").t('s').pe(3).n('p').realize()   
    ) == 'meuvent',\
    'mouvoir:s6'


def test_conjugation_fr_1498():
    assert (
V("naître").t('p').pe(1).n('s').realize()   
    ) == 'nais',\
    'naître:p1'


def test_conjugation_fr_1499():
    assert (
V("naître").t('p').pe(2).n('s').realize()   
    ) == 'nais',\
    'naître:p2'


def test_conjugation_fr_1500():
    assert (
V("naître").t('ip').pe(2).n('s').realize()   
    ) == 'nais',\
    'naître:ip2'


def test_conjugation_fr_1501():
    assert (
V("naître").t('pr').realize()   
    ) == 'naissant',\
    'naître:pr'


def test_conjugation_fr_1502():
    assert (
V("naître").t('p').pe(3).n('p').realize()   
    ) == 'naissent',\
    'naître:p6'


def test_conjugation_fr_1503():
    assert (
V("naître").t('p').pe(2).n('p').realize()   
    ) == 'naissez',\
    'naître:p5'


def test_conjugation_fr_1504():
    assert (
V("naître").t('ip').pe(2).n('p').realize()   
    ) == 'naissez',\
    'naître:ip5'


def test_conjugation_fr_1505():
    assert (
V("naître").t('p').pe(1).n('p').realize()   
    ) == 'naissons',\
    'naître:p4'


def test_conjugation_fr_1506():
    assert (
V("naître").t('ip').pe(1).n('p').realize()   
    ) == 'naissons',\
    'naître:ip4'


def test_conjugation_fr_1507():
    assert (
V("naître").t('p').pe(3).n('s').realize()   
    ) == 'naît',\
    'naître:p3'


def test_conjugation_fr_1508():
    assert (
V("naître").t('pp').realize()   
    ) == 'né',\
    'naître:pp'


def test_conjugation_fr_1509():
    assert (
V("naître").t('s').pe(1).n('s').realize()   
    ) == 'naisse',\
    'naître:s1'


def test_conjugation_fr_1510():
    assert (
V("naître").t('s').pe(2).n('s').realize()   
    ) == 'naisses',\
    'naître:s2'


def test_conjugation_fr_1511():
    assert (
V("naître").t('s').pe(3).n('s').realize()   
    ) == 'naisse',\
    'naître:s3'


def test_conjugation_fr_1512():
    assert (
V("naître").t('s').pe(1).n('p').realize()   
    ) == 'naissions',\
    'naître:s4'


def test_conjugation_fr_1513():
    assert (
V("naître").t('s').pe(2).n('p').realize()   
    ) == 'naissiez',\
    'naître:s5'


def test_conjugation_fr_1514():
    assert (
V("naître").t('s').pe(3).n('p').realize()   
    ) == 'naissent',\
    'naître:s6'


def test_conjugation_fr_1515():
    assert (
V("obtenir").t('pr').realize()   
    ) == 'obtenant',\
    'obtenir:pr'


def test_conjugation_fr_1516():
    assert (
V("obtenir").t('p').pe(2).n('p').realize()   
    ) == 'obtenez',\
    'obtenir:p5'


def test_conjugation_fr_1517():
    assert (
V("obtenir").t('ip').pe(2).n('p').realize()   
    ) == 'obtenez',\
    'obtenir:ip5'


def test_conjugation_fr_1518():
    assert (
V("obtenir").t('p').pe(1).n('p').realize()   
    ) == 'obtenons',\
    'obtenir:p4'


def test_conjugation_fr_1519():
    assert (
V("obtenir").t('ip').pe(1).n('p').realize()   
    ) == 'obtenons',\
    'obtenir:ip4'


def test_conjugation_fr_1520():
    assert (
V("obtenir").t('p').pe(3).n('p').realize()   
    ) == 'obtiennent',\
    'obtenir:p6'


def test_conjugation_fr_1521():
    assert (
V("obtenir").t('p').pe(1).n('s').realize()   
    ) == 'obtiens',\
    'obtenir:p1'


def test_conjugation_fr_1522():
    assert (
V("obtenir").t('p').pe(2).n('s').realize()   
    ) == 'obtiens',\
    'obtenir:p2'


def test_conjugation_fr_1523():
    assert (
V("obtenir").t('ip').pe(2).n('s').realize()   
    ) == 'obtiens',\
    'obtenir:ip2'


def test_conjugation_fr_1524():
    assert (
V("obtenir").t('p').pe(3).n('s').realize()   
    ) == 'obtient',\
    'obtenir:p3'


def test_conjugation_fr_1525():
    assert (
V("obtenir").t('pp').realize()   
    ) == 'obtenu',\
    'obtenir:pp'


def test_conjugation_fr_1526():
    assert (
V("obtenir").t('s').pe(1).n('s').realize()   
    ) == 'obtienne',\
    'obtenir:s1'


def test_conjugation_fr_1527():
    assert (
V("obtenir").t('s').pe(2).n('s').realize()   
    ) == 'obtiennes',\
    'obtenir:s2'


def test_conjugation_fr_1528():
    assert (
V("obtenir").t('s').pe(3).n('s').realize()   
    ) == 'obtienne',\
    'obtenir:s3'


def test_conjugation_fr_1529():
    assert (
V("obtenir").t('s').pe(1).n('p').realize()   
    ) == 'obtenions',\
    'obtenir:s4'


def test_conjugation_fr_1530():
    assert (
V("obtenir").t('s').pe(2).n('p').realize()   
    ) == 'obteniez',\
    'obtenir:s5'


def test_conjugation_fr_1531():
    assert (
V("obtenir").t('s').pe(3).n('p').realize()   
    ) == 'obtiennent',\
    'obtenir:s6'


def test_conjugation_fr_1532():
    assert (
V("offrir").t('pr').realize()   
    ) == 'offrant',\
    'offrir:pr'


def test_conjugation_fr_1533():
    assert (
V("offrir").t('p').pe(1).n('s').realize()   
    ) == 'offre',\
    'offrir:p1'


def test_conjugation_fr_1534():
    assert (
V("offrir").t('p').pe(3).n('s').realize()   
    ) == 'offre',\
    'offrir:p3'


def test_conjugation_fr_1535():
    assert (
V("offrir").t('ip').pe(2).n('s').realize()   
    ) == 'offre',\
    'offrir:ip2'


def test_conjugation_fr_1536():
    assert (
V("offrir").t('p').pe(3).n('p').realize()   
    ) == 'offrent',\
    'offrir:p6'


def test_conjugation_fr_1537():
    assert (
V("offrir").t('p').pe(2).n('s').realize()   
    ) == 'offres',\
    'offrir:p2'


def test_conjugation_fr_1538():
    assert (
V("offrir").t('p').pe(2).n('p').realize()   
    ) == 'offrez',\
    'offrir:p5'


def test_conjugation_fr_1539():
    assert (
V("offrir").t('ip').pe(2).n('p').realize()   
    ) == 'offrez',\
    'offrir:ip5'


def test_conjugation_fr_1540():
    assert (
V("offrir").t('p').pe(1).n('p').realize()   
    ) == 'offrons',\
    'offrir:p4'


def test_conjugation_fr_1541():
    assert (
V("offrir").t('ip').pe(1).n('p').realize()   
    ) == 'offrons',\
    'offrir:ip4'


def test_conjugation_fr_1542():
    assert (
V("offrir").t('pp').realize()   
    ) == 'offert',\
    'offrir:pp'


def test_conjugation_fr_1543():
    assert (
V("offrir").t('s').pe(1).n('s').realize()   
    ) == 'offre',\
    'offrir:s1'


def test_conjugation_fr_1544():
    assert (
V("offrir").t('s').pe(2).n('s').realize()   
    ) == 'offres',\
    'offrir:s2'


def test_conjugation_fr_1545():
    assert (
V("offrir").t('s').pe(3).n('s').realize()   
    ) == 'offre',\
    'offrir:s3'


def test_conjugation_fr_1546():
    assert (
V("offrir").t('s').pe(1).n('p').realize()   
    ) == 'offrions',\
    'offrir:s4'


def test_conjugation_fr_1547():
    assert (
V("offrir").t('s').pe(2).n('p').realize()   
    ) == 'offriez',\
    'offrir:s5'


def test_conjugation_fr_1548():
    assert (
V("offrir").t('s').pe(3).n('p').realize()   
    ) == 'offrent',\
    'offrir:s6'


def test_conjugation_fr_1549():
    assert (
V("ouvrir").t('pr').realize()   
    ) == 'ouvrant',\
    'ouvrir:pr'


def test_conjugation_fr_1550():
    assert (
V("ouvrir").t('p').pe(1).n('s').realize()   
    ) == 'ouvre',\
    'ouvrir:p1'


def test_conjugation_fr_1551():
    assert (
V("ouvrir").t('p').pe(3).n('s').realize()   
    ) == 'ouvre',\
    'ouvrir:p3'


def test_conjugation_fr_1552():
    assert (
V("ouvrir").t('ip').pe(2).n('s').realize()   
    ) == 'ouvre',\
    'ouvrir:ip2'


def test_conjugation_fr_1553():
    assert (
V("ouvrir").t('p').pe(3).n('p').realize()   
    ) == 'ouvrent',\
    'ouvrir:p6'


def test_conjugation_fr_1554():
    assert (
V("ouvrir").t('p').pe(2).n('s').realize()   
    ) == 'ouvres',\
    'ouvrir:p2'


def test_conjugation_fr_1555():
    assert (
V("ouvrir").t('p').pe(2).n('p').realize()   
    ) == 'ouvrez',\
    'ouvrir:p5'


def test_conjugation_fr_1556():
    assert (
V("ouvrir").t('ip').pe(2).n('p').realize()   
    ) == 'ouvrez',\
    'ouvrir:ip5'


def test_conjugation_fr_1557():
    assert (
V("ouvrir").t('p').pe(1).n('p').realize()   
    ) == 'ouvrons',\
    'ouvrir:p4'


def test_conjugation_fr_1558():
    assert (
V("ouvrir").t('ip').pe(1).n('p').realize()   
    ) == 'ouvrons',\
    'ouvrir:ip4'


def test_conjugation_fr_1559():
    assert (
V("ouvrir").t('pp').realize()   
    ) == 'ouvert',\
    'ouvrir:pp'


def test_conjugation_fr_1560():
    assert (
V("ouvrir").t('s').pe(1).n('s').realize()   
    ) == 'ouvre',\
    'ouvrir:s1'


def test_conjugation_fr_1561():
    assert (
V("ouvrir").t('s').pe(2).n('s').realize()   
    ) == 'ouvres',\
    'ouvrir:s2'


def test_conjugation_fr_1562():
    assert (
V("ouvrir").t('s').pe(3).n('s').realize()   
    ) == 'ouvre',\
    'ouvrir:s3'


def test_conjugation_fr_1563():
    assert (
V("ouvrir").t('s').pe(1).n('p').realize()   
    ) == 'ouvrions',\
    'ouvrir:s4'


def test_conjugation_fr_1564():
    assert (
V("ouvrir").t('s').pe(2).n('p').realize()   
    ) == 'ouvriez',\
    'ouvrir:s5'


def test_conjugation_fr_1565():
    assert (
V("ouvrir").t('s').pe(3).n('p').realize()   
    ) == 'ouvrent',\
    'ouvrir:s6'


def test_conjugation_fr_1566():
    assert (
V("paître").t('p').pe(1).n('s').realize()   
    ) == 'pais',\
    'paître:p1'


def test_conjugation_fr_1567():
    assert (
V("paître").t('p').pe(2).n('s').realize()   
    ) == 'pais',\
    'paître:p2'


def test_conjugation_fr_1568():
    assert (
V("paître").t('ip').pe(2).n('s').realize()   
    ) == 'pais',\
    'paître:ip2'


def test_conjugation_fr_1569():
    assert (
V("paître").t('pr').realize()   
    ) == 'paissant',\
    'paître:pr'


def test_conjugation_fr_1570():
    assert (
V("paître").t('p').pe(3).n('p').realize()   
    ) == 'paissent',\
    'paître:p6'


def test_conjugation_fr_1571():
    assert (
V("paître").t('p').pe(2).n('p').realize()   
    ) == 'paissez',\
    'paître:p5'


def test_conjugation_fr_1572():
    assert (
V("paître").t('ip').pe(2).n('p').realize()   
    ) == 'paissez',\
    'paître:ip5'


def test_conjugation_fr_1573():
    assert (
V("paître").t('p').pe(1).n('p').realize()   
    ) == 'paissons',\
    'paître:p4'


def test_conjugation_fr_1574():
    assert (
V("paître").t('p').pe(3).n('s').realize()   
    ) == 'paît',\
    'paître:p3'


def test_conjugation_fr_1575():
    assert (
V("paître").t('s').pe(1).n('s').realize()   
    ) == 'paisse',\
    'paître:s1'


def test_conjugation_fr_1576():
    assert (
V("paître").t('s').pe(2).n('s').realize()   
    ) == 'paisses',\
    'paître:s2'


def test_conjugation_fr_1577():
    assert (
V("paître").t('s').pe(3).n('s').realize()   
    ) == 'paisse',\
    'paître:s3'


def test_conjugation_fr_1578():
    assert (
V("paître").t('s').pe(1).n('p').realize()   
    ) == 'paissions',\
    'paître:s4'


def test_conjugation_fr_1579():
    assert (
V("paître").t('s').pe(2).n('p').realize()   
    ) == 'paissiez',\
    'paître:s5'


def test_conjugation_fr_1580():
    assert (
V("paître").t('s').pe(3).n('p').realize()   
    ) == 'paissent',\
    'paître:s6'


def test_conjugation_fr_1581():
    assert (
V("paraître").t('p').pe(1).n('s').realize()   
    ) == 'parais',\
    'paraître:p1'


def test_conjugation_fr_1582():
    assert (
V("paraître").t('p').pe(2).n('s').realize()   
    ) == 'parais',\
    'paraître:p2'


def test_conjugation_fr_1583():
    assert (
V("paraître").t('ip').pe(2).n('s').realize()   
    ) == 'parais',\
    'paraître:ip2'


def test_conjugation_fr_1584():
    assert (
V("paraître").t('pr').realize()   
    ) == 'paraissant',\
    'paraître:pr'


def test_conjugation_fr_1585():
    assert (
V("paraître").t('p').pe(3).n('p').realize()   
    ) == 'paraissent',\
    'paraître:p6'


def test_conjugation_fr_1586():
    assert (
V("paraître").t('p').pe(2).n('p').realize()   
    ) == 'paraissez',\
    'paraître:p5'


def test_conjugation_fr_1587():
    assert (
V("paraître").t('ip').pe(2).n('p').realize()   
    ) == 'paraissez',\
    'paraître:ip5'


def test_conjugation_fr_1588():
    assert (
V("paraître").t('p').pe(1).n('p').realize()   
    ) == 'paraissons',\
    'paraître:p4'


def test_conjugation_fr_1589():
    assert (
V("paraître").t('ip').pe(1).n('p').realize()   
    ) == 'paraissons',\
    'paraître:ip4'


def test_conjugation_fr_1590():
    assert (
V("paraître").t('p').pe(3).n('s').realize()   
    ) == 'paraît',\
    'paraître:p3'


def test_conjugation_fr_1591():
    assert (
V("paraître").t('pp').realize()   
    ) == 'paru',\
    'paraître:pp'


def test_conjugation_fr_1592():
    assert (
V("paraître").t('s').pe(1).n('s').realize()   
    ) == 'paraisse',\
    'paraître:s1'


def test_conjugation_fr_1593():
    assert (
V("paraître").t('s').pe(2).n('s').realize()   
    ) == 'paraisses',\
    'paraître:s2'


def test_conjugation_fr_1594():
    assert (
V("paraître").t('s').pe(3).n('s').realize()   
    ) == 'paraisse',\
    'paraître:s3'


def test_conjugation_fr_1595():
    assert (
V("paraître").t('s').pe(1).n('p').realize()   
    ) == 'paraissions',\
    'paraître:s4'


def test_conjugation_fr_1596():
    assert (
V("paraître").t('s').pe(2).n('p').realize()   
    ) == 'paraissiez',\
    'paraître:s5'


def test_conjugation_fr_1597():
    assert (
V("paraître").t('s').pe(3).n('p').realize()   
    ) == 'paraissent',\
    'paraître:s6'


def test_conjugation_fr_1598():
    assert (
V("parcourir").t('pr').realize()   
    ) == 'parcourant',\
    'parcourir:pr'


def test_conjugation_fr_1599():
    assert (
V("parcourir").t('p').pe(3).n('p').realize()   
    ) == 'parcourent',\
    'parcourir:p6'


def test_conjugation_fr_1600():
    assert (
V("parcourir").t('p').pe(2).n('p').realize()   
    ) == 'parcourez',\
    'parcourir:p5'


def test_conjugation_fr_1601():
    assert (
V("parcourir").t('ip').pe(2).n('p').realize()   
    ) == 'parcourez',\
    'parcourir:ip5'


def test_conjugation_fr_1602():
    assert (
V("parcourir").t('p').pe(1).n('p').realize()   
    ) == 'parcourons',\
    'parcourir:p4'


def test_conjugation_fr_1603():
    assert (
V("parcourir").t('ip').pe(1).n('p').realize()   
    ) == 'parcourons',\
    'parcourir:ip4'


def test_conjugation_fr_1604():
    assert (
V("parcourir").t('p').pe(1).n('s').realize()   
    ) == 'parcours',\
    'parcourir:p1'


def test_conjugation_fr_1605():
    assert (
V("parcourir").t('p').pe(2).n('s').realize()   
    ) == 'parcours',\
    'parcourir:p2'


def test_conjugation_fr_1606():
    assert (
V("parcourir").t('ip').pe(2).n('s').realize()   
    ) == 'parcours',\
    'parcourir:ip2'


def test_conjugation_fr_1607():
    assert (
V("parcourir").t('p').pe(3).n('s').realize()   
    ) == 'parcourt',\
    'parcourir:p3'


def test_conjugation_fr_1608():
    assert (
V("parcourir").t('pp').realize()   
    ) == 'parcouru',\
    'parcourir:pp'


def test_conjugation_fr_1609():
    assert (
V("parcourir").t('s').pe(1).n('s').realize()   
    ) == 'parcoure',\
    'parcourir:s1'


def test_conjugation_fr_1610():
    assert (
V("parcourir").t('s').pe(2).n('s').realize()   
    ) == 'parcoures',\
    'parcourir:s2'


def test_conjugation_fr_1611():
    assert (
V("parcourir").t('s').pe(3).n('s').realize()   
    ) == 'parcoure',\
    'parcourir:s3'


def test_conjugation_fr_1612():
    assert (
V("parcourir").t('s').pe(1).n('p').realize()   
    ) == 'parcourions',\
    'parcourir:s4'


def test_conjugation_fr_1613():
    assert (
V("parcourir").t('s').pe(2).n('p').realize()   
    ) == 'parcouriez',\
    'parcourir:s5'


def test_conjugation_fr_1614():
    assert (
V("parcourir").t('s').pe(3).n('p').realize()   
    ) == 'parcourent',\
    'parcourir:s6'


def test_conjugation_fr_1615():
    assert (
V("partir").t('p').pe(1).n('s').realize()   
    ) == 'pars',\
    'partir:p1'


def test_conjugation_fr_1616():
    assert (
V("partir").t('p').pe(2).n('s').realize()   
    ) == 'pars',\
    'partir:p2'


def test_conjugation_fr_1617():
    assert (
V("partir").t('ip').pe(2).n('s').realize()   
    ) == 'pars',\
    'partir:ip2'


def test_conjugation_fr_1618():
    assert (
V("partir").t('p').pe(3).n('s').realize()   
    ) == 'part',\
    'partir:p3'


def test_conjugation_fr_1619():
    assert (
V("partir").t('pr').realize()   
    ) == 'partant',\
    'partir:pr'


def test_conjugation_fr_1620():
    assert (
V("partir").t('p').pe(3).n('p').realize()   
    ) == 'partent',\
    'partir:p6'


def test_conjugation_fr_1621():
    assert (
V("partir").t('p').pe(2).n('p').realize()   
    ) == 'partez',\
    'partir:p5'


def test_conjugation_fr_1622():
    assert (
V("partir").t('ip').pe(2).n('p').realize()   
    ) == 'partez',\
    'partir:ip5'


def test_conjugation_fr_1623():
    assert (
V("partir").t('p').pe(1).n('p').realize()   
    ) == 'partons',\
    'partir:p4'


def test_conjugation_fr_1624():
    assert (
V("partir").t('ip').pe(1).n('p').realize()   
    ) == 'partons',\
    'partir:ip4'


def test_conjugation_fr_1625():
    assert (
V("partir").t('pp').realize()   
    ) == 'parti',\
    'partir:pp'


def test_conjugation_fr_1626():
    assert (
V("partir").t('s').pe(1).n('s').realize()   
    ) == 'parte',\
    'partir:s1'


def test_conjugation_fr_1627():
    assert (
V("partir").t('s').pe(2).n('s').realize()   
    ) == 'partes',\
    'partir:s2'


def test_conjugation_fr_1628():
    assert (
V("partir").t('s').pe(3).n('s').realize()   
    ) == 'parte',\
    'partir:s3'


def test_conjugation_fr_1629():
    assert (
V("partir").t('s').pe(1).n('p').realize()   
    ) == 'partions',\
    'partir:s4'


def test_conjugation_fr_1630():
    assert (
V("partir").t('s').pe(2).n('p').realize()   
    ) == 'partiez',\
    'partir:s5'


def test_conjugation_fr_1631():
    assert (
V("partir").t('s').pe(3).n('p').realize()   
    ) == 'partent',\
    'partir:s6'


def test_conjugation_fr_1632():
    assert (
V("parvenir").t('pr').realize()   
    ) == 'parvenant',\
    'parvenir:pr'


def test_conjugation_fr_1633():
    assert (
V("parvenir").t('p').pe(2).n('p').realize()   
    ) == 'parvenez',\
    'parvenir:p5'


def test_conjugation_fr_1634():
    assert (
V("parvenir").t('ip').pe(2).n('p').realize()   
    ) == 'parvenez',\
    'parvenir:ip5'


def test_conjugation_fr_1635():
    assert (
V("parvenir").t('p').pe(1).n('p').realize()   
    ) == 'parvenons',\
    'parvenir:p4'


def test_conjugation_fr_1636():
    assert (
V("parvenir").t('ip').pe(1).n('p').realize()   
    ) == 'parvenons',\
    'parvenir:ip4'


def test_conjugation_fr_1637():
    assert (
V("parvenir").t('p').pe(3).n('p').realize()   
    ) == 'parviennent',\
    'parvenir:p6'


def test_conjugation_fr_1638():
    assert (
V("parvenir").t('p').pe(1).n('s').realize()   
    ) == 'parviens',\
    'parvenir:p1'


def test_conjugation_fr_1639():
    assert (
V("parvenir").t('p').pe(2).n('s').realize()   
    ) == 'parviens',\
    'parvenir:p2'


def test_conjugation_fr_1640():
    assert (
V("parvenir").t('ip').pe(2).n('s').realize()   
    ) == 'parviens',\
    'parvenir:ip2'


def test_conjugation_fr_1641():
    assert (
V("parvenir").t('p').pe(3).n('s').realize()   
    ) == 'parvient',\
    'parvenir:p3'


def test_conjugation_fr_1642():
    assert (
V("parvenir").t('pp').realize()   
    ) == 'parvenu',\
    'parvenir:pp'


def test_conjugation_fr_1643():
    assert (
V("parvenir").t('s').pe(1).n('s').realize()   
    ) == 'parvienne',\
    'parvenir:s1'


def test_conjugation_fr_1644():
    assert (
V("parvenir").t('s').pe(2).n('s').realize()   
    ) == 'parviennes',\
    'parvenir:s2'


def test_conjugation_fr_1645():
    assert (
V("parvenir").t('s').pe(3).n('s').realize()   
    ) == 'parvienne',\
    'parvenir:s3'


def test_conjugation_fr_1646():
    assert (
V("parvenir").t('s').pe(1).n('p').realize()   
    ) == 'parvenions',\
    'parvenir:s4'


def test_conjugation_fr_1647():
    assert (
V("parvenir").t('s').pe(2).n('p').realize()   
    ) == 'parveniez',\
    'parvenir:s5'


def test_conjugation_fr_1648():
    assert (
V("parvenir").t('s').pe(3).n('p').realize()   
    ) == 'parviennent',\
    'parvenir:s6'


def test_conjugation_fr_1649():
    assert (
V("peindre").t('pr').realize()   
    ) == 'peignant',\
    'peindre:pr'


def test_conjugation_fr_1650():
    assert (
V("peindre").t('p').pe(3).n('p').realize()   
    ) == 'peignent',\
    'peindre:p6'


def test_conjugation_fr_1651():
    assert (
V("peindre").t('p').pe(2).n('p').realize()   
    ) == 'peignez',\
    'peindre:p5'


def test_conjugation_fr_1652():
    assert (
V("peindre").t('ip').pe(2).n('p').realize()   
    ) == 'peignez',\
    'peindre:ip5'


def test_conjugation_fr_1653():
    assert (
V("peindre").t('p').pe(1).n('p').realize()   
    ) == 'peignons',\
    'peindre:p4'


def test_conjugation_fr_1654():
    assert (
V("peindre").t('ip').pe(1).n('p').realize()   
    ) == 'peignons',\
    'peindre:ip4'


def test_conjugation_fr_1655():
    assert (
V("peindre").t('p').pe(1).n('s').realize()   
    ) == 'peins',\
    'peindre:p1'


def test_conjugation_fr_1656():
    assert (
V("peindre").t('p').pe(2).n('s').realize()   
    ) == 'peins',\
    'peindre:p2'


def test_conjugation_fr_1657():
    assert (
V("peindre").t('ip').pe(2).n('s').realize()   
    ) == 'peins',\
    'peindre:ip2'


def test_conjugation_fr_1658():
    assert (
V("peindre").t('p').pe(3).n('s').realize()   
    ) == 'peint',\
    'peindre:p3'


def test_conjugation_fr_1659():
    assert (
V("peindre").t('pp').realize()   
    ) == 'peint',\
    'peindre:pp'


def test_conjugation_fr_1660():
    assert (
V("peindre").t('s').pe(1).n('s').realize()   
    ) == 'peigne',\
    'peindre:s1'


def test_conjugation_fr_1661():
    assert (
V("peindre").t('s').pe(2).n('s').realize()   
    ) == 'peignes',\
    'peindre:s2'


def test_conjugation_fr_1662():
    assert (
V("peindre").t('s').pe(3).n('s').realize()   
    ) == 'peigne',\
    'peindre:s3'


def test_conjugation_fr_1663():
    assert (
V("peindre").t('s').pe(1).n('p').realize()   
    ) == 'peignions',\
    'peindre:s4'


def test_conjugation_fr_1664():
    assert (
V("peindre").t('s').pe(2).n('p').realize()   
    ) == 'peigniez',\
    'peindre:s5'


def test_conjugation_fr_1665():
    assert (
V("peindre").t('s').pe(3).n('p').realize()   
    ) == 'peignent',\
    'peindre:s6'


def test_conjugation_fr_1666():
    assert (
V("pendre").t('p').pe(3).n('s').realize()   
    ) == 'pend',\
    'pendre:p3'


def test_conjugation_fr_1667():
    assert (
V("pendre").t('pr').realize()   
    ) == 'pendant',\
    'pendre:pr'


def test_conjugation_fr_1668():
    assert (
V("pendre").t('p').pe(3).n('p').realize()   
    ) == 'pendent',\
    'pendre:p6'


def test_conjugation_fr_1669():
    assert (
V("pendre").t('p').pe(2).n('p').realize()   
    ) == 'pendez',\
    'pendre:p5'


def test_conjugation_fr_1670():
    assert (
V("pendre").t('ip').pe(2).n('p').realize()   
    ) == 'pendez',\
    'pendre:ip5'


def test_conjugation_fr_1671():
    assert (
V("pendre").t('p').pe(1).n('p').realize()   
    ) == 'pendons',\
    'pendre:p4'


def test_conjugation_fr_1672():
    assert (
V("pendre").t('ip').pe(1).n('p').realize()   
    ) == 'pendons',\
    'pendre:ip4'


def test_conjugation_fr_1673():
    assert (
V("pendre").t('p').pe(1).n('s').realize()   
    ) == 'pends',\
    'pendre:p1'


def test_conjugation_fr_1674():
    assert (
V("pendre").t('p').pe(2).n('s').realize()   
    ) == 'pends',\
    'pendre:p2'


def test_conjugation_fr_1675():
    assert (
V("pendre").t('ip').pe(2).n('s').realize()   
    ) == 'pends',\
    'pendre:ip2'


def test_conjugation_fr_1676():
    assert (
V("pendre").t('pp').realize()   
    ) == 'pendu',\
    'pendre:pp'


def test_conjugation_fr_1677():
    assert (
V("pendre").t('s').pe(1).n('s').realize()   
    ) == 'pende',\
    'pendre:s1'


def test_conjugation_fr_1678():
    assert (
V("pendre").t('s').pe(2).n('s').realize()   
    ) == 'pendes',\
    'pendre:s2'


def test_conjugation_fr_1679():
    assert (
V("pendre").t('s').pe(3).n('s').realize()   
    ) == 'pende',\
    'pendre:s3'


def test_conjugation_fr_1680():
    assert (
V("pendre").t('s').pe(1).n('p').realize()   
    ) == 'pendions',\
    'pendre:s4'


def test_conjugation_fr_1681():
    assert (
V("pendre").t('s').pe(2).n('p').realize()   
    ) == 'pendiez',\
    'pendre:s5'


def test_conjugation_fr_1682():
    assert (
V("pendre").t('s').pe(3).n('p').realize()   
    ) == 'pendent',\
    'pendre:s6'


def test_conjugation_fr_1683():
    assert (
V("perdre").t('p').pe(3).n('s').realize()   
    ) == 'perd',\
    'perdre:p3'


def test_conjugation_fr_1684():
    assert (
V("perdre").t('pr').realize()   
    ) == 'perdant',\
    'perdre:pr'


def test_conjugation_fr_1685():
    assert (
V("perdre").t('p').pe(3).n('p').realize()   
    ) == 'perdent',\
    'perdre:p6'


def test_conjugation_fr_1686():
    assert (
V("perdre").t('p').pe(2).n('p').realize()   
    ) == 'perdez',\
    'perdre:p5'


def test_conjugation_fr_1687():
    assert (
V("perdre").t('ip').pe(2).n('p').realize()   
    ) == 'perdez',\
    'perdre:ip5'


def test_conjugation_fr_1688():
    assert (
V("perdre").t('p').pe(1).n('p').realize()   
    ) == 'perdons',\
    'perdre:p4'


def test_conjugation_fr_1689():
    assert (
V("perdre").t('ip').pe(1).n('p').realize()   
    ) == 'perdons',\
    'perdre:ip4'


def test_conjugation_fr_1690():
    assert (
V("perdre").t('p').pe(1).n('s').realize()   
    ) == 'perds',\
    'perdre:p1'


def test_conjugation_fr_1691():
    assert (
V("perdre").t('p').pe(2).n('s').realize()   
    ) == 'perds',\
    'perdre:p2'


def test_conjugation_fr_1692():
    assert (
V("perdre").t('ip').pe(2).n('s').realize()   
    ) == 'perds',\
    'perdre:ip2'


def test_conjugation_fr_1693():
    assert (
V("perdre").t('pp').realize()   
    ) == 'perdu',\
    'perdre:pp'


def test_conjugation_fr_1694():
    assert (
V("perdre").t('s').pe(1).n('s').realize()   
    ) == 'perde',\
    'perdre:s1'


def test_conjugation_fr_1695():
    assert (
V("perdre").t('s').pe(2).n('s').realize()   
    ) == 'perdes',\
    'perdre:s2'


def test_conjugation_fr_1696():
    assert (
V("perdre").t('s').pe(3).n('s').realize()   
    ) == 'perde',\
    'perdre:s3'


def test_conjugation_fr_1697():
    assert (
V("perdre").t('s').pe(1).n('p').realize()   
    ) == 'perdions',\
    'perdre:s4'


def test_conjugation_fr_1698():
    assert (
V("perdre").t('s').pe(2).n('p').realize()   
    ) == 'perdiez',\
    'perdre:s5'


def test_conjugation_fr_1699():
    assert (
V("perdre").t('s').pe(3).n('p').realize()   
    ) == 'perdent',\
    'perdre:s6'


def test_conjugation_fr_1700():
    assert (
V("permettre").t('p').pe(3).n('s').realize()   
    ) == 'permet',\
    'permettre:p3'


def test_conjugation_fr_1701():
    assert (
V("permettre").t('p').pe(1).n('s').realize()   
    ) == 'permets',\
    'permettre:p1'


def test_conjugation_fr_1702():
    assert (
V("permettre").t('p').pe(2).n('s').realize()   
    ) == 'permets',\
    'permettre:p2'


def test_conjugation_fr_1703():
    assert (
V("permettre").t('ip').pe(2).n('s').realize()   
    ) == 'permets',\
    'permettre:ip2'


def test_conjugation_fr_1704():
    assert (
V("permettre").t('pr').realize()   
    ) == 'permettant',\
    'permettre:pr'


def test_conjugation_fr_1705():
    assert (
V("permettre").t('p').pe(3).n('p').realize()   
    ) == 'permettent',\
    'permettre:p6'


def test_conjugation_fr_1706():
    assert (
V("permettre").t('p').pe(2).n('p').realize()   
    ) == 'permettez',\
    'permettre:p5'


def test_conjugation_fr_1707():
    assert (
V("permettre").t('ip').pe(2).n('p').realize()   
    ) == 'permettez',\
    'permettre:ip5'


def test_conjugation_fr_1708():
    assert (
V("permettre").t('p').pe(1).n('p').realize()   
    ) == 'permettons',\
    'permettre:p4'


def test_conjugation_fr_1709():
    assert (
V("permettre").t('ip').pe(1).n('p').realize()   
    ) == 'permettons',\
    'permettre:ip4'


def test_conjugation_fr_1710():
    assert (
V("permettre").t('pp').realize()   
    ) == 'permis',\
    'permettre:pp'


def test_conjugation_fr_1711():
    assert (
V("permettre").t('s').pe(1).n('s').realize()   
    ) == 'permette',\
    'permettre:s1'


def test_conjugation_fr_1712():
    assert (
V("permettre").t('s').pe(2).n('s').realize()   
    ) == 'permettes',\
    'permettre:s2'


def test_conjugation_fr_1713():
    assert (
V("permettre").t('s').pe(3).n('s').realize()   
    ) == 'permette',\
    'permettre:s3'


def test_conjugation_fr_1714():
    assert (
V("permettre").t('s').pe(1).n('p').realize()   
    ) == 'permettions',\
    'permettre:s4'


def test_conjugation_fr_1715():
    assert (
V("permettre").t('s').pe(2).n('p').realize()   
    ) == 'permettiez',\
    'permettre:s5'


def test_conjugation_fr_1716():
    assert (
V("permettre").t('s').pe(3).n('p').realize()   
    ) == 'permettent',\
    'permettre:s6'


def test_conjugation_fr_1717():
    assert (
V("plaindre").t('pr').realize()   
    ) == 'plaignant',\
    'plaindre:pr'


def test_conjugation_fr_1718():
    assert (
V("plaindre").t('p').pe(3).n('p').realize()   
    ) == 'plaignent',\
    'plaindre:p6'


def test_conjugation_fr_1719():
    assert (
V("plaindre").t('p').pe(2).n('p').realize()   
    ) == 'plaignez',\
    'plaindre:p5'


def test_conjugation_fr_1720():
    assert (
V("plaindre").t('ip').pe(2).n('p').realize()   
    ) == 'plaignez',\
    'plaindre:ip5'


def test_conjugation_fr_1721():
    assert (
V("plaindre").t('p').pe(1).n('p').realize()   
    ) == 'plaignons',\
    'plaindre:p4'


def test_conjugation_fr_1722():
    assert (
V("plaindre").t('ip').pe(1).n('p').realize()   
    ) == 'plaignons',\
    'plaindre:ip4'


def test_conjugation_fr_1723():
    assert (
V("plaindre").t('p').pe(1).n('s').realize()   
    ) == 'plains',\
    'plaindre:p1'


def test_conjugation_fr_1724():
    assert (
V("plaindre").t('p').pe(2).n('s').realize()   
    ) == 'plains',\
    'plaindre:p2'


def test_conjugation_fr_1725():
    assert (
V("plaindre").t('ip').pe(2).n('s').realize()   
    ) == 'plains',\
    'plaindre:ip2'


def test_conjugation_fr_1726():
    assert (
V("plaindre").t('p').pe(3).n('s').realize()   
    ) == 'plaint',\
    'plaindre:p3'


def test_conjugation_fr_1727():
    assert (
V("plaindre").t('pp').realize()   
    ) == 'plaint',\
    'plaindre:pp'


def test_conjugation_fr_1728():
    assert (
V("plaindre").t('s').pe(1).n('s').realize()   
    ) == 'plaigne',\
    'plaindre:s1'


def test_conjugation_fr_1729():
    assert (
V("plaindre").t('s').pe(2).n('s').realize()   
    ) == 'plaignes',\
    'plaindre:s2'


def test_conjugation_fr_1730():
    assert (
V("plaindre").t('s').pe(3).n('s').realize()   
    ) == 'plaigne',\
    'plaindre:s3'


def test_conjugation_fr_1731():
    assert (
V("plaindre").t('s').pe(1).n('p').realize()   
    ) == 'plaignions',\
    'plaindre:s4'


def test_conjugation_fr_1732():
    assert (
V("plaindre").t('s').pe(2).n('p').realize()   
    ) == 'plaigniez',\
    'plaindre:s5'


def test_conjugation_fr_1733():
    assert (
V("plaindre").t('s').pe(3).n('p').realize()   
    ) == 'plaignent',\
    'plaindre:s6'


def test_conjugation_fr_1734():
    assert (
V("plaire").t('p').pe(1).n('s').realize()   
    ) == 'plais',\
    'plaire:p1'


def test_conjugation_fr_1735():
    assert (
V("plaire").t('p').pe(2).n('s').realize()   
    ) == 'plais',\
    'plaire:p2'


def test_conjugation_fr_1736():
    assert (
V("plaire").t('ip').pe(2).n('s').realize()   
    ) == 'plais',\
    'plaire:ip2'


def test_conjugation_fr_1737():
    assert (
V("plaire").t('pr').realize()   
    ) == 'plaisant',\
    'plaire:pr'


def test_conjugation_fr_1738():
    assert (
V("plaire").t('p').pe(3).n('p').realize()   
    ) == 'plaisent',\
    'plaire:p6'


def test_conjugation_fr_1739():
    assert (
V("plaire").t('p').pe(2).n('p').realize()   
    ) == 'plaisez',\
    'plaire:p5'


def test_conjugation_fr_1740():
    assert (
V("plaire").t('ip').pe(2).n('p').realize()   
    ) == 'plaisez',\
    'plaire:ip5'


def test_conjugation_fr_1741():
    assert (
V("plaire").t('p').pe(1).n('p').realize()   
    ) == 'plaisons',\
    'plaire:p4'


def test_conjugation_fr_1742():
    assert (
V("plaire").t('ip').pe(1).n('p').realize()   
    ) == 'plaisons',\
    'plaire:ip4'


def test_conjugation_fr_1743():
    assert (
V("plaire").t('p').pe(3).n('s').realize()   
    ) == 'plaît',\
    'plaire:p3'


def test_conjugation_fr_1744():
    assert (
V("plaire").t('s').pe(1).n('s').realize()   
    ) == 'plaise',\
    'plaire:s1'


def test_conjugation_fr_1745():
    assert (
V("plaire").t('s').pe(2).n('s').realize()   
    ) == 'plaises',\
    'plaire:s2'


def test_conjugation_fr_1746():
    assert (
V("plaire").t('s').pe(3).n('s').realize()   
    ) == 'plaise',\
    'plaire:s3'


def test_conjugation_fr_1747():
    assert (
V("plaire").t('s').pe(1).n('p').realize()   
    ) == 'plaisions',\
    'plaire:s4'


def test_conjugation_fr_1748():
    assert (
V("plaire").t('s').pe(2).n('p').realize()   
    ) == 'plaisiez',\
    'plaire:s5'


def test_conjugation_fr_1749():
    assert (
V("plaire").t('s').pe(3).n('p').realize()   
    ) == 'plaisent',\
    'plaire:s6'


def test_conjugation_fr_1750():
    assert (
V("pleuvoir").t('p').pe(3).n('s').realize()   
    ) == 'pleut',\
    'pleuvoir:p3'


def test_conjugation_fr_1751():
    assert (
V("pleuvoir").t('pr').realize()   
    ) == 'pleuvant',\
    'pleuvoir:pr'


def test_conjugation_fr_1752():
    assert (
V("pleuvoir").t('p').pe(3).n('p').realize()   
    ) == 'pleuvent',\
    'pleuvoir:p6'


def test_conjugation_fr_1753():
    assert (
V("pleuvoir").t('s').pe(3).n('s').realize()   
    ) == 'pleuve',\
    'pleuvoir:s3'


def test_conjugation_fr_1754():
    assert (
V("pleuvoir").t('s').pe(3).n('p').realize()   
    ) == 'pleuvent',\
    'pleuvoir:s6'


def test_conjugation_fr_1755():
    assert (
V("pondre").t('p').pe(3).n('s').realize()   
    ) == 'pond',\
    'pondre:p3'


def test_conjugation_fr_1756():
    assert (
V("pondre").t('pr').realize()   
    ) == 'pondant',\
    'pondre:pr'


def test_conjugation_fr_1757():
    assert (
V("pondre").t('p').pe(3).n('p').realize()   
    ) == 'pondent',\
    'pondre:p6'


def test_conjugation_fr_1758():
    assert (
V("pondre").t('p').pe(2).n('p').realize()   
    ) == 'pondez',\
    'pondre:p5'


def test_conjugation_fr_1759():
    assert (
V("pondre").t('ip').pe(2).n('p').realize()   
    ) == 'pondez',\
    'pondre:ip5'


def test_conjugation_fr_1760():
    assert (
V("pondre").t('p').pe(1).n('p').realize()   
    ) == 'pondons',\
    'pondre:p4'


def test_conjugation_fr_1761():
    assert (
V("pondre").t('ip').pe(1).n('p').realize()   
    ) == 'pondons',\
    'pondre:ip4'


def test_conjugation_fr_1762():
    assert (
V("pondre").t('p').pe(1).n('s').realize()   
    ) == 'ponds',\
    'pondre:p1'


def test_conjugation_fr_1763():
    assert (
V("pondre").t('p').pe(2).n('s').realize()   
    ) == 'ponds',\
    'pondre:p2'


def test_conjugation_fr_1764():
    assert (
V("pondre").t('ip').pe(2).n('s').realize()   
    ) == 'ponds',\
    'pondre:ip2'


def test_conjugation_fr_1765():
    assert (
V("pondre").t('pp').realize()   
    ) == 'pondu',\
    'pondre:pp'


def test_conjugation_fr_1766():
    assert (
V("pondre").t('s').pe(1).n('s').realize()   
    ) == 'ponde',\
    'pondre:s1'


def test_conjugation_fr_1767():
    assert (
V("pondre").t('s').pe(2).n('s').realize()   
    ) == 'pondes',\
    'pondre:s2'


def test_conjugation_fr_1768():
    assert (
V("pondre").t('s').pe(3).n('s').realize()   
    ) == 'ponde',\
    'pondre:s3'


def test_conjugation_fr_1769():
    assert (
V("pondre").t('s').pe(1).n('p').realize()   
    ) == 'pondions',\
    'pondre:s4'


def test_conjugation_fr_1770():
    assert (
V("pondre").t('s').pe(2).n('p').realize()   
    ) == 'pondiez',\
    'pondre:s5'


def test_conjugation_fr_1771():
    assert (
V("pondre").t('s').pe(3).n('p').realize()   
    ) == 'pondent',\
    'pondre:s6'


def test_conjugation_fr_1772():
    assert (
V("poursuivre").t('p').pe(1).n('s').realize()   
    ) == 'poursuis',\
    'poursuivre:p1'


def test_conjugation_fr_1773():
    assert (
V("poursuivre").t('p').pe(2).n('s').realize()   
    ) == 'poursuis',\
    'poursuivre:p2'


def test_conjugation_fr_1774():
    assert (
V("poursuivre").t('ip').pe(2).n('s').realize()   
    ) == 'poursuis',\
    'poursuivre:ip2'


def test_conjugation_fr_1775():
    assert (
V("poursuivre").t('p').pe(3).n('s').realize()   
    ) == 'poursuit',\
    'poursuivre:p3'


def test_conjugation_fr_1776():
    assert (
V("poursuivre").t('pr').realize()   
    ) == 'poursuivant',\
    'poursuivre:pr'


def test_conjugation_fr_1777():
    assert (
V("poursuivre").t('p').pe(3).n('p').realize()   
    ) == 'poursuivent',\
    'poursuivre:p6'


def test_conjugation_fr_1778():
    assert (
V("poursuivre").t('p').pe(2).n('p').realize()   
    ) == 'poursuivez',\
    'poursuivre:p5'


def test_conjugation_fr_1779():
    assert (
V("poursuivre").t('ip').pe(2).n('p').realize()   
    ) == 'poursuivez',\
    'poursuivre:ip5'


def test_conjugation_fr_1780():
    assert (
V("poursuivre").t('p').pe(1).n('p').realize()   
    ) == 'poursuivons',\
    'poursuivre:p4'


def test_conjugation_fr_1781():
    assert (
V("poursuivre").t('ip').pe(1).n('p').realize()   
    ) == 'poursuivons',\
    'poursuivre:ip4'


def test_conjugation_fr_1782():
    assert (
V("poursuivre").t('pp').realize()   
    ) == 'poursuivi',\
    'poursuivre:pp'


def test_conjugation_fr_1783():
    assert (
V("poursuivre").t('s').pe(1).n('s').realize()   
    ) == 'poursuive',\
    'poursuivre:s1'


def test_conjugation_fr_1784():
    assert (
V("poursuivre").t('s').pe(2).n('s').realize()   
    ) == 'poursuives',\
    'poursuivre:s2'


def test_conjugation_fr_1785():
    assert (
V("poursuivre").t('s').pe(3).n('s').realize()   
    ) == 'poursuive',\
    'poursuivre:s3'


def test_conjugation_fr_1786():
    assert (
V("poursuivre").t('s').pe(1).n('p').realize()   
    ) == 'poursuivions',\
    'poursuivre:s4'


def test_conjugation_fr_1787():
    assert (
V("poursuivre").t('s').pe(2).n('p').realize()   
    ) == 'poursuiviez',\
    'poursuivre:s5'


def test_conjugation_fr_1788():
    assert (
V("poursuivre").t('s').pe(3).n('p').realize()   
    ) == 'poursuivent',\
    'poursuivre:s6'


def test_conjugation_fr_1789():
    assert (
V("pourvoir").t('p').pe(3).n('p').realize()   
    ) == 'pourvoient',\
    'pourvoir:p6'


def test_conjugation_fr_1790():
    assert (
V("pourvoir").t('p').pe(1).n('s').realize()   
    ) == 'pourvois',\
    'pourvoir:p1'


def test_conjugation_fr_1791():
    assert (
V("pourvoir").t('p').pe(2).n('s').realize()   
    ) == 'pourvois',\
    'pourvoir:p2'


def test_conjugation_fr_1792():
    assert (
V("pourvoir").t('ip').pe(2).n('s').realize()   
    ) == 'pourvois',\
    'pourvoir:ip2'


def test_conjugation_fr_1793():
    assert (
V("pourvoir").t('p').pe(3).n('s').realize()   
    ) == 'pourvoit',\
    'pourvoir:p3'


def test_conjugation_fr_1794():
    assert (
V("pourvoir").t('pr').realize()   
    ) == 'pourvoyant',\
    'pourvoir:pr'


def test_conjugation_fr_1795():
    assert (
V("pourvoir").t('p').pe(2).n('p').realize()   
    ) == 'pourvoyez',\
    'pourvoir:p5'


def test_conjugation_fr_1796():
    assert (
V("pourvoir").t('ip').pe(2).n('p').realize()   
    ) == 'pourvoyez',\
    'pourvoir:ip5'


def test_conjugation_fr_1797():
    assert (
V("pourvoir").t('p').pe(1).n('p').realize()   
    ) == 'pourvoyons',\
    'pourvoir:p4'


def test_conjugation_fr_1798():
    assert (
V("pourvoir").t('ip').pe(1).n('p').realize()   
    ) == 'pourvoyons',\
    'pourvoir:ip4'


def test_conjugation_fr_1799():
    assert (
V("pourvoir").t('pp').realize()   
    ) == 'pourvu',\
    'pourvoir:pp'


def test_conjugation_fr_1800():
    assert (
V("pourvoir").t('s').pe(1).n('s').realize()   
    ) == 'pourvoie',\
    'pourvoir:s1'


def test_conjugation_fr_1801():
    assert (
V("pourvoir").t('s').pe(2).n('s').realize()   
    ) == 'pourvoies',\
    'pourvoir:s2'


def test_conjugation_fr_1802():
    assert (
V("pourvoir").t('s').pe(3).n('s').realize()   
    ) == 'pourvoie',\
    'pourvoir:s3'


def test_conjugation_fr_1803():
    assert (
V("pourvoir").t('s').pe(1).n('p').realize()   
    ) == 'pourvoyions',\
    'pourvoir:s4'


def test_conjugation_fr_1804():
    assert (
V("pourvoir").t('s').pe(2).n('p').realize()   
    ) == 'pourvoyiez',\
    'pourvoir:s5'


def test_conjugation_fr_1805():
    assert (
V("pourvoir").t('s').pe(3).n('p').realize()   
    ) == 'pourvoient',\
    'pourvoir:s6'


def test_conjugation_fr_1806():
    assert (
V("pouvoir").t('p').pe(3).n('s').realize()   
    ) == 'peut',\
    'pouvoir:p3'


def test_conjugation_fr_1807():
    assert (
V("pouvoir").t('p').pe(3).n('p').realize()   
    ) == 'peuvent',\
    'pouvoir:p6'


def test_conjugation_fr_1808():
    assert (
V("pouvoir").t('p').pe(1).n('s').realize()   
    ) == 'peux',\
    'pouvoir:p1'


def test_conjugation_fr_1809():
    assert (
V("pouvoir").t('pr').realize()   
    ) == 'pouvant',\
    'pouvoir:pr'


def test_conjugation_fr_1810():
    assert (
V("pouvoir").t('p').pe(2).n('p').realize()   
    ) == 'pouvez',\
    'pouvoir:p5'


def test_conjugation_fr_1811():
    assert (
V("pouvoir").t('p').pe(1).n('p').realize()   
    ) == 'pouvons',\
    'pouvoir:p4'


def test_conjugation_fr_1812():
    assert (
V("pouvoir").t('s').pe(1).n('s').realize()   
    ) == 'puisse',\
    'pouvoir:s1'


def test_conjugation_fr_1813():
    assert (
V("pouvoir").t('s').pe(2).n('s').realize()   
    ) == 'puisses',\
    'pouvoir:s2'


def test_conjugation_fr_1814():
    assert (
V("pouvoir").t('s').pe(3).n('s').realize()   
    ) == 'puisse',\
    'pouvoir:s3'


def test_conjugation_fr_1815():
    assert (
V("pouvoir").t('s').pe(1).n('p').realize()   
    ) == 'puissions',\
    'pouvoir:s4'


def test_conjugation_fr_1816():
    assert (
V("pouvoir").t('s').pe(2).n('p').realize()   
    ) == 'puissiez',\
    'pouvoir:s5'


def test_conjugation_fr_1817():
    assert (
V("pouvoir").t('s').pe(3).n('p').realize()   
    ) == 'puissent',\
    'pouvoir:s6'


def test_conjugation_fr_1818():
    assert (
V("pouvoir").t('pp').realize()   
    ) == 'pu',\
    'pouvoir:pp'


def test_conjugation_fr_1819():
    assert (
V("prendre").t('pr').realize()   
    ) == 'prenant',\
    'prendre:pr'


def test_conjugation_fr_1820():
    assert (
V("prendre").t('p').pe(3).n('s').realize()   
    ) == 'prend',\
    'prendre:p3'


def test_conjugation_fr_1821():
    assert (
V("prendre").t('p').pe(1).n('s').realize()   
    ) == 'prends',\
    'prendre:p1'


def test_conjugation_fr_1822():
    assert (
V("prendre").t('p').pe(2).n('s').realize()   
    ) == 'prends',\
    'prendre:p2'


def test_conjugation_fr_1823():
    assert (
V("prendre").t('ip').pe(2).n('s').realize()   
    ) == 'prends',\
    'prendre:ip2'


def test_conjugation_fr_1824():
    assert (
V("prendre").t('p').pe(2).n('p').realize()   
    ) == 'prenez',\
    'prendre:p5'


def test_conjugation_fr_1825():
    assert (
V("prendre").t('ip').pe(2).n('p').realize()   
    ) == 'prenez',\
    'prendre:ip5'


def test_conjugation_fr_1826():
    assert (
V("prendre").t('p').pe(3).n('p').realize()   
    ) == 'prennent',\
    'prendre:p6'


def test_conjugation_fr_1827():
    assert (
V("prendre").t('p').pe(1).n('p').realize()   
    ) == 'prenons',\
    'prendre:p4'


def test_conjugation_fr_1828():
    assert (
V("prendre").t('ip').pe(1).n('p').realize()   
    ) == 'prenons',\
    'prendre:ip4'


def test_conjugation_fr_1829():
    assert (
V("prendre").t('pp').realize()   
    ) == 'pris',\
    'prendre:pp'


def test_conjugation_fr_1830():
    assert (
V("prendre").t('s').pe(1).n('s').realize()   
    ) == 'prenne',\
    'prendre:s1'


def test_conjugation_fr_1831():
    assert (
V("prendre").t('s').pe(2).n('s').realize()   
    ) == 'prennes',\
    'prendre:s2'


def test_conjugation_fr_1832():
    assert (
V("prendre").t('s').pe(3).n('s').realize()   
    ) == 'prenne',\
    'prendre:s3'


def test_conjugation_fr_1833():
    assert (
V("prendre").t('s').pe(1).n('p').realize()   
    ) == 'prenions',\
    'prendre:s4'


def test_conjugation_fr_1834():
    assert (
V("prendre").t('s').pe(2).n('p').realize()   
    ) == 'preniez',\
    'prendre:s5'


def test_conjugation_fr_1835():
    assert (
V("prendre").t('s').pe(3).n('p').realize()   
    ) == 'prennent',\
    'prendre:s6'


def test_conjugation_fr_1836():
    assert (
V("prétendre").t('p').pe(3).n('s').realize()   
    ) == 'prétend',\
    'prétendre:p3'


def test_conjugation_fr_1837():
    assert (
V("prétendre").t('pr').realize()   
    ) == 'prétendant',\
    'prétendre:pr'


def test_conjugation_fr_1838():
    assert (
V("prétendre").t('p').pe(3).n('p').realize()   
    ) == 'prétendent',\
    'prétendre:p6'


def test_conjugation_fr_1839():
    assert (
V("prétendre").t('p').pe(2).n('p').realize()   
    ) == 'prétendez',\
    'prétendre:p5'


def test_conjugation_fr_1840():
    assert (
V("prétendre").t('ip').pe(2).n('p').realize()   
    ) == 'prétendez',\
    'prétendre:ip5'


def test_conjugation_fr_1841():
    assert (
V("prétendre").t('p').pe(1).n('p').realize()   
    ) == 'prétendons',\
    'prétendre:p4'


def test_conjugation_fr_1842():
    assert (
V("prétendre").t('ip').pe(1).n('p').realize()   
    ) == 'prétendons',\
    'prétendre:ip4'


def test_conjugation_fr_1843():
    assert (
V("prétendre").t('p').pe(1).n('s').realize()   
    ) == 'prétends',\
    'prétendre:p1'


def test_conjugation_fr_1844():
    assert (
V("prétendre").t('p').pe(2).n('s').realize()   
    ) == 'prétends',\
    'prétendre:p2'


def test_conjugation_fr_1845():
    assert (
V("prétendre").t('ip').pe(2).n('s').realize()   
    ) == 'prétends',\
    'prétendre:ip2'


def test_conjugation_fr_1846():
    assert (
V("prétendre").t('pp').realize()   
    ) == 'prétendu',\
    'prétendre:pp'


def test_conjugation_fr_1847():
    assert (
V("prétendre").t('s').pe(1).n('s').realize()   
    ) == 'prétende',\
    'prétendre:s1'


def test_conjugation_fr_1848():
    assert (
V("prétendre").t('s').pe(2).n('s').realize()   
    ) == 'prétendes',\
    'prétendre:s2'


def test_conjugation_fr_1849():
    assert (
V("prétendre").t('s').pe(3).n('s').realize()   
    ) == 'prétende',\
    'prétendre:s3'


def test_conjugation_fr_1850():
    assert (
V("prétendre").t('s').pe(1).n('p').realize()   
    ) == 'prétendions',\
    'prétendre:s4'


def test_conjugation_fr_1851():
    assert (
V("prétendre").t('s').pe(2).n('p').realize()   
    ) == 'prétendiez',\
    'prétendre:s5'


def test_conjugation_fr_1852():
    assert (
V("prétendre").t('s').pe(3).n('p').realize()   
    ) == 'prétendent',\
    'prétendre:s6'


def test_conjugation_fr_1853():
    assert (
V("prévenir").t('pr').realize()   
    ) == 'prévenant',\
    'prévenir:pr'


def test_conjugation_fr_1854():
    assert (
V("prévenir").t('p').pe(2).n('p').realize()   
    ) == 'prévenez',\
    'prévenir:p5'


def test_conjugation_fr_1855():
    assert (
V("prévenir").t('ip').pe(2).n('p').realize()   
    ) == 'prévenez',\
    'prévenir:ip5'


def test_conjugation_fr_1856():
    assert (
V("prévenir").t('p').pe(1).n('p').realize()   
    ) == 'prévenons',\
    'prévenir:p4'


def test_conjugation_fr_1857():
    assert (
V("prévenir").t('ip').pe(1).n('p').realize()   
    ) == 'prévenons',\
    'prévenir:ip4'


def test_conjugation_fr_1858():
    assert (
V("prévenir").t('p').pe(3).n('p').realize()   
    ) == 'préviennent',\
    'prévenir:p6'


def test_conjugation_fr_1859():
    assert (
V("prévenir").t('p').pe(1).n('s').realize()   
    ) == 'préviens',\
    'prévenir:p1'


def test_conjugation_fr_1860():
    assert (
V("prévenir").t('p').pe(2).n('s').realize()   
    ) == 'préviens',\
    'prévenir:p2'


def test_conjugation_fr_1861():
    assert (
V("prévenir").t('ip').pe(2).n('s').realize()   
    ) == 'préviens',\
    'prévenir:ip2'


def test_conjugation_fr_1862():
    assert (
V("prévenir").t('p').pe(3).n('s').realize()   
    ) == 'prévient',\
    'prévenir:p3'


def test_conjugation_fr_1863():
    assert (
V("prévenir").t('pp').realize()   
    ) == 'prévenu',\
    'prévenir:pp'


def test_conjugation_fr_1864():
    assert (
V("prévenir").t('s').pe(1).n('s').realize()   
    ) == 'prévienne',\
    'prévenir:s1'


def test_conjugation_fr_1865():
    assert (
V("prévenir").t('s').pe(2).n('s').realize()   
    ) == 'préviennes',\
    'prévenir:s2'


def test_conjugation_fr_1866():
    assert (
V("prévenir").t('s').pe(3).n('s').realize()   
    ) == 'prévienne',\
    'prévenir:s3'


def test_conjugation_fr_1867():
    assert (
V("prévenir").t('s').pe(1).n('p').realize()   
    ) == 'prévenions',\
    'prévenir:s4'


def test_conjugation_fr_1868():
    assert (
V("prévenir").t('s').pe(2).n('p').realize()   
    ) == 'préveniez',\
    'prévenir:s5'


def test_conjugation_fr_1869():
    assert (
V("prévenir").t('s').pe(3).n('p').realize()   
    ) == 'préviennent',\
    'prévenir:s6'


def test_conjugation_fr_1870():
    assert (
V("prévoir").t('p').pe(3).n('p').realize()   
    ) == 'prévoient',\
    'prévoir:p6'


def test_conjugation_fr_1871():
    assert (
V("prévoir").t('p').pe(1).n('s').realize()   
    ) == 'prévois',\
    'prévoir:p1'


def test_conjugation_fr_1872():
    assert (
V("prévoir").t('p').pe(2).n('s').realize()   
    ) == 'prévois',\
    'prévoir:p2'


def test_conjugation_fr_1873():
    assert (
V("prévoir").t('ip').pe(2).n('s').realize()   
    ) == 'prévois',\
    'prévoir:ip2'


def test_conjugation_fr_1874():
    assert (
V("prévoir").t('p').pe(3).n('s').realize()   
    ) == 'prévoit',\
    'prévoir:p3'


def test_conjugation_fr_1875():
    assert (
V("prévoir").t('pr').realize()   
    ) == 'prévoyant',\
    'prévoir:pr'


def test_conjugation_fr_1876():
    assert (
V("prévoir").t('p').pe(2).n('p').realize()   
    ) == 'prévoyez',\
    'prévoir:p5'


def test_conjugation_fr_1877():
    assert (
V("prévoir").t('ip').pe(2).n('p').realize()   
    ) == 'prévoyez',\
    'prévoir:ip5'


def test_conjugation_fr_1878():
    assert (
V("prévoir").t('p').pe(1).n('p').realize()   
    ) == 'prévoyons',\
    'prévoir:p4'


def test_conjugation_fr_1879():
    assert (
V("prévoir").t('ip').pe(1).n('p').realize()   
    ) == 'prévoyons',\
    'prévoir:ip4'


def test_conjugation_fr_1880():
    assert (
V("prévoir").t('pp').realize()   
    ) == 'prévu',\
    'prévoir:pp'


def test_conjugation_fr_1881():
    assert (
V("prévoir").t('s').pe(1).n('s').realize()   
    ) == 'prévoie',\
    'prévoir:s1'


def test_conjugation_fr_1882():
    assert (
V("prévoir").t('s').pe(2).n('s').realize()   
    ) == 'prévoies',\
    'prévoir:s2'


def test_conjugation_fr_1883():
    assert (
V("prévoir").t('s').pe(3).n('s').realize()   
    ) == 'prévoie',\
    'prévoir:s3'


def test_conjugation_fr_1884():
    assert (
V("prévoir").t('s').pe(1).n('p').realize()   
    ) == 'prévoyions',\
    'prévoir:s4'


def test_conjugation_fr_1885():
    assert (
V("prévoir").t('s').pe(2).n('p').realize()   
    ) == 'prévoyiez',\
    'prévoir:s5'


def test_conjugation_fr_1886():
    assert (
V("prévoir").t('s').pe(3).n('p').realize()   
    ) == 'prévoient',\
    'prévoir:s6'


def test_conjugation_fr_1887():
    assert (
V("produire").t('p').pe(1).n('s').realize()   
    ) == 'produis',\
    'produire:p1'


def test_conjugation_fr_1888():
    assert (
V("produire").t('p').pe(2).n('s').realize()   
    ) == 'produis',\
    'produire:p2'


def test_conjugation_fr_1889():
    assert (
V("produire").t('ip').pe(2).n('s').realize()   
    ) == 'produis',\
    'produire:ip2'


def test_conjugation_fr_1890():
    assert (
V("produire").t('pr').realize()   
    ) == 'produisant',\
    'produire:pr'


def test_conjugation_fr_1891():
    assert (
V("produire").t('p').pe(3).n('p').realize()   
    ) == 'produisent',\
    'produire:p6'


def test_conjugation_fr_1892():
    assert (
V("produire").t('p').pe(2).n('p').realize()   
    ) == 'produisez',\
    'produire:p5'


def test_conjugation_fr_1893():
    assert (
V("produire").t('ip').pe(2).n('p').realize()   
    ) == 'produisez',\
    'produire:ip5'


def test_conjugation_fr_1894():
    assert (
V("produire").t('p').pe(1).n('p').realize()   
    ) == 'produisons',\
    'produire:p4'


def test_conjugation_fr_1895():
    assert (
V("produire").t('ip').pe(1).n('p').realize()   
    ) == 'produisons',\
    'produire:ip4'


def test_conjugation_fr_1896():
    assert (
V("produire").t('p').pe(3).n('s').realize()   
    ) == 'produit',\
    'produire:p3'


def test_conjugation_fr_1897():
    assert (
V("produire").t('pp').realize()   
    ) == 'produit',\
    'produire:pp'


def test_conjugation_fr_1898():
    assert (
V("produire").t('s').pe(1).n('s').realize()   
    ) == 'produise',\
    'produire:s1'


def test_conjugation_fr_1899():
    assert (
V("produire").t('s').pe(2).n('s').realize()   
    ) == 'produises',\
    'produire:s2'


def test_conjugation_fr_1900():
    assert (
V("produire").t('s').pe(3).n('s').realize()   
    ) == 'produise',\
    'produire:s3'


def test_conjugation_fr_1901():
    assert (
V("produire").t('s').pe(1).n('p').realize()   
    ) == 'produisions',\
    'produire:s4'


def test_conjugation_fr_1902():
    assert (
V("produire").t('s').pe(2).n('p').realize()   
    ) == 'produisiez',\
    'produire:s5'


def test_conjugation_fr_1903():
    assert (
V("produire").t('s').pe(3).n('p').realize()   
    ) == 'produisent',\
    'produire:s6'


def test_conjugation_fr_1904():
    assert (
V("projeter").t('p').pe(1).n('s').realize()   
    ) == 'projette',\
    'projeter:p1'


def test_conjugation_fr_1905():
    assert (
V("projeter").t('p').pe(2).n('s').realize()   
    ) == 'projettes',\
    'projeter:p2'


def test_conjugation_fr_1906():
    assert (
V("projeter").t('p').pe(3).n('s').realize()   
    ) == 'projette',\
    'projeter:p3'


def test_conjugation_fr_1907():
    assert (
V("projeter").t('p').pe(3).n('p').realize()   
    ) == 'projettent',\
    'projeter:p6'


def test_conjugation_fr_1908():
    assert (
V("projeter").t('s').pe(1).n('s').realize()   
    ) == 'projette',\
    'projeter:s1'


def test_conjugation_fr_1909():
    assert (
V("projeter").t('s').pe(2).n('s').realize()   
    ) == 'projettes',\
    'projeter:s2'


def test_conjugation_fr_1910():
    assert (
V("projeter").t('s').pe(3).n('s').realize()   
    ) == 'projette',\
    'projeter:s3'


def test_conjugation_fr_1911():
    assert (
V("projeter").t('s').pe(1).n('p').realize()   
    ) == 'projetions',\
    'projeter:s4'


def test_conjugation_fr_1912():
    assert (
V("projeter").t('s').pe(2).n('p').realize()   
    ) == 'projetiez',\
    'projeter:s5'


def test_conjugation_fr_1913():
    assert (
V("projeter").t('s').pe(3).n('p').realize()   
    ) == 'projettent',\
    'projeter:s6'


def test_conjugation_fr_1914():
    assert (
V("promettre").t('p').pe(3).n('s').realize()   
    ) == 'promet',\
    'promettre:p3'


def test_conjugation_fr_1915():
    assert (
V("promettre").t('p').pe(1).n('s').realize()   
    ) == 'promets',\
    'promettre:p1'


def test_conjugation_fr_1916():
    assert (
V("promettre").t('p').pe(2).n('s').realize()   
    ) == 'promets',\
    'promettre:p2'


def test_conjugation_fr_1917():
    assert (
V("promettre").t('ip').pe(2).n('s').realize()   
    ) == 'promets',\
    'promettre:ip2'


def test_conjugation_fr_1918():
    assert (
V("promettre").t('pr').realize()   
    ) == 'promettant',\
    'promettre:pr'


def test_conjugation_fr_1919():
    assert (
V("promettre").t('p').pe(3).n('p').realize()   
    ) == 'promettent',\
    'promettre:p6'


def test_conjugation_fr_1920():
    assert (
V("promettre").t('p').pe(2).n('p').realize()   
    ) == 'promettez',\
    'promettre:p5'


def test_conjugation_fr_1921():
    assert (
V("promettre").t('ip').pe(2).n('p').realize()   
    ) == 'promettez',\
    'promettre:ip5'


def test_conjugation_fr_1922():
    assert (
V("promettre").t('p').pe(1).n('p').realize()   
    ) == 'promettons',\
    'promettre:p4'


def test_conjugation_fr_1923():
    assert (
V("promettre").t('ip').pe(1).n('p').realize()   
    ) == 'promettons',\
    'promettre:ip4'


def test_conjugation_fr_1924():
    assert (
V("promettre").t('pp').realize()   
    ) == 'promis',\
    'promettre:pp'


def test_conjugation_fr_1925():
    assert (
V("promettre").t('s').pe(1).n('s').realize()   
    ) == 'promette',\
    'promettre:s1'


def test_conjugation_fr_1926():
    assert (
V("promettre").t('s').pe(2).n('s').realize()   
    ) == 'promettes',\
    'promettre:s2'


def test_conjugation_fr_1927():
    assert (
V("promettre").t('s').pe(3).n('s').realize()   
    ) == 'promette',\
    'promettre:s3'


def test_conjugation_fr_1928():
    assert (
V("promettre").t('s').pe(1).n('p').realize()   
    ) == 'promettions',\
    'promettre:s4'


def test_conjugation_fr_1929():
    assert (
V("promettre").t('s').pe(2).n('p').realize()   
    ) == 'promettiez',\
    'promettre:s5'


def test_conjugation_fr_1930():
    assert (
V("promettre").t('s').pe(3).n('p').realize()   
    ) == 'promettent',\
    'promettre:s6'


def test_conjugation_fr_1931():
    assert (
V("provenir").t('pr').realize()   
    ) == 'provenant',\
    'provenir:pr'


def test_conjugation_fr_1932():
    assert (
V("provenir").t('p').pe(2).n('p').realize()   
    ) == 'provenez',\
    'provenir:p5'


def test_conjugation_fr_1933():
    assert (
V("provenir").t('ip').pe(2).n('p').realize()   
    ) == 'provenez',\
    'provenir:ip5'


def test_conjugation_fr_1934():
    assert (
V("provenir").t('p').pe(1).n('p').realize()   
    ) == 'provenons',\
    'provenir:p4'


def test_conjugation_fr_1935():
    assert (
V("provenir").t('ip').pe(1).n('p').realize()   
    ) == 'provenons',\
    'provenir:ip4'


def test_conjugation_fr_1936():
    assert (
V("provenir").t('p').pe(3).n('p').realize()   
    ) == 'proviennent',\
    'provenir:p6'


def test_conjugation_fr_1937():
    assert (
V("provenir").t('p').pe(1).n('s').realize()   
    ) == 'proviens',\
    'provenir:p1'


def test_conjugation_fr_1938():
    assert (
V("provenir").t('p').pe(2).n('s').realize()   
    ) == 'proviens',\
    'provenir:p2'


def test_conjugation_fr_1939():
    assert (
V("provenir").t('ip').pe(2).n('s').realize()   
    ) == 'proviens',\
    'provenir:ip2'


def test_conjugation_fr_1940():
    assert (
V("provenir").t('p').pe(3).n('s').realize()   
    ) == 'provient',\
    'provenir:p3'


def test_conjugation_fr_1941():
    assert (
V("provenir").t('pp').realize()   
    ) == 'provenu',\
    'provenir:pp'


def test_conjugation_fr_1942():
    assert (
V("provenir").t('s').pe(1).n('s').realize()   
    ) == 'provienne',\
    'provenir:s1'


def test_conjugation_fr_1943():
    assert (
V("provenir").t('s').pe(2).n('s').realize()   
    ) == 'proviennes',\
    'provenir:s2'


def test_conjugation_fr_1944():
    assert (
V("provenir").t('s').pe(3).n('s').realize()   
    ) == 'provienne',\
    'provenir:s3'


def test_conjugation_fr_1945():
    assert (
V("provenir").t('s').pe(1).n('p').realize()   
    ) == 'provenions',\
    'provenir:s4'


def test_conjugation_fr_1946():
    assert (
V("provenir").t('s').pe(2).n('p').realize()   
    ) == 'proveniez',\
    'provenir:s5'


def test_conjugation_fr_1947():
    assert (
V("provenir").t('s').pe(3).n('p').realize()   
    ) == 'proviennent',\
    'provenir:s6'


def test_conjugation_fr_1948():
    assert (
V("rappeler").t('p').pe(1).n('s').realize()   
    ) == 'rappelle',\
    'rappeler:p1'


def test_conjugation_fr_1949():
    assert (
V("rappeler").t('p').pe(2).n('s').realize()   
    ) == 'rappelles',\
    'rappeler:p2'


def test_conjugation_fr_1950():
    assert (
V("rappeler").t('p').pe(3).n('s').realize()   
    ) == 'rappelle',\
    'rappeler:p3'


def test_conjugation_fr_1951():
    assert (
V("rappeler").t('p').pe(3).n('p').realize()   
    ) == 'rappellent',\
    'rappeler:p6'


def test_conjugation_fr_1952():
    assert (
V("rappeler").t('s').pe(1).n('s').realize()   
    ) == 'rappelle',\
    'rappeler:s1'


def test_conjugation_fr_1953():
    assert (
V("rappeler").t('s').pe(2).n('s').realize()   
    ) == 'rappelles',\
    'rappeler:s2'


def test_conjugation_fr_1954():
    assert (
V("rappeler").t('s').pe(3).n('s').realize()   
    ) == 'rappelle',\
    'rappeler:s3'


def test_conjugation_fr_1955():
    assert (
V("rappeler").t('s').pe(1).n('p').realize()   
    ) == 'rappelions',\
    'rappeler:s4'


def test_conjugation_fr_1956():
    assert (
V("rappeler").t('s').pe(2).n('p').realize()   
    ) == 'rappeliez',\
    'rappeler:s5'


def test_conjugation_fr_1957():
    assert (
V("rappeler").t('s').pe(3).n('p').realize()   
    ) == 'rappellent',\
    'rappeler:s6'


def test_conjugation_fr_1958():
    assert (
V("recevoir").t('pr').realize()   
    ) == 'recevant',\
    'recevoir:pr'


def test_conjugation_fr_1959():
    assert (
V("recevoir").t('p').pe(2).n('p').realize()   
    ) == 'recevez',\
    'recevoir:p5'


def test_conjugation_fr_1960():
    assert (
V("recevoir").t('ip').pe(2).n('p').realize()   
    ) == 'recevez',\
    'recevoir:ip5'


def test_conjugation_fr_1961():
    assert (
V("recevoir").t('p').pe(1).n('p').realize()   
    ) == 'recevons',\
    'recevoir:p4'


def test_conjugation_fr_1962():
    assert (
V("recevoir").t('ip').pe(1).n('p').realize()   
    ) == 'recevons',\
    'recevoir:ip4'


def test_conjugation_fr_1963():
    assert (
V("recevoir").t('p').pe(1).n('s').realize()   
    ) == 'reçois',\
    'recevoir:p1'


def test_conjugation_fr_1964():
    assert (
V("recevoir").t('p').pe(2).n('s').realize()   
    ) == 'reçois',\
    'recevoir:p2'


def test_conjugation_fr_1965():
    assert (
V("recevoir").t('ip').pe(2).n('s').realize()   
    ) == 'reçois',\
    'recevoir:ip2'


def test_conjugation_fr_1966():
    assert (
V("recevoir").t('p').pe(3).n('s').realize()   
    ) == 'reçoit',\
    'recevoir:p3'


def test_conjugation_fr_1967():
    assert (
V("recevoir").t('p').pe(3).n('p').realize()   
    ) == 'reçoivent',\
    'recevoir:p6'


def test_conjugation_fr_1968():
    assert (
V("recevoir").t('s').pe(1).n('s').realize()   
    ) == 'reçoive',\
    'recevoir:s1'


def test_conjugation_fr_1969():
    assert (
V("recevoir").t('s').pe(2).n('s').realize()   
    ) == 'reçoives',\
    'recevoir:s2'


def test_conjugation_fr_1970():
    assert (
V("recevoir").t('s').pe(3).n('s').realize()   
    ) == 'reçoive',\
    'recevoir:s3'


def test_conjugation_fr_1971():
    assert (
V("recevoir").t('s').pe(1).n('p').realize()   
    ) == 'recevions',\
    'recevoir:s4'


def test_conjugation_fr_1972():
    assert (
V("recevoir").t('s').pe(2).n('p').realize()   
    ) == 'receviez',\
    'recevoir:s5'


def test_conjugation_fr_1973():
    assert (
V("recevoir").t('s').pe(3).n('p').realize()   
    ) == 'reçoivent',\
    'recevoir:s6'


def test_conjugation_fr_1974():
    assert (
V("recevoir").t('pp').realize()   
    ) == 'reçu',\
    'recevoir:pp'


def test_conjugation_fr_1975():
    assert (
V("reconduire").t('p').pe(1).n('s').realize()   
    ) == 'reconduis',\
    'reconduire:p1'


def test_conjugation_fr_1976():
    assert (
V("reconduire").t('p').pe(2).n('s').realize()   
    ) == 'reconduis',\
    'reconduire:p2'


def test_conjugation_fr_1977():
    assert (
V("reconduire").t('ip').pe(2).n('s').realize()   
    ) == 'reconduis',\
    'reconduire:ip2'


def test_conjugation_fr_1978():
    assert (
V("reconduire").t('pr').realize()   
    ) == 'reconduisant',\
    'reconduire:pr'


def test_conjugation_fr_1979():
    assert (
V("reconduire").t('p').pe(3).n('p').realize()   
    ) == 'reconduisent',\
    'reconduire:p6'


def test_conjugation_fr_1980():
    assert (
V("reconduire").t('p').pe(2).n('p').realize()   
    ) == 'reconduisez',\
    'reconduire:p5'


def test_conjugation_fr_1981():
    assert (
V("reconduire").t('ip').pe(2).n('p').realize()   
    ) == 'reconduisez',\
    'reconduire:ip5'


def test_conjugation_fr_1982():
    assert (
V("reconduire").t('p').pe(1).n('p').realize()   
    ) == 'reconduisons',\
    'reconduire:p4'


def test_conjugation_fr_1983():
    assert (
V("reconduire").t('ip').pe(1).n('p').realize()   
    ) == 'reconduisons',\
    'reconduire:ip4'


def test_conjugation_fr_1984():
    assert (
V("reconduire").t('p').pe(3).n('s').realize()   
    ) == 'reconduit',\
    'reconduire:p3'


def test_conjugation_fr_1985():
    assert (
V("reconduire").t('pp').realize()   
    ) == 'reconduit',\
    'reconduire:pp'


def test_conjugation_fr_1986():
    assert (
V("reconduire").t('s').pe(1).n('s').realize()   
    ) == 'reconduise',\
    'reconduire:s1'


def test_conjugation_fr_1987():
    assert (
V("reconduire").t('s').pe(2).n('s').realize()   
    ) == 'reconduises',\
    'reconduire:s2'


def test_conjugation_fr_1988():
    assert (
V("reconduire").t('s').pe(3).n('s').realize()   
    ) == 'reconduise',\
    'reconduire:s3'


def test_conjugation_fr_1989():
    assert (
V("reconduire").t('s').pe(1).n('p').realize()   
    ) == 'reconduisions',\
    'reconduire:s4'


def test_conjugation_fr_1990():
    assert (
V("reconduire").t('s').pe(2).n('p').realize()   
    ) == 'reconduisiez',\
    'reconduire:s5'


def test_conjugation_fr_1991():
    assert (
V("reconduire").t('s').pe(3).n('p').realize()   
    ) == 'reconduisent',\
    'reconduire:s6'


def test_conjugation_fr_1992():
    assert (
V("reconnaître").t('p').pe(1).n('s').realize()   
    ) == 'reconnais',\
    'reconnaître:p1'


def test_conjugation_fr_1993():
    assert (
V("reconnaître").t('p').pe(2).n('s').realize()   
    ) == 'reconnais',\
    'reconnaître:p2'


def test_conjugation_fr_1994():
    assert (
V("reconnaître").t('ip').pe(2).n('s').realize()   
    ) == 'reconnais',\
    'reconnaître:ip2'


def test_conjugation_fr_1995():
    assert (
V("reconnaître").t('pr').realize()   
    ) == 'reconnaissant',\
    'reconnaître:pr'


def test_conjugation_fr_1996():
    assert (
V("reconnaître").t('p').pe(3).n('p').realize()   
    ) == 'reconnaissent',\
    'reconnaître:p6'


def test_conjugation_fr_1997():
    assert (
V("reconnaître").t('p').pe(2).n('p').realize()   
    ) == 'reconnaissez',\
    'reconnaître:p5'


def test_conjugation_fr_1998():
    assert (
V("reconnaître").t('ip').pe(2).n('p').realize()   
    ) == 'reconnaissez',\
    'reconnaître:ip5'


def test_conjugation_fr_1999():
    assert (
V("reconnaître").t('p').pe(1).n('p').realize()   
    ) == 'reconnaissons',\
    'reconnaître:p4'


def test_conjugation_fr_2000():
    assert (
V("reconnaître").t('ip').pe(1).n('p').realize()   
    ) == 'reconnaissons',\
    'reconnaître:ip4'


def test_conjugation_fr_2001():
    assert (
V("reconnaître").t('p').pe(3).n('s').realize()   
    ) == 'reconnaît',\
    'reconnaître:p3'


def test_conjugation_fr_2002():
    assert (
V("reconnaître").t('pp').realize()   
    ) == 'reconnu',\
    'reconnaître:pp'


def test_conjugation_fr_2003():
    assert (
V("reconnaître").t('s').pe(1).n('s').realize()   
    ) == 'reconnaisse',\
    'reconnaître:s1'


def test_conjugation_fr_2004():
    assert (
V("reconnaître").t('s').pe(2).n('s').realize()   
    ) == 'reconnaisses',\
    'reconnaître:s2'


def test_conjugation_fr_2005():
    assert (
V("reconnaître").t('s').pe(3).n('s').realize()   
    ) == 'reconnaisse',\
    'reconnaître:s3'


def test_conjugation_fr_2006():
    assert (
V("reconnaître").t('s').pe(1).n('p').realize()   
    ) == 'reconnaissions',\
    'reconnaître:s4'


def test_conjugation_fr_2007():
    assert (
V("reconnaître").t('s').pe(2).n('p').realize()   
    ) == 'reconnaissiez',\
    'reconnaître:s5'


def test_conjugation_fr_2008():
    assert (
V("reconnaître").t('s').pe(3).n('p').realize()   
    ) == 'reconnaissent',\
    'reconnaître:s6'


def test_conjugation_fr_2009():
    assert (
V("recourir").t('pr').realize()   
    ) == 'recourant',\
    'recourir:pr'


def test_conjugation_fr_2010():
    assert (
V("recourir").t('p').pe(3).n('p').realize()   
    ) == 'recourent',\
    'recourir:p6'


def test_conjugation_fr_2011():
    assert (
V("recourir").t('p').pe(2).n('p').realize()   
    ) == 'recourez',\
    'recourir:p5'


def test_conjugation_fr_2012():
    assert (
V("recourir").t('ip').pe(2).n('p').realize()   
    ) == 'recourez',\
    'recourir:ip5'


def test_conjugation_fr_2013():
    assert (
V("recourir").t('p').pe(1).n('p').realize()   
    ) == 'recourons',\
    'recourir:p4'


def test_conjugation_fr_2014():
    assert (
V("recourir").t('ip').pe(1).n('p').realize()   
    ) == 'recourons',\
    'recourir:ip4'


def test_conjugation_fr_2015():
    assert (
V("recourir").t('p').pe(1).n('s').realize()   
    ) == 'recours',\
    'recourir:p1'


def test_conjugation_fr_2016():
    assert (
V("recourir").t('p').pe(2).n('s').realize()   
    ) == 'recours',\
    'recourir:p2'


def test_conjugation_fr_2017():
    assert (
V("recourir").t('ip').pe(2).n('s').realize()   
    ) == 'recours',\
    'recourir:ip2'


def test_conjugation_fr_2018():
    assert (
V("recourir").t('p').pe(3).n('s').realize()   
    ) == 'recourt',\
    'recourir:p3'


def test_conjugation_fr_2019():
    assert (
V("recourir").t('pp').realize()   
    ) == 'recouru',\
    'recourir:pp'


def test_conjugation_fr_2020():
    assert (
V("recourir").t('s').pe(1).n('s').realize()   
    ) == 'recoure',\
    'recourir:s1'


def test_conjugation_fr_2021():
    assert (
V("recourir").t('s').pe(2).n('s').realize()   
    ) == 'recoures',\
    'recourir:s2'


def test_conjugation_fr_2022():
    assert (
V("recourir").t('s').pe(3).n('s').realize()   
    ) == 'recoure',\
    'recourir:s3'


def test_conjugation_fr_2023():
    assert (
V("recourir").t('s').pe(1).n('p').realize()   
    ) == 'recourions',\
    'recourir:s4'


def test_conjugation_fr_2024():
    assert (
V("recourir").t('s').pe(2).n('p').realize()   
    ) == 'recouriez',\
    'recourir:s5'


def test_conjugation_fr_2025():
    assert (
V("recourir").t('s').pe(3).n('p').realize()   
    ) == 'recourent',\
    'recourir:s6'


def test_conjugation_fr_2026():
    assert (
V("recouvrir").t('pr').realize()   
    ) == 'recouvrant',\
    'recouvrir:pr'


def test_conjugation_fr_2027():
    assert (
V("recouvrir").t('p').pe(1).n('s').realize()   
    ) == 'recouvre',\
    'recouvrir:p1'


def test_conjugation_fr_2028():
    assert (
V("recouvrir").t('p').pe(3).n('s').realize()   
    ) == 'recouvre',\
    'recouvrir:p3'


def test_conjugation_fr_2029():
    assert (
V("recouvrir").t('ip').pe(2).n('s').realize()   
    ) == 'recouvre',\
    'recouvrir:ip2'


def test_conjugation_fr_2030():
    assert (
V("recouvrir").t('p').pe(3).n('p').realize()   
    ) == 'recouvrent',\
    'recouvrir:p6'


def test_conjugation_fr_2031():
    assert (
V("recouvrir").t('p').pe(2).n('s').realize()   
    ) == 'recouvres',\
    'recouvrir:p2'


def test_conjugation_fr_2032():
    assert (
V("recouvrir").t('p').pe(2).n('p').realize()   
    ) == 'recouvrez',\
    'recouvrir:p5'


def test_conjugation_fr_2033():
    assert (
V("recouvrir").t('ip').pe(2).n('p').realize()   
    ) == 'recouvrez',\
    'recouvrir:ip5'


def test_conjugation_fr_2034():
    assert (
V("recouvrir").t('p').pe(1).n('p').realize()   
    ) == 'recouvrons',\
    'recouvrir:p4'


def test_conjugation_fr_2035():
    assert (
V("recouvrir").t('ip').pe(1).n('p').realize()   
    ) == 'recouvrons',\
    'recouvrir:ip4'


def test_conjugation_fr_2036():
    assert (
V("recouvrir").t('pp').realize()   
    ) == 'recouvert',\
    'recouvrir:pp'


def test_conjugation_fr_2037():
    assert (
V("recouvrir").t('s').pe(1).n('s').realize()   
    ) == 'recouvre',\
    'recouvrir:s1'


def test_conjugation_fr_2038():
    assert (
V("recouvrir").t('s').pe(2).n('s').realize()   
    ) == 'recouvres',\
    'recouvrir:s2'


def test_conjugation_fr_2039():
    assert (
V("recouvrir").t('s').pe(3).n('s').realize()   
    ) == 'recouvre',\
    'recouvrir:s3'


def test_conjugation_fr_2040():
    assert (
V("recouvrir").t('s').pe(1).n('p').realize()   
    ) == 'recouvrions',\
    'recouvrir:s4'


def test_conjugation_fr_2041():
    assert (
V("recouvrir").t('s').pe(2).n('p').realize()   
    ) == 'recouvriez',\
    'recouvrir:s5'


def test_conjugation_fr_2042():
    assert (
V("recouvrir").t('s').pe(3).n('p').realize()   
    ) == 'recouvrent',\
    'recouvrir:s6'


def test_conjugation_fr_2043():
    assert (
V("recueillir").t('pr').realize()   
    ) == 'recueillant',\
    'recueillir:pr'


def test_conjugation_fr_2044():
    assert (
V("recueillir").t('p').pe(1).n('s').realize()   
    ) == 'recueille',\
    'recueillir:p1'


def test_conjugation_fr_2045():
    assert (
V("recueillir").t('p').pe(3).n('s').realize()   
    ) == 'recueille',\
    'recueillir:p3'


def test_conjugation_fr_2046():
    assert (
V("recueillir").t('ip').pe(2).n('s').realize()   
    ) == 'recueille',\
    'recueillir:ip2'


def test_conjugation_fr_2047():
    assert (
V("recueillir").t('p').pe(3).n('p').realize()   
    ) == 'recueillent',\
    'recueillir:p6'


def test_conjugation_fr_2048():
    assert (
V("recueillir").t('p').pe(2).n('s').realize()   
    ) == 'recueilles',\
    'recueillir:p2'


def test_conjugation_fr_2049():
    assert (
V("recueillir").t('p').pe(2).n('p').realize()   
    ) == 'recueillez',\
    'recueillir:p5'


def test_conjugation_fr_2050():
    assert (
V("recueillir").t('ip').pe(2).n('p').realize()   
    ) == 'recueillez',\
    'recueillir:ip5'


def test_conjugation_fr_2051():
    assert (
V("recueillir").t('p').pe(1).n('p').realize()   
    ) == 'recueillons',\
    'recueillir:p4'


def test_conjugation_fr_2052():
    assert (
V("recueillir").t('ip').pe(1).n('p').realize()   
    ) == 'recueillons',\
    'recueillir:ip4'


def test_conjugation_fr_2053():
    assert (
V("recueillir").t('pp').realize()   
    ) == 'recueilli',\
    'recueillir:pp'


def test_conjugation_fr_2054():
    assert (
V("recueillir").t('s').pe(1).n('s').realize()   
    ) == 'recueille',\
    'recueillir:s1'


def test_conjugation_fr_2055():
    assert (
V("recueillir").t('s').pe(2).n('s').realize()   
    ) == 'recueilles',\
    'recueillir:s2'


def test_conjugation_fr_2056():
    assert (
V("recueillir").t('s').pe(3).n('s').realize()   
    ) == 'recueille',\
    'recueillir:s3'


def test_conjugation_fr_2057():
    assert (
V("recueillir").t('s').pe(1).n('p').realize()   
    ) == 'recueillions',\
    'recueillir:s4'


def test_conjugation_fr_2058():
    assert (
V("recueillir").t('s').pe(2).n('p').realize()   
    ) == 'recueilliez',\
    'recueillir:s5'


def test_conjugation_fr_2059():
    assert (
V("recueillir").t('s').pe(3).n('p').realize()   
    ) == 'recueillent',\
    'recueillir:s6'


def test_conjugation_fr_2060():
    assert (
V("redescendre").t('p').pe(3).n('s').realize()   
    ) == 'redescend',\
    'redescendre:p3'


def test_conjugation_fr_2061():
    assert (
V("redescendre").t('pr').realize()   
    ) == 'redescendant',\
    'redescendre:pr'


def test_conjugation_fr_2062():
    assert (
V("redescendre").t('p').pe(3).n('p').realize()   
    ) == 'redescendent',\
    'redescendre:p6'


def test_conjugation_fr_2063():
    assert (
V("redescendre").t('p').pe(2).n('p').realize()   
    ) == 'redescendez',\
    'redescendre:p5'


def test_conjugation_fr_2064():
    assert (
V("redescendre").t('ip').pe(2).n('p').realize()   
    ) == 'redescendez',\
    'redescendre:ip5'


def test_conjugation_fr_2065():
    assert (
V("redescendre").t('p').pe(1).n('p').realize()   
    ) == 'redescendons',\
    'redescendre:p4'


def test_conjugation_fr_2066():
    assert (
V("redescendre").t('ip').pe(1).n('p').realize()   
    ) == 'redescendons',\
    'redescendre:ip4'


def test_conjugation_fr_2067():
    assert (
V("redescendre").t('p').pe(1).n('s').realize()   
    ) == 'redescends',\
    'redescendre:p1'


def test_conjugation_fr_2068():
    assert (
V("redescendre").t('p').pe(2).n('s').realize()   
    ) == 'redescends',\
    'redescendre:p2'


def test_conjugation_fr_2069():
    assert (
V("redescendre").t('ip').pe(2).n('s').realize()   
    ) == 'redescends',\
    'redescendre:ip2'


def test_conjugation_fr_2070():
    assert (
V("redescendre").t('pp').realize()   
    ) == 'redescendu',\
    'redescendre:pp'


def test_conjugation_fr_2071():
    assert (
V("redescendre").t('s').pe(1).n('s').realize()   
    ) == 'redescende',\
    'redescendre:s1'


def test_conjugation_fr_2072():
    assert (
V("redescendre").t('s').pe(2).n('s').realize()   
    ) == 'redescendes',\
    'redescendre:s2'


def test_conjugation_fr_2073():
    assert (
V("redescendre").t('s').pe(3).n('s').realize()   
    ) == 'redescende',\
    'redescendre:s3'


def test_conjugation_fr_2074():
    assert (
V("redescendre").t('s').pe(1).n('p').realize()   
    ) == 'redescendions',\
    'redescendre:s4'


def test_conjugation_fr_2075():
    assert (
V("redescendre").t('s').pe(2).n('p').realize()   
    ) == 'redescendiez',\
    'redescendre:s5'


def test_conjugation_fr_2076():
    assert (
V("redescendre").t('s').pe(3).n('p').realize()   
    ) == 'redescendent',\
    'redescendre:s6'


def test_conjugation_fr_2077():
    assert (
V("redevenir").t('pr').realize()   
    ) == 'redevenant',\
    'redevenir:pr'


def test_conjugation_fr_2078():
    assert (
V("redevenir").t('p').pe(2).n('p').realize()   
    ) == 'redevenez',\
    'redevenir:p5'


def test_conjugation_fr_2079():
    assert (
V("redevenir").t('ip').pe(2).n('p').realize()   
    ) == 'redevenez',\
    'redevenir:ip5'


def test_conjugation_fr_2080():
    assert (
V("redevenir").t('p').pe(1).n('p').realize()   
    ) == 'redevenons',\
    'redevenir:p4'


def test_conjugation_fr_2081():
    assert (
V("redevenir").t('ip').pe(1).n('p').realize()   
    ) == 'redevenons',\
    'redevenir:ip4'


def test_conjugation_fr_2082():
    assert (
V("redevenir").t('p').pe(3).n('p').realize()   
    ) == 'redeviennent',\
    'redevenir:p6'


def test_conjugation_fr_2083():
    assert (
V("redevenir").t('p').pe(1).n('s').realize()   
    ) == 'redeviens',\
    'redevenir:p1'


def test_conjugation_fr_2084():
    assert (
V("redevenir").t('p').pe(2).n('s').realize()   
    ) == 'redeviens',\
    'redevenir:p2'


def test_conjugation_fr_2085():
    assert (
V("redevenir").t('ip').pe(2).n('s').realize()   
    ) == 'redeviens',\
    'redevenir:ip2'


def test_conjugation_fr_2086():
    assert (
V("redevenir").t('p').pe(3).n('s').realize()   
    ) == 'redevient',\
    'redevenir:p3'


def test_conjugation_fr_2087():
    assert (
V("redevenir").t('pp').realize()   
    ) == 'redevenu',\
    'redevenir:pp'


def test_conjugation_fr_2088():
    assert (
V("redevenir").t('s').pe(1).n('s').realize()   
    ) == 'redevienne',\
    'redevenir:s1'


def test_conjugation_fr_2089():
    assert (
V("redevenir").t('s').pe(2).n('s').realize()   
    ) == 'redeviennes',\
    'redevenir:s2'


def test_conjugation_fr_2090():
    assert (
V("redevenir").t('s').pe(3).n('s').realize()   
    ) == 'redevienne',\
    'redevenir:s3'


def test_conjugation_fr_2091():
    assert (
V("redevenir").t('s').pe(1).n('p').realize()   
    ) == 'redevenions',\
    'redevenir:s4'


def test_conjugation_fr_2092():
    assert (
V("redevenir").t('s').pe(2).n('p').realize()   
    ) == 'redeveniez',\
    'redevenir:s5'


def test_conjugation_fr_2093():
    assert (
V("redevenir").t('s').pe(3).n('p').realize()   
    ) == 'redeviennent',\
    'redevenir:s6'


def test_conjugation_fr_2094():
    assert (
V("redire").t('p').pe(1).n('s').realize()   
    ) == 'redis',\
    'redire:p1'


def test_conjugation_fr_2095():
    assert (
V("redire").t('p').pe(2).n('s').realize()   
    ) == 'redis',\
    'redire:p2'


def test_conjugation_fr_2096():
    assert (
V("redire").t('ip').pe(2).n('s').realize()   
    ) == 'redis',\
    'redire:ip2'


def test_conjugation_fr_2097():
    assert (
V("redire").t('pr').realize()   
    ) == 'redisant',\
    'redire:pr'


def test_conjugation_fr_2098():
    assert (
V("redire").t('p').pe(3).n('p').realize()   
    ) == 'redisent',\
    'redire:p6'


def test_conjugation_fr_2099():
    assert (
V("redire").t('p').pe(1).n('p').realize()   
    ) == 'redisons',\
    'redire:p4'


def test_conjugation_fr_2100():
    assert (
V("redire").t('ip').pe(1).n('p').realize()   
    ) == 'redisons',\
    'redire:ip4'


def test_conjugation_fr_2101():
    assert (
V("redire").t('p').pe(3).n('s').realize()   
    ) == 'redit',\
    'redire:p3'


def test_conjugation_fr_2102():
    assert (
V("redire").t('p').pe(2).n('p').realize()   
    ) == 'redites',\
    'redire:p5'


def test_conjugation_fr_2103():
    assert (
V("redire").t('ip').pe(2).n('p').realize()   
    ) == 'redites',\
    'redire:ip5'


def test_conjugation_fr_2104():
    assert (
V("redire").t('pp').realize()   
    ) == 'redit',\
    'redire:pp'


def test_conjugation_fr_2105():
    assert (
V("redire").t('s').pe(1).n('s').realize()   
    ) == 'redise',\
    'redire:s1'


def test_conjugation_fr_2106():
    assert (
V("redire").t('s').pe(2).n('s').realize()   
    ) == 'redises',\
    'redire:s2'


def test_conjugation_fr_2107():
    assert (
V("redire").t('s').pe(3).n('s').realize()   
    ) == 'redise',\
    'redire:s3'


def test_conjugation_fr_2108():
    assert (
V("redire").t('s').pe(1).n('p').realize()   
    ) == 'redisions',\
    'redire:s4'


def test_conjugation_fr_2109():
    assert (
V("redire").t('s').pe(2).n('p').realize()   
    ) == 'redisiez',\
    'redire:s5'


def test_conjugation_fr_2110():
    assert (
V("redire").t('s').pe(3).n('p').realize()   
    ) == 'redisent',\
    'redire:s6'


def test_conjugation_fr_2111():
    assert (
V("réduire").t('p').pe(1).n('s').realize()   
    ) == 'réduis',\
    'réduire:p1'


def test_conjugation_fr_2112():
    assert (
V("réduire").t('p').pe(2).n('s').realize()   
    ) == 'réduis',\
    'réduire:p2'


def test_conjugation_fr_2113():
    assert (
V("réduire").t('ip').pe(2).n('s').realize()   
    ) == 'réduis',\
    'réduire:ip2'


def test_conjugation_fr_2114():
    assert (
V("réduire").t('pr').realize()   
    ) == 'réduisant',\
    'réduire:pr'


def test_conjugation_fr_2115():
    assert (
V("réduire").t('p').pe(3).n('p').realize()   
    ) == 'réduisent',\
    'réduire:p6'


def test_conjugation_fr_2116():
    assert (
V("réduire").t('p').pe(2).n('p').realize()   
    ) == 'réduisez',\
    'réduire:p5'


def test_conjugation_fr_2117():
    assert (
V("réduire").t('ip').pe(2).n('p').realize()   
    ) == 'réduisez',\
    'réduire:ip5'


def test_conjugation_fr_2118():
    assert (
V("réduire").t('p').pe(1).n('p').realize()   
    ) == 'réduisons',\
    'réduire:p4'


def test_conjugation_fr_2119():
    assert (
V("réduire").t('ip').pe(1).n('p').realize()   
    ) == 'réduisons',\
    'réduire:ip4'


def test_conjugation_fr_2120():
    assert (
V("réduire").t('p').pe(3).n('s').realize()   
    ) == 'réduit',\
    'réduire:p3'


def test_conjugation_fr_2121():
    assert (
V("réduire").t('pp').realize()   
    ) == 'réduit',\
    'réduire:pp'


def test_conjugation_fr_2122():
    assert (
V("réduire").t('s').pe(1).n('s').realize()   
    ) == 'réduise',\
    'réduire:s1'


def test_conjugation_fr_2123():
    assert (
V("réduire").t('s').pe(2).n('s').realize()   
    ) == 'réduises',\
    'réduire:s2'


def test_conjugation_fr_2124():
    assert (
V("réduire").t('s').pe(3).n('s').realize()   
    ) == 'réduise',\
    'réduire:s3'


def test_conjugation_fr_2125():
    assert (
V("réduire").t('s').pe(1).n('p').realize()   
    ) == 'réduisions',\
    'réduire:s4'


def test_conjugation_fr_2126():
    assert (
V("réduire").t('s').pe(2).n('p').realize()   
    ) == 'réduisiez',\
    'réduire:s5'


def test_conjugation_fr_2127():
    assert (
V("réduire").t('s').pe(3).n('p').realize()   
    ) == 'réduisent',\
    'réduire:s6'


def test_conjugation_fr_2128():
    assert (
V("refaire").t('p').pe(1).n('s').realize()   
    ) == 'refais',\
    'refaire:p1'


def test_conjugation_fr_2129():
    assert (
V("refaire").t('p').pe(2).n('s').realize()   
    ) == 'refais',\
    'refaire:p2'


def test_conjugation_fr_2130():
    assert (
V("refaire").t('ip').pe(2).n('s').realize()   
    ) == 'refais',\
    'refaire:ip2'


def test_conjugation_fr_2131():
    assert (
V("refaire").t('pr').realize()   
    ) == 'refaisant',\
    'refaire:pr'


def test_conjugation_fr_2132():
    assert (
V("refaire").t('p').pe(1).n('p').realize()   
    ) == 'refaisons',\
    'refaire:p4'


def test_conjugation_fr_2133():
    assert (
V("refaire").t('ip').pe(1).n('p').realize()   
    ) == 'refaisons',\
    'refaire:ip4'


def test_conjugation_fr_2134():
    assert (
V("refaire").t('p').pe(3).n('s').realize()   
    ) == 'refait',\
    'refaire:p3'


def test_conjugation_fr_2135():
    assert (
V("refaire").t('p').pe(2).n('p').realize()   
    ) == 'refaites',\
    'refaire:p5'


def test_conjugation_fr_2136():
    assert (
V("refaire").t('ip').pe(2).n('p').realize()   
    ) == 'refaites',\
    'refaire:ip5'


def test_conjugation_fr_2137():
    assert (
V("refaire").t('p').pe(3).n('p').realize()   
    ) == 'refont',\
    'refaire:p6'


def test_conjugation_fr_2138():
    assert (
V("refaire").t('pp').realize()   
    ) == 'refait',\
    'refaire:pp'


def test_conjugation_fr_2139():
    assert (
V("refaire").t('s').pe(1).n('s').realize()   
    ) == 'refasse',\
    'refaire:s1'


def test_conjugation_fr_2140():
    assert (
V("refaire").t('s').pe(2).n('s').realize()   
    ) == 'refasses',\
    'refaire:s2'


def test_conjugation_fr_2141():
    assert (
V("refaire").t('s').pe(3).n('s').realize()   
    ) == 'refasse',\
    'refaire:s3'


def test_conjugation_fr_2142():
    assert (
V("refaire").t('s').pe(1).n('p').realize()   
    ) == 'refassions',\
    'refaire:s4'


def test_conjugation_fr_2143():
    assert (
V("refaire").t('s').pe(2).n('p').realize()   
    ) == 'refassiez',\
    'refaire:s5'


def test_conjugation_fr_2144():
    assert (
V("refaire").t('s').pe(3).n('p').realize()   
    ) == 'refassent',\
    'refaire:s6'


def test_conjugation_fr_2145():
    assert (
V("rejeter").t('p').pe(1).n('s').realize()   
    ) == 'rejette',\
    'rejeter:p1'


def test_conjugation_fr_2146():
    assert (
V("rejeter").t('p').pe(2).n('s').realize()   
    ) == 'rejettes',\
    'rejeter:p2'


def test_conjugation_fr_2147():
    assert (
V("rejeter").t('p').pe(3).n('s').realize()   
    ) == 'rejette',\
    'rejeter:p3'


def test_conjugation_fr_2148():
    assert (
V("rejeter").t('p').pe(3).n('p').realize()   
    ) == 'rejettent',\
    'rejeter:p6'


def test_conjugation_fr_2149():
    assert (
V("rejeter").t('s').pe(1).n('s').realize()   
    ) == 'rejette',\
    'rejeter:s1'


def test_conjugation_fr_2150():
    assert (
V("rejeter").t('s').pe(2).n('s').realize()   
    ) == 'rejettes',\
    'rejeter:s2'


def test_conjugation_fr_2151():
    assert (
V("rejeter").t('s').pe(3).n('s').realize()   
    ) == 'rejette',\
    'rejeter:s3'


def test_conjugation_fr_2152():
    assert (
V("rejeter").t('s').pe(1).n('p').realize()   
    ) == 'rejetions',\
    'rejeter:s4'


def test_conjugation_fr_2153():
    assert (
V("rejeter").t('s').pe(2).n('p').realize()   
    ) == 'rejetiez',\
    'rejeter:s5'


def test_conjugation_fr_2154():
    assert (
V("rejeter").t('s').pe(3).n('p').realize()   
    ) == 'rejettent',\
    'rejeter:s6'


def test_conjugation_fr_2155():
    assert (
V("rejoindre").t('pr').realize()   
    ) == 'rejoignant',\
    'rejoindre:pr'


def test_conjugation_fr_2156():
    assert (
V("rejoindre").t('p').pe(3).n('p').realize()   
    ) == 'rejoignent',\
    'rejoindre:p6'


def test_conjugation_fr_2157():
    assert (
V("rejoindre").t('p').pe(2).n('p').realize()   
    ) == 'rejoignez',\
    'rejoindre:p5'


def test_conjugation_fr_2158():
    assert (
V("rejoindre").t('ip').pe(2).n('p').realize()   
    ) == 'rejoignez',\
    'rejoindre:ip5'


def test_conjugation_fr_2159():
    assert (
V("rejoindre").t('p').pe(1).n('p').realize()   
    ) == 'rejoignons',\
    'rejoindre:p4'


def test_conjugation_fr_2160():
    assert (
V("rejoindre").t('ip').pe(1).n('p').realize()   
    ) == 'rejoignons',\
    'rejoindre:ip4'


def test_conjugation_fr_2161():
    assert (
V("rejoindre").t('p').pe(1).n('s').realize()   
    ) == 'rejoins',\
    'rejoindre:p1'


def test_conjugation_fr_2162():
    assert (
V("rejoindre").t('p').pe(2).n('s').realize()   
    ) == 'rejoins',\
    'rejoindre:p2'


def test_conjugation_fr_2163():
    assert (
V("rejoindre").t('ip').pe(2).n('s').realize()   
    ) == 'rejoins',\
    'rejoindre:ip2'


def test_conjugation_fr_2164():
    assert (
V("rejoindre").t('p').pe(3).n('s').realize()   
    ) == 'rejoint',\
    'rejoindre:p3'


def test_conjugation_fr_2165():
    assert (
V("rejoindre").t('pp').realize()   
    ) == 'rejoint',\
    'rejoindre:pp'


def test_conjugation_fr_2166():
    assert (
V("rejoindre").t('s').pe(1).n('s').realize()   
    ) == 'rejoigne',\
    'rejoindre:s1'


def test_conjugation_fr_2167():
    assert (
V("rejoindre").t('s').pe(2).n('s').realize()   
    ) == 'rejoignes',\
    'rejoindre:s2'


def test_conjugation_fr_2168():
    assert (
V("rejoindre").t('s').pe(3).n('s').realize()   
    ) == 'rejoigne',\
    'rejoindre:s3'


def test_conjugation_fr_2169():
    assert (
V("rejoindre").t('s').pe(1).n('p').realize()   
    ) == 'rejoignions',\
    'rejoindre:s4'


def test_conjugation_fr_2170():
    assert (
V("rejoindre").t('s').pe(2).n('p').realize()   
    ) == 'rejoigniez',\
    'rejoindre:s5'


def test_conjugation_fr_2171():
    assert (
V("rejoindre").t('s').pe(3).n('p').realize()   
    ) == 'rejoignent',\
    'rejoindre:s6'


def test_conjugation_fr_2172():
    assert (
V("relire").t('p').pe(1).n('s').realize()   
    ) == 'relis',\
    'relire:p1'


def test_conjugation_fr_2173():
    assert (
V("relire").t('p').pe(2).n('s').realize()   
    ) == 'relis',\
    'relire:p2'


def test_conjugation_fr_2174():
    assert (
V("relire").t('ip').pe(2).n('s').realize()   
    ) == 'relis',\
    'relire:ip2'


def test_conjugation_fr_2175():
    assert (
V("relire").t('pr').realize()   
    ) == 'relisant',\
    'relire:pr'


def test_conjugation_fr_2176():
    assert (
V("relire").t('p').pe(3).n('p').realize()   
    ) == 'relisent',\
    'relire:p6'


def test_conjugation_fr_2177():
    assert (
V("relire").t('p').pe(2).n('p').realize()   
    ) == 'relisez',\
    'relire:p5'


def test_conjugation_fr_2178():
    assert (
V("relire").t('ip').pe(2).n('p').realize()   
    ) == 'relisez',\
    'relire:ip5'


def test_conjugation_fr_2179():
    assert (
V("relire").t('p').pe(1).n('p').realize()   
    ) == 'relisons',\
    'relire:p4'


def test_conjugation_fr_2180():
    assert (
V("relire").t('ip').pe(1).n('p').realize()   
    ) == 'relisons',\
    'relire:ip4'


def test_conjugation_fr_2181():
    assert (
V("relire").t('p').pe(3).n('s').realize()   
    ) == 'relit',\
    'relire:p3'


def test_conjugation_fr_2182():
    assert (
V("relire").t('pp').realize()   
    ) == 'relu',\
    'relire:pp'


def test_conjugation_fr_2183():
    assert (
V("relire").t('s').pe(1).n('s').realize()   
    ) == 'relise',\
    'relire:s1'


def test_conjugation_fr_2184():
    assert (
V("relire").t('s').pe(2).n('s').realize()   
    ) == 'relises',\
    'relire:s2'


def test_conjugation_fr_2185():
    assert (
V("relire").t('s').pe(3).n('s').realize()   
    ) == 'relise',\
    'relire:s3'


def test_conjugation_fr_2186():
    assert (
V("relire").t('s').pe(1).n('p').realize()   
    ) == 'relisions',\
    'relire:s4'


def test_conjugation_fr_2187():
    assert (
V("relire").t('s').pe(2).n('p').realize()   
    ) == 'relisiez',\
    'relire:s5'


def test_conjugation_fr_2188():
    assert (
V("relire").t('s').pe(3).n('p').realize()   
    ) == 'relisent',\
    'relire:s6'


def test_conjugation_fr_2189():
    assert (
V("remettre").t('p').pe(3).n('s').realize()   
    ) == 'remet',\
    'remettre:p3'


def test_conjugation_fr_2190():
    assert (
V("remettre").t('p').pe(1).n('s').realize()   
    ) == 'remets',\
    'remettre:p1'


def test_conjugation_fr_2191():
    assert (
V("remettre").t('p').pe(2).n('s').realize()   
    ) == 'remets',\
    'remettre:p2'


def test_conjugation_fr_2192():
    assert (
V("remettre").t('ip').pe(2).n('s').realize()   
    ) == 'remets',\
    'remettre:ip2'


def test_conjugation_fr_2193():
    assert (
V("remettre").t('pr').realize()   
    ) == 'remettant',\
    'remettre:pr'


def test_conjugation_fr_2194():
    assert (
V("remettre").t('p').pe(3).n('p').realize()   
    ) == 'remettent',\
    'remettre:p6'


def test_conjugation_fr_2195():
    assert (
V("remettre").t('p').pe(2).n('p').realize()   
    ) == 'remettez',\
    'remettre:p5'


def test_conjugation_fr_2196():
    assert (
V("remettre").t('ip').pe(2).n('p').realize()   
    ) == 'remettez',\
    'remettre:ip5'


def test_conjugation_fr_2197():
    assert (
V("remettre").t('p').pe(1).n('p').realize()   
    ) == 'remettons',\
    'remettre:p4'


def test_conjugation_fr_2198():
    assert (
V("remettre").t('ip').pe(1).n('p').realize()   
    ) == 'remettons',\
    'remettre:ip4'


def test_conjugation_fr_2199():
    assert (
V("remettre").t('pp').realize()   
    ) == 'remis',\
    'remettre:pp'


def test_conjugation_fr_2200():
    assert (
V("remettre").t('s').pe(1).n('s').realize()   
    ) == 'remette',\
    'remettre:s1'


def test_conjugation_fr_2201():
    assert (
V("remettre").t('s').pe(2).n('s').realize()   
    ) == 'remettes',\
    'remettre:s2'


def test_conjugation_fr_2202():
    assert (
V("remettre").t('s').pe(3).n('s').realize()   
    ) == 'remette',\
    'remettre:s3'


def test_conjugation_fr_2203():
    assert (
V("remettre").t('s').pe(1).n('p').realize()   
    ) == 'remettions',\
    'remettre:s4'


def test_conjugation_fr_2204():
    assert (
V("remettre").t('s').pe(2).n('p').realize()   
    ) == 'remettiez',\
    'remettre:s5'


def test_conjugation_fr_2205():
    assert (
V("remettre").t('s').pe(3).n('p').realize()   
    ) == 'remettent',\
    'remettre:s6'


def test_conjugation_fr_2206():
    assert (
V("renaître").t('p').pe(1).n('s').realize()   
    ) == 'renais',\
    'renaître:p1'


def test_conjugation_fr_2207():
    assert (
V("renaître").t('p').pe(2).n('s').realize()   
    ) == 'renais',\
    'renaître:p2'


def test_conjugation_fr_2208():
    assert (
V("renaître").t('ip').pe(2).n('s').realize()   
    ) == 'renais',\
    'renaître:ip2'


def test_conjugation_fr_2209():
    assert (
V("renaître").t('pr').realize()   
    ) == 'renaissant',\
    'renaître:pr'


def test_conjugation_fr_2210():
    assert (
V("renaître").t('p').pe(3).n('p').realize()   
    ) == 'renaissent',\
    'renaître:p6'


def test_conjugation_fr_2211():
    assert (
V("renaître").t('p').pe(2).n('p').realize()   
    ) == 'renaissez',\
    'renaître:p5'


def test_conjugation_fr_2212():
    assert (
V("renaître").t('ip').pe(2).n('p').realize()   
    ) == 'renaissez',\
    'renaître:ip5'


def test_conjugation_fr_2213():
    assert (
V("renaître").t('p').pe(1).n('p').realize()   
    ) == 'renaissons',\
    'renaître:p4'


def test_conjugation_fr_2214():
    assert (
V("renaître").t('ip').pe(1).n('p').realize()   
    ) == 'renaissons',\
    'renaître:ip4'


def test_conjugation_fr_2215():
    assert (
V("renaître").t('p').pe(3).n('s').realize()   
    ) == 'renaît',\
    'renaître:p3'


def test_conjugation_fr_2216():
    assert (
V("renaître").t('s').pe(1).n('s').realize()   
    ) == 'renaisse',\
    'renaître:s1'


def test_conjugation_fr_2217():
    assert (
V("renaître").t('s').pe(2).n('s').realize()   
    ) == 'renaisses',\
    'renaître:s2'


def test_conjugation_fr_2218():
    assert (
V("renaître").t('s').pe(3).n('s').realize()   
    ) == 'renaisse',\
    'renaître:s3'


def test_conjugation_fr_2219():
    assert (
V("renaître").t('s').pe(1).n('p').realize()   
    ) == 'renaissions',\
    'renaître:s4'


def test_conjugation_fr_2220():
    assert (
V("renaître").t('s').pe(2).n('p').realize()   
    ) == 'renaissiez',\
    'renaître:s5'


def test_conjugation_fr_2221():
    assert (
V("renaître").t('s').pe(3).n('p').realize()   
    ) == 'renaissent',\
    'renaître:s6'


def test_conjugation_fr_2222():
    assert (
V("rendre").t('p').pe(3).n('s').realize()   
    ) == 'rend',\
    'rendre:p3'


def test_conjugation_fr_2223():
    assert (
V("rendre").t('pr').realize()   
    ) == 'rendant',\
    'rendre:pr'


def test_conjugation_fr_2224():
    assert (
V("rendre").t('p').pe(3).n('p').realize()   
    ) == 'rendent',\
    'rendre:p6'


def test_conjugation_fr_2225():
    assert (
V("rendre").t('p').pe(2).n('p').realize()   
    ) == 'rendez',\
    'rendre:p5'


def test_conjugation_fr_2226():
    assert (
V("rendre").t('ip').pe(2).n('p').realize()   
    ) == 'rendez',\
    'rendre:ip5'


def test_conjugation_fr_2227():
    assert (
V("rendre").t('p').pe(1).n('p').realize()   
    ) == 'rendons',\
    'rendre:p4'


def test_conjugation_fr_2228():
    assert (
V("rendre").t('ip').pe(1).n('p').realize()   
    ) == 'rendons',\
    'rendre:ip4'


def test_conjugation_fr_2229():
    assert (
V("rendre").t('p').pe(1).n('s').realize()   
    ) == 'rends',\
    'rendre:p1'


def test_conjugation_fr_2230():
    assert (
V("rendre").t('p').pe(2).n('s').realize()   
    ) == 'rends',\
    'rendre:p2'


def test_conjugation_fr_2231():
    assert (
V("rendre").t('ip').pe(2).n('s').realize()   
    ) == 'rends',\
    'rendre:ip2'


def test_conjugation_fr_2232():
    assert (
V("rendre").t('pp').realize()   
    ) == 'rendu',\
    'rendre:pp'


def test_conjugation_fr_2233():
    assert (
V("rendre").t('s').pe(1).n('s').realize()   
    ) == 'rende',\
    'rendre:s1'


def test_conjugation_fr_2234():
    assert (
V("rendre").t('s').pe(2).n('s').realize()   
    ) == 'rendes',\
    'rendre:s2'


def test_conjugation_fr_2235():
    assert (
V("rendre").t('s').pe(3).n('s').realize()   
    ) == 'rende',\
    'rendre:s3'


def test_conjugation_fr_2236():
    assert (
V("rendre").t('s').pe(1).n('p').realize()   
    ) == 'rendions',\
    'rendre:s4'


def test_conjugation_fr_2237():
    assert (
V("rendre").t('s').pe(2).n('p').realize()   
    ) == 'rendiez',\
    'rendre:s5'


def test_conjugation_fr_2238():
    assert (
V("rendre").t('s').pe(3).n('p').realize()   
    ) == 'rendent',\
    'rendre:s6'


def test_conjugation_fr_2239():
    assert (
V("renouveler").t('p').pe(1).n('s').realize()   
    ) == 'renouvelle',\
    'renouveler:p1'


def test_conjugation_fr_2240():
    assert (
V("renouveler").t('p').pe(2).n('s').realize()   
    ) == 'renouvelles',\
    'renouveler:p2'


def test_conjugation_fr_2241():
    assert (
V("renouveler").t('p').pe(3).n('s').realize()   
    ) == 'renouvelle',\
    'renouveler:p3'


def test_conjugation_fr_2242():
    assert (
V("renouveler").t('p').pe(3).n('p').realize()   
    ) == 'renouvellent',\
    'renouveler:p6'


def test_conjugation_fr_2243():
    assert (
V("renouveler").t('s').pe(1).n('s').realize()   
    ) == 'renouvelle',\
    'renouveler:s1'


def test_conjugation_fr_2244():
    assert (
V("renouveler").t('s').pe(2).n('s').realize()   
    ) == 'renouvelles',\
    'renouveler:s2'


def test_conjugation_fr_2245():
    assert (
V("renouveler").t('s').pe(3).n('s').realize()   
    ) == 'renouvelle',\
    'renouveler:s3'


def test_conjugation_fr_2246():
    assert (
V("renouveler").t('s').pe(1).n('p').realize()   
    ) == 'renouvelions',\
    'renouveler:s4'


def test_conjugation_fr_2247():
    assert (
V("renouveler").t('s').pe(2).n('p').realize()   
    ) == 'renouveliez',\
    'renouveler:s5'


def test_conjugation_fr_2248():
    assert (
V("renouveler").t('s').pe(3).n('p').realize()   
    ) == 'renouvellent',\
    'renouveler:s6'


def test_conjugation_fr_2249():
    assert (
V("répandre").t('p').pe(3).n('s').realize()   
    ) == 'répand',\
    'répandre:p3'


def test_conjugation_fr_2250():
    assert (
V("répandre").t('pr').realize()   
    ) == 'répandant',\
    'répandre:pr'


def test_conjugation_fr_2251():
    assert (
V("répandre").t('p').pe(3).n('p').realize()   
    ) == 'répandent',\
    'répandre:p6'


def test_conjugation_fr_2252():
    assert (
V("répandre").t('p').pe(2).n('p').realize()   
    ) == 'répandez',\
    'répandre:p5'


def test_conjugation_fr_2253():
    assert (
V("répandre").t('ip').pe(2).n('p').realize()   
    ) == 'répandez',\
    'répandre:ip5'


def test_conjugation_fr_2254():
    assert (
V("répandre").t('p').pe(1).n('p').realize()   
    ) == 'répandons',\
    'répandre:p4'


def test_conjugation_fr_2255():
    assert (
V("répandre").t('ip').pe(1).n('p').realize()   
    ) == 'répandons',\
    'répandre:ip4'


def test_conjugation_fr_2256():
    assert (
V("répandre").t('p').pe(1).n('s').realize()   
    ) == 'répands',\
    'répandre:p1'


def test_conjugation_fr_2257():
    assert (
V("répandre").t('p').pe(2).n('s').realize()   
    ) == 'répands',\
    'répandre:p2'


def test_conjugation_fr_2258():
    assert (
V("répandre").t('ip').pe(2).n('s').realize()   
    ) == 'répands',\
    'répandre:ip2'


def test_conjugation_fr_2259():
    assert (
V("répandre").t('pp').realize()   
    ) == 'répandu',\
    'répandre:pp'


def test_conjugation_fr_2260():
    assert (
V("répandre").t('s').pe(1).n('s').realize()   
    ) == 'répande',\
    'répandre:s1'


def test_conjugation_fr_2261():
    assert (
V("répandre").t('s').pe(2).n('s').realize()   
    ) == 'répandes',\
    'répandre:s2'


def test_conjugation_fr_2262():
    assert (
V("répandre").t('s').pe(3).n('s').realize()   
    ) == 'répande',\
    'répandre:s3'


def test_conjugation_fr_2263():
    assert (
V("répandre").t('s').pe(1).n('p').realize()   
    ) == 'répandions',\
    'répandre:s4'


def test_conjugation_fr_2264():
    assert (
V("répandre").t('s').pe(2).n('p').realize()   
    ) == 'répandiez',\
    'répandre:s5'


def test_conjugation_fr_2265():
    assert (
V("répandre").t('s').pe(3).n('p').realize()   
    ) == 'répandent',\
    'répandre:s6'


def test_conjugation_fr_2266():
    assert (
V("reparaître").t('p').pe(1).n('s').realize()   
    ) == 'reparais',\
    'reparaître:p1'


def test_conjugation_fr_2267():
    assert (
V("reparaître").t('p').pe(2).n('s').realize()   
    ) == 'reparais',\
    'reparaître:p2'


def test_conjugation_fr_2268():
    assert (
V("reparaître").t('ip').pe(2).n('s').realize()   
    ) == 'reparais',\
    'reparaître:ip2'


def test_conjugation_fr_2269():
    assert (
V("reparaître").t('pr').realize()   
    ) == 'reparaissant',\
    'reparaître:pr'


def test_conjugation_fr_2270():
    assert (
V("reparaître").t('p').pe(3).n('p').realize()   
    ) == 'reparaissent',\
    'reparaître:p6'


def test_conjugation_fr_2271():
    assert (
V("reparaître").t('p').pe(2).n('p').realize()   
    ) == 'reparaissez',\
    'reparaître:p5'


def test_conjugation_fr_2272():
    assert (
V("reparaître").t('ip').pe(2).n('p').realize()   
    ) == 'reparaissez',\
    'reparaître:ip5'


def test_conjugation_fr_2273():
    assert (
V("reparaître").t('p').pe(1).n('p').realize()   
    ) == 'reparaissons',\
    'reparaître:p4'


def test_conjugation_fr_2274():
    assert (
V("reparaître").t('ip').pe(1).n('p').realize()   
    ) == 'reparaissons',\
    'reparaître:ip4'


def test_conjugation_fr_2275():
    assert (
V("reparaître").t('p').pe(3).n('s').realize()   
    ) == 'reparaît',\
    'reparaître:p3'


def test_conjugation_fr_2276():
    assert (
V("reparaître").t('pp').realize()   
    ) == 'reparu',\
    'reparaître:pp'


def test_conjugation_fr_2277():
    assert (
V("reparaître").t('s').pe(1).n('s').realize()   
    ) == 'reparaisse',\
    'reparaître:s1'


def test_conjugation_fr_2278():
    assert (
V("reparaître").t('s').pe(2).n('s').realize()   
    ) == 'reparaisses',\
    'reparaître:s2'


def test_conjugation_fr_2279():
    assert (
V("reparaître").t('s').pe(3).n('s').realize()   
    ) == 'reparaisse',\
    'reparaître:s3'


def test_conjugation_fr_2280():
    assert (
V("reparaître").t('s').pe(1).n('p').realize()   
    ) == 'reparaissions',\
    'reparaître:s4'


def test_conjugation_fr_2281():
    assert (
V("reparaître").t('s').pe(2).n('p').realize()   
    ) == 'reparaissiez',\
    'reparaître:s5'


def test_conjugation_fr_2282():
    assert (
V("reparaître").t('s').pe(3).n('p').realize()   
    ) == 'reparaissent',\
    'reparaître:s6'


def test_conjugation_fr_2283():
    assert (
V("repentir").t('p').pe(1).n('s').realize()   
    ) == 'me repens',\
    'repentir:p1'


def test_conjugation_fr_2284():
    assert (
V("repentir").t('p').pe(2).n('s').realize()   
    ) == 'te repens',\
    'repentir:p2'


def test_conjugation_fr_2285():
    assert (
V("repentir").t('ip').pe(2).n('s').realize()   
    ) == 'repens-toi',\
    'repentir:ip2'


def test_conjugation_fr_2286():
    assert (
V("repentir").t('p').pe(3).n('s').realize()   
    ) == 'se repent',\
    'repentir:p3'


def test_conjugation_fr_2287():
    assert (
V("repentir").t('pr').realize()   
    ) == 'se repentant',\
    'repentir:pr'


def test_conjugation_fr_2288():
    assert (
V("repentir").t('p').pe(3).n('p').realize()   
    ) == 'se repentent',\
    'repentir:p6'


def test_conjugation_fr_2289():
    assert (
V("repentir").t('p').pe(2).n('p').realize()   
    ) == 'vous repentez',\
    'repentir:p5'


def test_conjugation_fr_2290():
    assert (
V("repentir").t('ip').pe(2).n('p').realize()   
    ) == 'repentez-vous',\
    'repentir:ip5'


def test_conjugation_fr_2291():
    assert (
V("repentir").t('p').pe(1).n('p').realize()   
    ) == 'nous repentons',\
    'repentir:p4'


def test_conjugation_fr_2292():
    assert (
V("repentir").t('ip').pe(1).n('p').realize()   
    ) == 'repentons-nous',\
    'repentir:ip4'


def test_conjugation_fr_2293():
    assert (
V("repentir").t('pp').realize()   
    ) == 'repenti',\
    'repentir:pp'


def test_conjugation_fr_2294():
    assert (
V("repentir").t('s').pe(1).n('s').realize()   
    ) == 'me repente',\
    'repentir:s1'


def test_conjugation_fr_2295():
    assert (
V("repentir").t('s').pe(2).n('s').realize()   
    ) == 'te repentes',\
    'repentir:s2'


def test_conjugation_fr_2296():
    assert (
V("repentir").t('s').pe(3).n('s').realize()   
    ) == 'se repente',\
    'repentir:s3'


def test_conjugation_fr_2297():
    assert (
V("repentir").t('s').pe(1).n('p').realize()   
    ) == 'nous repentions',\
    'repentir:s4'


def test_conjugation_fr_2298():
    assert (
V("repentir").t('s').pe(2).n('p').realize()   
    ) == 'vous repentiez',\
    'repentir:s5'


def test_conjugation_fr_2299():
    assert (
V("repentir").t('s').pe(3).n('p').realize()   
    ) == 'se repentent',\
    'repentir:s6'


def test_conjugation_fr_2300():
    assert (
V("répondre").t('p').pe(3).n('s').realize()   
    ) == 'répond',\
    'répondre:p3'


def test_conjugation_fr_2301():
    assert (
V("répondre").t('pr').realize()   
    ) == 'répondant',\
    'répondre:pr'


def test_conjugation_fr_2302():
    assert (
V("répondre").t('p').pe(3).n('p').realize()   
    ) == 'répondent',\
    'répondre:p6'


def test_conjugation_fr_2303():
    assert (
V("répondre").t('p').pe(2).n('p').realize()   
    ) == 'répondez',\
    'répondre:p5'


def test_conjugation_fr_2304():
    assert (
V("répondre").t('ip').pe(2).n('p').realize()   
    ) == 'répondez',\
    'répondre:ip5'


def test_conjugation_fr_2305():
    assert (
V("répondre").t('p').pe(1).n('p').realize()   
    ) == 'répondons',\
    'répondre:p4'


def test_conjugation_fr_2306():
    assert (
V("répondre").t('ip').pe(1).n('p').realize()   
    ) == 'répondons',\
    'répondre:ip4'


def test_conjugation_fr_2307():
    assert (
V("répondre").t('p').pe(1).n('s').realize()   
    ) == 'réponds',\
    'répondre:p1'


def test_conjugation_fr_2308():
    assert (
V("répondre").t('p').pe(2).n('s').realize()   
    ) == 'réponds',\
    'répondre:p2'


def test_conjugation_fr_2309():
    assert (
V("répondre").t('ip').pe(2).n('s').realize()   
    ) == 'réponds',\
    'répondre:ip2'


def test_conjugation_fr_2310():
    assert (
V("répondre").t('pp').realize()   
    ) == 'répondu',\
    'répondre:pp'


def test_conjugation_fr_2311():
    assert (
V("répondre").t('s').pe(1).n('s').realize()   
    ) == 'réponde',\
    'répondre:s1'


def test_conjugation_fr_2312():
    assert (
V("répondre").t('s').pe(2).n('s').realize()   
    ) == 'répondes',\
    'répondre:s2'


def test_conjugation_fr_2313():
    assert (
V("répondre").t('s').pe(3).n('s').realize()   
    ) == 'réponde',\
    'répondre:s3'


def test_conjugation_fr_2314():
    assert (
V("répondre").t('s').pe(1).n('p').realize()   
    ) == 'répondions',\
    'répondre:s4'


def test_conjugation_fr_2315():
    assert (
V("répondre").t('s').pe(2).n('p').realize()   
    ) == 'répondiez',\
    'répondre:s5'


def test_conjugation_fr_2316():
    assert (
V("répondre").t('s').pe(3).n('p').realize()   
    ) == 'répondent',\
    'répondre:s6'


def test_conjugation_fr_2317():
    assert (
V("reprendre").t('pr').realize()   
    ) == 'reprenant',\
    'reprendre:pr'


def test_conjugation_fr_2318():
    assert (
V("reprendre").t('p').pe(3).n('s').realize()   
    ) == 'reprend',\
    'reprendre:p3'


def test_conjugation_fr_2319():
    assert (
V("reprendre").t('p').pe(1).n('s').realize()   
    ) == 'reprends',\
    'reprendre:p1'


def test_conjugation_fr_2320():
    assert (
V("reprendre").t('p').pe(2).n('s').realize()   
    ) == 'reprends',\
    'reprendre:p2'


def test_conjugation_fr_2321():
    assert (
V("reprendre").t('ip').pe(2).n('s').realize()   
    ) == 'reprends',\
    'reprendre:ip2'


def test_conjugation_fr_2322():
    assert (
V("reprendre").t('p').pe(2).n('p').realize()   
    ) == 'reprenez',\
    'reprendre:p5'


def test_conjugation_fr_2323():
    assert (
V("reprendre").t('ip').pe(2).n('p').realize()   
    ) == 'reprenez',\
    'reprendre:ip5'


def test_conjugation_fr_2324():
    assert (
V("reprendre").t('p').pe(3).n('p').realize()   
    ) == 'reprennent',\
    'reprendre:p6'


def test_conjugation_fr_2325():
    assert (
V("reprendre").t('p').pe(1).n('p').realize()   
    ) == 'reprenons',\
    'reprendre:p4'


def test_conjugation_fr_2326():
    assert (
V("reprendre").t('ip').pe(1).n('p').realize()   
    ) == 'reprenons',\
    'reprendre:ip4'


def test_conjugation_fr_2327():
    assert (
V("reprendre").t('pp').realize()   
    ) == 'repris',\
    'reprendre:pp'


def test_conjugation_fr_2328():
    assert (
V("reprendre").t('s').pe(1).n('s').realize()   
    ) == 'reprenne',\
    'reprendre:s1'


def test_conjugation_fr_2329():
    assert (
V("reprendre").t('s').pe(2).n('s').realize()   
    ) == 'reprennes',\
    'reprendre:s2'


def test_conjugation_fr_2330():
    assert (
V("reprendre").t('s').pe(3).n('s').realize()   
    ) == 'reprenne',\
    'reprendre:s3'


def test_conjugation_fr_2331():
    assert (
V("reprendre").t('s').pe(1).n('p').realize()   
    ) == 'reprenions',\
    'reprendre:s4'


def test_conjugation_fr_2332():
    assert (
V("reprendre").t('s').pe(2).n('p').realize()   
    ) == 'repreniez',\
    'reprendre:s5'


def test_conjugation_fr_2333():
    assert (
V("reprendre").t('s').pe(3).n('p').realize()   
    ) == 'reprennent',\
    'reprendre:s6'


def test_conjugation_fr_2334():
    assert (
V("résoudre").t('pr').realize()   
    ) == 'résolvant',\
    'résoudre:pr'


def test_conjugation_fr_2335():
    assert (
V("résoudre").t('p').pe(3).n('p').realize()   
    ) == 'résolvent',\
    'résoudre:p6'


def test_conjugation_fr_2336():
    assert (
V("résoudre").t('p').pe(2).n('p').realize()   
    ) == 'résolvez',\
    'résoudre:p5'


def test_conjugation_fr_2337():
    assert (
V("résoudre").t('ip').pe(2).n('p').realize()   
    ) == 'résolvez',\
    'résoudre:ip5'


def test_conjugation_fr_2338():
    assert (
V("résoudre").t('p').pe(1).n('p').realize()   
    ) == 'résolvons',\
    'résoudre:p4'


def test_conjugation_fr_2339():
    assert (
V("résoudre").t('ip').pe(1).n('p').realize()   
    ) == 'résolvons',\
    'résoudre:ip4'


def test_conjugation_fr_2340():
    assert (
V("résoudre").t('p').pe(1).n('s').realize()   
    ) == 'résous',\
    'résoudre:p1'


def test_conjugation_fr_2341():
    assert (
V("résoudre").t('p').pe(2).n('s').realize()   
    ) == 'résous',\
    'résoudre:p2'


def test_conjugation_fr_2342():
    assert (
V("résoudre").t('ip').pe(2).n('s').realize()   
    ) == 'résous',\
    'résoudre:ip2'


def test_conjugation_fr_2343():
    assert (
V("résoudre").t('p').pe(3).n('s').realize()   
    ) == 'résout',\
    'résoudre:p3'


def test_conjugation_fr_2344():
    assert (
V("résoudre").t('pp').realize()   
    ) == 'résolu',\
    'résoudre:pp'


def test_conjugation_fr_2345():
    assert (
V("résoudre").t('s').pe(1).n('s').realize()   
    ) == 'résolve',\
    'résoudre:s1'


def test_conjugation_fr_2346():
    assert (
V("résoudre").t('s').pe(2).n('s').realize()   
    ) == 'résolves',\
    'résoudre:s2'


def test_conjugation_fr_2347():
    assert (
V("résoudre").t('s').pe(3).n('s').realize()   
    ) == 'résolve',\
    'résoudre:s3'


def test_conjugation_fr_2348():
    assert (
V("résoudre").t('s').pe(1).n('p').realize()   
    ) == 'résolvions',\
    'résoudre:s4'


def test_conjugation_fr_2349():
    assert (
V("résoudre").t('s').pe(2).n('p').realize()   
    ) == 'résolviez',\
    'résoudre:s5'


def test_conjugation_fr_2350():
    assert (
V("résoudre").t('s').pe(3).n('p').realize()   
    ) == 'résolvent',\
    'résoudre:s6'


def test_conjugation_fr_2351():
    assert (
V("ressentir").t('p').pe(1).n('s').realize()   
    ) == 'ressens',\
    'ressentir:p1'


def test_conjugation_fr_2352():
    assert (
V("ressentir").t('p').pe(2).n('s').realize()   
    ) == 'ressens',\
    'ressentir:p2'


def test_conjugation_fr_2353():
    assert (
V("ressentir").t('ip').pe(2).n('s').realize()   
    ) == 'ressens',\
    'ressentir:ip2'


def test_conjugation_fr_2354():
    assert (
V("ressentir").t('p').pe(3).n('s').realize()   
    ) == 'ressent',\
    'ressentir:p3'


def test_conjugation_fr_2355():
    assert (
V("ressentir").t('pr').realize()   
    ) == 'ressentant',\
    'ressentir:pr'


def test_conjugation_fr_2356():
    assert (
V("ressentir").t('p').pe(3).n('p').realize()   
    ) == 'ressentent',\
    'ressentir:p6'


def test_conjugation_fr_2357():
    assert (
V("ressentir").t('p').pe(2).n('p').realize()   
    ) == 'ressentez',\
    'ressentir:p5'


def test_conjugation_fr_2358():
    assert (
V("ressentir").t('ip').pe(2).n('p').realize()   
    ) == 'ressentez',\
    'ressentir:ip5'


def test_conjugation_fr_2359():
    assert (
V("ressentir").t('p').pe(1).n('p').realize()   
    ) == 'ressentons',\
    'ressentir:p4'


def test_conjugation_fr_2360():
    assert (
V("ressentir").t('ip').pe(1).n('p').realize()   
    ) == 'ressentons',\
    'ressentir:ip4'


def test_conjugation_fr_2361():
    assert (
V("ressentir").t('pp').realize()   
    ) == 'ressenti',\
    'ressentir:pp'


def test_conjugation_fr_2362():
    assert (
V("ressentir").t('s').pe(1).n('s').realize()   
    ) == 'ressente',\
    'ressentir:s1'


def test_conjugation_fr_2363():
    assert (
V("ressentir").t('s').pe(2).n('s').realize()   
    ) == 'ressentes',\
    'ressentir:s2'


def test_conjugation_fr_2364():
    assert (
V("ressentir").t('s').pe(3).n('s').realize()   
    ) == 'ressente',\
    'ressentir:s3'


def test_conjugation_fr_2365():
    assert (
V("ressentir").t('s').pe(1).n('p').realize()   
    ) == 'ressentions',\
    'ressentir:s4'


def test_conjugation_fr_2366():
    assert (
V("ressentir").t('s').pe(2).n('p').realize()   
    ) == 'ressentiez',\
    'ressentir:s5'


def test_conjugation_fr_2367():
    assert (
V("ressentir").t('s').pe(3).n('p').realize()   
    ) == 'ressentent',\
    'ressentir:s6'


def test_conjugation_fr_2368():
    assert (
V("retenir").t('pr').realize()   
    ) == 'retenant',\
    'retenir:pr'


def test_conjugation_fr_2369():
    assert (
V("retenir").t('p').pe(2).n('p').realize()   
    ) == 'retenez',\
    'retenir:p5'


def test_conjugation_fr_2370():
    assert (
V("retenir").t('ip').pe(2).n('p').realize()   
    ) == 'retenez',\
    'retenir:ip5'


def test_conjugation_fr_2371():
    assert (
V("retenir").t('p').pe(1).n('p').realize()   
    ) == 'retenons',\
    'retenir:p4'


def test_conjugation_fr_2372():
    assert (
V("retenir").t('ip').pe(1).n('p').realize()   
    ) == 'retenons',\
    'retenir:ip4'


def test_conjugation_fr_2373():
    assert (
V("retenir").t('p').pe(3).n('p').realize()   
    ) == 'retiennent',\
    'retenir:p6'


def test_conjugation_fr_2374():
    assert (
V("retenir").t('p').pe(1).n('s').realize()   
    ) == 'retiens',\
    'retenir:p1'


def test_conjugation_fr_2375():
    assert (
V("retenir").t('p').pe(2).n('s').realize()   
    ) == 'retiens',\
    'retenir:p2'


def test_conjugation_fr_2376():
    assert (
V("retenir").t('ip').pe(2).n('s').realize()   
    ) == 'retiens',\
    'retenir:ip2'


def test_conjugation_fr_2377():
    assert (
V("retenir").t('p').pe(3).n('s').realize()   
    ) == 'retient',\
    'retenir:p3'


def test_conjugation_fr_2378():
    assert (
V("retenir").t('pp').realize()   
    ) == 'retenu',\
    'retenir:pp'


def test_conjugation_fr_2379():
    assert (
V("retenir").t('s').pe(1).n('s').realize()   
    ) == 'retienne',\
    'retenir:s1'


def test_conjugation_fr_2380():
    assert (
V("retenir").t('s').pe(2).n('s').realize()   
    ) == 'retiennes',\
    'retenir:s2'


def test_conjugation_fr_2381():
    assert (
V("retenir").t('s').pe(3).n('s').realize()   
    ) == 'retienne',\
    'retenir:s3'


def test_conjugation_fr_2382():
    assert (
V("retenir").t('s').pe(1).n('p').realize()   
    ) == 'retenions',\
    'retenir:s4'


def test_conjugation_fr_2383():
    assert (
V("retenir").t('s').pe(2).n('p').realize()   
    ) == 'reteniez',\
    'retenir:s5'


def test_conjugation_fr_2384():
    assert (
V("retenir").t('s').pe(3).n('p').realize()   
    ) == 'retiennent',\
    'retenir:s6'


def test_conjugation_fr_2385():
    assert (
V("revenir").t('pr').realize()   
    ) == 'revenant',\
    'revenir:pr'


def test_conjugation_fr_2386():
    assert (
V("revenir").t('p').pe(2).n('p').realize()   
    ) == 'revenez',\
    'revenir:p5'


def test_conjugation_fr_2387():
    assert (
V("revenir").t('ip').pe(2).n('p').realize()   
    ) == 'revenez',\
    'revenir:ip5'


def test_conjugation_fr_2388():
    assert (
V("revenir").t('p').pe(1).n('p').realize()   
    ) == 'revenons',\
    'revenir:p4'


def test_conjugation_fr_2389():
    assert (
V("revenir").t('ip').pe(1).n('p').realize()   
    ) == 'revenons',\
    'revenir:ip4'


def test_conjugation_fr_2390():
    assert (
V("revenir").t('p').pe(3).n('p').realize()   
    ) == 'reviennent',\
    'revenir:p6'


def test_conjugation_fr_2391():
    assert (
V("revenir").t('p').pe(1).n('s').realize()   
    ) == 'reviens',\
    'revenir:p1'


def test_conjugation_fr_2392():
    assert (
V("revenir").t('p').pe(2).n('s').realize()   
    ) == 'reviens',\
    'revenir:p2'


def test_conjugation_fr_2393():
    assert (
V("revenir").t('ip').pe(2).n('s').realize()   
    ) == 'reviens',\
    'revenir:ip2'


def test_conjugation_fr_2394():
    assert (
V("revenir").t('p').pe(3).n('s').realize()   
    ) == 'revient',\
    'revenir:p3'


def test_conjugation_fr_2395():
    assert (
V("revenir").t('pp').realize()   
    ) == 'revenu',\
    'revenir:pp'


def test_conjugation_fr_2396():
    assert (
V("revenir").t('s').pe(1).n('s').realize()   
    ) == 'revienne',\
    'revenir:s1'


def test_conjugation_fr_2397():
    assert (
V("revenir").t('s').pe(2).n('s').realize()   
    ) == 'reviennes',\
    'revenir:s2'


def test_conjugation_fr_2398():
    assert (
V("revenir").t('s').pe(3).n('s').realize()   
    ) == 'revienne',\
    'revenir:s3'


def test_conjugation_fr_2399():
    assert (
V("revenir").t('s').pe(1).n('p').realize()   
    ) == 'revenions',\
    'revenir:s4'


def test_conjugation_fr_2400():
    assert (
V("revenir").t('s').pe(2).n('p').realize()   
    ) == 'reveniez',\
    'revenir:s5'


def test_conjugation_fr_2401():
    assert (
V("revenir").t('s').pe(3).n('p').realize()   
    ) == 'reviennent',\
    'revenir:s6'


def test_conjugation_fr_2402():
    assert (
V("revêtir").t('p').pe(3).n('s').realize()   
    ) == 'revêt',\
    'revêtir:p3'


def test_conjugation_fr_2403():
    assert (
V("revêtir").t('pr').realize()   
    ) == 'revêtant',\
    'revêtir:pr'


def test_conjugation_fr_2404():
    assert (
V("revêtir").t('p').pe(3).n('p').realize()   
    ) == 'revêtent',\
    'revêtir:p6'


def test_conjugation_fr_2405():
    assert (
V("revêtir").t('p').pe(2).n('p').realize()   
    ) == 'revêtez',\
    'revêtir:p5'


def test_conjugation_fr_2406():
    assert (
V("revêtir").t('ip').pe(2).n('p').realize()   
    ) == 'revêtez',\
    'revêtir:ip5'


def test_conjugation_fr_2407():
    assert (
V("revêtir").t('p').pe(1).n('p').realize()   
    ) == 'revêtons',\
    'revêtir:p4'


def test_conjugation_fr_2408():
    assert (
V("revêtir").t('ip').pe(1).n('p').realize()   
    ) == 'revêtons',\
    'revêtir:ip4'


def test_conjugation_fr_2409():
    assert (
V("revêtir").t('p').pe(1).n('s').realize()   
    ) == 'revêts',\
    'revêtir:p1'


def test_conjugation_fr_2410():
    assert (
V("revêtir").t('p').pe(2).n('s').realize()   
    ) == 'revêts',\
    'revêtir:p2'


def test_conjugation_fr_2411():
    assert (
V("revêtir").t('ip').pe(2).n('s').realize()   
    ) == 'revêts',\
    'revêtir:ip2'


def test_conjugation_fr_2412():
    assert (
V("revêtir").t('pp').realize()   
    ) == 'revêtu',\
    'revêtir:pp'


def test_conjugation_fr_2413():
    assert (
V("revêtir").t('s').pe(1).n('s').realize()   
    ) == 'revête',\
    'revêtir:s1'


def test_conjugation_fr_2414():
    assert (
V("revêtir").t('s').pe(2).n('s').realize()   
    ) == 'revêtes',\
    'revêtir:s2'


def test_conjugation_fr_2415():
    assert (
V("revêtir").t('s').pe(3).n('s').realize()   
    ) == 'revête',\
    'revêtir:s3'


def test_conjugation_fr_2416():
    assert (
V("revêtir").t('s').pe(1).n('p').realize()   
    ) == 'revêtions',\
    'revêtir:s4'


def test_conjugation_fr_2417():
    assert (
V("revêtir").t('s').pe(2).n('p').realize()   
    ) == 'revêtiez',\
    'revêtir:s5'


def test_conjugation_fr_2418():
    assert (
V("revêtir").t('s').pe(3).n('p').realize()   
    ) == 'revêtent',\
    'revêtir:s6'


def test_conjugation_fr_2419():
    assert (
V("revivre").t('p').pe(1).n('s').realize()   
    ) == 'revis',\
    'revivre:p1'


def test_conjugation_fr_2420():
    assert (
V("revivre").t('p').pe(2).n('s').realize()   
    ) == 'revis',\
    'revivre:p2'


def test_conjugation_fr_2421():
    assert (
V("revivre").t('ip').pe(2).n('s').realize()   
    ) == 'revis',\
    'revivre:ip2'


def test_conjugation_fr_2422():
    assert (
V("revivre").t('p').pe(3).n('s').realize()   
    ) == 'revit',\
    'revivre:p3'


def test_conjugation_fr_2423():
    assert (
V("revivre").t('pr').realize()   
    ) == 'revivant',\
    'revivre:pr'


def test_conjugation_fr_2424():
    assert (
V("revivre").t('p').pe(3).n('p').realize()   
    ) == 'revivent',\
    'revivre:p6'


def test_conjugation_fr_2425():
    assert (
V("revivre").t('p').pe(2).n('p').realize()   
    ) == 'revivez',\
    'revivre:p5'


def test_conjugation_fr_2426():
    assert (
V("revivre").t('ip').pe(2).n('p').realize()   
    ) == 'revivez',\
    'revivre:ip5'


def test_conjugation_fr_2427():
    assert (
V("revivre").t('p').pe(1).n('p').realize()   
    ) == 'revivons',\
    'revivre:p4'


def test_conjugation_fr_2428():
    assert (
V("revivre").t('ip').pe(1).n('p').realize()   
    ) == 'revivons',\
    'revivre:ip4'


def test_conjugation_fr_2429():
    assert (
V("revivre").t('s').pe(1).n('s').realize()   
    ) == 'revive',\
    'revivre:s1'


def test_conjugation_fr_2430():
    assert (
V("revivre").t('s').pe(2).n('s').realize()   
    ) == 'revives',\
    'revivre:s2'


def test_conjugation_fr_2431():
    assert (
V("revivre").t('s').pe(3).n('s').realize()   
    ) == 'revive',\
    'revivre:s3'


def test_conjugation_fr_2432():
    assert (
V("revivre").t('s').pe(1).n('p').realize()   
    ) == 'revivions',\
    'revivre:s4'


def test_conjugation_fr_2433():
    assert (
V("revivre").t('s').pe(2).n('p').realize()   
    ) == 'reviviez',\
    'revivre:s5'


def test_conjugation_fr_2434():
    assert (
V("revivre").t('s').pe(3).n('p').realize()   
    ) == 'revivent',\
    'revivre:s6'


def test_conjugation_fr_2435():
    assert (
V("revoir").t('p').pe(3).n('p').realize()   
    ) == 'revoient',\
    'revoir:p6'


def test_conjugation_fr_2436():
    assert (
V("revoir").t('p').pe(1).n('s').realize()   
    ) == 'revois',\
    'revoir:p1'


def test_conjugation_fr_2437():
    assert (
V("revoir").t('p').pe(2).n('s').realize()   
    ) == 'revois',\
    'revoir:p2'


def test_conjugation_fr_2438():
    assert (
V("revoir").t('ip').pe(2).n('s').realize()   
    ) == 'revois',\
    'revoir:ip2'


def test_conjugation_fr_2439():
    assert (
V("revoir").t('p').pe(3).n('s').realize()   
    ) == 'revoit',\
    'revoir:p3'


def test_conjugation_fr_2440():
    assert (
V("revoir").t('pr').realize()   
    ) == 'revoyant',\
    'revoir:pr'


def test_conjugation_fr_2441():
    assert (
V("revoir").t('p').pe(2).n('p').realize()   
    ) == 'revoyez',\
    'revoir:p5'


def test_conjugation_fr_2442():
    assert (
V("revoir").t('ip').pe(2).n('p').realize()   
    ) == 'revoyez',\
    'revoir:ip5'


def test_conjugation_fr_2443():
    assert (
V("revoir").t('p').pe(1).n('p').realize()   
    ) == 'revoyons',\
    'revoir:p4'


def test_conjugation_fr_2444():
    assert (
V("revoir").t('ip').pe(1).n('p').realize()   
    ) == 'revoyons',\
    'revoir:ip4'


def test_conjugation_fr_2445():
    assert (
V("revoir").t('pp').realize()   
    ) == 'revu',\
    'revoir:pp'


def test_conjugation_fr_2446():
    assert (
V("revoir").t('s').pe(1).n('s').realize()   
    ) == 'revoie',\
    'revoir:s1'


def test_conjugation_fr_2447():
    assert (
V("revoir").t('s').pe(2).n('s').realize()   
    ) == 'revoies',\
    'revoir:s2'


def test_conjugation_fr_2448():
    assert (
V("revoir").t('s').pe(3).n('s').realize()   
    ) == 'revoie',\
    'revoir:s3'


def test_conjugation_fr_2449():
    assert (
V("revoir").t('s').pe(1).n('p').realize()   
    ) == 'revoyions',\
    'revoir:s4'


def test_conjugation_fr_2450():
    assert (
V("revoir").t('s').pe(2).n('p').realize()   
    ) == 'revoyiez',\
    'revoir:s5'


def test_conjugation_fr_2451():
    assert (
V("revoir").t('s').pe(3).n('p').realize()   
    ) == 'revoient',\
    'revoir:s6'


def test_conjugation_fr_2452():
    assert (
V("revoir").t('ps').pe(1).n('s').realize()   
    ) == 'revis',\
    'revoir:ps1'


def test_conjugation_fr_2453():
    assert (
V("revoir").t('ps').pe(2).n('s').realize()   
    ) == 'revis',\
    'revoir:ps2'


def test_conjugation_fr_2454():
    assert (
V("revoir").t('ps').pe(3).n('s').realize()   
    ) == 'revit',\
    'revoir:ps3'


def test_conjugation_fr_2455():
    assert (
V("revoir").t('ps').pe(1).n('p').realize()   
    ) == 'revîmes',\
    'revoir:ps4'


def test_conjugation_fr_2456():
    assert (
V("revoir").t('ps').pe(2).n('p').realize()   
    ) == 'revîtes',\
    'revoir:ps5'


def test_conjugation_fr_2457():
    assert (
V("revoir").t('ps').pe(3).n('p').realize()   
    ) == 'revirent',\
    'revoir:ps6'


def test_conjugation_fr_2458():
    assert (
V("rire").t('pr').realize()   
    ) == 'riant',\
    'rire:pr'


def test_conjugation_fr_2459():
    assert (
V("rire").t('p').pe(3).n('p').realize()   
    ) == 'rient',\
    'rire:p6'


def test_conjugation_fr_2460():
    assert (
V("rire").t('p').pe(2).n('p').realize()   
    ) == 'riez',\
    'rire:p5'


def test_conjugation_fr_2461():
    assert (
V("rire").t('ip').pe(2).n('p').realize()   
    ) == 'riez',\
    'rire:ip5'


def test_conjugation_fr_2462():
    assert (
V("rire").t('p').pe(1).n('p').realize()   
    ) == 'rions',\
    'rire:p4'


def test_conjugation_fr_2463():
    assert (
V("rire").t('ip').pe(1).n('p').realize()   
    ) == 'rions',\
    'rire:ip4'


def test_conjugation_fr_2464():
    assert (
V("rire").t('p').pe(1).n('s').realize()   
    ) == 'ris',\
    'rire:p1'


def test_conjugation_fr_2465():
    assert (
V("rire").t('p').pe(2).n('s').realize()   
    ) == 'ris',\
    'rire:p2'


def test_conjugation_fr_2466():
    assert (
V("rire").t('ip').pe(2).n('s').realize()   
    ) == 'ris',\
    'rire:ip2'


def test_conjugation_fr_2467():
    assert (
V("rire").t('p').pe(3).n('s').realize()   
    ) == 'rit',\
    'rire:p3'


def test_conjugation_fr_2468():
    assert (
V("rire").t('s').pe(1).n('s').realize()   
    ) == 'rie',\
    'rire:s1'


def test_conjugation_fr_2469():
    assert (
V("rire").t('s').pe(2).n('s').realize()   
    ) == 'ries',\
    'rire:s2'


def test_conjugation_fr_2470():
    assert (
V("rire").t('s').pe(3).n('s').realize()   
    ) == 'rie',\
    'rire:s3'


def test_conjugation_fr_2471():
    assert (
V("rire").t('s').pe(1).n('p').realize()   
    ) == 'riions',\
    'rire:s4'


def test_conjugation_fr_2472():
    assert (
V("rire").t('s').pe(2).n('p').realize()   
    ) == 'riiez',\
    'rire:s5'


def test_conjugation_fr_2473():
    assert (
V("rire").t('s').pe(3).n('p').realize()   
    ) == 'rient',\
    'rire:s6'


def test_conjugation_fr_2474():
    assert (
V("rire").t('pp').realize()   
    ) == 'ri',\
    'rire:pp'


def test_conjugation_fr_2475():
    assert (
V("rompre").t('pr').realize()   
    ) == 'rompant',\
    'rompre:pr'


def test_conjugation_fr_2476():
    assert (
V("rompre").t('p').pe(3).n('p').realize()   
    ) == 'rompent',\
    'rompre:p6'


def test_conjugation_fr_2477():
    assert (
V("rompre").t('p').pe(2).n('p').realize()   
    ) == 'rompez',\
    'rompre:p5'


def test_conjugation_fr_2478():
    assert (
V("rompre").t('ip').pe(2).n('p').realize()   
    ) == 'rompez',\
    'rompre:ip5'


def test_conjugation_fr_2479():
    assert (
V("rompre").t('p').pe(1).n('p').realize()   
    ) == 'rompons',\
    'rompre:p4'


def test_conjugation_fr_2480():
    assert (
V("rompre").t('ip').pe(1).n('p').realize()   
    ) == 'rompons',\
    'rompre:ip4'


def test_conjugation_fr_2481():
    assert (
V("rompre").t('p').pe(1).n('s').realize()   
    ) == 'romps',\
    'rompre:p1'


def test_conjugation_fr_2482():
    assert (
V("rompre").t('p').pe(2).n('s').realize()   
    ) == 'romps',\
    'rompre:p2'


def test_conjugation_fr_2483():
    assert (
V("rompre").t('ip').pe(2).n('s').realize()   
    ) == 'romps',\
    'rompre:ip2'


def test_conjugation_fr_2484():
    assert (
V("rompre").t('p').pe(3).n('s').realize()   
    ) == 'rompt',\
    'rompre:p3'


def test_conjugation_fr_2485():
    assert (
V("rompre").t('pp').realize()   
    ) == 'rompu',\
    'rompre:pp'


def test_conjugation_fr_2486():
    assert (
V("rompre").t('s').pe(1).n('s').realize()   
    ) == 'rompe',\
    'rompre:s1'


def test_conjugation_fr_2487():
    assert (
V("rompre").t('s').pe(2).n('s').realize()   
    ) == 'rompes',\
    'rompre:s2'


def test_conjugation_fr_2488():
    assert (
V("rompre").t('s').pe(3).n('s').realize()   
    ) == 'rompe',\
    'rompre:s3'


def test_conjugation_fr_2489():
    assert (
V("rompre").t('s').pe(1).n('p').realize()   
    ) == 'rompions',\
    'rompre:s4'


def test_conjugation_fr_2490():
    assert (
V("rompre").t('s').pe(2).n('p').realize()   
    ) == 'rompiez',\
    'rompre:s5'


def test_conjugation_fr_2491():
    assert (
V("rompre").t('s').pe(3).n('p').realize()   
    ) == 'rompent',\
    'rompre:s6'


def test_conjugation_fr_2492():
    assert (
V("ruisseler").t('p').pe(1).n('s').realize()   
    ) == 'ruisselle',\
    'ruisseler:p1'


def test_conjugation_fr_2493():
    assert (
V("ruisseler").t('p').pe(2).n('s').realize()   
    ) == 'ruisselles',\
    'ruisseler:p2'


def test_conjugation_fr_2494():
    assert (
V("ruisseler").t('p').pe(3).n('s').realize()   
    ) == 'ruisselle',\
    'ruisseler:p3'


def test_conjugation_fr_2495():
    assert (
V("ruisseler").t('p').pe(3).n('p').realize()   
    ) == 'ruissellent',\
    'ruisseler:p6'


def test_conjugation_fr_2496():
    assert (
V("ruisseler").t('s').pe(1).n('s').realize()   
    ) == 'ruisselle',\
    'ruisseler:s1'


def test_conjugation_fr_2497():
    assert (
V("ruisseler").t('s').pe(2).n('s').realize()   
    ) == 'ruisselles',\
    'ruisseler:s2'


def test_conjugation_fr_2498():
    assert (
V("ruisseler").t('s').pe(3).n('s').realize()   
    ) == 'ruisselle',\
    'ruisseler:s3'


def test_conjugation_fr_2499():
    assert (
V("ruisseler").t('s').pe(1).n('p').realize()   
    ) == 'ruisselions',\
    'ruisseler:s4'


def test_conjugation_fr_2500():
    assert (
V("ruisseler").t('s').pe(2).n('p').realize()   
    ) == 'ruisseliez',\
    'ruisseler:s5'


def test_conjugation_fr_2501():
    assert (
V("ruisseler").t('s').pe(3).n('p').realize()   
    ) == 'ruissellent',\
    'ruisseler:s6'


def test_conjugation_fr_2502():
    assert (
V("enfuir").t('p').pe(1).n('s').realize()   
    ) == "m'enfuis",\
    'enfuir:p1'


def test_conjugation_fr_2503():
    assert (
V("enfuir").t('p').pe(2).n('s').realize()   
    ) == "t'enfuis",\
    'enfuir:p2'


def test_conjugation_fr_2504():
    assert (
V("enfuir").t('p').pe(3).n('s').realize()   
    ) == "s'enfuit",\
    'enfuir:p3'


def test_conjugation_fr_2505():
    assert (
V("enfuir").t('p').pe(1).n('p').realize()   
    ) == 'nous enfuyons',\
    'enfuir:p4'


def test_conjugation_fr_2506():
    assert (
V("enfuir").t('p').pe(2).n('p').realize()   
    ) == 'vous enfuyez',\
    'enfuir:p5'


def test_conjugation_fr_2507():
    assert (
V("enfuir").t('p').pe(3).n('p').realize()   
    ) == "s'enfuient",\
    'enfuir:p6'


def test_conjugation_fr_2508():
    assert (
V("enfuir").t('ip').pe(2).n('s').realize()   
    ) == 'enfuis-toi',\
    'enfuir:ip2'


def test_conjugation_fr_2509():
    assert (
V("enfuir").t('ip').pe(1).n('p').realize()   
    ) == 'enfuyons-nous',\
    'enfuir:ip4'


def test_conjugation_fr_2510():
    assert (
V("enfuir").t('ip').pe(2).n('p').realize()   
    ) == 'enfuyez-vous',\
    'enfuir:ip5'


def test_conjugation_fr_2511():
    assert (
V("enfuir").t('pr').realize()   
    ) == "s'enfuyant",\
    'enfuir:pr'


def test_conjugation_fr_2512():
    assert (
V("enfuir").t('pp').realize()   
    ) == 'enfui',\
    'enfuir:pp'


def test_conjugation_fr_2513():
    assert (
V("enfuir").t('s').pe(1).n('s').realize()   
    ) == "m'enfuie",\
    'enfuir:s1'


def test_conjugation_fr_2514():
    assert (
V("enfuir").t('s').pe(2).n('s').realize()   
    ) == "t'enfuies",\
    'enfuir:s2'


def test_conjugation_fr_2515():
    assert (
V("enfuir").t('s').pe(3).n('s').realize()   
    ) == "s'enfuie",\
    'enfuir:s3'


def test_conjugation_fr_2516():
    assert (
V("enfuir").t('s').pe(1).n('p').realize()   
    ) == 'nous enfuyions',\
    'enfuir:s4'


def test_conjugation_fr_2517():
    assert (
V("enfuir").t('s').pe(2).n('p').realize()   
    ) == 'vous enfuyiez',\
    'enfuir:s5'


def test_conjugation_fr_2518():
    assert (
V("enfuir").t('s').pe(3).n('p').realize()   
    ) == "s'enfuient",\
    'enfuir:s6'


def test_conjugation_fr_2519():
    assert (
V("satisfaire").t('p').pe(1).n('s').realize()   
    ) == 'satisfais',\
    'satisfaire:p1'


def test_conjugation_fr_2520():
    assert (
V("satisfaire").t('p').pe(2).n('s').realize()   
    ) == 'satisfais',\
    'satisfaire:p2'


def test_conjugation_fr_2521():
    assert (
V("satisfaire").t('ip').pe(2).n('s').realize()   
    ) == 'satisfais',\
    'satisfaire:ip2'


def test_conjugation_fr_2522():
    assert (
V("satisfaire").t('pr').realize()   
    ) == 'satisfaisant',\
    'satisfaire:pr'


def test_conjugation_fr_2523():
    assert (
V("satisfaire").t('p').pe(1).n('p').realize()   
    ) == 'satisfaisons',\
    'satisfaire:p4'


def test_conjugation_fr_2524():
    assert (
V("satisfaire").t('ip').pe(1).n('p').realize()   
    ) == 'satisfaisons',\
    'satisfaire:ip4'


def test_conjugation_fr_2525():
    assert (
V("satisfaire").t('p').pe(3).n('s').realize()   
    ) == 'satisfait',\
    'satisfaire:p3'


def test_conjugation_fr_2526():
    assert (
V("satisfaire").t('p').pe(2).n('p').realize()   
    ) == 'satisfaites',\
    'satisfaire:p5'


def test_conjugation_fr_2527():
    assert (
V("satisfaire").t('ip').pe(2).n('p').realize()   
    ) == 'satisfaites',\
    'satisfaire:ip5'


def test_conjugation_fr_2528():
    assert (
V("satisfaire").t('p').pe(3).n('p').realize()   
    ) == 'satisfont',\
    'satisfaire:p6'


def test_conjugation_fr_2529():
    assert (
V("satisfaire").t('pp').realize()   
    ) == 'satisfait',\
    'satisfaire:pp'


def test_conjugation_fr_2530():
    assert (
V("satisfaire").t('s').pe(1).n('s').realize()   
    ) == 'satisfasse',\
    'satisfaire:s1'


def test_conjugation_fr_2531():
    assert (
V("satisfaire").t('s').pe(2).n('s').realize()   
    ) == 'satisfasses',\
    'satisfaire:s2'


def test_conjugation_fr_2532():
    assert (
V("satisfaire").t('s').pe(3).n('s').realize()   
    ) == 'satisfasse',\
    'satisfaire:s3'


def test_conjugation_fr_2533():
    assert (
V("satisfaire").t('s').pe(1).n('p').realize()   
    ) == 'satisfassions',\
    'satisfaire:s4'


def test_conjugation_fr_2534():
    assert (
V("satisfaire").t('s').pe(2).n('p').realize()   
    ) == 'satisfassiez',\
    'satisfaire:s5'


def test_conjugation_fr_2535():
    assert (
V("satisfaire").t('s').pe(3).n('p').realize()   
    ) == 'satisfassent',\
    'satisfaire:s6'


def test_conjugation_fr_2536():
    assert (
V("savoir").t('pr').realize()   
    ) == 'sachant',\
    'savoir:pr'


def test_conjugation_fr_2537():
    assert (
V("savoir").t('ip').pe(2).n('s').realize()   
    ) == 'sache',\
    'savoir:ip2'


def test_conjugation_fr_2538():
    assert (
V("savoir").t('ip').pe(2).n('p').realize()   
    ) == 'sachez',\
    'savoir:ip5'


def test_conjugation_fr_2539():
    assert (
V("savoir").t('ip').pe(1).n('p').realize()   
    ) == 'sachons',\
    'savoir:ip4'


def test_conjugation_fr_2540():
    assert (
V("savoir").t('p').pe(1).n('s').realize()   
    ) == 'sais',\
    'savoir:p1'


def test_conjugation_fr_2541():
    assert (
V("savoir").t('p').pe(2).n('s').realize()   
    ) == 'sais',\
    'savoir:p2'


def test_conjugation_fr_2542():
    assert (
V("savoir").t('p').pe(3).n('s').realize()   
    ) == 'sait',\
    'savoir:p3'


def test_conjugation_fr_2543():
    assert (
V("savoir").t('p').pe(3).n('p').realize()   
    ) == 'savent',\
    'savoir:p6'


def test_conjugation_fr_2544():
    assert (
V("savoir").t('p').pe(2).n('p').realize()   
    ) == 'savez',\
    'savoir:p5'


def test_conjugation_fr_2545():
    assert (
V("savoir").t('p').pe(1).n('p').realize()   
    ) == 'savons',\
    'savoir:p4'


def test_conjugation_fr_2546():
    assert (
V("savoir").t('pp').realize()   
    ) == 'su',\
    'savoir:pp'


def test_conjugation_fr_2547():
    assert (
V("savoir").t('s').pe(1).n('s').realize()   
    ) == 'sache',\
    'savoir:s1'


def test_conjugation_fr_2548():
    assert (
V("savoir").t('s').pe(2).n('s').realize()   
    ) == 'saches',\
    'savoir:s2'


def test_conjugation_fr_2549():
    assert (
V("savoir").t('s').pe(3).n('s').realize()   
    ) == 'sache',\
    'savoir:s3'


def test_conjugation_fr_2550():
    assert (
V("savoir").t('s').pe(1).n('p').realize()   
    ) == 'sachions',\
    'savoir:s4'


def test_conjugation_fr_2551():
    assert (
V("savoir").t('s').pe(2).n('p').realize()   
    ) == 'sachiez',\
    'savoir:s5'


def test_conjugation_fr_2552():
    assert (
V("savoir").t('s').pe(3).n('p').realize()   
    ) == 'sachent',\
    'savoir:s6'


def test_conjugation_fr_2553():
    assert (
V("secourir").t('pr').realize()   
    ) == 'secourant',\
    'secourir:pr'


def test_conjugation_fr_2554():
    assert (
V("secourir").t('p').pe(3).n('p').realize()   
    ) == 'secourent',\
    'secourir:p6'


def test_conjugation_fr_2555():
    assert (
V("secourir").t('p').pe(2).n('p').realize()   
    ) == 'secourez',\
    'secourir:p5'


def test_conjugation_fr_2556():
    assert (
V("secourir").t('ip').pe(2).n('p').realize()   
    ) == 'secourez',\
    'secourir:ip5'


def test_conjugation_fr_2557():
    assert (
V("secourir").t('p').pe(1).n('p').realize()   
    ) == 'secourons',\
    'secourir:p4'


def test_conjugation_fr_2558():
    assert (
V("secourir").t('ip').pe(1).n('p').realize()   
    ) == 'secourons',\
    'secourir:ip4'


def test_conjugation_fr_2559():
    assert (
V("secourir").t('p').pe(1).n('s').realize()   
    ) == 'secours',\
    'secourir:p1'


def test_conjugation_fr_2560():
    assert (
V("secourir").t('p').pe(2).n('s').realize()   
    ) == 'secours',\
    'secourir:p2'


def test_conjugation_fr_2561():
    assert (
V("secourir").t('ip').pe(2).n('s').realize()   
    ) == 'secours',\
    'secourir:ip2'


def test_conjugation_fr_2562():
    assert (
V("secourir").t('p').pe(3).n('s').realize()   
    ) == 'secourt',\
    'secourir:p3'


def test_conjugation_fr_2563():
    assert (
V("secourir").t('pp').realize()   
    ) == 'secouru',\
    'secourir:pp'


def test_conjugation_fr_2564():
    assert (
V("secourir").t('s').pe(1).n('s').realize()   
    ) == 'secoure',\
    'secourir:s1'


def test_conjugation_fr_2565():
    assert (
V("secourir").t('s').pe(2).n('s').realize()   
    ) == 'secoures',\
    'secourir:s2'


def test_conjugation_fr_2566():
    assert (
V("secourir").t('s').pe(3).n('s').realize()   
    ) == 'secoure',\
    'secourir:s3'


def test_conjugation_fr_2567():
    assert (
V("secourir").t('s').pe(1).n('p').realize()   
    ) == 'secourions',\
    'secourir:s4'


def test_conjugation_fr_2568():
    assert (
V("secourir").t('s').pe(2).n('p').realize()   
    ) == 'secouriez',\
    'secourir:s5'


def test_conjugation_fr_2569():
    assert (
V("secourir").t('s').pe(3).n('p').realize()   
    ) == 'secourent',\
    'secourir:s6'


def test_conjugation_fr_2570():
    assert (
V("sentir").t('p').pe(1).n('s').realize()   
    ) == 'sens',\
    'sentir:p1'


def test_conjugation_fr_2571():
    assert (
V("sentir").t('p').pe(2).n('s').realize()   
    ) == 'sens',\
    'sentir:p2'


def test_conjugation_fr_2572():
    assert (
V("sentir").t('ip').pe(2).n('s').realize()   
    ) == 'sens',\
    'sentir:ip2'


def test_conjugation_fr_2573():
    assert (
V("sentir").t('p').pe(3).n('s').realize()   
    ) == 'sent',\
    'sentir:p3'


def test_conjugation_fr_2574():
    assert (
V("sentir").t('pr').realize()   
    ) == 'sentant',\
    'sentir:pr'


def test_conjugation_fr_2575():
    assert (
V("sentir").t('p').pe(3).n('p').realize()   
    ) == 'sentent',\
    'sentir:p6'


def test_conjugation_fr_2576():
    assert (
V("sentir").t('p').pe(2).n('p').realize()   
    ) == 'sentez',\
    'sentir:p5'


def test_conjugation_fr_2577():
    assert (
V("sentir").t('ip').pe(2).n('p').realize()   
    ) == 'sentez',\
    'sentir:ip5'


def test_conjugation_fr_2578():
    assert (
V("sentir").t('p').pe(1).n('p').realize()   
    ) == 'sentons',\
    'sentir:p4'


def test_conjugation_fr_2579():
    assert (
V("sentir").t('ip').pe(1).n('p').realize()   
    ) == 'sentons',\
    'sentir:ip4'


def test_conjugation_fr_2580():
    assert (
V("sentir").t('pp').realize()   
    ) == 'senti',\
    'sentir:pp'


def test_conjugation_fr_2581():
    assert (
V("sentir").t('s').pe(1).n('s').realize()   
    ) == 'sente',\
    'sentir:s1'


def test_conjugation_fr_2582():
    assert (
V("sentir").t('s').pe(2).n('s').realize()   
    ) == 'sentes',\
    'sentir:s2'


def test_conjugation_fr_2583():
    assert (
V("sentir").t('s').pe(3).n('s').realize()   
    ) == 'sente',\
    'sentir:s3'


def test_conjugation_fr_2584():
    assert (
V("sentir").t('s').pe(1).n('p').realize()   
    ) == 'sentions',\
    'sentir:s4'


def test_conjugation_fr_2585():
    assert (
V("sentir").t('s').pe(2).n('p').realize()   
    ) == 'sentiez',\
    'sentir:s5'


def test_conjugation_fr_2586():
    assert (
V("sentir").t('s').pe(3).n('p').realize()   
    ) == 'sentent',\
    'sentir:s6'


def test_conjugation_fr_2587():
    assert (
V("servir").t('p').pe(1).n('s').realize()   
    ) == 'sers',\
    'servir:p1'


def test_conjugation_fr_2588():
    assert (
V("servir").t('p').pe(2).n('s').realize()   
    ) == 'sers',\
    'servir:p2'


def test_conjugation_fr_2589():
    assert (
V("servir").t('ip').pe(2).n('s').realize()   
    ) == 'sers',\
    'servir:ip2'


def test_conjugation_fr_2590():
    assert (
V("servir").t('p').pe(3).n('s').realize()   
    ) == 'sert',\
    'servir:p3'


def test_conjugation_fr_2591():
    assert (
V("servir").t('pr').realize()   
    ) == 'servant',\
    'servir:pr'


def test_conjugation_fr_2592():
    assert (
V("servir").t('p').pe(3).n('p').realize()   
    ) == 'servent',\
    'servir:p6'


def test_conjugation_fr_2593():
    assert (
V("servir").t('p').pe(2).n('p').realize()   
    ) == 'servez',\
    'servir:p5'


def test_conjugation_fr_2594():
    assert (
V("servir").t('ip').pe(2).n('p').realize()   
    ) == 'servez',\
    'servir:ip5'


def test_conjugation_fr_2595():
    assert (
V("servir").t('p').pe(1).n('p').realize()   
    ) == 'servons',\
    'servir:p4'


def test_conjugation_fr_2596():
    assert (
V("servir").t('ip').pe(1).n('p').realize()   
    ) == 'servons',\
    'servir:ip4'


def test_conjugation_fr_2597():
    assert (
V("servir").t('pp').realize()   
    ) == 'servi',\
    'servir:pp'


def test_conjugation_fr_2598():
    assert (
V("servir").t('s').pe(1).n('s').realize()   
    ) == 'serve',\
    'servir:s1'


def test_conjugation_fr_2599():
    assert (
V("servir").t('s').pe(2).n('s').realize()   
    ) == 'serves',\
    'servir:s2'


def test_conjugation_fr_2600():
    assert (
V("servir").t('s').pe(3).n('s').realize()   
    ) == 'serve',\
    'servir:s3'


def test_conjugation_fr_2601():
    assert (
V("servir").t('s').pe(1).n('p').realize()   
    ) == 'servions',\
    'servir:s4'


def test_conjugation_fr_2602():
    assert (
V("servir").t('s').pe(2).n('p').realize()   
    ) == 'serviez',\
    'servir:s5'


def test_conjugation_fr_2603():
    assert (
V("servir").t('s').pe(3).n('p').realize()   
    ) == 'servent',\
    'servir:s6'


def test_conjugation_fr_2604():
    assert (
V("sortir").t('p').pe(1).n('s').realize()   
    ) == 'sors',\
    'sortir:p1'


def test_conjugation_fr_2605():
    assert (
V("sortir").t('p').pe(2).n('s').realize()   
    ) == 'sors',\
    'sortir:p2'


def test_conjugation_fr_2606():
    assert (
V("sortir").t('ip').pe(2).n('s').realize()   
    ) == 'sors',\
    'sortir:ip2'


def test_conjugation_fr_2607():
    assert (
V("sortir").t('p').pe(3).n('s').realize()   
    ) == 'sort',\
    'sortir:p3'


def test_conjugation_fr_2608():
    assert (
V("sortir").t('pr').realize()   
    ) == 'sortant',\
    'sortir:pr'


def test_conjugation_fr_2609():
    assert (
V("sortir").t('p').pe(3).n('p').realize()   
    ) == 'sortent',\
    'sortir:p6'


def test_conjugation_fr_2610():
    assert (
V("sortir").t('p').pe(2).n('p').realize()   
    ) == 'sortez',\
    'sortir:p5'


def test_conjugation_fr_2611():
    assert (
V("sortir").t('ip').pe(2).n('p').realize()   
    ) == 'sortez',\
    'sortir:ip5'


def test_conjugation_fr_2612():
    assert (
V("sortir").t('p').pe(1).n('p').realize()   
    ) == 'sortons',\
    'sortir:p4'


def test_conjugation_fr_2613():
    assert (
V("sortir").t('ip').pe(1).n('p').realize()   
    ) == 'sortons',\
    'sortir:ip4'


def test_conjugation_fr_2614():
    assert (
V("sortir").t('pp').realize()   
    ) == 'sorti',\
    'sortir:pp'


def test_conjugation_fr_2615():
    assert (
V("sortir").t('s').pe(1).n('s').realize()   
    ) == 'sorte',\
    'sortir:s1'


def test_conjugation_fr_2616():
    assert (
V("sortir").t('s').pe(2).n('s').realize()   
    ) == 'sortes',\
    'sortir:s2'


def test_conjugation_fr_2617():
    assert (
V("sortir").t('s').pe(3).n('s').realize()   
    ) == 'sorte',\
    'sortir:s3'


def test_conjugation_fr_2618():
    assert (
V("sortir").t('s').pe(1).n('p').realize()   
    ) == 'sortions',\
    'sortir:s4'


def test_conjugation_fr_2619():
    assert (
V("sortir").t('s').pe(2).n('p').realize()   
    ) == 'sortiez',\
    'sortir:s5'


def test_conjugation_fr_2620():
    assert (
V("sortir").t('s').pe(3).n('p').realize()   
    ) == 'sortent',\
    'sortir:s6'


def test_conjugation_fr_2621():
    assert (
V("souffrir").t('pr').realize()   
    ) == 'souffrant',\
    'souffrir:pr'


def test_conjugation_fr_2622():
    assert (
V("souffrir").t('p').pe(1).n('s').realize()   
    ) == 'souffre',\
    'souffrir:p1'


def test_conjugation_fr_2623():
    assert (
V("souffrir").t('p').pe(3).n('s').realize()   
    ) == 'souffre',\
    'souffrir:p3'


def test_conjugation_fr_2624():
    assert (
V("souffrir").t('ip').pe(2).n('s').realize()   
    ) == 'souffre',\
    'souffrir:ip2'


def test_conjugation_fr_2625():
    assert (
V("souffrir").t('p').pe(3).n('p').realize()   
    ) == 'souffrent',\
    'souffrir:p6'


def test_conjugation_fr_2626():
    assert (
V("souffrir").t('p').pe(2).n('s').realize()   
    ) == 'souffres',\
    'souffrir:p2'


def test_conjugation_fr_2627():
    assert (
V("souffrir").t('p').pe(2).n('p').realize()   
    ) == 'souffrez',\
    'souffrir:p5'


def test_conjugation_fr_2628():
    assert (
V("souffrir").t('ip').pe(2).n('p').realize()   
    ) == 'souffrez',\
    'souffrir:ip5'


def test_conjugation_fr_2629():
    assert (
V("souffrir").t('p').pe(1).n('p').realize()   
    ) == 'souffrons',\
    'souffrir:p4'


def test_conjugation_fr_2630():
    assert (
V("souffrir").t('ip').pe(1).n('p').realize()   
    ) == 'souffrons',\
    'souffrir:ip4'


def test_conjugation_fr_2631():
    assert (
V("souffrir").t('pp').realize()   
    ) == 'souffert',\
    'souffrir:pp'


def test_conjugation_fr_2632():
    assert (
V("souffrir").t('s').pe(1).n('s').realize()   
    ) == 'souffre',\
    'souffrir:s1'


def test_conjugation_fr_2633():
    assert (
V("souffrir").t('s').pe(2).n('s').realize()   
    ) == 'souffres',\
    'souffrir:s2'


def test_conjugation_fr_2634():
    assert (
V("souffrir").t('s').pe(3).n('s').realize()   
    ) == 'souffre',\
    'souffrir:s3'


def test_conjugation_fr_2635():
    assert (
V("souffrir").t('s').pe(1).n('p').realize()   
    ) == 'souffrions',\
    'souffrir:s4'


def test_conjugation_fr_2636():
    assert (
V("souffrir").t('s').pe(2).n('p').realize()   
    ) == 'souffriez',\
    'souffrir:s5'


def test_conjugation_fr_2637():
    assert (
V("souffrir").t('s').pe(3).n('p').realize()   
    ) == 'souffrent',\
    'souffrir:s6'


def test_conjugation_fr_2638():
    assert (
V("soumettre").t('p').pe(3).n('s').realize()   
    ) == 'soumet',\
    'soumettre:p3'


def test_conjugation_fr_2639():
    assert (
V("soumettre").t('p').pe(1).n('s').realize()   
    ) == 'soumets',\
    'soumettre:p1'


def test_conjugation_fr_2640():
    assert (
V("soumettre").t('p').pe(2).n('s').realize()   
    ) == 'soumets',\
    'soumettre:p2'


def test_conjugation_fr_2641():
    assert (
V("soumettre").t('ip').pe(2).n('s').realize()   
    ) == 'soumets',\
    'soumettre:ip2'


def test_conjugation_fr_2642():
    assert (
V("soumettre").t('pr').realize()   
    ) == 'soumettant',\
    'soumettre:pr'


def test_conjugation_fr_2643():
    assert (
V("soumettre").t('p').pe(3).n('p').realize()   
    ) == 'soumettent',\
    'soumettre:p6'


def test_conjugation_fr_2644():
    assert (
V("soumettre").t('p').pe(2).n('p').realize()   
    ) == 'soumettez',\
    'soumettre:p5'


def test_conjugation_fr_2645():
    assert (
V("soumettre").t('ip').pe(2).n('p').realize()   
    ) == 'soumettez',\
    'soumettre:ip5'


def test_conjugation_fr_2646():
    assert (
V("soumettre").t('p').pe(1).n('p').realize()   
    ) == 'soumettons',\
    'soumettre:p4'


def test_conjugation_fr_2647():
    assert (
V("soumettre").t('ip').pe(1).n('p').realize()   
    ) == 'soumettons',\
    'soumettre:ip4'


def test_conjugation_fr_2648():
    assert (
V("soumettre").t('pp').realize()   
    ) == 'soumis',\
    'soumettre:pp'


def test_conjugation_fr_2649():
    assert (
V("soumettre").t('s').pe(1).n('s').realize()   
    ) == 'soumette',\
    'soumettre:s1'


def test_conjugation_fr_2650():
    assert (
V("soumettre").t('s').pe(2).n('s').realize()   
    ) == 'soumettes',\
    'soumettre:s2'


def test_conjugation_fr_2651():
    assert (
V("soumettre").t('s').pe(3).n('s').realize()   
    ) == 'soumette',\
    'soumettre:s3'


def test_conjugation_fr_2652():
    assert (
V("soumettre").t('s').pe(1).n('p').realize()   
    ) == 'soumettions',\
    'soumettre:s4'


def test_conjugation_fr_2653():
    assert (
V("soumettre").t('s').pe(2).n('p').realize()   
    ) == 'soumettiez',\
    'soumettre:s5'


def test_conjugation_fr_2654():
    assert (
V("soumettre").t('s').pe(3).n('p').realize()   
    ) == 'soumettent',\
    'soumettre:s6'


def test_conjugation_fr_2655():
    assert (
V("sourire").t('pr').realize()   
    ) == 'souriant',\
    'sourire:pr'


def test_conjugation_fr_2656():
    assert (
V("sourire").t('p').pe(3).n('p').realize()   
    ) == 'sourient',\
    'sourire:p6'


def test_conjugation_fr_2657():
    assert (
V("sourire").t('p').pe(2).n('p').realize()   
    ) == 'souriez',\
    'sourire:p5'


def test_conjugation_fr_2658():
    assert (
V("sourire").t('ip').pe(2).n('p').realize()   
    ) == 'souriez',\
    'sourire:ip5'


def test_conjugation_fr_2659():
    assert (
V("sourire").t('p').pe(1).n('p').realize()   
    ) == 'sourions',\
    'sourire:p4'


def test_conjugation_fr_2660():
    assert (
V("sourire").t('ip').pe(1).n('p').realize()   
    ) == 'sourions',\
    'sourire:ip4'


def test_conjugation_fr_2661():
    assert (
V("sourire").t('p').pe(1).n('s').realize()   
    ) == 'souris',\
    'sourire:p1'


def test_conjugation_fr_2662():
    assert (
V("sourire").t('p').pe(2).n('s').realize()   
    ) == 'souris',\
    'sourire:p2'


def test_conjugation_fr_2663():
    assert (
V("sourire").t('ip').pe(2).n('s').realize()   
    ) == 'souris',\
    'sourire:ip2'


def test_conjugation_fr_2664():
    assert (
V("sourire").t('p').pe(3).n('s').realize()   
    ) == 'sourit',\
    'sourire:p3'


def test_conjugation_fr_2665():
    assert (
V("sourire").t('s').pe(1).n('s').realize()   
    ) == 'sourie',\
    'sourire:s1'


def test_conjugation_fr_2666():
    assert (
V("sourire").t('s').pe(2).n('s').realize()   
    ) == 'souries',\
    'sourire:s2'


def test_conjugation_fr_2667():
    assert (
V("sourire").t('s').pe(3).n('s').realize()   
    ) == 'sourie',\
    'sourire:s3'


def test_conjugation_fr_2668():
    assert (
V("sourire").t('s').pe(1).n('p').realize()   
    ) == 'souriions',\
    'sourire:s4'


def test_conjugation_fr_2669():
    assert (
V("sourire").t('s').pe(2).n('p').realize()   
    ) == 'souriiez',\
    'sourire:s5'


def test_conjugation_fr_2670():
    assert (
V("sourire").t('s').pe(3).n('p').realize()   
    ) == 'sourient',\
    'sourire:s6'


def test_conjugation_fr_2671():
    assert (
V("soutenir").t('pr').realize()   
    ) == 'soutenant',\
    'soutenir:pr'


def test_conjugation_fr_2672():
    assert (
V("soutenir").t('p').pe(2).n('p').realize()   
    ) == 'soutenez',\
    'soutenir:p5'


def test_conjugation_fr_2673():
    assert (
V("soutenir").t('ip').pe(2).n('p').realize()   
    ) == 'soutenez',\
    'soutenir:ip5'


def test_conjugation_fr_2674():
    assert (
V("soutenir").t('p').pe(1).n('p').realize()   
    ) == 'soutenons',\
    'soutenir:p4'


def test_conjugation_fr_2675():
    assert (
V("soutenir").t('ip').pe(1).n('p').realize()   
    ) == 'soutenons',\
    'soutenir:ip4'


def test_conjugation_fr_2676():
    assert (
V("soutenir").t('p').pe(3).n('p').realize()   
    ) == 'soutiennent',\
    'soutenir:p6'


def test_conjugation_fr_2677():
    assert (
V("soutenir").t('p').pe(1).n('s').realize()   
    ) == 'soutiens',\
    'soutenir:p1'


def test_conjugation_fr_2678():
    assert (
V("soutenir").t('p').pe(2).n('s').realize()   
    ) == 'soutiens',\
    'soutenir:p2'


def test_conjugation_fr_2679():
    assert (
V("soutenir").t('ip').pe(2).n('s').realize()   
    ) == 'soutiens',\
    'soutenir:ip2'


def test_conjugation_fr_2680():
    assert (
V("soutenir").t('p').pe(3).n('s').realize()   
    ) == 'soutient',\
    'soutenir:p3'


def test_conjugation_fr_2681():
    assert (
V("soutenir").t('pp').realize()   
    ) == 'soutenu',\
    'soutenir:pp'


def test_conjugation_fr_2682():
    assert (
V("soutenir").t('s').pe(1).n('s').realize()   
    ) == 'soutienne',\
    'soutenir:s1'


def test_conjugation_fr_2683():
    assert (
V("soutenir").t('s').pe(2).n('s').realize()   
    ) == 'soutiennes',\
    'soutenir:s2'


def test_conjugation_fr_2684():
    assert (
V("soutenir").t('s').pe(3).n('s').realize()   
    ) == 'soutienne',\
    'soutenir:s3'


def test_conjugation_fr_2685():
    assert (
V("soutenir").t('s').pe(1).n('p').realize()   
    ) == 'soutenions',\
    'soutenir:s4'


def test_conjugation_fr_2686():
    assert (
V("soutenir").t('s').pe(2).n('p').realize()   
    ) == 'souteniez',\
    'soutenir:s5'


def test_conjugation_fr_2687():
    assert (
V("soutenir").t('s').pe(3).n('p').realize()   
    ) == 'soutiennent',\
    'soutenir:s6'


def test_conjugation_fr_2688():
    assert (
V("suffire").t('p').pe(1).n('s').realize()   
    ) == 'suffis',\
    'suffire:p1'


def test_conjugation_fr_2689():
    assert (
V("suffire").t('p').pe(2).n('s').realize()   
    ) == 'suffis',\
    'suffire:p2'


def test_conjugation_fr_2690():
    assert (
V("suffire").t('ip').pe(2).n('s').realize()   
    ) == 'suffis',\
    'suffire:ip2'


def test_conjugation_fr_2691():
    assert (
V("suffire").t('pr').realize()   
    ) == 'suffisant',\
    'suffire:pr'


def test_conjugation_fr_2692():
    assert (
V("suffire").t('p').pe(3).n('p').realize()   
    ) == 'suffisent',\
    'suffire:p6'


def test_conjugation_fr_2693():
    assert (
V("suffire").t('p').pe(2).n('p').realize()   
    ) == 'suffisez',\
    'suffire:p5'


def test_conjugation_fr_2694():
    assert (
V("suffire").t('ip').pe(2).n('p').realize()   
    ) == 'suffisez',\
    'suffire:ip5'


def test_conjugation_fr_2695():
    assert (
V("suffire").t('p').pe(1).n('p').realize()   
    ) == 'suffisons',\
    'suffire:p4'


def test_conjugation_fr_2696():
    assert (
V("suffire").t('ip').pe(1).n('p').realize()   
    ) == 'suffisons',\
    'suffire:ip4'


def test_conjugation_fr_2697():
    assert (
V("suffire").t('p').pe(3).n('s').realize()   
    ) == 'suffit',\
    'suffire:p3'


def test_conjugation_fr_2698():
    assert (
V("suffire").t('s').pe(1).n('s').realize()   
    ) == 'suffise',\
    'suffire:s1'


def test_conjugation_fr_2699():
    assert (
V("suffire").t('s').pe(2).n('s').realize()   
    ) == 'suffises',\
    'suffire:s2'


def test_conjugation_fr_2700():
    assert (
V("suffire").t('s').pe(3).n('s').realize()   
    ) == 'suffise',\
    'suffire:s3'


def test_conjugation_fr_2701():
    assert (
V("suffire").t('s').pe(1).n('p').realize()   
    ) == 'suffisions',\
    'suffire:s4'


def test_conjugation_fr_2702():
    assert (
V("suffire").t('s').pe(2).n('p').realize()   
    ) == 'suffisiez',\
    'suffire:s5'


def test_conjugation_fr_2703():
    assert (
V("suffire").t('s').pe(3).n('p').realize()   
    ) == 'suffisent',\
    'suffire:s6'


def test_conjugation_fr_2704():
    assert (
V("suivre").t('p').pe(1).n('s').realize()   
    ) == 'suis',\
    'suivre:p1'


def test_conjugation_fr_2705():
    assert (
V("suivre").t('p').pe(2).n('s').realize()   
    ) == 'suis',\
    'suivre:p2'


def test_conjugation_fr_2706():
    assert (
V("suivre").t('ip').pe(2).n('s').realize()   
    ) == 'suis',\
    'suivre:ip2'


def test_conjugation_fr_2707():
    assert (
V("suivre").t('p').pe(3).n('s').realize()   
    ) == 'suit',\
    'suivre:p3'


def test_conjugation_fr_2708():
    assert (
V("suivre").t('pr').realize()   
    ) == 'suivant',\
    'suivre:pr'


def test_conjugation_fr_2709():
    assert (
V("suivre").t('p').pe(3).n('p').realize()   
    ) == 'suivent',\
    'suivre:p6'


def test_conjugation_fr_2710():
    assert (
V("suivre").t('p').pe(2).n('p').realize()   
    ) == 'suivez',\
    'suivre:p5'


def test_conjugation_fr_2711():
    assert (
V("suivre").t('ip').pe(2).n('p').realize()   
    ) == 'suivez',\
    'suivre:ip5'


def test_conjugation_fr_2712():
    assert (
V("suivre").t('p').pe(1).n('p').realize()   
    ) == 'suivons',\
    'suivre:p4'


def test_conjugation_fr_2713():
    assert (
V("suivre").t('ip').pe(1).n('p').realize()   
    ) == 'suivons',\
    'suivre:ip4'


def test_conjugation_fr_2714():
    assert (
V("suivre").t('pp').realize()   
    ) == 'suivi',\
    'suivre:pp'


def test_conjugation_fr_2715():
    assert (
V("suivre").t('s').pe(1).n('s').realize()   
    ) == 'suive',\
    'suivre:s1'


def test_conjugation_fr_2716():
    assert (
V("suivre").t('s').pe(2).n('s').realize()   
    ) == 'suives',\
    'suivre:s2'


def test_conjugation_fr_2717():
    assert (
V("suivre").t('s').pe(3).n('s').realize()   
    ) == 'suive',\
    'suivre:s3'


def test_conjugation_fr_2718():
    assert (
V("suivre").t('s').pe(1).n('p').realize()   
    ) == 'suivions',\
    'suivre:s4'


def test_conjugation_fr_2719():
    assert (
V("suivre").t('s').pe(2).n('p').realize()   
    ) == 'suiviez',\
    'suivre:s5'


def test_conjugation_fr_2720():
    assert (
V("suivre").t('s').pe(3).n('p').realize()   
    ) == 'suivent',\
    'suivre:s6'


def test_conjugation_fr_2721():
    assert (
V("surprendre").t('pr').realize()   
    ) == 'surprenant',\
    'surprendre:pr'


def test_conjugation_fr_2722():
    assert (
V("surprendre").t('p').pe(3).n('s').realize()   
    ) == 'surprend',\
    'surprendre:p3'


def test_conjugation_fr_2723():
    assert (
V("surprendre").t('p').pe(1).n('s').realize()   
    ) == 'surprends',\
    'surprendre:p1'


def test_conjugation_fr_2724():
    assert (
V("surprendre").t('p').pe(2).n('s').realize()   
    ) == 'surprends',\
    'surprendre:p2'


def test_conjugation_fr_2725():
    assert (
V("surprendre").t('ip').pe(2).n('s').realize()   
    ) == 'surprends',\
    'surprendre:ip2'


def test_conjugation_fr_2726():
    assert (
V("surprendre").t('p').pe(2).n('p').realize()   
    ) == 'surprenez',\
    'surprendre:p5'


def test_conjugation_fr_2727():
    assert (
V("surprendre").t('ip').pe(2).n('p').realize()   
    ) == 'surprenez',\
    'surprendre:ip5'


def test_conjugation_fr_2728():
    assert (
V("surprendre").t('p').pe(3).n('p').realize()   
    ) == 'surprennent',\
    'surprendre:p6'


def test_conjugation_fr_2729():
    assert (
V("surprendre").t('p').pe(1).n('p').realize()   
    ) == 'surprenons',\
    'surprendre:p4'


def test_conjugation_fr_2730():
    assert (
V("surprendre").t('ip').pe(1).n('p').realize()   
    ) == 'surprenons',\
    'surprendre:ip4'


def test_conjugation_fr_2731():
    assert (
V("surprendre").t('pp').realize()   
    ) == 'surpris',\
    'surprendre:pp'


def test_conjugation_fr_2732():
    assert (
V("surprendre").t('s').pe(1).n('s').realize()   
    ) == 'surprenne',\
    'surprendre:s1'


def test_conjugation_fr_2733():
    assert (
V("surprendre").t('s').pe(2).n('s').realize()   
    ) == 'surprennes',\
    'surprendre:s2'


def test_conjugation_fr_2734():
    assert (
V("surprendre").t('s').pe(3).n('s').realize()   
    ) == 'surprenne',\
    'surprendre:s3'


def test_conjugation_fr_2735():
    assert (
V("surprendre").t('s').pe(1).n('p').realize()   
    ) == 'surprenions',\
    'surprendre:s4'


def test_conjugation_fr_2736():
    assert (
V("surprendre").t('s').pe(2).n('p').realize()   
    ) == 'surpreniez',\
    'surprendre:s5'


def test_conjugation_fr_2737():
    assert (
V("surprendre").t('s').pe(3).n('p').realize()   
    ) == 'surprennent',\
    'surprendre:s6'


def test_conjugation_fr_2738():
    assert (
V("survenir").t('pr').realize()   
    ) == 'survenant',\
    'survenir:pr'


def test_conjugation_fr_2739():
    assert (
V("survenir").t('p').pe(2).n('p').realize()   
    ) == 'survenez',\
    'survenir:p5'


def test_conjugation_fr_2740():
    assert (
V("survenir").t('ip').pe(2).n('p').realize()   
    ) == 'survenez',\
    'survenir:ip5'


def test_conjugation_fr_2741():
    assert (
V("survenir").t('p').pe(1).n('p').realize()   
    ) == 'survenons',\
    'survenir:p4'


def test_conjugation_fr_2742():
    assert (
V("survenir").t('ip').pe(1).n('p').realize()   
    ) == 'survenons',\
    'survenir:ip4'


def test_conjugation_fr_2743():
    assert (
V("survenir").t('p').pe(3).n('p').realize()   
    ) == 'surviennent',\
    'survenir:p6'


def test_conjugation_fr_2744():
    assert (
V("survenir").t('p').pe(1).n('s').realize()   
    ) == 'surviens',\
    'survenir:p1'


def test_conjugation_fr_2745():
    assert (
V("survenir").t('p').pe(2).n('s').realize()   
    ) == 'surviens',\
    'survenir:p2'


def test_conjugation_fr_2746():
    assert (
V("survenir").t('ip').pe(2).n('s').realize()   
    ) == 'surviens',\
    'survenir:ip2'


def test_conjugation_fr_2747():
    assert (
V("survenir").t('p').pe(3).n('s').realize()   
    ) == 'survient',\
    'survenir:p3'


def test_conjugation_fr_2748():
    assert (
V("survenir").t('pp').realize()   
    ) == 'survenu',\
    'survenir:pp'


def test_conjugation_fr_2749():
    assert (
V("survenir").t('s').pe(1).n('s').realize()   
    ) == 'survienne',\
    'survenir:s1'


def test_conjugation_fr_2750():
    assert (
V("survenir").t('s').pe(2).n('s').realize()   
    ) == 'surviennes',\
    'survenir:s2'


def test_conjugation_fr_2751():
    assert (
V("survenir").t('s').pe(3).n('s').realize()   
    ) == 'survienne',\
    'survenir:s3'


def test_conjugation_fr_2752():
    assert (
V("survenir").t('s').pe(1).n('p').realize()   
    ) == 'survenions',\
    'survenir:s4'


def test_conjugation_fr_2753():
    assert (
V("survenir").t('s').pe(2).n('p').realize()   
    ) == 'surveniez',\
    'survenir:s5'


def test_conjugation_fr_2754():
    assert (
V("survenir").t('s').pe(3).n('p').realize()   
    ) == 'surviennent',\
    'survenir:s6'


def test_conjugation_fr_2755():
    assert (
V("suspendre").t('p').pe(3).n('s').realize()   
    ) == 'suspend',\
    'suspendre:p3'


def test_conjugation_fr_2756():
    assert (
V("suspendre").t('pr').realize()   
    ) == 'suspendant',\
    'suspendre:pr'


def test_conjugation_fr_2757():
    assert (
V("suspendre").t('p').pe(3).n('p').realize()   
    ) == 'suspendent',\
    'suspendre:p6'


def test_conjugation_fr_2758():
    assert (
V("suspendre").t('p').pe(2).n('p').realize()   
    ) == 'suspendez',\
    'suspendre:p5'


def test_conjugation_fr_2759():
    assert (
V("suspendre").t('ip').pe(2).n('p').realize()   
    ) == 'suspendez',\
    'suspendre:ip5'


def test_conjugation_fr_2760():
    assert (
V("suspendre").t('p').pe(1).n('p').realize()   
    ) == 'suspendons',\
    'suspendre:p4'


def test_conjugation_fr_2761():
    assert (
V("suspendre").t('ip').pe(1).n('p').realize()   
    ) == 'suspendons',\
    'suspendre:ip4'


def test_conjugation_fr_2762():
    assert (
V("suspendre").t('p').pe(1).n('s').realize()   
    ) == 'suspends',\
    'suspendre:p1'


def test_conjugation_fr_2763():
    assert (
V("suspendre").t('p').pe(2).n('s').realize()   
    ) == 'suspends',\
    'suspendre:p2'


def test_conjugation_fr_2764():
    assert (
V("suspendre").t('ip').pe(2).n('s').realize()   
    ) == 'suspends',\
    'suspendre:ip2'


def test_conjugation_fr_2765():
    assert (
V("suspendre").t('pp').realize()   
    ) == 'suspendu',\
    'suspendre:pp'


def test_conjugation_fr_2766():
    assert (
V("suspendre").t('s').pe(1).n('s').realize()   
    ) == 'suspende',\
    'suspendre:s1'


def test_conjugation_fr_2767():
    assert (
V("suspendre").t('s').pe(2).n('s').realize()   
    ) == 'suspendes',\
    'suspendre:s2'


def test_conjugation_fr_2768():
    assert (
V("suspendre").t('s').pe(3).n('s').realize()   
    ) == 'suspende',\
    'suspendre:s3'


def test_conjugation_fr_2769():
    assert (
V("suspendre").t('s').pe(1).n('p').realize()   
    ) == 'suspendions',\
    'suspendre:s4'


def test_conjugation_fr_2770():
    assert (
V("suspendre").t('s').pe(2).n('p').realize()   
    ) == 'suspendiez',\
    'suspendre:s5'


def test_conjugation_fr_2771():
    assert (
V("suspendre").t('s').pe(3).n('p').realize()   
    ) == 'suspendent',\
    'suspendre:s6'


def test_conjugation_fr_2772():
    assert (
V("taire").t('p').pe(1).n('s').realize()   
    ) == 'tais',\
    'taire:p1'


def test_conjugation_fr_2773():
    assert (
V("taire").t('p').pe(2).n('s').realize()   
    ) == 'tais',\
    'taire:p2'


def test_conjugation_fr_2774():
    assert (
V("taire").t('ip').pe(2).n('s').realize()   
    ) == 'tais',\
    'taire:ip2'


def test_conjugation_fr_2775():
    assert (
V("taire").t('pr').realize()   
    ) == 'taisant',\
    'taire:pr'


def test_conjugation_fr_2776():
    assert (
V("taire").t('p').pe(3).n('p').realize()   
    ) == 'taisent',\
    'taire:p6'


def test_conjugation_fr_2777():
    assert (
V("taire").t('p').pe(2).n('p').realize()   
    ) == 'taisez',\
    'taire:p5'


def test_conjugation_fr_2778():
    assert (
V("taire").t('ip').pe(2).n('p').realize()   
    ) == 'taisez',\
    'taire:ip5'


def test_conjugation_fr_2779():
    assert (
V("taire").t('p').pe(1).n('p').realize()   
    ) == 'taisons',\
    'taire:p4'


def test_conjugation_fr_2780():
    assert (
V("taire").t('ip').pe(1).n('p').realize()   
    ) == 'taisons',\
    'taire:ip4'


def test_conjugation_fr_2781():
    assert (
V("taire").t('p').pe(3).n('s').realize()   
    ) == 'tait',\
    'taire:p3'


def test_conjugation_fr_2782():
    assert (
V("taire").t('pp').realize()   
    ) == 'tu',\
    'taire:pp'


def test_conjugation_fr_2783():
    assert (
V("taire").t('s').pe(1).n('s').realize()   
    ) == 'taise',\
    'taire:s1'


def test_conjugation_fr_2784():
    assert (
V("taire").t('s').pe(2).n('s').realize()   
    ) == 'taises',\
    'taire:s2'


def test_conjugation_fr_2785():
    assert (
V("taire").t('s').pe(3).n('s').realize()   
    ) == 'taise',\
    'taire:s3'


def test_conjugation_fr_2786():
    assert (
V("taire").t('s').pe(1).n('p').realize()   
    ) == 'taisions',\
    'taire:s4'


def test_conjugation_fr_2787():
    assert (
V("taire").t('s').pe(2).n('p').realize()   
    ) == 'taisiez',\
    'taire:s5'


def test_conjugation_fr_2788():
    assert (
V("taire").t('s').pe(3).n('p').realize()   
    ) == 'taisent',\
    'taire:s6'


def test_conjugation_fr_2789():
    assert (
V("tenir").t('pr').realize()   
    ) == 'tenant',\
    'tenir:pr'


def test_conjugation_fr_2790():
    assert (
V("tenir").t('p').pe(2).n('p').realize()   
    ) == 'tenez',\
    'tenir:p5'


def test_conjugation_fr_2791():
    assert (
V("tenir").t('ip').pe(2).n('p').realize()   
    ) == 'tenez',\
    'tenir:ip5'


def test_conjugation_fr_2792():
    assert (
V("tenir").t('p').pe(1).n('p').realize()   
    ) == 'tenons',\
    'tenir:p4'


def test_conjugation_fr_2793():
    assert (
V("tenir").t('ip').pe(1).n('p').realize()   
    ) == 'tenons',\
    'tenir:ip4'


def test_conjugation_fr_2794():
    assert (
V("tenir").t('p').pe(3).n('p').realize()   
    ) == 'tiennent',\
    'tenir:p6'


def test_conjugation_fr_2795():
    assert (
V("tenir").t('p').pe(1).n('s').realize()   
    ) == 'tiens',\
    'tenir:p1'


def test_conjugation_fr_2796():
    assert (
V("tenir").t('p').pe(2).n('s').realize()   
    ) == 'tiens',\
    'tenir:p2'


def test_conjugation_fr_2797():
    assert (
V("tenir").t('ip').pe(2).n('s').realize()   
    ) == 'tiens',\
    'tenir:ip2'


def test_conjugation_fr_2798():
    assert (
V("tenir").t('p').pe(3).n('s').realize()   
    ) == 'tient',\
    'tenir:p3'


def test_conjugation_fr_2799():
    assert (
V("tenir").t('pp').realize()   
    ) == 'tenu',\
    'tenir:pp'


def test_conjugation_fr_2800():
    assert (
V("tenir").t('s').pe(1).n('s').realize()   
    ) == 'tienne',\
    'tenir:s1'


def test_conjugation_fr_2801():
    assert (
V("tenir").t('s').pe(2).n('s').realize()   
    ) == 'tiennes',\
    'tenir:s2'


def test_conjugation_fr_2802():
    assert (
V("tenir").t('s').pe(3).n('s').realize()   
    ) == 'tienne',\
    'tenir:s3'


def test_conjugation_fr_2803():
    assert (
V("tenir").t('s').pe(1).n('p').realize()   
    ) == 'tenions',\
    'tenir:s4'


def test_conjugation_fr_2804():
    assert (
V("tenir").t('s').pe(2).n('p').realize()   
    ) == 'teniez',\
    'tenir:s5'


def test_conjugation_fr_2805():
    assert (
V("tenir").t('s').pe(3).n('p').realize()   
    ) == 'tiennent',\
    'tenir:s6'


def test_conjugation_fr_2806():
    assert (
V("tordre").t('p').pe(3).n('s').realize()   
    ) == 'tord',\
    'tordre:p3'


def test_conjugation_fr_2807():
    assert (
V("tordre").t('pr').realize()   
    ) == 'tordant',\
    'tordre:pr'


def test_conjugation_fr_2808():
    assert (
V("tordre").t('p').pe(3).n('p').realize()   
    ) == 'tordent',\
    'tordre:p6'


def test_conjugation_fr_2809():
    assert (
V("tordre").t('p').pe(2).n('p').realize()   
    ) == 'tordez',\
    'tordre:p5'


def test_conjugation_fr_2810():
    assert (
V("tordre").t('ip').pe(2).n('p').realize()   
    ) == 'tordez',\
    'tordre:ip5'


def test_conjugation_fr_2811():
    assert (
V("tordre").t('p').pe(1).n('p').realize()   
    ) == 'tordons',\
    'tordre:p4'


def test_conjugation_fr_2812():
    assert (
V("tordre").t('ip').pe(1).n('p').realize()   
    ) == 'tordons',\
    'tordre:ip4'


def test_conjugation_fr_2813():
    assert (
V("tordre").t('p').pe(1).n('s').realize()   
    ) == 'tords',\
    'tordre:p1'


def test_conjugation_fr_2814():
    assert (
V("tordre").t('p').pe(2).n('s').realize()   
    ) == 'tords',\
    'tordre:p2'


def test_conjugation_fr_2815():
    assert (
V("tordre").t('ip').pe(2).n('s').realize()   
    ) == 'tords',\
    'tordre:ip2'


def test_conjugation_fr_2816():
    assert (
V("tordre").t('pp').realize()   
    ) == 'tordu',\
    'tordre:pp'


def test_conjugation_fr_2817():
    assert (
V("tordre").t('s').pe(1).n('s').realize()   
    ) == 'torde',\
    'tordre:s1'


def test_conjugation_fr_2818():
    assert (
V("tordre").t('s').pe(2).n('s').realize()   
    ) == 'tordes',\
    'tordre:s2'


def test_conjugation_fr_2819():
    assert (
V("tordre").t('s').pe(3).n('s').realize()   
    ) == 'torde',\
    'tordre:s3'


def test_conjugation_fr_2820():
    assert (
V("tordre").t('s').pe(1).n('p').realize()   
    ) == 'tordions',\
    'tordre:s4'


def test_conjugation_fr_2821():
    assert (
V("tordre").t('s').pe(2).n('p').realize()   
    ) == 'tordiez',\
    'tordre:s5'


def test_conjugation_fr_2822():
    assert (
V("tordre").t('s').pe(3).n('p').realize()   
    ) == 'tordent',\
    'tordre:s6'


def test_conjugation_fr_2823():
    assert (
V("transmettre").t('p').pe(3).n('s').realize()   
    ) == 'transmet',\
    'transmettre:p3'


def test_conjugation_fr_2824():
    assert (
V("transmettre").t('p').pe(1).n('s').realize()   
    ) == 'transmets',\
    'transmettre:p1'


def test_conjugation_fr_2825():
    assert (
V("transmettre").t('p').pe(2).n('s').realize()   
    ) == 'transmets',\
    'transmettre:p2'


def test_conjugation_fr_2826():
    assert (
V("transmettre").t('ip').pe(2).n('s').realize()   
    ) == 'transmets',\
    'transmettre:ip2'


def test_conjugation_fr_2827():
    assert (
V("transmettre").t('pr').realize()   
    ) == 'transmettant',\
    'transmettre:pr'


def test_conjugation_fr_2828():
    assert (
V("transmettre").t('p').pe(3).n('p').realize()   
    ) == 'transmettent',\
    'transmettre:p6'


def test_conjugation_fr_2829():
    assert (
V("transmettre").t('p').pe(2).n('p').realize()   
    ) == 'transmettez',\
    'transmettre:p5'


def test_conjugation_fr_2830():
    assert (
V("transmettre").t('ip').pe(2).n('p').realize()   
    ) == 'transmettez',\
    'transmettre:ip5'


def test_conjugation_fr_2831():
    assert (
V("transmettre").t('p').pe(1).n('p').realize()   
    ) == 'transmettons',\
    'transmettre:p4'


def test_conjugation_fr_2832():
    assert (
V("transmettre").t('ip').pe(1).n('p').realize()   
    ) == 'transmettons',\
    'transmettre:ip4'


def test_conjugation_fr_2833():
    assert (
V("transmettre").t('pp').realize()   
    ) == 'transmis',\
    'transmettre:pp'


def test_conjugation_fr_2834():
    assert (
V("transmettre").t('s').pe(1).n('s').realize()   
    ) == 'transmette',\
    'transmettre:s1'


def test_conjugation_fr_2835():
    assert (
V("transmettre").t('s').pe(2).n('s').realize()   
    ) == 'transmettes',\
    'transmettre:s2'


def test_conjugation_fr_2836():
    assert (
V("transmettre").t('s').pe(3).n('s').realize()   
    ) == 'transmette',\
    'transmettre:s3'


def test_conjugation_fr_2837():
    assert (
V("transmettre").t('s').pe(1).n('p').realize()   
    ) == 'transmettions',\
    'transmettre:s4'


def test_conjugation_fr_2838():
    assert (
V("transmettre").t('s').pe(2).n('p').realize()   
    ) == 'transmettiez',\
    'transmettre:s5'


def test_conjugation_fr_2839():
    assert (
V("transmettre").t('s').pe(3).n('p').realize()   
    ) == 'transmettent',\
    'transmettre:s6'


def test_conjugation_fr_2840():
    assert (
V("tressaillir").t('pr').realize()   
    ) == 'tressaillant',\
    'tressaillir:pr'


def test_conjugation_fr_2841():
    assert (
V("tressaillir").t('p').pe(1).n('s').realize()   
    ) == 'tressaille',\
    'tressaillir:p1'


def test_conjugation_fr_2842():
    assert (
V("tressaillir").t('p').pe(3).n('s').realize()   
    ) == 'tressaille',\
    'tressaillir:p3'


def test_conjugation_fr_2843():
    assert (
V("tressaillir").t('ip').pe(2).n('s').realize()   
    ) == 'tressaille',\
    'tressaillir:ip2'


def test_conjugation_fr_2844():
    assert (
V("tressaillir").t('p').pe(3).n('p').realize()   
    ) == 'tressaillent',\
    'tressaillir:p6'


def test_conjugation_fr_2845():
    assert (
V("tressaillir").t('p').pe(2).n('s').realize()   
    ) == 'tressailles',\
    'tressaillir:p2'


def test_conjugation_fr_2846():
    assert (
V("tressaillir").t('p').pe(2).n('p').realize()   
    ) == 'tressaillez',\
    'tressaillir:p5'


def test_conjugation_fr_2847():
    assert (
V("tressaillir").t('ip').pe(2).n('p').realize()   
    ) == 'tressaillez',\
    'tressaillir:ip5'


def test_conjugation_fr_2848():
    assert (
V("tressaillir").t('p').pe(1).n('p').realize()   
    ) == 'tressaillons',\
    'tressaillir:p4'


def test_conjugation_fr_2849():
    assert (
V("tressaillir").t('ip').pe(1).n('p').realize()   
    ) == 'tressaillons',\
    'tressaillir:ip4'


def test_conjugation_fr_2850():
    assert (
V("tressaillir").t('pp').realize()   
    ) == 'tressailli',\
    'tressaillir:pp'


def test_conjugation_fr_2851():
    assert (
V("tressaillir").t('s').pe(1).n('s').realize()   
    ) == 'tressaille',\
    'tressaillir:s1'


def test_conjugation_fr_2852():
    assert (
V("tressaillir").t('s').pe(2).n('s').realize()   
    ) == 'tressailles',\
    'tressaillir:s2'


def test_conjugation_fr_2853():
    assert (
V("tressaillir").t('s').pe(3).n('s').realize()   
    ) == 'tressaille',\
    'tressaillir:s3'


def test_conjugation_fr_2854():
    assert (
V("tressaillir").t('s').pe(1).n('p').realize()   
    ) == 'tressaillions',\
    'tressaillir:s4'


def test_conjugation_fr_2855():
    assert (
V("tressaillir").t('s').pe(2).n('p').realize()   
    ) == 'tressailliez',\
    'tressaillir:s5'


def test_conjugation_fr_2856():
    assert (
V("tressaillir").t('s').pe(3).n('p').realize()   
    ) == 'tressaillent',\
    'tressaillir:s6'


def test_conjugation_fr_2857():
    assert (
V("vaincre").t('p').pe(3).n('s').realize()   
    ) == 'vainc',\
    'vaincre:p3'


def test_conjugation_fr_2858():
    assert (
V("vaincre").t('p').pe(1).n('s').realize()   
    ) == 'vaincs',\
    'vaincre:p1'


def test_conjugation_fr_2859():
    assert (
V("vaincre").t('p').pe(2).n('s').realize()   
    ) == 'vaincs',\
    'vaincre:p2'


def test_conjugation_fr_2860():
    assert (
V("vaincre").t('ip').pe(2).n('s').realize()   
    ) == 'vaincs',\
    'vaincre:ip2'


def test_conjugation_fr_2861():
    assert (
V("vaincre").t('pr').realize()   
    ) == 'vainquant',\
    'vaincre:pr'


def test_conjugation_fr_2862():
    assert (
V("vaincre").t('p').pe(3).n('p').realize()   
    ) == 'vainquent',\
    'vaincre:p6'


def test_conjugation_fr_2863():
    assert (
V("vaincre").t('p').pe(2).n('p').realize()   
    ) == 'vainquez',\
    'vaincre:p5'


def test_conjugation_fr_2864():
    assert (
V("vaincre").t('ip').pe(2).n('p').realize()   
    ) == 'vainquez',\
    'vaincre:ip5'


def test_conjugation_fr_2865():
    assert (
V("vaincre").t('p').pe(1).n('p').realize()   
    ) == 'vainquons',\
    'vaincre:p4'


def test_conjugation_fr_2866():
    assert (
V("vaincre").t('ip').pe(1).n('p').realize()   
    ) == 'vainquons',\
    'vaincre:ip4'


def test_conjugation_fr_2867():
    assert (
V("vaincre").t('pp').realize()   
    ) == 'vaincu',\
    'vaincre:pp'


def test_conjugation_fr_2868():
    assert (
V("vaincre").t('s').pe(1).n('s').realize()   
    ) == 'vainque',\
    'vaincre:s1'


def test_conjugation_fr_2869():
    assert (
V("vaincre").t('s').pe(2).n('s').realize()   
    ) == 'vainques',\
    'vaincre:s2'


def test_conjugation_fr_2870():
    assert (
V("vaincre").t('s').pe(3).n('s').realize()   
    ) == 'vainque',\
    'vaincre:s3'


def test_conjugation_fr_2871():
    assert (
V("vaincre").t('s').pe(1).n('p').realize()   
    ) == 'vainquions',\
    'vaincre:s4'


def test_conjugation_fr_2872():
    assert (
V("vaincre").t('s').pe(2).n('p').realize()   
    ) == 'vainquiez',\
    'vaincre:s5'


def test_conjugation_fr_2873():
    assert (
V("vaincre").t('s').pe(3).n('p').realize()   
    ) == 'vainquent',\
    'vaincre:s6'


def test_conjugation_fr_2874():
    assert (
V("valoir").t('pr').realize()   
    ) == 'valant',\
    'valoir:pr'


def test_conjugation_fr_2875():
    assert (
V("valoir").t('p').pe(3).n('p').realize()   
    ) == 'valent',\
    'valoir:p6'


def test_conjugation_fr_2876():
    assert (
V("valoir").t('p').pe(2).n('p').realize()   
    ) == 'valez',\
    'valoir:p5'


def test_conjugation_fr_2877():
    assert (
V("valoir").t('ip').pe(2).n('p').realize()   
    ) == 'valez',\
    'valoir:ip5'


def test_conjugation_fr_2878():
    assert (
V("valoir").t('p').pe(1).n('p').realize()   
    ) == 'valons',\
    'valoir:p4'


def test_conjugation_fr_2879():
    assert (
V("valoir").t('ip').pe(1).n('p').realize()   
    ) == 'valons',\
    'valoir:ip4'


def test_conjugation_fr_2880():
    assert (
V("valoir").t('p').pe(3).n('s').realize()   
    ) == 'vaut',\
    'valoir:p3'


def test_conjugation_fr_2881():
    assert (
V("valoir").t('p').pe(1).n('s').realize()   
    ) == 'vaux',\
    'valoir:p1'


def test_conjugation_fr_2882():
    assert (
V("valoir").t('p').pe(2).n('s').realize()   
    ) == 'vaux',\
    'valoir:p2'


def test_conjugation_fr_2883():
    assert (
V("valoir").t('ip').pe(2).n('s').realize()   
    ) == 'vaux',\
    'valoir:ip2'


def test_conjugation_fr_2884():
    assert (
V("valoir").t('pp').realize()   
    ) == 'valu',\
    'valoir:pp'


def test_conjugation_fr_2885():
    assert (
V("valoir").t('s').pe(1).n('s').realize()   
    ) == 'vaille',\
    'valoir:s1'


def test_conjugation_fr_2886():
    assert (
V("valoir").t('s').pe(2).n('s').realize()   
    ) == 'vailles',\
    'valoir:s2'


def test_conjugation_fr_2887():
    assert (
V("valoir").t('s').pe(3).n('s').realize()   
    ) == 'vaille',\
    'valoir:s3'


def test_conjugation_fr_2888():
    assert (
V("valoir").t('s').pe(1).n('p').realize()   
    ) == 'valions',\
    'valoir:s4'


def test_conjugation_fr_2889():
    assert (
V("valoir").t('s').pe(2).n('p').realize()   
    ) == 'valiez',\
    'valoir:s5'


def test_conjugation_fr_2890():
    assert (
V("valoir").t('s').pe(3).n('p').realize()   
    ) == 'vaillent',\
    'valoir:s6'


def test_conjugation_fr_2891():
    assert (
V("vendre").t('p').pe(3).n('s').realize()   
    ) == 'vend',\
    'vendre:p3'


def test_conjugation_fr_2892():
    assert (
V("vendre").t('pr').realize()   
    ) == 'vendant',\
    'vendre:pr'


def test_conjugation_fr_2893():
    assert (
V("vendre").t('p').pe(3).n('p').realize()   
    ) == 'vendent',\
    'vendre:p6'


def test_conjugation_fr_2894():
    assert (
V("vendre").t('p').pe(2).n('p').realize()   
    ) == 'vendez',\
    'vendre:p5'


def test_conjugation_fr_2895():
    assert (
V("vendre").t('ip').pe(2).n('p').realize()   
    ) == 'vendez',\
    'vendre:ip5'


def test_conjugation_fr_2896():
    assert (
V("vendre").t('p').pe(1).n('p').realize()   
    ) == 'vendons',\
    'vendre:p4'


def test_conjugation_fr_2897():
    assert (
V("vendre").t('ip').pe(1).n('p').realize()   
    ) == 'vendons',\
    'vendre:ip4'


def test_conjugation_fr_2898():
    assert (
V("vendre").t('p').pe(1).n('s').realize()   
    ) == 'vends',\
    'vendre:p1'


def test_conjugation_fr_2899():
    assert (
V("vendre").t('p').pe(2).n('s').realize()   
    ) == 'vends',\
    'vendre:p2'


def test_conjugation_fr_2900():
    assert (
V("vendre").t('ip').pe(2).n('s').realize()   
    ) == 'vends',\
    'vendre:ip2'


def test_conjugation_fr_2901():
    assert (
V("vendre").t('pp').realize()   
    ) == 'vendu',\
    'vendre:pp'


def test_conjugation_fr_2902():
    assert (
V("vendre").t('s').pe(1).n('s').realize()   
    ) == 'vende',\
    'vendre:s1'


def test_conjugation_fr_2903():
    assert (
V("vendre").t('s').pe(2).n('s').realize()   
    ) == 'vendes',\
    'vendre:s2'


def test_conjugation_fr_2904():
    assert (
V("vendre").t('s').pe(3).n('s').realize()   
    ) == 'vende',\
    'vendre:s3'


def test_conjugation_fr_2905():
    assert (
V("vendre").t('s').pe(1).n('p').realize()   
    ) == 'vendions',\
    'vendre:s4'


def test_conjugation_fr_2906():
    assert (
V("vendre").t('s').pe(2).n('p').realize()   
    ) == 'vendiez',\
    'vendre:s5'


def test_conjugation_fr_2907():
    assert (
V("vendre").t('s').pe(3).n('p').realize()   
    ) == 'vendent',\
    'vendre:s6'


def test_conjugation_fr_2908():
    assert (
V("venir").t('pr').realize()   
    ) == 'venant',\
    'venir:pr'


def test_conjugation_fr_2909():
    assert (
V("venir").t('p').pe(2).n('p').realize()   
    ) == 'venez',\
    'venir:p5'


def test_conjugation_fr_2910():
    assert (
V("venir").t('ip').pe(2).n('p').realize()   
    ) == 'venez',\
    'venir:ip5'


def test_conjugation_fr_2911():
    assert (
V("venir").t('p').pe(1).n('p').realize()   
    ) == 'venons',\
    'venir:p4'


def test_conjugation_fr_2912():
    assert (
V("venir").t('ip').pe(1).n('p').realize()   
    ) == 'venons',\
    'venir:ip4'


def test_conjugation_fr_2913():
    assert (
V("venir").t('p').pe(3).n('p').realize()   
    ) == 'viennent',\
    'venir:p6'


def test_conjugation_fr_2914():
    assert (
V("venir").t('p').pe(1).n('s').realize()   
    ) == 'viens',\
    'venir:p1'


def test_conjugation_fr_2915():
    assert (
V("venir").t('p').pe(2).n('s').realize()   
    ) == 'viens',\
    'venir:p2'


def test_conjugation_fr_2916():
    assert (
V("venir").t('ip').pe(2).n('s').realize()   
    ) == 'viens',\
    'venir:ip2'


def test_conjugation_fr_2917():
    assert (
V("venir").t('p').pe(3).n('s').realize()   
    ) == 'vient',\
    'venir:p3'


def test_conjugation_fr_2918():
    assert (
V("venir").t('pp').realize()   
    ) == 'venu',\
    'venir:pp'


def test_conjugation_fr_2919():
    assert (
V("venir").t('s').pe(1).n('s').realize()   
    ) == 'vienne',\
    'venir:s1'


def test_conjugation_fr_2920():
    assert (
V("venir").t('s').pe(2).n('s').realize()   
    ) == 'viennes',\
    'venir:s2'


def test_conjugation_fr_2921():
    assert (
V("venir").t('s').pe(3).n('s').realize()   
    ) == 'vienne',\
    'venir:s3'


def test_conjugation_fr_2922():
    assert (
V("venir").t('s').pe(1).n('p').realize()   
    ) == 'venions',\
    'venir:s4'


def test_conjugation_fr_2923():
    assert (
V("venir").t('s').pe(2).n('p').realize()   
    ) == 'veniez',\
    'venir:s5'


def test_conjugation_fr_2924():
    assert (
V("venir").t('s').pe(3).n('p').realize()   
    ) == 'viennent',\
    'venir:s6'


def test_conjugation_fr_2925():
    assert (
V("vêtir").t('p').pe(3).n('s').realize()   
    ) == 'vêt',\
    'vêtir:p3'


def test_conjugation_fr_2926():
    assert (
V("vêtir").t('pr').realize()   
    ) == 'vêtant',\
    'vêtir:pr'


def test_conjugation_fr_2927():
    assert (
V("vêtir").t('p').pe(3).n('p').realize()   
    ) == 'vêtent',\
    'vêtir:p6'


def test_conjugation_fr_2928():
    assert (
V("vêtir").t('p').pe(2).n('p').realize()   
    ) == 'vêtez',\
    'vêtir:p5'


def test_conjugation_fr_2929():
    assert (
V("vêtir").t('ip').pe(2).n('p').realize()   
    ) == 'vêtez',\
    'vêtir:ip5'


def test_conjugation_fr_2930():
    assert (
V("vêtir").t('p').pe(1).n('p').realize()   
    ) == 'vêtons',\
    'vêtir:p4'


def test_conjugation_fr_2931():
    assert (
V("vêtir").t('ip').pe(1).n('p').realize()   
    ) == 'vêtons',\
    'vêtir:ip4'


def test_conjugation_fr_2932():
    assert (
V("vêtir").t('p').pe(1).n('s').realize()   
    ) == 'vêts',\
    'vêtir:p1'


def test_conjugation_fr_2933():
    assert (
V("vêtir").t('p').pe(2).n('s').realize()   
    ) == 'vêts',\
    'vêtir:p2'


def test_conjugation_fr_2934():
    assert (
V("vêtir").t('ip').pe(2).n('s').realize()   
    ) == 'vêts',\
    'vêtir:ip2'


def test_conjugation_fr_2935():
    assert (
V("vêtir").t('pp').realize()   
    ) == 'vêtu',\
    'vêtir:pp'


def test_conjugation_fr_2936():
    assert (
V("vêtir").t('s').pe(1).n('s').realize()   
    ) == 'vête',\
    'vêtir:s1'


def test_conjugation_fr_2937():
    assert (
V("vêtir").t('s').pe(2).n('s').realize()   
    ) == 'vêtes',\
    'vêtir:s2'


def test_conjugation_fr_2938():
    assert (
V("vêtir").t('s').pe(3).n('s').realize()   
    ) == 'vête',\
    'vêtir:s3'


def test_conjugation_fr_2939():
    assert (
V("vêtir").t('s').pe(1).n('p').realize()   
    ) == 'vêtions',\
    'vêtir:s4'


def test_conjugation_fr_2940():
    assert (
V("vêtir").t('s').pe(2).n('p').realize()   
    ) == 'vêtiez',\
    'vêtir:s5'


def test_conjugation_fr_2941():
    assert (
V("vêtir").t('s').pe(3).n('p').realize()   
    ) == 'vêtent',\
    'vêtir:s6'


def test_conjugation_fr_2942():
    assert (
V("vivre").t('p').pe(1).n('s').realize()   
    ) == 'vis',\
    'vivre:p1'


def test_conjugation_fr_2943():
    assert (
V("vivre").t('p').pe(2).n('s').realize()   
    ) == 'vis',\
    'vivre:p2'


def test_conjugation_fr_2944():
    assert (
V("vivre").t('ip').pe(2).n('s').realize()   
    ) == 'vis',\
    'vivre:ip2'


def test_conjugation_fr_2945():
    assert (
V("vivre").t('p').pe(3).n('s').realize()   
    ) == 'vit',\
    'vivre:p3'


def test_conjugation_fr_2946():
    assert (
V("vivre").t('pr').realize()   
    ) == 'vivant',\
    'vivre:pr'


def test_conjugation_fr_2947():
    assert (
V("vivre").t('p').pe(3).n('p').realize()   
    ) == 'vivent',\
    'vivre:p6'


def test_conjugation_fr_2948():
    assert (
V("vivre").t('p').pe(2).n('p').realize()   
    ) == 'vivez',\
    'vivre:p5'


def test_conjugation_fr_2949():
    assert (
V("vivre").t('ip').pe(2).n('p').realize()   
    ) == 'vivez',\
    'vivre:ip5'


def test_conjugation_fr_2950():
    assert (
V("vivre").t('p').pe(1).n('p').realize()   
    ) == 'vivons',\
    'vivre:p4'


def test_conjugation_fr_2951():
    assert (
V("vivre").t('ip').pe(1).n('p').realize()   
    ) == 'vivons',\
    'vivre:ip4'


def test_conjugation_fr_2952():
    assert (
V("vivre").t('s').pe(1).n('s').realize()   
    ) == 'vive',\
    'vivre:s1'


def test_conjugation_fr_2953():
    assert (
V("vivre").t('s').pe(2).n('s').realize()   
    ) == 'vives',\
    'vivre:s2'


def test_conjugation_fr_2954():
    assert (
V("vivre").t('s').pe(3).n('s').realize()   
    ) == 'vive',\
    'vivre:s3'


def test_conjugation_fr_2955():
    assert (
V("vivre").t('s').pe(1).n('p').realize()   
    ) == 'vivions',\
    'vivre:s4'


def test_conjugation_fr_2956():
    assert (
V("vivre").t('s').pe(2).n('p').realize()   
    ) == 'viviez',\
    'vivre:s5'


def test_conjugation_fr_2957():
    assert (
V("vivre").t('s').pe(3).n('p').realize()   
    ) == 'vivent',\
    'vivre:s6'


def test_conjugation_fr_2958():
    assert (
V("voir").t('p').pe(3).n('p').realize()   
    ) == 'voient',\
    'voir:p6'


def test_conjugation_fr_2959():
    assert (
V("voir").t('p').pe(1).n('s').realize()   
    ) == 'vois',\
    'voir:p1'


def test_conjugation_fr_2960():
    assert (
V("voir").t('p').pe(2).n('s').realize()   
    ) == 'vois',\
    'voir:p2'


def test_conjugation_fr_2961():
    assert (
V("voir").t('ip').pe(2).n('s').realize()   
    ) == 'vois',\
    'voir:ip2'


def test_conjugation_fr_2962():
    assert (
V("voir").t('p').pe(3).n('s').realize()   
    ) == 'voit',\
    'voir:p3'


def test_conjugation_fr_2963():
    assert (
V("voir").t('pr').realize()   
    ) == 'voyant',\
    'voir:pr'


def test_conjugation_fr_2964():
    assert (
V("voir").t('p').pe(2).n('p').realize()   
    ) == 'voyez',\
    'voir:p5'


def test_conjugation_fr_2965():
    assert (
V("voir").t('ip').pe(2).n('p').realize()   
    ) == 'voyez',\
    'voir:ip5'


def test_conjugation_fr_2966():
    assert (
V("voir").t('p').pe(1).n('p').realize()   
    ) == 'voyons',\
    'voir:p4'


def test_conjugation_fr_2967():
    assert (
V("voir").t('ip').pe(1).n('p').realize()   
    ) == 'voyons',\
    'voir:ip4'


def test_conjugation_fr_2968():
    assert (
V("voir").t('pp').realize()   
    ) == 'vu',\
    'voir:pp'


def test_conjugation_fr_2969():
    assert (
V("voir").t('s').pe(1).n('s').realize()   
    ) == 'voie',\
    'voir:s1'


def test_conjugation_fr_2970():
    assert (
V("voir").t('s').pe(2).n('s').realize()   
    ) == 'voies',\
    'voir:s2'


def test_conjugation_fr_2971():
    assert (
V("voir").t('s').pe(3).n('s').realize()   
    ) == 'voie',\
    'voir:s3'


def test_conjugation_fr_2972():
    assert (
V("voir").t('s').pe(1).n('p').realize()   
    ) == 'voyions',\
    'voir:s4'


def test_conjugation_fr_2973():
    assert (
V("voir").t('s').pe(2).n('p').realize()   
    ) == 'voyiez',\
    'voir:s5'


def test_conjugation_fr_2974():
    assert (
V("voir").t('s').pe(3).n('p').realize()   
    ) == 'voient',\
    'voir:s6'


def test_conjugation_fr_2975():
    assert (
V("vouloir").t('p').pe(3).n('p').realize()   
    ) == 'veulent',\
    'vouloir:p6'


def test_conjugation_fr_2976():
    assert (
V("vouloir").t('p').pe(3).n('s').realize()   
    ) == 'veut',\
    'vouloir:p3'


def test_conjugation_fr_2977():
    assert (
V("vouloir").t('p').pe(1).n('s').realize()   
    ) == 'veux',\
    'vouloir:p1'


def test_conjugation_fr_2978():
    assert (
V("vouloir").t('p').pe(2).n('s').realize()   
    ) == 'veux',\
    'vouloir:p2'


def test_conjugation_fr_2979():
    assert (
V("vouloir").t('ip').pe(2).n('s').realize()   
    ) == 'veuille',\
    'vouloir:ip2'


def test_conjugation_fr_2980():
    assert (
V("vouloir").t('pr').realize()   
    ) == 'voulant',\
    'vouloir:pr'


def test_conjugation_fr_2981():
    assert (
V("vouloir").t('p').pe(2).n('p').realize()   
    ) == 'voulez',\
    'vouloir:p5'


def test_conjugation_fr_2982():
    assert (
V("vouloir").t('ip').pe(2).n('p').realize()   
    ) == 'veuillez',\
    'vouloir:ip5'


def test_conjugation_fr_2983():
    assert (
V("vouloir").t('p').pe(1).n('p').realize()   
    ) == 'voulons',\
    'vouloir:p4'


def test_conjugation_fr_2984():
    assert (
V("vouloir").t('ip').pe(1).n('p').realize()   
    ) == 'voulons',\
    'vouloir:ip4'


def test_conjugation_fr_2985():
    assert (
V("vouloir").t('pp').realize()   
    ) == 'voulu',\
    'vouloir:pp'


def test_conjugation_fr_2986():
    assert (
V("vouloir").t('s').pe(1).n('s').realize()   
    ) == 'veuille',\
    'vouloir:s1'


def test_conjugation_fr_2987():
    assert (
V("vouloir").t('s').pe(2).n('s').realize()   
    ) == 'veuilles',\
    'vouloir:s2'


def test_conjugation_fr_2988():
    assert (
V("vouloir").t('s').pe(3).n('s').realize()   
    ) == 'veuille',\
    'vouloir:s3'


def test_conjugation_fr_2989():
    assert (
V("vouloir").t('s').pe(1).n('p').realize()   
    ) == 'voulions',\
    'vouloir:s4'


def test_conjugation_fr_2990():
    assert (
V("vouloir").t('s').pe(2).n('p').realize()   
    ) == 'vouliez',\
    'vouloir:s5'


def test_conjugation_fr_2991():
    assert (
V("vouloir").t('s').pe(3).n('p').realize()   
    ) == 'veuillent',\
    'vouloir:s6'

