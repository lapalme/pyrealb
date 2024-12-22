import copy
import re,datetime,sys

from .Lexicon import getLexicon, getRules, load

quoteOOV=False # TODO: make this settable globally

optionListMethods = ('a', 'b', 'ba', 'en')

deprels = ["root","subj","det","mod","comp","coord"] # list of implemented dependency relations

class Constituent:
    def __init__(self,constType):
        self.constType=constType
        # initialize other params
        self.parentConst=None
        self.props = {}
        self.realization=None 
        self.optSource=""     # string corresponding to the calls to the options
    
    # TODO: make this settable globally or from the command line
    # hack taken from https://intellij-support.jetbrains.com/hc/en-us/community/posts/205819799/comments/206004059
    debug = sys.gettrace() is not None or "-d" in sys.argv # used in Constituent.__str__()

    exceptionOnWarning = False

    #  unary plus to print the realization of a Constituent
    #  useful within a real-eval-print loop
    def __pos__(self):
        print(self.realize())

    def error(self,mess):
        raise Exception ("Internal error: this should never have happened,sorry!\n"+self.me()+"::"+mess)
    
    def isA(self,*types):
        if len(types)==1:
            if isinstance(types[0],str):
                return self.constType==types[0]
            return self.constType in types[0]
        return self.constType in types

    # get/set the value of a property by first checking the special shared properties
    def getProp(self,propName):
        if propName in self.props:
            return self.props[propName] 
        if propName in ["pe","n","g"]:
            if not hasattr(self, "peng") or self.peng is None: return None
            return self.peng[propName] if propName in self.peng else None
        if propName in ["t","aux"]:
            if not hasattr(self,"taux") or self.taux is None: return None
            return self.taux[propName] if propName in self.taux else None 
        return None

    # Get the value of the "n" property taking into account possible local "majestic" override
    def getNumber(self):
        if hasattr(self,"peng") and self.peng["n"] == "s" and self.peng["pe"]<3:
            if "maje" in self.peng and not self.peng["maje"]: return "s"
            if self.isMajestic():return "p"
        return self.getProp("n")

    def setProp(self,propName,val,inSetLemma=False):
        if propName in ["pe","n","g"] and hasattr(self,"peng") and self.peng is not None:
            self.peng[propName]=val
        if propName in ["t","aux"] and hasattr(self,"taux") and self.taux is not None:
            self.taux[propName]=val
        # this is important for to ensure that local options override global values
        # but it must not be done at initialization for peng and taux in Terminal.setLemma
        if propName not in ["pe","n","g","t","aux"] or not inSetLemma:
            self.props[propName]=val

    # should be in Terminal.prototype... but here for consistency with three previous definitions
    pengNO=0 # useful for debugging: identifier of peng struct to check proper sharing in the debugger
    tauxNO=0 # useful for debugging: identifier of taux struct to check proper sharing in the debugger
   
    def initProps(self):
        if self.isA("N","A","D","V","NO","Pro","Q","DT"):
            Constituent.pengNO+=1
            props = self.defaultProps()
            self.peng={"pe":props["pe"],
                       "n" :props["n"],
                       "g" :props["g"],
                       "pengNO":Constituent.pengNO}
            if self.isA("V"):
                self.taux={"t":props["t"]}
                Constituent.tauxNO+=1
                self.taux["tauxNO"]=Constituent.tauxNO

    # get a given constituent with a path starting at this
    #   path is a list of node type , or list of node types (an empty string in this list means optional)
    #   returns undefined if any node does not exist on the path
    def getFromPath(self,path):
        if len(path)==0: return self
        current=path.pop(0)
        c=self.getConst(current)
        if c is None:
            if isinstance(current,list) and "" in current and len(path)>0: # optional
                return self.getFromPath(path)
            return None
        return c.getFromPath(path)

    # return a pronoun corresponding to this object
    # taking into account the current gender, number and person
    #  do not change the current pronoun, if it is already using the tonic form or does not have one (e.g. this)
    # if case_ is not given, return the tonic form else return the corresponding case
    # HACK:: parameter case_ is followed by _ so that it is not displayed as a keyword in the editor
    def getTonicPro(self,case_=None):
        from .utils import Pro
        if self.isA("Pro"): # this is already a pronoun
            if "tn" in self.props or "c" in self.props: # already has tn() or c()
                if case_ is not None:
                    self.props["c"]=case_
                else: # ensure tonic form
                    self.props["tn"]=""
                    if "c" in self.props: del self.props["c"]
                return self
            else:
                if self.lemma in self.tonic_forms():
                    # the lemma is already in tonic form
                    if case_ is not None:
                        return Pro(self.lemma).c(case_)
                else:
                    if case_ is not None:
                        return Pro(self.realize()).c(case_)
                return self
        else: # generate the string corresponding to the tonic form
            pro=Pro(self.tonic_pe_1())
            g=self.getProp("g")
            if g is not None: pro.g(g)
            n=self.getProp("n")
            if n is not None: pro.n(n)
            pe=self.getProp("pe")
            if pe is not None: pro.pe(pe)
            if case_ is None:return Pro(pro.realize(),self.lang()).tn("")
            return Pro(pro.realize(),self.lang()).c(case_)
    
    def getParentLang(self):
        if hasattr(self,"lang"):return self.lang()
        if self.parentConst is None: return getLexicon().lang
        return self.parentConst.getParentLang()
                
    def addOptSource(self,optionName,val):
        self.optSource+=f'.{optionName}({repr(val)})'

    ###  genOptionFunc : see makeOptionMethod below
    
    ###  genOptionListFunc: see makeOptionListMethod below
    
    ## HTML tags
    def tag(self,name,attrs=None):
        if attrs is None or len(attrs)==0:
            self.addOptSource("tag",name)
            attrs={}
        else:
            self.optSource+=f'.tag("{name}",{str(attrs)})' # special case of addOptionSource
        if "tag" not in self.props:self.props["tag"]=[]
        self.props["tag"].append([name,attrs])
        return self
    
    def parseDateString(self,dateS):
        try:  ## parse the string as an iso-like time format 
            m=re.match(r"(\d{4}-\d{2}-\d{2})([T ](\d{2}:\d{2}:\d{2}))?",dateS)
            if m is None:
                self.warn("bad parameter","an isotime format string",dateS)
                return datetime.datetime.today()
            if m[2] is None:
                return datetime.datetime(int(m[1][0:4]),int(m[1][5:7]),int(m[1][8:10]))
            else:
                return datetime.datetime(int(m[1][0:4]),int(m[1][5:7]),int(m[1][8:10]),
                                            hour=int(m[3][0:2]),minute=int(m[3][3:5]),
                                            second=int(m[3][6:8]))
        except ValueError as e:
            self.warn("bad parameter","an isotime format string",dateS+":"+str(e))
            return datetime.datetime.today()

    
    ## date and number options
    def dOpt(self,dOptions):
        self.addOptSource("dOpt",dOptions)
        if not isinstance(dOptions,dict):
            return self.warn("bad application","dOpt","dict",type(dOptions).__name__)
        if self.isA("DT"):
            allowedKeys =["year" , "month" , "date" , "day" , "hour" , "minute" , "second" , "nat", "det", "rtime"]
            if "dOpt" not in self.props:self.props["dOpt"]={}
            for key,val in dOptions.items():
                if key in allowedKeys:
                    if key=="rtime":
                        if isinstance(val,bool):
                            self.props["dOpt"]["rtime"]=datetime.datetime.today() if val else False
                        elif isinstance(val,str):
                            self.props["dOpt"]["rtime"]=self.parseDateString(val)
                        elif isinstance(val,datetime.datetime):
                            self.props["dOpt"]["rtime"]=val
                        else:
                            return self.warn("bad application",'dOpt("rtime")',["bool","str","datetime"],val)
                    elif isinstance(val,bool):
                        self.props["dOpt"][key]=val
                    else:
                        return self.warn("bad application",f'dOpt("{key}")',["bool"],val)
                else:
                    return self.warn("ignored value for option","DT.dOpt",key)
        elif self.isA("NO"):
            allowedKeys = ["mprecision","raw","nat","ord","rom"]
            if "dOpt" not in self.props:self.props["dOpt"]={}
            for key,val in dOptions.items():
                if key in allowedKeys:
                    if key=="mprecision":
                        if isinstance(val,int):
                            self.props["dOpt"]["mprecision"]=val
                        else:
                            return self.warn("bad application","precision",val)
                    elif isinstance(val,bool):
                        self.props["dOpt"][key]=val
                    else:
                        return self.warn("bad application",f'.dOpt("{key}")',"bool",val)
                else:
                    return self.warn("ignored value for option","NO.dOpt",key)
        else:
            return self.warn("bad application",".dOpt",["DT","NO"],self.constType)
        return self

    # number option
    def nat(self,isNat=True):
        if self.isA("DT","NO"):
            if "dOpt" not in self.props:self.props["dOpt"]={}
            if isinstance(isNat,bool):
                self.props["dOpt"]["nat"]=isNat
                self.addOptSource("nat", isNat)
                return self
            return self.warn("bad application",".nat","bool",isNat)
        return self.warn("bad application",".nat",["DT","NO"],self.constType)

    # Override the global "majestic" flog for this Pro or D
    # HACK: this adds a flag to the peng structure so that agreements are correctly made
    def maje(self, isMaje):
        if self.isA("Pro","D"):
            if isinstance(isMaje,bool):
                self.setProp("maje",isMaje)
                self.peng["maje"]=isMaje
                self.addOptSource("maje",isMaje)
                return self
            return self.warn("bad application",".maje","boolean",isMaje)
        return self.warn("bad application",".maje",["Pro","D"],self.constType)

    def typ(self,types):
        allowedTypes={
              "neg": [False,True],
              "pas": [False,True],
              "prog":[False,True],
              "exc": [False,True],
              "perf":[False,True],
              "refl":[False,True],
              "contr":[False,True],
              "maje" :[False,True], # majestative (en français: politesse, modestie, majesté...)
              "mod": [False,"poss","perm","nece","obli","will"],
              "int": [False,"yon","wos","wod","woi","was","wad","wai","whe","why","whn","how","muc","tag"]
        }
        if not isinstance(types, dict):
            self.warn("ignored value for option",".typ",type(types).__name__+":"+str(types))
        elif not self.isA("S", "SP", "VP", *deprels):
            self.warn("bad application", f'.typ("{str(types)}")', ["S", "SP", "VP"], self.constType)
        else: # validate types and keep only the valid ones
            for key,val in types.copy().items():
                if key not in allowedTypes:
                    self.warn("unknown type",key,allowedTypes.keys())
                else:
                    if key == "neg" and self.validate_neg_option(val,types):
                        pass
                    elif val not in allowedTypes[key]:
                        self.warn("ignored value for option",f'.typ("{key}")',val)
                        del types[key]
            self.addOptSource("typ", types)
            if "typ" in self.props:
                self.props["typ"].update(types)
            else:
                self.props["typ"] = types

        return self


    # applies to a list of Constituents (can be a single one)
    # adds either to the first or last token (which can be the same)
    def doFormat(self,cList):
        punctuation=getRules(self.lang())["punctuation"]
        lex=getLexicon(self.lang())
    
        def getBeforeAfterString(punct):
            if punct in lex and "Pc" in lex[punct]:
                if "compl" in lex[punct]["Pc"]:
                    compl=lex[punct]["Pc"]["compl"]
                    before=punct
                    after=compl
                    tab=lex[punct]["Pc"]["tab"]
                    tabBefore=tab[0]
                    tabAfter=tab[1] if len(tab)==2 else lex[compl]["Pc"]["tab"][0] # get from table of compl 
                    puncRuleBefore=punctuation[tabBefore]
                    puncRuleAfter=punctuation[tabAfter]
                    return {"b":puncRuleBefore["b"]+before+puncRuleBefore["a"],
                            "a":puncRuleAfter["b"]+after+puncRuleAfter["a"]}
                else:
                    tab=lex[punct]["Pc"]["tab"][0]
                    puncRule=punctuation[tab]
                    punct=puncRule["b"]+punct+puncRule["a"]
            return {"b":punct,"a":punct}
    
        # add before the first element of cList and after the last element of cList
        def wrapWith(before,after):
            cList[0].realization=before+cList[0].realization
            cList[-1].realization+=after

        def startTag(tagName, attrs=None):
            if attrs is None:attrs = {}
            attString="".join(f' {key}="{val}"' for key,val in attrs.items())
            return "<"+tagName+attString+">"
    
        # remove possible empty realization strings (often generated by D("a").n("p")) which can break elision
        # but ensure there is at least one left so that options (.en, .a, .b) can be added.
        def removeEmpty(cList):
            i=0
            while i<len(cList):
                if cList[i].realization=="" and len(cList)>1: del cList[i]
                else:
                    i+=1
    
        # start of processing
        removeEmpty(cList)
        if self.isA("VP") or (self.isA(deprels) and self.terminal.isA("V")):
            self.doPronounPlacement(cList)
        self.doElision(cList)

        if self.getProp("poss"):
            cList[-1].realization += "'" if cList[-1].realization.endswith("s") else "'s"

        if self.getProp("cap") == True:
            cList[0].realization=cList[0].realization.capitalize()
 
        if "tag" in self.props:
            for attName,attVal in self.props["tag"]:
                wrapWith(startTag(attName,attVal),"</"+attName+">")

        if "a" in self.props:
            for a in self.props["a"]:
                wrapWith("",getBeforeAfterString(a)["b"])
 
        if "b" in self.props:
            for b in self.props["b"]:
                wrapWith(getBeforeAfterString(b)["b"],"")

        if "en" in self.props or "ba" in self.props:
            ens= self.props["en"] if "en" in self.props else self.props["ba"]
            for en in ens:
                ba=getBeforeAfterString(en)
                wrapWith(ba["b"],ba["a"])
        
        return cList
    # Apply Title case to the realization of a Terminal
    # according to https://apastyle.apa.org/style-grammar-guidelines/capitalization/title-case
    # Only the current terminal is taken into account,
    # so the "first word after a colon, em dash, or end punctuation" might not be capitalized as it should
    def titleCase(self,t):
        s = t.realization
        m = self.sepWordRE().match(s)
        word = m.group(2)
        l = len(word)  # get length of realization
        if l>=4 or not t.isA("C","P","D"):
            # capitalize words of 4 letters or more or short
            # non minor (conjunction,preposition,articles)
            idx = len(m.group(1)) # get index of first letter
            t.realization = s[0:idx] + s[idx].upper() + s[idx + 1:]

    def detokenize(self,terminals):
        if len(terminals)==0:return ""
        s=""
        doTitleCase = self.isEn() and self.getProp("cap")=="tit"
        for i in range(0,len(terminals)-1):
            terminal=terminals[i]
            if doTitleCase:self.titleCase(terminal)
            if terminal.realization.startswith(" "):    # remove redundant initial space
                terminal.realization=terminal.realization[1:]
            if terminal.getProp("lier"):
                # HACK: terminal.realization might be changed in French by check_for_t
                liaison = "-"+self.check_for_t(terminals,i);
                s+=terminal.realization+liaison;
            elif re.search(r"[- ']$",terminal.realization):
                s+=terminal.realization
            elif len(terminal.realization)>0:
                s+=terminal.realization+" "

        if doTitleCase : self.titleCase(terminals[-1])
        last = terminals[-1].realization
        if last.startswith(" "): last = last[1:] # remove redundant initial space
        s+=last
        # apply capitalization and final full stop unless .cap(False)
        if self.parentConst is None:
            if ((self.isA("S","root")
                 or (self.isA("coord") and len(self.dependents)>0 and self.dependents[0].isA("root")))
                and len(s)>0): ## this is a top-level S
                if "cap" not in self.props or self.getProp("cap") in [True,"tit"]:
                    m=self.sepWordRE().match(s)
                    idx=len(m.group(1)) # get index of first letter
                    if idx<len(s): # check if there was a letter
                        s=s[0:idx]+s[idx].upper()+s[idx+1:]
                    if "tag" not in self.props or self.props["tag"]==False: # do not touch top-level tag
                        # and a full stop at the end unless there is already one
                        # taking into account any trailing HTML tag
                        m=re.search(r"(.)( |(<[^>]+>))*$",s)
                        if m is not None and m.group(1) not in "?!.:;/)]}":
                            s+=". "   # add a space after "." , like for rule "pc4"
        return s
    
    ## this looks very simple, but it is the start of the realization process
    def realize(self,lang=None) -> str:
        if lang is not None:load(lang)
        terminals=self.real()
        return self.detokenize(terminals)
    
    def __str__(self):
        ## in Javascript, the realization is implicit with .toString(),
        ## so in Python, it should be also implicit with str(), but
        ## the Python debugger in PyCharm also uses str() to display information
        ## which can in some cases change the structure.
        ## This makes it hard to follow when tracing... a classic case of Heisenbug!
        ## When debug is True (tested with sys.gettrace()) : return the source of the expression
        ## but then realization must be launched with ".realize()"
        return self.toSource(-1) if Constituent.debug else self.realize()

    def clone(self):
        cln = copy.deepcopy(self)
        return cln
    
    def toSource(self,_indent):
        return self.optSource

    def addJSONprops(self,res):
        props = self.props
        if len(props) == 0 : return res
        res["props"] = {("ow" if prop=="own" else prop):self.props[prop] for prop in props}
        return res

    def setJSONprops(self,json):
        if "props" in json:
            for opt,val in json["props"].items():
                if hasattr(self,opt):
                    if isinstance(val,list):
                        for o in val:
                            if isinstance(o,list):
                                getattr(self,opt)(*o)
                            else:
                                getattr(self,opt)(o)
                    else:
                        getattr(self, opt)(val)
                elif opt not in ["pat","h","cnt","niveau","ldv"]: # do not copy properties from Terminal already in the lexicon
                    print("Constituent.fromJSON: illegal prop:"+opt,file=sys.stderr)
        return self                    



    def warn(self, *args):
        # print("WARNING:",self.me(),args,file=sys.stderr)
        mess = self.warning(args)
        if Constituent.exceptionOnWarning:
            raise Exception(mess)
        print(mess, file=sys.stderr)
        return self


    
