import re
from .Lexicon import getLemma
from .Constituent import Constituent

class ConstituentFr:
    def lang(self):
        return "fr"

    def isEn(self):
        return False

    def isFr(self):
        return True

    def defaultProps(self):
        return {"g": "m", "n": "s", "pe": 3, "t": "p", "aux": "av"}

    def initProps(self):
        super().initProps()
        if self.isA("V"):
            self.taux["aux"] = "av"

    def tonic_forms(self):
        return {"toi", "lui", "nous", "vous", "eux", "elle", "elles", "on", "soi"}

    def tonic_pe_1(self):
        return "moi"

    def relative_pronouns(self):
        return ["qui", "que", "dont", "où", "lequel", "auquel","duquel"]

    def relative_pronouns_propagate(self):
        return ["qui", "que", "lequel", "auquel", "duquel"]

    def validate_neg_option(self, val, types):
        if not isinstance(val, (str, bool)):  # also accept string as neg value in French
            self.warn("ignored value for option", f'.typ("neg")', val)
            del types["neg"]
        return True

    # regex for matching the first word in a generated string (ouch!!! it is quite subtle...)
    #  match index:
    #     1-possible non-word chars and optional html tags
    #     2-the real word
    #     3-the rest after the word
    sepWordREC = re.compile(r"((?:[^<\wàâéèêëîïôöùüç'-]*(?:<[^>]+>)?)*)([\wàâéèêëîïôöùüç'-]+)?(.*)", re.I)

    def sepWordRE(self):
        return ConstituentFr.sepWordREC

    def doElision(self, cList):
        # Elision rules for French
        # implements the obligatory elision rules of the "Office de la langue française du Québec"
        #    https://vitrinelinguistique.oqlf.gouv.qc.ca/21737/lorthographe/elision-et-apostrophe/elision-obligatoire
        # for Euphonie, rules were taken from Antidote (Guide/Phonétique)

        elidableWordFrRE = re.compile(r"^(la|le|je|me|te|se|de|ne|que|puisque|lorsque|jusque|quoique)$", re.I)
        euphonieFrRE = re.compile(r"^(ma|ta|sa|ce|beau|fou|mou|nouveau|vieux)$", re.I)
        euphonieFrTable = {"ma": "mon", "ta": "ton", "sa": "son", "ce": "cet",
                           "beau": "bel", "fou": "fol", "mou": "mol", "nouveau": "nouvel", "vieux": "vieil"}

        contractionFrTable = {
            "à+le": "au", "à+les": "aux", "ça+a": "ç'a",
            "de+le": "du", "de+les": "des", "de+des": "de", "de+autres": "d'autres",
            "des+autres": "d'autres",
            "si+il": "s'il", "si+ils": "s'ils"}

        def isElidableFr(realization, lemma, pos):
            # check if realization starts with a vowel
            if re.match(r"^[aeiouyàâéèêëîïôöùü]", realization, re.I): return True
            if re.match(r"^h", realization, re.I):
                #  check for a French "h aspiré" for which no elision should be done
                lexiconInfo = getLemma(
                    lemma if isinstance(lemma, str) else realization)  # get the lemma with the right pos
                if lexiconInfo is None:
                    lexiconInfo = getLemma(lemma.lower())  # check with lower case
                    if lexiconInfo is None: return True  # elide when unknown
                if pos not in lexiconInfo: pos = next(iter(lexiconInfo))  # try the first pos if current not found
                if pos in lexiconInfo and "h" in lexiconInfo[pos] and lexiconInfo[pos][
                    "h"] == 1: return False  # h aspiré found
                return True
            return False

        last = len(cList) - 1
        if last == 0: return  # do not try to elide a single word
        i = 0
        while i < last:
            if i > 0 and cList[i - 1].getProp("lier"):  # ignore if the preceding word is "lié" to this one
                i += 1
                continue
            m1 = ConstituentFr.sepWordREC.match(cList[i].realization) if cList[i].realization is not None else None
            if m1 is None or m1.group(2) is None:
                i += 1
                continue
            m2 = ConstituentFr.sepWordREC.match(cList[i + 1].realization) if cList[i].realization is not None else None
            if m2 is None or m2.group(2) is None:
                i += 1
                continue
            # HACK: m1 and m2 save the parts before and after the first word (w1 and w2) which is in m_i[2]
            # for a single word
            w1 = m1.group(2)
            w2 = m2.group(2)
            w3NoWords = not re.match(r"^\s*\w",
                                     m1.group(3))  # check that the rest of the first word does not start with a word
            elisionFound = False
            if isElidableFr(w2, cList[i + 1].lemma, cList[i + 1].constType):
                if elidableWordFrRE.match(w1) and w3NoWords:
                    cList[i].realization = m1[1] + w1[:-1] + "'" + m1[3]
                    elisionFound = True
                elif euphonieFrRE.match(w1) and w3NoWords and cList[i].getProp("n") == "s":  # euphonie
                    if re.match(r"ce", w1, re.I) and re.match(r"(^est$)|(^étai)|(^a$)", w2, re.I):
                        # very special case but very frequent
                        cList[i].realization = m1[1] + w1[:-1] + "'" + m1[3]
                    elif w2 not in ["et", "ou", "où", "aujourd'hui"]:
                        # avoid euphonie before "et", "or" ....: e.g. "beau et fort" and not "bel et fort"
                        cList[i].realization = m1[1] + euphonieFrTable[w1] + m1[3]
                    elisionFound = True
            if elisionFound:
                i += 1
            elif (w1 + "+" + w2) in contractionFrTable and w3NoWords:
                # try contraction
                contr = contractionFrTable[w1 + "+" + w2]
                # check if the next word would be elidable, so instead elide it instead of contracting
                # except when the next word is a date which has a "strange" realization
                if (elidableWordFrRE.match(w2) and i + 2 <= last and not cList[i + 1].isA("DT") and
                        isElidableFr(cList[i + 2].realization, cList[i + 2].lemma, cList[i + 2].constType)):
                    cList[i + 1].realization = m2[1] + w2[:-1] + "'" + m2[3]
                else:  # do contraction of first word and remove second word (keeping start and end)
                    cList[i].realization = m1[1] + contr + m1[3]
                    cList[i + 1].realization = m2[1] + m2[3].strip()
                i += 1
            i += 1

    def check_for_t(self, terminals, i):
        # check for adding -t- in French between a verb and a pronoun
        if terminals[i].isA("V") and terminals[i + 1].isA("Pro"):
            # According to Antidote:
            # C'est le cas, notamment, quand le verbe à la 3e personne du singulier du passé, du présent ou
            # du futur de l'indicatif se termine par une autre lettre que d ou t et qu'il est suivi
            # des pronoms sujets il, elle ou on. Dans ce cas, on ajoute un ‑t‑ entre le verbe
            # et le pronom sujet inversé.
            if (re.search(r"[^dt]$", terminals[i].realization) and
                    # ignore final punctuation in the realization
                    re.sub(r"(\w+).*",r"\1",terminals[i + 1].realization) in ["il","elle","on"]):
                return "t-"
            elif terminals[i].realization=="peux" and terminals[i+1].realization == "je":
                terminals[i].realization="puis" # HACK replace "peux-je" by "puis-je"
        return ""

    def warning(self, args):
        from .utils import N,A,Pro,D,Adv,V,P,C,NO,Q, NP,VP,AdvP,PP,CP,S,SP
        # create a list of elements [a,b,c] => "a, b ou c"
        def makeDisj(elems):
            args = [C("ou")] + [Q(e) for e in elems]
            return CP(*args)

        warnings = {
            "bad parameter": lambda good, bad:
                # le paramètre devrait être $good, non $bad
                S(NP(D("le"), N("paramètre")),
                  VP(V("être").t("c"), Q(good).a(","), Q("non"), Q(bad))).typ({"mod": "nece"}),
            "bad application": lambda info, goods, bad:
                # $info devrait être appliqué à $good, non à $bad.
                S(Q(info), VP(V("appliquer").t("c"),
                              PP(P("à"), makeDisj(goods)).a(","), Q("non"), PP(P("à"), Q(bad)))
                  ).typ({"mod": "nece", "pas": True}),
            "bad position": lambda bad, limit:
                # $bad devrait être plus petit que $limit.
                S(Q(bad), VP(V("être").t("c"), A("petit").f("co"), C("que"), Q(limit))).typ({"mod": "nece"}),
            "bad const for option": lambda option, constType, allowedConsts:
                # l'option $option est appliquée à $constType, mais devrait être à $allowedConsts
                CP(C("mais"),
                   VP(V("appliquer"), NP(D("le"), N("option"), Q(option)), PP(P("à"), Q(constType)))
                       .typ({"pas": True}).a(","),
                   SP(VP(V("être").t("c"), PP(P("à"), makeDisj(allowedConsts)))).typ({"mod": "nece"})),
            "ignored value for option": lambda option, bad:
                # $bad: cette mauvaise valeur pour l'option $option est ignorée
                S(Q(bad).a(":"),
                  VP(V("ignorer"), NP(D("ce"), A("mauvais").pos("pre"), N("valeur"),
                                     PP(P("pour"), D("le"),N("option"), Q(option)))).typ({"pas": True})),
            "unknown type": lambda key, allowedTypes:
                # type illégal : $key, il devrait être $allowedTypes.
                S(NP(A("illégal"), N("type"), Q(key).b(":")).a(","),
                  VP(V("être").t("c"), makeDisj(allowedTypes)).typ({"mod": "nece"})),
            "no value for option": lambda option, validVals:
                # aucune valeur pour l'option $option, elle devrait être une parmi $validVals.
                S(NP(D("aucun"), N("valeur"),
                     PP(P("pour"), D("le"), N("option"), Q(option))).a(","),
                  SP(Pro("elle"),
                     VP(V("être").t("c"), Pro("un").g("f"),
                        PP(P("parmi"), Q(makeDisj(validVals))))).typ({"mod": "nece"})),
            "not found": lambda missing, context:
                # aucun $missing trouvé dans $context.
                S(AdvP(D("aucun"), Q(missing)), VP(V("trouver").t("pp"), PP(P("dans"), Q(context)))),
            "bad ordinal": lambda value:
                # $value ne peut pas être réalisé comme un ordinal.
                S(VP(V("réaliser"), Q(value), AdvP(Adv("comme"), D("un"), N("ordinal")))).typ({"neg": True, "mod": "poss"}),
            "bad roman": lambda value:
                # cannot realize $value as a Roman number.
                # ne peut pas réaliser $value comme un nombre romain.
                S(VP(V("réaliser"), Q(value), AdvP(Adv("comme"), NP(D("un"), A("romain"), N("nombre"))))).typ(
                    {"neg": True, "mod": "poss"}),
            "bad number in word": lambda value:
                # cannot realize $value in words.
                # $value ne peut pas être réalisé en mots.
                S(VP(V("réaliser"), Q(value), PP(P("en"), N("mot").n("p")))).typ({"neg": True, "mod": "poss"}),
            "no French contraction": lambda:
                # la contraction est ignorée en français.
                S(VP(V("ignorer"), NP(D("le"),N("contraction")), PP(P("en"), N("français")))).typ({"pas": True}),
            "morphology error": lambda info:
                # erreur dans la morphologie : $info.
                S(NP(N("erreur"), PP(P("dans"), NP(D("le"), N("morphologie")))).a(":"), Q(info)),
            "not implemented": lambda info:
                # $info n'est pas implémenté
                S(Q(info), VP(V("implémenter"))).typ({"neg": True, "pas": True}),
            "not in lexicon": lambda lang, altPos:
                # absent du lexique $lang, mais existe comme $altPos
                S(A("absent"),
                  PP(P("de"), D("le"), A("français") if lang=="fr" else A("anglais"), N("lexique")),
                  AdvP(Adv("mais"), V("exister"), Adv("comme"), makeDisj(altPos)) if altPos is not None else Q("")),
            "no appropriate pronoun": lambda:
                # un pronom adéquat ne peut pas être trouvé
                S(VP(V("trouver"), NP(D("un"), A("approprié"), N("pronom")))).typ({"neg": True, "pas": True, "mod": "poss"}),
            "both tonic and clitic": lambda:
                # tn(..) et c(..) ne peuvent pas être utilisés ensemble, tn(..) est ignoré.
                S(CP(C("et"), Q("tn(..)"), Q("c(..)")),
                  VP(V("être"),V("utiliser").t("pp"), Adv("ensemble"))
                      .typ({"neg": True, "mod": "poss"}).a(","),
                  Q("tn(..)"), VP(V("ignorer")).typ({"pas": True})),
            "bad Constituent": lambda rank, type:
                # le $rank paramètre n'est pas Constituent.
                S(NP(D("le"), Q(rank), N("paramètre")),
                  VP(V("être"), Q("Constituent"), Adv("mais"), Q(type))).typ({"neg": True}),
            "bad Dependent": lambda rank, type:
                # le $rank paramètre n'est pas Dependent mais $type
                S(NP(D("le"), Q(rank), N("paramètre")),
                  VP(V("être"), Q("Dependent"), Adv("mais"), Q(type))).typ({"neg": True}),
            "Dependent needs Terminal": lambda type:
                # le premier paramètre du Dependent n'est pas Terminal mais $type.
                S(NP(D("le"), NO(1).dOpt({"ord": True}), N("paramètre"), PP(P("de"), Q("Dependent"))),
                  VP(V("être"), Q("Terminal"), Adv("mais"), Q(type))).typ({"neg": True}),
            "bad number of parameters": lambda termType, number:
                # $termType accepte un seul paramètre, mais en a $number.
                S(Q(termType), VP(V("accepter"), NP(D("un"), A("seul").pos("pre"), N("paramètre"))).a(","),
                  SP(C("mais"), Pro("je"), VP(VP(Pro("en"),V("avoir"), NO(number))))),
            "Dependent without params": lambda:
                # Dependent sans paramètre
                S(Q("Dependent"), PP(P("sans"), N("paramètre"))),
            "bad lexicon table": lambda lemma, ending:
                # erreur dans le lexique: $lemma devrait terminer par $ending
                S(NP(N("erreur"), PP(P("dans"), NP(D("le"), N("lexique")))).a(":"),
                  SP(Q(lemma), VP(V("terminer"), PP(P("par"), Q(ending)))).typ({"neg": True})),
            "bad language": lambda lang:
                # langage doit être "en" ou "fr", non $lang
                S(NP(N("langage")), VP(V("être"), CP(C("ou"), Q('"en"'), Q('"fr"')).a(","), Q("non"), Q(lang).en('"'))).typ(
                    {"mod": "obli"}),
            "ignored reflexive": lambda pat:
                # ne peut pas être réflexif, seulement $pat
                S(VP(V("être"), A("réflexif")).typ({"mod": "poss", "neg": True}).a(","),
                  AdvP(Adv("seulement"), makeDisj(pat)) if len(pat) > 0 else None),
            "inconsistent dependents within a coord": lambda expected, found:
                # $expected attendu dans ce coord mais $found a été trouvé
                S(Q(expected), VP(V("attendre").t("pp"), PP(P("dans"), NP(D("ce"), Q("coord")))),
                  SP(C("mais"), Q(found), V("être").t("pc"), V("trouver").t("pp"))),
            "user-warning": lambda mess:
                # user specific message, either a String or a Constituent that will be realized
                S(Q(mess.realize()) if isinstance(mess, Constituent) else Q(str(mess)))
        }

        args = list(args)
        mess = args.pop(0)
        if mess not in warnings:
            self.error("warn appelé avec un message inconnu:" + str(mess))
        messExp = warnings[mess](*args).cap(False)
        messS = self.me() + ":: " + messExp.realize()  # realize the warning
        return messS
