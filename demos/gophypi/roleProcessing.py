'''
Created on Jan 20, 2021

@author: lapalme
'''

import re

import specialConcept, SemanticRep
import SemR2SyntR
 
from amrDico import gender, determiners, getSyntR, isPronoun, pronounOptions, isNoun, isAdverb, isVerb, makeV,\
                    isAdjective, isPreposition, makePro, isPossessive, makePoss, hasMorphVerb, getMorphVerb,\
                    nouns, adjectives, verbs
# from jsRealBclass import N, A, Pro, D, Adv, V, C, P, DT, NO, Q, NP, AP, AdvP, VP, CP, PP, S, SP, \
#                          Constituent, Terminal, Phrase
from pyrealb import *
from utils import traceSyntR, setTraceSyntR, is_number, unquote, generateConceptWord, errorSyntR, predicate,\
                  relative, adverbFromAdjective, isArgOp, hasNegPolarity
from lexicalSemantics import LexSem, Env, Options, nounInfo, adjInfo

## simplify notation because "from SemR2SyntR import makeSyntR"
#  makes the "recursive" import loop
def makeSyntR(semR,checkSpecial=True):
    return SemR2SyntR.makeSyntR(semR,checkSpecial)

#  add Preposition but change possible pronoun to accusative
def addPrep(prep,semR,env):
    syntR=makeSyntR(semR)
    if syntR.isA("Pro") and syntR.lemma=="I":
        syntR.lemma="me"
    env.push(PP(P(prep),syntR))

##  specific roles
def accompanierRole(semR,env,opts):
    traceSyntR("accompanierRole",semR)
    addPrep("with",semR,env)

def ageRole(semR,env,opts):
    traceSyntR("ageRole",semR)
    if semR.get_concept()=="amr-unknown":
        env.unshift(Q("how old"))
        opts.add("a","?")
    else:
        env.push(makeSyntR(semR).lier())
        env.push(A("old"))
 
def beneficiaryRole(semR,env,opts):
    traceSyntR("beneficiary", semR)
    addPrep("for",semR,env)

def causeRole(semR,env,opts):
    traceSyntR("causeRole",semR)
    concept=semR.get_concept()
    if concept=="amr-unknown":
        opts.add("typ",{"int":"why"})
    else:
        syntR=makeSyntR(semR)
        if syntR.isOneOf(["N","Q"]):
            env.push(SP(C("because"),P("of"),syntR))
        else:
            env.push(SP(C("because"),syntR))
  
comp="" # HACK: global variable to pass info between degreeRole and comparedToRole
 
def comparedToRole(semR,env,opts):
    traceSyntR("comparedToRole",semR)
    global comp
    if comp=="co":        
        env.push(PP(P("than"),makeSyntR(semR)))
        return
    if comp=="su":
        env.push(PP(P("in"),makeSyntR(semR)))
        return
    errorSyntR(" :compared-to without :degree:%s in %s"%(semR,semR.parent))
     
def concessionRole(semR,env,opts):
    traceSyntR("concessionRole",semR)
    syntR=makeSyntR(semR)
    if syntR.isOneOf(["S","SP"]):
        env.push(SP(C("although"),syntR))
    elif syntR.isOneOf(["AdvP","Adv"]):
        env.push(syntR)
    else:
        addPrep("despite", semR, env)
    
def conditionRole(semR,env,opts):
    traceSyntR("conditionRole",semR)
    concept=semR.get_concept()
    if concept=="as-long-as":
        roles=semR.get_roles()
        if ":op1" in roles:
            env.push(PP(P("as"),A("long"),P("as"),makeSyntR(roles[":op1"])))
            return
    if concept=="otherwise":
        env.push(SP(C("otherwise"),makeSyntR(semR)))
    else:
        env.push(SP(C("if"),makeSyntR(semR)))
        
def consistOfRole(semR,env,opts):
    traceSyntR("consistOfRole",semR)
    addPrep("of", semR, env)

def costRole(semR,env,opts):
    traceSyntR("costRole",semR)
    env.push(VP(V("cost").t("pr"),makeSyntR(semR)))

def degreeRole(semR,env,opts):
    traceSyntR("degreeRole",semR)
    global comp
    comp=""
    deg=semR.get_concept()
    if deg=="amr-unknown":
        opts.add("b","how ")
    elif deg=="more":
        opts.add("f","co")
        comp="co"
    elif deg=="most":
        opts.add("f","su")
        comp="su"
    elif deg=="part":
        env.unshift(Adv("partially"))
    elif deg in ["too","so","very","all","quite"]:
        env.unshift(Adv(deg))
    elif isAdverb(deg):
        env.push(Adv(deg))
    elif isAdjective(deg):
        env.push(A(deg))
    else:
        env.push(makeSyntR(semR))
     
