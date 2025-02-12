from pyrealb import *
from pyrealb.Lexicon import getLexicon, getRules # specific import used by the IDE
from pyrealb.lemmatize import buildLemmataMap

import unicodedata,re, sys
from ppJson import ppJson

trace=False

# only set this flag during development fo this IDE because it takes a while to execute
# and is not needed unless the lexicons or the rules are changed 
checkAmbiguities=False

lemmataLang="en"

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
lemmataEn=buildLemmataMap("en")
lemmataFr=buildLemmataMap("fr")

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
##  this program should be called with the -i command linge argument to accept other commands
print(f"** pyRealB {pyrealb_version} Interactive Development Environment [_help() for info]")
_en()
  
## some unit tests
# if __name__ == '__main__':
#     def show(cmd):
#         print("==>"+cmd)
#         eval(cmd)
#     print(lemmatize("love",lemmataEn))
#     print(lemmatize(".*love",lemmataEn))
#     print(lemmatize("suis",lemmataFr))
#     print(lemmatize("suis.*",lemmataFr))
#     print(getLexiconInfo("love",getLexicon("en")))
#     print(getLexiconInfo(".*ling",getLexicon("en")))
#     print("** try IDE commands **")
#     show("_en()")
#     show('_lm("him")')
#     show('+Pro("me")')
#     show('+Pro("me").tn("")')
#     show('+Pro("him")')
#     show('+Pro("him").tn("")')
#     show('_cn("v10")')
#     show('_cn("v.")')
#     show('_ce("y")')
#     show('_ce(".e")')
#     show('_lm("checks")')
#     show('_lx(".ling")')
#     show('_lx(".ling","N")')
#     show('+NP(D("a"),N("cat").n("p")).cap(False)')
#     show('_fr()')
#     show('_lm("se")')
#     show('_cn("v10")')
#     show('_cn("v.")')
#     show('_ce("oir")')
#     show('_ce(".re")')
#     show('_lm("amour")')
#     show('_lm(".*mour.")')
#     show('_lm("chat[^o]*")')
#     show('_lx(".*voir")')
#     show('_lx(".*voir","V")')
