from pyrealb import *
from pyrealb.Lexicon import getLexicon, getRules # specific import used by the IDE

import unicodedata,re, sys
from ppJson import ppJson

__all__ = [ # from pyRealB
     'A','Adv','C', 'D', 'DT', 'N', 'NO','P', 'Pro', 'Q','V',            # from Terminal
     'AP',  'AdvP',  'CP', 'NP', 'PP',  'VP', 'S', 'SP',                 # from Phrase
     'root', 'subj', 'det', 'mod', 'comp', 'coord',                      # from Dependent
     'currentLanguage', 'addToLexicon', 'getLemma', 'loadEn', 'loadFr',  # from Lexicon
     'fromJSON', 'oneOf', 'pyrealb_version',                             # from utils
     'pyrealb_datecreated',
     # from this IDE
     "_en", "_fr", "_cn", "_ce", "_dn", "_de", "_lm", "_lx", "_help"]

trace=False

# only set this flag during development fo this IDE because it takes a while to execute
# and is not needed unless the lexicons or the rules are changed 
checkAmbiguities=False

lemmataLang="en"

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


def removeAccent(s):
    return unicodedata.normalize('NFD',s.lower()).encode('ascii', 'ignore').decode("utf-8")

def lemmatize(query,lemmata):
    if query in lemmata: # check for verbatim
        return "\n".join(map(lambda e:e.toSource(),lemmata[query]))
    # try to match with a regular expression
    queryRE=re.compile(query)
    res =[(key,val) for key,val in lemmata.items() 
                                if queryRE.fullmatch(key) is not None]
    if len(res)==0:
        return query+" : "+("cannot be lemmatized" if lang=="en" 
                            else "ne peut être lemmatisé")
    else:
        # sort without accent to get more usual dictionary order
        res.sort(key=lambda k:removeAccent(k[0]))
        return "\n".join(key+" : "+"; ".join(map(lambda e:e.toSource(),val)) for key,val in res)

def getLexiconInfo(word,lexicon):
    if word in lexicon:
        return (word,lexicon[word])
    # try with a regular expression
    return [(entry,infos) for entry,infos in lexicon.items() 
                if re.fullmatch(word,entry)]

## build lemmata tables
loadEn()
lemmataEn=buildLemmata("en", getLexicon("en"),getRules("en"))
loadFr()
lemmataFr=buildLemmata("fr",getLexicon("fr"),getRules("fr"))

def getNo(no,table):
    if no in table: return [(no,table[no])]
    # try with a regular expression
    return [(key,val) for key,val in table.items() if re.fullmatch(no, key) is not None]

def getEnding(ending,table):
    return [(key,val) for key,val in table.items() 
                if re.fullmatch(ending,val["ending"]) is not None]

def displayResults(query,res,mess):
    if len(res)==0:
        print(f"{query} : {mess}")
        return
    # print("\n".join(f"{key} : {val}" for key,val in res))
    for key,val in res:
        print(key+":",end="")
        ppJson(sys.stdout,val,len(key)+1)
        print()

#### start of the interface
lemmata=None
lexicon=None
rules=None
lang=None

def _en():
    global lemmata,lexicon,rules,lang
    lemmata=lemmataEn
    rules=getRules("en")
    lexicon=getLexicon("en")
    lang="en"
    loadEn(True)

def _fr():
    global lemmata,lexicon,rules,lang
    lemmata=lemmataFr
    rules=getRules("fr")
    lexicon=getLexicon("fr")
    lang="fr"
    loadFr(True)



def _cn(no):
    displayResults(no,getNo(no,rules["conjugation"]),
                   "no conjugation found" if lang=="en" else "pas de conjugaison")

def _ce(ending):
    displayResults(ending,getEnding(ending,rules["conjugation"]),
                   "no conjugation ending found" if lang=="en" else "pas de fin de conjugaison")

def _dn(no):
    displayResults(no,getNo(no,rules["declension"]),
                   "no declension found" if lang=="en" else "pas de déclinaison")

def _de(ending):
    displayResults(ending,getEnding(ending,rules["declension"]),
                   "no declension ending found" if lang=="en" else "pas de fin de déclinaison")

def _lm(word):
    print(lemmatize(word,lemmata))

def _lx(word,terminal=None):
    res=getNo(word,lexicon)
    if terminal is not None:
        res=[(key,val) for key,val in res if terminal in val]
    displayResults(word,res,
                   "no lexicon lemma found" if lang=="en" else "pas d'entrée dans le lexique")

def _help():
    print('''pyrealb_ide: special commands (starting with _)

 _en() : load English lexicon and rules
 _fr() : load French lexicon and rules

 _cn("no"): show conjugation table no 
 _ce("no"): show conjugation ending no
 _dn("no"): show declension table no
 _de("no"): show declension ending no
 _lm("word"): show jsRealB expressions that can realize word
 _lx("word"[,"terminal"]) : show lexical information about word, 
            if terminal is present, show only entries having terminal in its table
 a parameter for these functions can be a regex that matches fully 
 
 Online documentation: http://www.iro.umontreal.ca/~lapalme/pyrealb/documentation.html?lang=en
''')


## start of the program
print(f"** pyRealB {pyrealb_version} Interactive Development Environment [_help() for info]")
_en()
  
## some unit tests
if __name__ == '__main__':
    def show(cmd):
        print("==>"+cmd)
        eval(cmd)
    print(lemmatize("love",lemmataEn))
    print(lemmatize(".*love",lemmataEn))
    print(lemmatize("suis",lemmataFr))
    print(lemmatize("suis.*",lemmataFr))
    print(getLexiconInfo("love",getLexicon("en")))
    print(getLexiconInfo(".*ling",getLexicon("en")))
    # print("** try IDE commands **")
    # show("_en()")
    # show('_lm("him")')
    # show('+Pro("me")')
    # show('+Pro("me").tn("")')
    # show('+Pro("him")')
    # show('+Pro("him").tn("")')
    # show('_cn("v10")')
    # show('_cn("v.")')
    # show('_ce("y")')
    # show('_ce(".e")')
    # show('_lm("checks")')
    # show('_lx(".ling")')
    # show('_lx(".ling","N")')
    # show('+NP(D("a"),N("cat").n("p")).cap(False)')
    # show('_fr()')
    # show('_lm("se")')
    # show('_cn("v10")')
    # show('_cn("v.")')
    # show('_ce("oir")')
    # show('_ce(".re")')
    # show('_lm("amour")')
    # show('_lm(".*mour.")')
    # show('_lm("chat[^o]*")')
    # show('_lx(".*voir")')
    # show('_lx(".*voir","V")')

    
    
    