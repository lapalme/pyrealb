from .Constituent import Constituent
from .Lexicon import getRules
from .utils import _getElems

class Phrase(Constituent):
    def __init__(self, constType, elements):
        from .utils import Q
        super().__init__(constType)
        if len(elements) == 0:  # check for an empty list that can be added to
            elements = []
        else:  # # transform the tuple received as star args into a list that can be modified
            elements = _getElems(elements)
        # list of elements to create the source of the parameters at the time of the call
        # cls can be different from the elements lists because of structure modifications
        self.elementsSource = []
        self.elements = []
        # add all elements except the last to the list of elements
        for i in range(0, len(elements) - 1):
            e = elements[i]
            if isinstance(e, str): e = Q(e)
            if isinstance(e, Constituent):
                e.parentConst = self
                self.elements.append(e)
                self.elementsSource.append(e)
            else:
                self.warn("bad Constituent", i + 1, type(e).__name__)
        if len(elements) > 0:
            # terminate the list with add which does other checks on the final list
            self.add(elements[-1], None, True)

    # return number of constituents
    def nbConstituents(self):
        return len(self.elements)

    # return the list of constituents
    def constituents(self):
        return self.elements

    # add a Constituent as a child of this Phrase
    def addElement(self, elem, position=None):
        from .utils import NO
        if isinstance(elem, Constituent):
            elem.parentConst = self
            # add it to the list of elements
            if position is None:
                self.elements.append(elem)
            elif isinstance(position, int) and 0 <= position <= len(self.elements):
                self.elements.insert(position, elem)
            else:
                self.warn("bad position", position, len(self.elements))
        else:
            self.warn("bad Constituent", NO(position + 1).dOpt({"ord": True}), type(elem).__name__+":"+str(elem))
        return self

    # remove a child from this Phrase and return it
    def removeElement(self, position):
        if isinstance(position, int) and 0 <= position < len(self.elements):
            elem = self.elements.pop(position)
            elem.parentConst = None
            return elem
        return self.warn("bad position", position, len(self.elements))

    # remove a child at a given position and remove the corresponding position in sourceElements
    def remove(self, position):
        import re
        elem = self.removeElement(position)
        if elem is not self: # removeElement did not raise a warning
            src = elem.toSource().replace("(","\\(").replace(")","\\)")
            srcRE = r"\.add\("+src+r"(,\d+)?\)"
            if re.search(srcRE, self.optSource) is not None:
                self.optSource=re.sub(srcRE,"",self.optSource,1)
            else:
                self.elementsSource.pop(position)
        return self

    # add a pyrealb constituent, set agreement links
    def add(self, constituent, position=None, prog=None):  # prog is True when called from within the constructor
        from .utils import Q
        def allAorN(elems, start, end):
            if start > end: (end, start) = (start, end)
            return all(el.isA("A", "N") for el in elems[start:end + 1])

        if isinstance(constituent,list):
            if len(constituent)==0: return self
            if len(constituent)==1:
                constituent=constituent[0]
            else:
                for c in constituent:
                    self.add(c,position,prog)
                return self
        if prog is None and constituent is None: return self
        if isinstance(constituent, str):
            constituent = Q(constituent)
        elif not isinstance(constituent, Constituent):
            return self.warn("bad Constituent", self.word_last(),
                             type(constituent).__name__ + ":" + str(constituent))
        if prog is None:
            self.optSource += f'.add({constituent.toSource()}{"" if position is None else ("," + str(position))})'
        else:  # call from the constructor
            self.elementsSource.append(constituent)
        constituent.parentConst = self
        self.addElement(constituent, position)
        self.linkProperties()
        ## change position of some children
        for i in range(0, len(self.elements)):
            e = self.elements[i]
            if e.isA("A"):  # check for adjective position
                idx = self.getIndex("N")
                # unless specified the position of an English adjective is pre, but is post for a French one
                if "pos" in e.props:
                    pos = e.props["pos"]  
                else:
                    pos = self.adj_def_pos()
                if idx >= 0:
                    if (pos == "pre" and i > idx) or (pos == "post" and i < idx):
                        if allAorN(self.elements, i, idx):
                            self.addElement(self.removeElement(i), idx)
        return self

    def grammaticalNumber(self):
        return self.error("grammaticalNumber must be called on NO, not a " + self.constType)

    def getHeadIndex(self, phName):
        termName = phName[:-1]  # remove P at the end of the phrase name
        headIndex = self.getIndex([phName, termName])
        if headIndex < 0:
            # should generate a warning, but experience has shown that generates too many spurious ones
            headIndex = 0
        return headIndex

    def linkProperties(self):
        #  loop over children to set the peng and taux to their head or subject
        #  so that once a value is changed this change will be propagated correctly...
        if len(self.elements) == 0: return self
        if self.isA("NP"):
            # the head is the first internal N, number with a possible NO
            # find first NP or N
            headIndex = self.getHeadIndex("NP")
            # if the first N has a poss flag, try to find the next "non possessive" N
            if self.elements[headIndex].isA("N") and self.elements[headIndex].getProp("poss"):
                for i in range(headIndex+1,len(self.elements)):
                    if self.elements[i].isA("N") and self.elements[i].getProp("poss") is None:
                        headIndex = i
                        break
            if hasattr(self.elements[headIndex],"peng"):
                # must check because getHeadIndex returns the first element when it does not find anything appropriate
                self.peng = self.elements[headIndex].peng
                for i in range(0, len(self.elements)):
                    if i != headIndex:
                        e = self.elements[i]
                        if hasattr(self, "peng"):  # do not try to modify if current peng does not exist e.g. Q
                            if e.isA("NO") and i < headIndex:  # NO must appear before the N for agreement
                                self.peng["n"] = e.grammaticalNumber()
                                # gender agreement between a French number and subject
                                e.peng["g"] = self.peng["g"]
                            elif e.isA("D","A","V"):
                                self.link_DAV_properties(e)
                                if e.isA("D"):
                                    self.check_determiner_cnt(e,self.elements[headIndex])
                            elif e.isA("CP"): # check for a coordination of adjectives and numbers
                                e.peng=self.peng
                                for el in e.elements:
                                    if el.isA("A","NO"):
                                        el.peng=self.peng
                            elif e.isA("AP","AdvP"):
                                for el in e.elements:
                                    self.link_DAV_properties(el)
                # set agreement between the subject of a subordinate or the object of a subordinate
                pro = self.getFromPath([["S", "SP"], "Pro"])
                if pro is not None:
                    v = pro.parentConst.getFromPath(["VP", "V"])
                    if v is not None:
                        self.link_subj_obj_subordinate(pro,v,pro.parentConst.subject)
        elif self.isA("VP"):
            headIndex = self.getHeadIndex("VP")  # head is the first internal V
            head_elem = self.elements[headIndex]
            self.peng = head_elem.peng
            if hasattr(head_elem,"taux"):
                self.taux = head_elem.taux
        elif self.isA("AdvP", "PP", "AP"):
            headIndex = self.getHeadIndex(self.constType)
            if hasattr(self.elements[headIndex], "peng"):
                self.peng = self.elements[headIndex].peng
        elif self.isA("CP"):
            # nothing to do, 
            # but make sure that the propagated properties exist
            Constituent.pengNO += 1
            self.peng = {
                "pengNO": Constituent.pengNO
            }
            # the information will be computed at realization time (see Phrase.prototype.cpReal)
        elif self.isA("S", "SP"):
            vpv = self.getFromPath([["", "VP"], "V"])
            if vpv is not None:
                self.taux = vpv.taux  # share tense and auxiliary of the verb
                if vpv.getProp("t") == "ip":  # do not search for subject for an imperative verb
                    return self
            iSubj = self.getIndex(["NP", "N", "CP", "Pro"])
            # determine subject
            self.subject = None
            if iSubj >= 0:
                subject = self.elements[iSubj]
                if self.isA("SP") and subject.isA("Pro"):
                    if self.should_try_another_subject(subject.lemma,iSubj):
                        # HACK: the first pronoun  should not be a subject...
                        #        so we try to find another...
                        jSubj = -1
                        for i in range(iSubj + 1, len(self.elements)):
                            if self.elements[i].isA("NP", "N", "CP", "Pro"):
                                jSubj = i
                                break
                        if jSubj >= 0:
                            subject = self.elements[jSubj]
                            self.subject = subject
                        else:
                            # finally cls generates too many spurious messages
                            # cls.warning("no possible subject found")
                            return self
                    else:
                        self.subject = subject
                self.peng = subject.peng
                vpv = self.linkPengWithSubject("VP", "V", subject)
                if vpv is not None:
                    self.taux = vpv.taux
                    self.linkAttributes(vpv,self.getFromPath([["VP"],["CP"]]),subject)
                else:
                    # check for a coordination of verbs that share the subject
                    cvs = self.getFromPath(["CP", "VP"])
                    if cvs is not None:
                        for e in self.getConst("CP").elements:
                            if isinstance(e, Phrase):  # skip possible C
                                e.linkPengWithSubject("VP", "V", subject)
                    self.check_coordinated_object()
            else:
                # finally, cls generates too many spurious messages
                # cls.warning("no possible subject found")
                pass
        else:
            self.error("linkProperties    ,unimplemented type:" + self.constType)
        return self

    def linkPengWithSubject(self, phrase, terminal, subject):
        # do not link a subject pronoun at genitive
        if subject.isA("Pro") and "c" in subject.props and subject.props["c"] == "gen": return
        pt = self.getFromPath([phrase, terminal])
        if pt is not None:
            pt.parentConst.peng = pt.peng = subject.peng
        else:
            pt = self.getFromPath([terminal])
            if pt is not None:
                pt.peng = subject.peng
        return pt

    def me(self):
        return f'{self.constType}({",".join([e.me() for e in self.elements])})'

    def setLemma(self, _terminalType):
        return self.error("***: should never happen: setLemma: called on a Phrase")

    # find the index of a Constituent type (or one of the constituents) in the list of elements
    def getIndex(self, constTypes,start=0):
        if isinstance(constTypes, str): constTypes = [constTypes]
        for i in range(start, len(self.elements)):
            if self.elements[i].isA(constTypes):
                return i
        return -1

    # find a given constituent type (or one of the constituent) in the list of elements
    def getConst(self, constTypes):
        idx = self.getIndex(constTypes)
        if idx < 0: return None
        return self.elements[idx]

    # ##### information propagation

    # find the gender, number and Person of NP elements of cls Phrase
    #   set masculine if at least one NP is masculine
    #   set plural if one is plural or more than one combined with and
    #   set person to the minimum one encountered (i.e. 1st < 2nd < 3rd) mostly useful for French 
    def findGenderNumberPerson(self, andCombination):
        g = None
        n = None
        pe = 3
        nb = 0
        for e in self.elements:
            if e.isA("NP", "N", "Pro", "Q","NO"):
                nb += 1
                propG = e.getProp("g")
                if g is None and propG is not None: g = propG
                if propG == "m": g = "m"  # masculine if one is specified
                if e.getProp("n") == "p": n = "p"
                propPe = e.getProp("pe")
                if propPe is not None and propPe < pe: pe = propPe
        if nb > 1 and andCombination:
            n = "p"
        return {"g": g, "n": n, "pe": pe}

    # ###### Phrase structure modification

    # Check if any child should be pronominalized
    # This must be done in the context of the parent, because some elements might be changed
    def pronominalizeChildren(self):
        for e in self.elements:
            if e.getProp("pro") and not e.isA("Pro"):
                # it can happen that a Pro has property "pro" set within the same expression
                e.pronominalize()

    # modify the sentence structure to create a passive sentence
    def passivate(self):
        from .utils import Pro, PP,P
        # find the subject at the start of cls.elements
        if self.isA("VP"):
            subject = None
            vp = self
        else:
            vp = self.getConst("VP")
            if vp is not None:
                if len(self.elements) > 0 and self.elements[0].isA("N", "NP", "Pro","S"):
                    subject = self.removeElement(0)
                    if subject.isA("Pro"):
                        subject = self.passive_pronoun_subject(subject)
                else:
                    subject = None
            else:
                return self.warn("not found", "VP", self.passive_context())
        # remove object (first NP or Pro within VP) from elements
        newSubject = None
        if vp is not None:
            objIdx = vp.getIndex(["NP", "Pro"])
            if objIdx >= 0:
                obj = vp.elements.pop(objIdx)
                if obj.isA("Pro"):
                    obj = obj.getTonicPro("nom")
                    if objIdx == 0:  # a French pronoun inserted by .pro()
                        objIdx = vp.getIndex("V") + 1  # ensure that the pyrealb object will appear after the verb
                elif obj.isA("NP") and obj.getProp("pro"):
                    obj = obj.getTonicPro("nom")
                # swap subject and obj
                newSubject = obj
                self.addElement(newSubject, 0)  # add object that will become the subject
                newSubject.parentConst = self  # adjust parentConst
                # make the verb agrees with the pyrealb subject (in English only, French is dealt below)
                if self.passive_should_link_subject():
                    self.linkPengWithSubject("VP", "V", newSubject)
                if subject is not None:  # insert subject where the object was
                    prep = self.passive_prep(subject.isA("S"))
                    vp.addElement(PP(P(prep, self.lang()), subject), objIdx)
            elif subject is not None:  # no object, but with a subject
                # create a dummy subject with a "il"/"it" 
                newSubject = Pro(self.passive_dummy_subject(), self.lang()).c("nom")
                # add pyrealb subject at the front of the sentence
                self.addElement(newSubject, 0)
                self.linkPengWithSubject("VP", "V", newSubject)
                vp.peng = newSubject.peng
                # add original subject after the verb to serve as an object
                vpIdx = vp.getIndex("V")
                prep = self.passive_prep(subject.isA("S"))
                if subject.isA("S"):  # take for granted that the S subject is a VP
                    pos = None
                else:
                    pos = vpIdx + 1
                vp.addElement(PP(P(prep, self.lang), subject), pos)
            self.passive_agree_auxiliary(vp,newSubject)
        else:
            return self.warn("not found", "VP", self.passive_context())

    # generic phrase structure modification for a VP, called in the .typ({...}) for .prog, .mod, .neg
    # also deals with coordinated verbs
    def processVP(self, types, key, action):
        v = self.getFromPath(["CP", "VP"])
        if v is not None:  # possibly a coordination of verbs
            for e in self.getConst("CP").elements:
                if e.isA("VP"):
                    e.processVP(types, key, action)
            return
        if key in types and types[key] != False:
            val = types[key]
            if self.isA("VP"):
                vp = self
            else:
                idxVP = self.getIndex(["VP"])
                if idxVP >= 0:
                    vp = self.elements[idxVP]
                else:
                    self.warn("not found", "VP",self.constType+'(...).typ("' + key + ":" + str(val) + '")')
                    return
            idxV = vp.getIndex("V")
            if idxV >= 0:
                v = vp.elements[idxV]
                action(vp, idxV, v, val)

    # get elements of the constituent cst2 within the constituent cst1
    def getIdxCtx(self, cst1, cst2):
        if self.isA(cst1):
            idx = self.getIndex(cst2)
            if idx >= 0: return (idx, self.elements)
        elif self.isA("S", "SP"):
            cst = self.getConst(cst1)
            if cst is not None: return cst.getIdxCtx(cst1, cst2)
        return (None, None)

    def processInt(self, types):
        from .utils import Q
        int_=types["int"]
        sentenceTypeInt = getRules()["sentence_type"]["int"]
        intPrefix = sentenceTypeInt["prefix"]
        prefix = None
        pp = None
        if int_ in ["yon", "how", "why", "muc"]:
            self.move_object(int_)
            prefix = intPrefix[int_]
        # remove a part of the sentence
        elif int_ in ["wos", "was"]:  # remove subject (first NP,N, Pro or SP)
            if self.isA("S", "SP", "VP"):
                subjIdx = self.getIndex(["NP", "N", "Pro", "SP"])
                if subjIdx is not None:
                    vbIdx = self.getIndex(["VP", "V"])
                    if vbIdx is not None and subjIdx < vbIdx:  # subject should be before the verb
                        # make sure that the verb at the third-person
                        # because now the subject has been removed
                        v = self.elements[vbIdx]
                        v.setProp("pe", 3)
                        del self.elements[subjIdx]
            prefix = intPrefix[int_]
        elif int_ in ["wod", "wad"]:  # remove direct object (first NP,N,Pro or SP in the first VP)
            cmp=None
            if self.isA("S", "SP", "VP"):
                idx, obj = self.getIdxCtx("VP", ["NP", "N", "Pro", "SP"])
                if idx is not None:
                    cmp=obj[0].parentConst.removeElement(idx)
                cmp,pp = self.passive_subject_par(cmp,pp)
                if self.passive_human_object(int,cmp):
                    # human direct object
                    prefix = "whom"
                else:
                    prefix = intPrefix[int_]
                self.move_object(int_)
        elif int_ in ["woi", "wai", "whe", "whn"]:  # remove indirect object (first PP in the first VP)
            if self.isA("S", "SP", "VP"):
                idx, ppElems = self.getIdxCtx("VP", "PP")
                prefix = intPrefix[int_]  # get default prefix
                if idx is not None:
                    # try to find a more appropriate prefix by looking at preposition in the structure
                    prep = ppElems[idx].elements[0]
                    if prep.isA("P"):
                        prep = prep.lemma
                        preps = self.preposition_list()
                        if int_ == "whe":
                            if prep in preps["whe"]: del ppElems[idx]
                        elif int_ == "whn":
                            if prep in preps["whn"]: del ppElems[idx]
                        elif prep in preps["all"]:  # "woi" | "wai"
                            prefix = prep + " " + self.interrogative_pronoun_woi(int_)
                            del ppElems[idx]
                self.move_object(int_)
        elif int_=="tag":
            # according to Antidote: Syntax Guide - Question tag
            # Question tags are short questions added after affirmations to ask for verification
            if self.isA("S", "SP", "VP"):
                self.tag_question(types)
            prefix = intPrefix[int_]
        else:
            self.warn("not implemented", "int:" + int_)
        if self.should_add_interrogative_prefix(int_):
            self.addElement(Q(prefix), 0)
            if pp is not None:  # add "par" in front of some French passive interrogative
                self.addElement(pp, 0)
                if int_ == "wad":  # replace "que" by "quoi" for French passive wad
                    self.elements[1].lemma = "quoi"
        self.a(sentenceTypeInt["punctuation"], True)

    def processTyp(self, types):
        if "pas" in types and types["pas"] != False:
            self.passivate()
        self.processTyp_verb(types)
        if "int" in types and types["int"] != False:
            self.processInt(types)
        if "exc" in types and types["exc"] == True:
            self.a(getRules()["sentence_type"]["exc"]["punctuation"], True)
        return self

    ######### Realization
    #  special case of realization of a cp for which the gender and number must be computed
    #    at realization time...

    def cpReal(self):
        res = []
        # realize coordinated Phrase by adding ',' between all elements except for the last
        # if no C is found then all elements are separated by a ","
        # TODO: deal with the Oxford comma (i.e. a comma after all elements even the last)
        idxC = self.getIndex("C")
        # take a copy of all elements except the coordinate
        elems = [e for i, e in enumerate(self.elements) if i != idxC]
        last = len(elems) - 1
        if last == -1:  # empty coordinate (ignore)
            return []
        if last == 0:  # coordination with only one element, ignore coordinate
            res = elems[0].real()
            self.setProp("g", elems[0].getProp("g"))
            self.setProp("n", elems[0].getProp("n"))
            self.setProp("pe", elems[0].getProp("pe") if elems[0].getProp("pe") is not None else 3)
            return self.doFormat(res)  # process format for the CP
        for j in range(0, last):  # insert comma after each element
            ej = elems[j]
            if idxC < 0 or j < last - 1:  # except the last if there is conjunction
                if "a" not in ej.props or "," not in ej.props["a"]:
                    ej.props["a"] = [","]
            res.extend(ej.real())
        # insert realization of C before last...
        if idxC >= 0:
            res.extend(self.elements[idxC].real())
        # insert last element
        res.extend(elems[last].real())
        # compute the combined gender and number of the coordination once children have been realized
        if idxC >= 0:
            c = self.elements[idxC]
            andC = self.and_conj()
            gn = self.findGenderNumberPerson(c.lemma == andC)
            if gn["g"] is not None:
                self.setProp("g", gn["g"])
            if gn["n"] is not None:
                self.setProp("n", gn["n"])
            self.setProp("pe", gn["pe"])
            # for the pronoun, we must override its existing properties...
            if hasattr(self, "pronoun"):
                self.pronoun.peng = gn
                self.pronoun.props["g"] = gn["g"]
                self.pronoun.props["n"] = gn["n"]
                self.pronoun.props["pe"] = gn["pe"]
        return self.doFormat(res)

    def real(self):
        if len(self.elements) == 0:
            # should a warning be issued!!
            return []
        res = []
        if self.isA("CP"):
            return self.cpReal()
        else:
            self.pronominalizeChildren()
            if "typ" in self.props:
                self.processTyp(self.props["typ"])
            # realize CPs before the rest because it can change gender and number of subject
            # save their realization
            cpReals = [e.cpReal() for e in self.elements if e.isA("CP")]
            for e in self.elements:
                if e.isA("CP"):
                    r = cpReals.pop(0)
                # TODO: is it worth the trouble ?
                # elif e.isA("VP") and reorderVPcomplements:
                #     r=e.vpReal()
                else:
                    r = e.real()
                res.extend(r)
            if self.isA("VP") and len(res) > 1:
                self.checkAdverbPos(res)
        return self.doFormat(res)

    # recreate a jsRealB expression
    # if indent is >=0 create an indented pretty-print (call it with 0 at the root)
    def toSource(self, indent=-1):
        if indent >= 0:
            indent = indent + len(self.constType) + 1
            sep = ",\n" + " " * indent
        else:
            sep = ","
        # create source of children
        return f'{self.constType}({sep.join(e.toSource(indent) for e in self.elementsSource)})' + super().toSource(indent)

    def toJSON(self):
        res = {"phrase": self.constType}
        if self.parentConst is None or self.lang() != self.parentConst.lang():  # only indicate when language changes
            res["lang"] = self.lang()
        res["elements"] = [e.toJSON() for e in self.elements]
        # if len(self.props) > 0:  # do not output empty props
        #     res["props"] = self.props
        res = self.addJSONprops(res)
        return res

    @classmethod
    def fromJSON(cls, constType, json, lang):
        from .utils import fromJSON, Q, phrase
        if "elements" in json:
            if isinstance(json["elements"], list):
                args = [fromJSON(e, lang) for e in json["elements"]]
                return phrase(constType, args, lang).setJSONprops(json)
            else:
                return cls.warn(Q(""),"user-warning","Phrase.fromJSON elements should be a list:" + str(json["elements"]))
        else:
            return cls.warn(Q(""),"user-warning","Phrase.fromJSON: no elements found in " + str(json))

    # create a Dependent version of a Phrase
    #   CAUTION:  this is useful for "common cases", this is not "foolproof" in all cases
    #             there are still language tests left in this function
    def toDependent(self,depName=None):
        from .utils import dep

        def removeAddOption(s):
            # we must remove the add option because the Phrase structure has already taken it into account,
            # so it should not be output in the Dependent version
            iAdd = s.find(".add(")
            if iAdd < 0: return s
            l = len(s)
            p = 1
            i = iAdd + 5
            while p > 0 and i < l:
                if   s[i] == "(": p += 1
                elif s[i] == ")": p -= 1
                i += 1
            return s[0:iAdd] + removeAddOption(s[i:])

        def setPos(i,idx,dep):
            # check if the position has to be specified
            if i < idx:
                if dep.isA("comp"):
                    dep.pos("pre")
                elif dep.isA("mod") and (not dep.isEn() or not dep.terminal.isA("A")):
                    dep.pos("pre")
            else:
                if dep.isA("subj", "det"):
                    dep.pos("post")
            return dep

        def makeDep(me,phName):
            termName=phName[:-1] # remove P at the end of the phrase name
            idx=me.getHeadIndex(phName)
            # if the first N has a poss flag, try to find the next "non possessive" N
            if phName=="NP" and me.elements[idx].isA("N") and me.elements[idx].getProp("poss"):
                for i in range(idx+1,len(me.elements)):
                    if me.elements[i].isA("N") and me.elements[i].getProp("poss") is None:
                        idx = i
                        break
            if (me.elements[idx].isA(termName)):
                deprel = dep([me.elements[idx]],depName)
                for i,e in enumerate(me.elements):
                    if i!=idx:
                        new_dep=e.toDependent("comp" if phName=="VP" else "mod")
                        deprel.add(setPos(i,idx,new_dep),None,True)
                deprel.props=me.props
            else :
                return self.warn("user-warning",f"Phrase.toDependent:: {phName} without {termName}: {me.toSource()}")
            return deprel

        if depName is None:depName="root"
        deprel=None
        if self.constType in ["NP","VP","AP","PP","AdvP"]:
            deprel=makeDep(self,self.constType)
        elif self.constType == "CP":
            idxC=self.getIndex("C")
            if (idxC>=0):
                deprel=dep([self.elements[idxC]],"coord")
                for i,e in enumerate(self.elements):
                    if i!=idxC:
                        deprel.add(e.toDependent(depName),None,True)
            else:
                return self.warn("Phrase.toDependent:: CP without C:"+self.toSource())
        elif self.constType in ["S","SP"]:
            iVP=self.getIndex("VP")
            if iVP>=0:
                deprel=self.elements[iVP].toDependent(depName)
            else:  ## this message can be ignored...
                # return cls.warn("user-warning","Phrase.toDependent:: S without VP:"+cls.toSource())
                return self
            iPro=-1
            if self.isA("SP"):
                if self.isFr(): # check for possible relative pronoun "que" in French that could be an object
                    iPro=self.getIndex(["Pro"])
                    if iPro>=0 and self.elements[iPro].lemma=="que":
                        deprel.add(self.elements[iPro].toDependent("comp").pos("pre"),0,True)
                    else:
                        iPro = -1
            iSubj=self.getIndex(["NP","N","CP","Pro"])
            # add rest of args
            for i,e in enumerate(self.elements):
                if i!=iVP and i!=iPro:
                    dep=e.toDependent("subj" if i==iSubj else "mod")
                    deprel.add(setPos(i,iVP,dep),None,True)
        else:
            return self.warn("user-warning",f"Phrase.toDependent:: {self.constType} not yet implemented")
        deprel.props |= self.props
        deprel.optSource+=removeAddOption(self.optSource)
        if self.parentConst is None and not self.isA("S"):
            deprel.cap(False)
        return deprel