## add Constituent methods for setting properties 
## adapted from https://stackoverflow.com/questions/8276733/dynamically-add-methods-to-a-class-in-python-3-0
# for standard options
def makeOptionMethod(option,validVals,allowedConsts,optionName=None):
    def _method(self, val=None,prog=None):
        nonlocal optionName
        if optionName is None: optionName = option
        if val is None:
            if "" not in validVals:
                return self.warn("no value for option",option,validVals)
        if self.isA("CP") and option not in ["cap","lier","pos"]:
            # propagate an option through the children of a CP except for "cap", "lier" and "pos"
            if prog is None:self.addOptSource(optionName,val)
            for e in self.elements:
                if len(allowedConsts)==0 or e.isA(allowedConsts):
                    getattr(e,option)(val,True)  # do not add this option in the source
            return self
        if self.isA("coord") and option not in ["cap","lier","pos"]:
            # propagate an option through the head of the children of a coord except for "cap", "lier" and "pos"
            if prog is None: self.addOptSource(optionName, val)
            for e in self.dependents:
                if len(allowedConsts) == 0 or e.terminal.isA(allowedConsts):
                    getattr(e.terminal, option)(val, True)  # do not add this option in the source
            return self
        if len(allowedConsts)==0 or self.isA(allowedConsts) or self.isA(deprels):
            if val is None:
                if "" not in validVals:
                    return self.warn("ignored value for option", option, val)
                val = True
            elif val not in validVals:
                self.warn("ignored value for option", option, val)
                if False not in validVals:return self
                val = False
            self.setProp(optionName,val)
            if prog is None:self.addOptSource(option,val)
            return self
        else:
            if quoteOOV and self.isA("Q"):return self
            return self.warn("bad const for option",option,self.constType,allowedConsts)
        
    return _method


