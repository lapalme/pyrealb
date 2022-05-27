'''
Created on Feb 12, 2021

@author: lapalme
'''
import re
from utils import traceSyntR, setTraceSyntR, is_number, unquote, generateConceptWord, errorSyntR, predicate,\
                  relative, adverbFromAdjective, isArgOp, ensurePhrase, hasNegPolarity
from lexicalSemantics import Env, Options, LexSem
# from jsRealBclass import N,A,Pro,D,Adv,V,C,P,DT,NO,Q,  NP,AP,AdvP,VP,CP,PP,S,SP,  Constituent, Terminal, Phrase
from pyrealb import *
from amrDico import gender, getSyntR, makePoss, isPossessive, isPronoun, makePro, \
                    isNoun, makeN, isAdjective, makeA, isVerb, makeV,makeCP, nouns, verbs, getNominalization, getPOS
from amrDicoGen import verbalizations,morphVerbalizations,adjInfo,nounInfo

import SemR2SyntR,roleProcessing


quoteInfo= lambda string:LexSem(string,"Q",[],lambda:Q(unquote(string)))

## simplify notation because "from SemR2SyntR import makeSyntR"
#  makes the "recursive" import loop
def makeSyntR(semR,checkSpecial=True):
    return SemR2SyntR.makeSyntR(semR,checkSpecial)

##  add syntR for all roles except for the ignored ones at the end of syntR
def addRoles(concept,roles,ignored,dictInfo,env,opts):
    dictInfo=roleProcessing.processRoles(concept,roles,ignored,dictInfo,env,opts)
    syntR=dictInfo.apply(env,opts)
    return syntR

# create a Date using DT by first building a string for the Javascript Date object and the jsRealB dOpt
# monthNames=["*dummy*","January","February","March","April","May","June","July","August",
#             "September","October","November","December"]
## https://www.isi.edu/~ulf/amr/lib/amr-dict.html#date-entity
# https://github.com/amrisi/amr-guidelines/blob/master/amr.md#other-entities-dates-times-percentages-phone-email-urls
def dateEntity(concept,roles,env,opts):
    def zPad(s): #ensure a string of length 2 padded with a 0 
        if len(s)==2: return s
        if len(s)==1: return "0"+s
        if len(s)>2 : return s[0:2]
        return s
    
    def checkDateComp(date,rName,dOptField,length,default):
        if rName in roles:
            val=roles[rName].instance
            if is_number(val) and len(val)<=length:
                date+=val.rjust(length,"0")
                dOpt[dOptField]=True
            else:
                print("dateEntity: strange %s:%s"%(rName,val))
                date+=default
        else:
            date+=default
        return date
    
    traceSyntR("dateEntity",concept)
    if ":time" in roles and roles[":time"].get_concept()=="amr-unknown":
        return Q("what time is it ?")
    date="" # ISO format "YYYY-MM-DDTHH:mm:ss"
    dOpt={"year":False , "month":False , "date":False , "day":False , "hour":False , 
          "minute":False , "second":False , "nat":True, "det":False, "rtime":False}
    date=checkDateComp(date,":year","year",4,"2021")+"-"
    date=checkDateComp(date,":month", "month", 2, "01")+"-"
    date=checkDateComp(date,":day", "date", 2, "01")+"T"
    if ":time" in roles:
        timeS=roles[":time"].instance
        if isinstance(timeS,str) and ":" in timeS:
            time=unquote(timeS)
            tParts=time.split(":")
            if len(tParts)==2:
                tParts.append("00")
            if len(tParts)==3:
                date+=zPad(tParts[0])+":"+zPad(tParts[1])+":"+zPad(tParts[2])
                dOpt["hour"]=True
                dOpt["minute"]=True
                dOpt["second"]=True
    if not dOpt["hour"]:
        date+="00:00:00"
        dOpt["hour"]=False
        dOpt["minute"]=False
        dOpt["second"]=False
    sp=SP(DT(date+"-05:00").dOpt(dOpt))## HACK: force Montreal time zone  
    if ":timezone" in roles:
        sp.add(makeSyntR(roles[":timezone"]))
    if ":weekday" in roles:
        sp.add(Q(unquote(roles[":weekday"].get_concept()).capitalize()),0)
    if ":season" in roles:
        sp.add(Q(unquote(roles[":season"].get_concept())),0)
    if ":mod" in roles:
        sp.add(Q(unquote(roles[":mod"].get_concept())),0)
    if ":dayperiod" in roles:
        sp.add(Q(unquote(roles[":dayperiod"].get_concept())))
    if ":quarter" in roles:
        sp.add(NP(makeSyntR(roles[":quarter"]).dOpt({"ord":True}),N("quarter")))
    if ":year2" in roles:
        sp.add(makeSyntR(roles[":year2"]).dOpt({"raw":True}).b("-"))
    if ":era" in roles:
        sp.add(Q(unquote(roles[":era"].get_instance())))
    if ":calendar" in roles:
        sp.add(N("calendar").a(":"))
        sp.add(makeSyntR(roles[":calendar"]))
    if ":decade" in roles:
        sp.add(makeSyntR(roles[":decade"]))
        sp.add(Q("s"))
    return sp

