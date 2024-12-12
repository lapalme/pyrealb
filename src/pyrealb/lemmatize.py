from .utils import fromJSON
from .Lexicon import getLexicon, getRules, getLanguage, getLemma, load
import sys

trace=False
# only set this flag during development fo this IDE because it takes a while to execute
# and is not needed unless the lexicons or the rules are changed
checkAmbiguities=False

def addLemma(lemmata,word,jsrExp):
    if trace:print(f"addLemma::{word}:{jsrExp}")
    if checkAmbiguities:
        # check if jsRealB generates the same string...
        genWord=jsrExp.realize()
        if genWord!=word:
            # ignore differences for French "essentiellement réflexifs" verbs
            if (getLanguage() == "en" or  not jsrExp.isA("V") or  not jsrExp.isReflexive() or
                   (not genWord.endswith(word) and not genWord.startswith(word))):
                print("%s => %s != %s"%(jsrExp,genWord,word))
    # add word
    if word in lemmata:
        lemmata[word].append(jsrExp)
    else:
        lemmata[word]=[jsrExp]

def jsrExpInit(pos,lemma):
    return fromJSON({"terminal": pos, "lemma": lemma, "lang": getLanguage()})

# generate a list of jsRealB expressions (only Pro will have more than 1)
#  from a given form (lemma), for a given part-of-speech (pos)
#  using information from the declension and lexicon information (declension, lexiconEntry)
def genExp(declension, pos, lemma, lexiconEntry):
    lemmataLang = getLanguage()
    if trace:print(f"genExp(declension,{pos},{lemma},{lexiconEntry}")
    jsrExp = jsrExpInit(pos, lemma)
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
            if pe!=3 or lemma== "moi": jsrExp.pe(pe)
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

def expandConjugation(lemmata,rules,lemma,tab):
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
            if t == "pp" and getLanguage() == "fr" and word != "été":
                # conjuguer les participes passés français
                if word.endswith("û"): word = word[:-1]+"u"
                addLemma(lemmata,word+"e",jsrExp.clone().g("f"))
                addLemma(lemmata,word+("" if word.endswith("s") else "s"),
                         jsrExp.clone().g("m").n("p"))
                addLemma(lemmata,word+"es",jsrExp.clone().g("f").n("p"))
        else:
            print("***Strange persons:",lemma,persons,file=sys.stderr)

def expandDeclension(lexicon,lemmata,rules,entry,pos,tab):
    if trace:print(f"expandDeclension::{entry}:{tab}")
    rulesDecl=rules["declension"]
    declension=None
    if tab in rulesDecl:
        declension=rulesDecl[tab]
    elif tab in rules["regular"] or declension is None:
        addLemma(lemmata,entry,jsrExpInit(pos,entry))
        return
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

def buildLemmataMap(lang):
    load(lang)
    lexicon = getLexicon()
    rules = getRules()
    if checkAmbiguities:
        print("Checking realization ambiguities for Enlish lemmata ..." if lang=="en" \
                  else "Vérification de la table des lemmes en français")
    lemmata={}
    for entry,entryInfos in lexicon.items():
        for pos in entryInfos.keys():
            if pos=="ldv" or pos=="niveau" or pos=="value":continue
            if pos=="Pc": continue; # ignore punctuation
            if pos=="V": # conjugation
                expandConjugation(lemmata,rules,entry,
                                  entryInfos["V"]["tab"])
            else:       # declension
                expandDeclension(lexicon,lemmata,rules,entry,pos,entryInfos[pos]["tab"])
    return lemmata
