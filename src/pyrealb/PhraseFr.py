from .ConstituentFr import ConstituentFr
from .NonTerminalFr import NonTerminalFr
from .Phrase import Phrase
from .Lexicon import getRules

class PhraseFr(ConstituentFr,NonTerminalFr,Phrase):

    def link_DAV_properties(self, e):
        if e.isA("A") and e.lemma == "quelques":
            self.peng = "p"
            return
        if e.isA("A", "D"):
            # link gender and number of the noun to the determiners and adjectives
            e.peng = self.peng
            return
        if e.isA("V") and e.getProp("t") == "pp":
            e.peng = self.peng
            return

    def check_determiner_cnt(self, det, headNoun):
        pass

    def link_subj_obj_subordinate(self, pro, v, subject):
        if pro.lemma in ["qui","lequel"] and pro == subject:  # agrees with self NP
            v.peng = self.peng
            if pro.lemma == "lequel":pro.peng = self.peng
            self.linkAttributes(v, self.getFromPath([["VP"], ["CP"]]), self)
        elif pro.lemma in ["duquel","auquel"]: # only agree the pronoun
            pro.peng = self.peng
        elif pro.lemma == "que":
            # in French past participle can agree with a cod appearing before... keep that info just in case
            v.cod = self
            # HACK: check for a "temps composé" formed by "avoir" followed by a past participle
            if v.lemma == "avoir":
                idx = v.parentConst.getIndex("V")
                if len(v.parentConst.elements) > idx + 1:
                    next = v.parentConst.elements[idx + 1]
                    if next.isA("V") and next.getProp("t") == "pp":
                        next.cod = self

    def linkAttributes(self, vpv, vpcp, subject):
        if vpv.lemma in ["être", "paraître", "sembler", "devenir", "rester"]:
            # check for a coordination of attributes or past participles
            # vpcp = self.getFromPath([["VP"], ["CP"]])
            if vpcp is not None:
                for e in vpcp.elements:
                    if e.isA("A"):
                        e.peng = subject.peng
                    elif e.isA("V") and e.getProp("t") == "pp":
                        e.peng = subject.peng
                    elif e.isA("AP"):
                        e.linkPengWithSubject("AP", "A", subject)
                    elif e.isA("VP"):
                        v = e.getConst("V")
                        if v is not None and v.getProp("t") == "pp":
                            v.peng = subject.peng
            else:
                # check for a single French attribute of a copula verb
                # with an adjective
                attribute = vpv.parentConst.linkPengWithSubject("AP", "A", subject)
                if attribute is None:
                    elems = vpv.parentConst.elements
                    try:
                        vpvIdx = elems.index(vpv)
                        for i in range(vpvIdx + 1, len(elems)):
                            e = elems[i]
                            if e.isA("V") and e.getProp("t") == "pp":
                                e.peng = subject.peng
                    except ValueError:
                        self.error("linkProperties    : verb not found")

    def should_try_another_subject(self,lemma,iSubj):
         # Check if a lemma is pronoun that should not be subject of a subordinate
        return lemma in ["que","où","dont"] or \
              (lemma == "qui" and iSubj>0 and self.elements[iSubj-1].isA("P"))

    def check_coordinated_object(self):
        #  in French, check for a coordinated object of a verb in an SP used as cod
        #  occurring before the verb
        cp = self.getConst("CP")
        sp = self.getConst("SP")
        if cp is not None and sp is not None:
            sppro = sp.getConst("Pro")
            if sppro is not None and sppro.lemma == "que":
                v = sp.getFromPath([["VP", ""], "V"])
                if v is not None:
                    v.cod = cp

    # Phrase structure modification but that must be called in the context of the parentConst
    # because the pronoun depends on the role of the NP in the sentence
    #         and its position can also change relatively to the verb
    def pronominalize(self):
        from .utils import Pro
        npParent = self.parentConst
        pro = None
        if npParent is not None:
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
                elif idxV>=0:
                    pro = self.getTonicPro("acc")  # is direct complement
                    npParent.elements[idxV].cod = self  # indicate that self is a direct object
                else: # only replace the noun
                    pro = self.getTonicPro("nom")
            elif self.isA("PP"):  # is indirect complement
                np = self.getFromPath([["NP", "Pro"]])  # either a NP or Pro within the PP
                prep = self.getFromPath(["P"])
                if prep is not None and np is not None:
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

    def passive_agree_auxiliary(self, vp, newSubject):
        from .utils import V
        # do this only for French because in English this is done by processTyp_en
        # change verbe to "être" auxiliary and make it agree with the newSubject
        verbeIdx = vp.getIndex("V")
        verbe = vp.removeElement(verbeIdx)
        aux = V("avoir" if verbe.lemma == "être" else "être", "fr")
        aux.parentConst = vp
        aux.taux = verbe.taux
        if newSubject is not None:  # this can happen when a subject is Q
            aux.peng = newSubject.peng
        aux.props = verbe.props
        if vp.getProp("t") == "ip":
            aux.t("s")  # set subjonctive present tense for an imperative
        pp = V(verbe.lemma, "fr").t("pp")
        if newSubject is not None:  # self can happen when a subject is Q
            # make the past participle agree with the new subject
            pp.setProp("g", newSubject.getProp("g"))
            pp.setProp("n", newSubject.getProp("n"))
        vp.addElement(aux, verbeIdx).addElement(pp, verbeIdx + 1)

    def processTyp_verb(self, types):
        from .utils import Q, V
        if "contr" in types and types["contr"] != False:
            self.warn("no French contraction")
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
            vp.addElement(V(origLemma).t("b"), idxV + 3)

        self.processVP(types, "prog", prog)

        def mod(vp, idxV, v, mod):
            origLemma = v.lemma
            for key in rules["verb_option"]["modalityVerb"]:
                if key.startswith(mod):
                    v.setLemma(rules["verb_option"]["modalityVerb"][key])
                    if hasattr(v, "cod"): del v.cod
                    break
            v.isMod = True
            i = idxV - 1
            # move the modality verb before the pronoun(s) inserted by .pro()
            while i >= 0 and vp.elements[i].isA("Pro") and vp.elements[i].peng != vp.peng: i -= 1
            if i != idxV - 1:
                vp.addElement(vp.removeElement(idxV),
                              i + 1)  # remove the modality verb and move it before the pronouns
            newV = V(origLemma).t("b")
            newV.pe(v.getProp("pe")).n(v.getProp("n")) # copy also person and number used for pronoun of reflexive verb
            if hasattr(v, "isProg"):  # copy progressive from original verb...
                newV.isProg = v.isProg
                del v.isProg
            vp.addElement(newV, idxV + 1)  # add the original verb at infinitive

        self.processVP(types, "mod", mod)

        def process_neg(vp, _idxV, v, neg):
            if neg == True: neg = "pas"
            v.neg2 = neg  # HACK: to be used when conjugating at the realization time

        self.processVP(types, "neg", process_neg)

    def move_object(self,int_):
        from .utils import Pro, Q
        # in French : use inversion rule which is quite "delicate"
        # rules from https:#francais.lingolia.com/fr/grammaire/la-phrase/la-phrase-interrogative
        # if subject is a pronoun, invert and add "-t-" or "-"
        # except for first person singular ("je") which is, in some cases, non colloquial (e.g. aime-je or
        # prends-je)
        # if subject is a noun or certain pronouns, the subject stays but add a pyrealb pronoun
        proLikeNoun = ["aucun", "beaucoup", "ça", "ceci", "cela", "celui-ci", "celui-là", "quelqu'un", "tout"]
        subjIdx = self.getIndex(["NP", "N", "Pro", "SP", "CP"])
        if subjIdx >= 0:
            subj = self.elements[subjIdx]
            if subj.isA("Pro") and subj.lemma not in proLikeNoun:
                if subj.getProp("pe") == 1 and subj.getProp("n") == "s":  # add "est-ce que" at the start
                        # unless the verb is one of "ai, dis, dois, fais, puis, sais, suis, vais, veux, vois"
                        # according to https://www.academie-francaise.fr/questions-de-langue#42_strong-em-inversion
                        # -du-sujet-je-puis-je-em-strong
                        v = self.getFromPath([["VP",""],["V"]]) # find the verb
                        if v.getProp("t")=="p" and v.getProp("pe")==1:
                            if v.lemma not in ["avoir","dire","devoir","faire","pouvoir","savoir","être","aller",
                                               "vouloir","voir"]:
                                self.add(Q("est-ce que"), subjIdx)
                                return
                pro = self.removeElement(subjIdx)  # remove subject pronoun
            elif int_ in ["wod", "wad"]:  # special cases when inversion gives strange results
                self.add(Q("est-ce que"), subjIdx)
                return
            elif subj.isA("CP"):
                pro = Pro("moi", "fr").c("nom").g("m").n("p").pe(
                    3)  # create a "standard" pronoun, to be patched by cpReal
                subj.pronoun = pro  # add a flag to be processed by cpReal
            else:
                pro = Pro("moi", "fr").g(subj.getProp("g")).n(subj.getProp("n")).pe(3).c("nom")  # create a pronoun
            (idx, vpElems) = self.getIdxCtx("VP", "V")
            if idx is not None:
                v = vpElems[idx]
                v.parentConst.addElement(pro, idx + 1)  # add pronoun after verb
                v.lier()  # add - after verb

    def passive_subject_par(self, cmp, pp):
        # check for passive subject starting with par
        idx, ppElems = self.getIdxCtx("VP", "PP")
        if idx is not None:
            pp = ppElems[idx].getConst("P")
            if pp is not None and pp.lemma == "par":
                cmp = ppElems[0].parentConst.removeElement(idx)  # remove the passive subject
            else:
                pp = None
        return cmp, pp

    # all prepositions from getLexicon-en|fr.js (used for implementing int:"woi|wai|whn|whe"
    # tail +2 getLexicon-en|fr.js | jq 'to_entries | map(select(.value|has("P"))|.key )'
    def preposition_list(self):
        return dict(all={"à", "après", "avant", "avec", "chez", "contre", "d'après", "dans", "de", "dedans", "depuis",
                         "derrière", "dès", "dessous", "dessus", "devant", "durant", "en", "entre", "hors", "jusque",
                         "malgré",
                         "par", "parmi", "pendant", "pour", "près", "sans", "sauf", "selon", "sous", "sur", "vers",
                         "via",
                         "voilà"},
                    whe={"après", "avant", "chez", "dans", "dedans", "derrière", "dessous", "dessus", "devant", "entre",
                         "hors",
                         "près", "sous", "sur", "vers", "via"},
                    whn={"après", "avant", "depuis", "dès", "durant", "en", "pendant"}
                    )

    def interrogative_pronoun_woi(self, int_):
        return ("qui" if int_ == "woi" else "quoi")