def exemplifyEntity(concept,roles,env,opts):
    traceSyntR("exemplifyEntity",concept)
    if roles.areEmpty():
        return PP(P("for"),N("example"))
    return None

# very special (and frequent) case of government-organization
# ['government-organization',\g, [':*:ARG0',['govern-01',g2, [':ARG0',g], [':ARG1',Country]
#   by "government of Country"
def governmentOrganization(concept,roles,env,opts):
    traceSyntR("governmentOrganization", concept)
    if ":*:ARG0" in roles:
        if roles[":*:ARG0"].get_concept()=="govern-01":
            starArg0Roles=roles[":*:ARG0"].roles
            if len(roles)==1:
                return addRoles(concept, starArg0Roles, [":ARG0"], nounInfo("government"), env, opts)
            elif  ":ARG1" in starArg0Roles:
                dictInfo=nounInfo("government")
                env.push(PP(P("of"),makeSyntR(starArg0Roles[":ARG1"])))
                return addRoles(concept, starArg0Roles,[":ARG0",":ARG1"], dictInfo, env, opts)
    dictInfo=nounInfo("organization")
    env.put(":A",A("governmental"))
    return addRoles(concept, roles, [":*:ARG0"], dictInfo, env, opts)
     
### special roles called "constructions" described in the LREC2018 paper by Bonial et al.
###       https://www.aclweb.org/anthology/L18-1266.pdf
def haveDegree91(concept,roles,env,opts):
    traceSyntR("haveDegree91",concept)
    subject=None
    attribute=None
    comp=""
    quant=None
    if ":ARG1" in roles:
        arg1=roles[":ARG1"]
