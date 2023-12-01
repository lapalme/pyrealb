# coding=utf-8
# from jsRealBclass import N,A,Pro,D,Adv,V,C,P,DT,NO,Q,  NP,AP,AdvP,VP,CP,PP,S,SP, jsRealB, Terminal, Phrase,Constituent
from pyrealb import *
from amrDicoGen import nouns,adjectives,verbs,adverbs,prepositions, verbalizations ,morphVerbalizations

from lexicalSemantics import LexSem, nounInfo,adjInfo,pp,optD
import utils
import copy,re

## function to build a noun syntR
dn = lambda det,arg: NP(D(det),arg) if arg!=None else None
cn = lambda conj,arg:S(C(conj),arg) if arg!=None else None

def addOptions(syntR,opts):
    for (key,val) in opts.items():
        getattr(syntR, key)(val)
    return syntR

def delCat(dct,w):
    if w in dct:del dct[w]

### Pronouns
pronounOptions = {
    "I":{"pe":1},
    "i":{"pe":1},
    "me":{"pe":1},
    "you":{"pe":2},
    "he":{"pe":3,"g":"m"},
    "she":{"pe":3,"g":"f"},
    "it":{"pe":3,"g":"n"},
    "we":{"pe":1,"n":"p"},
    "they":{"pe":3,"n":"p"},
    "everything":{}
}

def isPronoun(lemma):return lemma in pronounOptions
def makePro(lemma):
    if lemma=="everything":
        return LexSem(lemma,"Pro",[],lambda:Pro("everything"))
    if lemma in pronounOptions:
        return LexSem(lemma,"Pro",[],lambda:addOptions(Pro("I"),pronounOptions[lemma]))
    else:
        print("makePro: unknown lemma:"+lemma)

def isPossessive(s):return s in pronounOptions
def makePoss(s):
    if isinstance(s,str):
        if s in pronounOptions:
            return addOptions(D("my"),pronounOptions[s]) ## IT MUST return a Terminal not a LexSem 
        else:
            print("makePoss: unknown s:"+str(s))
    elif s.isA("Pro"):
        s.terminal="D"
        s.lemma="my"
        return s

### Determiners
determiners= {"my", "that", "the", "what", "whatever", "which", "whichsoever", "whose", "a", "this"}

### Conjunctions
def op16(conj):
    return LexSem(conj,"C",[":op1",":op2",":op3",":op4",":op5",":op6"],
                  lambda op1,op2,op3,op4,op5,op6:CP(C(conj),op1,op2,op3,op4,op5,op6))  
def op12(lemma,np,prep):
    return LexSem(lemma,"P",[":op1",":op2"],
                  lambda op1,op2:SP(np,op1,pp(prep,op2)))
conjunctions={}   
conjunctions["or"]=op16("or")
conjunctions["and"]=op16("and")
conjunctions["either"]=op16("either")
conjunctions["product-of"]=op16("times")
conjunctions["sum-of"]=op16("and")
conjunctions["ratio-of"]=op12("ratio-of",NP(N("ratio"),P("of")),"to")
conjunctions["difference-of"]=op16("minus")
conjunctions["quotient-of"]=op16("divided by")
conjunctions["power-of"]=op16("to the power of")
conjunctions["root-of"]= LexSem("root-of","P",[":op1",":op2"],
                                lambda op1,op2:NP(NO(op2[0].lemma).dOpt({"ord":True}),N("root"),PP(P("of"),op1)))
conjunctions["logarithm-of"]= LexSem("log-of","P",[":op1",":op2"],
                                     lambda op1,op2:NP(N("logarithm"),PP(P("of"),op1,N("base").a(":"),op2)))

def isConjunction(lemma):return lemma in conjunctions
def makeCP(lemma):
    return  conjunctions[lemma]

### Adverbs
adverbs["et-cetera"]=AdvP(Adv("etc"))
adverbs["at-least"]=AdvP(P("at"),Adv("least"))
adverbs["next-to"]=AdvP(Adv("next"),P("to"))
adverbs["kind-of"]=AdvP(Q("kind of"))
adverbs["away"]=AdvP(Adv("away"),P("from"))
delCat(adverbs,"between")
delCat(adverbs,"near")
delCat(adverbs,"this")
delCat(adverbs,"that")
delCat(adverbs,"after") # keep only prep
delCat(adverbs,"this")

