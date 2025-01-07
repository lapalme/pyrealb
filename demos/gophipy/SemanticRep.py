'''
Created on 5 sept. 2017
Updated February 1st 2021

@author: Guy Lapalme <lapalme@iro.umontreal.ca> / Université de Montréal

Parse an AMR input stream to produce a list of the corresponding SemanticRep instances
'''

import re,os,textwrap
from collections import Counter

def isInvRole(role):
    return role.endswith("-of") and \
           role not in [":consist-of",":domain-of",":part-of",":polarity-of",
                        ":subevent-of",":subset-of","prep-on-behalf-of",":prep-out-of"]

# list of pairs ("argname", value)
class RoleList:
    def __init__(self):
        self.__roles=[]
        
    def __str__(self):
        if len(self)==0:return "[*]"
        return "[* "+", ".join([("%s:%s"%(repr(k),v)) for (k,v) in self.__roles])+" *]"
    def __repr__(self): # HACK so that tuples use also this notation...
        return self.__str__()
    def __getitem__(self,key): # indexing
        if isinstance(key,int):
            return self.__roles[key]
        for (k,v) in self.__roles:
            if k==key:return v
        return None
    def __setitem__(self,key,value): # assignment
        if isinstance(key,int):
            self.__roles[key]=value
            return
        for (k,_) in self.__roles:
            if k==key:
                self.__roles[key]=value
                return
        print("role: % cannot be changed to %s"%(key,value))

    def __delitem__(self,key):
        for i in range(len(self.__roles)):
            if self.__roles[i][0]==key:
                del self.__roles[i]
                return

    def __contains__(self,key):  # in operator
        for (k,_v) in self.__roles:
            if k==key:return True
        return False
      
    def __len__(self):
        return len(self.__roles)

    def items(self):
        return iter(self.__roles)
    def keys(self):
        return [k for (k,_) in self.__roles]
    def areEmpty(self):
        return len(self.__roles)==0
    
    
    def addRole(self,key,val):
        self.__roles.append((key,val))
    def delRole(self,key):
        for i in range(len(self.__roles)):
            if self.__roles[i][0]==key:
                del self.__roles[i]
                return 
        print('delRole: %s not found in %s'%(key,self.keys()))
        return        
    def matchRole(self,pat):
        for (k,_v) in self.__roles:
            if re.match(pat,k):return True
        return False


                                   
## flags for debugging
traceParse=False

################################################################################################
#### tokenizer for the SemanticRep input
## tokenizer adapted from https://docs.python.org/3.4/library/re.html#writing-a-tokenizer
currentLine=""

def tokenizeAMR(inputSt):
    global currentLine
    token_specification = [
        # escaped quoted string regex taken from http://stackoverflow.com/questions/16130404/regex-string-and-escaped-quote
        ("STR",           r'"(?:\\.|[^"\\])*?"'+"|"+ r"'(?:\\.|[^'\\])*?'"),# double or single quoted string
        ("NUMBER",        r'-?\d+((\.|:)\d+)?'),         # integer or decimal number or hour:minutes
        ("IDENT",         r'[A-Za-z_][-A-Za-z_0-9]*'),   # Identifiers
        ("ROLE",          r':[A-Za-z_][-A-Za-z_0-9]*'),  # role identifier
        ("OPEN_PAREN",    r'\('),
        ("CLOSE_PAREN",   r'\)'),
        ("SLASH",         r'/'),
        ("BACKSLASH",     r'\\'),
        ("MINUS",         r'-'),
        ("PLUS",          r'\+'),
        ("EOL",           r'\n'),
        ("SKIP",          r'[ \t\r]+|;.*|#.*'),  # Skip over spaces and tabs and comments 
        ("UNDEF",         r'.')                # Any other character
    ]
    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
    line_num = 1
    line_start = 0
    line_end=inputSt.find('\n',line_start)
    currentLine=inputSt[line_start:line_end] if line_end>=0 else inputSt[line_start:]
    for mo in re.finditer(tok_regex, inputSt):
        kind = mo.lastgroup
        value = mo.group(kind)
        # print "kind:"+kind+"; value:"+value
        if kind == "EOL":
            line_num += 1
            line_start = mo.end()
            line_end=inputSt.find('\n',line_start)
            currentLine=inputSt[line_start:line_end] if line_end>=0 else inputSt[line_start:]
        elif kind == "SKIP":
            pass
        elif kind == "UNDEF":
            yield Token("UNDEF",value,line_num,mo.start()-line_start)
        else:
            column = mo.start() - line_start
            yield Token(kind, value, line_num, column)
    yield Token("EOF"," ",line_num,0)