#         print("haveDegree1:",arg1.instanceIsRef())
        if not arg1.instanceIsRef(): # do not follow link for subject
            subject=makeSyntR(arg1)
    if ":ARG2" in roles:
        concept=roles[":ARG2"].concept
        attribute=makeSyntR(roles[":ARG2"])
        # HACK: remove spurious pronouns created by starrole
        if isinstance(attribute, AP) and len(attribute.elements)>1 and isinstance(attribute.elements[1],Pro):
            del attribute.elements[1]
            if len(attribute.elements)==1:
                attribute=attribute.elements[0]
    else:
        errorSyntR("have-degree-91 without :ARG2:%s"%concept)
        return Q("degree-91")
    if ":mod" in roles:
        if isinstance(attribute,Terminal):
            attribute=AP(attribute)
        attribute.add(makeSyntR(roles[":mod"]))        
    if ":ARG3" in roles:
        rolesARG3=roles[":ARG3"]
        deg=rolesARG3.get_concept()
        moreRoles=rolesARG3.get_roles()
        if moreRoles!=None and len(moreRoles)>0:
            if ":quant" in moreRoles:
                quant=makeSyntR(moreRoles[":quant"])
            else:
                attribute.add(makeSyntR(moreRoles[0][1]))
        if deg=="more":
            attribute=attribute.f("co")
            if quant!=None:
                attribute=NP(quant,attribute)
                quant=None
            comp="co"
        elif deg=="most":
            if isinstance(attribute,A):
                attribute=AP(D("the"),attribute.f("su"))
            else:
                attribute=AP(attribute,D("the"),Adv("most"))
            comp="su"
        elif deg in ["too","so","less"]:
            attribute=AdvP(Adv(deg),attribute)
            if deg=="less":
                comp="co"
            elif quant!=None:
                attribute=AP(attribute,quant)
                quant=None
        elif deg=="equal":
            attribute=AdvP(Adv("as"),attribute,Adv("as"))
        elif deg=="times":
            if quant!=None:
                quant=NP(quant,N("time"))
                attribute=attribute.f("co")
            comp="co"
        else:
            attribute=AdvP(attribute,Adv(deg))
    if ":ARG4" in roles:
        syntR4=makeSyntR(roles[":ARG4"])
        if comp=="co":
            attribute=PP(attribute,P("than"),syntR4)
            if quant!=None:
                attribute.add(quant,0)
        elif comp=="su":
            attribute=AP(attribute,Adv("in"),syntR4)
        else:
            attribute.add(syntR4)
    if ":ARG5" in roles:
        attribute.add(makeSyntR(roles[":ARG5"]))
    if ":ARG6" in roles:
        attribute=NP(attribute,makeSyntR(roles[":ARG6"]))
#     print("have-degree-91:subject:",subject)
    while ":li" in roles:
        semR=roles[":li"]
        del roles[":li"]
        ## analogous to roleProcessing.lirole
        semR_i=unquote(semR.get_instance())
        if semR_i=="-1":
            attribute.add(Adv("lastly"),0)
        elif semR_i=="1":
            attribute.add(Adv("first"),0)
        elif is_number(semR_i):
            attribute.add(Q("("+str(semR_i)+")"),0)
        elif semR_i[0]=='"':
            attribute.add(Q("("+semR_i+")"),0)
    restRoles=addRoles(concept, roles, [":ARG1",":ARG2",":ARG3",":ARG4",":ARG5",":ARG6",":li",":mod",":polarity"], 
                       LexSem("degree","SP",[],lambda:SP()),env, opts)        
    if len(restRoles.elements)>0:
        attribute=ensurePhrase(attribute).add(restRoles)
    if subject!=None:
        attribute=predicate(subject,attribute)
        if hasNegPolarity(roles):
            return attribute.typ({"neg":True})
    else:
        if hasNegPolarity(roles):
            return AdvP(Adv("not"),attribute)
    return attribute

def havePolarity91(concept,roles,env,opts):
    if ":ARG2" in roles:
        pol=unquote(roles[":ARG2"].get_instance())
        if  pol=='-':
            env.push(AdvP(Adv("not")))
        elif pol =='+':
            env.push(AdvP(Adv("yes")))
        return addRoles(concept, roles, [":ARG2"], LexSem("polarity","SP",[],lambda:SP()), env, opts)
    return None
        
def havePurpose91(concept,roles,env,opts):
    if ":ARG2" in roles:
        if roles[":ARG2"].get_concept()=="amr-unknown":
            env.put(":start",Q("For what ?"))
        return addRoles(concept, roles, [],
                        LexSem("have-purpose","S",[":ARG1",":ARG2"],
                               lambda arg1,arg2:S(arg1,VP(V("be"),PP(P("for"),arg2)))), env, opts)
    return None
    
  
