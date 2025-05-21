#!/usr/bin/env python3

# Implantation de la contrainte OULIPO S+7
#       https://www.oulipo.net/fr/contraintes/s7
#    La méthode S+7 consiste à remplacer chaque substantif (S) d’un texte préexistant par
#    le septième substantif trouvé après lui dans un dictionnaire (S+7) donné.

# - parser la phrase française avec Stanza
# - transformer les lemmes des noms/verbes avec le 7e mot de la même catégorie selon le dictionnaire
# - transformer ces dépendances en pyrealb
# - regénérer la phrase

# description de l'API de stanza: https://stanfordnlp.github.io/stanza/data_objects.html

import stanza
import re, sys, argparse

from pyrealb import *
from UDNode_fr import UDNode_fr
from UDNode_en import UDNode_en
from levenshtein import getLevenshteinOps, applyEdits, expandContractions

nouns = None
verbs = None
auxiliaries = None
adjectives = None

trace = True

def setLang(lang):
    load(lang,True)
    global nlp,nouns,verbs,adjectives,auxiliaries
    nouns = []
    verbs = []
    adjectives = []
    # create lst keeping lexicon order
    for lemma,infos in getLexicon(lang).items():
        if "N" in infos: nouns.append(lemma)
        if "V" in infos: verbs.append(lemma)
        if "A" in infos: adjectives.append(lemma)
    if lang == "en":
        auxiliaries = ["have","be","do","will"]
    else:
        auxiliaries = ["avoir","être"]
    # initialize Stanza
    processors='tokenize,pos,lemma,depparse'
    if lang == "fr": processors+=",mwt"
    nlp = stanza.Pipeline(lang,processors=processors,download_method=None,verbose=False)
    print("Stanza loaded" if lang=="en" else "Stanza chargé")
    return nlp

def makeDocTree(nlp,text):
    lang = getLanguage()
    doc = nlp(text)
    if trace: print("End of Stanza parsing" if lang == "en" else "Analyse par Stanza terminée")
    for sentence in doc.sentences:
        nodes = []
        root = None
        for word in sentence.words:
            nodes.append((UDNode_en if lang=="en" else UDNode_fr)(word,sentence))
        for node in nodes:
            id = node.id()
            head = node.head()
            if head == 0:
                root = node
            else:
                node.parent = nodes[head-1]
                if id < head:
                    nodes[head-1].left.append(node)
                else:
                    nodes[head-1].right.append(node)
        setattr(sentence,"root",root) # add a new sentence property
    return doc

def showCONLL(sentence):
    def c(val):
        if val is None: return "_"
        if isinstance(val, int): return str(val)
        return val

    print("# sent_id =",sentence.index)
    print("# text =",sentence.text.replace("\n"," "))
    for word in sentence.words:
        print("\t".join([c(word.id), word.text, word.lemma, c(word.upos), c(word.xpos),
                         c(word.feats), c(word.head), c(word.deprel), c(word.deps), "_"]))

def s_plus(n,word,lemmas):
    try:
        idx = lemmas.index(word)
        return lemmas[(idx+n)%len(lemmas)]
    except ValueError:
        return word

def isIntransitive(lemma):
    v_infos = getLemma(lemma)["V"]
    return "pat" in v_infos and len(v_infos["pat"])==1 and v_infos["pat"][0]=="intr"

def shift(n,pyr_expr):
    terminal = pyr_expr.terminal
    lemma = terminal.lemma
    if terminal.isA("N"):
        new_lemma = s_plus(n,lemma,nouns)
        terminal.setLemma(new_lemma)
        # special cases
        if terminal.isFr():
            new_gender = getLemma(new_lemma)["N"]["g"]
            # forcer le genre du nouveau s'il est différent du genre actuel
            if new_gender != terminal.getProp("g"):
                terminal.g(new_gender)
        else:
            if getLemma(new_lemma)["N"]["cnt"] == "no" and terminal.getProp("n") == "p":
                terminal.setProp("n","s")   # force singular for an uncountable noun
    elif terminal.isA("V") and lemma not in auxiliaries:
        new_lemma = s_plus(n,lemma,verbs)
        # special case
        if terminal.isFr() and terminal.getProp("t") == "pp":
            while isIntransitive(new_lemma):  # find next non French intransitive verb...
                new_lemma = s_plus(1,new_lemma,verbs)
        terminal.setLemma(new_lemma)
    elif terminal.isA("A"):
        terminal.setLemma(s_plus(n,lemma,adjectives))
    for dep in pyr_expr.dependents:
        shift(n,dep)

def realize(expr):
    return re.sub("^—","— ",expr.clone().realize().replace(" , ",", ").replace(" -","-"))

