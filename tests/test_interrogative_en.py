import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..','src')))

from pyrealb import *
load("en")

def test_interrogative_en_1():
    assert (
S(NP(D("the"),
     N("cat")),
  VP(V("eat"),
     NP(D("the"),
        N("mouse")))).realize()   
    ) == 'The cat eats the mouse. ',\
    'Simple sentence, no option'


def test_interrogative_en_2():
    assert (
S(NP(D("the"),
     N("cat")),
  VP(V("eat"),
     NP(D("the"),
        N("mouse")))).typ({'int': 'yon'}).realize()   
    ) == 'Does the cat eat the mouse? ',\
    'Interrogative sentence'


def test_interrogative_en_3():
    assert (
S(NP(D("the"),
     N("cat")),
  VP(V("eat"),
     NP(D("the"),
        N("mouse")))).typ({'int': 'wos'}).realize()   
    ) == 'Who eats the mouse? ',\
    'Interrogative sentence (subject-who)'


def test_interrogative_en_4():
    assert (
S(NP(D("the"),
     N("cat")),
  VP(V("eat"),
     NP(D("the"),
        N("mouse")))).typ({'int': 'wod'}).realize()   
    ) == 'Who does the cat eat? ',\
    'Interrogative sentence (direct object-who)'


def test_interrogative_en_5():
    assert (
S(NP(D("the"),
     N("cat")),
  VP(V("eat"),
     NP(D("the"),
        N("mouse")))).typ({'int': 'wad'}).realize()   
    ) == 'What does the cat eat? ',\
    'Interrogative sentence (direct object-what)'


def test_interrogative_en_6():
    assert (
S(NP(D("the"),
     N("cat")),
  VP(V("eat"),
     NP(D("the"),
        N("mouse")),
     PP(P("to"),
        NP(D("my"),
           N("family"))))).typ({'int': 'woi'}).realize()   
    ) == 'To whom does the cat eat the mouse? ',\
    'Interrogative sentence (indirect object-who)'


def test_interrogative_en_7():
    assert (
S(NP(D("the"),
     N("cat")),
  VP(V("eat"),
     NP(D("the"),
        N("mouse")))).typ({'int': 'whe'}).realize()   
    ) == 'Where does the cat eat the mouse? ',\
    'Interrogative sentence (where)'


def test_interrogative_en_8():
    assert (
S(NP(D("the"),
     N("cat")),
  VP(V("eat"),
     NP(D("the"),
        N("mouse")))).typ({'int': 'how'}).realize()   
    ) == 'How does the cat eat the mouse? ',\
    'Interrogative sentence (how)'


def test_interrogative_en_9():
    assert (
S(NP(D("the"),
     N("cat")),
  VP(V("eat").t('ps'),
     NP(D("the"),
        N("mouse")))).typ({'int': 'yon'}).realize()   
    ) == 'Did the cat eat the mouse? ',\
    'Interrogative sentence(past)'


def test_interrogative_en_10():
    assert (
S(NP(D("the"),
     N("cat")),
  VP(V("eat").t('f'),
     NP(D("the"),
        N("mouse")))).typ({'int': 'yon'}).realize()   
    ) == 'Will the cat eat the mouse? ',\
    'Interrogative sentence(future)'


def test_interrogative_en_11():
    assert (
S(NP(D("the"),
     N("cat")),
  VP(V("eat").t('f'),
     NP(D("the"),
        N("mouse")))).typ({'int': 'wad'}).realize()   
    ) == 'What will the cat eat? ',\
    'Interrogative sentence(wad,future)'


def test_interrogative_en_12():
    assert (
S(NP(D("the"),
     N("cat")),
  VP(V("eat").t('f'),
     NP(D("the"),
        N("mouse")))).typ({'int': 'wos'}).realize()   
    ) == 'Who will eat the mouse? ',\
    'Interrogative sentence (subject-who)'


def test_interrogative_en_13():
    assert (
S(NP(D("the"),
     N("cat")),
  VP(V("eat").t('f'),
     NP(D("the"),
        N("mouse")))).typ({'int': 'wod'}).realize()   
    ) == 'Who will the cat eat? ',\
    'Interrogative sentence (direct object-who)'


def test_interrogative_en_14():
    assert (
S(NP(D("the"),
     N("cat")),
  VP(V("eat").t('f'),
     NP(D("the"),
        N("mouse")))).typ({'int': 'whe'}).realize()   
    ) == 'Where will the cat eat the mouse? ',\
    'Interrogative sentence(whe,future)'