def isAdverb(lemma):return lemma in adverbs
def makeAdv(lemma):
    adv=adverbs[lemma]
    if isinstance(adv,str):
        return LexSem(lemma,"Adv",[":op1"],lambda op1:Adv(adv) if op1==None else AdvP(Adv(adv),accPron(op1)))
    if adv.isA("AdvP"):
        return LexSem(lemma,"Adv",[":op1"],lambda op1:copy.deepcopy(adv).add(accPron(op1)))
    if adv.isA("Adv"):
        return LexSem(lemma,"Adv",[":op1"],lambda op1:AdvP(copy.deepcopy(adv),accPron(op1)))
    print("### strange adverb:"+str(adv))
    return adverbs[lemma]

### Prepositions
prepositions["up-to"]=PP(P("up"),P("to"))

def accPron(op): # if op is pronoun make it accusative "i"=>"me"
    if isinstance(op,list):
        if op[0].isA("Pro"):op[0].lemma="me"
    elif op.isA("Pro"):
        op.lemma="me"
    return op
    
def isPreposition(lemma):return lemma in prepositions
def makeP(lemma):
    prep=prepositions[lemma]
    if prep.isA("PP"):
        return LexSem(lemma,"P",[":op1"],lambda op1:copy.deepcopy(prep).add(accPron(op1)))
    if prep.isA("P"):
        return LexSem(lemma,"P",[":op1"],lambda op1:PP(copy.deepcopy(prep),accPron(op1)))
    if isinstance(prep,str):
        return LexSem(lemma,"P",[":op1"],lambda op1:P(prep) if op1==None else PP(P(prep),accPron(op1)))
    print("### strange preposition:"+str(prep))
    return prep

delCat(prepositions,"away")

### Verbs
delCat(verbs,"contrast-01") # keep it as noun
delCat(verbs,"hyperlink-91") # keep it as noun
delCat(verbs,"infer-01")

verbs["exemplify-01"]=LexSem("exemplify","PP",[":ARG0"],lambda _:PP(P("for"),N("example")))

def isVerb(lemma):return lemma in verbs
def makeV(lemma):return verbs[lemma]

# ARG0:giver / ARG1:thing given / ARG2:entity given to [give.xml]
verbs['give-01']=LexSem("give","V",[":ARG0",":ARG1",":ARG2"],
                        lambda arg0,arg1,arg2:S(arg0,VP(V("give"),arg1,pp("to",arg2))))

verbs['know-01']=LexSem("know","V",[":ARG0",":ARG1",":ARG2"], # strangely the lemma is "idk" in PropBank
                        lambda arg0,arg1,arg2:S(arg0,VP(V("know"),arg1,pp("to",arg2))))

## in PropBank : bear-02 :ARG0 should be the "bearer" (e.g. the mother) and :ARG1 the "bearee" 
## but in AMR, :ARG1 is used as the person who is born... without :ARG0
verbs['bear-02']=LexSem("born","V",[":ARG0",":ARG1"],
                        lambda arg0,arg1:S(arg1,VP(V("be"),V("born").t("pp"),pp("to",arg0))))

## in PropBank: hunger-01 :ARG0 corresponds to the person who is hungry (hunger is archaic in this acception)
## so we translate with a more colloquial "be hungry [for...]"
verbs['hunger-01']=LexSem("hunger","V",[":ARG0",":ARG1"],
                          lambda arg0,arg1:S(arg0,VP(V("be"),A("hungry"),pp("for",arg1))))

## correction of prepositions...
# ARG0:buyer / ARG1:thing bought / ARG2:seller / ARG3:price paid / ARG4:benefactive [buy.xml]
verbs['buy-01']=LexSem("buy","V",[":ARG0",":ARG1",":ARG2",":ARG3",":ARG4"],
                  lambda arg0,arg1,arg2,arg3,arg4:S(arg0,VP(V("buy"),arg1,pp("from",arg2),pp("at",arg3),pp("for",arg4))))

#  ARG0:assessor of not failing / ARG1:thing failing / ARG2:task / ARG3:benefactive [fail.xml]
verbs['fail-01']=LexSem("fail","V",[":ARG0",":ARG1",":ARG2",":ARG3"],
                        lambda arg0,arg1,arg2,arg3:S(arg0,arg1,VP(V("fail"),pp("to",arg2),pp("on",arg3))))

