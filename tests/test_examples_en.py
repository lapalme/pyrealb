import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..','src')))

from pyrealb import *
load("en")

apple = NP(D("a"),N("apple"))
appleC = lambda:NP(D("a"),N("apple"))
appleF = lambda:NP(D("a"),N("apple"))

def test_examples_en_1():
    assert (
V("love").realize()   
    ) == 'loves',\
    'Phrase complète:  loves'


def test_examples_en_2():
    assert (
V("have").t('ps').realize()   
    ) == 'had',\
    'Phrase complète:  had'


def test_examples_en_3():
    assert (
V("be").pe(3).realize()   
    ) == 'is',\
    'Phrase complète:  is'


def test_examples_en_4():
    assert (
VP(V("love")).typ({'neg': True}).realize()   
    ) == 'does not love',\
    'Phrase complète:  does not love'


def test_examples_en_5():
    assert (
VP(V("love")).typ({'int': 'yon'}).realize()   
    ) == 'does love? ',\
    'Phrase complète:  does love? '


def test_examples_en_6():
    assert (
VP(V("love")).typ({'prog': True}).realize()   
    ) == 'is loving',\
    'Phrase complète:  is loving'


def test_examples_en_7():
    assert (
VP(V("love")).typ({'mod': 'poss'}).realize()   
    ) == 'can love',\
    'Phrase complète:  can love'


def test_examples_en_8():
    assert (
S(Pro("him").c('nom'),
  VP(V("eat"),
     NP(D("a"),
        N("apple").n('p')).tag('em'))).realize()   
    ) == 'He eats <em>apples</em>. ',\
    'Phrase complète:  He eats <em>apples</em>. '


def test_examples_en_9():
    assert (
S(Pro("him").c('nom'),
  VP(V("eat"),
     NP(D("a"),
        N("apple").n('p')).tag('em'))).t('ps').realize()   
    ) == 'He ate <em>apples</em>. ',\
    'Phrase complète:  He ate <em>apples</em>. '


def test_examples_en_10():
    assert (
S(Pro("him").c('nom'),
  VP(V("eat"),
     NP(D("a"),
        N("apple").n('p')))).typ({'neg': True}).realize()   
    ) == 'He does not eat apples. ',\
    'Phrase complète:  He does not eat apples. '


def test_examples_en_11():
    assert (
S(Pro("him").c('nom').g('m'),
  VP(V("eat"),
     NP(D("a"),
        N("apple").n('p')))).typ({'neg': True, 'pas': True}).realize()   
    ) == 'Apples are not eaten by him. ',\
    'Phrase complète:  Apples are not eaten by him. '


def test_examples_en_12():
    assert (
S(Pro("him").c('nom'),
  VP(V("eat"),
     NP(D("a"),
        N("apple").n('p')).add(A("red")))).add(Adv("now").a(','),0).realize()   
    ) == 'Now, he eats red apples. ',\
    'Phrase complète:  Now, he eats red apples. '


def test_examples_en_13():
    assert (
S(CP(C("and"),
     NP(D("the"),
        N("apple")),
     NP(D("the"),
        N("orange")),
     NP(D("the"),
        N("banana"))),
  VP(V("be"),
     A("good"))).realize()   
    ) == 'The apple, the orange and the banana are good. ',\
    'Phrase complète:  The apple, the orange and the banana are good. '


def test_examples_en_14():
    assert (
S(CP(C("and"),
     NP(D("the"),
        N("apple"))),
  VP(V("be"),
     A("good"))).realize()   
    ) == 'The apple is good. ',\
    'Phrase complète:  The apple is good. '


def test_examples_en_15():
    assert (
S(Pro("him").c('nom'),
  CP(C("and"),
     VP(V("eat"),
        NP(D("a"),
           N("apple"))),
     VP(V("love"),
        NP(D("a"),
           N("apple")).pro(True)))).realize()   
    ) == 'He eats an apple and loves it. ',\
    'Phrase complète:  He eats an apple and loves it. '


def test_examples_en_16():
    assert (
S(NP(D("a"),
     N("apple")).pro(True),
  VP(V("be"),
     A("red"))).realize()   
    ) == 'It is red. ',\
    'Phrase complète:  It is red. '


def test_examples_en_17():
    assert (
S(Pro("him").c('nom'),
  CP(C("and"),
     VP(V("eat"),
        NP(D("a"),
           N("apple"))),
     VP(V("love"),
        NP(D("a"),
           N("apple")).pro(True)))).realize()   
    ) == 'He eats an apple and loves it. ',\
    'Phrase complète:  He eats an apple and loves it. '


