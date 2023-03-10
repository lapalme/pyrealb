from pyrealb import *
from test import test
from ppJson import ppJson
from io import StringIO

def json_tests():
    loadEn()
    exp=S(NP(D("the"),N("cat").n("p")),
                VP(V("sit").t("ps"),
                   PP(P("on"),
                      NP(D("the"),N("mat"))))).typ({"neg":True})
    outExp=StringIO()
    ppJson(outExp,exp.toJSON())
    dep=root(V("sit").t("f"),
                   subj(N("cat").n("p"),
                        det(D("the"))),
                   comp(P("on"),
                        mod(N("mat"),
                            det(D("the"))))).typ({"neg":True})
    outDep=StringIO()
    ppJson(outDep,dep.toJSON())

    tests=[
        {"expression": exp,
         "expected": "The cats did not sit on the mat. ",
         "message": "original sentence built using Phrase"},
        {"expression": outExp.getvalue(),
         "expected":
"""{"phrase":"S",
 "lang":"en",
 "elements":[{"phrase":"NP",
              "elements":[{"terminal":"D",
                           "lemma":"the"},
                          {"terminal":"N",
                           "lemma":"cat",
                           "props":{"n":"p"}}]},
             {"phrase":"VP",
              "elements":[{"terminal":"V",
                           "lemma":"sit",
                           "props":{"t":"ps"}},
                          {"phrase":"PP",
                           "elements":[{"terminal":"P",
                                        "lemma":"on"},
                                       {"phrase":"NP",
                                        "elements":[{"terminal":"D",
                                                     "lemma":"the"},
                                                    {"terminal":"N",
                                                     "lemma":"mat"}]}]}]}],
 "props":{"typ":{"neg":true}}}
""",
         "message": "pretty-print of JSON froom Phrase"},
        {"expression": fromJSON(exp.toJSON()),
         "expected": "The cats did not sit on the mat. ",
         "message": "original sentence built using Phrase"},

        {"expression": dep,
         "expected": "The cats will not sit on the mat. ",
         "message": "original sentence built using Phrase"},
        {"expression": outDep.getvalue(),
         "expected":
 """{"dependent":"root",
 "terminal":{"terminal":"V",
             "lemma":"sit",
             "props":{"t":"f"}},
 "dependents":[{"dependent":"subj",
                "terminal":{"terminal":"N",
                            "lemma":"cat",
                            "props":{"n":"p"}},
                "dependents":[{"dependent":"det",
                               "terminal":{"terminal":"D",
                                           "lemma":"the"},
                               "dependents":[]}]},
               {"dependent":"comp",
                "terminal":{"terminal":"P",
                            "lemma":"on"},
                "dependents":[{"dependent":"mod",
                               "terminal":{"terminal":"N",
                                           "lemma":"mat"},
                               "dependents":[{"dependent":"det",
                                              "terminal":{"terminal":"D",
                                                          "lemma":"the"},
                                              "dependents":[]}]}]}],
 "props":{"typ":{"neg":true}},
 "lang":"en"}
""",
         "message": "pretty-print of JSON froom Phrase"},
        {"expression": fromJSON(dep.toJSON()),
         "expected": "The cats will not sit on the mat. ",
         "message": "original sentence built using Phrase"},

    ]
    return tests

if __name__ == '__main__':
    test("JSON-tests","en",json_tests)