# ARG0:pilot, agentive entity capable of flight (like a bird) / ARG1:passenger, cargo / ARG2:aircraft flown, flight number, steed, non-agentive thing in motion / ARG3:type of flight plan, mission, cognate object (like 'a flight' or 'sorties') / ARG4:airline [fly.xml]
verbs['fly-01'] = LexSem("V","fly",[":ARG0",":ARG1",":ARG2",":ARG3",":ARG4"],
                         lambda arg0,arg1,arg2,arg3,arg4:S(arg0,arg1,arg2,VP(V("fly"),arg3,pp("by",arg4))))

## ARG1 <=> ARG2 because of bad parsing of Propbank
verbs['promise-01']=LexSem("promise","V",[":ARG0",":ARG1",":ARG2"],
                           lambda arg0,arg1,arg2:S(arg0,VP(V("promise"),pp("to",arg1),arg2)))

# ARG0:provider / ARG1:thing provided / ARG2:entity provided for (benefactive) [provide.xml]
verbs['provide-01']= LexSem("provide","V",[":ARG0",":ARG1",":ARG2"],
                            lambda arg0,arg1,arg2:S(arg0,VP(V("provide"),arg1,pp("to",arg2))))

# ARG0:causer of inception/rising of arg1, likely to occur with light verb / ARG1:Logical subject, patient, thing rising / ARG2:EXT, amount risen / ARG3:start point / ARG4:end point / ARGM:medium [rise.xml]
verbs['rise-01'] = LexSem("rise","V",[":ARG0",":ARG1",":ARG2",":ARG3",":ARG4"],
                          lambda arg0,arg1,arg2,arg3,arg4:S(arg0,arg1,VP(V("rise"),arg2,pp("from",arg3),pp("to",arg4))))

# ARG0:Sayer / ARG1:Utterance / ARG2:Hearer / ARG3:Attributive [say.xml]
verbs['say-01'] = LexSem("V","say",[":ARG0",":ARG1",":ARG2",":ARG3"],
                         lambda arg0,arg1,arg2,arg3:
                            S(arg0,VP(V("say"),arg1,pp("to",arg2),pp("of",arg3))) 
                            if arg0!=None else S(arg1,pp("to",arg2),pp("of",arg3)))

#  ARG0:causer of sinking / ARG1:thing sinking / ARG2:EXT / ARG3:start point / ARG4:end point, destination / ARG5:instrument [sink.xml]
verbs['sink-01']=LexSem("sink","V",[":ARG0",":ARG1",":ARG2",":ARG3",":ARG4",":ARG5"],
                        lambda arg0,arg1,arg2,arg3,arg4,arg5:S(arg0,arg1,VP(V("sink"),arg2,pp("from",arg3),pp("to",arg4),pp("with",arg5))))

# ARG0:agent who activates arg1 / ARG1:noise-maker / ARG2:the sound itself (the name of the sound/song, etc., not just a characteristic) / ARG3:characteristic of the sound [sound.xml]
verbs['sound-02']=LexSem("V","sound",[":ARG0",":ARG1",":ARG2",":ARG3"],
                         lambda arg0,arg1,arg2,arg3:S(arg0,arg1,VP(V("sound"),pp("of",arg2),arg3)))

verbs['shout-01']=LexSem("shout","V",[":ARG0",":ARG1",":ARG2"],
                         lambda arg0,arg1,arg2:S(arg0,VP(V("shout"),arg1,pp("at",arg2))))
verbs['make-it-14']=LexSem("make it","V",[":ARG0"],
                           lambda arg0:S(arg0,VP(V("make"),Pro("me").g("n"))))

delCat(verbs,"war-01")
delCat(verbs,"policy-01")
delCat(verbs,"slew")

verbalizations['explode-01']={'':'explosion'}
verbalizations["maraud-00"]={"":"marauder"}
verbalizations['thing'][':*:ARG1']['propose-01']="proposal"
# verbalizations['thing'][':*:ARG1']['paint-02']="painting"
# verbalizations['thing'][':*:ARG1']['produce-01']="product"