def test_interrogative_en_15():
    assert (
S(NP(D("the"),
     N("cat")),
  VP(V("eat").t('f'),
     NP(D("the"),
        N("mouse")))).typ({'int': 'how'}).realize()   
    ) == 'How will the cat eat the mouse? ',\
    'Interrogative sentence (how)'


def test_interrogative_en_16():
    assert (
S(NP(D("the"),
     N("cat")),
  VP(V("eat").t('ps'),
     NP(D("the"),
        N("mouse")))).typ({'perf': True, 'int': 'yon'}).realize()   
    ) == 'Had the cat eaten the mouse? ',\
    'Interrogative/Perfect sentence(past)'


def test_interrogative_en_17():
    assert (
S(NP(D("the"),
     N("cat")),
  VP(V("eat").t('f'),
     NP(D("the"),
        N("mouse")))).typ({'perf': True, 'int': 'yon'}).realize()   
    ) == 'Will the cat have eaten the mouse? ',\
    'Interrogative/Perfect sentence(future)'


def test_interrogative_en_18():
    assert (
S(NP(D("the"),
     N("cat")),
  VP(V("eat").t('ps'),
     NP(D("the"),
        N("mouse")))).typ({'perf': True, 'int': 'wad'}).realize()   
    ) == 'What had the cat eaten? ',\
    'Interrogative/Perfect sentence(wad,past)'


def test_interrogative_en_19():
    assert (
S(NP(D("the"),
     N("cat")),
  VP(V("eat").t('f'),
     NP(D("the"),
        N("mouse")))).typ({'perf': True, 'int': 'wad'}).realize()   
    ) == 'What will the cat have eaten? ',\
    'Interrogative/Perfect sentence(wad,future)'


def test_interrogative_en_20():
    assert (
S(NP(D("the"),
     N("cat")),
  VP(V("eat").t('ps'),
     NP(D("the"),
        N("mouse")))).typ({'perf': True, 'int': 'wos'}).realize()   
    ) == 'Who had eaten the mouse? ',\
    'Interrogative/Perfect sentence (wos,past)'


def test_interrogative_en_21():
    assert (
S(NP(D("the"),
     N("cat")),
  VP(V("eat").t('f'),
     NP(D("the"),
        N("mouse")))).typ({'perf': True, 'int': 'wos'}).realize()   
    ) == 'Who will have eaten the mouse? ',\
    'Interrogative/Perfect sentence (wos, future)'


def test_interrogative_en_22():
    assert (
S(NP(D("the"),
     N("cat")),
  VP(V("eat").t('ps'),
     NP(D("the"),
        N("mouse")))).typ({'perf': True, 'int': 'wod'}).realize()   
    ) == 'Who had the cat eaten? ',\
    'Interrogative/Perfect sentence (wod, past)'


def test_interrogative_en_23():
    assert (
S(NP(D("the"),
     N("cat")),
  VP(V("eat").t('f'),
     NP(D("the"),
        N("mouse")))).typ({'perf': True, 'int': 'wod'}).realize()   
    ) == 'Who will the cat have eaten? ',\
    'Interrogative/Perfect sentence (wod, future)'


def test_interrogative_en_24():
    assert (
S(NP(D("the"),
     N("cat")),
  VP(V("eat").t('ps'),
     NP(D("the"),
        N("mouse")))).typ({'perf': True, 'int': 'whe'}).realize()   
    ) == 'Where had the cat eaten the mouse? ',\
    'Interrogative/Perfect sentence(whe,past)'


def test_interrogative_en_25():
    assert (
S(NP(D("the"),
     N("cat")),
  VP(V("eat").t('f'),
     NP(D("the"),
        N("mouse")))).typ({'perf': True, 'int': 'whe'}).realize()   
    ) == 'Where will the cat have eaten the mouse? ',\
    'Interrogative/Perfect sentence(whe,future)'


def test_interrogative_en_26():
    assert (
S(NP(D("the"),
     N("cat")),
  VP(V("eat").t('ps'),
     NP(D("the"),
        N("mouse")))).typ({'perf': True, 'int': 'how'}).realize()   
    ) == 'How had the cat eaten the mouse? ',\
    'Interrogative/Perfect sentence (how, past)'


def test_interrogative_en_27():
    assert (
S(NP(D("the"),
     N("cat")),
  VP(V("eat").t('f'),
     NP(D("the"),
        N("mouse")))).typ({'perf': True, 'int': 'how'}).realize()   
    ) == 'How will the cat have eaten the mouse? ',\
    'Interrogative/Perfect sentence (how, future)'


