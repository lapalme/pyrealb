import copy
import re,datetime,sys

from .Lexicon import getLexicon, getLemma, getRules, currentLanguage, load

defaultProps = {"en":{"g":"n","n":"s","pe":3,"t":"p"},             # language dependent default properties
                "fr":{"g":"m","n":"s","pe":3,"t":"p","aux":"av"}}

quoteOOV=False # TODO: make this settable globally

optionListMethods = ('a', 'b', 'ba', 'en')

deprels = ["root","subj","det","mod","comp","coord"] # list of implemented dependency relations

# regex for matching the first word in a generated string (ouch!!! it is quite subtle...) 
#  match index:
#     1-possible non-word chars and optional html tags
#     2-the real word 
#     3-the rest after the word  
sepWordREen=re.compile(r"((?:[^<\w'-]*(?:<[^>]+>)?)*)([\w'-]+)?(.*)")
# same as sepWordREen but the [\w] class is extended with French accented letters and cedilla
sepWordREfr=re.compile(r"((?:[^<\wàâéèêëîïôöùüç'-]*(?:<[^>]+>)?)*)([\wàâéèêëîïôöùüç'-]+)?(.*)",re.I)

# tables des positions des clitiques en français, tirées de
#    Choi-Jonin (I.) & Lagae (V.), 2016, « Les pronoms personnels clitiques », in Encyclopédie Grammaticale du Français,
#    en ligne : http:#encyclogram.fr

#  section 3.1.1. (http:#encyclogram.fr/notx/006/006_Notice.php#tit31)

proclitiqueOrdre = {  # page 11 du PDF
    # premier pronom que nous ignorons pour les besoins de cette application
    # "je":1, "tu":1, "il":1, "elle":1, "on":1, "on":1, "nous":1, "vous":1, "vous":1, "ils":1, "elle":1,
    "ne": 2,
    "me": 3, "te": 3, "se": 3, "nous": 3, "vous": 3,
    "le": 4, "la": 4, "les": 4,
    "lui": 5, "leur": 5,
    "y": 6,
    "en": 7,
    "*verbe*": 8,
    "pas": 9,  # S'applique aussi aux autre négations... plus, guère
}

proclitiqueOrdreImperatifNeg = {  # page 14 du PDF
    "ne": 1,
    "me": 2, "te": 2, "nous": 2, "vous": 2,
    "le": 3, "la": 3, "les": 3,
    "lui": 4, "leur": 4,
    "y": 5,
    "en": 6,
    "*verbe*": 7,
    "pas": 8,  # S'applique aussi aux autre négations... plus, guère
}

proclitiqueOrdreImperatifPos = {  # page 15 du PDF
    "*verbe*": 1,
    "le": 2, "la": 2, "les": 2,
    "lui": 3, "leur": 3,
    "me": 4, "te": 4, "nous": 2, "vous": 2,
    "y": 5,
    "en": 6,
}

proclitiqueOrdreInfinitif = {  # page 17 du PDF
    "ne": 1,
    "pas": 2,  # S'applique aussi aux autre négations... plus, guère, jamais
    "me": 3, "te": 3, "se": 3, "nous": 3, "vous": 3,
    "le": 4, "la": 4, "les": 4,
    "lui": 5, "leur": 5,
    "y": 6,
    "en": 7,
    "*verbe*": 8,
}

modalityVerbs = ["vouloir", "devoir", "pouvoir"]

# return a list of elements that are not None flattening embedded lists (used by Phrase and Dependent)
def _getElems(es):
    res = []
    for e in es:
        if e != None:
            if isinstance(e, (list,tuple)):res.extend([e0 for e0 in _getElems(e) if e0 != None])
            else:res.append(e)
    return res