### reifications
## TODO: à compléter
# % reifications 
# verb('be-destined-for-91',(':ARG1':A1)^(':ARG2':A2)
#                          ^s(A1,vp(v("be"),A2/pp(p("for"),A2)))).
# verb('be-from-91',(':ARG1':A1)^(':ARG2':A2)
#                          ^s(A1,vp(v("be"),A2/pp(p("from"),A2)))).
# verb('be-with-10',(':ARG0':A0)^(':ARG1':A1)
#                          ^s(A0,vp(v("be"),A1/pp(p("with"),A1)))).
# verb('be-temporally-at-91',(':ARG1':A1)^(':ARG2':A2)
#                          ^s(A1,vp(v("be"),A2/pp(p("on"),A2)))).
# verb('be-located-at-91',(':ARG1':A1)^(':ARG2':A2)^(':time':T)
#                          ^s(A1,vp(v("be"),A2/pp(p("in"),A2),T))).
# % verb('have-concession-91',(':ARG1':A1)^(':ARG2':A2) %% seems always used without args...
# %                          ^s(A1,vp(v("be"),A2/pp(p("despite"),A2)))).
# verb('have-concession-91',q("in spite of that")).
# verb('have-condition-91',(':ARG1':A1)^(':ARG2':A2)
#                          ^s(A1,vp(v("be"),A2/cp(c("if"),A2)))).

### Adjectives
delCat(adjectives,"near")   # keep only prep
delCat(adjectives,"after")  # keep only prep
delCat(adjectives,"regardless")
delCat(adjectives,"soon")
delCat(adjectives,"kind-of")
delCat(adjectives,"still")  #keep only adverb
delCat(adjectives,"rate-entity-91") # strange in amrDicoGen

def isAdjective(lemma):return lemma in adjectives
def makeA(lemma):
    adj=adjectives[lemma]
    if isinstance(adj,LexSem):
        return adj
    if adj.isA("AP"):
        return LexSem(lemma,"A",[":ARG1"],lambda arg1:copy.deepcopy(adj).add(arg1))
    if adj.isA("A"):
        return LexSem(lemma,"A",[":ARG1"],lambda arg1:AP(copy.deepcopy(adj),arg1))
    if isinstance(adj.str):
        return LexSem(lemma,"A",[":ARG1"],lambda arg1:A(adj) if arg1==None else AP(A(adj),arg1))
    print("### strange adjective:"+str(adj))
    return adj


### Nouns
def isNoun(lemma):return lemma in nouns
def makeN(lemma):
    noun=nouns[lemma]
    if isinstance(noun,str):
        return nounInfo(noun)
    if isinstance(noun,LexSem):
        return noun
    print("### strange noun:"+str(noun))
    return noun

# keep only the adjective
delCat(nouns,"alcoholic")
delCat(nouns,"bad")
delCat(nouns,"brief")
delCat(nouns,"common")
delCat(nouns,"dear")
delCat(nouns,"even")
delCat(nouns,"extreme")
delCat(nouns,"fast")
delCat(nouns,"good")  
delCat(nouns,"large")
delCat(nouns,"little")
delCat(nouns,"next")
delCat(nouns,"no")
delCat(nouns,"old")
delCat(nouns,"sharp")
delCat(nouns,"small")
delCat(nouns,"still")

## keep only the verb
delCat(nouns,"like")
delCat(nouns,"desire-01")
delCat(nouns,"desire")
delCat(nouns,"want")
delCat(nouns,"go")

## keep only the adverb
delCat(nouns,"yesterday")
delCat(nouns,"today")
delCat(nouns,"tomorrow")
delCat(nouns,"well")
## keep only the preposition
delCat(nouns,"over")

## add words to the dictionary
for noun in ['constrictor','anion','media','tsunami','fingernail']:
    nouns[noun]=nounInfo(noun)
for noun in ['sunday','monday','tuesday','wednesday','thursday','friday','saturday']:
    nouns[noun]=nounInfo(noun.capitalize())

def addCompound(entry,t1,t2):
    nouns[entry]=LexSem(entry,"N",[":D"],lambda d:NP(optD(d),t1,t2))
    
addCompound("government-organisation",A("governmental"),N("organization"))
addCompound("criminal-organization", A("criminal"), N("organization"))
addCompound("religious-group", A("religious"), N("group"))
addCompound("ethnic-group",A("ethnic"),N("group"))
addCompound("political-movement", A("political"), N("movement"))
addCompound("political-party", A("political"), N("party"))
addCompound("world-region",N("world"),N("region"))