def destinationRole(semR,env,opts):
    traceSyntR("destinationRole",semR)
    addPrep("to", semR, env)

def directionRole(semR,env,opts):
    traceSyntR("directionRole",semR)
    addPrep("to", semR, env)

def domainRole(semR,env,opts):
    traceSyntR("domainRole",semR)
    concept=semR.get_concept()
    if concept in determiners:
        env.put(":D",D(concept))
    elif isPronoun(concept):
        env.unshift(SP(Pro(concept),V("be")))
    else:
        env.push(VP(V("be"),makeSyntR(semR)))

##  :domain-of  => :mod

def durationRole(semR,env,opts):
    traceSyntR("durationRole",semR)
    if semR.get_concept()=="amr-unknown":
        env.unshift(Q("how long"))
        opts.add("a","?")
    else:
        addPrep("for", semR, env)
 
def employedByRole(semR,env,opts):
    traceSyntR("employedByRole",semR)
    env.push(VP(V("work").t("pr"),PP(P("for"),makeSyntR(semR))))

def exampleRole(semR,env,opts):
    traceSyntR("exampleRole",semR)
    env.push(PP(P("for"),N("example").a(','),makeSyntR(semR)))
 
def extentRole(semR,env,opts):
    traceSyntR("extentRole",semR)
    env.push(PP(P("for"),makeSyntR(semR)))
 
def frequencyRole(semR,env,opts):
    traceSyntR("frequencyRole",semR)
    concept=semR.get_concept()
    instance=semR.get_instance()
    if concept is None and is_number(instance):
        if instance==1:
            env.push(Adv("once"))
        elif instance==2:
            env.push(D("twice"))
        else:
            env.push(NP(NO(instance),N("time")))
    else: 
        env.push(makeSyntR(semR))

def instrumentRole(semR,env,opts):
    traceSyntR("instrumentRole",semR)
    addPrep("with", semR, env)
 
def liRole(semR,env,opts):
    traceSyntR("liRole",semR)
    semR_i=unquote(semR.get_instance())
    if semR_i=="-1":
        env.unshift(Adv("lastly"))
    elif semR_i=="1":
        env.unshift(Adv("first"))
    elif is_number(semR_i):
        env.unshift(Q("("+str(semR_i)+")"))
    elif semR_i[0]=='"':
        env.unshift(Q("("+semR_i+")"))

def locationRole(semR,env,opts):
    traceSyntR("locationRole",semR)
    concept=semR.get_concept()
    roles=semR.roles
    if concept=="amr-unknown":
        opts.add("typ",{"int":"whe"})
    elif concept=="between" and ":op1" in roles and ":op2" in roles:
        env.push(CP(C("and"),PP(P("between"),makeSyntR(roles[":op1"])),makeSyntR(roles[":op2"])))
        del roles[":op1"]
        del roles[":op2"]
    else:
        if isPreposition(concept) or isAdverb(concept):
            env.push(makeSyntR(semR))
        else:
            env.push(PP(P("in"),makeSyntR(semR)))
    
def mannerRole(semR,env,opts):
    traceSyntR("mannerRole",semR)
    cManner=semR.get_concept()
    if cManner=="amr-unknown":
        opts.add("typ",{"int":"how"})
    else:
        syntR=makeSyntR(semR)
        if syntR.isA("Q"):
            env.push(syntR)
        elif syntR.isA("A"):
            adv=Adv(adverbFromAdjective(syntR.lemma))
            adv.props=syntR.props
            env.push(adv)
        elif syntR.isOneOf(["S","V","VP"]):
            env.push(PP(P("by"),syntR.typ({"prog":True})))
        else:
            addPrep("with", semR, env)
 
def meaningRole(semR,env,opts):
    traceSyntR("meaningRole",semR)
    env.push(VP(V("mean").t("pr"),makeSyntR(semR)))
    
def mediumRole(semR,env,opts):
    traceSyntR("mediumRole",semR)
    addPrep("in", semR, env)