class Token:
    """packaging for the output of token"""
    def __init__(self, kind,value,line_num,column):
        self.kind=kind
        self.value=value
        self.line_num=line_num
        self.column=column
        # print self
    
    def __repr__(self):
        return "Token(%s:%s:%d:%d)"%(self.kind,self.value,self.line_num,self.column)

################################################################################################

### EBNF Grammar of the SemanticRep input
#   according to Definition 5 of  
#    Johan Bos,Expressive Power of Abstract Meaning
#    Representation, Computational Linguistics, 42:3, pp 527-535, 2016.
#        A ::= c | x | (x/P) | (x/P :RiAi) | (x/P :RiAi :polarity–)  
#                    | (x\P) | (x\P :RiAi) | (x\P :RiAi :polarity–)
token=None
tokenizer=None

def errorAMR(module,message,recoveryTokens):
    global currentLine,token,tokenizer,traceParse
    if traceParse:print(">>>errorAMR:"+module)
    # print("line %3d: %s"%(token.line_num,currentLine))
    # print(((token.column+10)*" ")+"@:"+message)
    print("line %d,%d : %s"%(token.line_num,token.column,message))
    if recoveryTokens!=None:
        endTokens=set(["EOF"]+recoveryTokens)
        while token.kind not in endTokens:
            token=next(tokenizer)

class SemanticRep:
    def __init__(self,instance,concept,roles,parent):
        self.instance=instance
        self.concept=concept
        self.roles=roles
        self.parent=parent
        
    def __str__(self):
#         inst = "^%s"%self.instance.instance if type(self.instance) is SemanticRep else self.instance
#         parent=(",@%s"%self.parent.instance) if self.parent!=None else ""
#         return "SemanticRep(%s,%s,%s%s)"%(inst,self.concept,self.roles,parent)
        return self.prettyStr()
        
    def get_instance(self):
        if self.instanceIsRef():
            return self.instance.instance
        return self.instance

    def instanceIsRef(self):
        return type(self.instance) is SemanticRep
    
    def get_concept(self):
        if self.instanceIsRef():
            return self.instance.concept
        return self.concept

    def get_roles(self):
        return self.roles

    def get_parent(self):
        return self.parent
    
#     def findRolePath(self,rolePath):
#         # get the AMR at the end of a path of roles
#         if isinstance(rolePath,str):
#             return self.findRolePath([rolePath])
#         if rolePath[0] in self.roles:
#             amr=self.roles[rolePath[0]]
#             if len(rolePath)>1:
#                 return amr.findRolePath(rolePath[1:])
#             return amr
#         else:
#             return None
            
    # find the role of an AMR within its parent
    def get_my_role(self):
        if self.parent==None:return None
        for (k,v) in self.parent.get_roles().items():
            if v==self:
                return k        
        return None
    # find the parent concept
    def get_parent_concept(self):
        if self.parent==None:return None
        return self.parent.concept
    