def test_interrogative_en_28():
    assert (
S(NP(D("the"),
     N("cat")),
  VP(V("eat").t('ps'),
     NP(D("the"),
        N("mouse")))).typ({'int': 'yon', 'neg': True}).realize()   
    ) == 'Did the cat not eat the mouse? ',\
    'Interrogative/Negative sentence(past)'


def test_interrogative_en_29():
    assert (
S(NP(D("the"),
     N("cat")),
  VP(V("eat").t('f'),
     NP(D("the"),
        N("mouse")))).typ({'int': 'yon', 'neg': True}).realize()   
    ) == 'Will the cat not eat the mouse? ',\
    'Interrogative/Negative sentence(future)'


def test_interrogative_en_30():
    assert (
S(NP(D("the"),
     N("cat")),
  VP(V("eat").t('ps'),
     NP(D("the"),
        N("mouse")))).typ({'int': 'wad', 'neg': True}).realize()   
    ) == 'What did the cat not eat? ',\
    'Interrogative/Negative sentence(wad,past)'


def test_interrogative_en_31():
    assert (
S(NP(D("the"),
     N("cat")),
  VP(V("eat").t('f'),
     NP(D("the"),
        N("mouse")))).typ({'int': 'wad', 'neg': True}).realize()   
    ) == 'What will the cat not eat? ',\
    'Interrogative/Negative sentence(wad,future)'


def test_interrogative_en_32():
    assert (
S(NP(D("the"),
     N("cat")),
  VP(V("eat").t('ps'),
     NP(D("the"),
        N("mouse")))).typ({'int': 'wos', 'neg': True}).realize()   
    ) == 'Who did not eat the mouse? ',\
    'Interrogative/Negative sentence (wos,past)'


def test_interrogative_en_33():
    assert (
S(NP(D("the"),
     N("cat")),
  VP(V("eat").t('f'),
     NP(D("the"),
        N("mouse")))).typ({'int': 'wos', 'neg': True}).realize()   
    ) == 'Who will not eat the mouse? ',\
    'Interrogative/Negative sentence (wos, future)'


def test_interrogative_en_34():
    assert (
S(NP(D("the"),
     N("cat")),
  VP(V("eat").t('ps'),
     NP(D("the"),
        N("mouse")))).typ({'int': 'wod', 'neg': True}).realize()   
    ) == 'Who did the cat not eat? ',\
    'Interrogative/Negative sentence (wod, past)'


def test_interrogative_en_35():
    assert (
S(NP(D("the"),
     N("cat")),
  VP(V("eat").t('f'),
     NP(D("the"),
        N("mouse")))).typ({'int': 'wod', 'neg': True}).realize()   
    ) == 'Who will the cat not eat? ',\
    'Interrogative/Negative sentence (wod, future)'


def test_interrogative_en_36():
    assert (
S(NP(D("the"),
     N("cat")),
  VP(V("eat").t('ps'),
     NP(D("the"),
        N("mouse")))).typ({'int': 'whe', 'neg': True}).realize()   
    ) == 'Where did the cat not eat the mouse? ',\
    'Interrogative/Negative sentence(whe,past)'


def test_interrogative_en_37():
    assert (
S(NP(D("the"),
     N("cat")),
  VP(V("eat").t('f'),
     NP(D("the"),
        N("mouse")))).typ({'int': 'whe', 'neg': True}).realize()   
    ) == 'Where will the cat not eat the mouse? ',\
    'Interrogative/Negative sentence(whe,future)'


def test_interrogative_en_38():
    assert (
S(NP(D("the"),
     N("cat")),
  VP(V("eat").t('ps'),
     NP(D("the"),
        N("mouse")))).typ({'int': 'how', 'neg': True}).realize()   
    ) == 'How did the cat not eat the mouse? ',\
    'Interrogative/Negative sentence (how, past)'


def test_interrogative_en_39():
    assert (
S(NP(D("the"),
     N("cat")),
  VP(V("eat").t('f'),
     NP(D("the"),
        N("mouse")))).typ({'int': 'how', 'neg': True}).realize()   
    ) == 'How will the cat not eat the mouse? ',\
    'Interrogative/Negative sentence (how, future)'


def test_interrogative_en_40():
    assert (
S(NP(D("the"),
     N("cat")),
  VP(V("eat").t('ps'),
     NP(D("the"),
        N("mouse")))).typ({'perf': True, 'int': 'yon', 'neg': True}).realize()   
    ) == 'Had the cat not eaten the mouse? ',\
    'Interrogative/Negative/Perfect sentence(past)'