def test_examples_en_18():
    assert (
S(NP(D("a"),
     N("apple")),
  VP(V("be"),
     A("red"))).realize()   
    ) == 'An apple is red. ',\
    'Phrase complète:  An apple is red. '


def test_examples_en_19():
    assert (
S(Pro("him").c('nom'),
  CP(C("and"),
     VP(V("eat"),
        NP(D("a"),
           N("apple"))),
     VP(V("love"),
        NP(D("a"),
           N("apple")).pro(True)))).realize()   
    ) == 'He eats an apple and loves it. ',\
    'Phrase complète:  He eats an apple and loves it. '


def test_examples_en_20():
    assert (
S(NP(D("a"),
     N("apple")),
  VP(V("be"),
     A("red"))).realize()   
    ) == 'An apple is red. ',\
    'Phrase complète:  An apple is red. '


def test_examples_en_21():
    assert (
S(Pro("him").c('nom'),
  VP(V("eat"),
     NP(D("a"),
        N("apple").tag("a",{'href': 'https:#en.wikipedia.org/wiki/Apple'})))).realize()   
    ) == 'He eats an <a href="https:#en.wikipedia.org/wiki/Apple">apple</a>. ',\
    'Phrase complète:  He eats an <a href="https:#en.wikipedia.org/wiki/Apple">apple</a>. '


def test_examples_en_22():
    assert (
NP(NO("1").dOpt({'nat': True}),
   N("plane")).realize()   
    ) == 'one plane',\
    'Phrase complète:  one plane'


def test_examples_en_23():
    assert (
NP(NO("3").dOpt({'nat': True}),
   N("plane")).realize()   
    ) == 'three planes',\
    'Phrase complète:  three planes'


def test_examples_en_24():
    assert (
SP(SP(D("the"),
      A("large").f('su'),
      NP(P("of"),
         D("the"),
         N("trainer").n('p')).a(',')),
   D("this").n('s'),
   N("addition").n('s')).realize()   
    ) == 'the largest of the trainers, this addition',\
    'Phrase complète:  the largest of the trainers, this addition'


def test_examples_en_25():
    assert (
root(V("love")).cap(False).realize()   
    ) == 'loves',\
    'Phrase complète:  loves'


def test_examples_en_26():
    assert (
root(V("have").t('ps')).cap(False).realize()   
    ) == 'had',\
    'Phrase complète:  had'


def test_examples_en_27():
    assert (
root(V("be").pe(3)).cap(False).realize()   
    ) == 'is',\
    'Phrase complète:  is'


def test_examples_en_28():
    assert (
root(V("love")).typ({'neg': True}).cap(False).realize()   
    ) == 'does not love',\
    'Phrase complète:  does not love'


def test_examples_en_29():
    assert (
root(V("love")).typ({'int': 'yon'}).cap(False).realize()   
    ) == 'does love? ',\
    'Phrase complète:  does love? '


def test_examples_en_30():
    assert (
root(V("love")).typ({'prog': True}).cap(False).realize()   
    ) == 'is loving',\
    'Phrase complète:  is loving'


def test_examples_en_31():
    assert (
root(V("love")).typ({'mod': 'poss'}).cap(False).realize()   
    ) == 'can love',\
    'Phrase complète:  can love'


def test_examples_en_32():
    assert (
root(V("eat"),
     comp(N("apple").n('p'),
          det(D("a"))).tag('em'),
     subj(Pro("him").c('nom'))).realize()   
    ) == 'He eats <em>apples</em>. ',\
    'Phrase complète:  He eats <em>apples</em>. '


def test_examples_en_33():
    assert (
root(V("eat"),
     comp(N("apple").n('p'),
          det(D("a"))).tag('em'),
     subj(Pro("him").c('nom'))).t('ps').realize()   
    ) == 'He ate <em>apples</em>. ',\
    'Phrase complète:  He ate <em>apples</em>. '


def test_examples_en_34():
    assert (
root(V("eat"),
     comp(N("apple").n('p'),
          det(D("a"))),
     subj(Pro("him").c('nom'))).typ({'neg': True}).realize()   
    ) == 'He does not eat apples. ',\
    'Phrase complète:  He does not eat apples. '


