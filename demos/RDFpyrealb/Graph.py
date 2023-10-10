from rqDBPedia import isA
# nodes of the graph
from Node import Node

import random

class Graph:
    """Graph creation from triples """
    def __init__(self, category,triples):
        self.category=category
        self.subjects = [] # [Node]
        text2Node={} # {string:Node}
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
        
    def getASubPredObj(self,lemma):
        # print("getASubObj",lemma)
        node=self.getNode(lemma)
        # print("node",node)
        if node is not None and len(node.predObj)==1:
            # print("node.predObj.items:",node.predObj.items())
            return list(node.predObj.items())[0]
        return None
