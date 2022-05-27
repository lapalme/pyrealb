'''
Created on 4 mars 2021

@author: lapalme
'''

import re,json
# from jsRealBclass import N,A,Pro,D,Adv,V,C,P,DT,NO,Q,  NP,AP,AdvP,VP,CP,PP,S,SP,\
#                          Constituent, Terminal, Phrase, jsRealB
from pyrealb import *
## environment management
##    manage an environment as a list of pairs [(str,Constituent)] 
##    CAUTION: args can be repeated
##    - add to the environment
##       put(arg,value) : adds to the environment
##       putAll(pairs) : adds all pairs to the environment
##       push(value): add (":end",value) to the environment
##       unshift(value) : add(":start",value) to the environment
##       insertBefore(befKey,arg,value): add before befKey
##       insertAfter(aftKey,arg,value):  add after aftKey
##    - get and remove from the environment  
##       get(arg) : returns a list of all values associated with this arg
##    - info about the environment
##       arg in self : check if arg appears at least once in the environment
##       len(args) : return the number of args
##     
class Env:
    def __init__(self,pairs=None):
        self.pairs=pairs if pairs!=None else []
    
    def __str__(self):
        return "[%s]"%(", ".join(["(%s,%s)"%pair for pair in self.pairs]))
    
    def __contains__(self,kind):
        for rolei,_ in self.pairs:
            if re.match(kind,rolei):return True
        return False
    
    def __len__(self):
        return len(self.pairs)
    
    def __getitem__(self,arg):
        for key,val in self.pairs:
            if key==arg:return val
        return None
    
    def __setitem__(self,arg,val):
        for i in range(len(self.pairs)):
            if self.pairs[i][0]==arg:
                self.pairs[i][1]=val        
    
    def __delitem__(self,arg):
        for i in range(len(self.pairs)):
            if self.pairs[i][0]==arg:
                del self.pairs[i]
                return        
    
    def put(self,arg,value):
        if not isinstance(value,(N,A,Pro,D,Adv,V,C,P,DT,NO,Q,  NP,AP,AdvP,VP,CP,PP,S,SP)):
            print("Env.put:%s : %s is not a Constituent"%(arg,value))
        self.pairs.append((arg,value))
        return self
    
    def putAll(self,pairs):
        [self.put(key,value) for key,value in pairs]
        return self
    
    ## returns a list of elements associated with kind and remove them from the environment 
    def get(self,kind):
        res=[]
        i=0
        while i<len(self.pairs):
            argi,rolei=self.pairs[i]
            if re.fullmatch(kind,argi):
                res.append(rolei)
                self.pairs.pop(i)
            else:
                i+=1            
        return res
    
    ### most often we push at the end... or unshift at the start (like in JavaScript)
    def push(self,value):
        return self.put(':end',value)
    def unshift(self,value):
        return self.put(':start',value)
    
    def insertBefore(self,befKey,key,value):
        nb=len(self.pairs)
        i=0
        while i<nb and self.pairs[i][0]!=befKey:i+=1
        self.pairs.insert(i,(key,value))
    
    def insertAfter(self,aftKey,key,value):
        i=len(self.pairs)-1
        while i>=0 and self.pairs[i][0]!=aftKey:i-=1
        self.pairs.insert(i+1,(key,value))
        

class Options:
    def __init__(self,opts=None):
        self.opts=opts if opts!=None else []
    
    def __str__(self):
        return "".join(['.%s(%s)'%(opt,json.dumps(value)) for opt,value in self.opts])

    def __len__(self):
        return len(self.opts)
    
    def add(self,opt,value):
        if opt in ["typ","dOpt"]:
            try:
                idx=self.opts.index(opt)
                self.opts[idx].update(value)
            except ValueError :
                self.opts.append((opt,value))
        else:         
            self.opts.append((opt,value))
        return self
    
    def apply(self,syntR):
        for opt,value in self.opts:
            # adapted from https://stackoverflow.com/questions/3061/calling-a-function-of-a-module-by-using-its-name-a-string
            if opt=="tag":
                syntR.tag(*value)
            else:
                getattr(syntR, opt)(value)
        return syntR

nounInfo = lambda lemma:LexSem(lemma,"N",[":D",":A"],lambda d,a:NP(optD(d),a,N(lemma)))
adjInfo  = lambda lemma:LexSem(lemma,"A",[":ARG1"],lambda a1:A(lemma) if a1==None else AP(A(lemma),a1))
pp       = lambda prep, arg: PP(P(prep),arg) if arg!=None else None
optD     = lambda det : det if det!=None else D("the")

