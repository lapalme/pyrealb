import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..','src')))

from pyrealb import *
load("en")

def test_sentences_en_1():
    assert (
S(NP(D("the"),
     N("cat")),
  VP(V("sit").t('ps'),
     PP(P("on"),
        NP(D("the"),
           N("couch"))))).realize()   
    ) == 'The cat sat on the couch. ',\
    'Full sentence'


def test_sentences_en_2():
    assert (
S(N("gift").n('p')).cap(True).realize()   
    ) == 'Gifts. ',\
    'Word with a capital'


def test_sentences_en_3():
    assert (
S(NP(D("a"),
     N("man")),
  VP(V("hit").t('p'),
     NP(D("a"),
        N("ball")))).typ({'pas': True}).realize()   
    ) == 'A ball is hit by a man. ',\
    'Passive sentence'


def test_sentences_en_4():
    assert (
S(NP(D("a"),
     N("cat")),
  VP(V("play").t('f'),
     NP(N("piano")))).typ({'neg': True}).realize()   
    ) == 'A cat will not play piano. ',\
    'Negative sentence'


def test_sentences_en_5():
    assert (
S(NP(A("nice"),
     N("dog").n('p')),
  VP(V("like").t('pr'),
     NP(D("a"),
        N("cat").n('p')))).realize()   
    ) == 'Nice dogs liking cats. ',\
    'Present participle'


def test_sentences_en_6():
    assert (
S(NP(D("a"),
     N("boy")),
  VP(V("drink"),
     NP(N("water")))).typ({'perf': True}).realize()   
    ) == 'A boy has drunk water. ',\
    'Present perfect'


def test_sentences_en_7():
    assert (
S(NP(D("a"),
     N("boy")),
  VP(V("drink"),
     NP(N("water")))).typ({'int': 'yon'}).realize()   
    ) == 'Does a boy drink water? ',\
    'Yes or no question'


def test_sentences_en_8():
    assert (
S(NP(D("a"),
     N("boy")),
  VP(V("drink"),
     NP(N("water")))).typ({'int': 'wos', 'mod': 'perm'}).realize()   
    ) == 'Who may drink water? ',\
    'Who question with permission'


def test_sentences_en_9():
    assert (
S(NP(D("a"),
     N("boy")),
  VP(V("drink").t('ps'),
     NP(N("water")))).typ({'mod': 'perm'}).realize()   
    ) == 'A boy might drink water. ',\
    'Modality permission'


def test_sentences_en_10():
    assert (
S(CP(C("and"),
     NP(D("the"),
        N("seller")),
     NP(D("the"),
        N("customer"))),
  VP(V("speak"))).realize()   
    ) == 'The seller and the customer speak. ',\
    'Coordination'


def test_sentences_en_11():
    assert (
S(NP(D("a"),
     N("mouse").n('p')),
  VP(V("run"),
     NP(D("a"),
        N("mile")))).realize()   
    ) == 'Mice run a mile. ',\
    'Plural subject, but singular complement'


def test_sentences_en_12():
    assert (
S(NP(D("the"),
     N("cat").n('p')),
  VP(V("eat"),
     NP(D("a"),
        A("grey"),
        N("mouse")))).typ({'pas': True}).realize()   
    ) == 'A grey mouse is eaten by the cats. ',\
    'Subject changes number in passive mode'


def test_sentences_en_13():
    assert (
S(NP(D("the"),
     N("cat").n('p')),
  VP(V("eat").t('f'),
     NP(D("a"),
        A("grey"),
        N("mouse")))).realize()   
    ) == 'The cats will eat a grey mouse. ',\
    'Global change of number'


def test_sentences_en_14():
    assert (
S(NP(D("the"),
     N("cat")),
  VP(V("eat").t('f'),
     NP(D("a"),
        A("grey"),
        N("mouse")))).typ({'int': 'why', 'pas': True, 'neg': True}).realize()   
    ) == 'Why will a grey mouse not be eaten by the cat? ',\
    'Interrogative, passive and negative'