#  from https://github.com/amrisi/amr-guidelines/blob/master/amr.md#quantities
#             have-quant-91
# ARG1: entity (thing being quantified)
# ARG2: quantity (numerical or quantifier: many, much)
# ARG3: degree mention (more, less, equal, too)
# ARG4: compared-to
# ARG5: superlative: reference to superset
# ARG6: consequence, result
def haveQuant91(concept,roles,env,opts):
    traceSyntR("haveQuant91",concept)
    if ":ARG1" in roles:
        quant=makeSyntR(roles[":ARG1"])
    else:
        errorSyntR("haveQuant91 without entity:%s"%concept)
        quant=SP(Q("*entity*"))
    if isinstance(quant,Terminal):
        quant=SP(quant)
    if ":ARG2" in roles:
        quant.add(makeSyntR(roles[":ARG2"]),0)
    else:
        quant.add(NP(D("the"),N("number"),P("of")),0)
    if ":ARG3" in roles:
        quant.add(VP(V("be"),makeSyntR(roles[":ARG3"])))        
    if ":ARG4" in roles:
        quant.add(PP(P("than"),
                        makeSyntR(roles[":ARG4"])))
    if ":ARG5" in roles:
        quant.add(PP(P("of"),makeSyntR(roles[":ARG5"])))
    if ":ARG6" in roles:
        quant.add(PP(P("for"),makeSyntR(roles[":ARG6"])))
    return addRoles(concept, roles, [":ARG1",":ARG2",":ARG3",":ARG4",":ARG5",":ARG6"], 
                    LexSem("qty","NP",[],lambda:quant), env, opts)

## https://github.com/amrisi/amr-guidelines/blob/master/amr.md#special-frames-for-roles
# Core roles of have-rel-role-91:
#
# :ARG0 of have-rel-role-91 entity A
# :ARG1 of have-rel-role-91 entity B
# :ARG2 of have-rel-role-91 role of entity A (must be specified)
# :ARG3 of have-rel-role-91 role of entity B (often left unspecified)
# :ARG4 of have-rel-role-91 relationship basis (contract, case; rarely used)
# Typical have-rel-role-91 roles: father, sister, husband, grandson, godfather,
#            stepdaughter, brother-in-law; friend, boyfriend, buddy, enemy; landlord, tenant etc.
def haveRelRole91(concept,roles,env,opts):
    traceSyntR("haveRelRole91",concept)
#     syntR_A=makeSyntR(roles[":ARG0"]) if ":ARG0" in roles else None
    syntR_B=makeSyntR(roles[":ARG1"]) if ":ARG1" in roles else None
    if ":ARG2" in roles: 
        relation=makeSyntR(roles[":ARG2"])
        if isinstance(syntR_B,Pro) and isinstance(relation,NP):
            relation.elements[0]=makePoss(syntR_B.lemma)
            return addRoles(concept, roles, [":ARG1",":ARG2"], 
                            LexSem("relation","NP",[":ARG0"],lambda arg0:S(arg0,VP(V("be"),relation))), env, opts)
        if syntR_B!=None:
            dictInfo=LexSem("have-relation","S",[":ARG0",":ARG3",":ARG4"],
                            lambda arg0,arg3,arg4:S(arg0,VP(V("be"),relation,syntR_B,arg3,arg4)))
            return addRoles(concept, roles, [":ARG1",":ARG2"], dictInfo, env, opts)        
        else:
            return addRoles(concept, roles, [":ARG2"],LexSem("rel-role","NP",[],lambda:relation), env, opts)
    else:
        errorSyntR("haveRelRole91 with no :ARG2:\n%s"%concept)
        return Q("*rel*")

def hyperlink91(concept,roles,env,opts):
    traceSyntR("hyperlink91",concept)
    if ":ARG1" in roles:
        text=makeSyntR(roles[":ARG1"])
    else:
        text=NP(N("link"))
    if roles.areEmpty():
        return text.tag(("a",{"href":"#"}))
    if ":ARG3" in roles:
        if roles[":ARG3"].instanceIsRef():
            return text.tag(("a",{"href":"#"}))
        if roles[":ARG3"].concept=="url-entity":
            urlEntity=roles[":ARG3"]
            if ":value" in urlEntity.roles:
                link=urlEntity.roles[":value"].get_instance()
            elif urlEntity.roles.areEmpty():
                link="#"
            opts.add("tag",("a",{"href":link}))
            return addRoles(concept,roles,[":ARG1",":ARG3"],LexSem("hyperlink","NP",[],lambda:text),env,opts)
    return None
    
