import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..','src')))

from pyrealb import *
load("en")

def test_elision_en_1():
    assert (
NP(D("a"),
   N("apple")).realize()   
    ) == 'an apple',\
    'elision in an apple'


def test_elision_en_2():
    assert (
CP(C("or"),
   NP(D("a"),
      N("elevator")),
   NP(D("a"),
      N("eucalyptus"))).realize()   
    ) == 'an elevator or a eucalyptus',\
    'elision in an elevator or a eucalyptus'


def test_elision_en_3():
    assert (
CP(C("and"),
   NP(D("a"),
      N("one"),
      N("way")),
   NP(D("a"),
      N("overpass"))).realize()   
    ) == 'a one way and an overpass',\
    'elision in a one way and an overpass'


def test_elision_en_4():
    assert (
S(VP(V("eat"),
     NP(D("a"),
        N("apple").tag("a",{'href': 'https:en.wikipedia.org/wiki/Apple'})))).realize()   
    ) == 'Eats an <a href="https:en.wikipedia.org/wiki/Apple">apple</a>. ',\
    'elision in Eats an <a href="https:en.wikipedia.org/wiki/Apple">apple</a>. '


def test_elision_en_5():
    assert (
NP(NO("123"),
   N("man")).tag('i').tag('p').realize()   
    ) == '<p><i>123 men</i></p>',\
    'elision in <p><i>123 men</i></p>'


def test_elision_en_6():
    assert (
NP(D("a").b('@@').cap(True),
   N("elevator").tag('p')).realize()   
    ) == '@@An <p>elevator</p>',\
    'elision in @@An <p>elevator</p>'


def test_elision_en_7():
    assert (
CP(C("and"),
   NP(D("a"),
      N("unicorn")),
   NP(D("a"),
      A("unusual"),
      N("exercise")),
   NP(D("a"),
      A("honourable"),
      N("mention")),
   NP(D("a"),
      A("humorous"),
      N("guy"))).realize()   
    ) == 'a unicorn, an unusual exercise, an honourable mention and a humorous guy',\
    'elision in a unicorn, an unusual exercise, an honourable mention and a humorous guy'


def test_elision_en_8():
    assert (
S(Pro("this"),
  VP(V("be"),
     NP(D("a"),
        Q("XML"),
        N("exercise"),
        SP(Pro("that"),
           NP(D("a").tag('b'),
              N("educator")).tag('i'),
           VP(V("give")).typ({'mod': 'poss'}))))).realize()   
    ) == 'This is an XML exercise that <i><b>an</b> educator</i> can give. ',\
    'elision in This is an XML exercise that <i><b>an</b> educator</i> can give. '


def test_elision_en_9():
    assert (
S(VP(V("play").t('ip'),
     NP(D("a"),
        A("musical"),
        N("note"),
        V("name").t('pp'),
        Q("A")).tag("a",{'href': 'https:en.wikipedia.org/wiki/A_(musical_note)'}),
     PP(P("on"),
        NP(D("a"),
           N("oboe"))),
     PP(P("for"),
        VP(V("tune").t('pr'),
           NP(D("a"),
              N("orchestra")))))).realize()   
    ) == 'Play <a href="https:en.wikipedia.org/wiki/A_(musical_note)">a musical note named A</a> on an oboe for tuning an orchestra. ',\
    'elision in Play <a href="https:en.wikipedia.org/wiki/A_(musical_note)">a musical note named A</a> on an oboe for tuning an orchestra. '


def test_elision_en_10():
    assert (
Q("&").realize()   
    ) == '&',\
    'elision in &'