class LexSem:
    def __init__(self,lemma,pos,args,lambda_):
        self.lemma=lemma
        self.pos=pos
        self.args=args
        self.lambda_=lambda_
        
    def __str__(self):
        return "LexSem(%s,%s)"%(self.lemma,self.pos)
    
    def __getitem__(self,attr):
        return None if not hasattr(self,"attrs") or attr not in self.attrs else self.attrs[attr]
    
    def addAttributes(self,attrs):
        self.attrs=attrs if not hasattr(self,"attrs") else self.attrs.update(attrs)
        return self
            
    def apply(self,env=None,opts=None):
        if env==None:env=Env()
        if opts==None:opts=Options()
        ## process args from dictInfo building the list of arguments or None
        argV=[env.get(arg) if arg in env else None for arg in self.args]
        syntR = self.lambda_(*argV)
        if all([arg == None for arg in argV]) and len(env)==0:
            return opts.apply(syntR)
        if isinstance(syntR,Terminal):
            if isinstance(syntR,A):
                if ":ARG1" in env:
                    syntR=S(env.get(":ARG1"),VP(V("be"),syntR))
                else:    
                    syntR=AP(syntR)
            elif isinstance(syntR,(Pro,Q,NO)):syntR=SP(syntR)
            elif isinstance(syntR,Adv):syntR=AdvP(syntR)
            elif isinstance(syntR,P):  syntR=PP(syntR)
            else:
                print("** apply: strange syntR:%s:%s"%(type(syntR),syntR))
                syntR=SP(syntR)
        ## add unprocessed args
        if len(env)>0:
            syntR.add(env.get(":start"),0)
            syntR.add(env.get(".*")) 
        return opts.apply(syntR)
   
##   for unit testing
if __name__ == '__main__':
    def showSyntR(syntR):
        print(syntR)
        print(syntR.toSource(0))
        # print(jsRealB(syntR.show(-1)))
        print(syntR.realize())
        print("----")
    ## a few lexicon entries
    verbs={}
    nouns={}
    adjectives={}
    conjunctions={}

    def op16(conj):
        return LexSem(conj,"C",[":op1",":op2",":op3",":op4",":op5",":op6"],
                      lambda op1,op2,op3,op4,op5,op6:CP(C(conj),op1,op2,op3,op4,op5,op6))  
    conjunctions["or"]=op16("or")
    conjunctions["and"]=op16("and")
    
    verbs['give-01']=LexSem("V","give",[":ARG0",":ARG1",":ARG2"],
                            lambda arg0,arg1,arg2:S(arg0,VP(V("give"),arg1,pp("to",arg2))))    
    nouns['envelope'] = LexSem("envelope","N",[":D",":A"],lambda d,a:NP(optD(d),a,N("envelope")))
    nouns['boy']      = LexSem("boy","N",[":D",":A"],lambda d,a:NP(optD(d),a,N("boy")))
    nouns['girl']     = LexSem("girl","N",[":D",":A"],lambda d,a:NP(optD(d),a,N("girl")))
    
    adjectives["little"]=LexSem("little","A",[],lambda :A("little"))
    adjectives["nice"]  =LexSem("nice","A",[],lambda :A("nice"))
    
    
    ## start of tests
    boyEnv=Env([(':D',D("a"))])
    little=adjectives["little"].apply()
    boyEnv.putAll([(":A",little),(":A",A("nice"))])
    boy=nouns["boy"]
    print(boy)
    boySyntR=boy.apply(boyEnv,Options([("n","p")]))
    showSyntR(boySyntR) # little nice boys
    
    envelope=nouns["envelope"]
    envelopeSyntR=envelope.apply()
    showSyntR(envelopeSyntR) # the envelope
     
    girl=nouns["girl"]
    girlSyntR=girl.apply(Env([(":D",D("this"))]))
    showSyntR(girlSyntR) # this girl
          
    give=verbs["give-01"]
    giveSyntR=give.apply(Env([(":ARG0",boySyntR),(":ARG1",envelopeSyntR),(":ARG2",girlSyntR)]),
                         Options([("typ",{"neg":True})]))
    showSyntR(giveSyntR) # Little nice boys do not give the envelope to this girl.
 
    boySyntR=nouns["boy"].apply(boyEnv)
    envelopeSyntR=nouns["envelope"].apply()
    bookSyntR=nounInfo("book").apply(Env([(":D",D("a"))]))
    penSyntR=nounInfo("pen").apply()
    envelopeBookSyntR=conjunctions["or"].apply(Env([(":op1",envelopeSyntR),
                                                    (":op2",bookSyntR),
                                                    (":op6",penSyntR)]))
    showSyntR(envelopeBookSyntR) #the envelope, a book or the pen
    
    giveSyntR=give.apply(Env([(":ARG0",boySyntR),
                              (":ARG1",envelopeBookSyntR),
                              (":ARG2",girlSyntR),
                              (":start",Q("start")),
                              (":test",Q("test")),
                              (":end",Q("end")),
                              ]))
    showSyntR(giveSyntR) # Start the boy gives the envelope, a book or the pen to this girl test end.
    
    giveSyntR=give.apply(Env([(":ARG1",envelopeBookSyntR),
                              (":ARG2",girlSyntR)]))
    showSyntR(giveSyntR) # Gives the envelope, a book or the pen to this girl.
