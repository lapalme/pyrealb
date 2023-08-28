from .Constituent import Constituent
from .Terminal import  Terminal, N,A,Pro,D,Adv,V,P,C,DT,NO,Q
from .Phrase import Phrase, NP,AP,VP,AdvP,PP,CP,S,SP
from .Lexicon import loadEn, loadFr

# create a list of elements [a,b,c] => "a, b $conj c" 
def makeDisj(conj,elems):     
    args=[C(conj)]+[Q(e) for e in elems]
    return CP(*args)

warnings = {
    "bad parameter": lambda good,bad  :
        # the parameter should be $good, not $bad
        # le paramètre devrait être $good, pas $bad
        S(NP(D("the"),N("parameter")),
            VP(V("be").t("c"),Q(good).a(","),Q("not"),Q(bad))).typ({"mod":"nece"}),
    "bad application": lambda info,goods,bad :
        # $info should be applied to $good, not to $bad
        # $info devrait être appliqué à $good, non à $bad.
        S(Q(info),VP(V("apply").t("c"),
                         PP(P("to"),makeDisj("or",goods)).a(","),Q("not"),PP(P("to"),Q(bad)))
               ).typ({"mod":"nece","pas":True}),
    "bad position": lambda bad,limit :
        # $bad should be smaller than $limit.
        # $bad devrait être plus petit que $limit.
        S(Q(bad),VP(V("be").t("c"),A("small").f("co"),C("than"),Q(limit))).typ({"mod":"nece"}),
    "bad const for option": lambda option,constType,allowedConsts :
         # the option $option is applied to $constType, but should be to $allowedConsts.
         # l'option $option est appliquée à $constType, mais devrait être à $allowedConsts
        CP(C("but"),
            VP(V("apply"),NP(D("the"),N("option"),Q(option)),PP(P("to"),Q(constType))).typ({"pas":True}).a(","),
            SP(VP(V("be").t("c"),PP(P("to"),makeDisj("or",allowedConsts)))).typ({"mod":"nece"})),
    "ignored value for option": lambda option,bad :
        # $bad: this bad value for option $option is ignored.
        # $bad: cette mauvaise valeur pour l'option $option est ignorée
        S(Q(bad).a(":"),
            VP(V("ignore"),NP(D("this"),A("bad").pos("pre"),N("value"),
                            PP(P("for"),N("option"),Q(option)))).typ({"pas":True})),
    "unknown type": lambda key,allowedTypes :
        # illegal type: $key, it should be $allowedTypes.
        # type illégal : $key, il devrait être $allowedTypes.
        S(NP(A("illegal"),N("type"),Q(key).b(":")).a(","),
            VP(V("be").t("c"),makeDisj("or",allowedTypes)).typ({"mod":"nece"})),
    "no value for option": lambda option,validVals :
        # no value for option $option should be one of $validVals.
        # aucune valeur pour l'option $option, devrait être une parmi $validVals.
        S(NP(D("no"),N("value"),PP(P("for"),N("option"),Q(option))),
            VP(V("be"),PP(P("among"),Q(validVals)))).typ({"mod":"nece"}),
    "not found": lambda missing,context :
        # no $missing found in $context.
        # aucun $missing trouvé dans $context.
        S(AdvP(D("no"),Q(missing)),VP(V("find").t("pp"),PP(P("in"),Q(context)))),
    "bad ordinal": lambda value:
        # cannot realize $value as ordinal.
        # $value ne peut pas être réalisé comme un ordinal.
        S(VP(V("realize"),Q(value),AdvP(Adv("as"),D("a"),N("ordinal")))).typ({"neg":True,"mod":"poss"}),
    "bad roman": lambda value :
        # cannot realize $value as a Roman number.
        # $value ne peut pas être réalisé comme un nombre romain.
        S(VP(V("realize"),Q(value),AdvP(Adv("as"),NP(D("a"),A("Roman"),N("number"))))).typ({"neg":True,"mod":"poss"}),
    "bad number in word": lambda value :
        # cannot realize $value in words.
        # $value ne peut pas être réalisé en mots.
        S(VP(V("realize"),Q(value),PP(P("in"),N("word").n("p")))).typ({"neg":True,"mod":"poss"}),
    "no French contraction": lambda  :
        # contraction is ignored in French.
        # la contraction est ignorée en français.
        S(VP(V("ignore"),NP(N("contraction")),PP(P("in"),N("French")))).typ({"pas":True}),
    "morphology error": lambda info :
        # error within the morphology: $info.
        # erreur dans la morphologie : $info.
        S(NP(N("error"),PP(P("within"),NP(D("the"),N("morphology")))).a(":"),Q(info)),
    "not implemented": lambda info : # $info is not implemented.
        S(Q(info),VP(V("implement"))).typ({"neg":True,"pas":True}),
    "not in lexicon": lambda lang,altPos :
        # not found in lexicon.
        # absent du lexique.
        S(Adv("not"),V("find").t("pp"),PP(P("within"),D("the"),A("English" if lang=="en" else "French"),N("lexicon")),
              AdvP(Adv("but"),V("exist"),Adv("as"),makeDisj("or",altPos)) if altPos is not None else Q("")),
    "no appropriate pronoun": lambda  :
        # an appropriate pronoun cannot be found
        # un pronom adéquat ne peut être trouvé
        S(VP(V("find"),NP(D("a"),A("appropriate"),N("pronoun")))).typ({"neg":True,"pas":True,"mod":"poss"}),
    "both tonic and clitic": lambda  :
        # tn(..) and c(..) cannot be used together, tn(..) is ignored.
        # tn(..) et c(..) ne peuvent pas être utilisés ensemble, tn(..) est ignoré.
        S(CP(C("and"),Q("tn(..)"),Q("c(..)")),VP(V("use").n("p"),Adv("together"))
                  .typ({"neg":True,"pas":True,"mod":"poss"}).a(","),
               Q("tn(..)"),VP(V("ignore")).typ({"pas":True})),
    "bad Constituent": lambda rank,type :
        # the $rank parameter is not Constituent, but type.
        # le $rank paramètre n'est pas Constituent.
        S(NP(D("the"),N("parameter"),Q(rank)),
              VP(V("be"),Q("Constituent"),Adv("but"),Q(type))).typ({"neg":True}),
    "bad Dependent": lambda rank,type :
        # the $rank parameter is not Dependent but $type.
        # le $rank paramètre n'est pas Dependent mais  $type
        S(NP(D("the"),N("parameter"),Q(rank)),
              VP(V("be"),Q("Dependent"),Adv("but"),Q(type))).typ({"neg":True}),
    "Dependent needs Terminal": lambda type :
        # the first parameter of Dependent is not Terminal but $type.
        # le premier paramètre du Dependent n'est pas Terminal mais $type.
        S(NP(D("the"),NO(1).dOpt({"ord":True}),N("parameter"),PP(P("of"),Q("Dependent"))),
              VP(V("be"),Q("Terminal"),Adv("but"),Q(type))).typ({"neg":True}),
    "bad number of parameters": lambda termType,number :
        # $termType accepts one parameter, but has $number.
        # $termType accepte un seul paramètre, mais en a $number.
        S(Q(termType),VP(V("accept"),NP(D("a"),A("single").pos("pre"),N("parameter"))).a(","),
               SP(C("but"),Pro("I"),VP(VP(V("have"),NO(number))))),
    "Dependent without params": lambda  :
        # Dependent without parameter
        # Dependent sans paramètre
        S(Q("Dependent"),PP(P("without"),N("parameter"))),
    "bad lexicon table": lambda lemma,ending :
        # error in lexicon: $lemma should end with $ending
        # erreur dans lexique: $lemma devrait terminer par $ending
        S(NP(N("error"),PP(P("within"),NP(D("the"),N("lexicon")))).a(":"),
              SP(Q(lemma),VP(V("end"),PP(P("with"),Q(ending)))).typ({"neg":True})),
    "bad language": lambda lang :
        # language must be "en" or "fr", not $lang
        # langage doit être "en" ou "fr", non $lang
        S(NP(N("language")),VP(V("be"),CP(C("or"),Q('"en"'),Q('"fr"')).a(","),Q("not"),Q(lang).en('"'))).typ({"mod":"obli"}),
    "ignored reflexive": lambda pat :
        # cannot be reflexive, only $pat
        # ne peut être réflexif, seulement $pat
        S(VP(V("be"),A("reflexive")).typ({"mod":"poss","neg":True}).a(","),
            AdvP(Adv("only"),makeDisj("or",pat)) if len(pat)>0 else None),
    "inconsistent dependents within a coord": lambda expected,found :
        #  $expected expected within this coord, but $found was found
        # toutes les dépendances d'un coord devraient être $expected, mais $found a été rencontré
        S(Q(expected),VP(V("expect").t("pp"),PP(P("within"),NP(D("this"),Q("coord")))),
              SP(C("but"),Q(found),V("be").t("ps"),V("find").t("pp"))),
    "user-warning": lambda mess :
        # user specific message, either a String or a Constituent that will be realized
        S(Q(mess.realize()) if isinstance(mess,Constituent) else Q(mess.toString()))
}


