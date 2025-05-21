from UDNode import UDNode
from UD2pyr import applyOptions, findIndex, findLemma, checkLemma, checkLast
from pyrealb import *

class UDNode_fr(UDNode):
    lemmataMap = None

    def __init__(self, word,sentence):
        super().__init__(word,sentence)
        if UDNode_fr.lemmataMap is None: # only initialize
            UDNode_fr.lemmataMap = buildLemmataMap("fr")

    def toTerminal(self,copyGenderNumber):
        def tonicPronoun(form,udLemma):
            nomList = ["je", "tu", "il", "elle", "nous", "vous", "ils", "elles"]
            accList = ["me", "te", "le", "les", "la"]
            if form in nomList or udLemma in nomList:
                return Pro("moi").c("nom")
            if form in accList or udLemma in accList:
                return Pro("moi").c("acc")
            return Pro(udLemma)

        def possessivePronoun(form,pluralPsor):
            ppTable = {
                "mien": ["mien", 1],
                "tien": ["mien", 2],
                "sien": ["mien", 3],
                "nôtre": ["nôtre", 1],
                "vôtre": ["nôtre", 2],
                "leur": ["nôtre", 3],
            }
            plurTable = {"mien": "nôtre", "tien": "vôtre", "sien": "leur"}
            if form in ppTable:
                if pluralPsor and form in plurTable:
                    form = plurTable[form]
                lemma,person = ppTable[form]
                return Pro(lemma).pe(person)
            return Pro(form)

        def possessiveDeterminer(udLemma,pluralPsor):
            pdTable = {
                "mon": ["mon", 1],
                "ton": ["mon", 2],
                "son": ["mon", 3],
                "notre": ["notre", 1],
                "votre": ["notre", 2],
                "leur": ["notre", 3],
            }
            plurTable = {"mon": "notre", "ton": "votre", "son": "leur"}
            if udLemma in pdTable:
                if pluralPsor and udLemma in plurTable:
                    udLemma = plurTable[udLemma]
                lemma,person = pdTable[udLemma]
                return D(lemma).pe(person)
            return D(udLemma)
        
        text = self.text()
        lemma = self.lemma()
        upos = self.upos()
        feats = self.feats
        # open classes
        if upos == "ADJ":
            expr = findLemma(self.lemmataMap,lemma,text,"A",A)
            if expr is None:
                if text in self.lemmataMap:
                    try: # vérifier si ça ne pourrait pas être un participe passé..
                        return self.feats2options(next(expr for expr in self.lemmataMap[text]
                                                       if (expr.isA("V") and expr.getProp("t")=="pp")),
                                                  ["Number","Gender"] if copyGenderNumber else ["Number"])
                    except StopIteration:
                        pass
                return Q(text)
            else:
                return self.feats2options(expr,["Number","Gender"] if copyGenderNumber else ["Number"])
        if upos == "ADV": return checkLemma(lemma,"Adv",Adv)
        if upos == "INTJ": return Q(text)
        if upos == "NOUN":
            expr = findLemma(self.lemmataMap,lemma,text,"N",N)
            if expr is None: return Q(text)
            else:
                return self.feats2options(expr,["Number","Gender"])
        if upos == "PROPN": return Q(self.text())
        if upos == "VERB":
            expr = findLemma(self.lemmataMap,lemma,text,"V",V)
            if expr is None: return Q(text)
            else:
                return self.feats2options(expr,
                        ["Mood","VerbForm","Tense","Person","Number","Gender"])
        if upos == "AUX":
            return self.feats2options(V(lemma),  ["Mood", "VerbForm", "Tense", "Person", "Number"])
        # closed classes
        if upos == "ADP": return checkLemma(lemma,"P",P)
        if upos == "CCONJ": return checkLemma(lemma,"C",C)
        if upos == "DET":
            if "Poss" in feats and feats["Poss"]=="Yes":
                pluralPsor = "Number_psor" in feats and feats["Number_psor"] == "Plur"
                return self.feats2options(possessiveDeterminer(lemma,pluralPsor),
                        ["Person","Person_psor","Number","Gender"] if copyGenderNumber else ["Person","Person_psor"])
            if "Definite" in feats:
                return self.feats2options(D(lemma),["Person","Number","Gender"] if copyGenderNumber else ["Person"])
            return self.feats2options(checkLemma(lemma,"D",D), ["Person", "Number", "Gender"] if copyGenderNumber else ["Person"])
        if upos == "NUM":
            nombres = ["zéro","un","deux","trois","quatre","cinq","six","sept","huit","neuf","dix"]
            if lemma in nombres:
                ix = nombres.index(lemma)
                return NO(ix).dOpt({"nat":True})
            try:
                float(lemma)
                return NO(lemma).dOpt({"raw":True})
            except ValueError:
                return Q(text)
        if upos == "PART":
            if lemma == "non" and len(feats) == 0:
                return Adv("non")
            return Q(text)
        if upos == "PRON":
            if self.hasFeature("Reflex","Yes"):
                return self.feats2options(Pro("moi").c("refl"),["Person","Number"])
            pro = None
            if self.hasFeature("Poss","Yes") and self.hasFeature("PronType","Prs"):
                pro = possessivePronoun(self.text().lower(),False)
            elif lemma == "lui":
                if self.text() == "lui":
                    return Pro("lui").tn("")
                else:
                    pro = Pro("moi")
                    if self.text().lower() in ["il","ils"]:
                        if "Case" not in feats:
                            pro.c("nom")
            if pro is None:
                pro = tonicPronoun(self.text().lower(),lemma)
            # HACK: this should be done using "lier()" with the previous self or add a new terminal
            #  but this would imply knowing the previous token, not available right now or returning a lst of tokens
            if self.text().startswith("-"):pro.b("-")
            if "Case" in feats:
                return self.feats2options(pro,["Case","Person","Gender","Number","Reflex"])
            pro = self.feats2options(pro,["Person","Person_psor","Gender","Number","Number_psor","Reflex"])
            if self.deprel() == 'nsubj':pro.c("nom")
            elif self.deprel() == "obj":pro.c("acc")
            elif self.deprel() == "iobj":pro.c("dat")
            return pro
        if upos == "SCONJ": return checkLemma(lemma,"C",C)
        if upos in ["PUNCT","SYM","X"]: return Q(text)
        print("upos inconnu",upos)
        return Q(text)

    # modify the UD structure to better reflect the structure expected by pyrealb
    def toDependent(self,copyGenderNumber):
        # check coordination
        if findIndex(self.right,lambda e:e.deprel()=="conj")>=0:
            return self.processCoordination([],copyGenderNumber)

        sentOptions = self.getSentOptions()
        res = self.toDependent_common(sentOptions,copyGenderNumber)
        if res is not None: return res
        cmpTenses = {"Pres":("Ppc","Ppce"),
                     "Imp": ("Ppq","Ppqe"),
                     "Past":("Ppa","Ppae"),
                     "Fut": ("Pfa","Pfae")}

        if self.upos() in ["VERB", "AUX"]:
            if self.hasFeature("Tense", "Past") and self.hasFeature("VerbForm", "Part"):
                for i in range(0, len(self.left)):
                    leftChild = self.left[i]
                    if leftChild.upos() == "AUX" and leftChild.hasFeature("VerbForm", "Fin"):
                        t = leftChild.getFeature("Tense")
                        if t in cmpTenses:
                            self.feats["Tense"] = cmpTenses[t][0 if leftChild.lemma() == "avoir" else 1]
                            del self.feats["VerbForm"]
                            self.left.pop(i) # remove aux
                            # check for advmod - ADV before the verb and the old auxiliary
                            # set its position to "right"
                            for k in range(i,len(self.left)):
                                if self.left[k].deprel()=="advmod" and self.left[k].upos=="ADV":
                                    self.left[k].isLeft=False
                            break

        # remove "se" in front of "essentiellement reflexif" verb that will be regenerated by pyrealb
        if self.upos() == "VERB":
            lemmaInfos = getLemma(self.lemma())
            if lemmaInfos is not None and "V" in lemmaInfos and "pat" in lemmaInfos["V"]:
                pat = lemmaInfos["V"]["pat"]
                if isinstance(pat,list) and len(pat)==1 and pat[0]=="réfl":
                    idx = findIndex(self.left,lambda e:e.upos()=="PRON" and e.hasFeature("Reflex","Yes"))
                    if idx>=0:
                        self.left.pop(idx)

        headTerm = self.toTerminal(copyGenderNumber)
        return applyOptions(self.childrenDeps(headTerm,copyGenderNumber), sentOptions)

    # generate options in the form of a lst of (name of optionFunction,parameter)
    def getSentOptions(self):
        # check for a "ne" ... "pas" in both left and right dependents
        advs = []
        neIdx = None

        # find all adverbs, keeping track of "ne"
        # check negation...
        for deps in [self.left, self.right]:
            for i, node in enumerate(deps):
                if node.deprel() == "advmod" and node.upos() == "ADV":
                    if node.lemma() == "ne": neIdx = len(advs)
                    advs.append((deps, i))
        if neIdx is not None:  # possible negation
            for j in range(neIdx + 1, len(advs)):
                deps, i = advs[j]
                if deps[i].lemma() in ["pas", "jamais", "plus", "guère"]:  # negation foud
                    negParam = deps[i].lemma()
                    if negParam == "pas": negParam = True
                    deps.pop(i)
                    depsNe, iNe = advs[neIdx]
                    depsNe.pop(iNe)
                    return self.getSentOptions()+[("typ", {"neg": negParam})]

        # check for interrogative with final ? and remove an expl:subj pronoun to the right
        if checkLast(self.right,lambda e: e.lemma() == "?") is not None:
            dep,idx = self.findDeprelUpos("expl:subj","PRON")
            if dep is not None:
                dep.pop(idx)            # remove expletive pronoun subject
                self.right.pop()        # remove "?"
                return self.getSentOptions()+[("typ", {"int": "yon"})]

        return []