#     # modifier l'AMR en fonction d'une nominalisation pour un role
#     #  attention: on suppose que les tests d'application ont été faits
#     def nominalizeRole(self,role,newConcept):
# #         print("nominalizeRole(%s,%s)"%(role,newConcept))
#         self.instance="_"+newConcept[0]
#         self.concept=newConcept
#         if role!=None:
#             subRoles=self.roles[role].get_roles()
#             ## add subRoles to concept (not sure this is right!!!)
#             for sr in subRoles.keys():
#                 self.roles.addRole(sr,subRoles[sr])
#             self.roles.delRole(role)
# #         print("nominalize:=>\n"+self.prettyStr())
#         return self
    
    ## indented string to display the structure of the AMR      
    def prettyStr(self,indent=0):
        inst="^%s"%self.instance.instance if type(self.instance) is SemanticRep else self.instance
        parent="" if self.parent==None else " @%s"%(self.parent.get_instance())            
        if self.concept==None and self.roles.areEmpty():
            return "(%s # []%s)"%(inst,parent)
        else:
            cs=[]
            concept=self.concept if self.concept!=None else "#"
            indent+=len(inst)+1+len(concept)+2
            for (role,amr) in self.roles.items():
                if amr!=None:
                    cs.append(role+" "+amr.prettyStr(indent+len(role)+2))
            roles=(",\n"+(" "*(indent+1))).join(cs)
            return "(%s %s [%s]%s)"%(inst,concept,roles,parent)

    ## string that only shows the global structure without the role content
    ## useful for traces    
    def shortStr(self):
        inst="^%s"%self.instance.instance if type(self.instance) is SemanticRep else self.instance
        parent="" if self.parent==None else " @%s"%(self.parent.get_instance())            
        if self.concept==None and self.roles.areEmpty():
            return "(%s # []%s)"%(inst,parent)
        keys=""
        if not self.roles.areEmpty(): # display only keys
            keys="["+", ".join(k+" .." for k in self.roles.keys())+"]"
        return "(%s %s %s%s)"%(inst,self.concept,keys,parent)

    ##  baseline generator to build a string using
    #     :ARG0 concept [other :ARGS] 
    #     :polarity - add "not"
    #     inverse roles: add "that"
    #       remove digits from concepts
    
    def baselineGen(self):
        if self.concept==None and self.roles.areEmpty():
            inst=self.instance
            return "" if type(inst) is SemanticRep else inst
        if self.roles.areEmpty():
            return re.sub(r'(-\d+)?$',r'',self.concept) # remove number at end of concept
        res=[]
        isVerb=re.match(r'([a-z]+)-\d+',self.concept)
        if isVerb: # first generate ARG0 and "not" if it is a verb (ending by digits)
            if  ":*:ARG0" in self.roles:
                    res.extend(["that",self.roles[":*:ARG0"].baselineGen()])
            elif  ":ARG0" in self.roles:
                res.append(self.roles[":ARG0"].baselineGen())
            if  ":polarity" in self.roles:
                if self.roles[":polarity"].instance=="-":res.append("not")
        res.append(re.sub(r'(-\d+)?$',r'',self.concept))
        for (role,amr) in self.roles.items():
            if not isVerb or role not in [":ARG0",":polarity",":*:ARG0"]:
                if role.startswith(":*"):res.append("that")
                res.append(amr.baselineGen())
        return " ".join([r for r in res if r!=""])
    
    ## remove inverse role by adding a "special" role that will be rendered as as relative
    ## for example
    # (g girl [:ARG1-of (s see-01 [:ARG0 (b boy [] @s)] @g)])
    #  is changed to
    # (g girl [:*:ARG1 (s see-01 [:ARG0 (b boy [] @s),
    #                             :ARG1 ^g @s] @g)])
    # and
    # (p4 place [:location-of (e2 None [] @x)])
    #  is changed to
    # (p4 place [:*:location  (e2 None [:location ^p4 [] @p4] @x])]) 
    def elimInv(self):       
        nbRoles=len(self.roles)
        for i in range(0,nbRoles):
            (role,amr)=self.roles[i]
            if isInvRole(role):
                amrNoInv=amr.elimInv()
                amrNoInv.roles.addRole(role[0:-3],
                                   SemanticRep(self.instance,None,RoleList(),amr)\
                                      .__linkInstance(self.instance))
                self.roles[i]=(":*"+role[0:-3],amrNoInv)
            else:
                amr.elimInv()
        return self        
    
    def hasInverseRole(self):
        for (role,amr) in self.get_roles():
            if isInvRole(role) or amr.hasInverseRole():return True
        return False
    
    # instance dict to manage links between AMRs
    #   its key is the name of the instance
    #   its value is either 
    #        - AMR the AMR in which it is defined
    #        - AMR list which reference it (backward links)
    instanceDict={}
    
    def __showInstanceDict(self):
        if traceParse: 
            for (key,val) in self.instanceDict.items():
                if type(val) is list:
                    print("%s::[%s]"%(key,",".join([str(v) for v in val])))
                else:
                    print("%s::%s"%(key,val))
            print("---")
        return self
    
    def __addInstance(self,instance):
        if traceParse:print("__addInstance:"+instance)
        if instance in self.instanceDict:
            val=self.instanceDict[instance]
            if type(val) is SemanticRep:
                print("__addInstance: double definition:"+instance)
            else:
                for amr in val:
                    amr.instance=self
        self.instanceDict[instance]=self
        return self.__showInstanceDict()
    
    def __linkInstance(self,instance):
        if traceParse:print("__linkInstance:"+instance)
        if instance in self.instanceDict:
            val=self.instanceDict[instance]
            if  type(val) is SemanticRep:
                self.instance=val
            elif type(val) is list:
                val.append(self)
            else:
                print("__linkInstance:error"+instance+":"+val)
        else:
            self.instanceDict[instance]=[self]
        return self.__showInstanceDict()
        
            
    ## parse a SemanticRep
    @classmethod
    def parse(cls,parent):
        global token, tokenizer,traceParse
        amr=None
        if traceParse:print(">>>parse:"+str(token)+"^"+str(parent))
        if token.kind == "OPEN_PAREN":
            token=next(tokenizer)
            if token.kind == "IDENT":
                instance=token.value
                token=next(tokenizer)
                if token.kind in ["SLASH","BACKSLASH"]:
                    token=next(tokenizer);
                    if token.kind == "IDENT":
                        concept=token.value
                        token=next(tokenizer)
                        amr=SemanticRep(instance,concept,None,parent)
                        amr.__addInstance(instance)
                        amr.roles=cls.parseRoles(amr)
                    else:
                        errorAMR("parse","Identifier expected",["IDENT"])
            else:
                errorAMR("parse","Identifier expected",["IDENT"])
            if token.kind=="CLOSE_PAREN":
                token=next(tokenizer)
            else:
                errorAMR("parse","Close parenthesis expected",["CLOSE_PAREN"])
        elif token.kind in ["STR","NUMBER","IDENT","MINUS","PLUS"]:
            instance=token.value
            amr=SemanticRep(instance,None,RoleList(),parent)
            if token.kind=="IDENT":
                amr.__linkInstance(instance)
            token=next(tokenizer) 
        else: 
            errorAMR("parse","Open parenthesis expected",["OPEN_PAREN"])
        return amr
    
    @classmethod
    def parseRoles(cls,parent):
        global token,tokenizer,lines, traceParse
        if traceParse:print(">>>parseRoles:"+str(token)+"^"+str(parent))
        roles = RoleList()
        while token.kind=="ROLE":
            roleId=token.value
            token=next(tokenizer)
            roleValue=cls.parse(parent)
            roles.addRole(roleId,roleValue)
        return roles
    
    wrapper=textwrap.TextWrapper(width=90,subsequent_indent="\t",break_on_hyphens=False)
    @classmethod
    def showCountVals(cls,countVals):
        (count,vals)=countVals
        cls.wrapper.initial_indent="%d\t"%count
        print(cls.wrapper.fill(", ".join(sorted(vals))))
        return
    
    @classmethod
    def showCounts(cls,counters):
        sortedCounters=sorted(list(counters.items()), key=lambda v:v[1],reverse=True)
        # group counters by count value to shorten output
        groups={}
        for (val,count) in sortedCounters:
            if count in groups:
                groups[count].append(val)
            else:
                groups[count]=[val]
        sortedGroups=sorted(groups.items(),reverse=True)
        for group in sortedGroups:
            cls.showCountVals(group)
    
    @classmethod
    def saveCounts(cls,counters,file):
        sortedCounters=sorted(list(counters.items()))
        for (val,count) in sortedCounters:
            file.write("%s\t%d\n"%(val,count))
        
    conceptCounts=Counter()
    roleCounts=Counter()
 
    def updateCounts(self):
        if self.concept!=None:
            self.conceptCounts[self.concept]+=1
        if self.roles!=None:
            for (role,amr) in self.roles.items():
                self.roleCounts[role]+=1
                amr.updateCounts() # recursive statistics
    
    @classmethod
    def fromString(cls,inString):
        global token,tokenizer,lines
        tokenizer=tokenizeAMR(inString)
        token=next(tokenizer)
        try:
            cls.instanceDict={}
            parsed=cls.parse(None)
            return parsed
        except StopIteration:
            errorAMR("parseAMRs","unexpected end of file",None)    
    
    
    
    #  parse many AMRs from an IOStream and return a list of AMRs while computing statistics
    #  assuming that an AMR ends with an empty line
    @classmethod
    def fromStream(cls,inputSt):
        global token,tokenizer,lines
        snt="*snt*"
        lines=""
        parsedS=[]
        for line in inputSt:
            if line.startswith("#"):
                if re.match(r"# ::snt .*",line):
                    snt=line.rstrip()
            elif len(line.strip())==0 and len(lines)>0:
                parsed=cls.fromString(lines)
                parsed.updateCounts()
                parsedS.append((parsed,snt))
                snt="*snt*"
                lines=""
            else:
                lines+=line
        if len(lines)>0:
            parsed=cls.fromString(lines)
            parsed.updateCounts()
            parsedS.append((parsed,snt))
        return parsedS