def multisentence(concept,roles,env,opts):
    traceSyntR("multisentence",concept)
    # HACK: only works for :snt[1-9]
    sntKeys=sorted([key for key in roles.keys() if re.fullmatch(r":snt\d",key)])
    last=len(sntKeys)-1
    multiS=S()
    for i in range(len(sntKeys)):
        si=S(makeSyntR(roles[sntKeys[i]])).cap("")
        if i<last:si.a(". ")
        multiS.add(si)
    return addRoles(concept, roles, sntKeys,LexSem("multi-sentence","S",[],lambda:multiS), env, opts)

def namedEntity(concept,roles,env,opts):
    name = roles[":name"]
    if name != None:
#         name_named = name.roles[":named"] or name.roles[":op1"]
#         if name_named != None:
#             #### (p / NamedEntity :name NAME  other roles)) replaced by evaluation of NAME followed by other roles
#             nameSyntR=
#             return addRoles(concept, name.roles, [":named",":op1"], quoteInfo(name_named.get_instance()), env, opts)
        if name.concept == "name":
            nameSyntR=makeSyntR(name)
            return addRoles(concept, roles, [":name"], LexSem("name","NP",[],lambda:nameSyntR), env, opts)
        return addRoles(concept, roles, [":name"], nounInfo(concept), env, opts)
    return None
    

# def nextTo(semR):
#     return AdvP(Adv("next"),P("to"),
#                 makeSyntR(semR.get_roles()[":op1"]))

## deal with frequent pattern associated with a number
# (n / number :quant-of AMR) == [number,\n, [':*:quant',[AMR [':quant',n]] ==>
#     NP(D("the"),N("number"),PP(P("of"),{AMR}))
def number(concept,roles,env,opts):
    traceSyntR("number", concept)
    if ":*:quant" in roles:
        roles1=roles[":*:quant"].get_roles()
        if ":quant" in roles1:
            del roles1[":quant"]
            dictInfo=nounInfo(concept)
            env.push(PP(P("of"),makeSyntR(roles[":*:quant"],False).n("p")))
            return addRoles(concept,roles,[":*:quant"],dictInfo,env,opts)
    return addRoles(concept, roles, [":*:quant"], nounInfo(concept), env, opts)
        