def modRole(semR,env,opts):    
    def simpleModNoun(concept,neg): ## check for "simple" cases
        if concept in ["all","many","both","no","too","any","other","some","one","kind-yy","then","such"]:
            env.put(":D",Q("kind of" if concept=="kind-yy" else concept))
            if neg:env.unshift(Q("not"))
            if concept in ["all","many","both"]:
                opts.add("n","p")
        elif concept in determiners:
            env.put(":D",D(concept))
        elif is_number(concept):
            env.push(NO(concept))
        elif isNoun(concept):## prefix the :mod for nouns
            newNoun=N(nouns[concept].lemma) # keep only noun from NP
            if ":A" in env:
                env.insertAfter(":A",":A",newNoun)
            else:
                env.put(":A",newNoun)
            if neg:env.insertBefore(":A",":A",Q("non"))
        elif isAdjective(concept):## postfix the :mod for adjectives
            newAdj=A(adjectives[concept].lemma)
            if ":A" in env:
                env.insertAfter(":A",":A",newAdj)
            else:
                env.put(":A",newAdj)
            if neg:env.insertBefore(":A",":A",Q("non"))
        elif isAdverb(concept):
            env.put(":D",Adv(concept))
        elif isVerb(concept):
            env.push(V(re.sub(r"-\d+$",'',concept)).t("pr"))
        elif semR.roles.areEmpty(): ## equivalent to processSimpleModOther
            env.push(Q(generateConceptWord(concept)))
        else:
            return False
        return True
            
    traceSyntR("modRole",semR)
    concept=semR.get_concept()
    if concept is None:
        env.push(makeSyntR(semR))
        return 
    roles=semR.roles
    neg=False
    if hasNegPolarity(roles):# negation will be applied to the generated relative 
        neg=True
    if roles.areEmpty():
        simpleModNoun(concept,neg)
        return
    syntR=makeSyntR(semR)
    if syntR.isOneOf(["N","NP"]):
        env.push(PP(P("of"),syntR))
    else:
        rel=relative(concept,syntR)
        if neg:rel.typ({"neg":True})
        env.push(rel)

def modeRole(semR,env,opts):
    traceSyntR("modeRole",semR)
    modeType=semR.get_instance()
    if modeType=="interrogative":
        opts.add("typ",{"int":"yon"})
    elif modeType=="expressive":
        opts.add("a","!")
    elif modeType=="imperative":
        opts.add("t","ip")
        if ":ARG0" in env: 
            del env[":ARG0"]
        if semR.parent is not None:
            pRoles= semR.parent.roles
            if ":ARG0" in pRoles:
                if pRoles[":ARG0"].concept=="we":
                    env.unshift(Q("let's"))
                if isPronoun(pRoles[":ARG0"].concept):
                    del semR.parent.roles[":ARG0"]
    else:
        errorSyntR("unknown mode:%s"%modeType)

def nameRole(semR,env,opts):
    traceSyntR("nameRole",semR)
    env.push(makeSyntR(semR))
    
def namedRole(semR,env,opts):
    traceSyntR("namedRole",semR)
    return nameRole(semR,env,opts)

def ordRole(semR,env,opts):
    traceSyntR("ordRole",semR)
    if semR.get_concept()=="ordinal-entity" :
        env.put(":A", makeSyntR(semR))
    else:
        errorSyntR("ord without ordinal-entity:%s"%semR)
 
def partOfRole(semR,env,opts):
    traceSyntR("partOfRole",semR)
    syntR=makeSyntR(semR)
    if syntR.isA("Pro"):
        poss=makePoss(syntR.lemma)
        poss.props=syntR.props
        env.put(":D",poss)
    else:
        addPrep("of", semR, env)

def pathRole(semR,env,opts):
    traceSyntR("pathRole",semR)
    concept=semR.get_concept()
    if concept=="past" and ":op1" in semR.roles:
        env.push(AdvP(Adv("past"),makeSyntR(semR.roles[":op1"])))
    else:
        syntR=makeSyntR(semR)
        if syntR.isA("Pro"):
            syntR.lemma="me"
        else:
            if syntR.isOneOf(["Adv","P","PP"]):
                env.push(syntR)
            else:
                env.push(PP(P("via"),syntR))

def polarityRole(semR,env,opts):
    traceSyntR("polarityRole",semR)
    if unquote(semR.get_instance())=="-":
        parent_concept=semR.get_parent_concept()
        if isVerb(parent_concept):
            opts.add("typ",{"neg":True})
        elif isNoun(parent_concept):
            env.put(":D",Adv("no"))
        else: 
            env.unshift(Adv("not"))
    elif semR.get_concept()=="amr-unknown":
        opts.add("typ",{"int":"yon"})