def test_sentences_en_15():
    assert (
S(CP(C("and"),
     NP(D("a"),
        N("apple").tag("a",{'href': 'https:en.wikipedia.org/wiki/Apple'})),
     NP(D("a"),
        N("university")),
     NP(D("a"),
        A("humble"),
        N("guy")),
     NP(D("a"),
        A("honourable"),
        N("mention")),
     NP(D("a"),
        Q("XML"),
        N("exercise"))),
  VP(V("be"),
     NP(D("a"),
        A("interesting").tag('i'),
        N("case").n('p')))).realize()   
    ) == 'An <a href="https:en.wikipedia.org/wiki/Apple">apple</a>, a university, a humble guy, an honourable mention and an XML exercise are <i>interesting</i> cases. ',\
    'English elision with a coordinated subject'


def test_sentences_en_16():
    assert (
S(Pro("I").g('f'),
  VP(V("play"),
     NP(D("a"),
        A("musical"),
        N("note"),
        VP(V("name").t('pp'),
           Q("a").cap(True).tag("a",{'href': 'https:en.wikipedia.org/wiki/A_(musical_note)'}),
           PP(P("on"),
              NP(D("the"),
                 N("piano"))))))).realize()   
    ) == 'She plays a musical note named <a href="https:en.wikipedia.org/wiki/A_(musical_note)">A</a> on the piano. ',\
    'Elision with a strange a'


def test_sentences_en_17():
    assert (
S(Pro("I").g('m'),
  VP(V("love"),
     NP(D("a"),
        N("woman")).pro(True))).realize()   
    ) == 'He loves her. ',\
    'Pronominalization of a noun designating a person'


def test_sentences_en_18():
    assert (
S(Pro("me").g('m'),
  VP(V("love"),
     NP(D("a"),
        N("woman")).pro(True))).typ({'int': 'wos', 'pas': True}).realize()   
    ) == 'Who is loved by him? ',\
    'Interrogative passive'


def test_sentences_en_19():
    assert (
S(CP(C("and"),
     NP(D("the"),
        N("cat"))).add(NP(D("the"),N("dog"))),
  VP(V("play"),
     PP(P("with"),
        NP(D("a"),
           N("elephant"))))).realize()   
    ) == 'The cat and the dog play with an elephant. ',\
    'Coordination built incrementaly '


def test_sentences_en_20():
    assert (
S(VP().add(V("eat")).add(NP(D("the"),N("apple")))).add(NP(D("a"),N("boy").n('p')),0).realize()   
    ) == 'Boys eat the apple. ',\
    'Adding constituents both before and after'


def test_sentences_en_21():
    assert (
S(NP(D("the"),
     N("girl")).pro(True),
  VP(V("see"),
     NP(D("the"),
        N("man")).pro(True),
     PP(P("through"),
        NP(D("the"),
           N("window")).pro(True)))).realize()   
    ) == 'She sees him through it. ',\
    'Pronominalization of subject, object and indirect object'


def test_sentences_en_22():
    assert (
S(Pro("him").c('nom'),
  VP(V("eat"),
     NP(D("a"),
        N("apple").n('p')).tag('em'))).typ({'int': 'tag'}).realize()   
    ) == "He eats <em>apples</em>, doesn't he? ",\
    'question tag affirmative sentence'


def test_sentences_en_23():
    assert (
S(Pro("him").c('nom'),
  VP(V("eat"),
     NP(D("a"),
        N("apple").n('p')).tag('em'))).typ({'int': 'tag', 'neg': True}).realize()   
    ) == 'He does not eat <em>apples</em>, does he? ',\
    'question tag negative sentence'


def test_sentences_en_24():
    assert (
S(Pro("him").c('nom'),
  VP(V("eat").t('f'),
     NP(D("a"),
        N("apple").n('p')).tag('em'))).typ({'int': 'tag'}).realize()   
    ) == "He will eat <em>apples</em>, won't he? ",\
    'question tag affirmative sentence future'


def test_sentences_en_25():
    assert (
S(NP(D("a"),
     N("child")),
  VP(V("find"),
     NP(D("a"),
        N("cat"))).t('ps')).realize()   
    ) == 'A child found a cat. ',\
    '2. VP'


def test_sentences_en_26():
    assert (
S(NP(Pro("I").pe(3).g('m')),
  VP(V("hate"),
     NP(N("soup")))).realize()   
    ) == 'He hates soup. ',\
    '3. VP'


def test_sentences_en_27():
    assert (
S(NP(Pro("I").pe(3).g('f')),
  VP(V("eat"),
     NP(N("soup"))).t('ps')).realize()   
    ) == 'She ate soup. ',\
    '4. VP'


