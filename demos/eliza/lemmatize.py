from pyrealb import *
import re,sys

trace=False

# only set this flag during development fo this IDE because it takes a while to execute
# and is not needed unless the lexicons or the rules are changed
checkAmbiguities=False

lemmataLang="fr"

def addLemma(lemmata,word,jsrExp):
    if trace:print(f"addLemma::{word}:{jsrExp}")
    if checkAmbiguities:
        # check if jsRealB generates the same string...
        genWord=jsrExp.realize()
        if genWord!=word:
            # ignore differences for French "essentiellement réflexifs" verbs
            if (lemmataLang == "en" or  not jsrExp.isA("V") or  not jsrExp.isReflexive() or
                   (not genWord.endswith(word) and not genWord.startswith(word))):
                print("%s => %s != %s"%(jsrExp,genWord,word))
    # add word
    if word in lemmata:
        lemmata[word].append(jsrExp)
    else:
        lemmata[word]=[jsrExp]

def jsrExpInit(pos,lemma):
    return fromJSON({"terminal": pos, "lemma": lemma, "lang": lemmataLang})

# generate a list of jsRealB expressions (only Pro will have more than 1)
#  from a given form (lemma), for a given part-of-speech (pos)
#  using information from the declension and lexicon information (declension, lexiconEntry)
def genExp(declension,pos,entry,lexiconEntry):
    if trace:print(f"genExp(declension,{pos},{entry},{lexiconEntry}")
    jsrExp = jsrExpInit(pos,entry)
    if pos=="N":
        g=lexiconEntry["g"] if "g" in lexiconEntry else None
        # gender are ignored in English
        if lemmataLang=="en" or declension["g"]==g:
            if declension["n"]=="p": jsrExp.n("p")
        elif g=="x":
            if declension["g"]=="f": jsrExp.g("f")
            if declension["n"]=="p": jsrExp.n("p")
    elif pos=="Pro" or pos== "D":
        # gender
        defaultG="m" if lemmataLang=="fr" else "n"
        if "g" in declension:
            dg=declension["g"]
            if dg=="x" or dg=="n":
                dg=defaultG
        else:
            dg=defaultG
        if dg!=defaultG: jsrExp.g(dg)
        if "n" in declension:
            dn = declension["n"]
            if dn=="x":
                dn="s"
            if dn!="s": jsrExp.n(dn)
        if "pe" in declension:
            pe=declension["pe"]
            if pe!=3 or entry=="moi": jsrExp.pe(pe)
        if "own" in declension:
            jsrExp.ow(declension["own"])
        if "tn" in declension:
            jsrExp.tn(declension["tn"])
        elif "c" in declension:
            jsrExp.c(declension["c"])
    elif pos=="A":
        if lemmataLang=="fr":
            g=declension["g"]
            if "g" not in declension or declension["g"]=="x":
                g=declension["g"]
            if g != "m":jsrExp.g(g)
            if "n" in declension:
                n=declension["n"]
            else:
                n="s"
            if n!="s": jsrExp.n(n)
        else: # comparatif en anglais
            if "f" in declension:
                jsrExp.f(declension["f"])
    elif pos=="Adv":
        if lemmataLang=="en":
            if "f" in declension:
                jsrExp.f(declension["f"])
    else:
        print("***POS not implemented:%s",pos,file=sys.stderr)
    return jsrExp

def expandConjugation(lexicon,lemmata,rules,lemma,tab):
    if trace:print(f"expandConjugation::{lemma}:{tab}")
    if tab not in rules["conjugation"]:return
    conjug=rules["conjugation"][tab]
    ending=conjug["ending"]
    endRadical=len(lemma)-len(ending)
    radical=lemma[:endRadical]
    if lemma[endRadical:]!=ending:
        print("strange ending:",lemma,":",ending,file=sys.stderr)
        return
    for t in conjug["t"]:
        persons=conjug["t"][t]
        if persons is None: continue
        if isinstance(persons,list) and len(persons)==6:
            for pe in range(0,6):
                if persons[pe] is None: continue
                word=radical+persons[pe]
                pe3=pe%3+1
                n="p" if pe>=3 else "s"
                jsrExp= jsrExpInit("V",lemma)
                if t != "p": jsrExp.t(t)
                if pe3 != 3: jsrExp.pe(pe3)
                if n != "s": jsrExp.n(n)
                addLemma(lemmata,word,jsrExp)
        elif isinstance(persons,str):
            word = radical+persons
            jsrExp=jsrExpInit("V",lemma)
            if t != "p": jsrExp.t(t)
            addLemma(lemmata,word,jsrExp)
        else:
            print("***Strange persons:",lemma,persons,file=sys.stderr)