def politeRole(semR,env,opts): 
    traceSyntR("politeRole",semR)
    instance=unquote(semR.get_instance())
    if instance=="+":
        env.unshift(Q("Please"))
    elif instance=="-":
        env.unshift(Q("F..."))
    else:
        errorSyntR(":polite strange value:%s"%instance)

def possRole(semR,env,opts):
    traceSyntR("possRole",semR)
    if semR.get_concept()=="amr-unknown":
        env.push(PP(P("of"),Pro("whom")))
        opts.add("a","?")
    else:
        syntR=makeSyntR(semR)
        if syntR.isA("D"):
            env.put(":D",syntR)
        elif syntR.isA("Pro"):
            concept=semR.concept
            if concept is not None:
                env.put(":D",makePoss(concept))
            elif isinstance(semR.instance,SemanticRep.SemanticRep):
                ref=semR.instance.get_concept()
                poss=D("my")
                if isNoun(ref):
                    g=nouns[ref]["g"]
                    env.put(":D",poss.g(g if g is not None else "n"))
                elif isPronoun(ref):
                    poss.props=pronounOptions[ref]
                    env.put(":D",poss
                            .g(pronounOptions[ref]["g"] if "g" in pronounOptions[ref] else "m"))
                else:
                    env.put(":D",poss)
            else:
                env.put(":D",makePoss(syntR.lemma))
        else:
            env.push(PP(P("of"),syntR))

def purposeRole(semR,env,opts):
    traceSyntR("purposeRole",semR)
    roles=semR.get_roles()
    if ":ARG0" in roles:
        # remove useless subject reference to a variable
        del roles[":ARG0"]
    syntR=makeSyntR(semR)
    if syntR.isA("S") and syntR.elements[0].isA("VP"):
        env.push(PP(P("for"),syntR.elements[0].t("pr")))
    else:
        env.push(PP(P("for"),syntR))

 
def quantRole(semR,env,opts):
    def processSimpleQuant(concept):
        simpleQuants={ # concept: string to add to the start, boolean to indicate if plural
            "most":["most of",True],
            "more":["more",True],
            "numerous":["numerous",True],
            "many":["many",True],
            "multiple":["multiple",True],
            "few":["few",True],
            "some":["some",False],
            "such":["a sack of",False],
            "last":["last",False],
            "one":["one",False],
            "entire":["entire",False],
            "lot":["a lot",False],
            "sack":["a sack of",False]
            }
        if concept in simpleQuants:
            if concept=="lot": 
                env.push(Q(simpleQuants[concept][0]))
            else:
                env.unshift(Q(simpleQuants[concept][0]))
            if simpleQuants[concept][1]:opts.add("n","p")
            return True
        return False

    #  fuzzy operators from https://www.isi.edu/~ulf/amr/lib/popup/quantities.html#non-exact-quantities
    #  role :op1
    #  about, above, almost, approximately, around, at-least, at-most, below, close-to, couple, few, less-than, 
    #  lot, many, more-than, multiple, nearly, no-more-than, over, roughly, several, some, under, up-to
    #  number is dealt separately
    def fuzzyQuant1(concept):
        fuzzyQuants=['about', 'above', 'almost', 'approximately', 'around', 'at-least', 'at-most', 'below', 'close-to', 
                   'couple', 'few', 'less-than', 'lot', 'many', 'more-than', 'nearly', 'no-more-than', 
                   'over', 'roughly', 'several', 'some', 'under', 'up-to']
        if concept=="multiple":
            env.unshift(Q("multiple"))
            env.push(Q("of"))
            if ":op1" in semR.roles:
                env.push(makeSyntR(semR.roles[":op1"]))
            return True
        if concept in fuzzyQuants and ":op1" in semR.roles: 
            env.put(":D",AP(Q(generateConceptWord(concept)),makeSyntR(semR.roles[":op1"])))
            opts.add("n","p")
            return True
        return False

    def fuzzyQuant2(concept):
        roles=semR.get_roles()
        if ":op1" in roles and ":op2" in roles:
            env.put(":D",PP(P("between"),makeSyntR(roles[":op1"]),
                            C("and"),makeSyntR(roles[":op2"])))
            return True
        return False
    
    traceSyntR("quantRole",semR)
    concept=semR.get_concept()
    roles=semR.roles
    if len(roles)==0 and processSimpleQuant(concept):return
    if fuzzyQuant1(concept):return
    if fuzzyQuant2(concept):return
    if isinstance(concept,str) and re.match(r'.+-quantity$',concept): 
        env.unshift(PP(specialConcept.quantity(concept,roles,Env(),Options()),P("of")))
        return
    
    if concept=="amr-unknown":
        env.unshift(AdvP(Adv("how"),Adv("much")))
        opts.add("a","?")
    else:
        syntR=makeSyntR(semR,False)
        if syntR.isA("NO"):
            env.put(":D",syntR)
        else:
            env.unshift(PP(syntR,P("of")))
    

