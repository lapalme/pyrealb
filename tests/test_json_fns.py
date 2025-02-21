import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..','src')))

from pyrealb import *
from io import StringIO
from ppJson import ppJson

load("en")

exp = lambda:S(NP(D("the"), N("cat").n("p")),
        VP(V("sit").t("ps"),
           PP(P("on"),
              NP(D("the"), N("mat"))))).typ({"neg": True})
outExp = StringIO()
ppJson(outExp, exp().toJSON())
dep = lambda: root(V("sit").t("f"),
           subj(N("cat").n("p"),
                det(D("the"))),
           comp(P("on"),
                mod(N("mat"),
                    det(D("the"))))).typ({"neg": True})
outDep = StringIO()
ppJson(outDep, dep().toJSON())


def test_json_fns_1():
    assert exp().realize() == "The cats did not sit on the mat. ", \
        "original sentence built using Phrase"
    
def test_json_fns_2():
    assert (outExp.getvalue() ==
"""{"phrase":"S",
 "lang":"en",
 "elements":[{"phrase":"NP",
              "elements":[{"terminal":"D",
                           "lemma":"the"},
                          {"terminal":"N",
                           "lemma":"cat",
                           "props":{"cnt":"yes",
                                    "n":"p"}}]},
             {"phrase":"VP",
              "elements":[{"terminal":"V",
                           "lemma":"sit",
                           "props":{"t":"ps"}},
                          {"phrase":"PP",
                           "elements":[{"terminal":"P",
                                        "lemma":"on",
                                        "props":{"ldv":true}},
                                       {"phrase":"NP",
                                        "elements":[{"terminal":"D",
                                                     "lemma":"the"},
                                                    {"terminal":"N",
                                                     "lemma":"mat",
                                                     "props":{"cnt":"yes"}}]}]}]}],
 "props":{"typ":{"neg":true}}}
"""), "pretty-print of JSON from Phrase"

def test_json_fns_3():
    assert (fromJSON(exp().toJSON()).realize() == "The cats did not sit on the mat. "), \
        "original sentence rebuilt using json of Phrase"
    
def test_json_fns_4():
    assert (dep().realize() == "The cats will not sit on the mat. "), \
         "original sentence built using Dependent"

def test_json_fns_5():
    assert (outDep.getvalue() ==
"""{"dependent":"root",
 "terminal":{"terminal":"V",
             "lemma":"sit",
             "props":{"t":"f"}},
 "dependents":[{"dependent":"subj",
                "terminal":{"terminal":"N",
                            "lemma":"cat",
                            "props":{"cnt":"yes",
                                     "n":"p"}},
                "dependents":[{"dependent":"det",
                               "terminal":{"terminal":"D",
                                           "lemma":"the"},
                               "dependents":[]}]},
               {"dependent":"comp",
                "terminal":{"terminal":"P",
                            "lemma":"on",
                            "props":{"ldv":true}},
                "dependents":[{"dependent":"mod",
                               "terminal":{"terminal":"N",
                                           "lemma":"mat",
                                           "props":{"cnt":"yes"}},
                               "dependents":[{"dependent":"det",
                                              "terminal":{"terminal":"D",
                                                          "lemma":"the"},
                                              "dependents":[]}]}]}],
 "props":{"typ":{"neg":true}},
 "lang":"en"}
"""
), "pretty-print of JSON from Dependent"
    
def test_json_fns_6():
    assert (fromJSON(dep().toJSON()).realize() == "The cats will not sit on the mat. "), \
    "original sentence rebuilt using JSON version Dependent"

