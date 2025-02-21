import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..','src')))

from pyrealb import *
load("fr")

def test_pronouns_fr_0():
    assert (
Pro("moi").tn('').realize()   
    ) == 'moi',\
    'Pro("moi").tn(\'\')=>moi'


def test_pronouns_fr_1():
    assert (
Pro("moi").tn('refl').realize()   
    ) == 'moi-même',\
    'Pro("moi").tn(\'refl\')=>moi'


def test_pronouns_fr_2():
    assert (
Pro("moi").c('nom').realize()   
    ) == 'je',\
    'Pro("moi").c(\'nom\')=>moi'


def test_pronouns_fr_3():
    assert (
Pro("moi").c('acc').realize()   
    ) == 'me',\
    'Pro("moi").c(\'acc\')=>moi'


def test_pronouns_fr_4():
    assert (
Pro("moi").c('dat').realize()   
    ) == 'me',\
    'Pro("moi").c(\'dat\')=>moi'


def test_pronouns_fr_5():
    assert (
Pro("moi").c('refl').realize()   
    ) == 'me',\
    'Pro("moi").c(\'refl\')=>moi'


def test_pronouns_fr_6():
    assert (
Pro("toi").tn('').realize()   
    ) == 'toi',\
    'Pro("toi").tn(\'\')=>toi'


def test_pronouns_fr_7():
    assert (
Pro("toi").tn('refl').realize()   
    ) == 'toi-même',\
    'Pro("toi").tn(\'refl\')=>toi'


def test_pronouns_fr_8():
    assert (
Pro("toi").c('nom').realize()   
    ) == 'tu',\
    'Pro("toi").c(\'nom\')=>toi'


def test_pronouns_fr_9():
    assert (
Pro("toi").c('acc').realize()   
    ) == 'te',\
    'Pro("toi").c(\'acc\')=>toi'


def test_pronouns_fr_10():
    assert (
Pro("toi").c('dat').realize()   
    ) == 'te',\
    'Pro("toi").c(\'dat\')=>toi'


def test_pronouns_fr_11():
    assert (
Pro("toi").c('refl').realize()   
    ) == 'te',\
    'Pro("toi").c(\'refl\')=>toi'


def test_pronouns_fr_12():
    assert (
Pro("lui").tn('').realize()   
    ) == 'lui',\
    'Pro("lui").tn(\'\')=>lui'


def test_pronouns_fr_13():
    assert (
Pro("lui").tn('refl').realize()   
    ) == 'lui-même',\
    'Pro("lui").tn(\'refl\')=>lui'


def test_pronouns_fr_14():
    assert (
Pro("lui").c('nom').realize()   
    ) == 'il',\
    'Pro("lui").c(\'nom\')=>lui'


def test_pronouns_fr_15():
    assert (
Pro("lui").c('acc').realize()   
    ) == 'le',\
    'Pro("lui").c(\'acc\')=>lui'


def test_pronouns_fr_16():
    assert (
Pro("lui").c('dat').realize()   
    ) == 'lui',\
    'Pro("lui").c(\'dat\')=>lui'


def test_pronouns_fr_17():
    assert (
Pro("lui").c('refl').realize()   
    ) == 'se',\
    'Pro("lui").c(\'refl\')=>lui'


def test_pronouns_fr_18():
    assert (
Pro("elle").tn('').realize()   
    ) == 'elle',\
    'Pro("elle").tn(\'\')=>elle'


def test_pronouns_fr_19():
    assert (
Pro("elle").tn('refl').realize()   
    ) == 'elle-même',\
    'Pro("elle").tn(\'refl\')=>elle'


def test_pronouns_fr_20():
    assert (
Pro("elle").c('nom').realize()   
    ) == 'elle',\
    'Pro("elle").c(\'nom\')=>elle'


def test_pronouns_fr_21():
    assert (
Pro("elle").c('acc').realize()   
    ) == 'la',\
    'Pro("elle").c(\'acc\')=>elle'


