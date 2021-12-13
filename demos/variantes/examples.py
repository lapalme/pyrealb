# add person names to the vocabulary
 
# {"ref":"Huang","url":"http://www.people.fas.harvard.edu/~ctjhuang/lecture_notes/lecch6.html","no":"35a",
#  "expr":f"""
# """},

examplesEn = [
{
 "expr":f"""
S(NP(D('the'),
     N('cat')),
  VP(V('eat'),
     NP(D('the'),
        N('mouse'))))"""},
{"ref":"Huang","url":"http://www.people.fas.harvard.edu/~ctjhuang/lecture_notes/lecch6.html","no":"35a",
 "expr":f"""
S(Pro("I").pe(2),
  VP(V("know"),
     SP(Pro("that"),
        S(N("Bill"),
          VP(V("marry").t("ps"),
             NP(D("my").g("m").ow("s"),
                Q("ex").lier("-"),N("wife")))))))
"""},
{"ref":"Huang","url":"http://www.people.fas.harvard.edu/~ctjhuang/lecture_notes/lecch6.html","no":"35b",
 "expr":f"""
S(Pro("I").g("f"),
  VP(V("love"),
     Pro("me"),Adv("still")))
"""},
{"ref":"Huang","url":"http://www.people.fas.harvard.edu/~ctjhuang/lecture_notes/lecch6.html","no":"Homework 6 (1a)",
 "expr":f"""
S(N("Mary"),
  VP(V("talk"),
     PP(P("to"),N("Bill"))))
"""},
{"ref":"Huang","url":"http://www.people.fas.harvard.edu/~ctjhuang/lecture_notes/lecch7.html","no":"11",
 "expr":f"""
S(NP(N("John")),
  VP(V("cheat").t("ps"),NP(N("Bill"))))
"""},
{"ref":"Huang","url":"http://www.people.fas.harvard.edu/~ctjhuang/lecture_notes/lecch7.html","no":"12",
 "expr":f"""
S(NP(D("the"),N("teacher")),
  VP(V("put").t("ps"),
     NP(D("the"),N("glass").n("p")),
     PP(P("in"),NP(D("the"),N("drawer")))))"""},
{"ref":"Huang","url":"http://www.people.fas.harvard.edu/~ctjhuang/lecture_notes/lecch7.html","no":"26b",
 "expr":f"""
S(NP(N("Bill")),
  VP(V("explain"),
     NP(D("the"),N("problem")),
        PP(P("to"),Pro("me").g("f"))))
"""},
{"ref":"Huang","url":"http://www.people.fas.harvard.edu/~ctjhuang/lecture_notes/lecch7.html","no":"26c",
 "expr":f"""
S(NP(N("Jim")),
  VP(V("make"),
     NP(D("the"),N("claim"),
        SP(S(Pro("that"),
          NP(N("Bill")),
          VP(V("put").t("ps"),
             NP(D("the"),N("idea")),
             PP(P("behind"),
                Pro("me")))).typ({{"mod":"nece"}})
           ))))
"""},
];
examplesFr = [
    {
     "expr":f"""
S(NP(D('le'),
     N('chat')),
  VP(V('manger'),
     NP(D('le'),
        N('souris'))))"""},
{"ref":"Lingolia","url":"https://francais.lingolia.com/fr/grammaire/les-verbes/passif","no":"2",
     "expr":f"""
S(NP(D('le'),
     N('passant').n("p")),
  VP(V('appeler'),
     NP(D('le'),
        N('ambulance'))))"""},
{"ref":"Lingolia","url":"https://francais.lingolia.com/fr/grammaire/les-verbes/passif","no":"3",
     "expr":f"""
S(NP(D('le'),
     N('police')),
  VP(V('recueillir'),
     NP(D('un'),
        N('témoignage').n("p"))))"""},
{"ref":"Huang","url":"http://www.people.fas.harvard.edu/~ctjhuang/lecture_notes/lecch6.html","no":"35a",
 "expr":f"""
S(Pro("je").pe(2),
  VP(V("savoir"),
     SP(Pro("que"),
        S(Q("Bill"),
          VP(V("épouser").t("ps"),
             D("mon").g("m"),
             Q("ex").lier("-"),N("femme"))))
             ))
"""},
{"ref":"Point du FLE","url":"https://www.lepointdufle.net/ressources_fle/cod_coi_3.htm","no":"3",
 "expr":f"""
# Essayez en enlevant un ou les .pro()
S(Pro("lui").c("nom"),
  VP(V("montrer"),
     NP(D("le"),N("lettre").n("p"),
        SP(Pro("que"),
           Pro("lui").c("nom"),
           VP(V("recevoir").t("pc")))).pro(),
     PP(P("à"),
        NP(D("mon"),N("ami").g("f"))).pro()))
"""},
{"ref":"Point du FLE","url":"https://www.lepointdufle.net/ressources_fle/cod_coi_3.htm","no":"8",
 "expr":f"""
# Essayez en enlevant un ou les .pro()
S(Pro("lui").c("nom"),
  VP(V("parler").t("pc"),
     PP(P("à"),NP(D("mon"),N("ami"))).pro(),
     PP(P("de"),NP(D("mon"),N("problème"))).pro()))
"""}
];
