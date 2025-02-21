import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..','src')))

from pyrealb import *
load("en")

def test_pronouns_en_0():
    assert (
Pro("me").tn('').pe(1).realize()   
    ) == 'me',\
    'Pro("me").tn(\'\').pe(1)=>me'


def test_pronouns_en_1():
    assert (
Pro("me").tn('refl').pe(1).realize()   
    ) == 'myself',\
    'Pro("me").tn(\'refl\').pe(1)=>me'


def test_pronouns_en_2():
    assert (
Pro("me").c('nom').pe(1).realize()   
    ) == 'I',\
    'Pro("me").c(\'nom\').pe(1)=>me'


def test_pronouns_en_3():
    assert (
Pro("me").c('acc').pe(1).realize()   
    ) == 'me',\
    'Pro("me").c(\'acc\').pe(1)=>me'


def test_pronouns_en_4():
    assert (
Pro("me").c('dat').pe(1).realize()   
    ) == 'me',\
    'Pro("me").c(\'dat\').pe(1)=>me'


def test_pronouns_en_5():
    assert (
Pro("me").c('gen').pe(1).realize()   
    ) == 'mine',\
    'Pro("me").c(\'gen\').pe(1)=>me'


def test_pronouns_en_6():
    assert (
Pro("you").tn('').realize()   
    ) == 'you',\
    'Pro("you").tn(\'\')=>you'


def test_pronouns_en_7():
    assert (
Pro("you").tn('refl').realize()   
    ) == 'yourself',\
    'Pro("you").tn(\'refl\')=>you'


def test_pronouns_en_8():
    assert (
Pro("you").c('nom').realize()   
    ) == 'you',\
    'Pro("you").c(\'nom\')=>you'


def test_pronouns_en_9():
    assert (
Pro("you").c('acc').realize()   
    ) == 'you',\
    'Pro("you").c(\'acc\')=>you'


def test_pronouns_en_10():
    assert (
Pro("you").c('dat').realize()   
    ) == 'you',\
    'Pro("you").c(\'dat\')=>you'


def test_pronouns_en_11():
    assert (
Pro("you").c('gen').realize()   
    ) == 'yours',\
    'Pro("you").c(\'gen\')=>you'


def test_pronouns_en_12():
    assert (
Pro("him").tn('').realize()   
    ) == 'him',\
    'Pro("him").tn(\'\')=>him'


def test_pronouns_en_13():
    assert (
Pro("him").tn('refl').realize()   
    ) == 'himself',\
    'Pro("him").tn(\'refl\')=>him'


def test_pronouns_en_14():
    assert (
Pro("him").c('nom').realize()   
    ) == 'he',\
    'Pro("him").c(\'nom\')=>him'


def test_pronouns_en_15():
    assert (
Pro("him").c('acc').realize()   
    ) == 'him',\
    'Pro("him").c(\'acc\')=>him'


def test_pronouns_en_16():
    assert (
Pro("him").c('dat').realize()   
    ) == 'him',\
    'Pro("him").c(\'dat\')=>him'


def test_pronouns_en_17():
    assert (
Pro("him").c('gen').realize()   
    ) == 'his',\
    'Pro("him").c(\'gen\')=>him'


def test_pronouns_en_18():
    assert (
Pro("her").tn('').realize()   
    ) == 'her',\
    'Pro("her").tn(\'\')=>her'


def test_pronouns_en_19():
    assert (
Pro("her").tn('refl').realize()   
    ) == 'herself',\
    'Pro("her").tn(\'refl\')=>her'


def test_pronouns_en_20():
    assert (
Pro("her").c('nom').realize()   
    ) == 'she',\
    'Pro("her").c(\'nom\')=>her'


def test_pronouns_en_21():
    assert (
Pro("her").c('acc').realize()   
    ) == 'her',\
    'Pro("her").c(\'acc\')=>her'


def test_pronouns_en_22():
    assert (
Pro("her").c('dat').realize()   
    ) == 'her',\
    'Pro("her").c(\'dat\')=>her'


def test_pronouns_en_23():
    assert (
Pro("her").c('gen').realize()   
    ) == 'hers',\
    'Pro("her").c(\'gen\')=>her'


def test_pronouns_en_24():
    assert (
Pro("it").tn('').realize()   
    ) == 'it',\
    'Pro("it").tn(\'\')=>it'


