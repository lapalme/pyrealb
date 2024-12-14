from .Constituent import Constituent,deprels, quoteOOV
from .Number import enToutesLettres, ordinal, roman
from .Lexicon import getLemma, getRules

import datetime, re

class Terminal(Constituent):
    def __init__(self, terminalType,lemma):
        super().__init__(terminalType)
        self.lemma=lemma # needed for error message
        self.setLemma(lemma,terminalType)
            
    def me(self):
        return self.constType+"("+repr(self.lemma)+")"
    
    def morphoError(self,errorKind,keyVals):
        self.warn("morphology error",errorKind+f" {self.me()} :"+repr(keyVals))
        self.realization=f"[[{self.lemma}]]"
        self.constType="Q"
        return self
    
    ## TODO: see Warning.js
    def add(self,_):
        self.warn("bad application",".add","Phrase",type(self))
        return self
    
    # set lemma, precompute stem and store conjugation/declension table number 
    # TODO: add lang as last parameter
    def setLemma(self,lemma,terminalType=None):
        if terminalType is None: # when it is not called from a Constructor, keep the current terminalType
            terminalType=self.constType
        if isinstance(lemma, str):
            lemma=lemma.replace("œ","oe").replace("æ","ae")
        self.lemma=lemma
        if not hasattr(self, "peng"):self.initProps()
        if terminalType=="DT":
            if lemma is None or lemma=="":
                self.date=datetime.datetime.today()
                self.lemma=str(self.date)
            else:
                if isinstance(lemma,str):
                    self.date=self.parseDateString(lemma)
                elif isinstance(lemma,datetime.datetime):
                    self.date=lemma
                else:
                    self.warn("bad parameter","str,datetime.datetime",type(lemma).__name__)
                    self.date=datetime.datetime.today()                   
            ## set defaults
            self.props["dOpt"]={"year":True,"month":True,"date":True,"day":True,
                        "hour":True,"minute":True,"second":True,
                        "nat":True,"det":True,"rtime":False}
        elif terminalType=="NO":
            if not isinstance(lemma,(str,int,float)):
                self.warn("bad parameter",["str","int","float"],type(lemma).__name__)
                self.lemma=0
            elif isinstance(lemma,str):
                lexInfo = getLemma(self.lemma)
                if lexInfo is not None and "value" in lexInfo:
                    if "A" in lexInfo:
                        # if it exists as an adjective it is considered as an ordinal number written in letters
                        # is given its "value" as lemma
                        self.lemma=self.value=lexInfo["value"]
                        self.nbDecimals=0
                        self.props["dOpt"] = {"ord":True}
                        self.addOptSource("ord",True)
                        return
                    else:
                        # a number written in letters is given its "value" as lemma
                        self.lemma=self.value=lexInfo["value"]
                        self.nbDecimals=0
                        self.props["dOpt"] = {"nat":True}
                        self.addOptSource("nat",True)
                        return
                # check if this looks like a legal number
                else:
                    if not re.match(r"^[-+]?[0-9]+([., ][0-9]*)?([Ee][-+][0-9]+)?$",lemma):
                        self.warn("bad parameter","number",type(lemma).__name__)
                        self.lemma=0
                    else:
                        self.lemma=re.sub(self.thousands_separator(),"",self.lemma)
                    try:
                        self.value=int(self.lemma)
                    except ValueError:
                        self.value=float(self.lemma)
                    self.nbDecimals=str(self.lemma)[::-1].find(".")
            else:
                self.value=lemma
                self.nbDecimals=str(lemma)[::-1].find(".")
                if self.nbDecimals<0:self.nbDecimals=0
            self.props["dOpt"]={"mprecision":2,"raw":False,"ord":False}
        elif terminalType=="Q":
            self.lemma=str(lemma)
        elif terminalType in ["N","A","Pro","D","V","Adv","C","P"]:
            if not isinstance(lemma,str):
                self.tab=None 
                self.realization=f"[[{lemma}]]"
                return self.warn("bad parameter","string",type(lemma).__name__)
            lexInfo=getLemma(self.lemma)
            if lexInfo is None:
                self.tab=None 
                self.realization=f"[[{lemma}]]"
                return self.warn("not in lexicon",self.lang(),None)
                # if quoteOOV: # not currently used
                #     self.lemma=str(lemma)
                #     self.realization=self.lemma
                #     self.constType="Q"
            else:
                if terminalType not in lexInfo:
                    self.tab=None 
                    self.realization=f"[[{lemma}]]"
                    otherPOS=list(lexInfo.keys())
                    if "ldv" in otherPOS:otherPOS.remove("ldv")
                    return self.warn("not in lexicon",self.lang(),otherPOS)
                    # if quoteOOV: # not currently used
                    #     self.lemma=str(lemma)
                    #     self.realization=self.lemma
                    #     self.constType="Q"
                else:
                    lexInfo=lexInfo[terminalType]
                    rules=getRules(self.lang())
                    for (key,info) in lexInfo.items():
                        if key=="tab": # save table number and compute stem
                            ending=None 
                            self.tab=info
                            if not self.isA("V"):
                                if self.tab in rules["declension"]: #  occurs for C, Adv and P
                                    declension=rules["declension"][self.tab]
                                    ending=declension["ending"]
                                    if terminalType=="Pro":
                                        #  set person for Pro when different from 3 (i.e. all elements of
                                        #  declension are the same)
                                        dd=declension["declension"]
                                        if "pe" in dd[0]:
                                            pe=dd[0]["pe"]
                                            if pe!=3:
                                                i=1
                                                while i<len(dd) and dd[i]["pe"]==pe:i+=1
                                                if i==len(dd):self.setProp("pe",pe)
                                        else:
                                            pe=3
                                    elif terminalType=="N" and self.tab in self.noun_always_plural():
                                        self.setProp("n","p")
                            else:
                                if self.tab in rules["conjugation"]:
                                    ending=rules["conjugation"][self.tab]["ending"]
                                else:
                                    ending=""
                                    self.warn("bad lexicon table",lemma,ending)
                            if ending is not None and self.lemma.endswith(ending):
                                self.stem=self.lemma if ending=="" else self.lemma[:-len(ending)]
                            else:
                                self.tab=None 
                                if not self.isA("Adv","C","P"):
                                    self.warn("bad lexicon table",lemma,ending)
                        else:
                            # if isinstance(info,list) and len(info)==1:info=info[0]
                            self.setProp(key,info,True)
        else:
            self.warn("not implemented",terminalType)
    
    def grammaticalNumber(self):
        # overriden in TerminalEn and TerminalFr
        if not self.isA("NO"):
            return self.warn("bad application","grammaticalNumber","NO",self.constType)
        n = self.getProp("")
        if n is not None: # explicit number given to NO
            return n
        if "dOpt" in self.props and "ord" in self.props["dOpt"] and self.props["dOpt"]["ord"]:
            return "s"
        return None

    def getIndex(self,constTypes):
        if isinstance(constTypes, str):
            return 0 if self.isA(constTypes) else -1
        return 0 if self.isA(constTypes) else -1
    
    def getConst(self,constTypes):
        return self if self.getIndex(constTypes)==0 else None 
    
    # try to find the best declension match
    #    value equal = 2
    #    equal with x = 1
    #    no match = 0
    #  but if the person does not match set score to 0           
    def bestMatch(self,errorKind,declension,keyVals):                       
        bestMatch=(0,None)
        for d in declension:
            nbMatches=0
            for key,val in keyVals.items():
                if key in d:
                    if key=="pe" and d[key]!=val: # persons must match exactly
                        nbMatches=0
                        break
                    if d[key]==val:nbMatches+=2
                    elif d[key]=="x":nbMatches+=1
            if nbMatches>bestMatch[0]:
                bestMatch=(nbMatches,d["val"])
        if bestMatch[0]==0:
            self.morphoError(errorKind, keyVals)
            return None 
        return bestMatch[1]                 

    def isMajestic(self):
        maje = self.getProp("maje") # check local value
        if maje != None : return maje
        pc = self.parentConst
        while pc != None:   # check context
            if "typ" in pc.props and "maje" in pc.props["typ"] and pc.props["typ"]["maje"]: return True
            pc = pc.parentConst
        return False


    def decline(self,setPerson):
        rules=getRules(self.lang())
        declension=rules["declension"][self.tab]["declension"]
        stem=self.stem
        g = self.getProp("g")
        if self.isA("D", "N") and g is None: g = "m"
        n = self.getNumber()
        if self.isA("D", "N") and n is None: n = "s"
        if self.isA("A","Adv"):
            return self.decline_adj_adv(rules,declension,stem)
        elif len(declension)==1: # no declension
            self.realization = self.stem+declension[0]["val"]
        else: # for N,D,Pro
            pe=3
            if setPerson:
                p=self.getProp("pe")
                pe=3 if p is None else int(p)
            keyVals={"pe":pe,"g":g,"n":n} if setPerson else {"g":g,"n":n}
            if not self.isA("N") and self.isMajestic():
                if self.check_majestic(keyVals):
                    declension = rules["declension"][self.tab]["declension"]
            if "own" in self.props:
                keyVals["own"]=self.props["own"]
            if self.isA("Pro"):
                c  = self.props["c"] if "c" in self.props else None
                if c is not None:
                    if not self.check_bad_pronoun_case(c):
                        keyVals["c"]=c
                tn = self.props["tn"] if "tn" in self.props else None
                if tn  is not None:
                    if c is not None:
                        self.warn("both tonic and clitic")
                    else:
                        keyVals["tn"]=tn
                if c  is not None or tn  is not None:
                    if self.lemma == self.tonic_pe_1():
                        # HACK:remove defaults from pronoun such as "moi" in French and "me" in English
                        #      because their definition is special in order to try to keep some upward compatibility
                        #      with the original way of specifying the pronouns
                        if self.getProp("g")  is None: del keyVals["g"]
                        if self.getProp("n")  is None: del keyVals["n"]
                        # make sure it matches the first and set the property for verb agreement
                        if (c=="nom" or tn=="") and self.getProp("pe") is None:
                            keyVals["pe"]=1
                            self.setProp("pe",1)
                    else: # set person, gender and number except when subject in an English genitive
                        d0=declension[0]
                        if self.should_set_person_number(c):
                            self.setProp("g", d0["g"] if "g" in d0 else g)
                            self.setProp("n", d0["n"] if "n" in d0 else n)
                            keyVals["pe"] = d0["pe"] if "pe" in d0 else 3
                            self.setProp("pe",keyVals["pe"])
                else: # no c, nor tn set tn to "" except for "on"
                    if self.lemma!="on": keyVals["tn"]=""
            ending=self.bestMatch(self.declension_word(),declension,keyVals)
            if ending is None:
                return [self.morphoError("decline [en]: N,D Pro", {"g": g, "n": n, "pe":pe})]
            self.realization = self.stem+ending
        if self.isA("N"):
            res = self.check_gender_lexicon(g, n)
            if res is not None: return res
            if n == "p":
                rescnt = self.check_countable()
                if rescnt is not None: return rescnt
        return [self]

    def removeNextConstInSentence(self):
        parentElems=self.parentConst.elements
        try:
            myIndex=parentElems.index(self)
            nextWord=parentElems[myIndex+1]
            del parentElems[myIndex+1]
            nextWord.realization=nextWord.realize()
            return nextWord
        except:
            return self.error("no parent for removeNextConstInSentence")
    
    # fill the realization field of a constituent
    # used heavily in conjugate_fr and conjugate_en       
    # insert a pyrealb terminal with its realization field already filled in a list of terminal
    # used heavily in conjugate_fr and conjugate_en
    def insertReal(self,terms,newTerminal,position=None):
        if isinstance(newTerminal,Terminal):
            newTerminal.parentConst=self.parentConst
            newTerminal.realize()
            if position is None:
                terms.append(newTerminal)
            else:
                terms.insert(position,newTerminal)
        else:
            from .utils import NO
            self.warn("bad Constituent",NO(position+1).dOpt({"ord":True}),type(newTerminal).__name__)
        return terms
    
    def isReflexive(self):
        if not self.isA("V"):
            return self.error("isReflexive() should be called only for a verb,  not a "+self.constType)
        if hasattr(self,"ignoreRefl"):return False # HACK: this might be set in Phrase.processTyp_fr when
                                                   # dealing with "progressive"
        pat=self.getProp("pat")
        if pat is not None and len(pat)==1 and pat[0]=="réfl": return True # essentiellement réflexif
        # check for "refl" typ (only called for V): Terminal.conjugate_fr
        pc=self.parentConst
        while pc is not None:
            # look for the first enclosing S, SP or Dependent with a terminal V
            if pc.isA("VP","SP","S") or (pc.isA(deprels) and pc.terminal.isA("V")):
                if "typ" in pc.props:
                    typs=pc.props["typ"]
                    if "refl" in typs and typs["refl"]==True:
                        if "réfl" not in pat:
                            self.ignoreRefl=True
                            if self.lemma not in ["avoir","être","pouvoir","devoir","vouloir"]:
                                self.warn("ignored reflexive",pat)
                            return False
                        return True
                if not pc.isA("VP"):  # unless it is VP stop at the first sentence
                    return False
            pc=pc.parentConst
        return False


    ### Number 
    ###   implementation differs from the JavaScript one using the Python format function
    ###    we avoid using locale...
    def numberFormatter(self,maxPrecision=None):
        if isinstance(self.value,int):
            precision=0
        else:
            precision = 2 if maxPrecision  is None else maxPrecision
        res=("{:,."+str(precision)+"f}").format(self.value)
        symbol = getRules(self.lang())["number"]["symbol"]
        if symbol["group"]!=",":res=res.replace(",",symbol["group"])
        if symbol["decimal"]!=".":res=res.replace(".",symbol["decimal"]) 
        return res
        
    def numberToWord(self):
        if not isinstance(self.value,int):
            self.warn("bad number in word",self.value)
            return str(self.value)
        one = self.numberOne()
        if one is not None:
            return one
        return enToutesLettres(self.value,self.lang())

    def numberToOrdinal(self):
        if not isinstance(self.value,int) or self.value<0:
            self.warn("bad ordinal",self.value)
            return f"[[{self.value}]]"
        return ordinal(self.value,self.lang(),self.peng["g"])

    def numberToRoman(self):
        if not isinstance(self.value,int) or self.value<0 or self.value>=4000:
            self.warn("bad roman",self.value)
            return f"[[{self.value}]]"
        return roman(self.value)

    ### Date
    def dateFormat(self,dateObj,dOpts):
        fmtRE=re.compile(r"(.*?)\[(.+?)]|(.+$)")
        dateRule = getRules(self.lang())["date"]
        fmts=dateRule["format"]["natural" if dOpts["nat"] else "non_natural"]

        def interpret(fields):
            if len(fields)==0:return ""
            res=""
            fmt=fmts[fields]
            if "det" in dOpts and not dOpts["det"]:
                fmt=fmt[fmt.index("["):] # remove determiner before the first left bracket
            for m in fmtRE.finditer(fmt):
                if m[1] is None:
                    res+=m[3]
                else:
                    res+=m[1]+{
                            "Y" :lambda:str(dateObj.year),
                            "F" :lambda:dateRule["text"]["month"][str(dateObj.month)],
                            "M0":lambda:f"{dateObj.month:02}",
                            "M" :lambda:str(dateObj.month),
                            "d0":lambda:f"{dateObj.day:02}",
                            "d" :lambda:str(dateObj.day),
                            "l" :lambda:dateRule["text"]["weekday"][(dateObj.weekday()+1)%7],
                            "A" :lambda:dateRule["text"]["meridiem"][0 if dateObj.hour<12 else 1],
                            "h" :lambda:str(dateObj.hour%12),
                            "H0":lambda:f"{dateObj.hour:02}",
                            "H" :lambda:str(dateObj.hour),
                            "m0":lambda:f"{dateObj.minute:02}",
                            "m" :lambda:str(dateObj.minute),
                            "s0":lambda:f"{dateObj.second:02}",
                            "s" :lambda:str(dateObj.second),
                        }[m[2]]()
            return res

        if isinstance(dOpts["rtime"],datetime.datetime):
            relativeDate = dateRule["format"]["relative_time"]
            # find the number of days of difference between relDay and the current date
            # use the "proleptic Gregorian ordinal number" to get the right number of days
            diffDays=dateObj.toordinal()-dOpts["rtime"].toordinal()
            if str(diffDays) in relativeDate: # within a week before or after
                dateS = relativeDate[str(diffDays)].replace("[l]",
                            dateRule["text"]["weekday"][(dateObj.weekday()+1)%7])
            else:
                ## more than a week
                sign="-" if diffDays<0 else "+"
                dateS = relativeDate[sign].replace("[x]",str(abs(diffDays)))
        else:
            ## process date fields
            dateS = interpret("-".join(field for field in ["year", "month", "date", "day"] if dOpts[field]))

        timeFields = ":".join(field for field in ["hour","minute","second"] if dOpts[field])
        if dOpts["nat"]:
            h = dateObj.hour
            m = dateObj.minute
            s = dateObj.second
            if timeFields == "hour:minute:second":
                if m==0 and s==0:
                    if h==0: timeFields = "0h"
                    elif h==12: timeFields = "12h"
                    else: timeFields = "hour"
                elif s==0 : timeFields = "hour:minute"
            elif timeFields == "hour:minute":
                if m==0: timeFields = "hour"
        timeS=interpret(timeFields)
        return " ".join(s for s in [dateS,timeS] if len(s)>0)



    def real(self):
        if self.isA("N","A"):
            if hasattr(self, "tab") and self.tab  is not None:
                return self.doFormat(self.decline(False))
        elif self.isA("Adv"):
            if hasattr(self, "tab") and self.tab  is not None:
                return self.doFormat(self.decline(False))
            elif self.realization is None:
                self.realization=self.lemma
        elif self.isA("C","P","Q"):
            if self.realization is None:
                self.realization=self.lemma
        elif self.isA("D","Pro"):
            if hasattr(self, "tab") and self.tab is not None:
                return self.doFormat(self.decline(True))
        elif self.isA("V"):
            return self.doFormat(self.conjugate())
        elif self.isA("DT"):
            self.realization=self.dateFormat(self.date,self.getProp("dOpt"))
        elif self.isA("NO"):
            if "dOpt" in self.props:
                self.setProp("n",self.grammaticalNumber())
                opts=self.getProp("dOpt")
                if "nat" in opts and opts["nat"]==True:
                    self.realization=self.numberToWord()
                elif "ord" in opts and opts["ord"]==True:
                    self.setProp("n","s")  # the number of an ordinal is always singular
                    self.realization=self.numberToOrdinal()
                elif "rom" in opts and opts["rom"]==True:
                    self.realization=self.numberToRoman()
                elif "raw" in opts and opts["raw"]==False:
                    self.realization=self.numberFormatter(opts["mprecision"])
                else: # opts["raw"]==True
                    self.realization=str(self.value)
            else:
                self.realization=str(self.value)
        else:
            self.error("Terminal.error:"+self.constType+"not implemented")
        return self.doFormat([self])
    
    def toSource(self,_indent=0):
        return f"{self.constType}(\"{self.lemma}\")"+super().toSource(_indent)

    def toJSON(self):
        res={"terminal":self.constType,"lemma":self.lemma}
        if self.parentConst is None or self.lang()!=self.parentConst.lang(): # only indicate when language changes
            res["lang"]=self.lang()
        # if len(self.props): # do not output empty props
        #     res["props"]=self.props
        res=self.addJSONprops(res)
        return res
    
    @classmethod
    def fromJSON(cls,constType,json,lang):
        from .utils import terminal
        if "lemma" in json:
            return terminal(constType,json["lemma"],lang).setJSONprops(json)
        else:
            print("Terminal.fromJSON: no lemma found in "+str(json))
        return cls
        
    def toDependent(self,depName=None):
        from .utils import dep,det
        # HACK: self.parentConst in changed during transformation to refer to the parent dependennt...
        isTopLevel = self.parentConst is None  # we save it to use it at the end
        if self.isA("D", "NO"):
            deprel=det(self)
        else:
            deprel= dep([self], "root" if depName is None else depName)
        if isTopLevel: deprel.cap(False)
        return deprel
