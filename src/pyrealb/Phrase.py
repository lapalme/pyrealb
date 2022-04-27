from .Constituent import Constituent
from .Terminal import Terminal, N, A, Pro, D, Adv, V, P, C, DT, NO, Q
from .Lexicon import getLexicon, getRules, currentLanguage
import sys

# all prepositions from getLexicon-en|fr.js (used for implementing int:"woi|wai|whn|whe"
# tail +2 getLexicon-en|fr.js | jq 'to_entries | map(select(.value|has("P"))|.key )'
prepositionsList = {
    "en": dict(all={"about", "above", "across", "after", "against", "along", "alongside", "amid", "among", "amongst",
                    "around", "as", "at", "back", "before", "behind", "below", "beneath", "beside", "besides",
                    "between", "beyond", "by", "concerning", "considering", "despite", "down", "during", "except",
                    "for", "from", "in", "inside", "into", "less", "like", "minus", "near", "next", "of", "off", "on",
                    "onto", "outside", "over", "past", "per", "plus", "round", "since", "than", "through", "throughout",
                    "till", "to", "toward", "towards", "under", "underneath", "unlike", "until", "up", "upon", "versus",
                    "with", "within", "without"},
               whe={"above", "across", "along", "alongside", "amid", "around", "before", "behind", "below", "beneath",
                    "beside", "besides", "between", "beyond", "in", "inside", "into", "near", "next", "onto", "outside",
                    "over", "past", "toward", "towards", "under", "underneath", "until", "via", "within"},
               whn={"after", "before", "during", "since", "till"}),
    "fr": dict(all={"à", "après", "avant", "avec", "chez", "contre", "d'après", "dans", "de", "dedans", "depuis",
                    "derrière", "dès", "dessous", "dessus", "devant", "durant", "en", "entre", "hors", "jusque",
                    "malgré",
                    "par", "parmi", "pendant", "pour", "près", "sans", "sauf", "selon", "sous", "sur", "vers", "via",
                    "voilà"},
               whe={"après", "avant", "chez", "dans", "dedans", "derrière", "dessous", "dessus", "devant", "entre",
                    "hors",
                    "près", "sous", "sur", "vers", "via"},
               whn={"après", "avant", "depuis", "dès", "durant", "en", "pendant"})
}

# negation of modal auxiliaries
negMod = {"can": "cannot", "may": "may not", "shall": "shall not", "will": "will not", "must": "must not",
          "could": "could not", "might": "might not", "should": "should not", "would": "would not"}