def person(concept,roles,env,opts):
    traceSyntR("person",concept)
    ## with a single :named role ignore person
    if ":named" in roles and len(roles)==1:
        return makeSyntR(roles[":named"])
    ## deal with frequent patterns associated with a person
    #### (p/person :ARG0-of (v / verb)) == ((p/person :*:ARG0 (v / verb :ARG0 p))) 
    ####         ==> find verbalization
    starARG0=roles[":*:ARG0"]
    if starARG0!=None:
        starARG0_ARG0=starARG0.roles[":ARG0"] if ":ARG0" in starARG0.roles else None
        if starARG0_ARG0!=None:
            if len(starARG0_ARG0.roles)==1:
                verb=starARG0_ARG0.get_concept()
                nom=getNominalization(verb)
                if nom!=None:
                    return addRoles(concept, roles, [":*:ARG0"], nounInfo(nom), env, opts)
        if re.match(r"have-(org|rel)-role-91",starARG0.get_concept()) and len(starARG0.roles)==2:
            ##### shortcut : https://www.isi.edu/~ulf/amr/lib/amr-dict.html#shortcuts
            ### (p2 / person :ARG0-of (h / have-org-role-91 :ARG2 (m / mayor))) ==
            ###      [person,\p2,[':*:ARG0',['have-org-role-91',h,[':ARG0',p2], [':ARG2',[mayor,m]]] ==>
            ###  mayor !!!
            starARG0_ARG2=starARG0.roles[":ARG2"]
            if starARG0_ARG2!=None:
                nom=makeSyntR(starARG0_ARG2)
                if isinstance(nom,(NP,N)):
                    return addRoles(concept, roles, [":*:ARG0"], LexSem("person","NP",[],lambda:nom), env, opts)
        if re.match(r"have-(org|rel)-role-91",starARG0.get_concept()) and len(starARG0.roles)==3:
            ##### shortcut : https://www.isi.edu/~ulf/amr/lib/amr-dict.html#shortcuts
            ### (p / person
            ###          :ARG0-of (h / have-rel-role-91 :ARG1 (i / i):ARG2 (g / mother))) ==
            ### (p person [:*:ARG0 (h2 have-rel-role-91 [:ARG1 ^h ↑h2,
            ###                                          :ARG2 (m mother [] ↑h2),
            ###                                          :ARG0 ^p ↑h2] ↑p) ^_])            
            ###   (his/her) mother !!! 
            starARG0_ARG1=starARG0.roles[":ARG1"]
            starARG0_ARG2=starARG0.roles[":ARG2"]
            person=None
            if starARG0_ARG1!=None and starARG0_ARG2!=None and isNoun(starARG0_ARG2.get_concept()):
                conceptSyntR=makeSyntR(starARG0_ARG2)
                if starARG0_ARG1.instanceIsRef():
                    env.put(":D",makePoss(SemR2SyntR.instance2SyntR(starARG0_ARG1)))
                    person=addRoles(concept, starARG0_ARG2.roles,[":ARG1",":ARG2"], 
                                    LexSem("person","NP",[],lambda:conceptSyntR), env, opts)
                elif starARG0_ARG1.roles.areEmpty():
                    starARG0_ARG1concept=starARG0_ARG1.get_concept()
                    if isNoun(starARG0_ARG1concept):
                        env.put(":D",makeSyntR(starARG0_ARG1))
                        person=addRoles(concept,starARG0_ARG2.roles,[":ARG1",":ARG2",":ARG0"],
                                        LexSem("person","NP",[],lambda:conceptSyntR),env,opts)
                    elif isPronoun(starARG0_ARG1concept):
                        conceptSyntR.elements[0]=makePoss(starARG0_ARG1concept)
                        person=addRoles(concept,starARG0_ARG2.roles,[":ARG1",":ARG2",":ARG0"],
                                        LexSem("person","NP",[],lambda:conceptSyntR),env,opts)
                if person!=None:
                    return addRoles(concept, roles, [":*:ARG0"],LexSem("person","NP",[],lambda:person), env, opts)
    return namedEntity(concept,roles,env,opts)


### dealing with different types of quantity
#       https://github.com/amrisi/amr-guidelines/blob/master/amr.md#quantities
def quantity(concept,roles,env,opts):
    traceSyntR("quantity",concept)
    if ":quant" in roles:
        qty=makeSyntR(roles[":quant"])
        if ":unit" in roles:
            unit=makeSyntR(roles[":unit"])
            if isinstance(unit,Pro): # get the referenced unit...
                unit=makeSyntR(roles[":unit"].instance)
            if isinstance(unit,NP) and qty!=None and isinstance(qty,NO):
                unit.elements[0]=qty
                qty=unit
            elif isinstance(unit,Phrase):
                qty=unit.add(qty)
            else:
                qty=SP(unit,qty)
        elif len(roles)>1 and isinstance(qty,Terminal):
            qty=NP(qty)
        if ":scale" in roles:
            qty.add(PP(P("on"),makeSyntR(roles[":scale"]),N("scale")))
        if ":*:ARG1" in roles:
            qty.add([D("the"),N("quantity"),Pro("that")])
        env.push(qty)
    return addRoles(concept,roles,[":quant",":unit",":scale"],LexSem("qty","SP",[],lambda:SP()),env,opts)

def streetAddress91(concept,roles,env,opts):
    traceSyntR("streetAddress91", concept)
    res=SP()
    for i in range(1,7):
        argi=":ARG"+str(i)
        if argi in roles:
            argi_role=roles[argi]
            if argi_role.get_concept()==None:
                res.add(Q(unquote(argi_role.get_instance())))
            else:
                res.add(makeSyntR(argi_role))
    return res