def test_sentences_en_28():
    assert (
S(NP(Pro("I").pe(2)),
  VP(V("enjoy"),
     NP(D("a"),
        N("meat")))).realize()   
    ) == 'You enjoy a meat. ',\
    '5. VP'


def test_sentences_en_29():
    assert (
S(NP(D("a"),
     N("girl")),
  VP(V("have"))).realize()   
    ) == 'A girl has. ',\
    '6. VP'


def test_sentences_en_30():
    assert (
AP(Adv("extremely"),
   A("pleasant")).realize()   
    ) == 'extremely pleasant',\
    '1. AP'


def test_sentences_en_31():
    assert (
AP(Adv("much"),
   A("quick").f('co')).realize()   
    ) == 'much quicker',\
    '2. AP'


def test_sentences_en_32():
    assert (
AP(Adv("very"),
   A("hard")).realize()   
    ) == 'very hard',\
    '3. AP'


def test_sentences_en_33():
    assert (
AdvP(Adv("very"),
     Adv("quietly")).realize()   
    ) == 'very quietly',\
    '1. AdvP'


def test_sentences_en_34():
    assert (
AdvP(Adv("extremely"),
     Adv("softly")).realize()   
    ) == 'extremely softly',\
    '2. AdvP'


def test_sentences_en_35():
    assert (
AdvP(Adv("totally"),
     Adv("abruptly")).realize()   
    ) == 'totally abruptly',\
    '3. AdvP'


def test_sentences_en_36():
    assert (
PP(P("on"),
   NP(D("a"),
      N("table"))).realize()   
    ) == 'on a table',\
    '1. PP'


def test_sentences_en_37():
    assert (
PP(P("by"),
   NP(D("a"),
      N("window"))).realize()   
    ) == 'by a window',\
    '2. PP'


def test_sentences_en_38():
    assert (
PP(P("in"),
   NP(D("the"),
      N("dark"),
      PP(P("of"),
         N("night")))).realize()   
    ) == 'in the dark of night',\
    '3. PP'


def test_sentences_en_39():
    assert (
PP(P("for"),
   NP(D("a"),
      N("while"))).realize()   
    ) == 'for a while',\
    '4. PP'


def test_sentences_en_40():
    assert (
PP(P("against"),
   AdvP(Adv("all")),
   N("odds")).realize()   
    ) == 'against all odds',\
    '5. PP'


def test_sentences_en_41():
    assert (
PP(P("of"),
   NP(A("great"),
      N("talent"))).realize()   
    ) == 'of great talent',\
    '6. PP'


def test_sentences_en_42():
    assert (
PP(P("with"),
   NP(D("that"),
      N("key"))).realize()   
    ) == 'with that key',\
    '7. PP'


def test_sentences_en_43():
    assert (
PP(P("of"),
   NP(N("piano"))).realize()   
    ) == 'of piano',\
    '8. PP'


def test_sentences_en_44():
    assert (
CP(C("or"),
   Pro("me").pe(1),
   Pro("I").pe(2),
   Pro("I").pe(3).g('f')).realize()   
    ) == 'me, you or she',\
    '1. CP'


def test_sentences_en_45():
    assert (
CP(C("and"),
   NP(N("cat")),
   NP(N("dog")),
   NP(N("snake"))).n('p').realize()   
    ) == 'cats, dogs and snakes',\
    '2. CP'


def test_sentences_en_46():
    assert (
CP(NP(N("cat")),
   NP(N("dog")),
   NP(N("snake"))).realize()   
    ) == 'cat, dog, snake',\
    '3. CP'


def test_sentences_en_47():
    assert (
S(NP(D("the"),
     N("mouse"),
     SP(Adv("that"),
        NP(D("the"),
           N("cat")),
        VP(V("eat").t('ps'))))).realize()   
    ) == 'The mouse that the cat ate. ',\
    '1. SP'


def test_sentences_en_48():
    assert (
NP(D("a"),
   N("girl"),
   SP(Pro("who"),
      VP(V("play"),
         NP(N("soccer"))))).realize()   
    ) == 'a girl who plays soccer',\
    '2. SP(who)'


def test_sentences_en_49():
    assert (
NP(D("the"),
   N("girl").n('p'),
   SP(Pro("who"),
      VP(V("play"),
         NP(N("soccer"))))).realize()   
    ) == 'the girls who play soccer',\
    '2. SP(who)'


def test_sentences_en_50():
    assert (
S(NP(D("the"),
     N("chicken")),
  VP(V("bite").t('p'))).realize()   
    ) == 'The chicken bites. ',\
    'No pronoun'


