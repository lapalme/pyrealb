import re,sys
from .Constituent import Constituent

class ConstituentEn:
    def lang(self):
        return "en"

    def isEn(self):
        return True

    def isFr(self):
        return False

    def defaultProps(self):
        return {"g": "n", "n": "s", "pe": 3, "t": "p"}

    def tonic_forms(self):
        return {"us", "her", "you", "him", "them", "it"}

    def tonic_pe_1(self):
        return "me"

    def relative_pronouns(self):
        return ["that", "who", "which"]

    def relative_pronouns_propagate(self):
        return ["that", "who", "which"]

    def validate_neg_option(self, _val, _types):
        return False

    # regex for matching the first word in a generated string (ouch!!! it is quite subtle...)
    #  match index:
    #     1-possible non-word chars and optional html tags
    #     2-the real word
    #     3-the rest after the word
    sepWordREC = re.compile(r"((?:[^<\w'-]*(?:<[^>]+>)?)*)([\w'-]+)?(.*)")

    def sepWordRE(self):
        return ConstituentEn.sepWordREC

    def doElision(self, cList):
        # English elision rule only for changing "a" to "an"
        # according to https://owl.english.purdue.edu/owl/resource/591/1/
        hAnRE = re.compile(r"^(heir|herb|honest|honou?r(able)?|hour)", re.I)
        # https://www.quora.com/Where-can-I-find-a-list-of-words-that-begin-with-a-vowel-but-use-the-article-a-instead-of-an
        uLikeYouRE = re.compile(r"^(uni.*|ub.*|use.*|usu.*|uv.*)", re.I)
        acronymRE = re.compile(r"^[A-Z]+$")
        # Common Contractions in the English Language taken from :http:#www.everythingenglishblog.com/?p=552
        contractionEnTable = {
            "are+not": "aren't", "can+not": "can't", "did+not": "didn't", "do+not": "don't", "does+not": "doesn't",
            "had+not": "hadn't", "has+not": "hasn't", "have+not": "haven't", "is+not": "isn't", "must+not": "mustn't",
            "need+not": "needn't", "should+not": "shouldn't", "was+not": "wasn't", "were+not": "weren't",
            "will+not": "won't", "would+not": "wouldn't",
            "let+us": "let's",
            "I+am": "I'm", "I+will": "I'll", "I+have": "I've", "I+had": "I'd", "I+would": "I'd",
            "she+will": "she'll", "he+is": "he's", "he+has": "he's", "she+had": "she'd", "she+would": "she'd",
            "he+will": "he'll", "she+is": "she's", "she+has": "she's", "he+would": "he'd", "he+had": "he'd",
            "you+are": "you're", "you+will": "you'll", "you+would": "you'd", "you+had": "you'd", "you+have": "you've",
            "we+are": "we're", "we+will": "we'll", "we+had": "we'd", "we+would": "we'd", "we+have": "we've",
            "they+will": "they'll", "they+are": "they're", "they+had": "they'd", "they+would": "they'd",
            "they+have": "they've",
            "it+is": "it's", "it+will": "it'll", "it+had": "it'd", "it+would": "it'd",
            "there+will": "there'll", "there+is": "there's", "there+has": "there's", "there+have": "there've",
            "that+is": "that's", "that+had": "that'd", "that+would": "that'd", "that+will": "that'll",
            "what+is": "what's"
        }
        # search for terminal "a" and check if it should be "an" depending on the next word
        last = len(cList) - 1
        if last == 0: return  # do not try to elide a single word
        i = 0
        while i < last:
            m1 = ConstituentEn.sepWordREC.match(cList[i].realization)
            if m1 is None or m1.group(2) is None:
                i += 1
                continue
            m2 = ConstituentEn.sepWordREC.match(cList[i + 1].realization)
            if m2 is None or m2.group(2) is None:
                i += 1
                continue
            # HACK: m1 and m2 save the parts before and after the first word (w1 and w2) which is in m_i.group(2)
            # for a single word
            w1 = m1.group(2)
            w2 = m2.group(2)
            if (w1 == "a" or w1 == "A") and cList[i].isA("D"):
                if (re.match(r"^[ai]", w2, re.I) or  # starts with a or i
                        (re.match(r"^e", w2, re.I) and not re.match(r"^eu", w2, re.I) or  # starts with e but not eu
                         re.match(r"^o", w2, re.I) and not re.match(r"^onc?e", w2,
                                                                    re.I) or  # starts with o but not one or once
                         re.match(r"^u", w2, re.I) and not uLikeYouRE.match(w2) or  # u does not sound like you
                         hAnRE.match(w2) or  # silent h
                         acronymRE.match(w2))):  # is an acronym
                    cList[i].realization = m1.group(1) + w1 + "n" + m1.group(3)
                    i += 1  # skip next word
            elif hasattr(self, "contraction") and self.contraction == True:
                if w1 == "cannot":  # special case...
                    cList[i].realization = m1.group(1) + "can't" + m1.group(3)
                else:
                    key = w1 + "+" + w2
                    if key in contractionEnTable:
                        contr = contractionEnTable[key]
                        # do contraction of first word and remove second word (keeping start and end)
                        cList[i].realization = m1.group(1) + contr + m1.group(3)
                        cList[i + 1].realization = m2.group(1) + m2.group(3).strip()
                        i += 1
            i += 1


    def doPronounPlacement(self, cList):
        pass

    def check_for_t(self, _terminals, _i):
        return ""

    def warning(self, args):
        from .utils import N,A,Pro,D,Adv,V,P,C,DT,NO,Q, NP,AP,VP,AdvP,PP,CP,S,SP
        # create a list of elements [a,b,c] => "a, b or c"
        def makeDisj(elems):
            args = [C("or")] + [Q(e) for e in elems]
            return CP(*args)

        warnings = {
            "bad parameter": lambda good, bad:
                # the parameter should be $good, not $bad
                S(NP(D("the"), N("parameter")),
                  VP(V("be").t("c"), Q(good).a(","), Q("not"), Q(bad))).typ({"mod": "nece"}),
            "bad application": lambda info, goods, bad:
                # $info should be applied to $good, not to $bad
                S(Q(info), VP(V("apply").t("c"),
                              PP(P("to"), makeDisj(goods)).a(","), Q("not"), PP(P("to"), Q(bad)))
                  ).typ({"mod": "nece", "pas": True}),
            "bad position": lambda bad, limit:
                # $bad should be smaller than $limit.
                S(Q(bad), VP(V("be").t("c"), A("small").f("co"), C("than"), Q(limit))).typ({"mod": "nece"}),
            "bad const for option": lambda option, constType, allowedConsts:
                # the option $option is applied to $constType, but should be to $allowedConsts.
                CP(C("but"),
                   VP(V("apply"), NP(D("the"), N("option"), Q(option)), PP(P("to"), Q(constType))).typ({"pas": True}).a(
                       ","),
                   SP(VP(V("be").t("c"), PP(P("to"), makeDisj(allowedConsts)))).typ({"mod": "nece"})),
            "ignored value for option": lambda option, bad:
                # $bad: this bad value for option $option is ignored.
                S(Q(bad).a(":"),
                  VP(V("ignore"), NP(D("this"), A("bad").pos("pre"), N("value"),
                                     PP(P("for"), N("option"), Q(option)))).typ({"pas": True})),
            "unknown type": lambda key, allowedTypes:
                # illegal type: $key, it should be $allowedTypes.
                S(NP(A("illegal"), N("type"), Q(key).b(":")).a(","),
                  VP(V("be").t("c"), makeDisj(allowedTypes)).typ({"mod": "nece"})),
            "no value for option": lambda option, validVals:
                # no value for option $option should be one of $validVals.
                S(NP(D("no"), N("value"), PP(P("for"), N("option"), Q(option))),
                  VP(V("be"), PP(P("among"), makeDisj(validVals)))).typ({"mod": "nece"}),
            "not found": lambda missing, context:
                # no $missing found in $context.
                S(AdvP(D("no"), Q(missing)), VP(V("find").t("pp"), PP(P("in"), Q(context)))),
            "bad ordinal": lambda value:
                # cannot realize $value as ordinal.
                S(VP(V("realize"), Q(value), AdvP(Adv("as"), D("a"), N("ordinal")))).typ({"neg": True, "mod": "poss"}),
            "bad roman": lambda value:
                # cannot realize $value as a Roman number.
                S(VP(V("realize"), Q(value), AdvP(Adv("as"), NP(D("a"), A("Roman"), N("number"))))).typ(
                    {"neg": True, "mod": "poss"}),
            "bad number in word": lambda value:
                # cannot realize $value in words.
                S(VP(V("realize"), Q(value), PP(P("in"), N("word").n("p")))).typ({"neg": True, "mod": "poss"}),
            "no French contraction": lambda:
                # contraction is ignored in French.
                S(VP(V("ignore"), NP(N("contraction")), PP(P("in"), N("French")))).typ({"pas": True}),
            "morphology error": lambda info:
                # error within the morphology: $info.
                S(NP(N("morphology"),N("error")).a(":"), Q(info)),
            "not implemented": lambda info:
                # $info is not implemented.
                S(Q(info), VP(V("implement"))).typ({"neg": True, "pas": True}),
            "not in lexicon": lambda lang, altPos:
                # not found in $lang lexicon, but exists as $altPos.
                S(Adv("not"), V("find").t("pp"),
                  PP(P("within"), D("the"), A("English" if lang == "en" else "French"), N("lexicon")),
                  AdvP(Adv("but"), V("exist"), Adv("as"), makeDisj(altPos)) if altPos is not None else Q("")),
            "no appropriate pronoun": lambda:
                # an appropriate pronoun cannot be found
                S(VP(V("find"), NP(D("a"), A("appropriate"), N("pronoun")))).typ({"neg": True, "pas": True, "mod": "poss"}),
            "both tonic and clitic": lambda:
                # tn(..) and c(..) cannot be used together, tn(..) is ignored.
                S(CP(C("and"), Q("tn(..)"), Q("c(..)")), VP(V("use").n("p"), Adv("together"))
                  .typ({"neg": True, "pas": True, "mod": "poss"}).a(","),
                  Q("tn(..)"), VP(V("ignore")).typ({"pas": True})),
            "bad Constituent": lambda rank, type:
                # the $rank parameter is not Constituent, but type.
                S(NP(D("the"), N("parameter"), Q(rank)),
                  VP(V("be"), Q("Constituent"), Adv("but"), Q(type))).typ({"neg": True}),
            "bad Dependent": lambda rank, type:
                # the $rank parameter is not Dependent but $type.
                S(NP(D("the"), N("parameter"), Q(rank)),
                  VP(V("be"), Q("Dependent"), Adv("but"), Q(type))).typ({"neg": True}),
            "Dependent needs Terminal": lambda type:
                # the first parameter of Dependent is not Terminal but $type.
                S(NP(D("the"), NO(1).dOpt({"ord": True}), N("parameter"), PP(P("of"), Q("Dependent"))),
                  VP(V("be"), Q("Terminal"), Adv("but"), Q(type))).typ({"neg": True}),
            "bad number of parameters": lambda termType, number:
                # $termType accepts one parameter, but has $number.
                S(Q(termType), VP(V("accept"), NP(D("a"), A("single").pos("pre"), N("parameter"))).a(","),
                  SP(C("but"), Pro("I"), VP(VP(V("have"), NO(number))))),
            "Dependent without params": lambda:
                # Dependent without parameter
                S(Q("Dependent"), PP(P("without"), N("parameter"))),
            "bad lexicon table": lambda lemma, ending:
                # error in lexicon: $lemma should end with $ending
                S(NP(N("error"), PP(P("in"), NP(D("the"), N("lexicon")))).a(":"),
                  SP(Q(lemma), VP(V("end"), PP(P("with"), Q(ending)))).typ({"neg": True})),
            "bad language": lambda lang:
                # language must be "en" or "fr", not $lang
                S(NP(N("language")), VP(V("be"), CP(C("or"), Q('"en"'), Q('"fr"')).a(","), Q("not"), Q(lang).en('"'))).typ(
                    {"mod": "obli"}),
            "ignored reflexive": lambda pat:
                # cannot be reflexive, only $pat
                S(VP(V("be"), A("reflexive")).typ({"mod": "poss", "neg": True}).a(","),
                  AdvP(Adv("only"), makeDisj(pat)) if len(pat) > 0 else None),
            "inconsistent dependents within a coord": lambda expected, found:
                #  $expected expected within this coord, but $found was found
                S(Q(expected), VP(V("expect").t("pp"), PP(P("within"), NP(D("this"), Q("coord")))),
                  SP(C("but"), Q(found), V("be").t("ps"), V("find").t("pp"))),
            "user-warning": lambda mess:
                # user specific message, either a String or a Constituent that will be realized
                S(Q(mess.realize()) if isinstance(mess, Constituent) else Q(mess.toString()))
        }

        args = list(args)
        mess = args.pop(0)
        if mess not in warnings:
            self.error("warn called with an unknown error message:" + str(mess))
        messExp = warnings[mess](*args).cap(False)
        messS = self.me() + ":: " + messExp.realize()  # realize the warning
        return messS