def test_pronouns_en_25():
    assert (
Pro("it").tn('refl').realize()   
    ) == 'itself',\
    'Pro("it").tn(\'refl\')=>it'


def test_pronouns_en_26():
    assert (
Pro("it").c('nom').realize()   
    ) == 'it',\
    'Pro("it").c(\'nom\')=>it'


def test_pronouns_en_27():
    assert (
Pro("it").c('acc').realize()   
    ) == 'it',\
    'Pro("it").c(\'acc\')=>it'


def test_pronouns_en_28():
    assert (
Pro("it").c('dat').realize()   
    ) == 'it',\
    'Pro("it").c(\'dat\')=>it'


def test_pronouns_en_29():
    assert (
Pro("it").c('gen').realize()   
    ) == 'its',\
    'Pro("it").c(\'gen\')=>it'


def test_pronouns_en_30():
    assert (
Pro("us").tn('').realize()   
    ) == 'us',\
    'Pro("us").tn(\'\')=>us'


def test_pronouns_en_31():
    assert (
Pro("us").tn('refl').realize()   
    ) == 'ourselves',\
    'Pro("us").tn(\'refl\')=>us'


def test_pronouns_en_32():
    assert (
Pro("us").c('nom').realize()   
    ) == 'we',\
    'Pro("us").c(\'nom\')=>us'


def test_pronouns_en_33():
    assert (
Pro("us").c('acc').realize()   
    ) == 'us',\
    'Pro("us").c(\'acc\')=>us'


def test_pronouns_en_34():
    assert (
Pro("us").c('dat').realize()   
    ) == 'us',\
    'Pro("us").c(\'dat\')=>us'


def test_pronouns_en_35():
    assert (
Pro("us").c('gen').realize()   
    ) == 'ours',\
    'Pro("us").c(\'gen\')=>us'


def test_pronouns_en_36():
    assert (
Pro("them").tn('').realize()   
    ) == 'them',\
    'Pro("them").tn(\'\')=>them'


def test_pronouns_en_37():
    assert (
Pro("them").tn('refl').realize()   
    ) == 'themselves',\
    'Pro("them").tn(\'refl\')=>them'


def test_pronouns_en_38():
    assert (
Pro("them").c('nom').realize()   
    ) == 'they',\
    'Pro("them").c(\'nom\')=>them'


def test_pronouns_en_39():
    assert (
Pro("them").c('acc').realize()   
    ) == 'them',\
    'Pro("them").c(\'acc\')=>them'


def test_pronouns_en_40():
    assert (
Pro("them").c('dat').realize()   
    ) == 'them',\
    'Pro("them").c(\'dat\')=>them'


def test_pronouns_en_41():
    assert (
Pro("them").c('gen').realize()   
    ) == 'theirs',\
    'Pro("them").c(\'gen\')=>them'


def test_pronouns_en_42():
    assert (
D("my").pe(1).ow('s').realize()   
    ) == 'my',\
    'D("my").pe(1).ow(\'s\')=>my'


def test_pronouns_en_43():
    assert (
D("my").pe(2).ow('p').realize()   
    ) == 'your',\
    'D("my").pe(2).ow(\'p\')=>your'


def test_pronouns_en_44():
    assert (
D("my").pe(3).ow('s').g('m').realize()   
    ) == 'his',\
    'D("my").pe(3).ow(\'s\').g(\'m\')=>his'


def test_pronouns_en_45():
    assert (
D("my").pe(3).ow('s').g('m').g('f').realize()   
    ) == 'her',\
    'D("my").pe(3).ow(\'s\').g(\'m\').g(\'f\')=>her'


def test_pronouns_en_46():
    assert (
D("my").pe(3).ow('s').g('m').g('f').g('n').realize()   
    ) == 'its',\
    'D("my").pe(3).ow(\'s\').g(\'m\').g(\'f\').g(\'n\')=>its'


def test_pronouns_en_47():
    assert (
D("my").pe(1).ow('p').realize()   
    ) == 'our',\
    'D("my").pe(1).ow(\'p\')=>our'


def test_pronouns_en_48():
    assert (
D("my").pe(3).ow('p').realize()   
    ) == 'their',\
    'D("my").pe(3).ow(\'p\')=>their'