def test_pronouns_fr_22():
    assert (
Pro("elle").c('dat').realize()   
    ) == 'lui',\
    'Pro("elle").c(\'dat\')=>elle'


def test_pronouns_fr_23():
    assert (
Pro("elle").c('refl').realize()   
    ) == 'se',\
    'Pro("elle").c(\'refl\')=>elle'


def test_pronouns_fr_24():
    assert (
Pro("on").tn('').realize()   
    ) == 'soi',\
    'Pro("on").tn(\'\')=>on'


def test_pronouns_fr_25():
    assert (
Pro("on").tn('refl').realize()   
    ) == 'soi-même',\
    'Pro("on").tn(\'refl\')=>on'


def test_pronouns_fr_26():
    assert (
Pro("on").c('nom').realize()   
    ) == 'on',\
    'Pro("on").c(\'nom\')=>on'


def test_pronouns_fr_27():
    assert (
Pro("on").c('acc').realize()   
    ) == 'le',\
    'Pro("on").c(\'acc\')=>on'


def test_pronouns_fr_28():
    assert (
Pro("on").c('dat').realize()   
    ) == 'soi',\
    'Pro("on").c(\'dat\')=>on'


def test_pronouns_fr_29():
    assert (
Pro("on").c('refl').realize()   
    ) == 'se',\
    'Pro("on").c(\'refl\')=>on'


def test_pronouns_fr_30():
    assert (
Pro("nous").tn('').realize()   
    ) == 'nous',\
    'Pro("nous").tn(\'\')=>nous'


def test_pronouns_fr_31():
    assert (
Pro("nous").tn('refl').realize()   
    ) == 'nous-mêmes',\
    'Pro("nous").tn(\'refl\')=>nous'


def test_pronouns_fr_32():
    assert (
Pro("nous").c('nom').realize()   
    ) == 'nous',\
    'Pro("nous").c(\'nom\')=>nous'


def test_pronouns_fr_33():
    assert (
Pro("nous").c('acc').realize()   
    ) == 'nous',\
    'Pro("nous").c(\'acc\')=>nous'


def test_pronouns_fr_34():
    assert (
Pro("nous").c('dat').realize()   
    ) == 'nous',\
    'Pro("nous").c(\'dat\')=>nous'


def test_pronouns_fr_35():
    assert (
Pro("nous").c('refl').realize()   
    ) == 'nous',\
    'Pro("nous").c(\'refl\')=>nous'


def test_pronouns_fr_36():
    assert (
Pro("vous").tn('').realize()   
    ) == 'vous',\
    'Pro("vous").tn(\'\')=>vous'


def test_pronouns_fr_37():
    assert (
Pro("vous").tn('refl').realize()   
    ) == 'vous-mêmes',\
    'Pro("vous").tn(\'refl\')=>vous'


def test_pronouns_fr_38():
    assert (
Pro("vous").c('nom').realize()   
    ) == 'vous',\
    'Pro("vous").c(\'nom\')=>vous'


def test_pronouns_fr_39():
    assert (
Pro("vous").c('acc').realize()   
    ) == 'vous',\
    'Pro("vous").c(\'acc\')=>vous'


def test_pronouns_fr_40():
    assert (
Pro("vous").c('dat').realize()   
    ) == 'vous',\
    'Pro("vous").c(\'dat\')=>vous'


def test_pronouns_fr_41():
    assert (
Pro("vous").c('refl').realize()   
    ) == 'vous',\
    'Pro("vous").c(\'refl\')=>vous'


def test_pronouns_fr_42():
    assert (
Pro("eux").tn('').realize()   
    ) == 'eux',\
    'Pro("eux").tn(\'\')=>eux'


def test_pronouns_fr_43():
    assert (
Pro("eux").tn('refl').realize()   
    ) == 'eux-mêmes',\
    'Pro("eux").tn(\'refl\')=>eux'


def test_pronouns_fr_44():
    assert (
Pro("eux").c('nom').realize()   
    ) == 'ils',\
    'Pro("eux").c(\'nom\')=>eux'


