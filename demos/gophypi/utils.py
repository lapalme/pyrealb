"""
Created on Jan 20, 2021

@author: lapalme
"""
import re,json
# from jsRealBclass import N,A,Pro,D,Adv,V,C,P,DT,NO,Q,  NP,AP,AdvP,VP,CP,PP,S,SP, \
#                         Constituent,Terminal,Phrase
from pyrealb import *
import amrDico

## utilities functions
# taken from: https://stackoverflow.com/questions/354038/how-do-i-check-if-a-string-is-a-number-float
def is_number(s):
    s=unquote(s)
    try:
        float(s)
        return True
    except ValueError:
        return False    

def unquote(s):
    m=re.match(r'"(.*)"$',s)
    if m:return m.group(1)
    m=re.match(r"'(.*)'$",s)
    if m:return m.group(1)
    return s

def generateConceptWord(concept):
    cs=concept.split("-")
    if re.match(r"\d+|yy",cs[-1]):
        del cs[-1]
    if re.match("entity|quantity",cs[-1]):
        del cs[-1]
    return " ".join(cs)
    
def errorSyntR(message):
    print("@@@@ %s"%message)

def ensurePhrase(syntR):
    if isinstance(syntR,Phrase):return syntR
    if isinstance(syntR,Terminal):
        if syntR.isA("N"):return NP(syntR)
        if syntR.isA("A"):return AP(syntR)
        if syntR.isA("V"):return VP(syntR)
        if syntR.isA("Adv"):return Adv(syntR)
        return SP(syntR)
    print("ensurePhrase: type inattendu:%s"%type(syntR))

## check polarity which sometimes appears as "-" or -
##    if it has polarity it removes it from roles
def hasNegPolarity(roles):
    if ":polarity" in roles:
        pol=unquote(roles[":polarity"].get_instance())
        del roles[":polarity"]
        return pol=="-"
    return False   

def predicate(subject,attribute):
    if attribute==None:
        return S(subject,VP(V("be")))
    if subject.isA("S"):
        syntR=subject.add(attribute)
    else:
        syntR=S(subject,VP(V("be"),attribute))
    if isinstance(attribute, Phrase) and "typ" in attribute.props:
        if "neg" in attribute.props["typ"] and attribute.props["typ"]["neg"] != False:
            if "typ" not in syntR.props:syntR.props["typ"]={}
            syntR.props["typ"]["neg"]=attribute.props["typ"]["neg"]
    return syntR

def relative(concept,syntR):
    pronoun=Pro("who") if concept in amrDico.gender else D("that")
    if syntR.isA("S"):
        return syntR.add(pronoun,0)
    return predicate(pronoun,syntR)

def isArgOp(role):
    return re.fullmatch(r":(ARG|op)\d",role)

### Trace control
traceSyntRflag=False

def setTraceSyntR(val):
    global traceSyntRflag
    traceSyntRflag=val

def traceSyntR(mess,semR):
    global traceSyntRflag
    if not traceSyntRflag:return
    print("++%s: %s"%(mess,semR if semR.isA("str") else semR.shortStr()))


def adverbFromAdjective(adjective):
    m=re.match("([a-z]+)-\d+$",adjective) # remove possible trailing numbers
    if m: adjective=m.group(1)
    ## rules from https://www.ef.com/wwen/english-resources/english-grammar/forming-adverbs-adjectives/
    if adjective in ["early","fast","hard","high","late","near","straight","wrong"]: return adjective
    if adjective=="good" or adjective=="well":return "well";
    if adjective[-1]=="y": return adjective[:-1]+"ily"
    if adjective[-2:]=="le":return adjective[:-1]+"y"
    if adjective=="public":return "publicly"
    if adjective[-2:]=="ic":return adjective+"ally"
    if adjective[-4:]=="full":return adjective[:-4]+"fully";
    return adjective+"ly"   

if __name__ == '__main__':
    pass