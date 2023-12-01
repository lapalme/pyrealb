# negation of modal auxiliaries
negMod = {"can": "cannot", "may": "may not", "shall": "shall not", "will": "will not", "must": "must not",
          "could": "could not", "might": "might not", "should": "should not", "would": "would not"}

class NonTerminalEn:
    # shared between PhraseEn and DependentEn
    def word_last(self):
        return "last"

    def adj_def_pos(self):
        return "pre"

    def passive_pronoun_subject(self, subject):
        from .utils import Pro
        if subject.lemma == "I":
            return Pro("me").tn("").g(subject.getProp("g")) \
                .n(subject.getProp("n")).pe(subject.getProp("pe"))
        return subject.getTonicPro()

    def passive_dummy_subject(self):
        return "it"

    def passive_context(self):
        return "passive context"

    def passive_should_link_subject(self):
        return True

    def passive_prep(self, test):
        return "to" if test else "by"

    def passive_human_object(self, int, cmp):
        return int == "wod" and cmp is not None and cmp.getProp("g") in ["m", "f"]

    def should_add_interrogative_prefix(self, int_):
        return int_ != "yon"

    def and_conj(self):
        return "and"

    def affixHopping(self, v, t, compound, types):
        from .utils import V, Pro, Q, Adv, P
        v_peng = v.peng
        neg = "neg" in types and types["neg"] == True
        # English conjugation
        # it implements the "affix hopping" rules given in
        #      N. Chomsky, "Syntactic Structures", 2nd ed. Mouton de Gruyter, 2002, p 38 - 48
        auxils = []  # list of Aux followed by V
        affixes = []
        isFuture = False
        if t == "f" or t == "c":
            isFuture = True
            t = "p" if t == "f" else "ps"  # the auxiliary will be generated here so remove it from the V
        prog = "prog" in types and types["prog"] != False
        perf = "perf" in types and types["perf"] != False
        pas = "pas" in types and types["pas"] != False
        interro = types["int"] if "int" in types and types["int"] != False else None
        modality = types["mod"] if "mod" in types and types["mod"] != False else None
        if modality is not None:
            auxils.append(compound[modality]["aux"])
            affixes.append("b")
        elif isFuture:
            # caution: future and conditional in English are done with the modal will, so another modal cannot be used
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
        elif (interro is not None and
              len(auxils) == 0 and v.lemma != "be" and v.lemma != "have"):
            # add auxiliary for interrogative if not already there
            if interro not in ["wos", "was", "tag"]:
                if t not in ["pp", "pr", "b-to", "b"]:  # do not add auxiliary for participle and infinitive
                    auxils.append("do")
                    affixes.append("b")
        auxils.append(v.lemma)
        # realise the first verb, modal or auxiliary
        # but make the difference between "have" as an auxiliary and "have" as a verb
        vAux = auxils.pop(0)
        words = []
        # conjugate the first verb
        if neg:  # negate the first verb
            if t in ["pp", "pr", "b-to", "b", "bp", "bp-to"]:  # special case for these tenses
                words.append(Adv("not", "en"))
                if t == "b" or t == "bp": words.append(P("to", "en"))
                words.append(V(vAux, "en").t(t))
            elif t == "ip" and v_peng["pe"] == 1 and v_peng["n"] == "p":
                # very special case: insert "not" between "let's" and verb
                words.append(Q("let's"))
                words.append(Adv("not", "en"))
                words.append(V(vAux, "en").t("b"))
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
            newAux = V(vAux).t(t)
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

    # In a VP, place the first consecutive adverbs at a correct position according to the rules of English.
    # Usually an adverb is set according to either .pos("pre"|"post")
    # The problem occurs mainly with verbs with an auxiliary.
    # TODO: deal with more than one sequence of adverbs (although it should be rare)
    # this method is called by Phrase.real() and Dependent.real()
    # @param {Terminal[]} res : list of Terminals possibly modified in place
    #
    def checkAdverbPos(self, res):
        # move n elements starting at start to position toIdx (shifting the rest)
        def moveTo(startIdx, n, toIdx):
            save = res[startIdx:startIdx + n]
            del res[startIdx:startIdx + n]
            res[toIdx:toIdx] = save

        relpron = self.relative_pronouns()
        # find the start of the current "sentence" in order not to move an adverb across the boundary of a relative
        start = len(res) - 1
        while start >= 0 and not (res[start].isA("Pro") and res[start].lemma in relpron):
            start -= 1
        start += 1
        # find first consecutive adverbs (ignoring "not")
        advIdxes = [i for (i, e) in zip(range(start, len(res)), res[start:])
                    if e.isA("Adv") and e.lemma != "not"]
        if len(advIdxes) == 0:
            return
        advIdx = advIdxes[0]
        advTerminal = res[advIdx]
        # check that the indexes of adverbs are consecutive, remove those that are not
        for i in range(1, len(advIdxes)):
            if advIdxes[i] != advIdxes[i - 1] + 1:
                del advIdxes[i:]
                break

        def moveAfterAux(auxMods):
            for auxIdx in range(0, advIdx - 1):
                e = res[auxIdx]
                if e.isA("V") and e.lemma in auxMods:
                    if res[auxIdx + 1].isA("V"):
                        # there is an auxiliary/modals followed by a verb, insert adverb after the auxiliary
                        # except for "will" and "shall" when used as future auxiliary as indicated in the parentConst
                        if e.lemma == "will" or e.lemma == "shall":
                            if e.parentConst is not None and e.parentConst.getProp("t") == "f":
                                continue
                        moveTo(advIdx, len(advIdxes), auxIdx + 1)
                    else:
                        # in English insert after negation (in French, negation [ne  ... pas] is added after this step)
                        if res[auxIdx + 1].lemma == "not" and res[auxIdx + 2].isA("V"):
                            moveTo(advIdx, len(advIdxes), auxIdx + 2)
                    break

        if advIdx >= start + 2 and "pos" not in advTerminal.props:
            # do not touch adverb with pos specified
            # the adverb must be put after the first auxiliary
            moveAfterAux(["have", "can", "will", "shall", "may", "must"])

    def doPronounPlacement(self, cList):
        pass
