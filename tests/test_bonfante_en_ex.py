import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..','src')))

from pyrealb import *
load("en")

def test_bonfante_en_ex_1():
    assert (
root(V("follow"),
     subj(Pro("me").pe(1).c('nom')),
     comp(N("link").n('p'),
          mod(V("indicate"),
              subj(Pro("that")),
              mod(Adv("strongly")).pos('pre')))).typ({'perf': True, 'prog': True}).realize()   
    ) == 'I have been following links that strongly indicate. ',\
    'p 47 2.2'


def test_bonfante_en_ex_2():
    assert (
root(V("say").t('ps'),
     subj(Pro("them").c('nom')),
     comp(V("give"),
          subj(Pro("them").c('nom')),
          comp(Pro("me").pe(1).c('dat')),
          comp(N("detail").n('p'),
               det(D("that"))),
          comp(P("over"),
               comp(N("phone"),
                    det(D("the"))))).typ({'neg': True, 'mod': 'poss', 'contr': True})).realize()   
    ) == "They said they can't give me those details over the phone. ",\
    'p 56 2.16'


def test_bonfante_en_ex_3():
    assert (
coord(C("and"),
      root(V("finance").n('p'),
           subj(Pro("who"),
                mod(N("people"),
                    det(D("the")),
                    det(D("same"))).pos('pre')),
           comp(N("arm").n('p'))),
      root(V("dispatch").n('p'),
           comp(N("murderer").n('p'),
                mod(N("suicide")).pos('pre')))).realize()   
    ) == 'The same people who finance arms and dispatch suicide murderers. ',\
    'p 58'


def test_bonfante_en_ex_4():
    assert (
root(V("be"),
     subj(Pro("me").c('nom').pe(1)),
     mod(V("determine").t('pp'),
         comp(V("prove").t('b-to'),
              comp(P("to"),
                   comp(N("committee").cap(True),
                        det(D("the")))),
              comp(Pro("that"),
                   comp(V("be"),
                        subj(Pro("me").c('nom').pe(1)),
                        mod(A("successful"))).typ({'mod': 'poss'}))))).realize()   
    ) == 'I am determined to prove to the Committee that I can be successful. ',\
    ' Figure 2.24 p 61 '


def test_bonfante_en_ex_5():
    assert (
root(V("make"),
     det(Adv("so")),
     subj(V("kidnap").t('pr'),
          det(D("this"))),
     comp(Pro("him").c('acc'),
          comp(V("look").t('b'),
               mod(A("weak"))))).cap(False).realize()   
    ) == 'so this kidnapping makes him look weak',\
    ' Figure 2.26 p 62'


def test_bonfante_en_ex_6():
    assert (
S(CP(C("but"),
     SP(NP(D("a"),
           N("politician")),
        VP(V("fool"),
           NP(D("most"),
              N("voter").n('p')),
           PP(P("on"),
              NP(D("most"),
                 N("issue").n('p')),
              NP(D("most"),
                 PP(P("of"),
                    NP(D("the"),
                       N("time"))))))).typ({'mod': 'poss'}).a(','),
     SP(NP(D("no"),
           N("politician")),
        VP(V("fool"),
           NP(D("all"),
              N("voter").n('p')),
           PP(P("on"),
              NP(AP(D("every"),
                    A("single")),
                 N("issue").n('s')),
              NP(D("all"),
                 PP(P("of"),
                    NP(D("the"),
                       N("time"))))))).typ({'mod': 'poss'}))).realize()   
    ) == 'A politician can fool most voters on most issues most of the time, but no politicians can fool all voters on every single issue all of the time. ',\
    ' Figure 4.21 p 116 / REM: utilise une fonction pour factoriser le code'