def test_sentences_en_51():
    assert (
S(NP(D("the"),
     N("chicken")).pro(True),
  VP(V("bite").t('p'))).realize()   
    ) == 'It bites. ',\
    'Subject as pronoun'


def test_sentences_en_52():
    assert (
S(NP(D("the"),
     N("chicken")),
  VP(V("bite").t('p'),
     NP(D("a"),
        N("kid").n('p')))).realize()   
    ) == 'The chicken bites kids. ',\
    'No pronoun + cd'


def test_sentences_en_53():
    assert (
S(NP(D("the"),
     N("chicken")),
  VP(V("bite").t('p'),
     NP(D("a"),
        N("kid").n('p')).pro(True))).realize()   
    ) == 'The chicken bites them. ',\
    'Cd as pronoun'


def test_sentences_en_54():
    assert (
S(NP(D("the"),
     N("chicken")).pro(True),
  VP(V("bite").t('p'),
     NP(D("a"),
        N("kid").n('p')).pro(True))).realize()   
    ) == 'It bites them. ',\
    'Cd and subject as pronoun'


def test_sentences_en_55():
    assert (
S(NP(D("the"),
     N("chicken")),
  VP(V("bite").t('p'),
     NP(D("a"),
        N("kid").n('p')),
     PP(P("at"),
        NP(D("my").pe(1),
           N("house"))))).realize()   
    ) == 'The chicken bites kids at my house. ',\
    'No pronoun + cd + ci'


def test_sentences_en_56():
    assert (
S(NP(D("the"),
     N("chicken")),
  VP(V("bite").t('p'),
     NP(D("a"),
        N("kid").n('p')),
     PP(P("at"),
        NP(D("my").pe(1),
           N("house")).pro(True)))).realize()   
    ) == 'The chicken bites kids at it. ',\
    'Ci as pronoun'


def test_sentences_en_57():
    assert (
S(NP(D("the"),
     N("chicken")).pro(True),
  VP(V("bite").t('p'),
     NP(D("a"),
        N("kid").n('p')).pro(True),
     PP(P("at"),
        NP(D("my").pe(1),
           N("house")).pro(True)))).realize()   
    ) == 'It bites them at it. ',\
    'Subject, cd and ci as pronoun'


def test_sentences_en_58():
    assert (
S(NP(D("the"),
     N("chicken")).pro(True),
  VP(V("bite").t('p'),
     NP(D("a"),
        N("kid").n('p')).pro(True),
     PP(P("at"),
        NP(D("my").pe(1),
           N("house").g('n')).pro(True)))).realize()   
    ) == 'It bites them at it. ',\
    'Subject, cd and ci as pronoun'


def test_sentences_en_59():
    assert (
S(Pro("I").pe(1),
  VP(V("give"),
     PP(P("to"),
        NP(D("a"),
           N("woman"))))).realize()   
    ) == 'I give to a woman. ',\
    'woman -> feminine noun'


def test_sentences_en_60():
    assert (
S(Pro("I").pe(1),
  VP(V("give"),
     PP(P("to"),
        NP(D("a"),
           N("woman")).pro(True)))).realize()   
    ) == 'I give to her. ',\
    'woman -> feminine pronoun'


def test_sentences_en_61():
    assert (
S(NP(D("the"),
     N("soldier").n('p')),
  VP(V("find").t('ps'),
     NP(D("a"),
        N("girl")))).realize()   
    ) == 'The soldiers found a girl. ',\
    'Simple sentence'


def test_sentences_en_62():
    assert (
S(NP(D("the"),
     N("soldier").n('p')),
  VP(V("find").t('ps'),
     NP(D("a"),
        N("girl")))).typ({'pas': True}).realize()   
    ) == 'A girl was found by the soldiers. ',\
    'Passive sentence, with subject and cd'


def test_sentences_en_63():
    assert (
S(NP(D("the"),
     N("soldier").n('p')),
  VP(V("find").t('ps'))).typ({'pas': True}).realize()   
    ) == 'It was found by the soldiers. ',\
    'Passive sentence, no cd'


def test_sentences_en_64():
    assert (
S(VP(V("find").t('ps'),
     NP(D("a"),
        N("girl")))).typ({'pas': True}).realize()   
    ) == 'A girl was found. ',\
    'Passive sentence, no subject'