class Phrase(Constituent):
    def __init__(self, constType, elements, lang=None):
        elements = [e for e in elements if e != None]  # ignore None elements
        super().__init__(constType)
        if lang is None:
            self.lang = currentLanguage()
        elif lang in ["en", "fr"]:
            self.lang = lang
        else:
            self.lang = currentLanguage()
            self.warn("bad language", self.lang)
        # list of elements to create the source of the parameters at the time of the call
        # self can be different from the elements lists because of structure modifications
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
                self.warn("bad Constituent", i + 1, type(e).__name__, str(e))
        if len(elements) > 0:
            # terminate the list with add which does other checks on the final list
            self.add(elements[-1], None, True)

    # add a Constituent as a child of this Phrase
    def addElement(self, elem, position=None):
        if isinstance(elem, Constituent):
            elem.parentConst = self
            # add it to the list of elements
            if position == None:
                self.elements.append(elem)
            elif isinstance(position, int) and 0 <= position <= len(self.elements):
                self.elements.insert(position, elem)
            else:
                self.warn("bad position", position, len(self.elements))
        else:
            self.warn("bad Constituent", NO(position + 1).dOpt({"ord": True}), type(elem).__name__)
        return self

    # remove a child from this Phrase and return it
    def removeElement(self, position):
        if isinstance(position, int) and 0 <= position < len(self.elements):
            elem = self.elements.pop(position)
            elem.parentConst = None
            return elem
        return self.warn("bad position", position, len(self.elements))

    # add a pyrealb constituent, set agreement links
    def add(self, constituent, position=None, prog=None):  # prog is True when called from within the constructor
        def allAorN(elems, start, end):
            if start > end: (end, start) = (start, end)
            return all(el.isOneOf(["A", "N"]) for el in elems[start:end + 1])

        if prog is None and constituent is None: return self
        if isinstance(constituent, str):
            constituent = Q(constituent)
        elif not isinstance(constituent, Constituent):
            return self.warn("bad Constituent", "last" if self.isEn() else "dernier",
                             type(constituent).__name__ + ":" + str(constituent))
        if prog is None:
            self.optSource += f'.add({constituent.toSource(0)}{"" if position is None else ("," + str(position))})'
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
                if e.isFr():
                    pos = e.props["pos"] if "pos" in e.props else "post"
                else:
                    pos = "pre"
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
            self.peng = self.elements[headIndex].peng
            for i in range(0, len(self.elements)):
                if i != headIndex:
                    e = self.elements[i]
                    if hasattr(self, "peng"):  # do not try to modify if current peng does not exist e.g. Q
                        if e.isA("NO") and i < headIndex:  # NO must appear before the N for agreement
                            self.peng["n"] = e.grammaticalNumber()
                            # gender agreement between a French number and subject
                            e.peng["g"] = self.peng["g"]
                        elif e.isOneOf(["D", "A"]):
                            # link gender and number of the noun to the determiners and adjectives
                            # in English possessive determiner should not depend on the noun but on the "owner"
                            if self.isFr() or not e.isA("D") or "own" not in e.props:
                                e.peng = self.peng
            # set agreement between the subject of a subordinate or the object of a subordinate
            pro = self.getFromPath([["S", "SP"], "Pro"])
            if pro is not None:
                v = pro.parentConst.getFromPath(["VP", "V"])
                if v is not None:
                    if pro.lemma in ["qui", "who"]:  # agrees with self NP
                        v.peng = self.peng
                    elif self.isFr() and pro.lemma == "que":
                        # in French past participle can agree with a cod appearing before... keep that info just in case
                        v.cod = self
        elif self.isA("VP"):
            headIndex = self.getHeadIndex("VP")  # head is the first internal V
            self.peng = self.elements[headIndex].peng
            self.taux = self.elements[headIndex].taux
        elif self.isOneOf(["AdvP", "PP", "AP"]):
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
        elif self.isOneOf(["S", "SP"]):
            vpv = self.getFromPath([["", "VP"], "V"])
            if vpv is not None:
                self.taux = vpv.taux  # share tense and auxiliary of the verb
                if vpv.getProp("t") == "ip":  # do not search for subject for an imperative verb
                    return self
            iSubj = self.getIndex(["NP", "N", "CP", "Pro"])
            # determine subject
            if iSubj >= 0:
                subject = self.elements[iSubj]
                if self.isA("SP") and subject.isA("Pro"):
                    if subject.lemma in ["que", "où", "that"]:
                        # HACK: the first pronoun  should not be a subject...
                        #        so we try to find another...
                        jSubj = -1
                        for i in range(iSubj + 1, len(self.elements)):
                            if self.elements[i].isOneOf(["NP", "N", "CP", "Pro"]):
                                jSubj = i
                                break
                        if jSubj >= 0:
                            subject = self.elements[jSubj]
                        else:
                            # finally self generates too many spurious messages
                            # self.warning("no possible subject found")
                            return self
                self.peng = subject.peng
                vpv = self.linkPengWithSubject("VP", "V", subject)
                if vpv is not None:
                    self.taux = vpv.taux
                    if self.isFr() and vpv.lemma in ["être", "paraître", "sembler", "devenir", "rester"]:
                        # check for a French attribute of copula verb
                        # with an adjective
                        attribute = vpv.parentConst.linkPengWithSubject("AP", "A", subject)
                        if attribute is None:
                            elems = vpv.parentConst.elements
                            try:
                                vpvIdx = elems.index(vpv)
                                for i in range(vpvIdx + 1, len(elems)):
                                    pp = elems[i]
                                    if pp.isA("V") and pp.getProp("t") == "pp":
                                        pp.peng = subject.peng
                                        break
                            except ValueError:
                                self.error("linkProperties    : verb not found")

                else:
                    # check for a coordination of verbs that share the subject
                    cvs = self.getFromPath(["CP", "VP"])
                    if cvs is not None:
                        for e in self.getConst("CP").elements:
                            if isinstance(e, Phrase):  # skip possible C
                                e.linkPengWithSubject("VP", "V", subject)
                    if self.isFr():
                        #  in French, check for a coordinated object of a verb in an SP used as cod
                        #  occurring before the verb
                        cp = self.getConst("CP")
                        sp = self.getConst("SP")
                        if cp is not None and sp is not None:
                            sppro = sp.getConst("Pro")
                            if sppro is not None and sppro.lemma == "que":
                                v = sp.getFromPath([["VP", ""], "V"])
                                if v != None:
                                    v.cod = cp
            else:
                # finally, self generates too many spurious messages
                # self.warning("no possible subject found")
                self.peng = None
        else:
            self.error("linkProperties    ,unimplemented type:" + self.constType)
        return self

    def linkPengWithSubject(self, phrase, terminal, subject):
        # do not link a subject pronoun at genitive
        if subject.isA("Pro") and "c" in subject.props and subject.props["c"] == "gen": return
        pt = self.getFromPath([phrase, terminal])
        if pt != None:
            pt.parentConst.peng = pt.peng = subject.peng
        else:
            pt = self.getFromPath([terminal])
            if pt != None:
                pt.peng = subject.peng
        return pt

    def me(self):
        return f'{self.constType}({",".join([e.me() for e in self.elements])})'

    def setLemma(self, _terminalType):
        return self.error("***: should never happen: setLemma: called on a Phrase")

    # find the index of a Constituent type (or one of the constituents) in the list of elements
    def getIndex(self, constTypes):
        if isinstance(constTypes, str): constTypes = [constTypes]
        for i in range(0, len(self.elements)):
            if self.elements[i].isOneOf(constTypes):
                return i
        return -1

    # find a given constituent type (or one of the constituent) in the list of elements
    def getConst(self, constTypes):
        idx = self.getIndex(constTypes)
        if idx < 0: return None
        return self.elements[idx]

    # ##### information propagation

    # find the gender, number and Person of NP elements of self Phrase
    #   set masculine if at least one NP is masculine
    #   set plural if one is plural or more than one combined with and
    #   set person to the minimum one encountered (i.e. 1st < 2nd < 3rd) mostly useful for French 
    def findGenderNumberPerson(self, andCombination):
        g = "f"
        n = "s"
        pe = 3
        nb = 0
        for e in self.elements:
            if e.isOneOf(["NP", "N", "Pro", "Q"]):
                nb += 1
                propG = e.getProp("g")
                if propG == "m" or propG == "x" or e.isA("q"): g = "m"  # masculine if gender is unspecified
                if e.getProp("n") == "p": n = "p"
                propPe = e.getProp("pe")
                if propPe != None and propPe < pe: pe = propPe
        if nb == 0:
            g = "m"
        elif nb > 1 and n == "s" and andCombination:
            n = "p"
        return {"g": g, "n": n, "pe": pe}

    # ###### Phrase structure modification

    # Phrase structure modification but that must be called in the context of the parentConst
    # because the pronoun depends on the role of the NP in the sentence 
    #         and its position can also change relatively to the verb
    def pronominalize_fr(self):
        npParent = self.parentConst
        pro = None
        if npParent != None:
            idxMe = npParent.elements.index(self)
            idxV = idxMe - 1  # search for the first verb before the NP
            while idxV >= 0 and not npParent.elements[idxV].isA("V"): idxV -= 1
            if (idxV >= 1 and npParent.elements[idxV].getProp("t") == "pp"
                    and npParent.elements[idxV - 1].isA("V")):
                # take for granted that the preceding verb is an auxiliary, so skip it
                idxV -= 1
            if self.isA("NP"):
                np = self
                if hasattr(npParent, "peng") and self.peng == npParent.peng:  # is subject
                    pro = self.getTonicPro("nom")
                elif npParent.isA("SP") and npParent.elements[0].isA("Pro"):  # is relative
                    pro = self.getTonicPro("nom")
                else:
                    pro = self.getTonicPro("acc")  # is direct complement
                    npParent.elements[idxV].cod = self  # indicate that self is a direct object
            elif self.isA("PP"):  # is indirect complement
                np = self.getFromPath([["NP", "Pro"]])  # either a NP or Pro within the PP
                prep = self.getFromPath(["P"])
                if prep != None and np != None:
                    if prep.lemma == "à":
                        pro = np.getTonicPro("dat")
                    elif prep.lemma == "de":
                        pro = Pro("en", "fr").c("dat")
                    elif prep.lemma in ["sur", "vers", "dans"]:
                        pro = Pro("y", "fr").c("dat")
                    else:  # change only the NP within the PP
                        pro = np.getTonicPro()
                        pro.props = np.props
                        pro.peng = np.peng
                        np.elements = [pro]
                        return
            if pro is None:
                return npParent.warn("no appropriate pronoun")
            pro.peng = np.peng
            for key, val in np.props.items():
                pro.props[key] = val
            if "pro" in pro.props:
                del pro.props["pro"]  # self property should not be copied into the Pro
            # in French a pronominalized NP as direct object is moved before the verb
            # if idxV>=0 and npParent.elements[idxV].getProp("t") not in ["ip","b"]: # except for imperative and infinitive
            #     npParent.removeElement(idxMe)   # remove NP
            #     npParent.addElement(pro,idxV) # insert pronoun before the V
            # else:
            npParent.removeElement(idxMe)  # insert pronoun where the NP was
            npParent.addElement(pro, idxMe)
        else:  # special case without parentConst, so we leave the NP and change its elements
            pro = self.getTonicPro(None)
            pro.props = self.props
            pro.peng = self.peng
            self.elements = [pro]
        return pro

    # Pronominalization in English only applies to a NP (self is checked before the call)
    #  and does not need reorganisation of the sentence 
    def pronominalize_en(self):
        npParent = self.parentConst
        if npParent != None:
            idx = npParent.elements.index(self)
            if hasattr(npParent, "peng") and self.peng == npParent.peng:  # is subject
                pro = self.getTonicPro("nom")
            elif npParent.isA("SP") and npParent.elements[0].isA("Pro"):  # is relative
                pro = self.getTonicPro("nom")
            else:
                pro = self.getTonicPro("acc")  # is direct complement
            pro.peng = self.peng
            for key, val in self.props.items():
                pro.props[key] = val
            if hasattr(npParent, "peng") and self.peng == npParent.peng:
                npParent.peng = pro.peng
            npParent.removeElement(idx)  # insert pronoun where the NP was
            npParent.addElement(pro, idx)
        else:  # special case without parentConst, so we leave the NP and change its elements
            pro = self.getNomPro()
            pro.props = self.props
            pro.peng = self.peng
            self.elements = [pro]
        return pro

    def pronominalize(self, e):
        if "pro" in e.props and not e.isA(
                "Pro"):  # it can happen that a Pro has property "pro" set within the same expression
            if e.isFr():
                return e.pronominalize_fr()
            # in English pronominalize only applies to a NP
            if e.isA("NP"):
                return e.pronominalize_en()
            else:
                return self.warn("bad application", ".pro", ["NP"], e.constType)

    # check if any child should be pronominalized
    # self must be done in the context of the parent, because some elements might be changed
    def pronominalizeChildren(self):
        for e in self.elements:
            self.pronominalize(e)

            # modify the sentence structure to create a passive sentence

    def passivate(self):
        # find the subject at the start of self.elements
        if self.isA("VP"):
            subject = None
            vp = self
        else:
            vp = self.getConst("VP")
            if vp != None:
                if len(self.elements) > 0 and self.elements[0].isOneOf(["N", "NP", "Pro"]):
                    subject = self.removeElement(0)
                    if subject.isA("Pro"):
                        # as self pronoun will be preceded by "par" or "by", the "bare" tonic form is needed
                        # to which the original pe, gender and number are added
                        subject = subject.getTonicPro(None).pe(subject.getProp("pe")).g(subject.getProp("g")).n(
                            subject.getProp("n"))
                else:
                    subject = None
            else:
                return self.warn("not found", "VP", "contexte passif" if self.isFr() else "passive context")
        # remove object (first NP or Pro within VP) from elements
        newSubject = None
        if vp != None:
            objIdx = vp.getIndex(["NP", "Pro"])
            if objIdx >= 0:
                obj = vp.elements.pop(objIdx)
                if obj.isA("Pro"):
                    obj = obj.getTonicPro("nom")
                    if objIdx == 0:  # a French pronoun inserted by .pro()
                        objIdx = vp.getIndex("V") + 1  # ensure that the pyrealb object will appear after the verb
                elif obj.isA("NP") and "pro" in obj.props:
                    obj = obj.getTonicPro("nom")
                # swap subject and obj
                newSubject = obj
                self.addElement(newSubject, 0)  # add object that will become the subject
                newSubject.parentConst = self  # adjust parentConst
                # make the verb agrees with the pyrealb subject (in English only, French is dealt below)
                if self.isEn():
                    self.linkPengWithSubject("VP", "V", newSubject)
                if subject is not None:  # insert subject where the object was
                    vp.addElement(PP(P("par" if self.isFr() else "by", self.lang), subject), objIdx)
            elif subject is not None:  # no object, but with a subject
                # create a dummy subject with a "il"/"it" 
                newSubject = Pro("lui" if self.isFr() else "it", self.lang).c("nom")
                # add pyrealb subject at the front of the sentence
                self.addElement(newSubject, 0)
                self.linkPengWithSubject("VP", "V", newSubject)
                vp.peng = newSubject.peng
                # add original subject after the verb to serve as an object
                vpIdx = vp.getIndex("V")
                vp.addElement(PP(P("par" if self.isFr() else "by", self.lang), subject), vpIdx + 1)
            if self.isFr():
                # do this only for French because in English this is done by processTyp_en
                # change verbe to "être" auxiliary and make it agree with the newSubject
                verbeIdx = vp.getIndex("V")
                verbe = vp.removeElement(verbeIdx)
                aux = V("être", "fr")
                aux.parentConst = vp
                aux.taux = verbe.taux
                if newSubject != None:  # this can happen when a subject is Q
                    aux.peng = newSubject.peng
                aux.props = verbe.props
                aux.pe(3)  # force person to be 3rd (number and tense will come from the pyrealb subject)
                if vp.getProp("t") == "ip":
                    aux.t("s")  # set subjonctive present tense for an imperative
                pp = V(verbe.lemma, "fr").t("pp")
                if newSubject != None:  # self can happen when a subject is Q
                    # make the past participle agree with the new subject
                    pp.setProp("g",newSubject.getProp("g"))
                    pp.setProp("n",newSubject.getProp("n"))
                vp.addElement(aux, verbeIdx).addElement(pp, verbeIdx + 1)
        else:
            return self.warn("not found", "VP", "contexte passif" if self.isFr() else "passive context")

    # generic phrase structure modification for a VP, called in the .typ({...}) for .prog, .mod, .neg
    # also deals with coordinated verbs
    def processVP(self, types, key, action):
        v = self.getFromPath(["CP", "VP"])
        if v != None:  # possibly a coordination of verbs
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
                    self.warn("bad const for option", '.typ("' + key + ":" + str(val) + '")', self.constType, ["VP"])
                    return
            idxV = vp.getIndex("V")
            if idxV >= 0:
                v = vp.elements[idxV]
                action(vp, idxV, v, val)

    def processTyp_fr(self, types):
        # process types in a particular order
        rules = getRules()

        def prog(vp, idxV, _v, _w):
            # isReflexive=vp.elements[idxV].isReflexive() # must be called before removeElement to take account its parentConst
            verb = vp.elements.pop(idxV)
            origLemma = verb.lemma
            verb.setLemma("être")  # change verb, but keep person, number and tense properties of the original...
            verb.isProg = verb
            # insert "en train","de" (separate so that élision can be done...)
            # but do it BEFORE the pronouns created by .pro()
            i = idxV - 1
            while i >= 0 and vp.elements[i].isA("Pro") and vp.elements[i].peng is not vp.peng: i -= 1
            vp.addElement(verb, i + 1).addElement(Q("en train"), i + 2).addElement(Q("de"), i + 3)
            # if isReflexive:
            #     # or "essentiellement réflexifs" verbs, add appropriate pronoun before the infinitive (without se)
            #     vp.addElement(Pro("me*refl").pe(verb.getProp("pe")).n(verb.getProp("n")).g(verb.getProp("g")),idxV+3)\
            #         .addElement(Q(origLemma),idxV+4)
            # else:
            vp.addElement(V(origLemma).t("b"), idxV + 3)

        self.processVP(types, "prog", prog)

        def mod(vp, idxV, v, mod):
            origLemma = v.lemma
            for key in rules["verb_option"]["modalityVerb"]:
                if key.startswith(mod):
                    v.setLemma(rules["verb_option"]["modalityVerb"][key])
                    break
            v.isMod=True
            i = idxV - 1
            # move the modality verb before the pronoun(s) inserted by .pro()
            while i >= 0 and vp.elements[i].isA("Pro") and vp.elements[i].peng != vp.peng: i -= 1
            if i != idxV - 1:
                vp.addElement(vp.removeElement(idxV),
                              i + 1)  # remove the modality verb and move it before the pronouns
            newV=V(origLemma).t("b")
            if hasattr(v,"isProg"): #copy progressive from original verb...
                newV.isProg=v.isProg
                del v.isProg
            vp.addElement(newV, idxV + 1)  # add the original verb at infinitive

        self.processVP(types, "mod", mod)

        def process_neg(vp, idxV, v, neg):
            if neg == True: neg = "pas"
            v.neg2 = neg  # HACK: to be used when conjugating at the realization time
            # while idxV>0 and vp.elements[idxV-1].isA("Pro"):idxV-=1
            # # insert "ne" before the verb or before possible pronouns preceding the verb
            # if v.getProp("t")!="pp":
            #     vp.addElement(Adv("ne","fr"),idxV)

        self.processVP(types, "neg", process_neg)

    @staticmethod
    def affixHopping(v,t,compound,types):
        v_peng = v.peng
        neg = "neg" in types and types["neg"] == True
        # English conjugation
        # it implements the "affix hopping" rules given in
        #      N. Chomsky, "Syntactic Structures", 2nd ed. Mouton de Gruyter, 2002, p 38 - 48
        auxils = []  # list of Aux followed by V
        affixes = []
        isFuture = False
        if (t == "f"):
            isFuture = True
            t = "p"  # the auxiliary will be generated here so remove it from the V
        prog = "prog" in types and types["prog"] != False
        perf = "perf" in types and types["perf"] != False
        pas = "pas" in types and types["pas"] != False
        interro = types["int"] if "int" in types and types["int"] != False else None
        modality = types["mod"] if "mod" in types and types["mod"] != False else None
        # compound = getRules()["compound"]
        if modality != None:
            auxils.append(compound[modality]["aux"])
            affixes.append("b")
        elif isFuture:
            # caution: future in English is done with the modal will, so another modal cannot be used
            auxils.append(compound["future"]["aux"])
            affixes.append("b")
        if perf or prog or pas:
            if perf:
                auxils.append(compound["perfect"]["aux"])
                affixes.append(compound["perfect"]["participle"])
            if prog:
                auxils.append(compound["continuous"]["aux"])
                affixes.append(compound["continuous"]["participle"])
            if pas:
                auxils.append(compound["passive"]["aux"])
                affixes.append(compound["passive"]["participle"])
        elif (interro != None and
              len(auxils) == 0 and v.lemma != "be" and v.lemma != "have"):
            # add auxiliary for interrogative if not already there
            if interro != "wos" and interro != "was":
                auxils.append("do")
                affixes.append("b")
        auxils.append(v.lemma)
        # realise the first verb, modal or auxiliary
        # but make the difference between "have" as an auxiliary and "have" as a verb
        vAux = auxils.pop(0)
        words = []
        # conjugate the first verb
        if neg:  # negate the first verb
            if t == "pp" or t == "pr":  # special case for these tenses
                words.append(Adv("not", "en"))
                words.append(V(vAux, "en").t(t))
            elif vAux in negMod:
                if vAux == "can" and t == "p":
                    words.append(Q("cannot"))
                else:
                    words.append(V(vAux, "en").t(t))
                    words.append(Adv("not", "en"))
            elif vAux == "be" or (vAux == "have" and v.lemma != "have"):
                words.append(V(vAux).t(t))
                words.append(Adv("not", "en"))
            else:
                words.append(V("do", "en").t(t))
                words.append(Adv("not", "en"))
                if vAux != "do": words.append(V(vAux).t("b"))
        else:  # must only set necessary options, so that shared properties will work ok
            newAux = V(vAux)
            if not isFuture: newAux.t(t)
            if v in negMod: newAux.pe(1)
            words.append(newAux)
        # recover the original agreement info and set it to the first pyrealb verb...
        words[0].peng = v_peng
        # realise the other parts using the corresponding affixes
        while len(auxils) > 0:
            vb = auxils.pop(0)
            words.append(V(vb).t(affixes.pop(0)))
        if "refl" in types and types["refl"] == True and t != "pp":
            words.append(Pro("myself", "en").pe(v.getProp("pe"))
                         .n(v.getProp("n")).g(v.getProp("g")))
        return words

    def processTyp_en(self, types):
        # replace current verb with the list pyrealb words
        #  TODO: take into account the fact that there might be already a verb with modals...
        if self.isA("VP"):
            vp = self
        else:
            idxVP = self.getIndex(["VP"])
            if idxVP >= 0:
                vp = self.elements[idxVP]
            else:
                return self.warn("bad const for option", '.typ(' + str(types) + ')', self.constType, ["VP"])
        idxV = vp.getIndex("V")
        if idxV >= 0:
            v = vp.elements[idxV]
            if "contr" in types and types["contr"] != False:
                vp.contraction = True  # necessary because we want the negation to be contracted within the VP before the S or SP
                self.contraction = True
            words=Phrase.affixHopping(vp.elements[idxV],vp.getProp("t"),getRules()["compound"],types)
            # insert the content of the word array into vp.elements
            vp.removeElement(idxV)
            for i in range(0, len(words)):
                vp.addElement(words[i], idxV + i)
        else:
            self.warn("not found", "V", "VP")

    # get elements of the constituent cst2 within the constituent cst1
    def getIdxCtx(self, cst1, cst2):
        if self.isA(cst1):
            idx = self.getIndex(cst2)
            if idx >= 0: return (idx, self.elements)
        elif self.isOneOf(["S", "SP"]):
            cst = self.getConst(cst1)
            if cst != None: return cst.getIdxCtx(cst1, cst2)
        return (None, None)

    def moveAuxToFront(self):
        # in English move the auxiliary to the front 
        if self.isEn():
            if self.isOneOf(["S", "SP"]):
                (idx, vpElems) = self.getIdxCtx("VP", "V")
                if idx != None:
                    v = vpElems.pop(0)  # remove first V
                    # check if V is followed by a negation, if so move it also
                    if len(vpElems) > 0 and vpElems[0].isA("Adv") and vpElems[0].lemma == "not":
                        not_ = vpElems[0].parentConst.removeElement(0)
                        self.addElement(v, 0).addElement(not_, 1)
                    else:
                        self.addElement(v, 0)

    def invertSubject(self):
        # in French : use inversion rule which is quite "delicate"
        # rules from https:#francais.lingolia.com/fr/grammaire/la-phrase/la-phrase-interrogative
        # if subject is a pronoun, invert and add "-t-" or "-"
        # if subject is a noun, the subject stays but add a pyrealb pronoun
        subjIdx = self.getIndex(["NP", "N", "Pro", "SP", "CP"])
        if subjIdx >= 0:
            subj = self.elements[subjIdx]
            if subj.isA("Pro"):
                pro = self.removeElement(subjIdx)  # remove subject pronoun
            elif subj.isA("CP"):
                pro = Pro("moi", "fr").c("nom").g("m").n("p").pe(
                    3)  # create a "standard" pronoun, to be patched by cpReal
                subj.pronoun = pro  # add a flag to be processed by cpReal
            else:
                pro = Pro("moi", "fr").g(subj.getProp("g")).n(subj.getProp("n")).pe(3).c("nom")  # create a pronoun
            (idx, vpElems) = self.getIdxCtx("VP", "V")
            if idx != None:
                v = vpElems[idx]
                v.parentConst.addElement(pro, idx + 1)  # add pronoun after verb
                v.lier()  # add - after verb

    def processInt(self, int_):
        sentenceTypeInt = getRules()["sentence_type"]["int"]
        intPrefix = sentenceTypeInt["prefix"]
        prefix = None
        pp = None
        if int_ in ["yon", "how", "why", "muc"]:
            if self.isEn():
                self.moveAuxToFront()
            else:
                self.invertSubject()
            prefix = intPrefix[int_]
        # remove a part of the sentence
        elif int_ in ["wos", "was"]:  # remove subject (first NP,N, Pro or SP)
            if self.isOneOf(["S", "SP", "VP"]):
                subjIdx = self.getIndex(["NP", "N", "Pro", "SP"])
                if subjIdx != None:
                    vbIdx = self.getIndex(["VP", "V"])
                    if vbIdx != None and subjIdx < vbIdx:  # subject should be before the verb
                        # make sure that the verb at the third-person singular,
                        # because now the subject has been removed
                        v = self.elements[vbIdx]
                        v.setProp("n", "s")
                        v.setProp("pe", 3)
                        del self.elements[subjIdx]
            prefix = intPrefix[int_]
        elif int_ in ["wod", "wad"]:  # remove direct object (first NP,N,Pro or SP in the first VP)
            if self.isOneOf(["S", "SP", "VP"]):
                idx, obj = self.getIdxCtx("VP", ["NP", "N", "Pro", "SP"])
                if idx != None:
                    del obj[idx]
                elif self.isFr():  # check for passive subject starting with par
                    idx, ppElems = self.getIdxCtx("VP", "PP")
                    if idx != None:
                        pp = ppElems[idx].getConst("P")
                        if pp != None and pp.lemma == "par":
                            ppElems[0].parentConst.removeElement(idx)  # remove the passive subject
                        else:
                            pp = None
                prefix = intPrefix[int_]
                if self.isEn():
                    self.moveAuxToFront()
                else:
                    self.invertSubject()
        elif int_ in ["woi", "wai", "whe", "whn"]:  # remove indirect object (first PP in the first VP)
            if self.isOneOf(["S", "SP", "VP"]):
                idx, ppElems = self.getIdxCtx("VP", "PP")
                prefix = intPrefix[int_]  # get default prefix
                if idx != None:
                    # try to find a more appropriate prefix by looking at preposition in the structure
                    prep = ppElems[idx].elements[0]
                    if prep.isA("P"):
                        prep = prep.lemma
                        preps = prepositionsList[self.lang]
                        if int_ == "whe":
                            if prep in preps["whe"]: del ppElems[idx]
                        elif int_ == "whn":
                            if prep in preps["whn"]: del ppElems[idx]
                        elif prep in preps["all"]:  # "woi" | "wai"
                            # add the preposition in front of the prefix (should be in the table...)
                            if self.isEn():
                                prefix = prep + " " + ("whom" if int_ == "woi" else "what")
                            else:
                                prefix = prep + " " + ("qui" if int_ == "woi" else "quoi")
                            del ppElems[idx]
                if self.isEn():
                    self.moveAuxToFront()
                else:
                    self.invertSubject()
        else:
            self.warn("not implemented", "int:" + int_)
        if self.isFr() or int_ != "yon":  # add the interrogative prefix
            self.addElement(Q(prefix), 0)
            if pp != None:  # add "par" in front of some French passive interrogative
                self.addElement(pp, 0)
                if int_ == "wad":  # replace "que" by "quoi" for French passive wad
                    self.elements[1].lemma = "quoi"
        self.a(sentenceTypeInt["punctuation"], True)

    def processTyp(self, types):
        if "pas" in types and types["pas"] != False:
            self.passivate()
        if self.isFr():
            if "contr" in types and types["contr"] != False:
                self.warn("no French contraction")
            self.processTyp_fr(types)
        else:
            self.processTyp_en(types)
        if "int" in types and types["int"] != False:
            self.processInt(types["int"])
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
            self.setProp("pe", elems[0].getProp("pe") if elems[0].getProp("pe") != None else 3)
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
            _and = "et" if self.isFr() else "and"
            gn = self.findGenderNumberPerson(c.lemma == _and)
            self.setProp("g", gn["g"])
            self.setProp("n", gn["n"])
            self.setProp("pe", gn["pe"])
            # for the pronoun, we must override its existing properties...
            if hasattr(self, "pronoun"):
                self.pronoun.peng = gn
                self.pronoun.props["g"] = gn["g"]
                self.pronoun.props["n"] = gn["n"]
                self.pronoun.props["pe"] = gn["pe"]
        return res

    def real(self):
        res = []
        if self.isA("CP"):
            res = self.cpReal()
        else:
            self.pronominalizeChildren()
            if "typ" in self.props:
                self.processTyp(self.props["typ"])
            for e in self.elements:
                if e.isA("CP"):
                    r = e.cpReal()
                # TODO: is it worth the trouble ?
                # elif e.isA("VP") and reorderVPcomplements:
                #     r=e.vpReal()
                else:
                    r = e.real()
                res.extend(r)
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
        return f'{self.constType}({sep.join(e.toSource(indent) for e in self.elementsSource)})' + super().toSource()

    def toJSON(self):
        res = {"phrase": self.constType}
        if self.parentConst is None or self.lang != self.parentConst.lang:  # only indicate when language changes
            res["lang"] = self.lang
        res["elements"] = [e.toJSON() for e in self.elements]
        if len(self.props) > 0:  # do not output empty props
            res["props"] = self.props
        return res

    @classmethod
    def fromJSON(self, constType, json, lang):
        from .utils import fromJSON
        if "elements" in json:
            if isinstance(json["elements"], list):
                args = [fromJSON(e, lang) for e in json["elements"]]
                return Phrase(constType, args, lang).setJSONprops(json)
            else:
                return self.warn("user-warning","Phrase.fromJSON elements should be a list:" + str(json["elements"]))
        else:
            return self.warn("user-warning","Phrase.fromJSON: no elements found in " + str(json))

    # create a Dependent version of a Phrase
    def toDependent(self,depName=None):
        from .Dependent import Dependent

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
                if dep.isOneOf(["subj", "det"]):
                    dep.pos("post")
            return dep

        def makeDep(me,phName):
            termName=phName[:-1] # remove P at the end of the phrase name
            idx=me.getHeadIndex(phName)
            if (me.elements[idx].isA(termName)):
                deprel = Dependent([me.elements[idx]],depName)
                for i,e in enumerate(me.elements):
                    if i!=idx:
                        dep=e.toDependent("comp" if phName=="VP" else "mod")
                        deprel.add(setPos(i,idx,dep),None,True)
            else :
                return self.warn("user-warning",f"Phrase.toDependent:: {phName} without {termName} {me.toSource()}")
            return deprel

        if depName is None:depName="root"
        deprel=None
        if self.constType in ["NP","VP","AP","PP","AdvP"]:
            deprel=makeDep(self,self.constType)
        elif self.constType == "CP":
            idxC=self.getIndex("C")
            if (idxC>=0):
                deprel=Dependent([self.elements[idxC]],"coord")
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
                # return self.warn("user-warning","Phrase.toDependent:: S without VP:"+self.toSource())
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
        deprel.props=self.props
        deprel.optSource=removeAddOption(self.optSource)
        if self.parentConst is None and not self.isA("S"):
            deprel.cap(False)
        return deprel


# # create Phrase subclasses
#  which could be done using the following exec
# phraseDefString='''
# class {0}(Phrase):
#     def __init__(self, *elems):
#         super().__init__("{0}",elems)
# '''
# for p in ["NP","AP","AdvP","VP","PP","CP","S","SP"]:
#     exec(phraseDefString.format(p))
#
#  but we use in-line expansion of the above to avoid annoying error messages in Eclipse
class NP(Phrase):
    def __init__(self, *elems):
        super().__init__("NP", elems)


class AP(Phrase):
    def __init__(self, *elems):
        super().__init__("AP", elems)


class AdvP(Phrase):
    def __init__(self, *elems):
        super().__init__("AdvP", elems)


class VP(Phrase):
    def __init__(self, *elems):
        super().__init__("VP", elems)


class PP(Phrase):
    def __init__(self, *elems):
        super().__init__("PP", elems)


class CP(Phrase):
    def __init__(self, *elems):
        super().__init__("CP", elems)


class S(Phrase):
    def __init__(self, *elems):
        super().__init__("S", elems)


class SP(Phrase):
    def __init__(self, *elems):
        super().__init__("SP", elems)
