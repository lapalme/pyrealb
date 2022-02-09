from .Constituent import Constituent,quoteOOV
from .Number import enToutesLettres, ordinal
from .Lexicon import getLexicon,currentLanguage,getLemma,getRules

import datetime, sys,re,copy

class Terminal(Constituent):
    def __init__(self, terminalType,lemma,lang=None):
        super().__init__(terminalType)
        self.lemma=lemma # needed for error message
        if lang is None:
            self.lang=currentLanguage()
        elif lang in ["en","fr"]:
            self.lang=lang
        else:
            self.lang=currentLanguage()
            self.warn("bad language",self.lang)
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
            terminalType=type(self).__name__
        if isinstance(lemma, str):
            lemma=lemma.replace("œ","oe").replace("æ","ae")
        self.lemma=lemma
        if not hasattr(self, "peng"):self.initProps()
        if terminalType=="DT":
            if lemma is None or lemma=="":
                self.date=datetime.datetime.today()
            else:
                if isinstance(lemma,str):
                    self.date=self.parseDateString(lemma)
                elif isinstance(lemma,datetime.datetime):
                    self.date=lemma
                else:
                    self.warn("bad parameter","str,datetime.datetime",type(lemma).__name__)
                    self.date=datetime.datetime.today()                   
            self.lemma=str(self.date)
            ## set defaults
            self.props["dOpt"]={"year":True,"month":True,"date":True,"day":True,
                        "hour":True,"minute":True,"second":True,
                        "nat":True,"det":True,"rtime":False}
        elif terminalType=="NO":
            if not isinstance(lemma,(str,int,float)):
                self.warn("bad parameter",["str","int","float"],type(lemma).__name__)
                self.lemma=0
            elif isinstance(lemma,str):
                # check if this looks like a legal number
                if not re.match(r"^[-+]?[0-9]+([., ][0-9]*)?([Ee][-+][0-9]+)?$",lemma):
                    self.warn("bad parameter","number",type(lemma).__name__)
                    self.lemma=0
                else:
                    self.lemma=re.sub(r"," if self.isEn() else r" ","",self.lemma)
                try:
                    self.value=int(self.lemma)
                except ValueError:
                    self.value=float(self.lemma)
                self.nbDecimals=self.lemma[::-1].find(".")
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
                return self.warn("not in lexicon",self.lang)
                if quoteOOV:
                    self.lemma=str(lemma)
                    self.realization=self.lemma
                    self.constType="Q"
            else:
                if terminalType not in lexInfo:
                    self.tab=None 
                    self.realization=f"[[{lemma}]]"
                    return self.warn("not in lexicon",self.lang,lexInfo.keys())
                    if quoteOOV:
                        self.lemma=str(lemma)
                        self.realization=self.lemma
                        self.constType="Q"
                else:
                    lexInfo=lexInfo[terminalType]
                    rules=getRules()
                    for (key,info) in lexInfo.items():
                        if key=="tab": # save table number and compute stem
                            ending=None 
                            self.tab=info
                            if not self.isA("V"):
                                if self.tab in rules["declension"]: #  occurs for C, Adv and P
                                    declension=rules["declension"][self.tab]
                                    ending=declension["ending"]
                                    if terminalType=="Pro":
                                        #  set person for Pro when different than 3 (i.e. all elements of declension are the same)
                                        dd=declension["declension"]
                                        if "pe" in dd[0]:
                                            pe=dd[0]["pe"]
                                            if pe!=3:
                                                i=1
                                                while i<len(dd) and dd[i]["pe"]==pe:i+=1
                                                if i==len(dd):self.setProp("pe",pe)
                            else:
                                if self.tab in rules["conjugation"]:
                                    ending=rules["conjugation"][self.tab]["ending"]
                                else:
                                    ending=""
                                    self.warn("bad lexicon table",lemma,ending)
                            if ending!=None and self.lemma.endswith(ending):
                                self.stem=self.lemma if ending=="" else self.lemma[:-len(ending)]
                            else:
                                self.tab=None 
                                if not self.isOneOf(["Adv","C","P"]):
                                    self.warn("bad lexicon table",lemma,ending)
                        else:
                            # if isinstance(info,list) and len(info)==1:info=info[0]
                            self.setProp(key,info)
        else:
            self.warn("not implemented",terminalType)
    
    def grammaticalNumber(self):
        if not self.isA("NO"):
            return self.warn("bad application","grammaticalNumber","NO",self.constType)
        if "ord" in self.props and self.props["ord"]==True:
            return "s"
        number=self.value
        if self.isFr():
            # according to http:#bdl.oqlf.gouv.qc.ca/bdl/gabarit_bdl.asp?id=1582
            return "s" if -2<number<2 else "p"
        else:
            # according to https:#www.chicagomanualofstyle.org/book/ed17/part2/ch09/psec019.html
            #   any number other than 1 is plural... 
            # even 1.0 but this case is not handled here because nbDecimal(1.0)=>0
            return "s" if abs(number)==1 and self.nbDecimals==0 else "p"
    
    def getIndex(self,constTypes):
        if isinstance(constTypes, str):
            return 0 if self.isA(constTypes) else -1
        return 0 if self.isOneOf(constTypes) else -1
    
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
                                     
    def decline(self,setPerson):
        rules=getRules()
        declension=rules["declension"][self.tab]["declension"]
        stem=self.stem
        res=None 
        if self.isOneOf(["A","Adv"]):
            if self.isFr():
                g = self.getProp("g")
                n = self.getProp("n")
                ending=self.bestMatch("déclinaison d'adjectif", declension,{"g":g,"n":n})
                if ending is None:
                    return f"[[{self.lemma}]]"
                res=stem+ending
                f = self.getProp("f") # comparatif d'adjectif
                if f!=None and f != False:
                    specialFRcomp={"bon":"meilleur","mauvais":"pire"}
                    if f=="co":
                        if self.lemma in specialFRcomp:
                            return A(specialFRcomp[self.lemma]).g(g).n(n).realize()
                        else:
                            return "plus "+res
                    if f=="su":
                        art=D("le").g(g).n(n).realize()+" "
                        if self.lemma in specialFRcomp:
                            return art+A(specialFRcomp[self.lemma]).g(g).n(n).realize()
                        else:
                            return art+"plus "+res
            else: 
                # English adjective/adverbs are invariable but they can have comparative
                res=self.lemma
                f = self.getProp("f")
                if f!=None and f!=False:
                    if self.tab=="a1":
                        res=("more " if f=="co" else "most ")+res
                    else:
                        if self.tab=="b1": # adverb without comparative/superlative, try the adjective table
                            adjAdv=getLemma(self.lemma)
                            if "A" in adjAdv:
                                declension=rules["declension"][adjAdv["tab"]]["declension"]
                                ending=rules["declension"][adjAdv["tab"]]["ending"]
                                stem=stem[0:-len(ending)]
                            else:  # adverb without adjective
                                return res
                        # look in the adjective declension table
                        ending=self.bestMatch("adjective declension",declension,{"f":f})
                        if ending is None:
                            return f"[[{self.lemma}]]"
                        res=stem+ending
        elif len(declension)==1: # no declension
            res=stem+declension[0]["val"]
        else: # for N,D,Pro
            g=self.getProp("g")
            if self.isOneOf(["D","N"]) and g is None:g="m"
            n=self.getProp("n")
            if self.isOneOf(["D","N"]) and n is None:n="s"
            pe=3
            if setPerson:
                p=self.getProp("pe")
                pe=3 if p is None else int(p)
            keyVals={"pe":pe,"g":g,"n":n} if setPerson else {"g":g,"n":n}
            if "own" in self.props:
                keyVals["own"]=self.props["own"]
            if self.isA("Pro"):
                c  = self.props["c"] if "c" in self.props else None
                if c!= None:
                    if self.isFr() and c=="gen": # genitive cannot be used in French
                        self.warn("ignored value for option","c",c)
                    elif self.isEn() and c=="refl": # reflechi cannot be used in English
                        self.warn("ignored value for option","c",c)
                    else:
                        keyVals["c"]=c
                tn = self.props["tn"] if "tn" in self.props else None
                if tn != None:
                    if c!= None:
                        self.warn("both tonic and clitic")
                    else:
                        keyVals["tn"]=tn
                if c != None or tn != None:
                    if ((self.isFr() and self.lemma=="moi")) or  ((self.isEn() and self.lemma=="me")):
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
                        if self.isFr() or c != "gen":
                            self.setProp("g", d0["g"] if "g" in d0 else g)
                            self.setProp("n", d0["n"] if "n" in d0 else n)
                            keyVals["pe"] = d0["pe"] if "pe" in d0 else 3
                            self.setProp("pe",keyVals["pe"])
                else: # no c, nor tn set tn to "" except for "on"
                    if self.lemma!="on": keyVals["tn"]=""
            ending=self.bestMatch("déclinaison" if self.isFr() else "declension",declension,keyVals)
            if ending is None:
                return f"[[{self.lemma}]]"
            if self.isFr() and self.isA("N"):
                # check is French noun gender specified corresponds to the one given in the lexicon
                lexiconG=getLexicon()[self.lemma]["N"]
                if "g" not in lexiconG:
                    self.morphoError("absent du lexique",{"g":g,"n":n})
                    return f"[[{self.lemma}]]"
                lexiconG=lexiconG["g"]
                if lexiconG != "x" and lexiconG != g:
                    self.morphoError(
                        "genre différent de celui du lexique",{"g":g, "lexique":lexiconG})
                    return f"[[{self.lemma}]]"
            res=stem+ending
        return res

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
    # def constReal(self,cnst):
    #     cnst.realization=cnst.lemma if cnst.isA("Q") else cnst.realize()
    #     return cnst
    
    # insert a pyrealb terminal with its realization field already filled in a list of terminal
    # used heavily in conjugate_fr and conjugate_en
    def insertReal(self,terms,newTerminal,position=None):
        if isinstance(newTerminal,Terminal):
            newTerminal.parentConst=self.parentConst
            newTerminal.realize()
            if position==None:
                terms.append(newTerminal)
            else:
                terms.insert(position,newTerminal)
        else:
            self.warn("bad Constituent",NO(position+1).dOpt({"ord":True}),type(newTerminal).__name__)
        return terms
    
    def isReflexive(self):
        if not self.isA("V"):
            return self.error("isReflexive() should be called only for a verb,  not a "+self.constType)
        if hasattr(self,"ignoreRefl"):return False; #HACK: this might be set in Phrase.processTyp_fr when dealing with "progressive"
        pat=self.getProp("pat")
        if pat!=None and len(pat)==1 and pat[0]=="réfl": return True # essentiellement réflexif
        # check for "refl" typ (only called for V): Terminal.conjugate_fr
        pc=self.parentConst
        while pc is not None:
            if pc.isOneOf(["VP","SP","S"]):
                if "typ" in pc.props:
                    typs=pc.props["typ"]
                    if "refl" in typs and typs["refl"]==True:
                        if "réfl" not in pat:
                            self.ignoreRefl=True
                            if self.lemma not in ["avoir","être","pouvoir","devoir","vouloir"]:
                                self.warn("ignored reflexive",pat)
                            return False
                        return True
            pc=pc.parentConst
        return False

    
    def conjugate_fr(self):
        pe=int(self.getProp("pe"))
        g = self.getProp("g")
        n = self.getProp("n")
        t = self.getProp("t")
        neg=None 
        if self.tab is None:
            return [self.morphoError("conjugate_fr:tab",{"pe":pe,"n":n,"t":t})] 
        if t in ["pc","pq","cp","fa","spa","spq"]: # temps composés
            tempsAux={"pc":"p","pq":"i","cp":"c","fa":"f","spa":"s","spq":"si"}[t]
            aux=V("avoir","fr")
            aux.parentConst=self.parentConst
            aux.peng=self.peng
            aux.taux={"t":self.taux["t"],"aux":self.taux["aux"]} # separate tense of the auxiliary from the original
            if self.isReflexive():
                aux.setLemma("être")  # réflexive verbs must use French "être" auxiliary
                aux.setProp("pat",["réfl"]) # set reflexive for the auxiliary
            elif aux.taux["aux"]=="êt":
                aux.setLemma("être")
            else: # auxiliary "avoir"
                # check the gender and number of a cod appearing before the verb to do proper agreement of its part participle
                g="m"
                n="s"
                if hasattr(self,"cod"):
                    g=self.cod.getProp("g")
                    n=self.cod.getProp("n")
            aux.taux["t"]=tempsAux
            aux.realization=aux.realize()
            # change this verb to pp
            self.setProp("g",g)
            self.setProp("n",n)
            self.setProp("t","pp")
            self.realization=self.realize()
            if hasattr(self,"neg2"):
                aux.neg2=self.neg2 # save this flag to put on the auxiliary, 
                del self.neg2      # delete it on this verb
            if "lier" in self.props:
                aux.lier()         # put this flag on the auxiliary
                del self.props["lier"] # delete it from the verb
                # HACK: check if the verb was lié to a nominative pronoun (e.g. subject inversion for a question)
                myParent=self.parentConst
                if myParent != None:
                    myParentElems=myParent.elements
                    idxMe=myParentElems.index(self)
                    if idxMe>=0 and idxMe<len(myParentElems)-1:
                        idxNext=idxMe+1
                        next=myParentElems[idxNext]
                        if next.isA("Pro"):
                            thePro=myParentElems.pop(idxNext) # remove next pro from parent
                            thePro.realization=thePro.realize() # insert its realization after the auxiliary and before the verb
                            return [aux,thePro,self]
            return [aux,self]
        else: # simple tense
            conjugationTable=getRules()["conjugation"][self.tab]
            if "t" in conjugationTable and t in conjugationTable["t"]:
                conjugation=conjugationTable["t"]
                if t in ["p","i","f","ps","c","s","si"]:
                    term=conjugation[t][pe-1+(3 if n=="p" else 0)]
                    if term is None:
                        return [self.morphoError("conjugate_fr",{"pe":pe,"n":n,"t":t})]
                    else:
                        self.realization=self.stem+term
                    res=[self]
                    if self.parentConst is None and self.isReflexive():
                        self.insertReal(res, Pro("moi","fr").c("refl").pe(pe).n(n).g(g),0)
                    return res
                elif t=="ip":
                    if (n=="s" and pe!=2) or (n=="p" and pe==3):
                        return [self.morphoError("conjugate_fr",{"pe":pe,"n":n,"t":t})]
                    term=conjugation[t][pe-1+(3 if n=="p" else 0)]
                    if term is None:
                        return [self.morphoError("conjugate_fr",{"pe":pe,"n":n,"t":t})]
                    else:
                        self.realization=self.stem+term
                    res=[self]
                    if self.isReflexive() and self.parentConst==None:
                        self.lier()
                        self.insertReal(res,Pro("moi","fr").tn("").pe(pe).n(n).g(g))
                    return res
                elif t in ["b","pr","pp"]:
                    self.realization=self.stem+conjugation[t]
                    res=[self]
                    if t!="pp" and self.isReflexive() and self.parentConst==None:
                        self.insertReal(res, Pro("moi","fr").c("refl").pe(pe).n(n).g(g), 0)
                    if t=="pp" and self.realization!="été": # HACK: frequent case of être that does not change
                        g=self.getProp("g")
                        if g=="x":g="m"
                        n=self.getProp("n")
                        if n=="x":n="s"
                        term={"ms":"","mp":"s","fs":"e","fp":"es"}[g+n]
                        self.realization+=term
                    # neg=self.neg2 if hasattr(self,"neg2") else None
                    # if neg!=None and neg!="":
                    #     if t=="b" or t=="pp":
                    #         self.insertReal(res,Adv(neg,"fr"),0)
                    #     else:
                    #         self.insertReal(res,Adv(neg,"fr"))
                    return res
                else:
                    return [self.morphoError("conjugate_fr",{"pe":pe,"n":n,"t":t})]
            else:
                return [self.morphoError("conjugate_fr",{"pe":pe,"n":n,"t":t})]
    
    def conjugate_en(self):
        pe=int(self.getProp("pe"))
        n = self.getProp("n")
        t = self.getProp("t")
        if self.tab is None:
            return [self.morphoError("conjugate_en:tab",{"pe":pe,"n":n,"t":t})] 
        # subjonctive present is like present except that it does not end in s at 3rd person
        # subjonctive past is like simple past
        t1 = "p" if t=="s" else ("ps" if t=="si" else t)
        conjugationTable=getRules()["conjugation"][self.tab]
        res=[self]
        if "t" in conjugationTable and t1 in conjugationTable["t"]:
            conjugation=conjugationTable["t"][t1]
            if t in ["p","ps","s","si"]:
                if isinstance(conjugation,str):
                    self.realization=self.stem+conjugation
                    return [self]
                term=conjugation[pe-1+(3 if n=="p" else 0)]
                if term is None:
                    return [self.morphoError("conjugate_en:tab",{"pe":pe,"n":n,"t":t})]
                else:
                    # remove final s at subjonctive present by taking the form at the first person
                    if t=="s" and pe==3:term=conjugation[0]
                    self.realization=self.stem+term
                    return [self]
            elif t in ["b","pp","pr"]:
                self.realization=self.stem+conjugation
                return [self]
        elif t=="f":
            self.realization=self.lemma
            self.insertReal(res,Q("will"),0)
        elif t=="ip":
            self.realization=self.lemma
        else:
            return [self.morphoError("conjugate_en:tab",{"pe":pe,"n":n,"t":t})]
        return res 
        
                
    def conjugate(self):
        return self.conjugate_fr() if self.isFr() else self.conjugate_en()       

    ### Number 
    ###   implementation differes from the javascript one using format 
    ###    we avoid using locale...
    def numberFormatter(self,maxPrecision=None):
        if isinstance(self.value,int):
            precision=0
        else:
            precision = 2 if maxPrecision  is None else maxPrecision
        res=("{:,."+str(precision)+"f}").format(self.value)
        symbol = getRules()["number"]["symbol"]
        if symbol["group"]!=",":res=res.replace(",",symbol["group"])
        if symbol["decimal"]!=".":res=res.replace(".",symbol["decimal"]) 
        return res
        
    def numberToWord(self):
        if not isinstance(self.value,int):
            self.warn("bad number in word",self.value)
            return str(self.value)
        if self.isFr() and self.peng["g"]=="f":
            if self.value==1:return "une"
            if self.value==-1:return "moins une"
        return enToutesLettres(self.value,self.lang)

    def numberToOrdinal(self):
        if not isinstance(self.value,int) or self.value<0:
            self.warn("bad ordinal",self.value)
            return str(self.value)
        return ordinal(self.value,self.lang,self.peng["g"])
    
    ### Date
    def dateFormat(self,dateObj,dOpts):
        fmtRE=re.compile(r"(.*?)\[(.+?)\]|(.+$)")
        dateRule = getRules()["date"]
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
            diffDays=(dateObj-dOpts["rtime"]).days  # use datetime arithmetic to create timedelta
            if str(diffDays) in relativeDate: # within a week before or after
                return relativeDate[str(diffDays)].replace("[l]",
                            dateRule["text"]["weekday"][(dateObj.weekday()+1)%7])
            ## more than a week
            sign="-" if diffDays<0 else "+"
            return relativeDate[sign].replace("[x]",str(abs(diffDays)))
        
        ## process date fields
        dateS=interpret("-".join(field for field in ["year","month","date","day"] if dOpts[field]))
        timeS=interpret(":".join(field for field in ["hour","minute","second"] if dOpts[field]))
        return " ".join(s for s in [dateS,timeS] if len(s)>0)
     
    
    
    def real(self):
        if self.isOneOf(["N","A"]):
            if hasattr(self, "tab") and self.tab !=None:
                self.realization=self.decline(False)
        elif self.isA("Adv"):
            if hasattr(self, "tab") and self.tab !=None:
                self.realization=self.decline(False)
            else:
                self.realization=self.lemma
        elif self.isOneOf(["C","P","Q"]):
            if self.realization is None:
                self.realization=self.lemma
        elif self.isOneOf(["D","Pro"]):
            if hasattr(self, "tab") and self.tab !=None:
                self.realization=self.decline(True)
        elif self.isA("V"):
            return self.doFormat(self.conjugate())
        elif self.isA("DT"):
            self.realization=self.dateFormat(self.date,self.props["dOpt"])
        elif self.isA("NO"):
            if "dOpt" in self.props:
                opts=self.props["dOpt"]
                if "nat" in opts and opts["nat"]==True:
                    self.realization=self.numberToWord()
                elif "ord" in opts and opts["ord"]==True:
                    self.realization=self.numberToOrdinal()
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
        return f"{self.constType}(\"{self.lemma}\")"+super().toSource()

    def toJSON(self):
        res={"terminal":self.constType,"lemma":self.lemma}
        if self.parentConst is None or self.lang!=self.parentConst.lang: # only indicate when language changes
            res["lang"]=self.lang;
        if len(self.props): # do not output empty props
            res["props"]=self.props;
        return res;
    
    @classmethod
    def fromJSON(self,constType,json,lang):
        if "lemma" in json:
            return Terminal(constType,json["lemma"],lang).setJSONprops(json)
        else:
            print("Terminal.fromJSON: no lemma found in "+str(json))
        return self
        
    