def walkAMRdirs(path,operation,nbAMRs):
    # parse a file to count roles and concepts
    if os.path.isdir(path):
        for dirName,subdirNames,files in os.walk(path):
            for subdirName in subdirNames:
                if subdirName in ["training","dev"]:
                    nbAMRs=walkAMRdirs(os.path.join(dirName,subdirName),operation,nbAMRs)
            for fileName in files:
                if re.match(r'amr-.*\.txt',fileName):
                    nbAMRs=walkAMRdirs(os.path.join(dirName,fileName),operation,nbAMRs)
            return nbAMRs
    else:
        return operation(path,nbAMRs)

def statistics(path,nbAMRs):    
    stream=open(path,'r',encoding='utf-8')
    amrs=SemanticRep.fromStream(stream)
    print("%8d :: %s"%(len(amrs),path))
    return nbAMRs+len(amrs)

def findMatchingConcept(amr,conceptRE):
    concept=amr.get_concept()
    if concept!=None :
        if re.match(conceptRE,concept):
            return amr.prettyStr()
        for (_role,amr) in amr.get_roles().items():
            c=findMatchingConcept(amr, conceptRE)
            if c:return c
    return None

def showAMRconcepts(path,conceptRE,nbAMRs):
    print(path)
    stream=open(path,'r',encoding='utf-8')
    amrs=SemanticRep.fromStream(stream)
    nbVides=0
    for (amr,snt) in amrs:
