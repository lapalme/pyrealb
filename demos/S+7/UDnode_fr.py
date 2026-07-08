from UDnode import UDnode,findIndex
from ud2pyr import applyOptions, checkLast, findIndex, findLemma, checkLemma
from pyrealb import *
load("fr")

def isNaN(s):
    try:
        float(s)
        return False
    except ValueError:
        return True


class UDnode_fr(UDnode):
    lemmataMap = None
    def __init__(self, word):
        super().__init__(word)
        if UDnode_fr.lemmataMap is None: # only initialize once
            UDnode_fr.lemmataMap = buildLemmataMap("fr")

    def toTerminal(self,copyGenderNumber):
        def tonicPronoun(form,udLemma):
            nomList = ["je","tu","il","elle","nous","vous","ils","elles"]
            accList = ["me","te","le","les","la"]
            if form in nomList or udLemma in nomList:
                return Pro("moi").c("nom")
            if form in accList or udLemma in nomList:
                return Pro("moi").c("acc")
            return Pro(udLemma)

        def possessivePronoun (form,pluralPsor):
            ppTable={
                "mien":  ("mien", 1),
                "tien":  ("mien", 2),
                "sien":  ("mien", 3),
                "nôtre": ("nôtre",1),
                "vôtre": ("nôtre",2),
                "leur":  ("nôtre",3),
            }
            plurTable = {
                "mien":"nôtre","tien":"vôtre","sien":"leur"
            }
            if form in ppTable:
                if pluralPsor and form in plurTable:
                    form=plurTable[form]
                (lemma,person)=ppTable[form]
                return Pro(lemma).pe(person)
            return Pro(form)

        def possessiveDeterminer(udLemma,pluralPsor):
            pdTable = {
                "mon":    ("mon",  1),
                "ton":    ("mon",  2),
                "son":    ("mon",  3),
                "notre":  ("notre",1),
                "votre":  ("notre",2),
                "leur":   ("notre",3),
            }
            plurTable = {
                "mon":"notre","ton":"votre","son":"leur"
            }
            if (udLemma in pdTable):
                if pluralPsor and udLemma in plurTable:
                    udLemma = plurTable[udLemma]
                (lemma,person) = pdTable[udLemma]
                return D(lemma).pe(person)
            return D(udLemma)

        lemma = self.lemma
        match self.upos:
                # Open classes
            case "ADJ":
                expr = findLemma(self.lemmataMap, lemma, self.form, "A", A)
                if expr is None:
                    if self.form in self.lemmataMap:
                        try:  # vérifier si ça ne pourrait pas être un participe passé..
                            return self.feats2options(next(expr for expr in self.lemmataMap[self.lemma]
                                                           if (expr.isA("V") and expr.getProp("t") == "pp")),
                                                      ["Number", "Gender"] if copyGenderNumber else ["Number"])
                        except StopIteration:
                            pass

                    return Q(self.form)
                else:
                    return self.feats2options(A(lemma).pos("pre" if self.position=="l" else "post"),
                                              ["Gender","Number"] if copyGenderNumber else ["Number"])
            case "ADV":
                return checkLemma(lemma,"Adv",Adv)
            case "INTJ":
                return Q(lemma)
            case "NOUN":
                expr = findLemma(self.lemmataMap, lemma, self.form, "N", N)
                if expr is None:
                    return Q(self.form)
                else:
                    return self.feats2options(expr, ["Number", "Gender"])
            case "PROPN":
                # check if it exists in the lexicon as a noun... (e.g. days of week or months)
                infos = getLemma(lemma)
                if infos is not None and "N" in infos:
                    return N(lemma)
                return Q(lemma)
            case "VERB" | "AUX":
                expr = findLemma(self.lemmataMap, lemma, self.form, "V", V)
                if expr is None:
                    return Q(self.form)
                else:
                    return self.feats2options(V(lemma),["Mood","VerbForm","Tense","Person","Number","Gender"])
                # Closed classes
            case "ADP":
                return checkLemma(lemma,"P",P)
            case "CCONJ":
                return checkLemma(lemma,"C",C)
            case "DET":
                if self.hasFeature("Poss","Yes"):
                    return self.feats2options(possessiveDeterminer(lemma,self.hasFeature("Number_psor","Plur")),
                                        ["Person","Person_psor","Gender","Number"] if copyGenderNumber else ["Person","Person_psor"])
                definite=self.getFeature("Definite")
                if definite is not None:
                    return self.feats2options(D(lemma),["Person","Gender","Number"]if copyGenderNumber else ["Person","Person_psor"])
                return D(lemma)
            case "NUM":
                try:
                    ix = ["zéro","un","deux","trois","quatre","cinq","six","sept","huit","neuf","dix"].index(lemma)
                except ValueError:
                    ix = -1
                if ix>=0: return NO(ix).dOpt({"nat":True});
                if isNaN(lemma): return Q(lemma);
                return NO(lemma).dOpt({"raw":True})
            case "PART":
                if lemma=="not" and self.hasNoFeature():
                    return Adv("not")
                return Q(lemma)
            case "PRON":
                if self.hasFeature("Reflex","Yes"):
                    return self.feats2options(Pro("moi").c("refl"),["Person","Gender","Number"])
                if self.hasFeature("Poss","Yes") and self.hasFeature("PronType","Prs"):
                    pro=possessivePronoun(self.form.toLowerCase())
                pro = None
                if lemma=="lui":
                    if self.form=="lui":
                        return Pro("lui").tn("")
                    else:
                        pro = Pro("moi")
                        if  self.form in ["il","ils"]:
                            if not self.hasFeature("Case"):
                                pro.c("nom")
                if pro is None:
                    pro=tonicPronoun(self.form.lower(),lemma)
                # HACK: self should be done using "lier()" with the previous word or add a new terminal
                #   but self would imply knowing the previous token, not available right now or returning a list of tokens
                if self.form.startswith("-"): pro.b("-");
                if self.hasFeature("Case"):
                    return self.feats2options(pro,["Case","Person","Gender","Number","Reflex"])
                else:
                    pro = self.feats2options(pro,["Person","Person_psor","Gender","Number","Number_psor","Reflex"])
                    if (self.deprel=='nsubj'): pro.c("nom")
                    elif (self.deprel=="obj"): pro.c("acc")
                    elif (self.deprel=='iobj'): pro.c("dat");
                    return pro
            case "SCONJ":
                return checkLemma(lemma,"C",C)
            case "PUNCT" | "SYM" | "X":
                return Q(lemma)
            case _:
                print("UPOS inconnu:",self.upos)
                return Q(self.form)

    def toDependent(self,copyGenderNumber):
        cmpTenses = {"Pres": ["Ppc", "Ppce"],
                     "Imp": ["Ppq", "Ppqe"],
                     "Past": ["Ppa", "Ppae"],
                     "Fut": ["Pfa", "Pfae"]}
        subTenses = {"Pres":["Spa","Spe"],
                     "Past":["Spqa","Spqe"]}
        # check coordination
        if findIndex(self.right,lambda n:n.matches("conj","_"))>=0:
            c = self.processCoordination([],copyGenderNumber)
            if self.position=="l":c.pos("pre")
            return c

        # find sentence type
        sentOptions = self.getSentOptions()
        res = self.toDependent_common(sentOptions,copyGenderNumber)
        if res is not None: return res
        # check for "passé composé" when verb is past participle and a left child is an AUX
        #  remove AUX and add "special" tense (Ppc) to the verb for processing in toTerminal()
        if self.upos in ["VERB","AUX"]:
            if self.hasFeature("VerbForm","Part"):
                i=0
                while i < len(self.left): # cannot use a range because the list might change
                    leftChild = self.left[i]
                    if leftChild.upos == "AUX" and leftChild.hasFeature("VerbForm","Fin"):
                        t = leftChild.getFeature("Tense")
                        if t is not None:
                            mood = leftChild.getFeature("Mood")
                            if mood is not None and mood == "Sub":
                                self.setFeature("Tense",subTenses[t][0 if leftChild.lemma=="avoir" else 1])
                            else:
                                self.setFeature("Tense",cmpTenses[t][0 if leftChild.lemma=="avoir" else 1])
                            self.deleteFeature("VerbForm")
                            self.left.pop(i)
                            # check for advmod-ADV before the verb and the old auxiliary
                            # set its position after
                            for k in range(i,len(self.left)):
                                if self.left[k].deprel=="advmod" and self.left[k].upos=="ADV":
                                    self.left[k].position="r"
                        else:
                            i+=1
                    else:
                        i+=1
        if self.upos == "VERB":
            lemmaInfos = getLemma(self.lemma)
            if lemmaInfos is not None and "V" in lemmaInfos and "pat" in lemmaInfos["V"]:
                pat = lemmaInfos["V"]["pat"]
                if isinstance(pat,list) and len(pat) == 1 and pat[0] == "réfl":
                    # remove "se" in front of "essentiellement réflexif" verb that will be regenerated by jsRealB
                    idx = findIndex(self.left, lambda n:n.upos=="PRON" and n.hasFeature("Reflex","Yes"))
                    if idx>=0: self.left.pop(idx)
                elif isinstance(pat,list) and "réfl" in pat:
                    # remove reflexive pronoun and set refl typ option
                    idx = findIndex(self.left, lambda n: n.upos == "PRON" and n.hasFeature("Reflex", "Yes"))
                    if idx >= 0:
                        self.left.pop(idx)
                        sentOptions += [("typ",{"refl":True})]

        headTerm = self.toTerminal(copyGenderNumber)
        dep = applyOptions(self.childrenDeps(headTerm,copyGenderNumber),sentOptions)
        return dep

    def getSentOptions(self):
        # check for a "ne" ... "pas" in both left and right dependents
        advs = []
        neIdx = None
        for nodes in [self.left,self.right]:
            for i,node in enumerate(nodes):
                if node.deprel=="advmod" and node.upos=="ADV":
                    if node.lemma=="ne":neIdx=len(advs)
                    advs.append((nodes,i))
        if neIdx is not None: # possible negation
            # find next adverb following "ne"
            for j in range(neIdx+1,len(advs)):
                nodes,i = advs[j]
                if nodes[i].lemma in ["pas","jamais","plus","guère"]:
                    # found a negation
                    negParam = nodes[i].lemma
                    if negParam == "pas":negParam=True
                    nodes.pop(i)
                    nodesNe,iNe = advs[neIdx]
                    nodesNe.pop(iNe)
                    return self.getSentOptions()+[("typ",{"neg":negParam})]
        # check for interrogative with final ? and remove an expl:subj pronoun to the right
        if checkLast(self.right,lambda n:n.lemma=="?") is not None:
            dep,idx = self.findDeprelUpos("expl:subj","PRON")
            if idx>=0:
                dep.pop(idx)
                self.right.pop()
                return self.getSentOptions()+[("typ",{"int":"yon"})]
        return []