# # create Terminal subclasses
#  which could be done using the following exec
# terminalDefString ='''
# class {0}(Terminal):
#     def __init__(self, lemma,lang=None):
#         super().__init__("{0}",lemma)
# '''
# for t in ["N","A","Pro","D","Adv","V","P","C","DT","NO","Q"]:
#     exec(terminalDefString.format(t))
#
# but we use the following in-line expansion of the above to avoid annoying error messages in Eclipse
class N(Terminal):
    def __init__(self, lemma=None,lang=None):
        super().__init__("N",lemma,lang)

class A(Terminal):
    def __init__(self, lemma=None,lang=None):
        super().__init__("A",lemma,lang)

class Pro(Terminal):
    def __init__(self, lemma=None,lang=None):
        super().__init__("Pro",lemma,lang)

class D(Terminal):
    def __init__(self, lemma=None,lang=None):
        super().__init__("D",lemma,lang)

class Adv(Terminal):
    def __init__(self, lemma=None,lang=None):
        super().__init__("Adv",lemma,lang)

class V(Terminal):
    def __init__(self, lemma=None,lang=None):
        super().__init__("V",lemma,lang)

class P(Terminal):
    def __init__(self, lemma=None,lang=None):
        super().__init__("P",lemma,lang)

class C(Terminal):
    def __init__(self, lemma=None,lang=None):
        super().__init__("C",lemma,lang)

class DT(Terminal):
    def __init__(self, lemma=None,lang=None):
        super().__init__("DT", lemma) 
            
class NO(Terminal):
    def __init__(self, lemma=None,lang=None):
        super().__init__("NO",lemma,lang)

class Q(Terminal):
    def __init__(self, lemma=None,lang=None):
        super().__init__("Q",lemma,lang)
