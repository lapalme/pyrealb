class UD:
    def __init__(self,UDconstructor,sentence):
        self.text = sentence.text
        self.nodes = [UDconstructor(word) for word in sentence.words]
        for node in self.nodes:
            if node.head == 0:
                self.root = node
                node.position = ""
                node.parent = None
            elif node.id < node.head:
                node.addToLeftOf(self.nodes[node.head - 1])
            else:
                node.addToRightOf(self.nodes[node.head - 1])

    def pp(self):
        return self.root.pp()

    def to_pyrealb(self,copyGenderNumber):
        return self.root.toDependent(copyGenderNumber)

    def coNLL(self): #  show original coNNL
        return "\n".join(n.coNLL() for n in self.nodes)

    def toCoNLL(self):
        return "\n".join(n.toCoNLL() for n in self.nodes)

    def isProjective(self):
        return self.root.isProjective()
