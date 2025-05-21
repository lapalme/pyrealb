from UDNode import UDNode
from UD2pyr import ud2pyr_deprel, applyOptions, findIndex, findLemma, checkLemma
from pyrealb import *

class UDNode_en(UDNode):
    lemmataMap = None

    def __init__(self, word,sentence):
        super().__init__(word,sentence)
        if UDNode_en.lemmataMap is None: # only initialize
            UDNode_en.lemmataMap = buildLemmataMap("en")

    def toTerminal(self,copyGenderNumber):
        def tonicPronoun(udLemma):
            tpTable = {
                "i": "me",
                "I": "me",
                "he": "him",
                "she": "her",
                "we": "us",
                "they": "them"
            }
            if udLemma in tpTable:
                pro = Pro(tpTable[udLemma]).c("nom")
                if udLemma in '"iI':pro.pe(1)
                return pro
            return Pro(udLemma)

        def possessivePronoun(udLemma):
            ppTable = {
                "mine":"me",
                "his":"him",
                "hers":"her",
                "its":"me",
                "ours":"us",
                "yours":"you",
                "theirs":"them"
            }
            if udLemma in ppTable:
                pro = Pro(ppTable[udLemma]).c("gen")
                if udLemma == "mine":pro.p(1)
                return pro
            # elif udLemma == "my": #strangely UD tags this determiner as a pronoun...
            #     return D("my")
            return None

        def possessiveDeterminer(udLemma):
            options = {
                "my": [1, "s", None],
                "I": [1, "s", None],
                "your": [2, "s", None],
                "his": [3, "s", "m"],
                "he": [3, "s", "m"],
                "her": [3, "s", "f"],
                "she": [3, "s", "f"],
                "its": [3, "s", "n"],
                "it": [3, "s", "n"],
                "our": [1, "p", None],
                "we": [1, "p", None],
                "your": [2, "p", None],
                "you": [2, "p", None],
                "their": [3, "p", None],
                "they": [3, "p", None],
            }
            if udLemma in options:
                pe,n,g = options[udLemma]
                det = D("my").pe(pe).ow(n)
                if g is not None: det.g(g)
                return det
            return None

        text = self.text()
        lemma = self.lemma()
        upos = self.upos()
        feats = self.feats
        # open classes
        if upos == "ADJ":
            if self.hasFeature("NumType","Ord"):
                try:
                    ix = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
                          "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventen", "eighteen",
                          "nineteen", "twenty"].index(lemma)
                    return NO(ix).dOpt({"ord":True})
                except ValueError:
                    return Q(text)
            expr = findLemma(self.lemmataMap,lemma,text,"A",A)
            if expr is None:
                return Q(text)
            else:
                return self.feats2options(expr,["Number","Degree"])
        if upos == "ADV":
            if self.hasFeature("PronType","Rel"): return checkLemma(lemma,"C",C)
            if self.hasFeature("PronType","Int"): return checkLemma(lemma,"C",C) #  should update lexicon to add Adv et remove Pro
            return checkLemma(lemma,"Adv",Adv)
        if upos == "INTJ": return Q(text)
        if upos == "NOUN":
            expr = findLemma(self.lemmataMap,lemma,text,"N",N)
            if expr is None:
                return Q(text)
            else:
                return self.feats2options(expr,["Number","Gender"])
        if upos == "PROPN":
            # check if it exists in the lexicon as a noun... (e.g. days of week or months)
            infos = getLemma(lemma)
            if infos is not None and "N" in infos:
                return N(lemma)
            return Q(text)
        if upos == "VERB":
            expr = findLemma(self.lemmataMap,lemma,text,"V",V)
            if expr is None:
                return Q(text)
            else:
                return self.feats2options(expr,["Mood","VerbForm","Tense","Person","Number"])
        if upos == "AUX":
            return self.feats2options(V(lemma),  ["Mood", "VerbForm", "Tense", "Person", "Number"])
        # closed classes
        if upos == "ADP": return checkLemma(lemma,"P",P)
        if upos == "CCONJ": return checkLemma(lemma,"C",C)
        if upos == "DET":
            definite = self.getFeature("Definite")
            if definite is not None:
                return D("the" if definite == "Def" else "a")
            if self.getFeature("PronType") in ["Dem","Ind","Tot","Neg"]:
                return D(lemma)
            if self.hasFeature("Poss","Yes") and self.hasFeature("PronType","Prs"):
                return possessiveDeterminer(lemma)
            print("*** Strange determiner:", lemma)
            return checkLemma(lemma,"D",D)
        if upos == "NUM":
            if self.hasFeature("NumType","Card"):
                try:
                    ix = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
                          "ten"].index(lemma)
                    return NO(ix).dOpt({"nat":True})
                except ValueError:
                    return Q(text)
            try:
                float(lemma)
                return NO(lemma).dOpt({"raw":True})
            except ValueError:
                return Q(text)
        if upos == "PART":
            if lemma == "not" and len(feats) == 0:
                return Adv("not")
            return Q(text)
        if upos == "PRON":
            pro = None
            if self.hasFeature("Poss","Yes") and self.hasFeature("PronType","Prs"):
                pro = possessivePronoun(lemma)
                # many possessive determiner are coded as possessive pronouns
                # https://universaldependencies.org/u/feat/PronType.html#prs-personal-or-possessive-personal-pronoun-or-determiner
                if pro is None and self.hasFeature("Case","Gen"):
                    posDet = possessiveDeterminer(lemma)
                    if posDet is not None: return posDet
            if self.hasFeature("Reflex","Yes"):
                if lemma.endswith("self"):
                    return Pro(lemma[:-4]).tn("refl")
                elif lemma.endswith("selves"):
                    return Pro("us" if lemma=="ourselves" else lemma[:-6]).tn("refl")
            if pro is None:
                pro = tonicPronoun(lemma)
            if self.hasFeature("Case",None):
                return self.feats2options(pro,["Case","Person","Gender","Number"])
            else:
                return self.feats2options(pro,["Person","Gender","Number"])
        if upos == "SCONJ":
            if lemma == "that":return C("that")
            if lemma == "once": return Adv("once")
            return checkLemma(lemma,"C",C)
        if upos in ["PUNCT","SYM","X"]: return Q(text)
        print("unknown upos",upos)
        return Q(text)

    # modify the UD structure to better reflect the structure expected by pyrealb
    def toDependent(self,copyGenderNumber):
        # check coordination
        if findIndex(self.right,lambda e:e.deprel()=="conj")>=0:
            return self.processCoordination([],copyGenderNumber)

        sentOptions = self.getSentOptions()
        res = self.toDependent_common(sentOptions,copyGenderNumber)
        if res is not None: return res

        headTerm = self.toTerminal(copyGenderNumber)
        if headTerm.isA("N","Q"):
            # check 's possessive
            if len(self.right)==1 and self.right[0].lemma() == "'s":
                self.right.pop()
                headTerm.poss()
        elif headTerm.isA("V"):
            # check infinitive (remove the PART and change infinitive to "b-to")
            if len(self.left)>0 and self.left[-1].lemma() == "to" and headTerm.getProp("t") == "b":
                self.left.pop()
                headTerm.t("b-to")
            # check future tense
            dep,idx = self.findDeprelUpos("aux","AUX")
            if dep is not None and dep[idx].lemma()=="will":
                w = dep.pop(idx)
                headTerm.t("c" if w.hasFeature("Tense","Past") else "f")
        # process the rest by the common traversal
        return applyOptions(self.childrenDeps(headTerm,copyGenderNumber), sentOptions)

    # generate options in the form of a lst of (name of optionFunction,parameter)
    def getSentOptions(self):
        def checkNegation():
            dep, idx = self.findDeprelUpos("advmod", "PART")
            if dep is not None:
                if dep[idx].lemma() == "not":
                    dep.pop(idx)
                    return [("typ", {"neg": True})]
            return []

        modals = {
                 "can": "poss",
                 "could": "poss",
                 "may": "perm",
                 "might": "perm",
                 "shall": "nece",
                 "should": "nece",
                 "would": "will",
                 "must": "obli",
                 "ought": "obli",
                 # "will":"will", # will is most often used for future
        }

        # check for a modal
        dep,idx = self.findDeprelUpos("aux","AUX")
        if dep is not None:
            lemma = dep[idx].lemma()
            if lemma in modals:
                modal = modals[lemma]
                self.feats = dep[idx].feats # set verb feature to those of aux
                dep.pop(idx)  # remove aux
                options = [("typ",{'mod':modal})]
                if lemma in ["could","might","should","would","ought"]:
                    options.insert(0,("t","ps"))
                # check for negated modal
                options += checkNegation()
                return self.getSentOptions()+options

        # check for progressive
        if self.hasFeature("VerbForm","Prog") or \
                (self.hasFeature("VerbForm","Part") and self.hasFeature("Tense","Pres")):
            dep,idx = self.findDeprelUpos("aux","AUX")
            if dep is not None and dep[idx].lemma()=="be":
                self.feats = dep[idx].feats
                dep.pop(idx)
                options = [("typ",{"prog":True})]+checkNegation()
                return self.getSentOptions()+options

        # check for perfect
        if self.upos()=="VERB":
            dep,idx = self.findDeprelUpos("aux","AUX")
            if dep is not None and dep[idx].lemma() == "have":
                self.feats = dep[idx].feats # copy aux features to verb
                dep.pop(idx)  # remove auxiliary
                options = [("typ",{"perf":True})]+checkNegation()
                return self.getSentOptions()+options

        # check for some interrogation types
        dep,idx = self.findDeprelUpos("advmod","ADV")
        if dep is not None:
            adv = dep[idx].lemma()
            if adv in ["why","how","when"]:
                dep1,idx1 = self.findDeprelUpos("punct","PUNCT")
                if dep1 is not None and dep1[idx1].lemma() == "?":
                    dep1.pop(idx1)
                    dep.pop(idx)
                    options = [("typ",{"int":"whn" if adv=="when" else adv})]+checkNegation()
                    return self.getSentOptions()+options

        # check for yon interrogative
        dep,idx = self.findDeprelUpos(["aux","cop"],"AUX")
        if dep is not None and dep[idx].lemma() in ["do","have","be"]:
            dep1,idx1 = self.findDeprelUpos("punct","PUNCT")
            if dep1 is not None and dep1[idx1].lemma()=="?":
                dep1.pop(idx1)
                if dep[idx].lemma() == "do":
                    self.feats = dep[idx].feats
                    dep.pop(idx)
                options = [("typ",{"int":"yon"})]+checkNegation()
                return self.getSentOptions()+options

        # check for sole negation
        dep,idx = self.findDeprelUpos("advmod","PART")
        if dep is not None:
            if dep[idx].lemma() == "not":
                dep1,idx1 = self.findDeprelUpos("aux","AUX")
                if dep1 is not None and dep1[idx1].lemma() in ["do"]:
                    dep.pop(idx)
                    self.feats=dep1[idx1].feats  # copy to the verb the features from the removed auxiliary
                    dep1.pop(idx1) # remove auxiliary
                    return self.getSentOptions()+[("typ",{"neg":True})]

        return []