def test_pronouns_fr_45():
    assert (
Pro("eux").c('acc').realize()   
    ) == 'les',\
    'Pro("eux").c(\'acc\')=>eux'


def test_pronouns_fr_46():
    assert (
Pro("eux").c('dat').realize()   
    ) == 'leur',\
    'Pro("eux").c(\'dat\')=>eux'


def test_pronouns_fr_47():
    assert (
Pro("eux").c('refl').realize()   
    ) == 'se',\
    'Pro("eux").c(\'refl\')=>eux'


def test_pronouns_fr_48():
    assert (
Pro("elles").tn('').realize()   
    ) == 'elles',\
    'Pro("elles").tn(\'\')=>elles'


def test_pronouns_fr_49():
    assert (
Pro("elles").tn('refl').realize()   
    ) == 'elles-mêmes',\
    'Pro("elles").tn(\'refl\')=>elles'


def test_pronouns_fr_50():
    assert (
Pro("elles").c('nom').realize()   
    ) == 'elles',\
    'Pro("elles").c(\'nom\')=>elles'


def test_pronouns_fr_51():
    assert (
Pro("elles").c('acc').realize()   
    ) == 'les',\
    'Pro("elles").c(\'acc\')=>elles'


def test_pronouns_fr_52():
    assert (
Pro("elles").c('dat').realize()   
    ) == 'leur',\
    'Pro("elles").c(\'dat\')=>elles'


def test_pronouns_fr_53():
    assert (
Pro("elles").c('refl').realize()   
    ) == 'se',\
    'Pro("elles").c(\'refl\')=>elles'


def test_pronouns_fr_54():
    assert (
D("mon").pe(1).n('s').g('m').realize()   
    ) == 'mon',\
    'D("mon").pe(1).n(\'s\').g(\'m\')=>mon'


def test_pronouns_fr_55():
    assert (
D("mon").pe(1).n('s').g('f').realize()   
    ) == 'ma',\
    'D("mon").pe(1).n(\'s\').g(\'f\')=>ma'


def test_pronouns_fr_56():
    assert (
D("mon").pe(1).n('p').g('f').realize()   
    ) == 'mes',\
    'D("mon").pe(1).n(\'p\').g(\'f\')=>mes'


def test_pronouns_fr_57():
    assert (
D("ton").n('s').g('m').realize()   
    ) == 'ton',\
    'D("ton").n(\'s\').g(\'m\')=>ton'


def test_pronouns_fr_58():
    assert (
D("ton").n('s').g('f').realize()   
    ) == 'ta',\
    'D("ton").n(\'s\').g(\'f\')=>ta'


def test_pronouns_fr_59():
    assert (
D("ton").n('p').g('f').realize()   
    ) == 'tes',\
    'D("ton").n(\'p\').g(\'f\')=>tes'


def test_pronouns_fr_60():
    assert (
D("son").n('s').g('m').realize()   
    ) == 'son',\
    'D("son").n(\'s\').g(\'m\')=>son'


def test_pronouns_fr_61():
    assert (
D("son").n('s').g('f').realize()   
    ) == 'sa',\
    'D("son").n(\'s\').g(\'f\')=>sa'


def test_pronouns_fr_62():
    assert (
D("son").n('p').g('f').realize()   
    ) == 'ses',\
    'D("son").n(\'p\').g(\'f\')=>ses'


def test_pronouns_fr_63():
    assert (
D("notre").pe(1).n('s').g('f').realize()   
    ) == 'notre',\
    'D("notre").pe(1).n(\'s\').g(\'f\')=>notre'


def test_pronouns_fr_64():
    assert (
D("notre").pe(1).n('p').g('f').realize()   
    ) == 'nos',\
    'D("notre").pe(1).n(\'p\').g(\'f\')=>nos'


def test_pronouns_fr_65():
    assert (
D("votre").n('s').g('f').realize()   
    ) == 'votre',\
    'D("votre").n(\'s\').g(\'f\')=>votre'