class Constituent():
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

    #  unary plus to print the realization of a Constituent
    #  useful within a real-eval-print loop
    def __pos__(self):
        print(self.realize())

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
    
    def setProp(self,propName,val,inSetLemma=False):
        if propName in ["pe","n","g"] and hasattr(self,"peng") and self.peng is not None:
            self.peng[propName]=val
        if propName in ["t","aux"] and hasattr(self,"taux") and self.taux is not None:
            self.taux[propName]=val
        # this is important for to ensure that locol options override global values
        # but it must not be done at initialization for peng and taux in Terminal.setLemma
        if propName not in ["pe","n","g","t","aux"] or not inSetLemma:
            self.props[propName]=val

    # should be in Terminal.prototype... but here for consistency with three previous definitions
    pengNO=0 # useful for debugging: identifier of peng struct to check proper sharing in the debugger
    tauxNO=0 # useful for debugging: identifier of taux struct to check proper sharing in the debugger
   
    def initProps(self):
        if self.isOneOf(["N","A","D","V","NO","Pro","Q","DT"]):
            Constituent.pengNO+=1
            self.peng={"pe":defaultProps[self.lang]["pe"],
                       "n" :defaultProps[self.lang]["n"],
                       "g" :defaultProps[self.lang]["g"],
                       "pengNO":Constituent.pengNO}
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

    tonicForms = {
        "fr" : {"toi","lui","nous","vous","eux","elle","elles","on","soi"},
        "en" : {"us","her","you","him","them","it"}
    }
    # return a pronoun corresponding to this object
    # taking into account the current gender, number and person
    #  do not change the current pronoun, if it is already using the tonic form or does not have one (e.g. this)
    # if case_ is not given, return the tonic form else return the corresponding case
    # HACK:: parameter case_ is followed by _ so that it is not displayed as a keyword in the editor
    def getTonicPro(self,case_=None):
        from .Terminal import Pro
        if self.isA("Pro"): # this is already a pronoun
            if ("tn" in self.props or "c" in self.props): # already has tn() or c()
                if case_ is not None:
                    self.props["c"]=case_
                else: # ensure tonic form
                    self.props["tn"]=""
                    if "c" in self.props: del self.props["c"]
                return self
            else:
                if self.lemma in Constituent.tonicForms[self.lang]:
                    # the lemma is already in tonic form
                    if case_ is not None:
                        return Pro(self.lemma).c(case_)
                else:
                    if case_ is not None:
                        return Pro(self.realize()).c(case_)
                return self
        else: # generate the string corresponding to the tonic form
            pro=Pro("moi" if self.isFr() else "me",self.lang)
            g=self.getProp("g")
            if g is not None: pro.g(g)
            n=self.getProp("n")
            if n is not None: pro.n(n)
            pe=self.getProp("pe")
            if pe is not None: pro.pe(pe)
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
            self.optSource+=f'.tag("{name}",{str(attrs)})' # specila case of addOptionSource
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
        self.addOptSource("nat",isNat)
        if self.isOneOf(["DT","NO"]):
            if "dOpt" not in self.props:self.props["dOpt"]={}
            if isNat is None:
                self.props["dOpt"]["nat"]=True
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
              "int": [False,"yon","wos","wod","woi","was","wad","wai","whe","why","whn","how","muc","tag"]
        }
        self.addOptSource("typ",types)
        if not isinstance(types, dict):
            self.warn("ignored value for option",".typ",type(types).__name__+":"+str(types))
        elif not self.isOneOf(["S", "SP", "VP", *deprels]):
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
        # according to https://owl.english.purdue.edu/owl/resource/591/1/
        hAnRE=re.compile(r"^(heir|herb|honest|honou?r(able)?|hour)",re.I)
        # https://www.quora.com/Where-can-I-find-a-list-of-words-that-begin-with-a-vowel-but-use-the-article-a-instead-of-an
        uLikeYouRE=re.compile(r"^(uni.*|ub.*|use.*|usu.*|uv.*)",re.I)
        acronymRE=re.compile(r"^[A-Z]+$")
        # Common Contractions in the English Language taken from :http:#www.everythingenglishblog.com/?p=552
        contractionEnTable={
            "are+not":"aren't", "can+not":"can't", "did+not":"didn't", "do+not":"don't", "does+not":"doesn't",
            "had+not":"hadn't", "has+not":"hasn't", "have+not":"haven't", "is+not":"isn't", "must+not":"mustn't", 
            "need+not":"needn't", "should+not":"shouldn't", "was+not":"wasn't", "were+not":"weren't", 
            "will+not":"won't", "would+not":"wouldn't",
            "let+us":"let's",
            "I+am":"I'm", "I+will":"I'll", "I+have":"I've", "I+had":"I'd", "I+would":"I'd",
            "she+will":"she'll", "he+is":"he's", "he+has":"he's", "she+had":"she'd", "she+would":"she'd",
            "he+will":"he'll", "she+is":"she's", "she+has":"she's", "he+would":"he'd", "he+had":"he'd",
            "you+are":"you're", "you+will":"you'll", "you+would":"you'd", "you+had":"you'd", "you+have":"you've",
            "we+are":"we're", "we+will":"we'll", "we+had":"we'd", "we+would":"we'd", "we+have":"we've",
            "they+will":"they'll", "they+are":"they're", "they+had":"they'd", "they+would":"they'd", "they+have":"they've",
            "it+is":"it's", "it+will":"it'll", "it+had":"it'd", "it+would":"it'd",
            "there+will":"there'll", "there+is":"there's", "there+has":"there's", "there+have":"there've",
            "that+is":"that's", "that+had":"that'd", "that+would":"that'd", "that+will":"that'll",
            "what+is": "what's"
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
                if (re.match(r"^[ai]",w2,re.I) or   # starts with a or a i
                    (re.match(r"^e",w2,re.I) and not re.match(r"^eu",w2,re.I) or # starts with e but not eu
                     re.match(r"^o",w2,re.I) and not re.match(r"^onc?e",w2,re.I) or # starts with o but not one or once
                    re.match(r"^u",w2,re.I) and not uLikeYouRE.match(w2) or  # u does not sound like you
                    hAnRE.match(w2) or       # silent h
                    acronymRE.match(w2))):   # is an acronym
                        cList[i].realization=m1.group(1)+w1+"n"+m1.group(3)
                        i+=1                 # skip next word
            elif hasattr(self,"contraction") and self.contraction == True:
                if w1=="cannot": # special case...
                    cList[i].realization=m1.group(1)+"can't"+m1.group(3)
                else:
                    key=w1+"+"+w2
                    if key in contractionEnTable:
                        contr=contractionEnTable[key]
                        # do contraction of first word and remove second word (keeping start and end)
                        cList[i].realization=m1.group(1)+contr+m1.group(3)
                        cList[i+1].realization=m2.group(1)+m2.group(3).strip()
                        i+=1
            i+=1
        
    def doElisionFr(self,cList):
        # Elision rules for French
        # implements the obligatory elision rules of the "Office de la langue française du Québec"
        #    https://vitrinelinguistique.oqlf.gouv.qc.ca/21737/lorthographe/elision-et-apostrophe/elision-obligatoire
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
                    lexiconInfo=getLemma(lemma.lower()) # check with lower case
                    if lexiconInfo  is None: return True       # elide when unknown
                if pos not in lexiconInfo:pos=next(iter(lexiconInfo)) # try the first pos if current not found
                if pos in lexiconInfo and "h" in lexiconInfo[pos] and lexiconInfo[pos]["h"]==1: return False # h aspiré found
                return True
            return False

        contr=None
        last=len(cList)-1
        if last==0:return # do not try to elide a single word
        i=0
        while i < last:
            if i>0 and cList[i-1].getProp("lier") is not None: # ignore if the preceding word is "lié" to this one
                i+=1
                continue
            m1=sepWordREfr.match(cList[i].realization) if cList[i].realization is not None else None
            if m1  is None or m1.group(2) is None:
                i+=1
                continue
            m2=sepWordREfr.match(cList[i+1].realization) if cList[i].realization is not None else None
            if m2  is None or m2.group(2) is None:
                i+=1
                continue
            # HACK: m1 and m2 save the parts before and after the first word (w1 and w2) which is in m_i[2]
            # for a single word
            w1=m1.group(2)
            w2=m2.group(2)
            w3NoWords = not re.match(r"^\s*\w",m1.group(3)) # check that the rest of the first word does not start with a word
            elisionFound = False
            if isElidableFr(w2,cList[i+1].lemma,cList[i+1].constType):
                if elidableWordFrRE.match(w1) and w3NoWords:
                    cList[i].realization=m1[1]+w1[:-1]+"'"+m1[3]
                    elisionFound = True
                elif euphonieFrRE.match(w1) and  w3NoWords and cList[i].getProp("n")=="s": # euphonie
                    if re.match(r"ce",w1,re.I) and re.match(r"(^est$)|(^étai)|(^a$)",w2,re.I):
                        # very special case but very frequent
                        cList[i].realization=m1[1]+w1[:-1]+"'"+m1[3]
                    elif w2 not in ["et","ou","où","aujourd'hui"]:
                        # avoid euphonie before "et", "or" ....: e.g. "beau et fort" and not "bel et fort"
                        cList[i].realization=m1[1]+euphonieFrTable[w1]+m1[3]
                    elisionFound = True
            if elisionFound:
                i += 1
            elif (w1+"+"+w2) in contractionFrTable and w3NoWords:
                # try contraction
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


    def doFrenchPronounPlacement(self, cList):
        from .Terminal import Adv,Pro,Q
        iDeb = 0
        i = iDeb
        while i < len(cList):
            c = cList[i]
            if c.isA("V") and hasattr(c, "neg2"):
                if hasattr(c, "isMod") or hasattr(c, "isProg"):
                    if (c.getProp("lier")==None):
                        c.insertReal(cList, Q(c.neg2, "fr"), i + 2)
                    else:
                        c.insertReal(cList, Q(c.neg2, "fr"), i + 1)
                    c.insertReal(cList, Adv("ne", "fr"), i)
                    del c.neg2  # remove negation from the original verb
                    iDeb = i + 3  # skip these in the following loop
                    if hasattr(c, "isProg"): iDeb += 2  # skip "en train","de"
                    break
            i += 1
        # gather verb position and pronouns coming after the verb possibly adding a reflexive pronoun
        verbPos = None
        prog = None
        neg2 = None
        pros = []
        i = iDeb
        while i < len(cList):
            c = cList[i]
            if c.isA("V"):
                if verbPos is None:
                    if hasattr(c, "isProg") or hasattr(c, "isMod"):
                        if hasattr(c, "isProg"): prog = c
                        i += 1
                        continue
                    verbPos = i
                    # find the appropriate clitic table to use
                    t = c.getProp("t")
                    if t == "ip":
                        cliticTable = proclitiqueOrdreImperatifNeg if hasattr(c, "neg2") \
                            else proclitiqueOrdreImperatifPos
                    elif t == "b":
                        cliticTable = proclitiqueOrdreInfinitif
                    else:
                        cliticTable = proclitiqueOrdre
                    # check for negation
                    if hasattr(c, "neg2") and c.neg2 is not None:
                        c.insertReal(pros, Adv("ne", "fr"))
                        if t == "b":
                            c.insertReal(pros, Q(c.neg2, "fr"))
                        else:
                            neg2 = c.neg2
                            del c.neg2
                    if c.isReflexive() and c.getProp("t") != "pp":
                        if prog is not None: c = prog
                        c.insertReal(pros,
                                     Pro("moi", "fr").c("refl").pe(c.getProp("pe")).n(c.getProp("n")).g(c.getProp("g")))
                i += 1
            elif c.isA("Pro") and verbPos is not None:
                if c.getProp("pos") is None or (c.parentConst is not None and c.parentConst.getProp("pos") is None):
                    # do not try to change position of a constituent with specified pos
                    if c.getProp("c") in ["refl", "acc", "dat"] or c.lemma == "y" or c.lemma == "en":
                        pros.append(cList.pop(i))
                    elif c.lemma in ["qui","que","quoi","dont","où"]: # do not cross boundary of a relative
                        break
                    else:
                        i += 1
                else:
                    i += 1
            elif c.isOneOf(["P", "C", "Adv"]) and verbPos is not None:
                # HACK: stop when seeing a preposition or a conjunction
                #          or a "strange" pronoun that might start a phrase
                #       whose structure has been flattened at this stage
                if c.lemma == "par" and i<len(cList)-1 and cList[i+1].isA("Pro"):
                    # if "par"  followed by a Pro is encountered (probably for passive), keep them together
                    i += 2
                else:
                    break
            else:
                i += 1
        if verbPos is None: return
        # add ending "pas" after the verb unless it is "lié" in which cas it goes after the next word
        if neg2 is not None:
            vb = cList[verbPos]
            vb.insertReal(cList, Q(neg2, "fr"), verbPos + (1 if "lier" not in vb.props else 2))
        if len(pros) > 1:
            pros.sort(key=lambda pro: cliticTable[pro] if pro in cliticTable else 100)
        # insert pronouns before the verb
        cList[verbPos:verbPos] = pros

    #
    # In a VP, place the first consecutive adverbs at a correct position according to the rules of the language.
    # Usually an adverb is set according to either .pos("pre"|"post")
    # The problem occurs mainly with verbs with an auxiliary.
    # TODO: deal with more than one sequence of adverbs (although it should be rare)
    # this method is called by Phrase.real() and Dependent.real(), this is why it is moved to Constituent
    # @param {Terminal[]} res : list of Terminals possibly modified in place
    #
    def checkAdverbPos(self,res):
        # move n elements starting at start to position toIdx (shifting the rest)
        def moveTo(startIdx,n,toIdx):
            save = res[startIdx:startIdx+n]
            del res[startIdx:startIdx+n]
            res[toIdx:toIdx]=save

        relpron = ["that","who","which"] if self.isEn() else ["qui","que","dont","où"]
        # find the start of the current "sentence" in order not to move an adverb across the boundary of a relative
        start=len(res)-1
        while start>=0 and not (res[start].isA("Pro") and res[start].lemma in relpron):
            start -= 1
        start += 1
        # find first consecutive adverbs (ignoring "not" or "ne")
        advIdxes = [i for (i,e) in zip(range(start,len(res)),res[start:])
                                if e.isA("Adv") and e.lemma not in ["not","ne"] ]
        if len(advIdxes) == 0:
            return
        advIdx = advIdxes[0]
        advTerminal = res[advIdx]
        # check that the indexes of adverbs are consecutive, remove those that are not
        for i in range(1, len(advIdxes)):
            if advIdxes[i] != advIdxes[i - 1] + 1:
                del advIdxes[i:]
                break

        def moveAfterAux(auxMods):
            for auxIdx in range(0, advIdx - 1):
                e = res[auxIdx]
                if e.isA("V") and e.lemma in auxMods:
                    if res[auxIdx + 1].isA("V"):
                        if e.isFr() and res[auxIdx + 1].lemma in auxMods:
                            # another French modal ()
                            moveTo(advIdx,len(advIdxes),auxIdx+2)
                        else:
                            # there is an auxiliary/modals followed by a verb, insert adverb after the auxiliary
                            moveTo(advIdx, len(advIdxes), auxIdx + 1)
                    elif e.isEn():
                        # in English insert after negation (in French, negation [ne  ... pas] is added after this step)
                        if res[auxIdx + 1].lemma == "not" and res[auxIdx + 2].isA("V"):
                            moveTo(advIdx, len(advIdxes), auxIdx + 2)
                    else:
                        # in French
                        # check for infinitive verb (the adverb should go before it)
                        infinitiveFound = False
                        for idx in range(advIdx - 1, auxIdx, -1):
                            if "t" in res[idx].props and res[idx].props["t"] == "b":
                                moveTo(advIdx, len(advIdxes), idx)
                                infinitiveFound = True
                                break
                        if not infinitiveFound:
                            # check for inverted pronoun (added by .typ("int":"yon")
                            if res[auxIdx + 1].isA("Pro") and res[auxIdx + 2].isA("V"):
                                moveTo(advIdx, len(advIdxes), auxIdx + 2)
                    break

        if advIdx >= start+2 and "pos" not in advTerminal.props:
            # do not touch adverb with pos specified
            if advTerminal.isEn():
                # English: the adverb must be put after the first auxiliary
                moveAfterAux(["have", "can", "will", "shall", "may", "must"])
            else:
                # French : https:#fr.tsedryk.ca/grammaire/presentations/adverbes/4_La_place_de_l_adverbe.pdf (page 3)
                # place immediately after the auxiliary
                advLemma = advTerminal.lemma
                if advLemma.endswith("ment"): return;  # adverbe qui finit en -ment, laisser après le verbe
                #  adverbes de temps et de lieu qu'il faut laisser après le verbe
                #  extraits d'une liste de types d'adverbes à https:#www.scribbr.fr/elements-linguistiques/adverbe/
                tempsAdv = ["hier", "demain", "longtemps", "aujourd'hui", "tôt", "tard", "auparavant", "autrefois"]
                lieuAdv = ["ici", "là", "là-bas", "là-haut", "ailleurs", "autour", "derrière", "dessus", "dessous",
                           "devant",
                           "dedans", "dehors", "loin", "près", "alentour", "après", "avant", "partout",
                           "où", "partout", "au-dessus", "au-dessous", "au-devant", "nulle part", "quelque part"]
                if advLemma in tempsAdv or advLemma in lieuAdv: return
                if len(advLemma) <= 6 or advLemma in ["toujours", "souvent"]:
                    # adverbe court ou commun: déjà, très, trop, toujours, souvent ...
                    moveAfterAux(["avoir", "être", "vouloir", "devoir", "savoir"])

    # applies to a list of Constituents (can be a single one)
    # adds either to the first or last token (which can be the same)
    def doFormat(self,cList):
        punctuation=getRules(self.lang)["punctuation"]
        lex=getLexicon(self.lang)
    
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
        # reorder French pronouns within a VP
        if self.isFr() and (self.isA("VP") or (self.isOneOf(deprels) and self.terminal.isA("V"))):
            self.doFrenchPronounPlacement(cList)
            
        if self.isFr():
            self.doElisionFr(cList)
        else:
            self.doElisionEn(cList)
    
        if "cap" in self.props and self.props["cap"]!=False:
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
                    # C'est le cas, notamment, quand le verbe à la 3e personne du singulier du passé, du présent ou 
                    # du futur de l'indicatif se termine par une autre lettre que d ou t et qu'il est suivi 
                    # des pronoms sujets il, elle ou on. Dans ce cas, on ajoute un ‑t‑ entre le verbe 
                    # et le pronom sujet inversé.
                    if re.search(r"[^dt]$",terminal.realization) and re.match(r"[ieo]",terminals[i+1].realization):
                        s+="t-"
            elif re.search(r"[- ']$",terminal.realization):
                s+=terminal.realization
            elif len(terminal.realization)>0:
                s+=terminal.realization+" "
        s+=terminals[-1].realization
        # apply capitalization and final full stop unless .cap(False)
        if self.parentConst is None:
            if ((self.isOneOf(["S","root"])
                 or (self.isA("coord") and len(self.dependents)>0 and self.dependents[0].isA("root")))
                and len(s)>0): ## this is a top-level S
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
        return copy.deepcopy(self)
    
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
                        getattr(self, opt)(val)
                elif opt not in ["pat","h"]: # do not copy the pat or h properties of a verb
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
        if optionName is None: optionName = option
        if val is None:
            if validVals is not None and "" not in validVals:
                return self.warn("no value for option",option,validVals)
        if self.isOneOf("CP") and option not in ["cap","lier","pos"]:
            # propagate an option through the children of a CP except for "cap", "lier" and "pos"
            if prog is None:self.addOptSource(optionName,val)
            for e in self.elements:
                if len(allowedConsts)==0 or e.isOneOf(allowedConsts):
                    getattr(e,option)(val,True)  # do not add this option in the source
            return self
        if self.isA("coord") and option not in ["cap","lier","pos"]:
            # propagate an option through the head of the children of a coord except for "cap", "lier" and "pos"
            if prog is None: self.addOptSource(optionName, val)
            for e in self.dependents:
                if len(allowedConsts) == 0 or e.terminal.isOneOf(allowedConsts):
                    getattr(e.terminal, option)(val, True)  # do not add this option in the source
            return self
        if len(allowedConsts)==0 or self.isOneOf(allowedConsts) or self.isOneOf(deprels):
            if validVals is not None and val not in validVals:
                return self.warn("ignored value for option",option,val)
            # start of the real work
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
setattr(Constituent,"n",makeOptionMethod("n",["s","p","x"],["D","Pro","N","NP","A","AP","V","VP","S","SP","CP"]))
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

      