def process(nlp,text, n=7, showParse=False, showDiff=False):
    nbDiffs = 0
    nbSentences = 0
    # Constituent.exceptionOnWarning = True # stop in case realization error
    # if n=0 then only reproduce original text
    doc = makeDocTree(nlp,text)   # parse text to get UD for each sentence
    for sentence in doc.sentences: # process each sentence
        racine = sentence.root
        original_text = sentence.text.replace("\n"," ")
        if showParse:
            showCONLL(sentence)
            print(sentence.root.pp())
            if not sentence.root.isProjective():
                print("*** Not projective dependencies")
        if len(racine.right)>0 : # remove ending full stop, it will be regenerated by pyrealb
            last=racine.right[-1]
            if last.deprel() == "punct" and last.lemma() == ".":
                racine.right.pop()
        try:
            print("text:",original_text)  # show original text
            pyr_expr = racine.toDependent(n==0) # create pyrealb expression
            if pyr_expr.isA("coord"): # if root is a coord, add a dummy root, so that realization will be done correctly
                pyr_expr = root(Q(""),pyr_expr)
            if showParse: print(pyr_expr.toSource(0))           # show pyrealb expression
            realized_text = realize(pyr_expr)
            print("TEXT:",realized_text)                # show realization of the pyrealb expression
            nbSentences += 1
            if showDiff:
                # compute differences
                original_text = original_text.strip().split(" ")
                if getLanguage() == "en": # expand English contraction in source...
                    original_text = expandContractions(original_text)
                realized_text = realized_text.strip().split(" ")
                (editDist, edits) = getLevenshteinOps(original_text, realized_text)
                if editDist>0:
                    # print("edit distance:" + str(editDist) + ":" + str(edits))
                    nbDiffs += 1
                    print("DIFF:",applyEdits(edits, original_text, realized_text," "))
                    # print(pyr_expr.toSource(0))
        except PyrealbException as exc:
            print("*** Realisation exception:",exc)
            print("-" * 10)
            continue
        if n>0:
            shift(n,pyr_expr)                     # transform pyrealb expression
            print(f"S+{n}:",realize(pyr_expr))             # show "shifted" text
            if showParse: print(pyr_expr.toSource(0))  # show pyrealb expression
        print("-"*10)
    print(len(doc.sentences),"sentences")
    if showDiff:
        print(nbDiffs,"differences",round(nbDiffs*100/len(doc.sentences)),"%")
    print("="*10)

# by default ignore lines starting with #
def getText(fileName,transform=lambda l: None if l.startswith("#") else l):
    lines = open(fileName,"r").readlines()
    return "".join(l for l in map(transform,lines) if l is not None)

def process_arguments():
    parser = argparse.ArgumentParser(description="S_plus_7 : an OULIPIAN word game.\n"
                                     "Each content word is replaced by the seventh content "
                                     "noun that follows it in the pyrealb lexicon.")
    parser.add_argument("lang",help="language of the input",choices=["en","fr"])
    parser.add_argument('infile', nargs='?', help="text to transform, stdin by default",
                        type=argparse.FileType('r'),default = sys.stdin)
    parser.add_argument("-n",help="number of words to shift in the realized text, 7 by default;\n "
                                  "if n=0, only regenerate the input", type=int, default=7)
    parser.add_argument("-p","--showParse", help="show parsing result of the input",action="store_true")
    parser.add_argument("-d","--showDiff", help="display differences between original and regenerated sentence",
                        action="store_true")
    args = parser.parse_args()
    n = args.n
    showParse = args.showParse
    showDiff = args.showDiff
    nlp=setLang(args.lang)
    # print(args.lang,args.file,n,showParse,showDiff)
    process(nlp,"".join(args.infile.readlines()),n,showDiff=showDiff,showParse=showParse)

def development_tests():
    # tests directly from within PyCharm
    nlp = setLang("fr")
    # utile pour tester une seule phrase montrant tous les détails
    # process(nlp,"""
    # Elle se trouva fort dépourvue quand la bise fut venue.
    # """,7,showParse=True,showDiff=True)

    #  tester le contenu de fichiers
    process(nlp,getText("texts/Cigale_Fourmi.txt"),7)
    # process(nlp, getText("texts/Etranger.txt"),7)
    # process(nlp,getText("texts/UD-2.13-fr_gsd-test.txt"),0,showDiff=True)
    # process(nlp,getText("texts/tests_fr.txt"),0)
    # process(nlp,getText("texts/coordination_tests_fr.txt"),0)

    nlp = setLang("en")
    # useful for testing a single sentence showing all details
    process(nlp,"""
    He had a chance to present the company's story.
""",7,showParse=True, showDiff=True)

    # test content of a file
    # process(nlp,getText("texts/Grasshopper_Ant.txt"), 7)
    # process(nlp,getText("texts/Old_man_with_beard.txt"),0)
    # process(nlp,getText("texts/tests_en.txt"),0)
    # process(nlp,getText("texts/UD-2.13-en_ewt-test-extract.txt"),0,showDiff=True)


if __name__ == '__main__':
    if len(sys.argv) > 1:  # called from the command line...
        process_arguments()
        sys.exit(0)
    development_tests()