#  transform the SemanticRep by applying the nominalization
def checkNominalization(concept,roles,env,opts):
    traceSyntR("checkNominalization", concept)
    if roles.areEmpty():
        if concept in verbalizations and "" in verbalizations[concept]:
            nominalization=verbalizations[concept][""]
            return addRoles(nominalization,roles,[],nounInfo(nominalization),env,opts)
        elif isVerb(concept):
            verbLemma=re.sub(r"-\d+$","",concept)
            if verbLemma in morphVerbalizations and "noun" in morphVerbalizations[verbLemma]:
                nominalization=morphVerbalizations[verbLemma]["noun"]
                return addRoles(nominalization,roles,[],nounInfo(nominalization),env,opts)
        else:
            return None
    if concept in verbalizations:
        verbArgs=[key for key in verbalizations[concept].keys() if key!=""]
        if len(verbArgs)==0:return None
        for verbArg in verbArgs:
            if verbArg in roles:
                subSemR=roles[verbArg]
                if subSemR.concept in verbalizations[concept][verbArg]:
                    nominalization=verbalizations[concept][verbArg][subSemR.concept]
                    del subSemR.roles[verbArg[2:]] # remove added :ARGi corresponding to the :*:ARGi
                    # splice rest of roles of subSemR into parent roles
                    for rl,sem in subSemR.roles.items():
                        roles.addRole(rl,sem)
                    del roles[verbArg]
                    return addRoles(nominalization,roles,[],nounInfo(nominalization),env,opts)
    # process morphVerbalizations
    if isVerb(concept):
        verbLemma=re.sub(r"(-\d+)?$",r"",concept)
        if verbLemma in morphVerbalizations:
            morphVerb=morphVerbalizations[verbLemma]
            if ":polarity" in roles: return None #fail if :polarity role is present
            if ":ARG1" in roles:
                verbArgs=[key for key in roles.keys() if key!=":ARG1"]
                if any([isArgOp(arg) for arg in verbArgs]): return None #fail if any :ARGi or :opi is present
                # OK if :ARG1 is a pronoun that refers to the :ARG0 of the verb of the upper level
                if roles[":ARG1"].instanceIsRef():
                    refARG1=roles[":ARG1"].instance
                    instanceRole=refARG1.get_my_role()
                    if ":ARG0" == instanceRole and "noun" in morphVerb:
                        morphVerb=morphVerb["noun"]
                        return addRoles(morphVerb,roles,[":ARG1"],nounInfo(morphVerb),env,opts)
                # TODO: should check for "actor"...
    return None

# def reify(semR):
#     traceSyntR("reify",semR)
#     infos=reifications[semR.get_concept()]
#     rel=infos["rel"]
#     domain=infos["domain"]
#     range=infos["range"]
#     roles=semR.get_roles()
#     if roles.contains(domain):
#         conceptDSR=makeDSR(roles[domain])
#         if roles.contains(range):
#             rangeN=roles[range]
#             if rel in roleSwitch:
# #                 print("**reify %s\n%s\n%s"%(rel,rangeN.prettyStr(),conceptDSR.prettyStr()))
#                 conceptDSR=roleSwitch[rel](rangeN,conceptDSR,False)
#                 return conceptDSR if semR.get_parent()==None else sp(adv("that"),conceptDSR)
#             else:
#                 errorSyntR("%s not found"%rangeN)
#         else:
#             errorSyntR("no %s in %s"%(range,semR.shortStr()))
#     else:
#         errorSyntR("no %s in %s"%(domain,semR.shortStr()))
#     return ct(semR.get_concept()) 


## Modality
modalPattern="s(pronouns['it'],vp(v('be'),%s,sp(d('that')))"
##      concept:(word,argN,modOption,tense)
modals={"possible-01":("possible",":ARG1","poss","p"),
        "obligate-01":("mandatory",":ARG2","obli","p"),
        "permit-01":("permissible",":ARG1","perm","p"),
        "recommend-01":("recommended",":ARG1","nece","ps"),
#         "prefer-01":("preferable",":ARG1","will","ps"),
        }