def test_examples_en_35():
    assert (
root(V("eat"),
     comp(N("apple").n('p'),
          det(D("a"))),
     subj(Pro("him").c('nom').g('m'))).typ({'neg': True, 'pas': True}).realize()   
    ) == 'Apples are not eaten by him. ',\
    'Phrase complète:  Apples are not eaten by him. '


def test_examples_en_36():
    assert (
root(V("eat"),
     comp(N("apple").n('p'),
          det(D("a")),
          mod(A("red"))),
     mod(Adv("now").a(',')).pos('pre'),
     subj(Pro("him").c('nom'))).realize()   
    ) == 'Now, he eats red apples. ',\
    'Phrase complète:  Now, he eats red apples. '


def test_examples_en_37():
    assert (
root(V("be"),
     comp(A("good")),
     coord(C("and"),
           subj(N("apple"),
                det(D("the"))),
           subj(N("orange"),
                det(D("the"))),
           subj(N("banana"),
                det(D("the"))))).realize()   
    ) == 'The apple, the orange and the banana are good. ',\
    'Phrase complète:  The apple, the orange and the banana are good. '


def test_examples_en_38():
    assert (
root(V("be"),
     comp(A("good")),
     coord(C("and"),
           subj(N("apple"),
                det(D("the"))))).realize()   
    ) == 'The apple is good. ',\
    'Phrase complète:  The apple is good. '


def test_examples_en_39():
    assert (
S(Pro("him").c('nom'),
  CP(C("and"),
     VP(V("eat"),
        NP(D("a"),
           N("apple"))),
     VP(V("love"),
        NP(D("a"),
           N("apple")).pro(True)))).realize()   
    ) == 'He eats an apple and loves it. ',\
    'Phrase complète:  He eats an apple and loves it. '


def test_examples_en_40():
    assert (
root(V("be"),
     comp(A("red")),
     subj(N("apple"),
          det(D("a"))).pro(True)).realize()   
    ) == 'It is red. ',\
    'Phrase complète:  It is red. '


def test_examples_en_41():
    assert (
S(Pro("him").c('nom'),
  CP(C("and"),
     VP(V("eat"),
        NP(D("a"),
           N("apple"))),
     VP(V("love"),
        NP(D("a"),
           N("apple")).pro(True)))).realize()   
    ) == 'He eats an apple and loves it. ',\
    'Phrase complète:  He eats an apple and loves it. '


def test_examples_en_42():
    assert (
root(V("be"),
     comp(A("red")),
     subj(N("apple"),
          det(D("a")))).realize()   
    ) == 'An apple is red. ',\
    'Phrase complète:  An apple is red. '


def test_examples_en_43():
    assert (
S(Pro("him").c('nom'),
  CP(C("and"),
     VP(V("eat"),
        NP(D("a"),
           N("apple"))),
     VP(V("love"),
        NP(D("a"),
           N("apple")).pro(True)))).realize()   
    ) == 'He eats an apple and loves it. ',\
    'Phrase complète:  He eats an apple and loves it. '


def test_examples_en_44():
    assert (
root(V("be"),
     comp(A("red")),
     subj(N("apple"),
          det(D("a")))).realize()   
    ) == 'An apple is red. ',\
    'Phrase complète:  An apple is red. '


def test_examples_en_45():
    assert (
root(V("eat"),
     comp(N("apple").tag("a",{'href': 'https:#en.wikipedia.org/wiki/Apple'}),
          det(D("a"))),
     subj(Pro("him").c('nom'))).realize()   
    ) == 'He eats an <a href="https:#en.wikipedia.org/wiki/Apple">apple</a>. ',\
    'Phrase complète:  He eats an <a href="https:#en.wikipedia.org/wiki/Apple">apple</a>. '


def test_examples_en_46():
    assert (
root(N("plane"),
     det(NO("1").dOpt({'nat': True}))).cap(False).realize()   
    ) == 'one plane',\
    'Phrase complète:  one plane'


def test_examples_en_47():
    assert (
root(N("plane"),
     det(NO("3").dOpt({'nat': True}))).cap(False).realize()   
    ) == 'three planes',\
    'Phrase complète:  three planes'


def test_examples_en_48():
    assert (
SP(SP(D("the"),
      A("large").f('su'),
      NP(P("of"),
         D("the"),
         N("trainer").n('p')).a(',')),
   D("this").n('s'),
   N("addition").n('s')).realize()   
    ) == 'the largest of the trainers, this addition',\
    'Phrase complète:  the largest of the trainers, this addition'

