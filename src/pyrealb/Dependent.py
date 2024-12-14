from .Constituent import Constituent
from .Terminal import Terminal
from .Lexicon import getRules
from .utils import _getElems

class Dependent(Constituent):
    def __init__(self, params, deprel):
        from .utils import Q,NO
        super().__init__(deprel)
        self.terminal = Q("*terminal") # dummy terminal so that error messages can be issued
        if len(params)==0:
            self.warn("Dependent without params")
        params=list(params)
        if isinstance(params[0],Terminal):
            self.terminal=params.pop(0)
        elif isinstance(params[0],str):
            self.terminal=Q(params.pop(0))
        else:
            self.warn("Dependent needs Terminal",type(params[0]).__name__)
            params.pop(0)
        self.terminal.parentConst=self
        if hasattr(self.terminal,"peng"):
            self.peng=self.terminal.peng
        if self.terminal.isA("V"):
            self.taux=self.terminal.taux
        params = _getElems(params)  # flatten dependents and ignore None dependents
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
                self.warn("bad Dependent", NO(i + 2).dOpt({"ord":True}), type(d).__name__+":"+str(d))
        if len(params) > 0:
            # terminate the list with add which does other checks on the final list
            self.add(params[-1], None, True)

    def addDependent(self,dependent,position=None):
        from .utils import NO
        if isinstance(dependent,Dependent):
            dependent.parentConst=self
            # add it to the list of dependents
            if position is None:
                self.dependents.append(dependent)
            elif isinstance(position, int) and len(self.dependents) >= position >= 0:
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

    # return number of constituents
    def nbConstituents(self):
        return len(self.dependents)

    # return the list of constituents
    def constituents(self):
        return self.dependents

    def add(self,dependent,position=None,prog=None):
        if not isinstance(dependent,Dependent):
            return self.warn("bad Dependent",self.word_last(),type(dependent).__name__)
        if prog is None : # real call .add
            self.optSource+=f'.add({dependent.toSource()}{"" if position is None else (","+str(position))})'
        else:
            self.dependentsSource.append(dependent)
        self.addDependent(dependent,position)
        self.linkProperties()
        return self

    def remove(self,position):
        import re
        elem = self.removeDependent(position)
        if elem is not self: # removeDependent did not raise a warning
            src = elem.toSource().replace("(","\\(").replace(")","\\)")
            srcRE = r"\.add\("+src+r"(,\d+)?\)"
            if re.search(srcRE, self.optSource) is not None:
                self.optSource=re.sub(srcRE,"",self.optSource,1)
            else:
                self.dependentsSource.remove(position)
        return self

    def me(self):
        args=[self.terminal]
        if hasattr(self,"dependents"):
            args+=self.dependents
        return f'{self.constType}({",".join([e.me() for e in args])})'

    def setPengRecursive(self,oldDep,oldPengNO,newPeng):
        oldDep.peng = newPeng
        # check if terminal and children of oldDep have the same oldPengNO and change it to the newPeng
        if hasattr(oldDep.terminal,"peng") and oldDep.terminal.peng["pengNO"] == oldPengNO:
            oldDep.terminal.peng=newPeng
        for d in oldDep.dependents:
            self.setPengRecursive(d,oldPengNO,newPeng)


    def linkProperties(self):
        if len(self.dependents)==0:return self
        # loop over children to set the peng and taux to their head or subject
        # so that once a value is changed this change will be propagated correctly...
        headTerm=self.terminal
        if self.isA("coord"):
            # must create self.peng already because it might be used in the current dependents (for adjectives, attributes...)
            # the information will be computed at realization time (see Dependent.coordReal)
            Constituent.pengNO += 1
            self.peng={"pengNO":Constituent.pengNO}
            headTerm.peng = self.peng
        for dep in self.dependents:
            depTerm=dep.terminal
            deprel=dep.constType
            if deprel=="subj":
                if headTerm.isA("V"):
                    headTerm.peng=dep.peng
            elif deprel=="det":
                if depTerm.isA("D"):
                    if hasattr(self,"peng"):
                        depTerm.peng=self.peng
                    self.check_determiner_cnt(depTerm)
                elif depTerm.isA("NO"):
                    depTerm.peng=headTerm.peng
                elif depTerm.isA("P") and depTerm.lemma == "de":  # HACK: deal with specific case : det(P("de"),mod(D(...)))
                    if len(dep.dependents)==1 and dep.dependents[0].isA("mod") and dep.dependents[0].isA("D"):
                        dep.dependents[0].terminal.peng = self.peng
            elif deprel=="mod" or deprel=="comp":
                if depTerm.isA("A") or (depTerm.isA("V") and depTerm.getProp("t")=="pp"):
                    if hasattr(self,"peng"):
                        depTerm.peng=self.peng
                    self.linkAttributes(depTerm,headTerm)
                elif depTerm.isA("V"):
                    # set agreement between the subject of a subordinate or the object of a relative subordinate
                    iRel=dep.findIndex(lambda depI: depI.isA("subj", "comp", "mod") and
                                                    depI.terminal.isA("Pro") and
                                                    depI.terminal.lemma in self.relative_pronouns())
                    if iRel>=0:
                        rel = dep.dependents[iRel].constType
                        if rel=="subj": # verb agrees with this subject
                            depTerm.peng=self.peng
                        self.link_pp_before(dep,headTerm)
                    self.link_pp_with_head(depTerm)
                elif depTerm.isA("Pro") and depTerm.lemma in self.relative_pronouns_propagate():
                    # a relative linked to depTerm in which the new peng should be propagated
                    if hasattr(self,"peng"):
                        depTerm.peng=self.peng
                    for depI in dep.dependents:
                        if hasattr(depI,"peng") and hasattr(self,"peng"):
                            self.setPengRecursive(depI,depI.peng["pengNO"],self.peng)
                continue
            elif deprel=="root":
                # self.error("An internal root was found")
                pass
            elif deprel=="coord":
                depKinds = [d for d in dep.dependents if not d.isA("C")]
                if len(depKinds)>0:
                    firstDep=depKinds[0]
                    if firstDep.isA("subj"):
                        dep.peng = self.peng
                    elif firstDep.isA("det"):
                        dep.peng=headTerm.peng
                    elif firstDep.isA("mod","comp") and firstDep.terminal.isA("V","A"):
                        # consider this as a coordination of verb sharing a subject (the current root)
                        #            or as a coordination of adjectives
                        if hasattr(headTerm,"peng"):
                            dep.peng = headTerm.peng
                            for depI in dep.dependents:
                                depI.peng=headTerm.peng
                                depI.terminal.peng=headTerm.peng
            elif deprel in ["*pre*","*post*"]:
                pass
            else:
                self.error("Strange dependent:"+deprel)
        return

    def setLemma(self,_lemma,_terminalTyp):
        self.error("***: should never happen: setLemma: called on a Dependent")
        return self

    def findGenderNumberPerson(self,andCombination):
        g=None
        n=None
        pe=3
        nb=0
        for i in range(0,len(self.dependents)):
            e=self.dependents[i].terminal
            if e.isA("NP","N","Pro","Q","NO"):
                nb += 1
                propG=e.getProp("g")
                if g is None and propG is not None: g=propG
                if propG=="m": g="m" # masculine if one masculine is encountered
                if e.getProp("n")=="p":n="p"
                propPe=e.getProp("pe")
                if propPe is not None and propPe<pe:pe=propPe
        if nb>1 and andCombination:n="p"
        return {"g":g,"n":n,"pe":pe}

    # check if any child should be pronominalized
    # self must be done in the context of the parent, because some dependents might be changed
    def pronominalizeChildren(self):
        for d in self.dependents:
            if d.getProp("pro") and not d.terminal.isA("Pro"):  # it can happen that a Pro has property "pro" set within the same expression
                d.pronominalize()

    def passivate(self):
        from .utils import Pro,P,comp
        subj=None # original subject and object, they are swapped below...
        obj=None
        # find the subject
        if self.terminal.isA("V"):
            subjIdx=self.findIndex(lambda d:d.isA("subj"))
            if subjIdx>=0:
                subj=self.dependents[subjIdx]
                # if subj.terminal.isA("Pro"):
                #     subj.terminal = subj.terminal.getTonicPro()
                subject = subj.terminal
                if subject.isA("Pro"):
                    subject = self.passive_pronoun_subject(subject)
            else:
                subj=None
            # find direct object (first N or Pro of a comp) from dependents
            objIdx=self.findIndex(lambda d: d.isA("comp") and d.terminal.isA("N","Pro"))
            if objIdx>=0:
                obj=self.dependents[objIdx]
                if obj.terminal.isA("Pro"):
                    obj.terminal=obj.terminal.getTonicPro("nom")
                elif obj.terminal.isA("N") and obj.getProp("pro"):
                    obj=obj.getTonicPro("nom")
                # swap subject and object by changing their relation name !!!
                # HACK: obj is the new subject
                obj.changeDeprel("subj")
                # make the verb agrees with the new subject (in English only, French is dealt below)
                if self.passive_should_link_subject():
                    self.terminal.peng=obj.peng
                if subj is not None:   # the original subject is now the indirect object
                    subj.changeDeprel("mod")
                    self.removeDependent(subjIdx)
                    prep = self.passive_prep(subj.terminal.isA("V"))
                    self.addDependent(comp(P(prep,self.lang()),subj))
            elif subj is not None: # no object, but with a subject
                # create a dummy subject with "il"/"it"
                obj=Pro(self.passive_dummy_subject(),self.lang()).c("nom") #HACK: obj is the new subject
                # add new subject at the front of the sentence
                subj.changeDeprel("mod")
                self.removeDependent(subjIdx)
                self.addPre(obj)
                self.peng=obj.peng
                # add original subject after the verb to serve as an object
                prep = self.passive_prep(subj.terminal.isA("V"))
                self.addDependent(comp(P(prep,self.lang()),subj))
            self.passive_agree_auxiliary(obj)
        else:
            return self.warn("not found","V",self.passive_context())

    def processV(self, types, key, action):
        if self.isA("coord"):
            for d in self.dependents:
                d.processV(types, action)
        elif self.terminal.isA("V"):
            if key in types and types[key] is not False:
                action(self, types[key])

    # add special internal dependencies (used only during realization)
    def addPre(self, terminals, position=None):
        from .utils import dep
        if isinstance(terminals, Terminal):
            self.addDependent(dep([terminals], "*pre*"), position)
            return self
        for terminal in terminals:
            self.addDependent(dep([terminal], "*pre*"), position)
        return self

    def addPost(self, terminals):
        from .utils import dep
        if isinstance(terminals, Terminal):
            self.addDependent(dep([terminals], "*post*"), 0)
            return self
        terminals.reverse()  # must add them in reverse order because of position 0
        for terminal in terminals:
            self.addDependent(dep([terminal], "*post*"), 0)
        return self


    def processTypInt(self,types):
        from .utils import Q
        int_=types["int"]
        sentenceTypeInt = getRules()["sentence_type"]["int"]
        intPrefix = sentenceTypeInt["prefix"]
        prefix = None  # to be filled later
        pp = None
        if int_ in ["yon", "how", "why", "muc"]:
            self.move_object(int_)
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
            cmp=None
            i=0
            while i<len(self.dependents) and cmp is None:
                d = self.dependents[i]
                if d.isA("comp") and d.terminal.isA("N","Pro"):
                    cmp=self.removeDependent(i)
                i+=1
            pp = self.check_passive_subject_with_par()
            if self.passive_human_object(int_,cmp):
                # human direct object
                prefix = "whom"
            else:
                prefix = intPrefix[int_]
            self.move_object(int_)
        elif int_ in ["woi", "wai", "whe", "whn"]:  # remove indirect object first comp or mod with a P as terminal
            prefix = intPrefix[int_]  # get default prefix
            for i in range(0, len(self.dependents)):
                d = self.dependents[i]
                if d.isA("comp", "mod") and d.terminal.isA("P"):
                    # try to find a more appropriate prefix by looking at preposition in the structure
                    prep = d.terminal.lemma
                    preps = self.preposition_list()
                    remove = False
                    if int == "whe":
                        if preps["whe"].has(prep): remove = True
                    elif int == "whn":
                        if preps["whn"].has(prep): remove = True
                    elif preps["all"].has(prep):  # "woi" | "wai"
                        prefix = prep + " " + self.interrogative_pronoun_woi(int_)
                        remove = True
                    if remove:
                        self.removeDependent(i)
                        break
            self.move_object(int_)
        elif int_=="tag":
            self.tag_question(types)
            prefix=intPrefix[int_]
        else:
            self.warn("not implemented", "int:" + int_)
        if self.should_add_interrogative_prefix(int_):
            self.addPre(Q(prefix), 0)
        if pp is not None:  # add "par" in front of some French passive interrogative
            self.addPre(pp, 0)
            if int_ == "wad":  # replace "que" by "quoi" for French passive wad
                self.dependents[1].terminal.lemma = "quoi"
        self.a(sentenceTypeInt["punctuation"], True)

    def processTyp(self, types):
        # pp=None # flag for possible pp removal for French wod or wad
        if "pas" in types and types["pas"] is not False:
            self.passivate()
        self.processTyp_verb(types)
        if "int" in types and types["int"] is not False:
            self.processTypInt(types)
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
            self.setProp("pe",pe if pe is not None else 3)
            return self.doFormat(res) # process format for the CP
        # check that all dependents use the same deprel
        # except if a dependent is another coord
        deprel=self.dependents[0].constType
        noConnect = self.terminal.lemma == ""
        for j in range(0,last): #insert comma after each element
            dj=self.dependents[j]
            if noConnect or j<last-1:
                if "a" not in dj.props or "," in dj.props["a"]:
                    dj.props["a"]=[","]
            if dj.isA("coord"):
                res.extend(dj.coordReal())
            elif not dj.isA(deprel) and deprel != "coord":
                self.warn("inconsistent dependents within a coord",deprel,dj.constType)
            else:
                res.extend(dj.real())
        # insert realisation of the terminal before last...
        res.extend(self.terminal.real())
        lastD = self.dependents[last]
        if lastD.isA("coord"):
            res.extend(lastD.coordReal())
            return self.doFormat(res)
        elif not lastD.isA(deprel) and deprel != "coord":
            self.warn("inconsistent dependents within a coord",deprel,self.dependents[last].constType)
        # insert last element
        res.extend(self.dependents[last].real())
        # compute the combined gender and number of the coordination once children have been realized
        # CAUTION: gender and person might not be correct in the case of embedded coord
        selfCoord=self.terminal
        if selfCoord.isA("C"):
            andC = self.and_conj()
            gn=self.findGenderNumberPerson(selfCoord.lemma==andC)
            if gn["g"] is not None:
                self.setProp("g",gn["g"])
            if gn["n"] is not None:
                self.setProp("n",gn["n"])
            self.setProp("pe",gn["pe"])
            # for an inserted pronoun, we must override its existing properties...
            if  hasattr(selfCoord,"pronoun"):
                selfCoord.pronoun.peng=gn
                selfCoord.pronoun.props["g"]=gn["g"] if gn["g"] is not None else "m"
                selfCoord.pronoun.props["n"]=gn["n"]
                selfCoord.pronoun.props["pe"]=gn["pe"]
        elif not selfCoord.isA("Q"):
            # in some cases the coordination can be a quoted string (possibly empty)
            self.warn("bad parameter","C",selfCoord.constType)
        return self.doFormat(res)

    def depPosition(self):
        if "pos" in self.props: return self.props["pos"]
        pos="post" # default is post
        if self.isA("subj","det","*pre*"):
            # subject and det are always pre except when specified
            pos="pre"
        elif self.isA("mod") and self.terminal.isA("A") and self.parentConst.terminal.isA("N"):
            pos = self.terminal.props["pos"] if "pos" in self.terminal.props else self.adj_def_pos()
        elif self.isA("coord") and len(self.dependents)>0:
            pos=self.dependents[0].depPosition() #take the position of the first element of the coordination
        return pos

    def real(self):
        if self.isA("coord") and self.parentConst is None:
            # special case of coord at the root
            res=self.coordReal()
        else:
            self.pronominalizeChildren()
            if "typ" in self.props:
                self.processTyp(self.props["typ"])
            # realize "coord"s before the rest because it can change gender and number of subject
            # save their realization
            coordReals = [d.coordReal() for d in self.dependents if d.isA("coord")]
            # move all "pre" dependents at the front
            # HACK: we must move these in place because realization might remove some of them
            nextPre = 0
            for i in range(0,len(self.dependents)):
                d = self.dependents[i]
                if d.depPosition()=="pre":
                    if nextPre != i:
                        save = self.dependents[i]
                        del self.dependents[i]
                        self.dependents[nextPre:nextPre] = [save]
                    nextPre += 1
            # realize dependents
            if len(self.dependents) == 0:
                res = self.terminal.real()
            elif nextPre == 0:  # no pre
                res = self.terminal.real()
                for d in self.dependents:
                    res.extend(coordReals.pop(0) if d.isA("coord") else d.real())
            else:
                res = []
                i=0
                # cannot use "for i in range()" because dependents list might change during realization
                while i<len(self.dependents):
                    d = self.dependents[i]
                    res.extend(coordReals.pop(0) if d.isA("coord") else d.real())
                    if i == nextPre-1:
                        res.extend(self.terminal.real())
                    i += 1
            if self.terminal.isA("V"):
                self.checkAdverbPos(res)
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
        return f'{self.constType}({sep.join(deps)})' + super().toSource(indent)

    def toJSON(self):
        res = {"dependent": self.constType,
               "terminal":self.terminal.toJSON()}
        if hasattr(self,"dependents"):
            res["dependents"]=[e.toJSON() for e in self.dependents]
        # if len(self.props) > 0:  # do not output empty props
        #     res["props"] = self.props
        res = self.addJSONprops(res)
        if self.parentConst is None or self.lang() != self.parentConst.lang():  # only indicate when language changes
            res["lang"] = self.lang()
        return res

    @classmethod
    def fromJSON(cls, constType, json, lang):
        from .utils import fromJSON, dep
        if "terminal" not in json:
            print("Dependent.fromJSON: no terminal found in Dependent:"+str(json))
        else:
            args=[fromJSON(json["terminal"],lang)]
            if "dependents" in json:
                if isinstance(json["dependents"], list):
                    args.extend([fromJSON(e, lang) for e in json["dependents"]])
                else:
                    print("Dependent.fromJSON dependents should be a list:" + str(json["elements"]))
            return dep(args, constType, lang).setJSONprops(json)
