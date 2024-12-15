# generation of French sentences using a list of verbs with a few indications
# inspired by
#    "A Library for Automatic Natural Language Generation of Spanish Texts"
#     Silvia García-Méndez, Milagros Fernández-Gavilanes, Enrique Costa-Montenegro, Jonathan Juncal-Martínez, F. Javier González-Castaño
#     Expert Systems with Applications, 120, 372-386
#     https://doi.org/10.48550/arXiv.2405.17280
# but using pyrealb as a generation engine and not "guessing" prepositions

import re
from random import choice
from pyrealb import *

lang = None

# language dependent strings
fileNames   = {"en":"./English-words.txt","fr":"./French-words.txt"}
determiners = {"en":["the", "a"],"fr":["le","un"]}
and_conj    = {"en":"and","fr":"et"}
pronoun     = {"en":"him","fr":"lui"}
copulae     = {"en":["be"],"fr":["être","sembler","paraître"]}
messages    = {"unknown word":{"en":"unknown word", "fr":"mot inconnu"},
               "bad category":{"en":"category not implemented","fr":"categorie non traitée"},
               "no verb":{"en":"no verb found","fr":"aucun verbe trouvé"}}

def make_groups(words)->([Terminal],[Terminal],[Terminal]):
    subj = []
    verb = []
    obj = []

    def pos_specified(word):
        word, cat = word.split("_",1)
        if cat not in ["A", "N", "P", "Adv", "D"]:
            print(f"*** {messages['bad category'][lang]}: {cat}: " + word)
            return None
        lemma = getLemma(word)
        if lemma is None:
            print(f"*** {messages['unknown word'][lang]}: "+word)
            return None
        if cat not in lemma:
            print(f"*** {messages['bad category'][lang]}: {cat}: " + word)
            return None
        if cat == "A": return A(word)
        if cat == "N": return N(word)
        if cat == "P": return P(word)
        if cat == "Adv" : return Adv(word)
        if cat == "D" : return D(word)
        return None ## should never happen...

    def pos_guessed(word):
        lemma = getLemma(word)
        if lemma is None:
            print(f"*** {messages['unknown word'][lang]}: "+word)
            return None
        # this is a bit tricky because of possible lexical ambiguity
        if "V" in lemma and ("N" not in lemma or (len(obj)==0 and len(subj)>0 and not plural)):
            verb.append(V(word))
        else:
            if "P" in lemma:
                term = P(word)
            elif "A" in lemma:
                if "N" in lemma :
                    if len(verb)>0 and verb[0].lemma in copulae[lang]:
                        term=A(word)
                    elif len([e for e in l if e.isA("N")])==0: # vérifier qu'on n'a pas encore de N
                        term = N(word)
                        if plural:term.n("p")
                    else:
                        term=A(word)
                else:
                    term = A(word)
            elif "Adv" in lemma:
                term = Adv(word)
            elif "N" in lemma:
                term = N(word)
                if plural: term.n("p")
            elif "D" in lemma:
                term = D(word)
            else:
                print(f"*** {messages['bad category'][lang]}:"+
                      str([key for key in lemma.keys() if key not in ["ldv","niveau"]]))
                return None
            return term

    for word in words:
        l = subj if len(verb)==0 else obj # vérifier à quelle liste on ajoute
        plural = False
        if word.endswith("+"):
            word=word[:-1]
            plural = True
        if "_" in word:
            term = pos_specified(word)
        else:
            term = pos_guessed(word)
        if term is not None:
            l.append(term)
    return (subj,verb,obj)

def hasA(ph:Phrase,c_type:str)->bool:
    return any(e.isA(c_type) for e in ph.constituents())

# add to a phrase, but avoid duplicating a determiner
def add_to_ph(ph:Phrase, word:Constituent)->Phrase:
    if word.isA("N") and not hasA(ph, "D"): # avoid adding another determinant
        ph.add(D(choice(determiners[lang])),0,prog=True)
    ph.add(word, prog=True)
    return ph

def makeNPs(terminals:[Terminal])->Phrase:
    if len(terminals)==0:
        return Pro(pronoun[lang])
    np = NP() # current NP
    phs = [np]    # current root
    for terminal in terminals:
        # this is a bit tricky because of possible lexical ambiguity
        if terminal.isA("N"):
            if not hasA(np,"N"):
                add_to_ph(np, terminal)
            else:
                np=NP()
                phs.append(add_to_ph(np,terminal))
        elif terminal.isA("Adv"):
            if phs[0].nbConstituents() == 0:
                phs.pop(0)
            np=NP()
            phs.append(AdvP(terminal,np))
        elif terminal.isA("A","D"):
            add_to_ph(np, terminal)
        elif terminal.isA("P"):
            if phs[0].isA("AdvP"):
                phs[0].remove(1)
                phs[0].add(PP(terminal,np),prog=True)
            else:
                if phs[0].nbConstituents() == 0:
                    phs.pop(0)
                np=NP()
                phs.append(PP(terminal,np))
        else:
            print(f"*** {messages['bad category'][lang]}: {terminal.toSource()}")
    if len(phs) == 1:
        return phs[0]
    if all(ph.constType=="NP" for ph in phs):
        return CP(C(and_conj[lang]),phs)
    return SP(phs)


def getVP(words:[Terminal])->Phrase|None:
    if len(words) == 0:
        print(f"*** {messages['no verb'][lang]}")
        return None
    if len(words) == 1:
        return VP(words[0])
    return CP(C(and_conj[lang]),[VP(w) for w in words])

# build sentence
def makeSentence(words:[str])->Phrase:
    # check last token for possible sentence modifications
    interrogative = False
    neg = False
    if "?" in words[-1] or '-' in words[-1] and len(words[-1])<3:
        interrogative = "?" in words[-1]
        neg = "-" in words[-1]
        words.pop()
    # groups input tokens into lists of Terminal
    subj,verb,comp = make_groups(words)
    if details:
        print(([e.toSource() for e in subj],[e.toSource() for e in verb],[e.toSource() for e in comp]))
    # build subject NP
    subjNP = makeNPs(subj)
    if subjNP.isA("Pro"):
        subjNP.c("nom")
    # build VP
    vp = getVP(verb)
    if vp is None:
        return subjNP
    # build complement
    compNP = makeNPs(comp)
    if compNP.isA("Pro"):
        compNP.c("acc")
    # build sentence
    if vp.isA("CP"):
        vp.constituents()[-1].add(compNP,prog=True)
    else:
        vp.add(compNP,prog=True)
    s = S(subjNP,vp)
    # apply sentence options
    if neg or interrogative:
        flags ={}
        if neg: flags["neg"]=True
        if interrogative : flags["int"]="yon"
        s.typ(flags)
    return s

details = False
if __name__ == '__main__':
    for lang in ["en","fr"]:
        load(lang)
        for line in open(fileNames[lang],"r",encoding="utf-8").readlines():
            words = re.split(r"\s*,\s*",line.strip())
            if details: print(words)
            s = makeSentence(words)
            if details: print(s.toSource())
            print(f"{line.strip():40} => {s.realize()}")
            if details: print("---")
        print(10*"=")
