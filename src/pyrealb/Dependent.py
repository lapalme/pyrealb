from .Constituent import Constituent
from .Terminal import Terminal, N, A, Pro, D, Adv, V, P, C, DT, NO, Q
from .Phrase import Phrase, prepositionsList
from .Lexicon import getLexicon, getRules, currentLanguage
import sys

class Dependent(Constituent):
    def __init__(self, params, deprel, lang=None):
        super().__init__(deprel)
        if lang is None:
            self.lang = currentLanguage()
        elif lang in ["en", "fr"]:
            self.lang = lang
        else:
            self.lang = currentLanguage()
            self.warn("bad language", self.lang)
        self.terminal = Q("*terminal") # dummy terminal so that error messages can be issued
        if len(params)==0:
            self.warn("Dependent without params")
        params=list(params)
        if isinstance(params[0],Terminal):
            self.terminal=params.pop(0)
        else:
            self.warn("Dependent needs Terminal",type(params[0]).__name__)
            params.pop(0)
        self.terminal.parentConst=self
        if hasattr(self.terminal,"peng"):
            self.peng=self.terminal.peng
        if self.terminal.isA("V"):
            self.taux=self.terminal.taux
        params = [e for e in params if e != None]  # ignore None dependents
        # list of dependents to create the source of the parameters at the time of the call
        # self can be different from the dependents lists because of structure modifications
        self.dependentsSource = []
        self.dependents = []
        # add all dependents except the last to the list of dependents
        for i in range(0, len(params) - 1):
            d = params[i]
            if isinstance(d, Dependent):
                self.addDependent(d)
                self.dependentsSource.append(d)
            else:
                self.warn("bad Dependent", NO(i + 1).dOpt({"ord":True}), type(d).__name__+str(d))
        if len(params) > 0:
            # terminate the list with add which does other checks on the final list
            self.add(params[-1], None, True)

    def addDependent(self,dependent,position=None):
        if isinstance(dependent,Dependent):
            dependent.parentConst=self
            # add it to the list of dependents
            if position==None:
                self.dependents.append(dependent)
            elif isinstance(position,int) and position <= len(self.dependents) and position>=0:
                self.dependents.insert(position,dependent)
            else:
                self.warn("bad position", position, len(self.dependents))
        else:
            self.warn("bad Dependent", NO(position + 1).dOpt({"ord": True}), type(dependent).__name__)
        return self

    # remove a Dependent from this Dependent and return it
    def removeDependent(self, position):
        if isinstance(position, int) and 0 <= position < len(self.dependents):
            dependent = self.dependents.pop(position)
            dependent.parentConst = None
            return dependent
        return self.warn("bad position", position, len(self.dependents))

    def changeDeprel(self,newdep):
        if self.isA("coord"):
            for d in self.dependents:
                d.constType=newdep
        else:
            self.constType=newdep
        return self

    # find index of one of deprels taking into account possible coord starting from position start
    # returns -1 when not found
    def findIndex(self,test,start=0):
        for i in range(start,len(self.dependents)):
            d=self.dependents[i]
            if d.isA("coord") and len(d.dependents) and test(d.dependents[0]): return i
            if test(d):return i
        return -1

    def add(self,dependent,position=None,prog=None):
        if not isinstance(dependent,Dependent):
            return self.warn("bad Dependent","dernier" if self.isFr() else "last",type(dependent).__name__)
        if prog is None : # real call .add
            self.optSource+=f'.add({dependent.toSource()}{"" if position is None else (","+str(position))})'
        else:
            self.dependentsSource.append(dependent)
        self.addDependent(dependent,position)
        self.linkProperties()
        return self

    def me(self):
        args=[self.terminal]
        if hasattr(self,"dependents"):
            args+=self.dependents
        return f'{self.constType}({",".join([e.me() for e in args])})'

    def linkProperties(self):
        if len(self.dependents)==0:return self
        # loop over children to set the peng and taux to their head or subject
        # so that once a value is changed this change will be propagated correctly...
        headTerm=self.terminal
        if self.isA("coord"):
            # must create self.peng already because it might be used in the current dependents (for adjectives, attributes...)
            # the information will be computed at realization time (see Dependent.coordReal)
            self.peng={}
        for d in self.dependents:
            depTerm=d.terminal
            deprel=d.constType
            if deprel=="subj":
                if headTerm.isA("V"):
                    headTerm.peng=d.peng
            elif deprel=="det":
                if depTerm.isA("D"):
                    if hasattr(self,"peng"):
                        if hasattr(depTerm,"peng") and hasattr(depTerm.peng,"pe"): # save person (for possessives)
                            pe=depTerm.peng["pe"]
                            depTerm.peng=self.peng
                            depTerm.peng["pe"]=pe
                        else: #some strange determiner construct do not have peng
                            depTerm.peng=self.peng
                elif depTerm.isA("NO"):
                    headTerm.peng["n"]=depTerm.grammaticalNumber()
                    # gender agreement between a French numbeer and subject
                    depTerm.peng["g"]=headTerm.peng["g"]
                elif depTerm.isA("P") and depTerm.lemma=="de": # HACK: deal with specific case : det(P("de"),mod(D(...)))
                    if len(d.dependents)==1 and d.dependents[0].isA("mod") and d.dependents[0].terminal.isA("D"):
                        d.dependents[0].terminal.peng = self.peng
            elif deprel=="mod" or deprel=="comp":
                if depTerm.isA("A"):
                    depTerm.peng=self.peng
                    # check for an attribute of a copula with an adjective
                    if self.isFr() and headTerm.lemma in ["être", "paraître", "sembler", "devenir", "rester"]:
                        iSubj=self.findIndex(lambda d0:d0.isA("subj") and d0.terminal.isA("N"))
                        if iSubj>=0: depTerm.peng=self.dependents[iSubj].peng
                elif depTerm.isA("V"):
                    # set agreement between the subject of a subordinate or the object of a relative subordinate
                    iRel=d.findIndex(lambda d0:d0.isOneOf(["subj","comp","mod"]) and
                                                  d0.terminal.isA("Pro") and
                                                  d0.terminal.lemma in ["qui","que","who","that"])
                    if iRel>=0:
                        rel = d.dependents[iRel].constType
                        if rel=="subj": # verb agrees with this subject
                            depTerm.peng=self.peng
                        elif self.isFr():
                            depTerm.cod=headTerm
                    # check for past participle in French that should agree with the head
                    if self.isFr() and depTerm.getProp("t")=="pp":
                        depTerm.peng=self.peng
            elif deprel=="root":
                self.error("An internal root was found")
            elif deprel=="coord":
                if len(d.dependents)>0:
                    firstDep=d.dependents[0]
                    if firstDep.isA("subj"):
                        headTerm.peng=d.peng
                    elif firstDep.isOneOf(["mod","comp"]) and firstDep.terminal.isA("V"):
                        # consider this as coordination of verb sharing a subject (the current root)
                        for d0 in d.dependents:
                            d0.peng=self.peng
                            d0.terminal.peng=self.peng
            else:
                self.error("Strange dependent:"+d.constType)

    def setLemma(self,lemma,terminalTyp):
        self.error("***: should never happen: setLemma: called on a Dependent")
        return self

    def findGenderNumberPerson(self,andCombination):
        g="f"
        n="s"
        pe=3
        nb=0
        for i in range(0,len(self.dependents)):
            e=self.dependents[i].terminal
            if e.isOneOf(["NP","N","Pro","Q"]):
                nb += 1
                propG=e.getProp("g")
                if propG=="m" or propG=="x" or e.isA("Q"):g="m" # masculine if gender is unspecified
                if e.getProp("n")=="p":n="p"
                propPe=e.getProp("pe")
                if propPe != None and propPe<pe:pe=propPe
        if nb==0: g="m"
        elif nb>1 and n=="s" and andCombination:n="p"
        return {"g":g,"n":n,"pe":pe}

    # Dependency structure modification but that must be called in the context of the parentConst
    # because the pronoun depends on the role of the N in the sentence
    #         and its position can also change relatively to the verb
    def pronominalize_fr(self):
        mySelf = self
        if self.isA("subj"):
            if not self.terminal.isOneOf(["N", "Pro"]):
                return self.warn("no appropriate pronoun")
            pro = self.getTonicPro("nom")
        elif self.isOneOf(["comp", "mod"]) and self.terminal.isA("P"):
            prep = self.terminal.lemma
            if len(self.dependents) == 1 and self.dependents[0].isOneOf(["comp", "mod"]):
                if self.dependents[0].terminal.isA("N"):
                    n = self.dependents[0].terminal
                    if prep == "à":
                        pro = n.getTonicPro("dat")
                    elif prep == "de":
                        pro = Pro("en", "fr").c("dat")
                    elif prep in ["sur", "vers", "dans"]:
                        pro = Pro("y", "fr").c("dat")
                    else:  # change only the N keeping the P intact
                        pro = self.getTonicPro("nom")
                        mySelf = self.dependents[0]
                else:
                    return self.warn("no appropriate pronoun")
        else:
            pro = self.getTonicPro("acc")
            if self.parentConst != None and self.parentConst.terminal.isA("V"):  # consider that it is direct complement
                self.parentConst.terminal.cod = self  # indicate that self is a COD
        # replace the original with the pronoun
        pro.parentConst = self
        if hasattr(mySelf,"peng"):
            pro.peng = mySelf.peng
        mySelf.terminal = pro
        mySelf.dependents = []
        mySelf.dependentsSource = []

    # Pronominalization in English only applies to a N (self is checked before the call)
    #  and does not need reorganisation of the sentence
    #  Does not currently deal with "Give the book to her." that {c|sh}ould be "Give her the book."
    def pronominalize_en(self):
        self.props["pe"] = 3  # ensure that pronominalization of a noun is 3rd person
        if self.isA("subj"):  # is it a subject
            pro = self.getTonicPro("nom")
        else:
            pro = self.getTonicPro("acc")  # is direct complement
        pro.peng = self.peng
        pro.parentConst = self
        self.terminal = pro
        self.dependents = []
        self.dependentsSource = []

    # check if any child should be pronominalized
    # self must be done in the context of the parent, because some dependents might be changed
    def pronominalizeChildren(self):
        for d in self.dependents:
            if "pro" in d.props and not d.terminal.isA("Pro"):  # it can happen that a Pro has property "pro" set within the same expression
                if d.isFr():
                    d.pronominalize_fr()
                else:
                    if d.terminal.isA("N"):
                        d.pronominalize_en()
                    else:
                        self.warn("no appropriate pronoun")

    def passivate(self):
        subj=None # original subject and object, they are swapped below...
        obj=None
        # find the subject
        if self.terminal.isA("V"):
            subjIdx=self.findIndex(lambda d:d.isA("subj"))
            if subjIdx>=0:
                subj=self.dependents[subjIdx]
                if subj.terminal.isA("Pro"):
                    # as self pronoun will be preceded by "par" or "by", the "bare" tonic form is needed
                    # to which we assign the original person, number, gender
                    subj.terminal=subj.terminal.getTonicPro().g(subj.getProp("g"))\
                                            .n(subj.getProp("n")).pe(subj.getProp("pe"))
            else:
                subj=None
            # find direct object (first N or Pro of a comp) from dependents
            objIdx=self.findIndex(lambda d: d.isA("comp") and d.terminal.isOneOf(["N","Pro"]))
            if objIdx>=0:
                obj=self.dependents[objIdx]
                if obj.terminal.isA("Pro"):
                    obj.terminal=obj.terminal.getTonicPro("nom")
                elif obj.terminal.isA("N") and "pro" in obj.props:
                    obj=obj.getTonicPro("nom")
                # swap subject and object by changing their relation name !!!
                # HACK: obj is the new subject
                obj.changeDeprel("subj")
                # make the verb agrees with the new subject (in English only, French is dealt below)
                if self.isEn():
                    self.terminal.peng=obj.peng
                if subj is not None:   # the original subject is now the indirect object
                    subj.changeDeprel("mod")
                    self.removeDependent(subjIdx)
                    self.addDependent(comp(P("par" if self.isFr() else "by",self.lang),subj))
            elif subj is not None: # no object, but with a subject
                #create a dummy subject with a "il"/"it"
                obj=Pro("lui" if self.isFr() else "it",self.lang).c("nom") #HACK: obj is the new subject
                # add new subject at the front of the sentence
                self.addPre(obj)
                self.peng=obj.peng
                 # add original subject after the verb to serve as an object
                self.addDependent(comp(P("par" if self.isFr() else "by",self.lang),subj))
            if self.isFr():
                # do self only for French because in English self is done by processTyp_en
                # change verbe into an "être" auxiliary and make it agree with the newSubj
                # force person to be 3rd (number and tense will come from the new subject)
                verbe=self.terminal.lemma
                self.terminal.setLemma("être")
                self.terminal.pe(3)
                if self.getProp("t")=="ip":
                    self.t("s") # set subjonctive present tense for an imperativ
                pp = V(verbe,"fr").t("pp")
                if obj is not None: # self can be undefined when a subject is Q or missing
                    self.terminal.peng=obj.peng
                    pp.peng=obj.peng
                # insert the pp before the comp, so that it appears immediately after the verb
                #  calling addPost(pp) would not put it at the right place
                compIdx=self.findIndex(lambda d:d.isA("comp"))
                if compIdx==-1: compIdx=0
                self.addDependent(Dependent([pp],"*post*"),compIdx)
        else:
            return self.warn("not found","V","contexte passif" if self.isFr() else "passive context")

    def processV(self, types, key, action):
        if self.isA("coord"):
            for d in self.dependents:
                d.processV(types, action)
        elif self.terminal.isA("V"):
            if key in types and types[key] is not False:
                action(self, types[key])

    # add special internal dependencies (used only during realization)
    def addPre(self, terminals, position=None):
        if isinstance(terminals, Terminal):
            self.addDependent(Dependent([terminals], "*pre*"), position)
            return self
        for terminal in terminals:
            self.addDependent(Dependent([terminal], "*pre*"), position)
        return self

    def addPost(self, terminals):
        if isinstance(terminals, Terminal):
            self.addDependent(Dependent([terminals], "*post*"), 0)
            return self
        terminals.reverse()  # must add them in reverse order because of position 0
        for terminal in terminals:
            self.addDependent(Dependent([terminal], "*post*"), 0)
        return self

    def processTyp_fr(self, types):
        def progF(deprel, v):
            # insert "en train","de" (separate so that élision can be done...)
            # HACK::but do it BEFORE the pronouns created by .pro()
            origLemma = deprel.terminal.lemma
            deprel.terminal.setLemma(
                "être")  # change verb, but keep person, number and tense properties of the original...
            deprel.addPost([Q("en train"), Q("de"), V(origLemma).t("b")])
            deprel.terminal.isProg = v
        self.processV(types, "prog", progF)

        def modF(deprel, mod):
            rules = getRules()
            origLemma = deprel.terminal.lemma
            for key in rules["verb_option"]["modalityVerb"]:
                if (key.startswith(mod)):
                    deprel.terminal.setLemma(rules["verb_option"]["modalityVerb"][key])
                    break
            deprel.terminal.isMod = True
            newV = V(origLemma).t("b")
            if hasattr(deprel.terminal, "isProg"):  # copy progressive from original verb...
                newV.isProg = deprel.terminal.isProg
                del deprel.terminal.isProg
            deprel.addPost(newV)
        self.processV(types, "mod", modF)

        def negF(deprel, neg):
            if neg is True: neg="pas"
            deprel.terminal.neg2 = neg  # HACK: to be used when conjugating at the realization time
        self.processV(types, "neg", negF)

    def processTyp_en(self, types):
        # replace current verb with the list new words
        #  TODO: take into account the fact that there might be already a verb with modals...
        if ("contr" in types and types["contr"] is not False):
            # necessary because we want the negation to be contracted within the VP before the S or SP
            self.contraction = True
        words = Phrase.affixHopping(self.terminal, self.getProp("t"), getRules()["compound"], types)
        # the new root should be the last verb
        last = words.pop()
        if last.isA("Pro") and last.lemma == "myself":  # skip possible "myself" for reflexive verb
            self.addPost(last)
            last = words.pop()
        self.terminal = last
        self.addPre(words)

    def moveAuxToFront(self):
        auxIdx = self.findIndex(lambda d: d.isA("*pre*"))  # added by affixHopping
        if auxIdx >= 0:
            aux = self.dependents[auxIdx].terminal
            self.removeDependent(auxIdx)
            self.addPre(aux, 0)  # put auxiliary before

    def invertSubject(self):
        # in French : use inversion rule which is quite "delicate"
        # rules from https:#francais.lingolia.com/fr/grammaire/la-phrase/la-phrase-interrogative
        # if subject is a pronoun, invert and add "-t-" or "-"
        # if subject is a noun, the subject stays but add a new pronoun
        subjIdx = self.findIndex(lambda d: d.isA("subj"))
        if subjIdx >= 0:
            subj = self.dependents[subjIdx].terminal
            pro = None
            if subj.isA("Pro"):
                pro = self.removeDependent(subjIdx).terminal  # remove subject
            elif subj.isA("C"):
                pro = Pro("moi", "fr").c("nom").g("m").n("p").pe(3)  # create a "standard" pronoun, to be patched by cpReal
                subj.pronoun = pro  # add a flag to be processed by cpReal
            else:
                pro = Pro("moi", "fr").g(subj.getProp("g")).n(subj.getProp("n")).pe(3).c("nom")  # create a pronoun
            if self.terminal.isA("V"):
                self.addPost(pro)
                self.terminal.lier()

    def processTypInt(self,int_):
        sentenceTypeInt = getRules()["sentence_type"]["int"]
        intPrefix = sentenceTypeInt["prefix"]
        prefix = None  # to be filled later
        pp = None
        if int_ in ["yon", "how", "why", "muc"]:
            if self.isEn(): self.moveAuxToFront()
            else: self.invertSubject()
            prefix = intPrefix[int_]
        # remove a part of the sentence
        elif int_ in ["wos", "was"]:  # remove subject
            subjIdx = self.findIndex(lambda d: d.isA("subj"))
            if subjIdx >= 0:
                # insure that the verb at the third person singular,
                # because now the subject has been removed
                self.terminal.setProp("n", "s")
                self.terminal.setProp("pe", 3)
                self.removeDependent(subjIdx)
            prefix = intPrefix[int_]
        elif int_ in ["wod", "wad"]:  # remove direct object (first comp starting with N)
            for i in range(0, len(self.dependents)):
                d = self.dependents[i]
                if d.isA("comp") and d.terminal.isA("N"):
                    self.removeDependent(i)
            if self.isFr():  # check for passive subject starting with par
                parIdx = self.findIndex(
                    lambda d: d.isA("comp") and d.terminal.isA("P") and d.terminal.lemma == "par")
                if parIdx >= 0:
                    pp = self.dependents[parIdx].terminal
                    self.removeDependent(parIdx)  # remove the passive subject
            prefix = intPrefix[int_]
            if self.isEn():
                self.moveAuxToFront()
            else:
                self.invertSubject()
        elif int_ in ["woi", "wai", "whe", "whn"]:  # remove indirect object first comp or mod with a P as terminal
            remove = False
            prefix = intPrefix[int_]  # get default prefix
            for i in range(0, len(self.dependents)):
                d = self.dependents[i]
                if d.isOneOf(["comp", "mod"]) and d.terminal.isA("P"):
                    # try to find a more appropriate prefix by looking at preposition in the structure
                    prep = d.terminal.lemma
                    preps = prepositionsList[self.lang]
                    remove = False
                    if int == "whe":
                        if preps["whe"].has(prep): remove = True
                    elif int == "whn":
                        if preps["whn"].has(prep): remove = True
                    elif preps["all"].has(prep):  # "woi" | "wai"
                        # add the preposition in front of the prefix (should be in the table...)
                        prefix = prep + " " + (("whom" if int == "woi" else "what") if self.isEn()
                                               else ("qui" if int == "woi" else "quoi"))
                        remove = True
                    if remove:
                        self.removeDependent(i)
                        break
            if self.isEn():
                self.moveAuxToFront()
            else:
                self.invertSubject()
        else:
            self.warn("not implemented", "int:" + int_)
        if self.isFr() or (int_ != "yon"):   # add the interrogative prefix
            self.addPre(Q(prefix), 0)
        if pp != None:  # add "par" in front of some French passive interrogative
            self.addPre(pp, 0)
        if int_ == "wad":  # replace "que" by "quoi" for French passive wad
            self.dependents[1].terminal.lemma = "quoi"
        self.a(sentenceTypeInt["punctuation"], True)

    def processTyp(self, types):
        # pp=None # flag for possible pp removal for French wod or wad
        if "pas" in types and types["pas"] is not False:
            self.passivate()
        if self.isFr():
            if "contr" in types and types["contr"] is not False:
                self.warn("no French contraction")
            self.processTyp_fr(types)
        else:
            self.processTyp_en(types)
        if "int" in types and types["int"] is not False:
            self.processTypInt(types["int"])
        if "exc" in types and types["exc"] is True:
            self.a(getRules()["sentence_type"]["exc"]["punctuation"], True)
        return self

    def coordReal(self):
        res=[]
        # realize coordinated Dependents by adding ',' between all dependents except for the last
        # no check is done on the terminal, so
        #    if the terminal is Q(",") then all dependents are separated by a ","
        #    Q("and,") deal with the Oxford comma (i.e. a comma after all dependents even the last)
        last=len(self.dependents)-1
        if last==-1: return []
        if last==0: # coordination with only one element, ignore coordinate
            dep = self.dependents[0]
            res = dep.real()
            self.setProp("g",dep.getProp("g"))
            self.setProp("n",dep.getProp("n"))
            pe=dep.getProp("pe")
            self.setProp("pe",pe if pe!=None else 3)
            return self.doFormat(res) # process format for the CP
        # check that all dependents use the same deprel
        deprel=self.dependents[0].constType
        for j in range(0,last): #insert comma after each element
            dj=self.dependents[j]
            if not dj.isA(deprel):
                self.warn("inconsistent dependents within a coord",deprel,dj.constType)
            if j<last-1: dj.props["a"]=[","]
            res.extend(dj.real())
        # insert realisation of the terminal before last...
        res.extend(self.terminal.real())
        if not self.dependents[last].isA(deprel):
            self.warn("inconsistent dependents within a coord",deprel,self.dependents[last].constType)
        # insert last element
        res.extend(self.dependents[last].real())
        # compute the combined gender and number of the coordination once children have been realized
        selfCoord=self.terminal
        if selfCoord.isA("C"):
            andC="et" if self.isFr() else "and"
            gn=self.findGenderNumberPerson(selfCoord.lemma==andC)
            self.setProp("g",gn["g"])
            self.setProp("n",gn["n"])
            self.setProp("pe",gn["pe"])
            # for an inserted pronoun, we must override its existing properties...
            if  hasattr(selfCoord,"pronoun"):
                selfCoord.pronoun.peng=gn
                selfCoord.pronoun.props["g"]=gn["g"]
                selfCoord.pronoun.props["n"]=gn["n"]
                selfCoord.pronoun.props["pe"]=gn["pe"]
        elif not selfCoord.isA("Q"):
            # in some cases the coordination can be a quoted string (possibly empty)
            self.warn("bad parameter","C",selfCoord.constType)
        return res

    def depPosition(self):
        myPos = self.props["pos"] if "pos" in self.props else None
        if myPos=="pre": return "pre"
        pos="post" # default is post
        if self.isOneOf(["subj","det","*pre*"]) and myPos!="post":
            # subject and det are always pre except when specified
            pos="pre"
        elif self.isA("mod") and self.terminal.isA("A") and self.parentConst.terminal.isA("N"):
            # check adjective position with respect to a noun
            if self.isFr():
                pos=self.terminal.props["pos"] if "pos" in self.terminal.props else "post"
            else:
                pos="pre" # all English adjectives are pre
        elif self.isA("coord"):
            if myPos is not None:
                pos=myPos
            elif len(self.dependents)>0:
                pos=self.dependents[0].depPosition() #take the position of the first element of the coordination
        return pos

    def real(self):
        self.pronominalizeChildren()
        if "typ" in self.props:
            self.processTyp(self.props["typ"])
        # realize coordinations before anything elso to compute their final number and person
        for d in self.dependents:
            if d.isA("coord"):d.tokens=d.coordReal()
        before=[]
        after=[]
        # realize and order them by gathering the dependents that should appear before and after the terminal
        for d in self.dependents:
            if d.depPosition()=="pre":
                before += d.tokens if d.isA("coord") else d.real()
            else:
                after += d.tokens if d.isA("coord") else d.real()
        res=[*before,*self.terminal.real(),*after]
        return self.doFormat(res)

    # recreate a jsRealB expression
    # if indent is >=0 create an indented pretty-print (call it with 0 at the root)
    def toSource(self, indent=-1):
        if indent >= 0:
            indent = indent + len(self.constType) + 1
            sep = ",\n" + " " * indent
        else:
            sep = ","
        # create source of children
        deps=[self.terminal.toSource(indent)]+[e.toSource(indent) for e in self.dependentsSource]
        return f'{self.constType}({sep.join(deps)})' + super().toSource()

    def toJSON(self):
        res = {"dependent": self.constType,
               "terminal":self.terminal.toJSON()}
        if hasattr(self,"dependents"):
            res["dependents"]=[e.toJSON() for e in self.dependents]
        if len(self.props) > 0:  # do not output empty props
            res["props"] = self.props
        if self.parentConst is None or self.lang != self.parentConst.lang:  # only indicate when language changes
            res["lang"] = self.lang
        return res

    @classmethod
    def fromJSON(self, constType, json, lang):
        from .utils import fromJSON
        if "terminal" not in json:
            print("Dependent.fromJSON: no terminal found in Dependent:"+str(json))
        else:
            args=[fromJSON(json["terminal"],lang)]
            if "dependents" in json:
                if isinstance(json["dependents"], list):
                    args.extend([fromJSON(e, lang) for e in json["dependents"]])
                else:
                    print("Dependent.fromJSON dependents should be a list:" + str(json["elements"]))
            return Dependent(args, constType, lang).setJSONprops(json)

#  create Dependent instances
def root(*params): return Dependent(params,"root")
def subj(*params): return Dependent(params,"subj")
def det(*params): return Dependent(params,"det")
def mod(*params): return Dependent(params,"mod")

def comp(*params): return Dependent(params,"comp")
def compObj(*params): return Dependent(params,"comp")
def compObl(*params): return Dependent(params,"comp")

def coord(*params): return Dependent(params,"coord")