#         print(amr.prettyStr())
        mc=findMatchingConcept(amr, conceptRE)
        if mc:
            if re.match(r'\([a-z][0-9]? '+conceptRE+r' \[\]( @[a-z][0-9]?)?\)',mc):
                nbVides+=1
            else:
                print(snt)
                print(mc)
                print("---")
            nbAMRs+=1
    if nbVides>0:
        print("nbVides:"+str(nbVides))
    print("============")
    return nbAMRs


def checkMultiSentence(path,totals):
    (totalNb,totalNbUnsorted,totalNbAmrs)=totals
    stream=open(path,'r',encoding='utf-8')
    amrs=SemanticRep.fromStream(stream)
    nb=0
    nbUnsorted=0
    nbAmrs=len(amrs)
    for (amr,_) in amrs:
        if (amr.concept=="multi-sentence"):
            snts=[(key[0:4],int(key[4:])) for key in amr.roles.keys() if re.match(":snt",key)]
            nb+=1
            if sorted(snts,key=lambda x:x[1])!=snts:nbUnsorted+=1
    print("%5d : %5d : %5d : %s"%(nb,nbUnsorted,nbAmrs,path[len(amrDir):]))
    return (totalNb+nb,totalNbUnsorted+nbUnsorted,totalNbAmrs+nbAmrs)
    
