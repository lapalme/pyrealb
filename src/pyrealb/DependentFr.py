from .ConstituentFr import ConstituentFr
from .NonTerminalFr import NonTerminalFr
from .Dependent import Dependent
from .Lexicon import getRules

class DependentFr(ConstituentFr,NonTerminalFr,Dependent):
    def linkAttributes(self, depTerm, headTerm):
        # check for an attribute of a copula with an adjective or past participle
        if headTerm.lemma in ["être", "paraître", "sembler", "devenir", "rester"]:
            iSubj = self.findIndex(lambda d0: d0.isA("subj") and d0.terminal.isA("N", "Pro"))
            if iSubj >= 0:
                depTerm.peng = self.dependents[iSubj].peng

    def check_determiner_cnt(self, det):
        pass

    def link_pp_before(self, dep, headTerm):
        depTerm = dep.terminal
        # rel is comp or mod
        # in French past participle can agree with a cod appearing before... keep that info in case
        depTerm.cod = headTerm
        # HACK: check for a "temps composé" formed by "avoir" followed by a past participle
        if depTerm.lemma == "avoir":
            iVerb = dep.findIndex(lambda depI: depI.isA("comp") and
                                               depI.terminal.isA("V") and
                                               depI.terminal.getProp("t") == "pp")
            if iVerb >= 0:
                dep.dependents[iVerb].terminal.cod = headTerm

    def link_pp_with_head(self, depTerm):
        # check for past participle in French that should agree with the head
        if depTerm.getProp("t") == "pp":
            depTerm.peng = self.peng

    def passive_agree_auxiliary(self, obj):
        from .utils import V
        from .utils import dep
        # do this only for French because in English this is done by processTyp_en
        # change verbe into an "être" auxiliary and make it agree with the newSubj
        # force person to be 3rd (number and tense will come from the new subject)
        verbe = self.terminal.lemma
        self.terminal.setLemma("avoir" if verbe == "être" else "être")
        if self.getProp("t") == "ip":
            self.t("s")  # set subjonctive present tense for an imperative
        pp = V(verbe, "fr").t("pp")
        if obj is not None:  # self can be undefined when a subject is Q or missing
            self.terminal.peng = obj.peng
            pp.peng = obj.peng
        # insert the pp before the comp, so that it appears immediately after the verb
        #  calling addPost(pp) would not put it at the right place
        compIdx = self.findIndex(lambda d: d.isA("comp", "mod"))
        if compIdx == -1: compIdx = 0
        self.addDependent(dep([pp], "*post*"), compIdx)

    def check_passive_subject_with_par(self):
        # check for passive subject starting with par
        parIdx = self.findIndex(
            lambda d: d.isA("comp") and d.terminal.isA("P") and d.terminal.lemma == "par")
        pp = None
        if parIdx >= 0:
            pp = self.dependents[parIdx].terminal
            self.removeDependent(parIdx)  # remove the passive subject
        return pp

    # Dependency structure modification but that must be called in the context of the parentConst
    # because the pronoun depends on the role of the N in the sentence
    #         and its position can also change relatively to the verb
    def pronominalize(self):
        from .utils import Pro
        mySelf = self
        if self.isA("subj"):
            if not self.terminal.isA("N", "Pro"):
                return self.warn("no appropriate pronoun")
            pro = self.getTonicPro("nom")
        elif self.isA("comp", "mod") and self.terminal.isA("P"):
            prep = self.terminal.lemma
            if len(self.dependents) == 1 and self.dependents[0].isA("comp", "mod"):
                if self.dependents[0].terminal.isA("N"):
                    n = self.dependents[0].terminal
                    if prep == "à":
                        pro = n.getTonicPro("dat")
                    elif prep == "de":
                        pro = Pro("en", "fr").c("dat")
                    elif prep in ["sur", "vers", "dans"]:
                        pro = Pro("y", "fr").c("dat")
                    else:  # change only the N keeping the P intact
                        pro = self.getTonicPro("nom")
                        mySelf = self.dependents[0]
                else:
                    return self.warn("no appropriate pronoun")
        else:
            pro = self.getTonicPro("acc")
            if self.parentConst is not None and self.parentConst.terminal.isA(
                    "V"):  # consider that it is direct complement
                self.parentConst.terminal.cod = self  # indicate that self is a COD
        # replace the original with the pronoun
        pro.parentConst = self
        if hasattr(mySelf, "peng"):
            pro.peng = mySelf.peng
        mySelf.terminal = pro
        mySelf.dependents = []
        mySelf.dependentsSource = []

    def processTyp_verb(self, types):
        from .utils import V, Q
        def progF(deprel, v):
            # insert "en train","de" (separate so that élision can be done...)
            # HACK::but do it BEFORE the pronouns created by .pro()
            origLemma = deprel.terminal.lemma
            deprel.terminal.setLemma(
                "être")  # change verb, but keep person, number and tense properties of the original...
            deprel.addPost([Q("en train"), Q("de"), V(origLemma).t("b")])
            deprel.terminal.isProg = v

        self.processV(types, "prog", progF)

        def modF(deprel, mod):
            rules = getRules()
            origLemma = deprel.terminal.lemma
            for key in rules["verb_option"]["modalityVerb"]:
                if key.startswith(mod):
                    deprel.terminal.setLemma(rules["verb_option"]["modalityVerb"][key])
                    break
            deprel.terminal.isMod = True
            newV = V(origLemma).t("b")
            if hasattr(deprel.terminal, "isProg"):  # copy progressive from original verb...
                newV.isProg = deprel.terminal.isProg
                del deprel.terminal.isProg
            deprel.addPost(newV)

        self.processV(types, "mod", modF)

        def negF(deprel, neg):
            if neg is True: neg = "pas"
            deprel.terminal.neg2 = neg  # HACK: to be used when conjugating at the realization time

        self.processV(types, "neg", negF)

    def move_object(self,int_):
        if not self.terminal.isA("V"):
            return # cannot move if the head is not a verb...
        from .utils import Pro, Q
        from .utils import det
        # in French : use inversion rule which is quite "delicate"
        # rules from https:#francais.lingolia.com/fr/grammaire/la-phrase/la-phrase-interrogative
        # if subject is a pronoun, invert and add "-t-" or "-"
        # except for first person singular ("je") which is, in some cases, non colloquial (e.g. aime-je or
        # prends-je)
        # if subject is a noun or certain pronouns, the subject stays but add a pyrealb pronoun
        proLikeNoun = ["aucun", "beaucoup", "ça", "ceci", "cela", "celui-ci", "celui-là", "quelqu'un", "tout"]
        subjIdx = self.findIndex(lambda d: d.isA("subj"))
        if subjIdx >= 0:
            verb = self.terminal
            subject = self.dependents[subjIdx].terminal
            if subject.isA("Pro") and subject.lemma not in proLikeNoun:
                if subject.getProp("pe") == 1 and subject.getProp("n") == "s":  # add est-ce que at the start
                    # unless the verb is one of "ai, dis, dois, fais, puis, sais, suis, vais, veux, vois"
                    # according to https://www.academie-francaise.fr/questions-de-langue#42_strong-em-inversion
                    # -du-sujet-je-puis-je-em-strong
                    if verb.getProp("t")=="p" and verb.getProp("pe")==1:
                        if verb.lemma not in ["avoir","dire","devoir","faire","pouvoir","savoir","être","aller",
                                               "vouloir","voir"]:
                            self.add(det(Q("est-ce que")), 0)
                            return
                pro = self.removeDependent(subjIdx).terminal  # remove subject
            elif int_ in ["wod","wad"]:
                self.add(det(Q("est-ce que")), 0)
                return
            elif subject.isA("C"):
                pro = Pro("moi", "fr").c("nom").g("m").n("p").pe(
                    3)  # create a "standard" pronoun, to be patched by cpReal
                subject.pronoun = pro  # add a flag to be processed by cpReal
            else:
                pro = (Pro("moi", "fr").g(subject.getProp("g"))
                         .n(subject.getProp("n")).pe(3).c("nom"))  # create a pronoun
            if self.terminal.isA("V"):
                self.addPost(pro)
                self.terminal.lier()
