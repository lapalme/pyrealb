from .ConstituentEn import ConstituentEn
from .Terminal import Terminal
from .Lexicon import getLexicon, getLemma, getRules

class TerminalEn(ConstituentEn,Terminal):
    def thousands_separator(self):
        return ","

    def noun_always_plural(self):
        return ['n6']

    def grammaticalNumber(self):
        res = super().grammaticalNumber()
        if res is not None: return res
        # according to https://www.chicagomanualofstyle.org/book/ed17/part2/ch09/psec019.html
        #   any number other than 1 is plural...
        # even 1.0 but this case is not handled here because nbDecimal(1.0)=>0
        return "s" if abs(self.value) == 1 and self.nbDecimals == 0 else "p"

    def decline_adj_adv(self, rules, declension, stem):
        from .utils import Adv
        # English adjective/adverbs are invariable but they can have comparative, thus return more than one token
        self.realization = self.lemma
        f = self.getProp("f")
        if f is not None and f != False:
            if self.tab == "a1":
                comp = Adv("more" if f == "co" else "most")
                comp.realization = comp.lemma
                return [comp, self]
            else:
                if self.tab == "b1":  # adverb without comparative/superlative, try the adjective table
                    adjAdv = getLemma(self.lemma)
                    if "A" in adjAdv:
                        declension = rules["declension"][adjAdv["A"]["tab"]]["declension"]
                        ending = rules["declension"][adjAdv["A"]["tab"]]["ending"]
                        stem = stem[0:-len(ending)]
                    else:  # adverb without adjective
                        return [self]
                # look in the adjective declension table
                ending = self.bestMatch("adjective declension", declension, {"f": f})
                if ending is None:
                    return [self.morphoError("decline [en]: A", {"f": f})]
                self.realization = self.stem + ending
                return [self]
        return [self]

    def check_bad_pronoun_case(self, c):
        if c == "refl":  # réfléchi cannot be used in English
            self.warn("ignored value for option", "c", c)
            return True
        return False

    def should_set_person_number(self, c):
        return c != "gen"

    def declension_word(self):
        return "declension"

    def check_gender_lexicon(self, g, n):
        return None

    def check_countable(self):
        lexiconCnt = getLexicon(self.lang())[self.lemma]["N"]["cnt"]
        if lexiconCnt == "no":
            return [self.morphoError("An uncountable noun cannot be set to plural","")]
        return None

    def check_majestic(self,keyVals):
        if self.isA("D") and keyVals["pe"]<3:
            if self.lemma == "my" and self.getProp("own")=="s":
                self.setProp("own","p")
                return True
        return False

    def conjugate(self):
        from .utils import V, P, Q
        pe = self.getProp("pe")
        pe = 3 if pe is None else int(pe)
        n = self.getNumber()
        t = self.getProp("t")
        if self.tab is None:
            return [self.morphoError("conjugate_en:tab", {"pe": pe, "n": n, "t": t})]
        conjugationTable = getRules(self.lang())["conjugation"][self.tab]
        res = [self]
        if "t" in conjugationTable and t in conjugationTable["t"]:
            conjugation = conjugationTable["t"][t]
            if t in ["p", "ps", "s", "si"]:
                if isinstance(conjugation, str):
                    self.realization = self.stem + conjugation
                    return [self]
                term = conjugation[pe - 1 + (3 if n == "p" else 0)]
                if term is None:
                    return [self.morphoError("conjugate_en:tab", {"pe": pe, "n": n, "t": t})]
                else:
                    # remove final s at subjonctive present by taking the form at the first person
                    if t == "s" and pe == 3: term = conjugation[0]
                    self.realization = self.stem + term
                    return [self]
            elif t in ["b", "pp", "pr"]:
                self.realization = self.stem + conjugation
                return [self]
        elif t == "s":
            # subjonctive present is like plain verb form
            self.realization = self.lemma
        elif t == "si":
            # subjonctive past is like simple past, except for "be" 1st and 3rd person => were
            if self.lemma == "be" : self.realization = "were"
            else: self.realization = self.stem + getRules(self.lang())["conjugation"][self.tab]["t"]["ps"]
        elif t == "f":
            self.realization = self.lemma
            self.insertReal(res, V("will"), 0)
        elif t == "c":
            self.realization = self.lemma
            self.insertReal(res, V("will").t("ps"), 0)
        elif t == "bp" or t == "bp-to":
            if t in conjugationTable and "pp" in conjugationTable.t:
                self.realization = self.stem + conjugationTable.t["pp"]
            else:
                self.realization = self.lemma
            self.insertReal(res, V("have").t("b"), 0)
            if t == "bp-to":
                self.insertReal(res, P("to"), 0)
        elif t == "b-to":
            self.realization = self.lemma
            self.insertReal(res, P("to"), 0)
        elif t == "ip":
            self.realization = self.lemma
            if pe == 1 and n == "p":
                self.insertReal(res, Q("let's"), 0)
        else:
            return [self.morphoError("conjugate_en:tab", {"pe": pe, "n": n, "t": t})]
        return res

    def numberOne(self):
        return None
