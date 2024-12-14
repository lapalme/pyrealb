from .ConstituentEn import ConstituentEn
from .NonTerminalEn import NonTerminalEn
from .Dependent import Dependent
from .Lexicon import getRules

class DependentEn(ConstituentEn,NonTerminalEn,Dependent):
    def linkAttributes(self, depTerm, headTerm):
        pass

    def check_determiner_cnt(self,det):
        if det.lemma == "a" and self.terminal.getProp("cnt")=="no":
            det.morphoError("The indefinite determiner cannot be linked with an uncountable noun", self.terminal.lemma)

    def link_pp_before(self, dep, headTerm):
        pass

    def link_pp_with_head(self, depTerm):
        pass

    def passive_agree_auxiliary(self, obj):
        pass

    def check_passive_subject_with_par(self):
        return None

    # Pronominalization in English only applies to a N (self is checked before the call)
    #  and does not need reorganisation of the sentence
    #  Does not currently deal with "Give the book to her." that {c|sh}ould be "Give her the book."
    def pronominalize(self):
        if not self.terminal.isA("N"):
            return self.warn("no appropriate pronoun")
        self.props["pe"] = 3  # ensure that pronominalization of a noun is 3rd person
        if self.parentConst is None or self.isA("subj"):  # is it a subject
            pro = self.getTonicPro("nom")
        else:
            pro = self.getTonicPro("acc")  # is direct complement
        pro.peng = self.peng
        pro.parentConst = self
        self.terminal = pro
        self.dependents = []
        self.dependentsSource = []

    def processTyp_verb(self, types):
        # replace current verb with the list new words
        #  TODO: take into account the fact that there might be already a verb with modals...
        if "contr" in types and types["contr"] is not False:
            # necessary because we want the negation to be contracted within the VP before the S or SP
            self.contraction = True
        words = self.affixHopping(self.terminal, self.getProp("t"), getRules()["compound"], types)
        # the new root should be the last verb
        last = words.pop()
        if last.isA("Pro") and last.lemma == "myself":  # skip possible "myself" for reflexive verb
            self.addPost(last)
            last = words.pop()
        self.terminal = last
        self.addPre(words)

    def move_object(self,int_):
        auxIdx = self.findIndex(lambda d: d.isA("*pre*"))  # added by affixHopping
        if auxIdx >= 0 and self.getProp("t") not in ["pp", "pr"]:  # do not move when tense is participle
            aux = self.dependents[auxIdx].terminal
            self.removeDependent(auxIdx)
            self.addPre(aux, 0)  # put auxiliary before
        elif self.terminal.lemma in ["be", "have"]:
            # no auxiliary, but check for have or be "alone" for which the subject should appear after the aux
            subjIdx = self.findIndex(lambda d: d.isA("subj"))
            if subjIdx >= 0:
                self.dependents[subjIdx].pos("post")

    def tag_question(self, types):
        from .utils import Pro, V, Adv
        from .utils import subj, comp, mod
        # in English, sources: https://www.anglaisfacile.com/exercices/exercice-anglais-2/exercice-anglais-95625.php
        # must find  the pronoun and conjugate the auxiliary
        # look for the first verb or auxiliary (added by affixHopping)
        vIdx = self.findIndex(lambda d: d.terminal.isA("V") and d.depPosition() == "pre")
        currV = self.terminal if vIdx < 0 else self.dependents[vIdx].terminal
        if "mod" in types and types["mod"] != False:
            aux = getRules("en")["compound"][types["mod"]]["aux"]
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
        pro = Pro("I").pe(pe).n(n).g(g)  # default pronoun
        subjIdx = self.findIndex(lambda d: d.isA("subj"))
        # check for negative adverb
        advIdx = self.findIndex(lambda d: d.isA("mod") and d.terminal.isA("Adv"))
        if advIdx >= 0 and self.dependents[advIdx].terminal.lemma in ["hardly", "scarcely", "never", "seldom"]:
            neg = True
        if subjIdx >= 0:
            subject = self.dependents[subjIdx].terminal
            if subject.isA("Pro"):
                if subject.getProp("pe") == 1 and aux == "be" and t == "p" and not neg:
                    pe = 2  # I am => aren't I
                elif subject.lemma in ["this", "that", "nothing"]:
                    pro = Pro("I").g("n")  # it
                elif subject.lemma in ["somebody", "anybody", "nobody", "everybody",
                                       "someone", "anyone", "everyone"]:
                    pro = Pro("I").n("p")  # they
                    if subject.lemma == "nobody": neg = True
                else:
                    pro = subject.clone()
                pro = subj(pro).pos("post")
            elif subject.isA("N"):
                pro = self.dependents[subjIdx].clone().pro().pos("post")
                pro.g(subject.getProp("g")).n(subject.getProp("n"))  # ensure proper number and gender
            else:
                # must wrap into comp("",...) to force pronominalization of children
                pro = subj(Pro("it").c("nom")).pos("post")
        else:  # no subject, but check if the verb is imperative
            if t == "ip":
                if aux == "do": aux = "will"  # change aux when the aux is default
                pro = Pro("I").pe(2).n(n).g(g)
            else:
                pro = Pro("it").c("nom")
            pro = subj(pro).pos("post")
        iDeps = len(self.dependents) - 1
        while iDeps >= 0 and self.dependents[iDeps].depPosition() != "post":
            iDeps -= 1
        if iDeps < 0:  # add comma to the verb
            currV.a(",")
        else:  # add comma to the last current dependent
            self.dependents[iDeps].a(",")
        # nice use-case of jsRealB using itself for realization
        if aux == "have" and not neg:
            # special case because it should be realized as "have not" instead of "does not have"
            self.addDependent(comp(V("have").t(t).pe(pe).n(n),
                                   mod(Adv("not")), pro).typ({"contr": True}))
        else:
            self.addDependent(comp(V(aux).t(t).pe(pe).n(n),
                                   pro).typ({"neg": not neg, "contr": True}))