from .Terminal import  N,A,Pro,D,Adv,V,P,C,DT,NO,Q
from .Phrase import NP,AP,VP,AdvP,PP,CP,S,SP
from .Lexicon import loadEn, loadFr

# create a list of elements [a,b,c] => "a, b $conj c" 
def makeDisj(conj,elems):     
    args=[C(conj)]+[Q(e) for e in elems]
    return CP(*args)

warnings = {
    "bad parameter":
        {"en":lambda good,bad: # the parameter should be $good, not $bad
            S(NP(D("the"),N("parameter")),
              VP(V("be").t("ps"),Q(good).a(","),Adv("not"),Q(bad))).typ({"mod":"nece"}),
         "fr":lambda good,bad: # le paramètre devrait être $good, pas $bad
            S(NP(D("le"),N("paramètre")),
              VP(V("être").t("c"),Q(good).a(","),Adv("non"),Q(bad))).typ({"mod":"nece"})},
    "bad application":
        {"en":lambda info,goods,bad: # $info should be applied to $good, not to $bad
            S(Q(info),VP(V("apply").t("ps"),
                         PP(P("to"),makeDisj("or",goods)).a(","),Adv("not"),PP(P("to"),Q(bad))))
               .typ({"mod":"nece","pas":True}),
         "fr":lambda info,goods,bad: # $info devrait être appliqué à $good, non à $bad.
            S(Q(info),VP(V("appliquer").t("c"),
                         PP(P("à"),makeDisj("ou",goods)).a(','),Adv("non"),PP(P("à"),Q(bad))))
              .typ({"mod":"nece","pas":True})},
    "bad position":
        {"en":lambda bad,limit : # $bad should be smaller than $limit.
            S(Q(bad),VP(V("be").t("ps"),A("small").f("co"),P("than"),Q(limit))).typ({"mod":"nece"}),
         "fr":lambda bad,limit : # $bad devrait être plus petit que $limit.
            S(Q(bad),VP(V("être").t("c"),A("petit").f("co"),Pro("que"),Q(limit))).typ({"mod":"nece"})},
    "bad const for option":
        {"en":lambda option,constType,allowedConsts : 
            # option $option is applied to $constType, but it should be to $allowedConsts.
              CP(C("but"),
                 VP(V("apply"),NP(N("option"),Q(option)),PP(P("to"),Q(constType))).typ({"pas":True}).a(","),
                 SP(Pro("I"),VP(V("be").t("ps"),PP(P("to"),makeDisj("or",allowedConsts)))).typ({"mod":"nece"})
              ),
         "fr":lambda option,constType,allowedConsts :
              #  l'option $option est appliquée à $constType, mais elle devrait l'être à $allowedConsts
              CP(C("mais"),
                 VP(V("appliquer"),NP(D("le"),N("option"),Q(option)),PP(P("à"),Q(constType)))
                    .typ({"pas":True}).a(","),
                 SP(Pro("je").g("f"),
                    VP(Pro("elle").c("acc"),
                       V("être").t("c"),PP(P("à"),makeDisj("ou",allowedConsts)))).typ({"mod":"nece"})
              )},
    "ignored value for option":
        {"en":lambda option,bad : # $bad: bad value for option $option is ignored.
            S(Q(bad).a(":"),
              VP(V("ignore"),NP(D("this"),A("bad"),N("value"),
                                PP(P("for"),N("option"),Q(option)))).typ({"pas":True})),
         "fr":lambda option,bad :  # $bad : cette mauvaise valeur pour l'option $option est ignorée
            S(Q(bad).a(":"),
              VP(V("ignorer"),NP(D("ce"),A("mauvais"),N("valeur"),
                                 PP(P("pour"),D("le"),N("option"),Q(option)))).typ({"pas":True}))},
    "unknown type":
        {"en":lambda key,allowedTypes : # illegal type: $key, it should be $allowedTypes.
            S(NP(A("illegal"),N("type").a(":"),Q(key)).a(","),
              VP(Pro("I"),V("be").t("ps"),makeDisj("or",allowedTypes))).typ({"mod":"nece"}),
         "fr":lambda key,allowedTypes : # type illégal : $key, il devrait être $allowedTypes.
            S(NP(N("type"),A("illégal").a(":"),Q(key)).a(","),
              SP(Pro("je"),VP(V("être").t("c"),makeDisj("ou",allowedTypes))).typ({"mod":"nece"}))},
    "no value for option":
        {"en":lambda option,validVals : # no value for option $option should be one of $validVals.
            S(NP(Adv("no"),N("value"),PP(P("for"),N("option"),Q(option))),
              VP(V("be").t("ps"),Pro("one"),PP(P("of"),Q(validVals)))).typ({"mod":"nece"}),
         "fr":lambda option,validVals : # aucune valeur pour l'option $option, devrait être une parmi $validVals.
            S(NP(D("aucun"),N("valeur"),PP(P("pour"),D("le"),N("option"),Q(option))).a(","),
              VP(V("être").t("c"),D("un").g("f"),PP(P("parmi"),Q(validVals)))).typ({"mod":"nece"})},
    "not found":
        {"en":lambda missing,context : # no $missing found in $context.
            S(AdvP(Adv("no"),Q(missing)),VP(V("find").t("pp"),PP(P("in"),Q(context)))),
         "fr":lambda missing,context : # aucun $missing trouvé dans $context.
            S(D("aucun"),Q(missing),VP(V("trouver").t("pp"),PP(P("dans"),Q(context))))},
    "bad ordinal":
        {"en":lambda value : # cannot realize $value as ordinal.
            S(VP(V("realize"),Q(value),AdvP(Adv("as"),N("ordinal")))).typ({"neg":True,"mod":"poss"}),
         "fr":lambda value : # $value ne peut pas être réalisé comme un ordinal.
            S(Q(value),VP(V("réaliser"),AdvP(Adv("comme"),NP(D("un"),N("ordinal")))))
              .typ({"neg":True,"mod":"poss","pas":True})},
    "bad number in word":
        {"en":lambda value : # cannot realize $value in words.
            S(VP(V("realize"),Q(value),PP(P("in"),N("word").n("p")))).typ({"neg":True,"mod":"poss"}),
         "fr":lambda value :# $value ne peut pas être réalisé en mots.
            S(VP(Q(value),V("réaliser"),PP(P("en"),NP(N("mot").n("p"))))).typ({"neg":True,"mod":"poss","pas":True})},
    "no French contraction":
        {"en":lambda  : # contraction is ignored in French.
            S(VP(V("ignore"),NP(N("contraction")),PP(P("in"),N("French")))).typ({"pas":True}),
         "fr":lambda  : # la contraction est ignorée en français.
            S(VP(V("ignorer"),NP(D("le"),N("contraction")),PP(P("en"),N("français")))).typ({"pas":True})},
    "morphology error":
        {"en":lambda info : # morphology error: $info.
            S(NP(N("morphology"),N("error")).a(":"),Q(info)),
         "fr":lambda info : # erreur de morphologie : $info.
            S(NP(N("erreur"),PP(P("de"),N("morphologie"))).a(":"),Q(info))},
    "not implemented":
        {"en":lambda info : # $info is not implemented.
            S(Q(info),VP(V("implement"))).typ({"neg":True,"pas":True}),
         "fr":lambda info : # $info n'est pas implémenté.
            S(Q(info),VP(V("implémenter"))).typ({"neg":True,"pas":True})},
    "not in lexicon":
        {"en":lambda lang,altPos=None : # not found in lexicon.
            S(Adv("not"),V("find").t("pp"),PP(P("in"),A("English" if lang=="en" else "French"),N("lexicon")),
              Q("") if altPos is None else AdvP(Adv("but"),V("exist"),Adv("as"),makeDisj("or",altPos))),
         "fr":lambda lang,altPos=None : # absent du lexique.
            S(AP(A("absent"),PP(P("de"),NP(D("le"),N("lexique"),A("anglais" if lang=="en" else "français")))),
              Q("") if altPos is None else AdvP(Adv("mais"),V("exister"),Adv("comme"),makeDisj("ou",altPos)))},
    "no appropriate pronoun":
        {"en":lambda  :S(VP(V("find").t("ps"),NP(D("a"),A("appropriate"),N("pronoun")))).typ({"neg":True,"pas":True,"mod":"poss"}),
         "fr":lambda  :S(VP(V("trouver").t("pc"),NP(D("un"),A("adéquat"),N("pronom")))).typ({"neg":True,"pas":True,"mod":"poss"})
        },
    "both tonic and clitic":
        {"en":lambda  :# tn(..) and c(..) cannot be used together, tn(..) is ignored.
             S(CP(C("and"),Q("tn(..)"),Q("c(..)")),VP(V("use").n("p"),Adv("together"))
                  .typ({"neg":True,"pas":True,"mod":"poss"}).a(","),
               Q("tn(..)"),VP(V("ignore")).typ({"pas":True})),
         "fr":lambda  :# tn(..) et c(..) utilisés ensemble, tn(..) est ignoré.
             S(SP(CP(C("et"),Q("tn(..)"),Q("c(..)")),VP(V("utiliser").t("pp").n("p"),Adv("ensemble"))).a(","),
               SP(Q("tn(..)"),VP(V("ignorer")).typ({"pas":True})))
        },
    "bad Constituent":
        {"en":lambda rank,type : # the $rank parameter is not Constituent.
            S(NP(D("the"),Q(rank),N("parameter")),
              VP(V("be"),Q("Constituent"),Adv("but"),Q(type))).typ({"neg":True}),
         "fr":lambda rank,type : # le $rank paramètre n'est pas Constituent.
            S(NP(D("le"),Q(rank),N("paramètre")),
              VP(V("être"),Q("Constituent"),Adv("mais"),Q(type))).typ({"neg":True})},
    "bad number of parameters":
        {"en":lambda termType,number : # $termType accepts one parameter, but has $number.
             S(Q(termType),VP(V("accept"),NP(D("a"),A("single"),N("parameter"))).a(","),
               SP(C("but"),Pro("I"),VP(VP(V("have"),Q(number))))),
         "fr":lambda termType,number : # $termType accepte un seul paramètre, mais en a $number.
             S(Q(termType),VP(V("accepter"),NP(D("un"),A("seul").pos("pre"),N("paramètre"))).a(","),
               SP(C("mais"),Pro("je"),VP(VP(Pro("en"),V("avoir"),Q(number)))))},
    "bad lexicon table":
        {"en":lambda lemma,ending : # error in lexicon table number: $lemma should end with $ending
            S(NP(N("error"),P("in"),N("lexicon"),N("table"),N("number")).a(":"),
              SP(Q(lemma),VP(V("end"),PP(P("with"),Q(ending)))).typ({"neg":True})),
         "fr":lambda lemma,ending : # erreur de numéro de table dans le lexique: $lemma devrait terminer par $ending
            S(NP(N("erreur"),P("de"),N("numéro"),P("de"),N("table"),P("dans"),NP(D("le"),N("lexique"))).a(":"),
              SP(Q(lemma),VP(V("terminer"),PP(P("par"),Q(ending)))).typ({"neg":True}))},
    "bad language":{
        "en":lambda lang: # language should be "en" or "fr", it will be $lang
            S(N("language"),VP(V("be").t("ps"),CP(C("or"),Q("en").en("'"),Q("fr").en("'"))).typ({"mod":"nece"}).a(","),
              Pro("it"),VP(V("be").t("f"),Q(lang))),
        "fr":lambda lang: # langage devrait être "en" ou "fr", ce sera $lang
            S(N("langage"),VP(V("être").t("c"),CP(C("ou"),Q("en").en('"'),Q("fr").en('"'))).typ({"mod":"nece"}).a(","),
              Pro("ce"),VP(V("être").t("f"),Q(lang))),
        },
    "ignored reflexive":
        {"en":lambda pat: # cannot be reflexive, only $pat
            S(VP(V("be"),A("reflexive")).typ({"mod":"poss","neg":true}),Adv("only"),makeDisj("or",pat)),
         "fr":lambda pat: # ne peut être réflexif, seulement $pat
            S(VP(V("être"),A("réflexif")).typ({"mod":"poss","neg":true}),
              AdvP(Adv("seulement"),makeDisj("ou",pat)) if len(pat)>0 else None),
         },
    }

def warning(self,args):
    if self.isEn():
        lang="en"
        loadEn()
    else:
        lang="fr"
        loadFr()
    args=list(args)
    mess=args.pop(0)
    if mess not in warnings:
        self.error("warn called with an unknown error message:"+str(mess))        
    messS=self.me()+":: "+ warnings[mess][lang](*args).cap(False).realize() # realize the warning
    return messS


if __name__ == '__main__':
    args=["A","B","C","D","E","F"]
    for w in warnings.keys():
        print(w)
        # determine the number of argument for the function
        nbArgs=warnings[w]["en"].__code__.co_argcount
        loadEn()
        print(warning(NP(D("a"),N("error")),[w]+args[:nbArgs]))
        loadFr()
        print(warning(NP(D("un"),N("erreur")),[w]+args[:nbArgs]))
        print("---")
   