
# tables des positions des clitiques en français, tirées de
#    Choi-Jonin (I.) & Lagae (V.), 2016, « Les pronoms personnels clitiques », in Encyclopédie Grammaticale du Français,
#    en ligne : http:#encyclogram.fr

#  section 3.1.1. (http:#encyclogram.fr/notx/006/006_Notice.php#tit31)

proclitiqueOrdre = {  # page 11 du PDF
    # premier pronom que nous ignorons pour les besoins de cette application
    # "je":1, "tu":1, "il":1, "elle":1, "on":1, "on":1, "nous":1, "vous":1, "vous":1, "ils":1, "elle":1,
    "ne": 2,
    "me": 3, "te": 3, "se": 3, "nous": 3, "vous": 3,
    "le": 4, "la": 4, "les": 4,
    "lui": 5, "leur": 5,
    "y": 6,
    "en": 7,
    "*verbe*": 8,
    "pas": 9,  # S'applique aussi aux autre négations... plus, guère
}

proclitiqueOrdreImperatifNeg = {  # page 14 du PDF
    "ne": 1,
    "me": 2, "te": 2, "nous": 2, "vous": 2,
    "le": 3, "la": 3, "les": 3,
    "lui": 4, "leur": 4,
    "y": 5,
    "en": 6,
    "*verbe*": 7,
    "pas": 8,  # S'applique aussi aux autre négations... plus, guère
}

proclitiqueOrdreImperatifPos = {  # page 15 du PDF
    "*verbe*": 1,
    "le": 2, "la": 2, "les": 2,
    "lui": 3, "leur": 3,
    "me": 4, "te": 4, "nous": 4, "vous": 4,
    "y": 5,
    "en": 6,
}

proclitiqueOrdreInfinitif = {  # page 17 du PDF
    "ne": 1,
    "pas": 2,  # S'applique aussi aux autre négations... plus, guère, jamais
    "me": 3, "te": 3, "se": 3, "nous": 3, "vous": 3,
    "le": 4, "la": 4, "les": 4,
    "lui": 5, "leur": 5,
    "y": 6,
    "en": 7,
    "*verbe*": 8,
}


