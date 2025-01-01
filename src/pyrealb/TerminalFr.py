from .ConstituentFr import ConstituentFr
from .Terminal import Terminal
from .Lexicon import getLexicon, getRules

class TerminalFr(ConstituentFr,Terminal):
    def thousands_separator(self):
        return " "

    def grammaticalNumber(self):
        res = super().grammaticalNumber()
        if res is not None: return res
        # according to http:#bdl.oqlf.gouv.qc.ca/bdl/gabarit_bdl.asp?id=1582
        return "s" if -2 < self.value < 2 else "p"

    def decline_adj_adv(self, rules, declension, stem):
        from .utils import A, D, Adv
        # special case of French adjectives or adv, they can have more than one token
        g = self.getProp("g")
        n = self.getProp("n")
        ending = self.bestMatch("déclinaison d'adjectif", declension, {"g": g, "n": n})
        if ending is None:
            return [self.morphoError("decline [fr]: A", {"g": g, "n": n})]
        f = self.getProp("f")  # comparatif d'adjectif
        if f is not None and f != False:
            specialFRcomp = {"bon": "meilleur", "mauvais": "pire"}
            res = []
            if f == "co":
                if self.lemma in specialFRcomp:
                    self.insertReal(res, A(specialFRcomp[self.lemma]).g(g).n(n))
                else:
                    self.insertReal(res, Adv("plus"))
                    self.insertReal(res, A(self.lemma).g(g).n(n))
            elif f == "su":
                self.insertReal(res, D("le").g(g).n(n))
                if self.lemma in specialFRcomp:
                    self.insertReal(res, A(specialFRcomp[self.lemma]).g(g).n(n))
                else:
                    self.insertReal(res, Adv("plus"))
                    self.insertReal(res, A(self.lemma).g(g).n(n))
            return res
        else:
            self.realization = self.stem + ending
            return [self]

    def check_bad_pronoun_case(self, c):
        if c == "gen":  # genitive cannot be used in French
            self.warn("ignored value for option", "c", c)
            return True
        return False

    def should_set_person_number(self, c):
        return True

    def declension_word(self):
        return "déclinaison"

    def noun_always_plural(self):
        return ['n1','n15','n21','n22','n26']

    def check_gender_lexicon(self, g, n):
        if self.isA("N"):
            # check is French noun gender specified corresponds to the one given in the lexicon
            lexiconG = getLexicon("fr")[self.lemma]["N"]
            if "g" not in lexiconG:
                return [self.morphoError("genre absent du lexique", {"g": g, "n": n})]
            lexiconG = lexiconG["g"]
            if lexiconG != "x" and lexiconG != g:
                return [self.morphoError(
                    "genre différent de celui du lexique", {"g": g, "lexique": lexiconG})]
        return None

    def check_countable(self):
        pass

    def check_majestic(self,keyVals):
        if self.isA("D"):
            if self.lemma == "mon" and keyVals["pe"]<3:
                self.setLemma("notre")
                return True
            if self.lemma == "ton" or (self.lemma == "notre" and keyVals["pe"]==2 and keyVals["n"]=="s"):
                self.setLemma("votre")
                return True
        return False


    def conjugate(self):
        from .utils import V, Pro
        pe = self.getProp("pe")
        pe = 3 if pe is None else int(pe)
        g = self.getProp("g")
        n = self.getNumber()
        t = self.getProp("t")
        if self.tab is None:
            return [self.morphoError("conjugate_fr:tab", {"pe": pe, "n": n, "t": t})]
        if t in ["pc", "pq", "cp", "pa", "fa", "spa", "spq", "bp"]:  # temps composés
            tempsAux = {"pc": "p", "pq": "i", "cp": "c", "pa": "ps", "fa": "f", "spa": "s", "spq": "si", "bp": "b"}[
                t]
            aux = V("avoir", "fr")
            aux.parentConst = self.parentConst
            aux.peng = self.peng
            aux.taux = {"t": self.taux["t"],
                        "aux": self.taux["aux"]}  # separate tense of the auxiliary from the original
            if self.isReflexive():
                aux.setLemma("être")  # réflexive verbs must use French "être" auxiliary
                aux.setProp("pat", ["réfl"])  # set reflexive for the auxiliary
            elif aux.taux["aux"] == "êt":
                aux.setLemma("être")
            else:  # auxiliary "avoir"
                # check the gender and number of a cod appearing before the verb to do proper agreement
                # of its part participle, except when the verb is "être" which will always agree
                g = "m"
                n = "s"
                if self.lemma != "être":
                    if hasattr(self, "cod"):
                        g = self.cod.getProp("g")
                        n = self.cod.getProp("n")
            aux.taux["t"] = tempsAux
            aux.realization = aux.realize()
            # change this verb to pp
            pp = V(self.lemma, "fr")
            pp.setProp("g", g)
            if self.isMajestic():
                pp.setProp("n",self.peng["n"])  # HACK: keep original number (ignoring maje)
            else:
                pp.setProp("n", n)
            pp.setProp("t", "pp")
            pp.realization = pp.realize()  # realize the pp using jsRealB without other options
            self.realization = pp.realization  # set verb realization to the pp realization
            if hasattr(self, "neg2"):
                aux.neg2 = self.neg2  # save this flag to put on the auxiliary,
                del self.neg2  # delete it on this verb
            if self.getProp("lier"):
                aux.lier(True)  # put this flag on the auxiliary
                del self.props["lier"]  # delete it from the verb
                # HACK: check if the verb was lié to a nominative pronoun (e.g. subject inversion for a question)
                myParent = self.parentConst
                if myParent is not None:
                    if hasattr(myParent, "elements"):  # when dealing with a Phrase
                        myParentElems = myParent.elements
                        idxMe = myParentElems.index(self)
                        if idxMe >= 0 and idxMe < len(myParentElems) - 1:
                            idxNext = idxMe + 1
                            next = myParentElems[idxNext]
                            if next.isA("Pro"):
                                thePro = myParentElems.pop(idxNext)  # remove next pro from parent
                                thePro.realization = thePro.realize()  # insert its realization after the auxiliary
                                # and before the verb
                                return [aux, thePro, self]
                    elif hasattr(myParent, "dependents"):  # when dealing with a Dependent
                        proIndex = myParent.findIndex(lambda d: d.terminal.isA("Pro"))
                        if proIndex >= 0:
                            thePro = myParent.removeDependent(proIndex).terminal  # remove Pro from Parent
                            # as the original Pro is already realized in the output list, we must hack
                            thePro2=thePro.clone()
                            thePro2.realize()
                            # and before the verb
                            thePro.realization = ""  # set original Pro realization to nothing
                            return [aux, thePro2, self]
                    else:
                        self.error("Terminal.conjugate_fr:: Strange parent:" + type(myParent).__name__)
            return [aux, self]
        else:  # simple tense
            conjugationTable = getRules(self.lang())["conjugation"][self.tab]
            if "t" in conjugationTable and t in conjugationTable["t"]:
                conjugation = conjugationTable["t"]
                if t in ["p", "i", "f", "ps", "c", "s", "si"]:
                    term = conjugation[t][pe - 1 + (3 if n == "p" else 0)]
                    if term is None:
                        return [self.morphoError("conjugate_fr", {"pe": pe, "n": n, "t": t})]
                    else:
                        self.realization = self.stem + term
                    res = [self]
                    if self.parentConst is None and self.isReflexive():
                        self.insertReal(res, Pro("moi", "fr").c("refl").pe(pe).n(n).g(g), 0)
                    return res
                elif t == "ip":
                    if (n == "s" and pe != 2) or (n == "p" and pe == 3):
                        return [self.morphoError("conjugate_fr", {"pe": pe, "n": n, "t": t})]
                    term = conjugation[t][pe - 1 + (3 if n == "p" else 0)]
                    if term is None:
                        return [self.morphoError("conjugate_fr", {"pe": pe, "n": n, "t": t})]
                    else:
                        self.realization = self.stem + term
                    res = [self]
                    if self.isReflexive() and self.parentConst is None:
                        self.lier()
                        self.insertReal(res, Pro("moi", "fr").tn("").pe(pe).n(n).g(g))
                    return res
                elif t == "pp":
                    x = self.cod if hasattr(self, "cod") else self
                    g = x.getProp("g")
                    if g == "x" or g == "n": g = "m"  # neutre peut arriver si le sujet est en anglais
                    n = x.getProp("n")
                    if n == "x": n = "s"
                    if (self.isMajestic()): n = self.getNumber();
                    idx = 0 if n=="s" else 2
                    if g =="f": idx += 1
                    termPP = conjugation[t][idx]
                    if termPP is None:
                        return [self.morphoError("conjugate_fr", {"pe": pe, "n": n, "t": t})]
                    if idx > 0:
                        pat = self.getProp("pat")
                        if pat is not None and len(pat) == 1 and pat[0] == "intr" and self.getProp("aux") == "av":
                            # ne pas conjuguer un pp d'un verbe intransitif avec auxiliaire avoir
                            return [self.morphoError("conjugate_fr", {"pe": pe, "n": n, "t": t})]
                    self.realization = self.stem+termPP
                    return [self]
                elif t in ["b", "pr"] and t in conjugation:
                    self.realization = self.stem + conjugation[t]
                    res = [self]
                    if self.isReflexive() and self.parentConst is None:
                        self.insertReal(res, Pro("moi", "fr").c("refl").pe(pe).n(n).g(g), 0)
                    return res
                else:
                    return [self.morphoError("conjugate_fr", {"pe": pe, "n": n, "t": t})]
            else:
                return [self.morphoError("conjugate_fr", {"pe": pe, "n": n, "t": t})]

    def numberOne(self):
        if self.peng["g"] == "f":
            if self.value == 1: return "une"
            if self.value == -1: return "moins une"
        return None