# byline-91 frame arguments
# :ARG0 news organization :ARG1 author :ARG2 photographer, illustrator :ARG3 translator :ARG4 means
def optOpt(arg,key,val): # optional Option if parameter is not None
    if arg is None: return None
    if isinstance(arg,list):
        return [addOptions(arg[0],{key:val})]
    return addOptions(arg,{key:val})

nouns["byline-91"]=LexSem("byline","A",[":ARG0",":ARG1",":ARG2",":ARG3",":ARG4"],
                     lambda arg0,arg1,arg2,arg3,arg4:SP(
                         optOpt(arg0,"a",":"), optOpt(arg1,"a",","),optOpt(arg2,"a",","),
                         optOpt(arg3,"b","Trans:"),optOpt(arg4,"b","by:")))

nouns["name"]=LexSem("name","N",[":op1",":op2",":op3"],lambda op1,op2,op3:SP(op1,op2,op3) if op1!=None else NP(D("the"),N("name")))

delCat(nouns,"many")
delCat(nouns,"less")

### nouns and verbs with specific patterns

nouns["amr-choice"]=LexSem("amr-choice","N",[":op1",":op2"],
                     lambda op1,op2:S(D("the"),N("choice"),VP(V("be"),PP(P("between"),op1,C("and"),op2))))
nouns["amr-unintelligible"]=LexSem("amr-unintelligible","N",[":value"],
                                   lambda val:SP(val,Q("(unintelligible)")))
adjectives["amr-empty"]=LexSem("amr-empty","A",[],lambda:A("empty"))
adjectives["amr-unknown"]=LexSem("amr-unknown","A",[],lambda:A("unknown"))
verbs["be-located-at-91"]=LexSem("be located at","V",[":ARG1",":ARG2"],
                           lambda arg1,arg2:S(arg1,VP(V("be"),PP(P("in"),arg2))))
nouns['brother-in-law']=nounInfo("brother-in-law").addAttributes({"g":"m"})
nouns["contrast-01"]=LexSem("contrast","N",[":ARG1",":ARG2"], # considered as noun in order to avoid insertion of that in processRole
                      lambda arg1,arg2:S(arg1,C("but"),arg2))
verbs["correlate-91"]=LexSem("correlate","N",[":ARG1",":ARG2"], 
                             lambda arg1,arg2:S(arg1,VP(V("correlate"),PP(P("with"),arg2))))
nouns["date-interval"]=LexSem("date-interval","N",[":op1",":op2"],
                              lambda op1,op2:PP(P("from"),op1,P("to"),op2))
# % distribution-range-91   typically used for normal distributions with mean and standard deviation
# % frame arguments
# % :ARG1 center, mean
# % :ARG2 lower bound
# % :ARG3 upper bound
# % :ARG4 radius, distance from center to bounds
# % :ARG5 confidence that value is in range, typically a percentage, e.g. 95%
# % :ARG6 deviation covered by range, e.g. standard-deviation, standard-error-of-the-mean
# % :ARG7 type of distribution, e.g. normal-distribution
nouns["distribution-range-91"]=LexSem("distribution range","N",[":ARG1",":ARG2",":ARG3",":ARG4",":ARG5",":ARG6",":ARG7"],
                                      lambda a1,a2,a3,a4,a5,a6,a7:SP(
                                        a7,PP(P("with"),a5,N("confidence")).a(",") if a5!=None else None,
                                        a1,pp("±",a4),pp("from",a2),pp("to",a3),a6))
nouns["even-as"]=LexSem("even-as","N",[":op1"],lambda op1:AdvP(Adv("even"),Adv("as"),op1))
nouns["even-if"]=LexSem("even-if","N",[":op1"],lambda op1:AdvP(Adv("even"),C("if"),op1))
nouns["even-when"]=LexSem("even-when","N",[":op1"],lambda op1:AdvP(Adv("even"),C("when"),op1))
nouns["fluid-ounce"]=nouns["ounce"]
adverbs["have-concession-91"]=LexSem("concession","Adv",[],lambda:Adv("anyway"))

# have-degree-of-resemblance-91 - "Comparison of competing resemblances; for constructions such as 
#              'X is more like Y than Z'"
# 
# ARG1: Thing resembling things
# ARG2: First resemblance under comparison
# ARG3: Second resemblance under comparison
# ARG4: Degree word comparing ARG2 to ARG3
verbs["have-degree-of-resemblance-91"]=LexSem("have-resemblance","V",[":ARG1",":ARG2",":ARG3",":ARG4"],
        lambda arg1,arg2,arg3,arg4:S(arg1,VP(V("be"),arg4,A("like"),arg2,P("than"),arg3)))

