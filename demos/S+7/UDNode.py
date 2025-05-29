from UD2pyr import *

class UDNode:
    def __init__(self,word,sentence):
        self.word = word
        self.sentence = sentence
        self.feats = makeFeats(word)
        self.left = []
        self.right = []
        self.isLeftChild = True if word.head==0 else word.id < word.head
        self.parent = None

    def __str__(self):
        return f"{self.lemma()}:{self.upos()}:{self.deprel()}"

    def id(self): return self.word.id
    def text(self): return self.word.text
    def lemma(self): return self.word.lemma
    def upos(self): return self.word.upos
    def deprel(self): return self.word.deprel
    def head(self): return self.word.head

    def getFeature(self, key):
        return self.feats[key] if key in self.feats else None

    def hasFeature(self,key,val):
        return key in self.feats and (val is None or self.feats[key] == val)

    def deleteFeature(self,key):
        if key in self.feats:
            del self.feats[key]

    def selectFeature(self,key):
        if key in self.feats:
            val = self.feats[key]
            del self.feats[key]
            return val
        return None

    def showLemma(self):
        return f"{self.lemma()}:{self.upos()}:{self.feats}"

    def pp(self, prefix="", lr="*", middle=False):
        # fancy horizontal inorder tree print using Unicode box drawing characters
        #           https://en.wikipedia.org/wiki/Box-drawing_characters
        # CAUTION: this is quite a "hack" to get the vertical lines right
        angle = "──" if lr == "*" else "├─" if middle else "┌─" if lr == "l" else "└─"
        label = f" {self.deprel()} "
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
            [prefix + angle + label + self.text() + " : " + self.showLemma()] +
            [n.pp(prefix + (spaces if lr == "*" or (lr == "r" and not middle) else vertical), "r", i < lastRight)
             for (i, n) in enumerate(self.right)]
        )

    def isTerminal(self): return len(self.left)==0 and len(self.right)==0

    # check if an inorder traversal of the tree returns the ids in sequential order
    def isProjective(self):
        cnt = 1

        def check(node):
            nonlocal cnt
            for n in node.left:
                if not check(n): return False
            if node.id() == cnt:
                cnt += 1
            else:
                print("*",node.id(),"!=",cnt)
                return False
            for n in node.right:
                if not check(n): return False
            return True
        return check(self)

    def feats2options(self,constituent,selFeats):
        feats = self.feats
        if len(feats) == 0 or constituent.isA("Q"): return constituent

        # simple check on feature used for many cases below
        def check(feat, fields):
            if feat in feats:
                val = feats[feat]
                return getOption(feat, fields, val)

        for selFeat in selFeats:
            if selFeat == "Mood":
                moodVal = self.selectFeature("Mood")
                if moodVal is not None:
                    tense = self.selectFeature("Tense")
                    if tense is not None:
                        pyrTense = getOption(f"Mood[{moodVal}]", mood[moodVal], tense)
                        if pyrTense is not None:
                            constituent.t(pyrTense)
                    elif moodVal == "Imp":
                        constituent.t("ip")
                        self.deleteFeature("VerbForm")
            elif selFeat == "VerbForm":
                    formVal = self.selectFeature("VerbForm")
                    if formVal == "Part" and "Tense" in feats:
                        pyrTense = self.selectFeature("Tense")
                        if pyrTense == "Pres":
                            constituent.t("pr")
                        elif pyrTense == "Past":
                            constituent.t("pp")
                    elif formVal in ["Inf", "Ger"]:
                        constituent.t(verbform[formVal])
                    else:
                        tense = self.selectFeature("Tense")
                        if tense is not None:
                            pyrTense = getOption("Tense", tenses, tense)
                            if pyrTense is not None:
                                constituent.t(pyrTense)
                                if pyrTense in ["Ppce", "Ppae","Ppqe","Pfae"]:
                                    constituent.aux("êt")
            elif selFeat == "Tense":
                tense1 = self.selectFeature("Tense")
                if tense1 is not None:
                    pyrTense = getOption("Tense", tenses, tense1)
                    if pyrTense is not None:
                        constituent.t(pyrTense)
                        if tense1 in ["Ppce", "Ppae","Ppqe","Pfae"]:
                            constituent.aux("êt")
            elif selFeat == "Person":
                pyrPe = check("Person", person)
                if pyrPe and constituent.getProp("pe") != pyrPe: constituent.pe(pyrPe)
            elif selFeat == "Person_psor":
                pyrPe = check("Person_psor", person)
                if pyrPe and constituent.getProp("pe") != pyrPe: constituent.pe(pyrPe)
            elif selFeat == "Number":
                pyrN = check("Number", number)
                if pyrN and constituent.getProp("n") != pyrN: constituent.n(pyrN)
            elif selFeat == "Number_psor":
                pyrN = check("Number_psor", number)
                if pyrN and constituent.getProp("n") != pyrN: constituent.n(pyrN)
            elif selFeat == "Case":
                pyrC = check("Case", case_)
                if pyrC and constituent.getProp("c") != pyrC: constituent.c(pyrC)
            elif selFeat == "Definite":
                self.selectFeature("Definite") # ignore
                pass
            elif selFeat == "Gender":
                pyrG = check("Gender", gender)
                if pyrG and constituent.getProp("g") != pyrG: constituent.g(pyrG)
            elif selFeat == "Gender_psor":
                pyrG = check("Gender_psor", gender)
                if pyrG and constituent.getProp("g") != pyrG: constituent.g(pyrG)
            elif selFeat == "Degree":
                pyrDeg = check("Degree", degree)
                if pyrDeg: constituent.f(pyrDeg)
            elif selFeat == "PronType":
                self.selectFeature("PronType") # ignore
                pass
            elif selFeat == "NumType":
                self.selectFeature("NumType")  # ignore
                pass
            elif selFeat == "Reflex":
                pyrRefl = check("Reflex", reflex)
                if pyrRefl: constituent.c(pyrRefl)
            else:
                print(f"*** Strange feature: {selFeat} in {self.text()}")
        return constituent

    #  check if deprels is present with corresponding features, return (children lst,index)
    def findDeprelUpos(self, deprels, upos):
        try:
            ix = next(i for i, w in enumerate(self.left) if w.deprel() in deprels)
            if upos is None or self.left[ix].upos() == upos:
                return self.left, ix
        except StopIteration:
            pass
        try:
            ix = next(i for i, w in enumerate(self.right) if w.deprel() in deprels)
            if upos is None or self.right[ix].upos() == upos:
                return self.right, ix
        except StopIteration:
            pass
        return None, -1

    def toConstituent(self,copyGenderNumber):
        if self.isTerminal(): return self.toTerminal(copyGenderNumber)
        return self.toDependent(copyGenderNumber)

    # process coordination by gathering all children (starting at the second one) in a lst
    # creating phrase with the first child and then adding the coord
    def processCoordination(self,sentOptions,copyGenderNumber):
        def removeCommaCoord(n):
            # remove front comma if it exists,
            # if it is a coord return it otherwise return None
            if len(n.left)>0:
                first = n.left[0]
                if first.deprel()=="punct" and first.upos()=="PUNCT" and first.lemma() == ",":
                    n.left.pop(0)
                elif first.deprel()=="cc" and first.upos()=="CCONJ":
                    n.left.pop(0)
                    return first
            return None
        # split coordination children into separate trees that will be processed separately
        # according to https://surfacesyntacticud.github.io/guidelines/u/particular_phenomena/coord/
        conjs = []
        # In UD, all conjuncts of a coordination are attached to the head of the first conjunct in a bouquet.
        last = checkLast(self.right,lambda e: e.deprel() == "punct" and e.upos() == "PUNCT")
        # remove possible ending punct
        if last is not None:
            sentOptions.append(("a",last.lemma()))
            self.right.pop()
        c = None
        right = self.right
        for i in range(len(right)-1,-1,-1):
            # loop in reverse because some elements are removed and thus indices could change
            if right[i].deprel() == "conj":
                cc = removeCommaCoord(right[i])
                if cc is not None: c = cc
                conjs.append(right[i])
                right.pop(i)
        conjs.reverse() # reconver original order
        # process first
        firstConst = self.toConstituent(copyGenderNumber)
        if isinstance(firstConst,Dependent):
            deprel = firstConst.constType
            if deprel == "root":
                deprel = "subj"
        else:
            deprel = "mod"
        conjChildren = [firstConst]
        # combine children
        for conj in conjs:
            conjChildren.append(conj.toConstituent(copyGenderNumber))
        coordTerm = Q("") if c is None else c.toConstituent(copyGenderNumber)
        if isinstance(coordTerm,Dependent):
            # some strange coordination term (e.g. "ainsi que"), create specific a constant by realizing the dependent
            coordTerm = Q(coordTerm.realize())
        coordDep = coord(coordTerm)
        for child in conjChildren:
            if isinstance(child,Terminal):
                coordDep.add(globals()[deprel](child))
            else:
                child.constType = deprel
                coordDep.add(child)
        return applyOptions(coordDep,sentOptions)

    pairs = {"()":"(",
             "[]":"[",
             "{}":"{",
             "\"\"":"\"",
             "''":"'",
             "«»":"«"}

    def childrenDeps(self, head,copyGenderNumber):
        deprel = ud2pyr_deprel(self.deprel())
        dep = deprel(head)
        # check for a pair of surrounding punctuation
        first = checkFirst(self.left,lambda e:e.deprel()=="punct")
        last  = checkLast(self.right,lambda e:e.deprel()=="punct")
        if first is not None and last is not None:
            combined = first.lemma()+last.lemma()
            if combined in UDNode.pairs:
                dep.ba(UDNode.pairs[combined])
                self.left.pop(0)
                self.right.pop()
        # check left punctuation
        elif first is not None:
            dep.b(first.lemma())# add first punct as option b()
            self.left.pop(0)
        # check right punctuation
        elif last is not None:
            dep.a(last.lemma())
            self.right.pop()
        for w in self.left:
            dep.add(w.toDependent(copyGenderNumber))
        for w in self.right:
            dep.add(w.toDependent(copyGenderNumber))
        if self.isLeftChild is True and (deprel is mod or deprel is comp):
                # and not dep.terminal.isA("A","Adv"): # adjective and adverbs should not be forced into position
            dep.pos("pre")
        elif self.isLeftChild is False and (deprel is det or deprel is subj):
                # and not dep.terminal.isA("A","Adv"): # adjective and adverbs should not be forced into position
            dep.pos("post")
        return dep

    # change a cop upos to an aux (caution delicate HACK...)
    # it must be done before anything else...
    # this allows creating a sentence of the type root(V(be),subj(),comp(...)) from a dependency
    # having a noun or an adjective as root
    def move_copula(self,dep,idx):
        newAux = dep.pop(idx)
        if newAux.hasFeature("VerbForm","Inf"): # ensure verb is conjugated
            del newAux.feats["VerbForm"]
        dep1, idx1 = self.findDeprelUpos(["nsubj", "expl:subj"], None)
        subj = None
        if dep1 is not None:
            subj = dep1.pop(idx1)
            newAux.left.append(subj)  # add as subject of the new auxiliary
            subj.isLeft = True
        #  update parent of the new auxiliary
        if self.deprel() == "root":
            newAux.word.deprel = "root"
            self.sentence.root = newAux
            newAux.isLeftChild = None
            self.isLeftChild = True
        else:
            newAux.word.deprel = "aux"
            newAux.parent = self.parent  # update the parent
            newAux.isLeftChild = self.isLeftChild
            parentDep = self.parent.left if self.isLeftChild else self.parent.right
            for i in range(len(parentDep)):  # change the incoming link of the new parent
                if parentDep[i] is self:
                    parentDep[i] = newAux
        # change this self to the complement of the new auxiliary unless self is root in that case this is a subject
        self.word.deprel = "nsubj" if self.deprel() == "root" else "xcomp"
        newAux.right.insert(0, self)
        # push what was before the "old" subject to the front of the new auxiliary
        # only do this for a subject in front of the current node
        if subj is not None and dep1 is self.left:
            k= idx1 -1
            while k>=0:
                x = self.left.pop(k)
                newAux.left.insert(0,x)
                x.isLeftChild = True
                k -= 1
        self.parent = newAux
        self.isLeftChild = False
        return newAux

    def toTerminal(self,copyGenderNumber):
        raise NotImplementedError('toTerminal must be implemented in a subclass')

    def toDependent(self,copyGenderNumber):
        raise NotImplementedError('toDependent must be implemented in a subclass')

    def toDependent_common(self,sentOptions,copyGenderNumber):
        # language independent transformations
        # check for copula
        dep, idx = self.findDeprelUpos(["cop"], "AUX")
        if dep is not None:
            newAux = self.move_copula(dep,idx)
            return applyOptions(newAux.toDependent(copyGenderNumber),sentOptions)

        # check for a simple prepositional phrase
        if len(self.left)>0 and self.left[0].deprel() in ["case","mark"] and self.left[0].upos()=="ADP":
            prep = self.left[0].lemma()
            self.left.pop(0)
            return applyOptions(comp(P(prep),self.toDependent(copyGenderNumber)),sentOptions)
        return None

