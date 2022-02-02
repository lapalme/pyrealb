import re,datetime,sys

from .Lexicon import getLexicon, getLemma, getRules, currentLanguage

defaultProps = {"en":{"g":"n","n":"s","pe":3,"t":"p"},             # language dependent default properties
                "fr":{"g":"m","n":"s","pe":3,"t":"p","aux":"av"}}; 

quoteOOV=False # TODO: make this settable globally
optionListMethods = ('a', 'b', 'ba', 'en')

# regex for matching the first word in a generated string (ouch!!! it is quite subtle...) 
#  match index:
#     1-possible non-word chars and optional html tags
#     2-the real word 
#     3-the rest after the word  
sepWordREen=re.compile(r"((?:[^<\w'-]*(?:<[^>]+>)?)*)([\w'-]+)?(.*)")
# same as sepWordREen but the [\w] class is extended with French accented letters and cedilla
sepWordREfr=re.compile(r"((?:[^<\wàâéèêëîïôöùüç'-]*(?:<[^>]+>)?)*)([\wàâéèêëîïôöùüç'-]+)?(.*)",re.I)

class Constituent():
    def __init__(self,constType):
        self.constType=constType
        # initialize other params
        self.parentConst=None
        self.props = {}
        self.realization=None 
        self.optSource=""     # string corresponding to the calls to the options
    
    def error(self,mess):
        raise Exception ("Internal error: this should never have happened,sorry!\n"+self.me()+"::"+mess)
    
    def isA(self,aType):
        return self.constType==aType
    
    def isOneOf(self,types):
        return self.constType in types
    
    def isFr(self):
        return self.lang=="fr"
    
    def isEn(self):
        return self.lang=="en"
    
    # def __pos__(self): # prefix + :: useful trick for testing top-level expression realization
    #     print(str(self))
    
    # get/set the value of a property by first checking the special shared properties
    def getProp(self,propName):
        if propName in self.props:
            return self.props[propName] 
        if propName in ["pe","n","g"]:
            if not hasattr(self, "peng") or self.peng==None: return None
            return self.peng[propName] if propName in self.peng else None
        if propName in ["t","aux"]:
            if not hasattr(self,"taux") or self.taux==None: return None
            return self.taux[propName] if propName in self.taux else None 
        return None
    
    def setProp(self,propName,val):
        if propName in ["pe","n","g"] and hasattr(self,"peng"):
            self.peng[propName]=val
        if propName in ["t","aux"] and hasattr(self,"taux"):
            self.taux[propName]=val
        self.props[propName]=val

    # should be in Terminal.prototype... but here for consistency with three previous definitions
    pengNO=0; # useful for debugging: identifier of peng struct to check proper sharing in the debugger
    tauxNO=0; # useful for debugging: identifier of taux struct to check proper sharing in the debugger
   
    def initProps(self):
        if self.isOneOf(["N","A","D","V","NO","Pro","Q","DT"]):
            self.peng={"pe":defaultProps[self.lang]["pe"],
                       "n" :defaultProps[self.lang]["n"],
                       "g" :defaultProps[self.lang]["g"]}
            Constituent.pengNO+=1
            self.peng["pengNO"]=Constituent.pengNO
            if self.isA("V"):
                self.taux={"t":defaultProps[self.lang]["t"]}
                Constituent.tauxNO+=1
                self.taux["tauxNO"]=Constituent.tauxNO
                if self.isFr():
                    self.taux["aux"]=defaultProps[self.lang]["aux"]
    
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
    #  do not change the current pronoun, if it is already using the tonic form
    # if case_ is not given, return the tonic form else return the corresponding case
    # HACK:: parameter case_ is followed by _ so that it is not displayed as a keyword in the editor
    def getTonicPro(self,case_):
        from .Terminal import Pro
        if self.isA("Pro") and ("tn" in self.props or "c" in self.props):
            if case_ is None:
                self.props["c"]=case_
            else: # ensure tonic form
                self.props["tn"]=""
                if "c" in self.props: del self.props["c"]
            return self
        else: # generate the string corresponding to the tonic form
            pro=Pro("moi" if self.isFr() else "me",self.lang)
            g=self.getProp("g")
            if g!=None: pro.g(g)
            n=self.getProp("n")
            if n!=None: pro.n(n)
            pe=self.getProp("pe")
            if pe!=None: pro.pe(pe)
            if case_ is None:return Pro(pro.realize(),self.lang).tn("")
            return Pro(pro.realize(),self.lang).c(case_)
    
    def getParentLang(self):
        if hasattr(self,"lang"):return self.lang
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
            self.optSource+=f'.tag("{name}",str(attrs))' # specila case of addOptionSource
        if "tag" not in self.props:self.props["tag"]=[]
        self.props["tag"].append([name,attrs])
        return self
    
    def parseDateString(self,dateS):
        try:  ## parse the string as an iso-like time format 
            m=re.match(r"(\d{4}-\d{2}-\d{2})([T ](\d{2}:\d{2}:\d{2}))?",dateS)
            if m==None:
                self.warn("bad parameter","an isotime format string",dateS)
                return datetime.datetime.today()
            else:
                if m[2]==None:
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
            allowedKeys = ["mprecision","raw","nat","ord"]
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
        self.addOptSource("nat",isNat)
        if self.isOneOf(["DT","NO"]):
            if "dOpt" not in self.props:self.props["dOpt"]={}
            if isNat is None:
                self.props["dOpt"]["nat"]=False
            elif isinstance(isNat,bool):
                self.props["dOpt"]["nat"]=isNat
            else:
                return self.warn("bad application",".nat","bool",isNat)
        else:
            return self.warn("bad application",".nat",["DT","NO"],self.constType)
        return self
    
    def typ(self,types):
        allowedTypes={
              "neg": [False,True],
              "pas": [False,True],
              "prog":[False,True],
              "exc": [False,True],
              "perf":[False,True],
              "refl":[False,True],
              "contr":[False,True],
              "mod": [False,"poss","perm","nece","obli","will"],
              "int": [False,"yon","wos","wod","woi","was","wad","wai","whe","why","whn","how","muc"]
        }
        self.addOptSource("typ",types)
        if not isinstance(types, dict):
            self.warn("ignored value for option",".typ",type(types).__name__+":"+str(types))
        elif not self.isOneOf(["S", "SP", "VP"]):
            self.warn("bad application", f'.typ("{str(types)}")', ["S", "SP", "VP"], self.constType)
        else: # validate types and keep only the valid ones
            for key,val in types.copy().items():
                if key not in allowedTypes:
                    self.warn("unknown type",key,allowedTypes.keys())
                else:
                    if key=="neg" and self.isFr(): # also accept string as neg value in French
                        if not isinstance(val,(str,bool)):
                            self.warn("ignored value for option",f'.typ("{key}")',val)
                            del types[key]
                    elif val not in allowedTypes[key]:
                        self.warn("ignored value for option",f'.typ("{key}")',val)
                        del types[key]
            self.props["typ"]=types
        return self
                
    def doElisionEn(self,cList):
        # English elision rule only for changing "a" to "an"
        # according to https:#owl.english.purdue.edu/owl/resource/591/1/
        hAnRE=re.compile(r"^(heir|herb|honest|honou?r(able)?|hour)",re.I)
        # https:#www.quora.com/Where-can-I-find-a-list-of-words-that-begin-with-a-vowel-but-use-the-article-a-instead-of-an
        uLikeYouRE=re.compile(r"^(uni.*|ub.*|use.*|usu.*|uv.*)",re.I)
        acronymRE=re.compile(r"^[A-Z]+$")
        # Common Contractions in the English Language taken from :http:#www.everythingenglishblog.com/?p=552
        contractionEnTable={
            "are+not":"aren’t", "can+not":"can’t", "did+not":"didn’t", "do+not":"don’t", "does+not":"doesn’t", 
            "had+not":"hadn’t", "has+not":"hasn’t", "have+not":"haven’t", "is+not":"isn’t", "must+not":"mustn’t", 
            "need+not":"needn’t", "should+not":"shouldn’t", "was+not":"wasn’t", "were+not":"weren’t", 
            "will+not":"won’t", "would+not":"wouldn’t",
            "let+us":"let’s",
            "I+am":"I’m", "I+will":"I’ll", "I+have":"I’ve", "I+had":"I’d", "I+would":"I’d",
            "she+will":"she’ll", "he+is":"he’s", "he+has":"he’s", "she+had":"she’d", "she+would":"she’d",
            "he+will":"he’ll", "she+is":"she’s", "she+has":"she’s", "he+would":"he’d", "he+had":"he’d",
            "you+are":"you’re", "you+will":"you’ll", "you+would":"you’d", "you+had":"you’d", "you+have":"you’ve",
            "we+are":"we’re", "we+will":"we’ll", "we+had":"we’d", "we+would":"we’d", "we+have":"we’ve",
            "they+will":"they’ll", "they+are":"they’re", "they+had":"they’d", "they+would":"they’d", "they+have":"they’ve",
            "it+is":"it’s", "it+will":"it’ll", "it+had":"it’d", "it+would":"it’d",
            "there+will":"there’ll", "there+is":"there’s", "there+has":"there’s", "there+have":"there’ve",
            "that+is":"that’s", "that+had":"that’d", "that+would":"that’d", "that+will":"that’ll"
        } 
        # search for terminal "a" and check if it should be "an" depending on the next word
        last=len(cList)-1
        if last==0: return # do not try to elide a single word
        i=0
        while i<last:
            m1=sepWordREen.match(cList[i].realization)
            if m1 is None or m1.group(2) is None: 
                i+=1
                continue
            m2=sepWordREen.match(cList[i+1].realization)
            if m2 is None or m2.group(2) is None: 
                i+=1
                continue
            # HACK: m1 and m2 save the parts before and after the first word (w1 and w2) which is in m_i.group(2)
            # for a single word 
            w1=m1.group(2)
            w2=m2.group(2)
            if (w1=="a" or w1=="A") and cList[i].isA("D"):
                if (re.match(r"^[aeio]",w2,re.I) or   # starts with a vowel
                    (re.match(r"^u",w2,re.I) and not uLikeYouRE.match(w2) or  # u does not sound like you
                    hAnRE.match(w2) or       # silent h
                    acronymRE.match(w2))):   # is an acronym
                        cList[i].realization=m1.group(1)+w1+"n"+m1.group(3)
                        i+=1;                 # skip next word
            elif hasattr(self,"contraction") and self.contraction == True:
                if w1=="cannot": # special case...
                    cList[i].realization=m1.group(1)+"can't"+m1.group(3)
                else:
                    key=w1+"+"+w2
                    if key in contractionEnTable:
                        contr=contractionEnTable[key];   
                        # do contraction of first word and remove second word (keeping start and end)
                        cList[i].realization=m1.group(1)+contr+m1.group(3)
                        cList[i+1].realization=m2.group(1)+m2.group(3).strip()
                        i+=1
            i+=1
        
    def doElisionFr(self,cList):
        # Elision rules for French
        # implements the obligatory elision rules of the "Office de la langue française du Québec"
        #    http:#bdl.oqlf.gouv.qc.ca/bdl/gabarit_bdl.asp?Th=2&t1=&id=1737
        # for Euphonie, rules were taken from Antidote (Guide/Phonétique)

        elidableWordFrRE=re.compile(r"^(la|le|je|me|te|se|de|ne|que|puisque|lorsque|jusque|quoique)$",re.I)
        euphonieFrRE=re.compile(r"^(ma|ta|sa|ce|beau|fou|mou|nouveau|vieux)$",re.I)
        euphonieFrTable={"ma":"mon","ta":"ton","sa":"son","ce":"cet",
            "beau":"bel","fou":"fol","mou":"mol","nouveau":"nouvel","vieux":"vieil"}

        contractionFrTable={
            "à+le":"au","à+les":"aux","ça+a":"ç'a",
            "de+le":"du","de+les":"des","de+des":"de","de+autres":"d'autres",
            "des+autres":"d'autres",
            "si+il":"s'il","si+ils":"s'ils"}

        def isElidableFr(realization,lemma,pos):
            # check if realization starts with a vowel
            if re.match(r"^[aeiouyàâéèêëîïôöùü]",realization,re.I): return True
            if re.match(r"^h",realization,re.I):
                #  check for a French "h aspiré" for which no elision should be done
                lexiconInfo=getLemma(lemma if isinstance(lemma,str) else realization) # get the lemma with the right pos
                if lexiconInfo  is None: 
                    lexiconInfo=getLemma(lemma.toLowerCase()) # check with lower case
                    if lexiconInfo  is None: return True       # elide when unknown
                if pos not in lexiconInfo:pos=lexiconInfo.keys()[0] # try the first pos if current not found
                if pos in lexiconInfo and "h" in lexiconInfo[pos] and lexiconInfo[pos]["h"]==1: return False # h aspiré found
                return True
            return False

        contr=None
        last=len(cList)-1
        if last==0:return # do not try to elide a single word
        i=0
        while i < last:
            if i>0 and cList[i-1].getProp("lier")!=None: # ignore if the preceding word is "lié" to this one
                i+=1
                continue
            m1=sepWordREfr.match(cList[i].realization) if cList[i].realization!=None else None
            if m1  is None or m1.group(2) is None: continue
            m2=sepWordREfr.match(cList[i+1].realization) if cList[i].realization!=None else None
            if m2  is None or m2.group(2) is None: continue
            # HACK: m1 and m2 save the parts before and after the first word (w1 and w2) which is in m_i[2]
            # for a single word
            w1=m1.group(2)
            w2=m2.group(2)
            w3NoWords = not re.match(r"^\s*\w",m1.group(3)) # check that the rest of the first word does not start with a word
            if (elidableWordFrRE.match(w1) and isElidableFr(w2,cList[i+1].lemma,cList[i+1].constType) and w3NoWords):
                cList[i].realization=m1[1]+w1[:-1]+"'"+m1[3]
                i+=1
            elif euphonieFrRE.match(w1) and isElidableFr(w2,cList[i+1].lemma,cList[i+1].constType) and  w3NoWords: # euphonie
                if re.match(r"ce",w1,re.I) and re.match(r"(^est$)|(^étai)",w2,re.I):
                    # very special case but very frequent
                    cList[i].realization=m1[1]+w1[:-1]+"'"+m1[3]
                else:
                    cList[i].realization=m1[1]+euphonieFrTable[w1]+m1[3]
                i+=1
            elif (w1+"+"+w2) in contractionFrTable and w3NoWords:
                contr=contractionFrTable[w1+"+"+w2]
                # check if the next word would be elidable, so instead elide it instead of contracting
                # except when the next word is a date which has a "strange" realization
                if (elidableWordFrRE.match(w2) and i+2<=last and not cList[i+1].isA("DT") and
                    isElidableFr(cList[i+2].realization,cList[i+2].lemma,cList[i+2].constType)):
                    cList[i+1].realization=m2[1]+w2[:-1]+"'"+m2[3]
                else: # do contraction of first word and remove second word (keeping start and end)
                    cList[i].realization=m1[1]+contr+m1[3]
                    cList[i+1].realization=m2[1]+m2[3].strip()
                i+=1
            i+=1
        
    
    # applies to a list of Constituents (can be a single one)
    # adds either to the first or last token (which can be the same)
    def doFormat(self,cList):
        punctuation=getRules()["punctuation"]
        lex=getLexicon()   
    
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

        def startTag(tagName,attrs):
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
        # reorder French pronouns within a VP
        if self.isA("VP") and self.isFr():
            self.doFrenchPronounPlacement(cList)
            
        if self.isFr():
            self.doElisionFr(cList)
        else:
            self.doElisionEn(cList)
    
        if "cap" in self.props and self.props["cap"]!=False:
            cList[0].realization=cList[0].realization.capitalize()
 
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
        
        if "tag" in self.props:
            for attName,attVal in self.props["tag"]:
                wrapWith(startTag(attName,attVal),"</"+attName+">")

        return cList
    
    def detokenize(self,terminals):
        if len(terminals)==0:return ""
        s=""
        for i in range(0,len(terminals)-1):
            terminal=terminals[i]
            if "lier" in terminal.props:
                s+=terminal.realization+"-"
                # check for adding -t- in French between a verb and a pronoun
                if self.isFr() and terminal.isA("V") and terminals[i+1].isA("Pro"):
                    # According to Antidote:
                    # C’est le cas, notamment, quand le verbe à la 3e personne du singulier du passé, du présent ou 
                    # du futur de l’indicatif se termine par une autre lettre que d ou t et qu’il est suivi 
                    # des pronoms sujets il, elle ou on. Dans ce cas, on ajoute un ‑t‑ entre le verbe 
                    # et le pronom sujet inversé.
                    if re.search(r"[^dt]$",terminal.realization) and re.match(r"[ieo]",terminals[i+1].realization):
                        s+="t-"
            elif re.search(r"[- ']$",terminal.realization):
                s+=terminal.realization
            elif len(terminal.realization)>0:
                s+=terminal.realization+" "
        s+=terminals[-1].realization
        # apply capitalization and final full stop
        if self.parentConst is None:
            if self.isA("S") and len(s)>0: ## this is a top-level S
                if "cap" not in self.props or self.props["cap"]!=False:
                    sepWordRE=sepWordREen if self.isEn() else sepWordREfr
                    m=sepWordRE.match(s)
                    idx=len(m.group(1)) # get index of first letter
                    if idx<len(s): # check if there was a letter
                        s=s[0:idx]+s[idx].upper()+s[idx+1:]
                if "tag" not in self.props or self.props["tag"]==False: # do not touch top-level tag
                    # and a full stop at the end unless there is already one
                    # taking into account any trailing HTML tag
                    m=re.search(r"(.)( |(<[^>]+>))*$",s)
                    if m!=None and m.group(1) not in "?!.:;/":
                        s+="."
        return s
    
    ## this looks very simple, but it is the start of the realization process
    def realize(self) -> str:
        terminals=self.real()
        return self.detokenize(terminals)
    
    def __str__(self):
        ## in Javascript, the realization is implicit with __str__ but given that
        ##     the python debugger also uses str() to display information that
        ##     makes is hard to follow when tracing... 
        ##     I found more useful during development to (un)comment these lines
        ##     but then realization must be launched with ".realize()"
        # return self.toSource(-1)
        return self.realize()
    
    def clone(self):
        return eval(self.toSource(),globals())
    
    def toSource(self):
        return self.optSource
    
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
                        getattr(self,opt)(val)
                else:
                    print("Constituent.fromJSON: illegal prop:"+opt,file=sys.stderr)
        return self                    
    
    def warn(self,*args):
        from .Warning import warning
        # print("WARNING:",self.me(),args,file=sys.stderr)
        print(warning(self,args),file=sys.stderr)
        return self


    
