import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..','src')))

from pyrealb import *
load("en")

def test_dependencies_en_0():
    assert (
root(V("sit").t('ps'),
     subj(N("cat"),
          det(D("the"))),
     comp(P("on"),
          mod(N("couch"),
              det(D("the"))))).realize()   
    ) == 'The cat sat on the couch. ',\
    'Full sentence'


def test_dependencies_en_1():
    assert (
root(N("gift").n('p')).cap(True).realize()   
    ) == 'Gifts. ',\
    'Word with a capital'


def test_dependencies_en_2():
    assert (
root(V("hit").t('p'),
     subj(N("man"),
          det(D("a"))),
     comp(N("ball"),
          det(D("a")))).typ({'pas': True}).realize()   
    ) == 'A ball is hit by a man. ',\
    'Passive sentence'


def test_dependencies_en_3():
    assert (
root(V("play").t('f'),
     subj(N("cat"),
          det(D("a"))),
     comp(N("piano"))).typ({'neg': True}).realize()   
    ) == 'A cat will not play piano. ',\
    'Negative sentence'


def test_dependencies_en_4():
    assert (
root(V("like").t('pr'),
     subj(N("dog").n('p'),
          mod(A("nice"))),
     comp(N("cat"),
          det(D("a"))).n('p')).realize()   
    ) == 'Nice dogs liking cats. ',\
    'Present participle'


def test_dependencies_en_5():
    assert (
root(V("drink"),
     subj(N("boy"),
          det(D("a"))),
     comp(N("water"))).typ({'perf': True}).realize()   
    ) == 'A boy has drunk water. ',\
    'Present perfect'


def test_dependencies_en_6():
    assert (
root(V("drink"),
     comp(N("water")),
     subj(N("boy"),
          det(D("a")))).typ({'int': 'yon'}).realize()   
    ) == 'Does a boy drink water? ',\
    'Yes or no question'


def test_dependencies_en_7():
    assert (
root(V("drink"),
     comp(N("water")),
     subj(N("boy"),
          det(D("a")))).typ({'int': 'wos', 'mod': 'perm'}).realize()   
    ) == 'Who may drink water? ',\
    'Who question with permission'


def test_dependencies_en_8():
    assert (
root(V("drink").t('ps'),
     comp(N("water")),
     subj(N("boy"),
          det(D("a")))).typ({'mod': 'perm'}).realize()   
    ) == 'A boy might drink water. ',\
    'Modality permission'


def test_dependencies_en_9():
    assert (
root(V("speak"),
     coord(C("and"),
           subj(N("seller"),
                det(D("the"))),
           subj(N("customer"),
                det(D("the"))))).realize()   
    ) == 'The seller and the customer speak. ',\
    'Coordination'


def test_dependencies_en_10():
    assert (
root(V("run"),
     comp(N("mile"),
          det(D("a"))),
     subj(N("mouse").n('p'),
          det(D("a")))).realize()   
    ) == 'Mice run a mile. ',\
    'Plural subject, but singular complement'


def test_dependencies_en_11():
    assert (
root(V("eat"),
     comp(N("mouse"),
          det(D("a")),
          mod(A("grey"))),
     subj(N("cat").n('p'),
          det(D("the")))).typ({'pas': True}).realize()   
    ) == 'A grey mouse is eaten by the cats. ',\
    'Subject changes number in passive mode'


def test_dependencies_en_12():
    assert (
root(V("eat").t('f'),
     comp(N("mouse"),
          det(D("a")),
          mod(A("grey"))),
     subj(N("cat").n('p'),
          det(D("the")))).realize()   
    ) == 'The cats will eat a grey mouse. ',\
    'Global change of number'


def test_dependencies_en_13():
    assert (
root(V("eat").t('f'),
     comp(N("mouse"),
          det(D("a")),
          mod(A("grey"))),
     subj(N("cat"),
          det(D("the")))).typ({'int': 'why', 'pas': True, 'neg': True}).realize()   
    ) == 'Why will a grey mouse not be eaten by the cat? ',\
    'Interrogative, passive and negative'


def test_dependencies_en_14():
    assert (
root(V("be"),
     comp(N("case").n('p'),
          det(D("a")),
          mod(A("interesting").tag('i'))),
     coord(C("and"),
           subj(N("apple").tag("a",{'href': 'https:en.wikipedia.org/wiki/Apple'}),
                det(D("a"))),
           subj(N("university"),
                det(D("a"))),
           subj(N("guy"),
                det(D("a")),
                mod(A("humble"))),
           subj(N("mention"),
                det(D("a")),
                mod(A("honourable"))),
           subj(N("exercise"),
                det(D("a"),
                    mod(Q("XML")))))).realize()   
    ) == 'An <a href="https:en.wikipedia.org/wiki/Apple">apple</a>, a university, a humble guy, an honourable mention and an XML exercise are <i>interesting</i> cases. ',\
    'English elision with a coordinated subject'


def test_dependencies_en_15():
    assert (
root(V("play"),
     comp(N("note"),
          det(D("a")),
          mod(A("musical")),
          mod(V("name").t('pp'),
              comp(Q("a").cap(True).tag("a",{'href': 'https:en.wikipedia.org/wiki/A_(musical_note)'})),
              comp(P("on"),
                   mod(N("piano"),
                       det(D("the")))))),
     subj(Pro("I").g('f'))).realize()   
    ) == 'She plays a musical note named <a href="https:en.wikipedia.org/wiki/A_(musical_note)">A</a> on the piano. ',\
    'Elision with a strange a'


def test_dependencies_en_16():
    assert (
root(V("love"),
     comp(N("woman"),
          det(D("a"))).pro(True),
     subj(Pro("I").g('m'))).realize()   
    ) == 'He loves her. ',\
    'Pronominalization of a noun designating a person'


def test_dependencies_en_17():
    assert (
root(V("love"),
     comp(N("woman"),
          det(D("a"))).pro(True),
     subj(Pro("me").g('m'))).typ({'int': 'wos', 'pas': True}).realize()   
    ) == 'Who is loved by him? ',\
    'Interrogative passive'


def test_dependencies_en_18():
    assert (
root(V("play"),
     comp(P("with"),
          mod(N("elephant"),
              det(D("a")))),
     coord(C("and"),
           subj(N("cat"),
                det(D("the")))).add(subj(N("dog"),det(D("the"))))).realize()   
    ) == 'The cat and the dog play with an elephant. ',\
    'Coordination built incrementaly '


def test_dependencies_en_19():
    assert (
root(V("eat")).add(comp(N("apple"),det(D("a")))).add(subj(N("boy"),det(D("a"))).n('p')).realize()   
    ) == 'Boys eat an apple. ',\
    'Adding constituents both before and after'


def test_dependencies_en_20():
    assert (
root(V("see"),
     comp(N("man"),
          det(D("the"))).pro(True),
     comp(P("through"),
          mod(N("window"),
              det(D("the"))).pro(True)),
     subj(N("girl"),
          det(D("the"))).pro(True)).realize()   
    ) == 'She sees him through it. ',\
    'Pronominalization of subject, object and indirect object'