verbs["have-mod-91"]=LexSem("have-mod","V",[":ARG1",":ARG2",":degree"], 
                            lambda arg1,arg2,deg:S(arg1,V("be"),deg,P("from"),arg2))
verbs["have-org-role-91"]=LexSem("have-org","V",[":ARG0",":ARG1",":ARG2",":ARG3"], 
                                 lambda arg0,arg1,arg2,arg3:S(arg0,VP(V("be"),arg2,pp("in",arg1),arg3)))
nouns["hyperlink-91"]=LexSem("hyperlink","N",[":ARG1",":ARG3"],lambda arg1,arg3:SP(arg1).tag("a",arg3))
# frame arguments from https://www.isi.edu/~ulf/amr/lib/amr-dict.html#include-91
# :ARG1 subset
# :ARG2 superset
# :ARG3 relative size of subset compared to superset
verbs["include-91"]=LexSem("include","V",[":ARG1",":ARG2",":ARG3"], 
                           lambda arg1,arg2,arg3:S(arg1,VP(V("be"),P("within"),
                                                   SP(arg3,P("pf")) if arg3!=None else None),arg2))
verbs["include-01"]=verbs["include-91"]
verbs["infer-01"]=LexSem("infer","V",[":ARG1",":ARG2"], 
                         lambda arg1,arg2:AdvP(arg2,Adv("so"),arg1))
nouns["instead-of-91"]=LexSem("instead of","N",[":ARG1",":ARG2"], 
                              lambda arg1,arg2:AdvP(arg1,Adv("instead"),P("of"),arg2))
nouns["kind-yy"]=LexSem("kind of","NP",[],lambda:NP(D("a"),N("kind"),P("of")))
nouns["more-than"]=LexSem("more than","N",[":op1"],lambda op1:AdvP(Adv("more"),P("than"),op1))
nouns["natural-object"]=nouns["object"]
nouns["phone-number-entity"]=LexSem("phone number","N",[":value"],lambda val:SP(Q("tel:"),val))
nouns["rate-entity-91"]=LexSem("rate","N",[":ARG1",":ARG2",":ARG3",":ARG4"],
                               lambda a1,a2,a3,a4:
                               SP(NP(a1,N("time")) if a1!=None else a1,pp("per",a2),dn("every",a3),dn("every",a4)))
nouns["regardless-91"]=LexSem("regardless","N",[":ARG1",":ARG2"], 
                              lambda arg1,arg2:SP(arg1,pp("regardless",arg2)))
nouns["relative-position"]=LexSem("relative position","N",[":op1",":direction",":quant"],
                                  lambda op1,dirct,qnt:SP(qnt,pp("to",dirct),pp("of",op1)))
verbs["request-confirmation-91"]=LexSem("request confirmation","V",[],lambda:Q("is that right ?"))
nouns["score-entity"]=LexSem("score","N",[":op1",":op2"],lambda op1,op2:SP(op1,P("to"),op2))
nouns["score-on-scale-91"]=LexSem("score on scale","N",[":ARG1",":ARG2",":ARG3"], 
            lambda arg1,arg2,arg3:\
         SP(NP(N("score").a(":"),arg1) if arg1!=None else None,pp("from",arg2),pp("to",arg3)))
nouns["several"]=LexSem("several","N",[":op1"],
                        lambda op1:NP(D("several"),op1).n("p") if op1!=None else D("several"))                    
nouns["statistical-test-91"]=LexSem("stat-test","N",[":ARG2"], # HACK: ad-hoc but could not find doc.
                                    lambda arg2:SP(Q("p <"),arg2).ba("("))
nouns["truth-value"]=LexSem("truth value","N",[":polarity-of"],lambda pol:SP(Q("whether"),pol))
nouns["value-interval"]=LexSem("value-interval","N",[":op1",":op2"],lambda op1,op2:SP(pp("from",op1),pp("to",op2)))

# special parameters for which we must get a Constituent
def getC(val):
    if isinstance(val,Constituent):
        return val
    if isinstance(val.list):
        return getC(val[0])
    if val==None:
        return Q("")
    if isinstance(val.str):
        return Q(val)
    return val


