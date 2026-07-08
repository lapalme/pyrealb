import re
from pyrealb import *
from ud2pyr import mood, verbform, tenses, person, person_psor, number, number_psor, case_, definite, gender, gender_psor,\
        degree, pronType, numtype, reflex, udMapping, getOption, ud2pyrdeprel, applyOptions, checkFirst, checkLast, findIndex

featRE = re.compile(r"(.*?)\[(.*?)]")
pairs = {"()":"(",
         "[]":"[",
         "{}":"{",
         "\"\"":"\"",
         "''":"'",
         "«»":"«"}

dependentFunc = {"root": root, "det": det, "subj": subj, "comp": comp, "mod": mod}

# Idéalement, ce serait une sous-classe Word de stanza, mais je n'ai pas trouvé moyen "sûr" d'y faire référence
class UDnode:
    def __init__(self,word):
        self.word   = word
        self.id     = word.id
        self.form   = word.text
        self.lemma  = word.lemma
        self.upos   = word.upos
        self.feats  = self.makeFeats(word.feats)
        self.head   = word.head
        self.deprel = word.deprel
        self.misc   = self.makeFeats(word.misc)
        self.right  = []
        self.left   = []

    def toDependent(self,copyGenderNumber):
        raise NotImplementedError("You must define 'ToDependent' in the subclass.")

    def toTerminal(self,copyGenderNumber):
        raise NotImplementedError("You must define 'toTerminal' in the subclass.")

    def makeFeats(self,featsString): # build a Dict for features
        if featsString is None or featsString == "_":
            return {}
        feats = {}
        featsElems = featsString.split("|")
        for featsElem in featsElems:
            keyVal = featsElem.split("=")
            m = featRE.match(keyVal[0])
            if m is None:
                feats[keyVal[0]] = keyVal[1]
            else:
                feats[m.group(1) + "_" + m.group(2)] = keyVal[1];
        return feats

    def addToLeftOf(self,node):
        self.parent = node
        node.left.append(self)
        self.position="l"

    def addToRightOf(self,node):
        self.parent = node
        node.right.append(self)
        self.position="r"

    def pp(self, prefix="", lr="*", middle=False):
        # fancy horizontal inorder tree print using Unicode box drawing characters
        #           https://en.wikipedia.org/wiki/Box-drawing_characters
        # CAUTION: this is quite a "hack" to get the vertical lines right
        angle = "──" if lr == "*" else "├─" if middle else "┌─" if lr == "l" else "└─"
        label = f" {self.deprel} "
        if self.isTerminal():
            label = f"──{label}→ "
        elif len(self.left) > 0 and len(self.right) > 0: # has both left and right children
            label = f"├─{label}→ "
        elif len(self.left) > 0:  # has only left children
            label = f"└─{label}→ "
        else:                     # has only right children
            label = f"┌─{label}→ "
        spaces = "  "
        vertical = "│ "
        lastRight = len(self.right) - 1
        return "\n".join(
            [n.pp(prefix + (spaces if lr == "*" or (lr == "l" and not middle) else vertical), "l", i > 0)
             for (i, n) in enumerate(self.left)] +
            [prefix + angle + label + self.form + " : " + self.upos +" : " + repr(self.lemma) +
             ("" if len(self.feats) == 0 else (" "+str(self.feats)))] +
            [n.pp(prefix + (spaces if lr == "*" or (lr == "r" and not middle) else vertical), "r", i < lastRight)
             for (i, n) in enumerate(self.right)]
        )

    # def pp_old(self,indent="",prefix=""):
    #     new_indent = indent+(len(self.deprel))*" "
    #     nbl=len(self.left)
    #     nbr=len(self.right)
    #     if nbl==0 and nbr==0: sep = "→"
    #     elif nbl>0 and nbr==0: sep = "┴"
    #     elif nbl==0 and nbr>0: sep = "┬"
    #     else: sep = "┼"
    #     res= ""
    #     for i in range(nbl-1,-1,-1):
    #         c = "┌" if i==nbl-1 else "├"
    #         res += self.left[i].pp(new_indent+(" " if nbl>0 else ""),c)+"\n"
    #     res+=((indent)+prefix+
    #           self.deprel+sep+self.upos+":"+repr(self.lemma)+
    #           ("" if len(self.feats) == 0 else (":"+str(self.feats))))+self.position
    #     for i in range(nbr):
    #         c = "└" if i == nbr-1 else "├"
    #         res += "\n"+self.right[i].pp(new_indent+("│" if nbr>0 else ""),c)
    #     return res

    def isTerminal(self):
        return len(self.left)==0 and len(self.right)==0

    def coNLL(self):
        fields = "{:C}".format(self.word).split("\t")
        return "\t".join(fields[:-1])

    def toCoNLL(self):
        return "\t".join([str(self.id),self.form,self.lemma,
                          self.options2feats(self.feats),
                          str(self.head),self.deprel])

    # check if an inorder traversal of the tree returns the ids in sequential order
    def isProjective(self):
        cnt = 1

        def check(node):
            nonlocal cnt
            for n in node.left:
                if not check(n): return False
            if node.id == cnt:
                cnt += 1
            else:
                print("*", node.id, "!=", cnt)
                return False
            for n in node.right:
                if not check(n): return False
            return True

        return check(self)


    def matches(self,dep,upos):
        if isinstance(dep,list):
            if self.deprel not in dep: return False
        elif self.deprel not in ["_",dep]: return False
        return upos == "_" or self.upos == upos

    def hasFeature(self,key,val="_"):
        if key not in self.feats: return False
        return val == "_" or self.feats[key]==val;
    
    def hasNoFeature(self):
        return len(self.feats)==0
    
    def getFeature(self,key):
        if key not in self.feats: return None
        return self.feats[key]

    def setFeature(self,key,value):
        self.feats[key] = value
        return value

    def deleteFeature(self,key):
        if key in self.feats:
            del self.feats[key]
    
    def selectFeature(self,key):
        if key in self.feats:
            val = self.feats[key]
            del self.feats[key]
            return val
        return None

    def toConstituent(self,copyGenderNumber):
        if self.isTerminal():
            return self.toTerminal(copyGenderNumber)
        return self.toDependent(copyGenderNumber)

    def options2feats(self,options):
        if len(options)==0 : return "_"
        res = []
        for key,val in options.items():
            if key == "Number_": key="Number"
            elif key.endswith("_psor"):
                key = key[:-5]+"[psor]"
            res.append(key+("" if val is None else ("="+val)))
        return "|".join(res)

    def findDeprelUpos(self,deprel,upos):
        idx = findIndex(self.left,lambda n:n.matches(deprel,upos))
        if idx>=0: return (self.left,idx)
        idx = findIndex(self.right,lambda n:n.matches(deprel,upos))
        if idx>=0: return (self.right,idx)
        return (None,-1)

    def check(self,feat,fields):
        val = self.getFeature(feat)
        if val is not None:
            return getOption(feat,fields,val)
        return None
    
    def feats2options(self,constituent,selFeats):
        if self.hasNoFeature() or constituent.isA("Q"):return constituent
        for selFeat in selFeats:
            match selFeat:
                case "Mood":
                    moodVal = self.selectFeature("Mood")
                    if moodVal is not None:
                        tense = self.selectFeature("Tense")
                        if tense is not None:
                            pyrTense = getOption(f"Mood[{moodVal}]",mood[moodVal],tense)
                            if pyrTense is not None:
                                constituent.t(pyrTense)
                        elif moodVal == "Imp":
                            constituent.t("ip")
                case "VerbForm":
                    formVal = self.selectFeature("VerbForm")
                    if formVal is not None:
                        if formVal=="Part" and self.hasFeature("Tense"):
                            pyrTense = self.selectFeature("Tense")
                            if pyrTense=="Pres": constituent.t("pr")
                            elif pyrTense=="Past":constituent.t("pp")
                        elif formVal=="Part" and not self.hasFeature("Tense"):
                            # Stanza does not always the tense for a a past participle
                            constituent.t("pp")
                        elif formVal in ["Inf","Ger"]:
                            constituent.t(verbform[formVal])
                        else:
                            tense = self.selectFeature("Tense")
                            if tense is not None:
                                pyrTense = getOption("Tense",tenses,tense)
                                constituent.t(pyrTense);
                                if formVal in ["Ppce", "Ppae","Ppqe","Pfae"]:
                                    constituent.aux("êt")
                case "Tense":
                    tense = self.selectFeature("Tense")
                    if tense is not None:
                        pyrTense = getOption("Tense",tenses,tense)
                        if pyrTense is not None:
                            constituent.t(pyrTense)
                            if tense in ["Ppce", "Ppae","Ppqe","Pfae"]:
                                constituent.aux("êt")
                case "Person":
                    pyrPe = self.check("Person",person)
                    if pyrPe is not None and constituent.getProp("pe") != pyrPe:
                        constituent.pe(pyrPe)
                case "Person_psor":
                    pyrPe_psor = self.check("Person_psor",person)
                    if pyrPe_psor is not None and constituent.getProp("pe") != pyrPe_psor:
                        constituent.pe(pyrPe_psor)
                case "Number":
                    pyrN = self.check("Number",number)
                    if pyrN is not None and constituent.getProp("n") != pyrN:
                        constituent.n(pyrN)
                case "Number_psor":
                    pyrN_psor = self.check("Number_psor",number)
                    if pyrN_psor is not None and constituent.getProp("n") != pyrN_psor:
                        constituent.n(pyrN_psor)
                case "Case":
                    pyrC = self.check("Case",case_)
                    if pyrC is not None and constituent.getProp("c") != pyrC:
                        constituent.c(pyrC)
                case "Gender":
                    pyrG = self.check("Gender",gender)
                    if pyrG is not None and constituent.getProp("g") != pyrG:
                        constituent.g(pyrG)
                case "Gender_psor":
                    pyrG_psor = self.check("Gender_psor",gender)
                    if pyrG_psor is not None and constituent.getProp("g") != pyrG_psor:
                        constituent.g(pyrG_psor)
                case "Degree":
                    pyrDeg = self.check("Degree",degree)
                    if pyrDeg is not None and constituent.getProp("f") != pyrDeg:
                        constituent.f(pyrDeg)
                case "PronType":
                    self.selectFeature("PronTYpe") # ignore
                case "NumType":
                    self.selectFeature("NumType") # ignore
                case "Reflex":
                    pyrRefl = self.check("Reflex",reflex)
                    if pyrRefl is not None and constituent.getProp("c") != pyrRefl:
                        constituent.c(pyrRefl)
                case _:
                    print("*** strange feature",selFeat,str(self))
        return constituent

    # process coordination by gathering all children (starting at the second one) in a list
    # creating phrase with the first child and then adding the CP
    def processCoordination(self,sentOptions,copyGenderNumber):
        def removeCommaCoord(n):
            # remove front comma if it exists,
            # if it is a coord return it otherwise return None
            if len(n.left)>0:
                first = n.left[0]
                if first.deprel=="punct" and first.upos=="PUNCT" and first.lemma == ",":
                    n.left.pop(0)
                elif first.deprel=="cc" and first.upos=="CCONJ":
                    n.left.pop(0)
                    return first
            return None
        # split coordination children into separate trees that will be processed separately
        # according to https://surfacesyntacticud.github.io/guidelines/u/particular_phenomena/coord/
        conjs = []; n = None; c = None
        # In UD, all conjuncts of a coordination are attached to the head of the first conjunct in a bouquet.
        right = self.right
        # remove possible ending punct
        last = checkLast(right, lambda e: e.deprel=="punct" and e.upos == "PUNCT")
        if last is not None:
            sentOptions.append(("a",last.lemma))
            right.pop()
        # process in reverse so that indices stay the same after splice
        for i in range(len(right)-1,-1,-1):
            if right[i].deprel == "conj":
                cc = removeCommaCoord(right[i])
                if cc is not None: c = cc
                conjs.append(right[i])
                right.pop(i) # remove conj link
        conjs.reverse() # recover original order

        deprel = "subj" if self.deprel in ["nsubj","csubj"] else "mod"
        conjChildren = [self.toConstituent(copyGenderNumber)]
        # combine children
        for conj in conjs:
            conjChildren.append(conj.toConstituent(copyGenderNumber))

        coordTerm = Q("") if c is None else c.toConstituent(copyGenderNumber)
        # create coordination
        if isinstance(coordTerm,Dependent):
            # some strange coordination term (e.g. "ainsi que"), create specific a constant by realizing the dependent
            coordTerm = Q(coordTerm.realize())
        coordDep = coord(coordTerm)
        for child in conjChildren:
            if isinstance(child,Terminal):
                coordDep.add(dependentFunc[deprel](child))
            else:
                if child.constType != deprel:
                    child.changeDeprel(deprel)
                coordDep.add(child)
        return applyOptions(coordDep,sentOptions)


    def childrenDeps(self,head,copyGenderNumber):
        deprel = ud2pyrdeprel(self.deprel)
        dep = dependentFunc[deprel](head)
        # check for surrounding punctuation
        first = checkFirst(self.left,lambda e:e.deprel == "punct")
        last  = checkLast(self.right,lambda e:e.deprel == "punct")
        if first is not None and last is not None:
            combined = first.lemma + last.lemma
            if combined in pairs:
                dep.ba(pairs[combined])
                self.left.pop(0)
                self.right.pop()
        elif first is not None:
            dep.b(first.lemma)
            self.left.pop(0)
        elif last is not None:
            dep.a(last.lemma)
            self.right.pop()

        for n in self.left:
            d = n.toDependent(copyGenderNumber)
            if d.isA("mod","comp"):d.pos("pre")
            dep.add(d)
        for n in self.right:
            d = n.toDependent(copyGenderNumber)
            if d.isA("det","subj"):d.pos("post")
            dep.add(d)
        # if self.position == "l" and deprel in ["mod","comp"]:
        #     dep.pos("pre")
        # if self.position == "r" and deprel in ["det","subj"]:
        #     dep.pos("post")
        return dep

    # change a cop upos to an aux (caution delicate HACK...)
    # it must be done before anything else...
    # this allows creating a sentence of the type root(V(be),subj(),comp(...)) from a dependency
    # having a noun or an adjective as root
    def move_copula(self,dep,idx):
        newAux = dep.pop(idx)
        # if newAux.hasFeature("VerbForm","Inf"): # ensure verb is congugated
        #     newAux.deleteFeature("VerbForm")
        (dep1,idx1) = self.findDeprelUpos(["nsubj","expl:subj"],"_")
        subj=None
        if idx1>=0:
            subj=dep1.pop(idx1)
            subj.addToLeftOf(newAux) # add as subject of the new auxiliary
        #  update parent of the new auxiliary
        newAux.deprel = "aux"
        self.deprel = "xcomp" # change self to the complement of the new auxiliary
        newAux.right.insert(0,self)
        self.position="r"
        # push what was before the "old" subject to the front of the new auxiliary
        # only do this for a subject in front of the current node
        if subj is not None and dep1 is self.left:
            for k in range(idx1-1,-1,-1):
                x = self.left.pop(k)
                newAux.left.insert(0,x)
                x.position="l"
        self.patent = newAux
        self.position = "r"
        return newAux

    # language independent transformations
    def toDependent_common(self,sentOptions,copyGenderNumber):
        def isModal(option):
            key,val = option
            if key!="typ": return False
            return "mod" in val
        # check for copula
        modalIdx = findIndex(sentOptions,isModal)
        copUpos = "AUX" if modalIdx<0 else "VERB"
        (dep,idx) = self.findDeprelUpos("cop",copUpos)
        if idx>=0:
            if idx>=1 and dep[idx-1].deprel == "mark":return None # special case of "d'être" should not be toucher
            newAux = self.move_copula(dep,idx)
            return applyOptions(newAux.toDependent(copyGenderNumber),sentOptions)
        if len(self.left)>0:
            # check for simple prepositional phrase
            firstPrep = checkFirst(self.left,lambda e:e.deprel in ["case","mark"] and e.upos == "ADP")
            if firstPrep is not None:
                prep = firstPrep.lemma
                self.left.pop(0)
                expr = mod(P(prep),self.toDependent(copyGenderNumber))
                return applyOptions(expr,sentOptions)
            # check for subordinate clause
            first = checkFirst(self.left,lambda e: e.deprel == "mark" and e.upos == "SCONJ")
            if first is not None:
                conj = first.lemma
                self.left.pop(0)
                expr = applyOptions(self.toDependent(copyGenderNumber),sentOptions)
                # expr.pos("post")# HACK: force post after the conjonction
                return comp(C(conj),expr.pos("post"))


