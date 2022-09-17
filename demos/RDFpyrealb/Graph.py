from Realize import getPrecedence, predicateGroups, groupTerms
from Realize import  S, SP, C, CP, NP, VP, V, Q, Pro, q, getSentPatterns, getDefaultPattern, hasPattern, isHuman
from rqDBPedia import isA, getGender
# nodes of the graph
from Node import Node

import random

class Graph:
    """Graph creation from triples """
    def __init__(self, category,triples,sortPred):
        self.category=category
        self.subjects = [] # [Node]
        text2Node={} # {string:Node}
        if sortPred:
            triples=sorted(triples,key=lambda t:getPrecedence(t.p))
        for i in range(0,len(triples)):
            triple=triples[i]
            # print(triple.flat_triple())
            subj=triple.s
            if subj in text2Node:
                subjNode=text2Node[subj]
            else:
                subjNode=Node(subj)
                text2Node[subj]=subjNode
            if subjNode not in self.subjects:
                self.subjects.append(subjNode)
            obj=triple.o
            if obj in text2Node:
                objNode=text2Node[obj]
            else:
                objNode=Node(obj)
                text2Node[obj]=objNode
            subjNode.addPredObj(triple.p,objNode)
        if len(self.subjects)>1:
            self.subjects.sort(reverse=True,
                               key=lambda node:len(node.predObj)+\
                                   ## force starting with the subject being of the right category
                                   (len(triples) if isA(node.subj,category) else 0))
    
    def __str__(self):
        return "{"+",\n ".join(str(node) for node in self.subjects)+"}"
            
    def getSubjects(self):
        return [n.subj for n in self.subjects]
    
    def getNode(self,lemma):
        for node in self.subjects:
            if node.subj==lemma:return node
        return None
    
    def delNode(self,lemma):
        for i in range(0,len(self.subjects)):
            if self.subjects[i].subj==lemma:
                del self.subjects[i]
                return
    
    def show(self):
        return "\n".join([node.show() for node in self.subjects])

    # check if one of the subject has a predicate with more than one object
    def hasManyObjects(self):
        for subj in self.subjects:
            if subj.hasManyObjects():return True
        return False
        
    #############
    ##  start of the realization
        
    def inSameGroup(self,p1,p2):
        if p1.startswith("has to its ") and p2.startswith("has to its "):
            return True
        for g in predicateGroups:
            if p1 in g and p2 in g:return True
        return False
    
    def addToLastObject(self,phrase,newObj):
        if isinstance(phrase,(S,SP)):
            vp=phrase.elements[-1]
            if isinstance(vp,VP):
                vp.add(newObj)
                return
        print("addToLastObject: unrecognized structure")
        print(phrase.show())
        print("---")
        print(newObj.show())
        print("====")
    
    def getASubPredObj(self,lemma):
        # print("getASubObj",lemma)
        node=self.getNode(lemma)
        # print("node",node)
        if node !=None and len(node.predObj)==1:
            # print("node.predObj.items:",node.predObj.items())
            return list(node.predObj.items())[0]
        return None
    
    ## if an object has a single triple, merge it with the current one using a subordinate
    def combineObjects(self,objects,objNodes):
        if len(objNodes)==1: # look for a simple definition of the object
            # print("objNodes",objNodes)
            subPredObj=self.getASubPredObj(objNodes[0].subj)
            if subPredObj != None:
                p1=subPredObj[0]
                # print("p1",p1)
                (prec,isHuman,pats)=getSentPatterns(p1)
                pat=random.choice(pats)
                grouped=pat(groupTerms(subPredObj[1],p1))
                if isinstance(grouped,VP) and len(grouped.elements)>2:
                    ## do not add "that is" when the group starts with V("be"),V("...")
                    elem0=grouped.elements[0]
                    elem1=grouped.elements[1]
                    if isinstance(elem0,V) and elem0.lemma=="be" and \
                       isinstance(elem1,V) and elem1.props["t"]=="pp":
                        del grouped.elements[0]
                        objects=SP(objects,grouped)
                        self.delNode(objNodes[0].subj)
                        return objects
                objects=NP(objects, Pro("who" if isHuman else "that"), grouped)
                self.delNode(objNodes[0].subj)
        return objects
    
    def getVP(self,p,predObj):
        (prec,_,pats)=getSentPatterns(p)  #$ getSentPatterns::str ->  (int, [Constituent->Phrase] )
        # (prec,_,pats)=getDefaultPattern(p)  #$ getSentPatterns::str ->  (int, [Constituent->Phrase] )
        objNodes=predObj[p]
        objects=self.combineObjects(groupTerms(objNodes,p),objNodes)
        pat=random.choice(pats)
        return pat(objects)
    
    def getPro(self,subject,pred):
        g=getGender(subject)
        return Pro("I").g("n" if g==None else "f" if g=="female" else "m")
        # isH=isHuman(pred)
        # # print("getPro(%s,%s,%s)"%(isH,subject,pred))
        # if isH==None:
        # else:
        #     #,# it is human
        #     g=getGender(subject)
        #     return Pro("I").g("f" if g=="female" else "m")

    #$ realize:: (Graph) -> str
    def realize(self,show):
        res=[]
        while len(self.subjects)>0: ## watch out: self.subjects might be changed within the loop
            node=self.subjects.pop(0)
            predObj=node.predObj
            preds = list(predObj)  ## get the list of predicates
            nb=len(preds)
            if nb==1:
                res.append(S(q(node.subj),self.getVP(preds[0],predObj)))
            else:
                if nb>3: # split sentences into two when more than 3 triples
                    nb1=nb//2+1
                    ranges=[range(1,nb1),range(nb1+1,nb)]
                else:
                    ranges=[range(1,nb)]
                j=0
                pro = self.getPro(node.subj,preds[0])
                for rng in ranges:
                    exp0 = S(q(node.subj) if j==0 else pro,self.getVP(preds[j],predObj))
                    cp=CP(C("and"),exp0)
                    expi=exp0
                    for i in rng:
                        if self.inSameGroup(preds[i-1],preds[i]):
                            ## only add the complement
                            self.addToLastObject(expi,self.getVP(preds[i],predObj).elements[-1])
                        else:
                            pro = self.getPro(node.subj,preds[i])
                            expi = S(pro if i<nb-1 else Q(""),self.getVP(preds[i],predObj))
                            cp.add(expi)
                        j=i+1 # to set the start of the preds index for the next rng loop step 
                    res.append(S(cp))
        return " ".join([r.realize() for r in res])