def scaleRole(semR,env,opts):
    traceSyntR("scaleRole",semR)
    semR_c=semR.get_concept()
    if (semR_c=="celsius"):
        env.push(PP(makeSyntR(semR),N("degree"),Q("Celsius")))
    else:
        env.push(PP(P("on"),D("the"),makeSyntR(semR),N("scale")))
 
def sourceRole(semR,env,opts):
    traceSyntR("sourceRole",semR)
    addPrep("from", semR, env)
 
def subeventOfRole(semR,env,opts):
    traceSyntR("subeventOfRole",semR)
    addPrep("during",semR,env)
 
def subsetRole(semR,env,opts):
    traceSyntR("subsetRole",semR)
    env.push(VP(V("include").t("pr"),makeSyntR(semR)))
 
def subsetOfRole(semR,env,opts):
    traceSyntR("subsetOfRole",semR)
    addPrep("of",semR,env)
 
def supersetRole(semR,env,opts):
    traceSyntR("supersetRole",semR)
    env.push(VP(V("contain").t("pr"),makeSyntR(semR)))

def timeRole(semR,env,opts):
    def processTime(concept,syntR):
        if concept=="amr-unknown":
            opts.add("typ",{"int":"whn"})
            env.push(syntR)
        elif syntR==A("former"):
            env.unshift(Adv("formerly"))
        elif syntR==Q("ex"):
            env.unshift(syntR)
        elif syntR==Q("about to"):
            env.push(Adv("about"))
            env.push(P("to"))
        elif isVerb(concept):
            env.push(SP(C("when"),syntR))
        elif syntR.isA("A"):
            env.push(Adv(adverbFromAdjective(syntR.lemma)))
        else:
            env.push(syntR)
            
    traceSyntR("timeRole",semR)
    syntR=makeSyntR(semR)
    concept=semR.get_concept()
    if concept=='date-entity': # very frequent case
        env.push(PP(P("on"),syntR))
        return
    return processTime(concept,syntR)

def topicRole(semR,env,opts):
    traceSyntR("topicRole",semR)
    if semR.concept=="amr-unknown":
        opts.add("typ",{"int":"wad"})
    else:
        addPrep("about", semR, env)
 
def unitRole(semR,env,opts):
    traceSyntR("unitRole",semR)
    env.push(makeSyntR(semR))
 
def wikiRole(semR,env,opts):
    traceSyntR("wikiRole",semR)
    name=semR.get_instance()
    if name=="-":return None
    ## uncomment the following line for adding links to Wikipedia
    #  it is now commented to ease comparisons...
    opts.add("tag",("a",{"href":"https://en.wikipedia.org/wiki/"+unquote(name)}))

### list of roles identified in the AMR-dictionary    
## https://www.isi.edu/~ulf/amr/lib/amr-dict.html#c
roleSwitch={
    ":accompanier":accompanierRole,
    ":age":ageRole,
    ":beneficiary":beneficiaryRole,
#     ":calendar":calendarRole, # cf time-entity in DSRconcepts
    ":cause":causeRole, 
    ":compared-to":comparedToRole,
    ":concession":concessionRole,
    ":condition":conditionRole,
    ":consist-of":consistOfRole,
    ":cost":costRole,
    ":degree":degreeRole,
    ":destination":destinationRole,
    ":direction":directionRole,
    ":domain":domainRole,
    ":domain-of":modRole,
    ":duration":durationRole,
    ":employed-by":employedByRole,
#     ":era":eraRole, # cf time-entity in DSRconcepts
    ":example":exampleRole,
    ":extent":extentRole,
    ":frequency":frequencyRole,
    ":instrument":instrumentRole,
    ":li":liRole,
    ":location":locationRole,
    ":manner":mannerRole,
    ":meaning":meaningRole,
    ":medium":mediumRole,
    ":mod":modRole,
    ":mode":modeRole,
    ":name":nameRole,
    ":named":namedRole,
    ":ord":ordRole,
    ":part-of":partOfRole,
    ":path":pathRole,
    ":polite":politeRole,
    ":polarity":polarityRole,
    ":poss":possRole,
    ":purpose":purposeRole,
    ":quant":quantRole,
    ":scale":scaleRole,
    ":source":sourceRole,
    ":subevent-of":subeventOfRole,
    ":subset":subsetRole,
    ":subset-of":subsetOfRole,
    ":superset":supersetRole,
    ":time":timeRole,         # cf time-entity in DSRconcepts
#     ":timezone":timezoneRole, # cf time-entity in DSRconcepts
    ":topic":topicRole,
    ":unit":unitRole,
#     ":value":valueRole,       # cf *-entity in DSRconcepts
    ":wiki":wikiRole,
}