## add Constituent methods for setting properties 
## adapted from https://stackoverflow.com/questions/8276733/dynamically-add-methods-to-a-class-in-python-3-0
# for standard options
def makeOptionMethod(option,validVals,allowedConsts,optionName=None):
    def _method(self, val=None,prog=None):
        nonlocal optionName
        if val is None:
            if validVals!=None and "" not in validVals:
                return self.warn("no value for option",option,validVals)
        if self.isA("CP") and option not in ["cap","lier"]:
            # propagate an option through the children of a CP except for "cap" and "lier"
            if prog is None:self.addOptSource(optionName,val)
            for e in self.elements:
                if len(allowedConsts)==0 or e.isOneOf(allowedConsts):
                    e[option](val)
            return self
        if len(allowedConsts)==0 or self.isOneOf(allowedConsts):
            if validVals!=None and val not in validVals:
                return self.warn("ignored value for option",option,val)
            # start of the real work
            if optionName is None:optionName=option
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
setattr(Constituent,"n",makeOptionMethod("n",["s","p","x"],["D","Pro","N","NP","A","AP","V","VP","S","SP","CP"],None))
setattr(Constituent,"g",makeOptionMethod("g",["m","f","n","x"],["D","Pro","N","NP","A","AP","V","VP","S","SP","CP"]))
#  t, aux : can be applied to VP and sentence
setattr(Constituent,"t",makeOptionMethod("t",["p", "i", "f", "ps", "c", "s", "si", "ip", "pr", "pp", "b", # simple tenses
                   "pc", "pq", "cp", "fa", "spa", "spq"],["V","VP","S","SP","CP"]));  # composed tenses
setattr(Constituent,"aux",makeOptionMethod("aux",["av","êt","aê"],["V","VP","S","SP","CP"]))
# ordinary properties
setattr(Constituent,"f",makeOptionMethod("f",["co","su"],["A","Adv"]))
setattr(Constituent,"tn",makeOptionMethod("tn",["","refl"],["Pro"]))
setattr(Constituent,"c",makeOptionMethod("c",["nom","acc","dat","refl","gen"],["Pro"]))

setattr(Constituent,"pos",makeOptionMethod("pos",["post","pre"],["A"]))
setattr(Constituent,"pro",makeOptionMethod("pro",None,["NP","PP"]))
# English only
setattr(Constituent,"ow",makeOptionMethod("ow",["s","p","x"],["D","Pro"],"own"))

# Formatting options
setattr(Constituent,"cap",makeOptionMethod("cap",None,[]))
setattr(Constituent,"lier",makeOptionMethod("lier",None,[]))

def makeOptionListMethod(option):
    def _method(self,val,prog=None):
        if option not in self.props:self.props[option] = []
        self.props[option].append(val)
        if prog is None:self.addOptSource(option,val)
        return self
    return _method

for name in optionListMethods:
    setattr(Constituent, name, makeOptionListMethod(name))

      