def test_pronouns_fr_66():
    assert (
D("votre").n('p').g('f').realize()   
    ) == 'vos',\
    'D("votre").n(\'p\').g(\'f\')=>vos'


def test_pronouns_fr_67():
    assert (
D("leur").n('s').g('f').realize()   
    ) == 'leur',\
    'D("leur").n(\'s\').g(\'f\')=>leur'


def test_pronouns_fr_68():
    assert (
D("leur").n('p').g('f').realize()   
    ) == 'leurs',\
    'D("leur").n(\'p\').g(\'f\')=>leurs'


def test_pronouns_fr_69():
    assert (
Pro("mien").pe(1).realize()   
    ) == 'mien',\
    'Pro("mien").pe(1)=>mien'


def test_pronouns_fr_70():
    assert (
Pro("mien").n('p').pe(1).realize()   
    ) == 'miens',\
    'Pro("mien").n(\'p\').pe(1)=>miens'


def test_pronouns_fr_71():
    assert (
Pro("mien").g('f').pe(1).realize()   
    ) == 'mienne',\
    'Pro("mien").g(\'f\').pe(1)=>mienne'


def test_pronouns_fr_72():
    assert (
Pro("mien").n('p').g('f').pe(1).realize()   
    ) == 'miennes',\
    'Pro("mien").n(\'p\').g(\'f\').pe(1)=>miennes'


def test_pronouns_fr_73():
    assert (
Pro("tien").realize()   
    ) == 'tien',\
    'Pro("tien")=>tien'


def test_pronouns_fr_74():
    assert (
Pro("tien").n('p').realize()   
    ) == 'tiens',\
    'Pro("tien").n(\'p\')=>tiens'


def test_pronouns_fr_75():
    assert (
Pro("tien").g('f').realize()   
    ) == 'tienne',\
    'Pro("tien").g(\'f\')=>tienne'


def test_pronouns_fr_76():
    assert (
Pro("tien").n('p').g('f').realize()   
    ) == 'tiennes',\
    'Pro("tien").n(\'p\').g(\'f\')=>tiennes'


def test_pronouns_fr_77():
    assert (
Pro("sien").realize()   
    ) == 'sien',\
    'Pro("sien")=>sien'


def test_pronouns_fr_78():
    assert (
Pro("sien").n('p').realize()   
    ) == 'siens',\
    'Pro("sien").n(\'p\')=>siens'


def test_pronouns_fr_79():
    assert (
Pro("sien").g('f').realize()   
    ) == 'sienne',\
    'Pro("sien").g(\'f\')=>sienne'


def test_pronouns_fr_80():
    assert (
Pro("sien").n('p').g('f').realize()   
    ) == 'siennes',\
    'Pro("sien").n(\'p\').g(\'f\')=>siennes'


def test_pronouns_fr_81():
    assert (
Pro("nôtre").g('f').pe(1).realize()   
    ) == 'nôtre',\
    'Pro("nôtre").g(\'f\').pe(1)=>nôtre'


def test_pronouns_fr_82():
    assert (
Pro("nôtre").n('p').g('f').pe(1).realize()   
    ) == 'nôtres',\
    'Pro("nôtre").n(\'p\').g(\'f\').pe(1)=>nôtres'


def test_pronouns_fr_83():
    assert (
Pro("vôtre").g('f').realize()   
    ) == 'vôtre',\
    'Pro("vôtre").g(\'f\')=>vôtre'


def test_pronouns_fr_84():
    assert (
Pro("vôtre").n('p').g('f').realize()   
    ) == 'vôtres',\
    'Pro("vôtre").n(\'p\').g(\'f\')=>vôtres'


def test_pronouns_fr_85():
    assert (
Pro("leur").g('f').realize()   
    ) == 'leur',\
    'Pro("leur").g(\'f\')=>leur'


def test_pronouns_fr_86():
    assert (
Pro("leur").n('p').g('f').realize()   
    ) == 'leurs',\
    'Pro("leur").n(\'p\').g(\'f\')=>leurs'