class NonTerminalFr:
    def word_last(self):
        return "dernier"

    def adj_def_pos(self):
        return "post"

    def passive_pronoun_subject(self, subject):
        from .utils import Pro
        if subject.lemma == "je":
            return Pro("moi").tn("").g(subject.getProp("g")) \
                .n(subject.getProp("n")).pe(subject.getProp("pe"))
        return subject.getTonicPro()

    def passive_dummy_subject(self):
        return "lui"

    def passive_context(self):
        return "contexte passif"

    def passive_should_link_subject(self):
        return False

    def passive_prep(self, test):
        return "de" if test else "par"

    def passive_human_object(self, int, cmp):
        return False

    def should_add_interrogative_prefix(self, int_):
        return True

    def and_conj(self):
        return "et"

    # In a VP, place the first consecutive adverbs at a correct position according to the rules of French
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
        # find first consecutive adverbs (ignoring "not" or "ne")
        advIdxes = [i for (i, e) in zip(range(start, len(res)), res[start:])
                    if e.isA("Adv") and e.lemma != "ne"]
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
                        if res[auxIdx + 1].lemma in auxMods:
                            # another French modal ()
                            moveTo(advIdx, len(advIdxes), auxIdx + 2)
                        else:
                            moveTo(advIdx, len(advIdxes), auxIdx + 1)
                    else:
                        # check for infinitive verb (the adverb should go before it)
                        infinitiveFound = False
                        for idx in range(advIdx - 1, auxIdx, -1):
                            if "t" in res[idx].props and res[idx].props["t"] == "b":
                                moveTo(advIdx, len(advIdxes), idx)
                                infinitiveFound = True
                                break
                        if not infinitiveFound:
                            # check for inverted pronoun (added by .typ("int":"yon")
                            if res[auxIdx + 1].isA("Pro") and res[auxIdx + 2].isA("V"):
                                moveTo(advIdx, len(advIdxes), auxIdx + 2)
                    break

        if advIdx >= start + 2 and "pos" not in advTerminal.props:
            # do not touch adverb with pos specified
            # https:#fr.tsedryk.ca/grammaire/presentations/adverbes/4_La_place_de_l_adverbe.pdf (page 3)
            # place immediately after the auxiliary
            advLemma = advTerminal.lemma
            if advLemma.endswith("ment"): return;  # adverbe qui finit en -ment, laisser après le verbe
            #  adverbes de temps et de lieu qu'il faut laisser après le verbe
            #  extraits d'une liste de types d'adverbes à https:#www.scribbr.fr/elements-linguistiques/adverbe/
            tempsAdv = ["hier", "demain", "longtemps", "aujourd'hui", "tôt", "tard", "auparavant", "autrefois"]
            lieuAdv = ["ici", "là", "là-bas", "là-haut", "ailleurs", "autour", "derrière", "dessus", "dessous",
                       "devant",
                       "dedans", "dehors", "loin", "près", "alentour", "après", "avant", "partout",
                       "où", "partout", "au-dessus", "au-dessous", "au-devant", "nulle part", "quelque part"]
            if advLemma in tempsAdv or advLemma in lieuAdv: return
            if len(advLemma) <= 6 or advLemma in ["toujours", "souvent"]:
                # adverbe court ou commun: déjà, très, trop, toujours, souvent ...
                moveAfterAux(["avoir", "être", "vouloir", "devoir", "savoir"])

    def doPronounPlacement(self, cList):
        from .utils import Adv, Pro, Q
        iDeb = 0
        i = iDeb
        while i < len(cList):
            c = cList[i]
            if c.isA("V") and hasattr(c, "neg2"):
                if hasattr(c, "isMod") or hasattr(c, "isProg"):
                    if c.getProp("lier"):
                        c.insertReal(cList, Q(c.neg2, "fr"), i + 2)
                    else:
                        c.insertReal(cList, Q(c.neg2, "fr"), i + 1)
                    c.insertReal(cList, Adv("ne", "fr"), i)
                    del c.neg2  # remove negation from the original verb
                    iDeb = i + 3  # skip these in the following loop
                    if hasattr(c, "isProg"): iDeb += 2  # skip "en train","de"
                    break
            i += 1
        # gather verb position and pronouns coming after the verb possibly adding a reflexive pronoun
        verbPos = None
        prog = None
        neg2 = None
        pros = []
        i = iDeb
        while i < len(cList):
            c = cList[i]
            if c.isA("V"):
                if verbPos is None:
                    if hasattr(c, "isProg") or hasattr(c, "isMod"):
                        if hasattr(c, "isProg"): prog = c
                        i += 1
                        continue
                    # if c.getProp("lier") and not hasattr(c,"neg2"): #// do not change anything when a verb is lié
                    #     return
                    verbPos = i
                    # find the appropriate clitic table to use
                    t = c.getProp("t")
                    if t == "ip":
                        cliticTable = proclitiqueOrdreImperatifNeg if hasattr(c, "neg2") \
                            else proclitiqueOrdreImperatifPos
                    elif t == "b":
                        cliticTable = proclitiqueOrdreInfinitif
                    else:
                        cliticTable = proclitiqueOrdre
                    # check for negation
                    if hasattr(c, "neg2") and c.neg2 is not None:
                        c.insertReal(pros, Adv("ne", "fr"))
                        if t == "b":
                            c.insertReal(pros, Q(c.neg2, "fr"))
                        else:
                            neg2 = c.neg2
                            del c.neg2
                    if c.isReflexive() and c.getProp("t") != "pp":
                        if prog is not None: c = prog
                        c.insertReal(pros,
                                     Pro("moi", "fr").c("refl").pe(c.getProp("pe")).n(c.getProp("n")).g(c.getProp("g")))
                i += 1
            elif c.isA("Pro") and verbPos is not None:
                if (not c.realization.endswith("'")
                        and (c.getProp("pos") is None or (c.parentConst is not None and c.parentConst.getProp("pos") is None))):
                    # do not try to change position of a constituent with specified pos or with an elided realization
                    if c.getProp("c") in ["refl", "acc", "dat"] or c.lemma == "y" or c.lemma == "en":
                        pros.append(cList.pop(i))
                    elif c.lemma in ["qui", "que", "quoi", "dont", "où"]:  # do not cross boundary of a relative
                        break
                    else:
                        i += 1
                else:
                    i += 1
            elif c.isA("P", "C", "Adv") and verbPos is not None:
                # HACK: stop when seeing a preposition or a conjunction
                #          or a "strange" pronoun that might start a phrase
                #       whose structure has been flattened at this stage
                if c.lemma == "par" and i < len(cList) - 1 and cList[i + 1].isA("Pro"):
                    # if "par"  followed by a Pro is encountered (probably for passive), keep them together
                    i += 2
                else:
                    break
            else:
                i += 1
        if verbPos is None: return
        # add ending "pas" after the verb unless it is "lié" in which cas it goes after the next word
        if neg2 is not None:
            vb = cList[verbPos]
            vb.insertReal(cList, Q(neg2, "fr"), verbPos + (2 if vb.getProp("lier") else 1))
        if len(pros) > 1:
            pros.sort(key=lambda pro: cliticTable[pro] if pro in cliticTable else 100)
        # insert pronouns before the verb except for proclitiqueOrdreImperatifPos
        prosPos = verbPos
        if cliticTable["*verbe*"] == 1 : prosPos+=1
        cList[prosPos:prosPos] = pros

    def tag_question(self, types):
        # in French really simple, add "n'est-ce pas"
        return self.a(", n'est-ce pas")
