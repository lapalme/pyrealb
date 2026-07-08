import re
from pyrealb import *

# Mapping of UD POS tags to jsRaelB constructors
# taken from https://universaldependencies.org/u/pos/index.html
# udPos_jsrPos = {
#      #  Open class
#     ADJ:A,
#     ADV:Adv,
#     INTJ:Q,
#     NOUN:N,
#     PROPN:Q,
#     VERB:V,
#      # Closed class
#     ADP:P,
#     AUX:V,
#     CCONJ:C,
#     DET:D,
#     NUM:NO,
#     PART:Q,
#     PRON:Pro,
#     SCONJ:C,
#      # other
#     PUNCT:Q,
#     SYM:Q,
#     X:Q,
# };

#  Mapping from UD features to jsr options
#      https:#universaldependencies.org/u/feat/index.html
#   CAUTION: only deals with English and French phenomena that can be mapped to jsRealB options

# https:#universaldependencies.org/u/feat/Mood.html
mood = {"Ind":{"Past":"ps","Pres":"p","Fut":"f","Imp":"i","Pqp":"pq",
               "Ppc":"pc","Ppce":"pc", # Ppc added for jsRealB in French
               "Ppq":"pq","Ppqe":"pq",
               "Ppa":"pa","Ppae":"pa",
               "Pfa":"pa","Pfae":"pa"},
        "Imp":{"Pres":"ip"},
        "Cnd":{"Past":"cp","Pres":"c"},
        "Sub":{"Past":"spa","Pres":"s","Imp":"si","Pqp":"spq",
               "Spa":"spa","Spe":"spa", # Spa added for jsRealB in French
               "Spqa":"spq","Spqe":"spq"},
        "Part":{"Past":"pp","Pres":"pr"},
        }

# https:#universaldependencies.org/u/feat/VerbForm.html
verbform = {"Fin":None,"Inf":"b","Part":"pp","Ger":"pr"}

# https:#universaldependencies.org/u/feat/Tense.html
#   indicative mood if not specified
tenses = mood["Ind"] | mood["Sub"]

# https:#universaldependencies.org/u/feat/Person.html
person = {"1":1,"2":2,"3":3}
person_psor = person

# https:#universaldependencies.org/u/feat/Number.html
number = {"Sing":"s","Plur":"p", "Ptan":"s"}
number_psor = number

# https:#universaldependencies.org/u/feat/Case.html
case_ = {"Acc":"acc","Dat":"dat","Gen":"gen","Nom":"nom"}

#  https:#universaldependencies.org/u/feat/Definite.html
definite = {"Def":None,"Ind":None}
# https:#universaldependencies.org/u/feat/Gender.html
gender = {"Masc":"m", "Fem":"f", "Neut":"n"}
gender_psor = gender

# https:#universaldependencies.org/u/feat/Degree.html
degree = {"Cmp":"co","Sup":"su","Pos":None}

# https:#universaldependencies.org/u/feat/PronType.html
pronType = {"Prs":None,"Art":None,"Int":None,"Rel":None,"Dem":None,"Neg":None,"Ind":None}

numtype = {"Card":None,"Ord":None}

reflex = {"Yes":"refl"}

udMapping = { 
    # core arguments
    "nsubj":"subj","csubj":"subj",
    "obj":"comp","ccomp":"comp",
    "iobj":"comp","xcomp":"comp",
    # non-core dependents
    "obl":"comp","advcl":"mod","advmod":"mod","aux":"mod",
    "vocative":"mod","discourse":"mod","cop":"mod",
    "expl":"mod","mark":"mod",
    # nominal dependents
    "nmod":"mod","acl":"comp","amod":"mod","det":"det",
    "appos":"mod","clf":"mod",
    "nummod":"mod","case":"mod",
    # coordination
    "conj":"mod","cc":"mod",
    # multiword expressions
    "fixed":"mod","flat":"mod","compound":"mod",
    # loose
    "list":"mod","parataxis":"mod","dislocated":"mod",
    # special
    "orphan":"mod","goeswith":"mod","reparandum":"mod",
    # other
    "punct":"mod","root":"root","dep":"comp",
}

def getOption(featName,allowed,feat):
    if feat not in allowed:
        print("*** unknown feature for",featName,":",feat)
        return None
    return allowed[feat]

def ud2pyrdeprel(udDeprel):
    if ":" in udDeprel:# ignore colon and after
        udDeprel = udDeprel[:udDeprel.index(":")]
    if udDeprel in udMapping:
        return udMapping[udDeprel]
    print("*** unknown UD deprel : %s",udDeprel)
    return "comp"


# combine all typ options into a single list and apply other options directly to a dependent
def applyOptions(dep,options):
    typOpts={}
    for key,val in options:
        if key=="typ":
            typOpts |= val
        else:
            getattr(dep,key)(val)
    if len(typOpts)>0:
        getattr(dep,"typ")(typOpts)
    return dep

# check if first element of list satisfies a predicate
#  if so return it otherwise None
def checkFirst(list,pred):
    return list[0] if len(list)>0 and pred(list[0]) else None

# check if last element of list satisfies a predicate
#  if so return it otherwise None
def checkLast(list,pred):
    return list[-1] if len(list)>0 and pred(list[-1]) else None

def findIndex(elems,condition):
    return next((i for i, el in enumerate(elems) if condition(el)), -1)

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