# shared properties 
#   pe,n and g : can be applied to components of NP and Sentences
setattr(Constituent,"pe",makeOptionMethod("pe",[1,2,3,'1','2','3'],["D","Pro","N","NP","A","AP","V","VP","S","SP","CP"]))
setattr(Constituent,"n",makeOptionMethod("n",["s","p","x"],["D","Pro","N","NO","NP","A","AP","V","VP","S","SP","CP"]))
setattr(Constituent,"g",makeOptionMethod("g",["m","f","n","x"],["D","Pro","N","NP","A","AP","V","VP","S","SP","CP"]))
#  t, aux : can be applied to VP and sentence
setattr(Constituent,"t",makeOptionMethod("t",["p", "i", "f", "ps", "c", "s", "si", "ip", "pr", "pp", "b","b-to", # simple tenses
                   "pc", "pq", "cp", "pa", "fa", "spa", "spq","bp","bp-to"],["V","VP","S","SP","CP"]))  # compound tenses
setattr(Constituent,"aux",makeOptionMethod("aux",["av","êt","aê"],["V","VP","S","SP","CP"]))
# ordinary properties
setattr(Constituent,"f",makeOptionMethod("f",["co","su"],["A","Adv"]))
setattr(Constituent,"tn",makeOptionMethod("tn",["","refl"],["Pro"]))
setattr(Constituent,"c",makeOptionMethod("c",["nom","acc","dat","refl","gen"],["Pro"]))

setattr(Constituent,"pos",makeOptionMethod("pos",["post","pre"],["A","Adv",*deprels]))
setattr(Constituent,"pro",makeOptionMethod("pro",["",False,True],["NP","PP"]))
# English only
setattr(Constituent,"ow",makeOptionMethod("ow",["s","p","x"],["D","Pro"],"own"))
setattr(Constituent,"poss",makeOptionMethod("poss",["",False,True],["N","Q"]))

# Formatting options
setattr(Constituent,"cap",makeOptionMethod("cap",["",False,True,"tit"],[]))
setattr(Constituent,"lier",makeOptionMethod("lier",["",False,True],[]))

def makeOptionListMethod(option):
    def _method(self,val,prog=None):
        if option not in self.props:self.props[option] = []
        self.props[option].append(val)
        if prog is None:self.addOptSource(option,val)
        return self
    return _method

for name in optionListMethods:
    setattr(Constituent, name, makeOptionListMethod(name))

      