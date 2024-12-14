from .ConstituentEn import ConstituentEn
from .NonTerminalEn import NonTerminalEn
from .Phrase import Phrase
from .Lexicon import getRules

class PhraseEn(ConstituentEn,NonTerminalEn,Phrase):

    def link_DAV_properties(self, e):
        if e.isA("D") and e.lemma == "no":
            # check for "no" as determiner which should add plural in English
            self.peng["n"] = "p"
            return
        if e.isA("A") or (e.isA("D") and "own" not in e.props):
            # link gender and number of the noun to the determiners and adjectives
            # in English possessive determiner should not depend on the noun but on the "owner"
            e.peng = self.peng
            return

    def check_determiner_cnt(self,det,headNoun):
        if det.lemma == "a" and headNoun.getProp("cnt")=="no":
            det.morphoError("The indefinite determiner cannot be linked with an uncountable noun",headNoun.lemma)


    def link_subj_obj_subordinate(self, pro, v, _subject):
        if pro.lemma in ["who", "which", "that"]:
            v.peng = self.peng
            self.linkAttributes(v, self.getFromPath([["VP"], ["CP"]]), self)

    def linkAttributes(self, vpv, vpcp, subject):
        pass

    def check_coordinated_object(self):
        pass

    def should_try_another_subject(self,lemma,_iSubj):
            return lemma == "that"

    # Pronominalization in English only applies to a NP
    #  and does not need reorganisation of the sentence
    def pronominalize(self):
        if not self.isA("NP"):
            return self.warn("bad application", ".pro", ["NP"], self.constType)
        npParent = self.parentConst
        if npParent is not None:
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

    def passive_agree_auxiliary(self, vp, newSubject):
        # in English this is done by processTyp_en
        # change verbe to "être" auxiliary and make it agree with the newSubject
        pass

    def processTyp_verb(self, types):
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
                vp.contraction = True  # necessary because we want the negation to be contracted
                # within the VP before the S or SP
                self.contraction = True
            words = self.affixHopping(v, vp.getProp("t"), getRules()["compound"], types)
            # insert the content of the word array into vp.elements
            vp.removeElement(idxV)
            for i in range(0, len(words)):
                vp.addElement(words[i], idxV + i)
        else:
            self.warn("not found", "V", "VP")

    def move_object(self,int_):
        # in English move the auxiliary to the front
        if self.isA("S", "SP"):
            (idx, vpElems) = self.getIdxCtx("VP", "V")
            if idx is not None and self.getProp("t") not in ["pp", "pr", "b-to"]:
                # do not move when tense is participle or infinitive
                v = vpElems.pop(0)  # remove first V
                self.addElement(v, 0)

    def passive_subject_par(self, cmp, pp):
        return cmp, pp

    # all prepositions from getLexicon-en|fr.js (used for implementing int:"woi|wai|whn|whe"
    # tail +2 getLexicon-en|fr.js | jq 'to_entries | map(select(.value|has("P"))|.key )'
    def preposition_list(self):
        return dict(
            all={"about", "above", "across", "after", "against", "along", "alongside", "amid", "among", "amongst",
                 "around", "as", "at", "back", "before", "behind", "below", "beneath", "beside", "besides",
                 "between", "beyond", "by", "concerning", "considering", "despite", "down", "during", "except",
                 "for", "from", "in", "inside", "into", "less", "like", "minus", "near", "next", "of", "off", "on",
                 "onto", "outside", "over", "past", "per", "plus", "round", "since", "than", "through", "throughout",
                 "till", "to", "toward", "towards", "under", "underneath", "unlike", "until", "up", "upon", "versus",
                 "with", "within", "without"},
            whe={"above", "across", "along", "alongside", "amid", "around", "before", "behind", "below", "beneath",
                 "beside", "besides", "between", "beyond", "in", "inside", "into", "near", "next", "onto", "outside",
                 "over", "past", "toward", "towards", "under", "underneath", "until", "via", "within"},
            whn={"after", "before", "during", "since", "till"}
            )


    def interrogative_pronoun_woi(self, int_):
        return "whom" if int_ == "woi" else "what"

    def tag_question(self, types):
        from .utils import Pro, V, Adv
        from .utils import VP
        # in English, sources: https://www.anglaisfacile.com/exercices/exercice-anglais-2/exercice-anglais-95625.php
        # must find  and pronoun and conjugate the auxiliary
        currV = self.getFromPath(["VP", "V"])
        if currV is not None:
            if "mod" in types and types["mod"] != False:
                aux = getRules()["compound"][types["mod"]]["aux"]
            else:
                if currV.lemma in ["have", "be", "can", "will", "shall", "may", "must"]:
                    aux = currV.lemma
                else:
                    aux = "do"
        neg = "neg" in types and types["neg"] == True
        pe = currV.getProp("pe")
        t = currV.getProp("t")
        n = currV.getProp("n")
        g = currV.getProp("g")
        pro = Pro("I").pe(pe).n(n).g(g)  # get default pronoun
        subjIdx = self.getIndex(["NP", "N", "Pro", "SP"])
        if subjIdx >= 0:
            vbIdx = self.getIndex(["VP", "V"])
            if vbIdx >= 0 and subjIdx < vbIdx:  # subject should be before the verb
                subj = self.elements[subjIdx]
                if subj.isA("Pro"):
                    if subj.getProp("pe") == 1 and aux == "be" and t == "p" and not neg:
                        # very special case : I am => aren't I
                        pe = 2
                    elif subj.lemma in ["this", "that", "nothing"]:
                        pro = Pro("I", "en").g("n")  # it
                    elif subj.lemma in ["somebody", "anybody", "nobody", "everybody",
                                        "someone", "anyone", "everyone"]:
                        pro = Pro("I", "en").n("p")  # they
                        if subj.lemma == "nobody": neg = True
                    else:
                        pro = subj.clone()
                else:
                    pro = subj.clone().pro()
        else:  # no subject, but check if the verb is imperative
            if t == "ip":
                if aux == "do": aux = "will"  # change aux when the aux is default
                pro = Pro("I", "en").pe(2).n(n).g(g)
        # check for negative adverb
        adv = currV.parentConst.getConst("Adv")
        if adv is not None and adv.lemma in ["hardly", "scarcely", "never", "seldom"]:
            neg = True
        currV.parentConst.a(",")
        #   this is a nice illustration of jsRealB using itself for realization
        if aux == "have" and not neg:
            # special case because it should be realized as "have not" instead of "does not have"
            vp = VP(V("have").t(t).pe(pe).n(n), Adv("not"), pro).typ({"contr": True})
        else:  # use jsRealB itself for realizing the tag by adding a new VP
            vp = VP(V(aux).t(t).pe(pe).n(n), pro).typ({"neg": not neg, "contr": True})
        vp.peng = pro.peng  # ensure that the head of the vp is the pronoun for pronominalize_en
        self.addElement(vp)
