from pyrealb import *

load('en')
lexicon = getLexicon()
outAdj = open("english-Adj-comp.txt","w",encoding="utf-8")
outAdv = open("english-Adv-comp.txt","w",encoding="utf-8")

for lemma,entry in list(lexicon.items()):
    if "A" in entry and entry["A"]["tab"]!="a1":
        outAdj.write(f"{lemma}\t{A(lemma).f('co').realize()}\t{A(lemma).f('su').realize()}\n")
    if "Adv" in entry and entry["Adv"]["tab"]!="b1":
        outAdv.write(f"{lemma}\t{Adv(lemma).f('co').realize()}\t{Adv(lemma).f('su').realize()}\n")