def modal(concept,roles,env,opts):
    traceSyntR("modal",concept)
    (adj,arg,option,t)=modals[concept]
#     print("roles:"+str(roles))
    if arg not in roles:
        return A(adj)
    argSyntR=makeSyntR(roles[arg])
    opts.add("t",t)
    opts.add("typ",{"mod":option})
    return addRoles(concept,roles,[arg],LexSem("modal","S",[],lambda:argSyntR),env,opts)

conceptSwitch={
    "date-entity":dateEntity,
    "exemplify-01":exemplifyEntity,
    "government-organization":governmentOrganization,
    "have-degree-91":haveDegree91,
    "have-quant-91":haveQuant91,
    "have-polarity-91":havePolarity91,
    "have-purpose-91":havePurpose91,
    "have-rel-role-91":haveRelRole91,
    "hyperlink-91":hyperlink91,
    "multi-sentence":multisentence,
    "person":person,
    "street-address-91":streetAddress91,
}

namedEntityList = [
    ## list of NE taken from https://www.isi.edu/~ulf/amr/lib/ne-types.html
'aircraft', 'aircraft-type', 'airport', 'amino-acid', 'amusement-park', 'animal', 'award', 'bay', 'book', 'bridge',
'broadcast-program', 'building', 'canal' , 'canal', 'canyon', 'car-make', 'cell', 'cell-line', 'city',
'city-district', 'company', 'conference', 'constellation', 'continent', 'country', 'country-region', 'county',
'court-decision', 'criminal-organization', 'desert', 'disease', 'dna-sequence', 'earthquake', 'enzyme',
'ethnic-group', 'event', 'facility', 'family', 'festival', 'food-dish', 'forest', 'game', 'gene',
'government-organization', 'gulf', 'hotel', 'incident', 'island', 'journal', 'lake', 'language', 'law', 'league',
'local-region', 'location', 'macro-molecular-complex', 'magazine', 'market', 'market-sector', 'medical-condition',
'military', 'molecular-physical-entity', 'moon', 'mountain', 'museum', 'music', 'music-key', 'musical-note',
'nationality', 'natural-disaster', 'natural-object', 'newspaper', 'nucleic-acid', 'ocean', 'organization', 'palace',
'park', 'pathway', 'peninsula', 'person', 'picture', 'planet', 'political-movement', 'political-party', 'port',
'product', 'program', 'protein', 'protein-family', 'protein-segment', 'province', 'publication', 'railway-line',
'regional-group', 'religious-group', 'research-institute', 'river', 'road', 'school', 'sea', 'ship', 'show',
'small-molecule', 'species', 'sports-facility' , 'star', 'state', 'station', 'strait', 'taxon', 'team',
'territory', 'theater', 'treaty', 'tunnel', 'university', 'valley', 'variable', 'vehicle', 'volcano', 'war',
'work-of-art', 'world-region', 'worship-place', 'writing-script', 'zoo'
]

def isSpecialConcept(lemma): # used in semRep2SyntRep.instance2SyntR
    return lemma=="person" or lemma=="number" or lemma in modals or \
        re.match(r'.+-quantity$',lemma) or lemma in conceptSwitch or lemma in namedEntityList

def checkSpecialConcept(semR):
    concept=semR.get_concept()
    traceSyntR("checkSpecialConcept:%s"%concept,semR)
    roles=semR.roles
    env=Env()
    opts=Options()
    nominalizedSyntR = checkNominalization(concept,roles,env,opts)
    if nominalizedSyntR!=None:
        return nominalizedSyntR
    
    if concept=="person": return person(concept,roles,env,opts)
    if concept=="number": return number(concept,roles,env,opts)
    if concept in modals: return modal(concept,roles,env,opts) 
        
    if re.match(r'.+-quantity$',concept): return quantity(concept,roles,env,opts)
    if concept in conceptSwitch:   return conceptSwitch[concept](concept,roles,env,opts)
    if concept in namedEntityList: return namedEntity(concept,roles,env,opts)
#     if concept in reifications:
#         return reify(semR)
    return None


if __name__ == '__main__':
    pass