def test_interrogative_en_41():
    assert (
S(NP(D("the"),
     N("cat")),
  VP(V("eat").t('f'),
     NP(D("the"),
        N("mouse")))).typ({'perf': True, 'int': 'yon', 'neg': True}).realize()   
    ) == 'Will the cat not have eaten the mouse? ',\
    'Interrogative/Negative/Perfect sentence(future)'


def test_interrogative_en_42():
    assert (
S(NP(D("the"),
     N("cat")),
  VP(V("eat").t('ps'),
     NP(D("the"),
        N("mouse")))).typ({'perf': True, 'int': 'wad', 'neg': True}).realize()   
    ) == 'What had the cat not eaten? ',\
    'Interrogative/Negative/Perfect sentence(wad,past)'


def test_interrogative_en_43():
    assert (
S(NP(D("the"),
     N("cat")),
  VP(V("eat").t('f'),
     NP(D("the"),
        N("mouse")))).typ({'perf': True, 'int': 'wad', 'neg': True}).realize()   
    ) == 'What will the cat not have eaten? ',\
    'Interrogative/Negative/Perfect sentence (wad, future)'


def test_interrogative_en_44():
    assert (
S(NP(D("the"),
     N("cat")),
  VP(V("eat").t('ps'),
     NP(D("the"),
        N("mouse")))).typ({'perf': True, 'int': 'whe', 'neg': True}).realize()   
    ) == 'Where had the cat not eaten the mouse? ',\
    'Interrogative/Negative/Perfect sentence(whe,past)'


def test_interrogative_en_45():
    assert (
S(NP(D("the"),
     N("cat")),
  VP(V("eat").t('f'),
     NP(D("the"),
        N("mouse")))).typ({'perf': True, 'int': 'whe', 'neg': True}).realize()   
    ) == 'Where will the cat not have eaten the mouse? ',\
    'Interrogative/Negative/Perfect sentence(whe,future)'


def test_interrogative_en_46():
    assert (
S(NP(D("the"),
     N("cat")),
  VP(V("eat").t('ps'),
     NP(D("the"),
        N("mouse")))).typ({'int': 'yon', 'prog': True}).realize()   
    ) == 'Was the cat eating the mouse? ',\
    'Interrogative/Negative/Perfect sentence(past)'


def test_interrogative_en_47():
    assert (
S(NP(D("the"),
     N("cat")),
  VP(V("eat").t('f'),
     NP(D("the"),
        N("mouse")))).typ({'int': 'yon', 'prog': True}).realize()   
    ) == 'Will the cat be eating the mouse? ',\
    'Interrogative/Negative/Perfect sentence(future)'


def test_interrogative_en_48():
    assert (
S(NP(D("the"),
     N("cat")),
  VP(V("eat").t('ps'),
     NP(D("the"),
        N("mouse")))).typ({'int': 'wad', 'prog': True}).realize()   
    ) == 'What was the cat eating? ',\
    'Interrogative/Negative/Perfect sentence(wad,past)'


def test_interrogative_en_49():
    assert (
S(NP(D("the"),
     N("cat")),
  VP(V("eat").t('f'),
     NP(D("the"),
        N("mouse")))).typ({'int': 'wad', 'prog': True}).realize()   
    ) == 'What will the cat be eating? ',\
    'Interrogative/Negative/Perfect sentence (wad, future)'


def test_interrogative_en_50():
    assert (
S(NP(D("the"),
     N("cat")),
  VP(V("eat").t('ps'),
     NP(D("the"),
        N("mouse")))).typ({'int': 'whe', 'prog': True}).realize()   
    ) == 'Where was the cat eating the mouse? ',\
    'Interrogative/Negative/Perfect sentence(whe,past)'


def test_interrogative_en_51():
    assert (
S(NP(D("the"),
     N("cat")),
  VP(V("eat").t('f'),
     NP(D("the"),
        N("mouse")))).typ({'int': 'whe', 'prog': True}).realize()   
    ) == 'Where will the cat be eating the mouse? ',\
    'Interrogative/Negative/Perfect sentence(whe,future)'


def test_interrogative_en_52():
    assert (
S(NP(D("the"),
     N("cat")),
  VP(V("eat").t('ps'),
     NP(D("the"),
        N("mouse")))).typ({'int': 'yon', 'neg': True, 'prog': True}).realize()   
    ) == 'Was the cat not eating the mouse? ',\
    'Interrogative/Negative/Perfect sentence(past)'