def expandDeclension(lexicon,lemmata,rules,entry,pos,tab):
    if trace:print(f"expandDeclension::{entry}:{tab}")
    rulesDecl=rules["declension"]
    declension=None
    if tab in rulesDecl:
        declension=rulesDecl[tab]
    elif tab in rules["regular"]:
        addLemma(lemmata,entry,jsrExpInit(pos,entry))
        return
    if declension is None or "ending" not in declension: return
    ending=declension["ending"]
    endRadical=len(entry)-len(ending)
    radical=entry[:endRadical]
    if entry[endRadical:]!=ending:
        print("strange ending:",entry,":",ending,file=sys.stderr)
        return
    decl=declension["declension"]
    seenVals = []
    for  l  in range(0,len(decl)):
        dec = decl[l]
        if dec["val"] not in seenVals: # avoid identical values in the same table
            seenVals.append(dec["val"])
            jsrExp=genExp(decl[l],pos,entry,lexicon[entry][pos])
            if jsrExp is not None:
                word=radical+decl[l]["val"]
                addLemma(lemmata,word,jsrExp)

def buildLemmata(lang,lexicon,rules):
    global lemmataLang
    lemmataLang=lang
    if checkAmbiguities:
        print("Checking realization ambiguities for %s lemmata ..."%("English" if lang=="en" else "French"))
    lemmata={}
    for entry,entryInfos in lexicon.items():
        for pos in entryInfos.keys():
            if pos=="basic" or pos=="value":continue
            if pos=="Pc": continue; # ignore punctuation
            if pos=="V": # conjugation
                expandConjugation(lexicon,lemmata,rules,entry,
                                  entryInfos["V"]["tab"])
            else:       # declension
                expandDeclension(lexicon,lemmata,rules,entry,pos,entryInfos[pos]["tab"])
    return lemmata

def tokenizeFr(sentence):
    elidableFRList = ["ce", "la", "le", "je", "me", "te", "se", "de", "ne", "que", "puisque", "lorsque", "jusque", "quoique"]
    contractionFrTable = {
        "au":"à+le","aux":"à+les","ç'a":"ça+a",
        "du":"de+le","des":"de+les","d'autres":"de+autres",
        "s'il":"si+il","s'ils":"si+ils"}

    # split on non-French letter and apostrophe and remove empty tokens
    words = [w for w in re.split(r"[^a-z'àâéèêëîïôöùüç]",sentence.lower()) if len(w)>0]
    # expand elision and contraction
    i=0
    while i<len(words):
        word = words[i]
        if word not in lemmataFr:
            # word does not exist try to expand elision or contraction
            m = re.fullmatch(r"(.*?)'([haeiouyàâéèêëîïôöùüç].*)",word) # check for apostrophe followed by vowell or h
            if m :
                for elw in elidableFRList: # expand elision
                    if elw.startswith(m.group(1)):
                        words[i:i+1]=[elw,m.group(2)]
                        i+=1
                        break
            else:
                if word in contractionFrTable:
                    words[i:i+1]=contractionFrTable[word].split("+")
                    i+=1
        i+=1
    return words

loadFr()
lemmataFr = buildLemmata("fr",getLexicon("fr"),getRules("fr"))

print("---lammataFr: OK")

if __name__ == '__main__':
    # add tests fo  lemmatization
    tokens = tokenizeFr("J'ai mangé du pain aujourd'hui à l'hôpital, quoiqu'encore pas assez!")
    print(tokens)