def translate(en_exp):
    # English to French equivalents used in error messages
    # words that stay the same (e.g. option) are not indicated

    en_fr = {
        "a": "un", "accept": "accepter", "among": "parmi", "and": "et", "apply": "appliquer",
        "appropriate": "approprié", "as": "comme",
        "bad": "mauvais", "be": "être", "but": "mais",
        "end": "terminer", "error": "erreur", "English": "anglais", "exist": "exister", "expect": "attendre",
        "find": "trouver", "for": "pour", "French": "français",
        "have": "avoir",
        "I": "je", "illegal": "illégal", "in": "en", "ignore": "ignorer", "implement": "implémenter",
        "language": "langage", "lexicon": "lexique",
        "morphology": "morphologie",
        "no": "aucun", "not": "non", "number": "nombre",
        "of": "de", "one": "un", "only": "seulement", "or": "ou",
        "parameter": "paramètre", "pronoun": "pronom",
        "realize": "réaliser", "reflexive": "réflexif", "Roman": "romain",
        "small": "petit", "single": "seul",
        "than": "que", "the": "le", "this": "ce", "to": "à", "together": "ensemble",
        "use": "utiliser",
        "value": "valeur",
        "with": "avec", "within": "dans", "without": "sans", "word": "mot",
    }

    def setProps(newObj,oldObj):
        newObj.props = oldObj.props
        newObj.optSource = oldObj.optSource
        return newObj

    def terminal_tr(terminal):
        lemma = en_fr[terminal.lemma] if terminal.lemma in en_fr else terminal.lemma
        return setProps(terminal.__class__(lemma , "fr"), terminal)

    def phrase_tr(phrase):
        children = list(map(lambda e : phrase_tr(e) if isinstance(e,Phrase) else terminal_tr(e),phrase.elements))
        return setProps(phrase.__class__(*children), phrase)

    return phrase_tr(en_exp)


def warning(self,args):
    args = list(args)
    mess = args.pop(0)
    if mess not in warnings:
        self.error("warn called with an unknown error message:"+str(mess))        
    loadEn()
    messExp = warnings[mess](*args).cap(False)
    if self.isFr():
        loadFr()
        messExp = translate(messExp)
    messS=self.me()+":: "+ messExp.realize() # realize the warning
    return messS

def test_warnings():
    args=["A","B","C","D","E","F"]
    for w in warnings.keys():
        print(w)
        # determine the number of argument for the function
        nbArgs=warnings[w].__code__.co_argcount
        callArgs=[w]+args[:nbArgs] if w!="user-warning" else [w,Q("warning defined by the user")]
        loadEn()
        print(warning(NP(D("a"),N("error")),callArgs))
        loadFr()
        print(warning(NP(D("un"),N("erreur")),callArgs))
        print("---")