## special parameters from which we must get the Terminal 
def getT(val):
    if isinstance(val,Terminal):
        return val
    if isinstance(val,list):
        return getT(val[0])
    if isinstance(val,Phrase):
        return getT(val.elements[0])
    if val is None:
        return Q("")
    if isinstance(val,str):
        return Q(val)
    return val

nouns["email-address-entity"]=LexSem("email","N",[":value"],
                                     lambda val:getT(val).tag("a",{"href":"mailto:"+getT(val).lemma}))
nouns["ordinal-entity"]=LexSem("ordinal","N",[":value",":range"],
                               lambda val,rng:SP(getC(val).dOpt({"ord":True}),pp("in",rng)) if rng!=None
                                               else getC(val).dOpt({"ord":True}))
nouns["percentage-entity"]=LexSem("percentage","N",[":value"],
                                  lambda val:SP(getT(val) if val!=None else None,Q("percent")))
nouns["url-entity"]=LexSem("URL","N",[":value"],
                           lambda val:getT(val).tag("a",{"href":"http://"+getT(val).lemma}) if val!=None else Q("no URL"))
nouns["string-entity"]=LexSem("string","N",[":value",":mod"],
                              lambda val,mod:SP(getT(val).en('\\"'),mod))


gender={"boy":"m","man":"m","gentleman":"m","person":"m","father":"m",
        "soldier":"m","baby":"m","official":"m","professor":"m","mayor":"m",
        "investor":"m", "nerd":"m", "lawyer":"m",
        "he":"m",
        "girl":"f","woman":"f","lady":"f","mother":"f","matriarch":"f",
        "she":"f"}

######## external interface to the dictionary
posTables=[("V",verbs),("N",nouns),("Adj",adjectives),("Pro",pronounOptions),
           ("C",conjunctions),("P",prepositions),("Adv",adverbs),('Poss',pronounOptions)]

posFunctions={"V":makeV,"N":makeN,'Adj':makeA,'Pro':makePro,
              "C":makeCP,"P":makeP,'Adv':makeAdv,'Poss':makePoss}


def hasMorphVerb(s):
    return s in morphVerbalizations and 'noun' in morphVerbalizations[s]
def getMorphVerb(s,myRole):
    vrb=morphVerbalizations[s]
    kind='actor' if myRole.startswith(":ARG0") and 'actor' in vrb else 'noun'
    return N(vrb[kind])

def getNominalization(s,role=None,conceptR=""):
#     print("getNominalization(%s,%s,%s)"%(s,role,conceptR))
    if s in verbalizations:
        vs=verbalizations[s]
        if role==None:
            if "" in vs:
                return vs[""]
        elif role in vs:
                vsr=vs[role]
                if conceptR in vsr:
                    return vsr[conceptR]
    return None
            

def getPOS(word):
#     print("getPos(%s)"%word)
    for (pos,posTable) in posTables:
        if word in posTable:
            return (pos,word)
    return (None,None)

def getSyntR(word,posType=None):
    if posType==None:
        (posType,wordOK)=getPOS(word)
    if posType==None: ## create a quoted string for an unknown word
        print("$$$ word: %s not found"%word)
        return LexSem(word,"Q",[],lambda:Q(utils.generateConceptWord(word)))
    else:
#         print("posType:%s word:%s"%(posType,word))
        return posFunctions[posType](wordOK)


## query dictionary when called directly
if __name__ == '__main__':
    import re
    import specialConcept
    conceptKeys=specialConcept.conceptSwitch.keys()
    
    def showSpecialConcept(w):
        specials=[c for c in conceptKeys if re.fullmatch(w,c)]
        if len(specials)>0:
            print("** Special concepts:\n  %s"%"\n  ".join(specials))
    
    checkPos = [("V",verbs), ("N",nouns), ("A",adjectives), ("Pro",pronounOptions),
                ("C",conjunctions), ("P",prepositions),("Adv",adverbs)]
    
    def showPOS(wrdRE):
        for (pos,words) in checkPos:
            matches=[w for w in words if re.fullmatch(wrdRE,w)]
            if len(matches):
                print(pos+":")
                for m in matches:
                    print("  %s:%s"%(m,words[m]))
    
    
    import sys
    print("info from dictionary\n> ",end="")
    for line in sys.stdin:
        wordRE=line.rstrip()
        if len(wordRE)>0:
            showSpecialConcept(wordRE)
            showPOS(wordRE)
        print("> ",end="",flush=True)
    print("--")
    