# unit testing
test0='''
(g/girl :ARG1-of (s/see-01 :ARG0 (b/boy)))
'''
testPaper='''
(d / desire-01
    :ARG0 (b/boy)
    :ARG1 (g/girl
           :ARG0-of (l/like-01
                       :polarity - 
                       :ARG1 b)))
'''
test1='''(e/moan-01 :ARG0 (x/child))'''
test2='''(e/give-01
             :ARG0 (x/person :named "Ms Ribble")
             :ARG2 (y/child)
             :ARG1 (z/envelope))'''
test3='''
## commentaire
(s / say-01
     :ARG0 (g / organization
          :name (n / name
                  :op1 "UN"))
     :ARG1 (f / flee-05
          :ARG0 (p / person
                  :quant (a / about
                           :op1 14000))
          :ARG1 (h / home
                  :poss p)
          :time (w / weekend)
          :time (a2 / after
                  :op1 (w2 / warn-01
                         :ARG1 (t / tsunami)
                         :location (l / local))))
      :medium (s2 / site
            :poss g
            :mod (w3 / web)))
'''
test4='''
(w / want-01
             :ARG0 (b / boy
                    :named "Guy")
             :polarity -
             :ARG1 (b2 / believe-01
                   :ARG0 (g / girl)
                   :ARG1 b))
'''
test4b='''
(w / want-01
             :ARG1 (b2 / believe-01
                     :ARG0 (g / girl)
                     :ARG3 b
                     :ARG1 b)
             :ARG0 (b / boy
                    :named "Guy")
             :polarity -
                   )
'''
test5='''
(b / buy-01
      :ARG0 (h / he)
      :ARG1 (f / flower)
      :ARG4 (p / person
            :ARG0-of (h2 / have-rel-role-91
                  :ARG1 h
                  :ARG2 (m / mother))))
'''
test6='''
(s / say-01
      :ARG0 i
      :ARG1 (n / need-01
            :ARG0 (i / i)
            :ARG1 (m / money
                  :mod (m2 / more)))
      :ARG2 (p / person
            :ARG0-of (h / have-rel-role-91
                  :ARG1 i
                  :ARG2 (f / father))))
'''
test7 ='''
(p / permit-01
     :polarity -
     :ARG1 (g / go-02 
          :ARG0 (b / boy)))
'''
tests=[test0,testPaper,test1,test2,test3,test4,test5,test6,test7]

if __name__ == '__main__':
#     for test in tests:
#         amr=SemanticRep.fromString(test)
#         if amr!=None:
#             print(amr.prettyStr())
#             if amr.hasInverseRole():
#                 amr.elimInv()
#                 print(amr.prettyStr())
# #             print(amr.baselineGen())
#             print()