def test_interrogative_en_53():
    assert (
S(NP(D("the"),
     N("cat")),
  VP(V("eat").t('f'),
     NP(D("the"),
        N("mouse")))).typ({'int': 'yon', 'neg': True, 'prog': True}).realize()   
    ) == 'Will the cat not be eating the mouse? ',\
    'Interrogative/Negative/Perfect sentence(future)'


def test_interrogative_en_54():
    assert (
S(NP(D("the"),
     N("cat")),
  VP(V("eat").t('ps'),
     NP(D("the"),
        N("mouse")))).typ({'int': 'wad', 'neg': True, 'prog': True}).realize()   
    ) == 'What was the cat not eating? ',\
    'Interrogative/Negative/Perfect sentence(wad,past)'


def test_interrogative_en_55():
    assert (
S(NP(D("the"),
     N("cat")),
  VP(V("eat").t('f'),
     NP(D("the"),
        N("mouse")))).typ({'int': 'wad', 'neg': True, 'prog': True}).realize()   
    ) == 'What will the cat not be eating? ',\
    'Interrogative/Negative/Perfect sentence (wad, future)'


def test_interrogative_en_56():
    assert (
S(NP(D("the"),
     N("cat")),
  VP(V("eat").t('ps'),
     NP(D("the"),
        N("mouse")))).typ({'int': 'whe', 'neg': True, 'prog': True}).realize()   
    ) == 'Where was the cat not eating the mouse? ',\
    'Interrogative/Negative/Perfect sentence(whe,past)'


def test_interrogative_en_57():
    assert (
S(NP(D("the"),
     N("cat")),
  VP(V("eat").t('f'),
     NP(D("the"),
        N("mouse")))).typ({'int': 'whe', 'neg': True, 'prog': True}).realize()   
    ) == 'Where will the cat not be eating the mouse? ',\
    'Interrogative/Negative/Perfect sentence(whe,future)'


def test_interrogative_en_58():
    assert (
S(NP(D("the"),
     N("cat")),
  VP(V("eat").t('ps'),
     NP(D("the"),
        N("mouse")))).typ({'int': 'yon', 'neg': True, 'prog': True, 'perf': True}).realize()   
    ) == 'Had the cat not been eating the mouse? ',\
    'Interrogative/Negative/Perfect sentence(past)'


def test_interrogative_en_59():
    assert (
S(NP(D("the"),
     N("cat")),
  VP(V("eat").t('f'),
     NP(D("the"),
        N("mouse")))).typ({'int': 'yon', 'neg': True, 'prog': True, 'perf': True}).realize()   
    ) == 'Will the cat not have been eating the mouse? ',\
    'Interrogative/Negative/Perfect sentence(future)'


def test_interrogative_en_60():
    assert (
S(NP(D("the"),
     N("cat")),
  VP(V("eat").t('ps'),
     NP(D("the"),
        N("mouse")))).typ({'int': 'yon', 'pas': True}).realize()   
    ) == 'Was the mouse eaten by the cat? ',\
    'Interrogative/Negative/Perfect sentence(past)'


def test_interrogative_en_61():
    assert (
S(NP(D("the"),
     N("cat")),
  VP(V("eat").t('f'),
     NP(D("the"),
        N("mouse")))).typ({'int': 'yon', 'pas': True}).realize()   
    ) == 'Will the mouse be eaten by the cat? ',\
    'Interrogative/Negative/Perfect sentence(future)'


def test_interrogative_en_62():
    assert (
S(NP(D("the"),
     N("cat")),
  VP(V("like"),
     NP(D("the"),
        N("girl")))).typ({'int': 'tag', 'pas': False}).realize()   
    ) == "The cat likes the girl, doesn't it? ",\
    'tag question, affirmative'


def test_interrogative_en_63():
    assert (
S(NP(D("the"),
     N("cat")),
  VP(V("like"),
     NP(D("the"),
        N("girl")))).typ({'int': 'tag', 'pas': True}).realize()   
    ) == "The girl is liked by the cat, isn't she? ",\
    'tag question,passive '


def test_interrogative_en_64():
    assert (
S(NP(D("the"),
     N("cat")),
  VP(V("like").t('f'),
     NP(D("the"),
        N("girl")))).typ({'int': 'tag', 'pas': False}).realize()   
    ) == "The cat will like the girl, won't it? ",\
    'tag question, affirmative future'


def test_interrogative_en_65():
    assert (
S(NP(D("the"),
     N("cat")),
  VP(V("like").t('f'),
     NP(D("the"),
        N("girl")))).typ({'int': 'tag', 'pas': True}).realize()   
    ) == "The girl will be liked by the cat, won't she? ",\
    'tag question, passive, future'

