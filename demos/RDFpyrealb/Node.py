class Node:
    """ Node within a graph : this corresponds to a group of triples sharing a subject
          subj: the uri of the node
          predObj : a dictionary of predicates with a list of Node
    """
    def __init__(self,subj):
        self.subj=subj
        self.predObj={}   ## :: {pred:[Node]}
    
    def __str__(self):
        pos=[]
        indent=",\n"+(len(self.subj)+5)*" "
        for p in self.predObj:
            objects=[repr(o.subj) for o in self.predObj[p]]
            pos.append('"%s":[%s]'%(p,', '.join(objects)))
        return '"%s":{%s}'%(self.subj,indent.join(pos))
    
    def show(self): # show the triples in Turtle notation
        pos=[]
        for p in self.predObj:
            objects=[o.subj for o in self.predObj[p]]
            pos.append("\n   %s %s"%(p,", ".join(objects)))
        return self.subj+';'.join(pos)+"."
    
    def getSubj(self):
        return self.subj
        
    def getPreds(self):
        return list(self.predObj) 
    
    def getObjs(self,pred):
        if pred in self.predObj:
            return self.predObj[pred]
        return None
    
    def addPredObj(self,pred,obj):
        if pred in self.predObj:
            self.predObj[pred].append(obj)
        else:
            self.predObj[pred]=[obj]
        return self 
        
    # check if one of the predicates has more than one object
    def hasManyObjects(self):
        for p in self.predObj:
            if len(self.predObj[p])>1:return True
        return False