#     amrDir="/Users/lapalme/Dropbox/AMR/"
# #     nbAMRs=statistics(amrDir+"amr-ISI/amr-dict-examples.txt",0)
# #     nbAMRs=showAMRconcepts(amrDir+"amr-ISI/amr-dict-examples.txt", 'amr-unknown', 0)
# #     nbAMRs=walkAMRdirs(amrDir+"amr-ISI",statistics,0)
#     # conceptCountsFile=open(amrDir+"amr-ISI/"+"conceptCounts.txt","w")
# #     nbAMRs=walkAMRdirs(amrDir+"abstract_meaning_representation_amr_2.0/data/amrs/split",statistics,nbAMRs)
# #     nbAMRs=walkAMRdirs(amrDir+"amr-ISI",lambda path,nbAMRs:showAMRconcepts(path, r'amr-unknown', nbAMRs),0)
# #     nbAMRs=walkAMRdirs(amrDir+"abstract_meaning_representation_amr_2.0/data/amrs/split",statistics,nbAMRs)
#     nbAMRs=walkAMRdirs(amrDir+"amr_annotation_3.0/data/amrs/unsplit",statistics,0);
#     conceptCountsFile=open(amrDir+"amr_annotation_3.0/"+"conceptCounts.txt","w")
#     print("Total number of AMRs:%d"%nbAMRs)
#     print("CONCEPTS : %d"%sum(SemanticRep.conceptCounts.values()))
#     SemanticRep.showCounts(SemanticRep.conceptCounts)
#     print("ROLES : %d"%sum(SemanticRep.roleCounts.values()))
#     SemanticRep.showCounts(SemanticRep.roleCounts)
#     SemanticRep.saveCounts(SemanticRep.conceptCounts, conceptCountsFile)
    amrDir="/Users/lapalme/Dropbox/AMR/"
    # nbAMRs=walkAMRdirs(amrDir+,statistics,0)
    (nbUnsorted,nb,nbAmrs)=walkAMRdirs(amrDir+"amr_annotation_3.0/data/amrs/unsplit",checkMultiSentence,(0,0,0))
    print("%5d : %5d : %5d : %s"%(nbUnsorted,nb,nbAmrs,"all"))
    ### results
 #   34 :     7 :   204 : amr_annotation_3.0/data/amrs/unsplit/amr-release-3.0-amrs-mt09sdl.txt
 #    8 :     0 :   926 : amr_annotation_3.0/data/amrs/unsplit/amr-release-3.0-amrs-xinhua.txt
 #  611 :    55 :  7818 : amr_annotation_3.0/data/amrs/unsplit/amr-release-3.0-amrs-dfa.txt
 #  652 :    28 : 32915 : amr_annotation_3.0/data/amrs/unsplit/amr-release-3.0-amrs-dfb.txt
 #   87 :     8 :  5322 : amr_annotation_3.0/data/amrs/unsplit/amr-release-3.0-amrs-lorelei.txt
 #  369 :    39 :  1327 : amr_annotation_3.0/data/amrs/unsplit/amr-release-3.0-amrs-bolt.txt
 #    2 :     0 :   192 : amr_annotation_3.0/data/amrs/unsplit/amr-release-3.0-amrs-wiki.txt
 #    2 :     0 :  8252 : amr_annotation_3.0/data/amrs/unsplit/amr-release-3.0-amrs-proxy.txt
 #    4 :     0 :   970 : amr_annotation_3.0/data/amrs/unsplit/amr-release-3.0-amrs-guidelines.txt
 #    2 :     0 :   214 : amr_annotation_3.0/data/amrs/unsplit/amr-release-3.0-amrs-cctv.txt
 #    3 :     1 :    49 : amr_annotation_3.0/data/amrs/unsplit/amr-release-3.0-amrs-fables.txt
 #   13 :     0 :   866 : amr_annotation_3.0/data/amrs/unsplit/amr-release-3.0-amrs-wb.txt
 #    0 :     0 :   200 : amr_annotation_3.0/data/amrs/unsplit/amr-release-3.0-amrs-consensus.txt
 # 1787 :   138 : 59255 : all
#     amr=SemanticRep.fromString('''
# (a / and
#      :op1 (r / remain-01
#            :ARG1 (c / country :wiki "Bosnia_and_Herzegovina"
#                   :name (n / name :op1 "Bosnia"))
#            :ARG3 (d / divide-02
#                   :ARG1 c
#                   :topic (e / ethnic)))
#      :op2 (v / violence
#            :time (m / match
#                   :mod (f2 / football)
#                   :ARG1-of (m2 / major-02))
#            :location (h / here)
#            :frequency (o / occasional))
#      :time (f / follow-01
#             :ARG2 (w / war
#                    :time (d2 / date-interval
#                           :op1 (d3 / date-entity :year 1992)
#                           :op2 (d4 / date-entity :year 1995)))))
#     ''')
#     print(amr.prettyStr())
#     print(amr.baselineGen())