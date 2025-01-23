from pyrealb import *

load('en')
lexicon = getLexicon()

gerundAlsoNoun = []
for lemma,entry in list(lexicon.items()):
    if "V" in entry:
        gerund = V(lemma).t("pr").realize()
        if gerund in lexicon and "N" in lexicon[gerund]:
            gerundAlsoNoun.append(gerund)
print(len(gerundAlsoNoun))
open("gerundAlsoNoun.txt","w",encoding="utf-8").write("\n".join(gerundAlsoNoun))