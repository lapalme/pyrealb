'''
Created on Jan 18, 2021

@author: lapalme
'''
import re

from SemanticRep import SemanticRep, tests,RoleList
# from jsRealBclass import N,A,Pro,D,Adv,V,C,P,DT,NO,Q,  NP,AP,AdvP,VP,CP,PP,S,SP, \
#                          jsRealB, Constituent, Terminal, Phrase
from pyrealb import *
from amrDicoGen import pp
from amrDico import gender, getSyntR, makePoss, isPossessive, isPronoun, makePro, pronounOptions, addOptions,\
                    isNoun, isAdjective, makeN, isVerb, makeV,makeCP, nouns, verbs, getNominalization, getPOS
from utils import traceSyntR, setTraceSyntR, is_number, unquote, generateConceptWord, errorSyntR, predicate
from lexicalSemantics import Env, Options, LexSem
import roleProcessing
import specialConcept


def instance2SyntR(semR):
    traceSyntR("instance2dsr",semR)
    instance=semR.instance
    if isinstance(instance,SemanticRep):
        myRole=semR.get_my_role()
        amrRef=instance
        refRole=amrRef.get_my_role()
        refConcept=amrRef.get_concept()
#         print("myRole:%s  refRole:%s refConcept:%s"%(myRole,refRole,refConcept))
        if isNoun(refConcept) or specialConcept.isSpecialConcept(refConcept):
            if myRole==":ARG0" and refRole!=None:
                pronoun=Pro("I")
            elif myRole==":ARG1": # is object the same as the subject?
                parent=semR.get_parent()
                parentRoles=parent.get_roles()
                if ":ARG0" in parentRoles and (parentRoles[":ARG0"]==amrRef or instance==parentRoles[":ARG0"].instance):
                    pronoun=Pro("myself")
                elif parent.get_my_role()==":*:ARG0": # object is the subject of the subordinate
                    pronoun=Pro("me")
                else:
                    pronoun=Pro("I")
            else:
                pronoun=Pro("me")
            return pronoun.pe(3).g(gender[refConcept] if refConcept in gender else "n")
        elif isPronoun(refConcept):
            pronoun=Pro("I")
            return addOptions(pronoun,pronounOptions[refConcept]) if refConcept in pronounOptions else pronoun
        elif isVerb(refConcept):
            return VP(V(re.sub(r"-\d+$","",refConcept)).t("b"))
        else:
            # clean the referenced concept and quote it
            return Q(generateConceptWord(refConcept))            
    elif is_number(instance):
        return NO(unquote(instance))
    elif instance[0]=='"':
        return Q(unquote(instance))
    elif instance in ['-','+']:
        return instance 
    else:
        errorSyntR(instance+" :undefined instance")
        return Q(instance)


frameNumberRE=re.compile(r"[-a-z]+-\d\d")

def makeSyntR(semR,checkSpecial=True):
    # checkSpecial is False when called from within specialConcept.checkSpecialConcept
    #              to avoid infinite loop
    traceSyntR("makeSyntR",semR)
    concept=semR.concept
    if concept==None: # l'instance réfère à un autre AMR
        return instance2SyntR(semR)
    if checkSpecial:
        sConcept=specialConcept.checkSpecialConcept(semR)
        if sConcept!=None:
            traceSyntR("special concept", concept)
            return sConcept
    # evaluate each role to build the environment
    dictInfo=getSyntR(concept)
    env=Env()
    opts=Options()
    roles=semR.get_roles()
    if isVerb(concept): #only for verbs
        # HACK for passive :  seem to be too aggressive.... so we keep it only for top-level AMR
        # generate a passive sentence if concept has an :ARG0 and the actual roles does not have :ARG0 but has :ARG1
        # %% do not passivate the special case of bear-02 because it is already passive
        if concept!="bear-02" and semR.parent==None and \
           ":ARG0" in verbs[concept].args and ":ARG0" not in semR.roles and ":ARG1" in semR.roles:
            opts.add("typ",{"pas":True})
    
    roleProcessing.processRoles(concept,roles,[],dictInfo,env,opts)
    
    ## patch the syntactic structures for frequent special cases
    if isVerb(concept):
        # HACK for changing nominative pronoun to accusative for :ARG1 when :ARG0 is also present
        if ":ARG1" in env and ":ARG0" in env and isinstance(env[":ARG1"],Pro) and env[":ARG1"].lemma=="I":
            env[":ARG1"].lemma="me"
    elif isAdjective(concept): # adjective with :ARG0 and :ARG1
        adj=dictInfo.lemma
        adjTerm=opts.apply(A(adj))
        if ":ARG0" in env and ":ARG1" in env:
            if isinstance(env[":ARG0"],Pro) and env[":ARG0"].lemma=="me":
                env[":ARG0"].lemma="I"
            if isinstance(env[":ARG1"],Pro) and env[":ARG1"].lemma=="I":
                env[":ARG0"].lemma="me"
            dictInfo=LexSem(adj,"S",[":ARG0",":ARG1"],lambda arg0,arg1:S(arg0,VP(V("be"),adjTerm,pp("for",arg1))))
        elif ":ARG1" in env and ":ARG2" in env:
            if isinstance(env[":ARG1"],Pro) and env[":ARG1"].lemma=="me":
                env[":ARG1"].lemma="I"
            if isinstance(env[":ARG2"],Pro) and env[":ARG2"].lemma=="I":
                env[":ARG2"].lemma="me"
            dictInfo=LexSem(adj,"S",[":ARG1",":ARG2"],lambda arg1,arg2:S(arg1,VP(V("be"),adjTerm,pp("for",arg2))))
        elif ":ARG1" in env:
            if isinstance(env[":ARG1"],Pro) and env[":ARG1"].lemma=="me":
                env[":ARG1"].lemma="I"
            dictInfo=LexSem(adj,"S",[":ARG1"],lambda arg1:S(arg1,VP(V("be"),adjTerm)))
        syntR=dictInfo.apply(env,Options()) # options have been applied to the adjective
        return syntR
    syntR=dictInfo.apply(env,opts)
    return syntR

if __name__ == '__main__':
    no=0
    for test in tests[0:]:
        semR=SemanticRep.fromString(test).elimInv()
        print("*%d*"%no)
        print(semR.prettyStr())
        syntR=makeSyntR(semR)
        print(syntR)
        print(syntR.show())
        print(jsRealB(syntR.show(-1)))
        print("--------")
        no+=1
    