def processStarRole(role,parentConcept,semR,env):
    ## determine the pronoun unless it is a special concept
    if parentConcept in gender:
        g=gender[parentConcept]
        if g!='n':
            if ":ARG0"==role or (":ARG1"==role and semR.parent is not None and ":ARG0" not in semR.parent.roles):
                pro=Pro("who")
            else: 
                pro=Pro("whom")
    else: pro=Pro("that")
    if semR.get_concept() not in specialConcept.conceptSwitch:
        semR.roles.delRole(role)
    syntR=makeSyntR(semR)
    if syntR.isA(["A","AP"]):
        env.put(":A",syntR)
    elif syntR.isOneOf(["N","NP","Adv","AdvP"]):
        env.push(syntR)
    else:
        env.push(SP(pro,syntR))

## HACK: rough classification of question types based on the "usual" arguments...
questionTypes={":ARG0":"was",":ARG1":"wad",":ARG2":"wod",":ARG3":"whe",":ARG4":"how"}
 
def processFrameOpRole(rolei,semRi,env,opts):
    if semRi.get_concept()=="amr-unknown" and rolei in questionTypes:
        opts.add("typ", {"int":questionTypes[rolei]})
        for roleii,semRii in semRi.roles.items():
            env.put(roleii,makeSyntR(semRii))
    elif semRi.concept=="amr-choice":
        opts.add("typ",{"int":"yon"})
        roles=semRi.roles
        if ":op1" in roles:env.push(makeSyntR(roles[":op1"]))
        if ":op2" in roles:env.push(SP(C("or"),makeSyntR(roles[":op2"])))
    else:
        syntRi=makeSyntR(semRi)
        if syntRi.isA("S"):
            # infinitive when the sentence is a verb without subject
            if syntRi.elements[0].isA("VP"):
                syntRi.elements[0].t("b")
                env.put(rolei,PP(P("to"),syntRi))
            elif semRi.parent is not None and semRi.parent.concept not in ["or","and"]:
                env.put(rolei,syntRi.add(Pro("that"),0))
            else:
                env.put(rolei,syntRi)
        elif syntRi.isA("Pro") and syntRi.lemma=="I":
            if (rolei==":ARG1" and ":ARG0" in env) or re.match(":ARG[2-9]",rolei):
                syntRi.setLemma("me")
                env.put(rolei,syntRi)
            else:
                env.put(rolei,syntRi)
        elif syntRi.isA("str"):
            env.put(rolei,Q(syntRi))
        else:
            env.put(rolei,syntRi)
    
## returns syntR (possibly modified_
##         env   environment with key,value pairs
##         opts  that should be applied once the env has been applied
def processRoles(concept,roles,ignoredRoles,dictInfo,env,opts):
    traceSyntR("processRoles",str(dictInfo))
    
    for (rolei,semRi) in roles.items():
        if rolei not in ignoredRoles:
            if isArgOp(rolei) or (isinstance(dictInfo,LexSem) and rolei in dictInfo.args): 
                processFrameOpRole(rolei,semRi, env, opts)
            elif rolei.startswith(':*'):
                processStarRole(rolei[2:],concept,semRi,env)            
            elif rolei in roleSwitch:
                roleSwitch[rolei](semRi,env,opts)
            elif rolei.startswith(":conj-"):
                env.push(SP(C(generateConceptWord(rolei[6:])),makeSyntR(semRi)))
            elif rolei.startswith(":prep-"):
                env.push(PP(P(generateConceptWord(rolei[6:])),makeSyntR(semRi)))
            else:
    #             print("ignored role:"+rolei+":"+semRi.shortStr())
                env.push(makeSyntR(semRi))
    return dictInfo

if __name__ == '__main__':
    pass