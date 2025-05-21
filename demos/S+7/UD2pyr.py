# equivalent to jsRealB/demo/UDregenrator/UD2jsr.js
import re
from operator import methodcaller
from pyrealb import *

#  Mapping from UD features to jsr options
#      https://universaldependencies.org/u/feat/index.html
#   CAUTION: only deals with English and French phenomena that can be mapped to jsRealB options

# https://universaldependencies.org/u/feat/Mood.html
mood = {"Ind":{"Past":"ps","Pres":"p","Fut":"f","Imp":"i","Pqp":"pq",
                "Ppc":"pc","Ppce":"pc",#  added for pyrealb in French
                "Ppq":"pq","Ppqe":"pq",
                "Ppa":"pa","Ppae":"pa",
                "Pfa":"pa","Pfae":"pa"},
        "Imp":{"Pres":"ip"},
        "Cnd":{"Past":"cp","Pres":"c"},
        "Sub":{"Past":"spa","Pres":"s","Imp":"si","Pqp":"spq"},
        "Part":{"Past":"pp","Pres":"pr"},
        }

# https://universaldependencies.org/u/feat/VerbForm.html
verbform = {"Fin":None,"Inf":"b","Part":"pp","Ger":"pr"}

# https://universaldependencies.org/u/feat/Tense.html
#   indicative mood if not specified
tenses = mood["Ind"]

# https://universaldependencies.org/u/feat/Person.html
person = {"1":1,"2":2,"3":3}
person_psor=person

# https://universaldependencies.org/u/feat/Number.html
number = {"Sing":"s","Plur":"p", "Ptan":"s"}
number_psor = number

# https://universaldependencies.org/u/feat/Case.html
case_ = {"Acc":"acc","Dat":"dat","Gen":"gen","Nom":"nom"}

#  https://universaldependencies.org/u/feat/Definite.html
definite = {"Def":None,"Ind":None}
# https://universaldependencies.org/u/feat/Gender.html
gender = {"Masc":"m", "Fem":"f", "Neut":"n"}
gender_psor = gender

# https://universaldependencies.org/u/feat/Degree.html
degree = {"Cmp":"co","Sup":"su","Pos":None}

# https://universaldependencies.org/u/feat/PronType.html
pronType = {"Prs":None,"Art":None,"Int":None,"Rel":None,"Dem":None,"Neg":None,"Ind":None}

numtype = {"Card":None,"Ord":None}

reflex = {"Yes":"refl"}

udMapping = {
    # core arguments
    "nsubj":subj,"csubj":subj,
    "obj":comp,"ccomp":comp,
    "iobj":comp,"xcomp":comp,
    # non-core dependents
    "obl":comp,"advcl":mod,"advmod":mod,"aux":mod,
    "vocative":mod,"discourse":mod,"cop":mod,
    "expl":mod,"mark":mod,
    # nominal dependents
    "nmod":mod,"acl":comp,"amod":mod,"det":det,
    "appos":mod,"clf":mod,
    "nummod":mod,"case":mod,
    # coordination
    "conj":mod,"cc":mod,
    # multiword expressions
    "fixed":mod,"flat":mod,"compound":mod,
    # loose
    "list":mod,"parataxis":mod,"dislocated":mod,
    # special
    "orphan":mod,"goeswith":mod,"reparandum":mod,
    # other
    "punct":mod,"root":root,"dep":comp,
}

featsRE = re.compile(r"(.*?)\[(.*?)]")

def makeFeats(word):
    featsString = word.feats
    if featsString is None or featsString == "_" : return {}
    feats = {}
    for kv in featsString.split("|"):
        key,val=kv.split("=")
        m = featsRE.match(key)
        if m is None:
            feats[key]=val
        else:
            feats[m.group(1)+"_"+m.group(2)]=val
    return feats

def getOption(featName,allowed,feat):
    if feat not in allowed:
        print(f"*** Unknown feature for {featName}: {feat}")
        return None
    return allowed[feat]

def ud2pyr_deprel(ud_deprel):
     ixColon = ud_deprel.find(":") # ignore after colon
     if ixColon>=0: ud_deprel = ud_deprel[:ixColon]
     if ud_deprel in udMapping:
          return udMapping[ud_deprel]
     print("unknown UD deprels:",ud_deprel)
     return comp

# combine all typ options into a single lst and apply other options directly to a dependent
def applyOptions(expr,options):
    typOpts = {}
    for key,val in options:
        if key == "typ":
            typOpts.update(val)
        else:
            # method caller trick from https://medium.com/@jamesaaa100/how-to-call-a-python-function-with-a-string-cdd788fd5d42#:~:text=The%20operator%20module%20in%20Python,some%20condition%20or%20user%20input.
            methodcaller(key,val)(expr)
    if len(typOpts)>0:
        expr.typ(typOpts)
    return expr

# find index of first element in a lst that matches a condition, returns -1 if no one is found
# similar to Array.findIndex of JavaScript
def findIndex(array,condition):
    try:
        return next(i for i,e in enumerate(array) if condition(e))
    except StopIteration:
        return -1

def findLemma(lemmataMap,lemma,text,pos,posF):
    # check in the lexicon
    infos = getLemma(lemma)
    if infos is not None and pos in infos:
        return posF(lemma)
    # check in the lemmataMap and return first match of the right pos...
    if text in lemmataMap:
        try:
            return next(expr for expr in lemmataMap[text] if expr.isA(pos))
        except StopIteration:
            pass
    # try with lower case
    text_lower = text.lower()
    if text != text_lower and text_lower in lemmataMap:
        # try to find appropriate lemma
        try:
            return next(expr for expr in lemmataMap[text_lower] if expr.isA(pos)).cap()
        except StopIteration:
            pass
    # nothing found
    print(f"*** '{lemma}' not found as {pos}"+("" if infos is None else
            f", but exists as {', '.join(key for key in infos.keys() if key not in ['niveau','ldv','value'])}"))
    return None

def checkLemma(lemma,pos,posF):
    infos = getLemma(lemma)
    if infos is not None and pos in infos:
        return posF(lemma)
    # HACK: many UD determiners appear as adjectives
    if pos=="D" and "A" in infos: return A(lemma)
    print(f"*** '{lemma}' not found as {pos}"+("" if infos is None else
            f", but exists as {', '.join(key for key in infos.keys() if key not in ['niveau','ldv'])}"))
    return Q(lemma)

# check if first element of list satisfies a predicate
def checkFirst(lst, pred):
    return lst[0] if len(lst) > 0 and pred(lst[0]) else None

# check if last element of list satisfies a predicate
def checkLast(lst,pred):
    return lst[-1] if len(lst)>0 and pred(lst[-1]) else None
