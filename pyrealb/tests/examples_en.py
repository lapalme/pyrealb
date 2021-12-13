# examples adapted from jsRealB2.js
# some "hard" expressions used for debugging "corner cases"

import datetime
from context import pyrealb
from pyrealb import *
from tests.test import test

apple = NP(D("a"),N("apple"))
appleC = lambda:NP(D("a"),N("apple"))
appleF = lambda:NP(D("a"),N("apple"))

def examples_en():
    loadEn()
    examples_en = [
    [V("love"),"loves"],                             # 0
    [V("have").t("ps"),"had"],                       # 1
    [V("be").pe(3),"is"],                            # 2
    [VP(V("love")).typ({"neg":true}),"does not love"], # 3
    [VP(V("love")).typ({"int":"yon"}),"does love? "],  # 4
    [VP(V("love")).typ({"prog":true}),"is loving"],    # 5
    [VP(V("love")).typ({"mod":"poss"}),"can love"],    # 6
    # examples from the "Architecture..." paper
    # Figure 1
    [S(Pro("him").c("nom"),                          # 7
       VP(V("eat"),
          NP(D("a"),N("apple").n("p")).tag("em")
     )),"He eats <em>apples</em>."],
    #  Figure 1 (with global modification)
    [S(Pro("him").c("nom"),                          # 8
       VP(V("eat"),
          NP(D("a"),N("apple").n("p")).tag("em")
     )).t("ps"),
     "He ate <em>apples</em>."],
    # Figure 4
    [S(Pro("him").c("nom"),                          # 9
       VP(V("eat"),
          NP(D("a"),N("apple").n("p"))
     )).typ({"neg":true}),"He does not eat apples."],
    # Figure 5
    [S(Pro("him").c("nom"),                          #10
       VP(V("eat"),
          NP(D("a"),N("apple").n("p"))
     )).typ({"neg":true,"pas":true}),
     "Apples are not eaten by him."],
    # Section 6.1
    [S(Pro("him").c("nom"), VP(V("eat"),            # 11
       NP(D("a"),N("apple").n("p")).add(A("red"))) 
      ).add(Adv("now").a(","),0),
     "Now, he eats red apples."],
    # Section 6.2
    [S(CP(C("and"),NP(D("the"),N("apple")),         # 12
                   NP(D("the"),N("orange")),
                   NP(D("the"),N("banana"))), 
       VP(V("be"),A("good"))),
     "The apple, the orange and the banana are good."],
    [S(CP(C("and"),NP(D("the"),N("apple"))),        # 13
       VP(V("be"),A("good"))),
     "The apple is good."],
     # Section 6.3
     [S(Pro("him").c("nom"),                        # 14
        CP(C("and"),
           VP(V("eat"),apple), VP(V("love"),apple.pro()))),
      "He eats an apple and loves it."],
      # this example is not exactly what is in the paper, but I have not managed to make it work properly
     [S(NP(D("a"),N("apple")).pro(),VP(V("be"),A("red"))),# 15 
      "It is red."],
     [S(Pro("him").c("nom"),                       # 16
        CP(C("and"),
           VP(V("eat"),appleC()),
           VP(V("love"),appleC().pro()))),
      "He eats an apple and loves it."],
     [S(appleC() ,VP(V("be"),A("red"))),             # 17
      "An apple is red."],
     [S(Pro("him").c("nom"),                       # 18
        CP(C("and"),
           VP(V("eat"),appleF()), 
           VP(V("love"),appleF().pro()))),
      "He eats an apple and loves it."],
     [S(appleF() ,VP(V("be"),A("red"))),           # 19
      "An apple is red."],
      # Section 6.4
      [S(Pro("him").c("nom"),                      # 20
         VP(V("eat"),
            NP(D("a"), N("apple").tag("a", {"href":"https:#en.wikipedia.org/wiki/Apple"})))),
       'He eats an <a href="https:#en.wikipedia.org/wiki/Apple">apple</a>.'],
      # Section 6.6
      [NP(NO(1).dOpt({"nat":true}),N("plane")),     # 21
       "one plane"],   
      [NP(NO(3).dOpt({"nat":true}),N("plane")),     # 22
       "three planes"],
      [NP(NP(D("the"),                            # 23 
        A("large").f("su"),
        NP(P("of"),
           D("the"),
           N("trainer").n("p")).a(",")),
        D("this").n("s"),    # check propagation of the number (this should not be these)
        N("addition").n("s")),
       "the largest of the trainers, this addition"]
    ]
    tests = [{}]
    for exp, expected in examples_en:
        tests.append({
            "expression": exp,
            "expected": expected,
            "message": f"Phrase complète:  {expected}"
        })
    return tests

if __name__ == '__main__':
    test("Sentences in English","en",examples_en,badOnly=True)
