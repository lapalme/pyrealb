import sys,re
import xml.etree.ElementTree as ET
from pyrealb import *

#   Generate description from the XML logical form described in
#       https://aclanthology.org/L16-1273/
#   Amy Isard. 2016. The Methodius Corpus of Rhetorical Discourse Structures and Generated Texts.
#   In Proceedings of the Tenth International Conference on Language Resources and Evaluation (LREC'16),
#   pages 1732–1736, Portorož, Slovenia. European Language Resources Association (ELRA).

#   The corpus (500 files containing 10 exhibits each)
#      is freely available at https://www.inf.ed.ac.uk/research/isdd/admin/package?view=1&id=197
#   The file "example.xml" is the example described in the paper.
#   The program has been tested on the full corpus.

#   The generated text is not strictly the same as the one given in the paper, because it makes reference
#   to information in a database which is not available:
#       For example: "exhibit41-exhibit-depicts" corresponds to "an athlete preparing to perform a jump"
#   Such references are realized instead as the reference string surrounded by asterisks.

#   The XML format is first transformed into a Python structure built using the Node class constructor
#   whose method "to_pyrealb" creates the structure for realization.

def get_terminal(s):
    """ Return an appropriate terminal by looking at the lexicon entry"""
    infos = getLemma(s)
    if infos is None: return Q(s) # quote an unknown word
    if "A"   in infos: return A(s)
    if "N"   in infos: return N(s)
    if "D"   in infos: return D(s)
    if "Pro" in infos: return Pro(s)
    if "P"   in infos: return P(s)
    if "Adv" in infos: return Adv(s)
    print("strange pred:"+s,file=sys.stderr)
    return Q(s)

class Node:
    def __init__(self, node):
        """Traverse the XML structure to select relevant information from XML attributes.
        Inner nodes are saved as the values of the list 'rels'."""
        for name in node.attrib:
            if name != "id":
                setattr(self, name, node.get(name))
        self.rels = []
        for rel in node.findall("rel"):
            n=Node(rel.find("node"))
            if not hasattr(n,"idref"): # ignore node with idref
                self.rels.append(n)

    def attrs(self):
        """Return the list of attributes"""
        res = []
        for k, v in self.__dict__.items():
            if k != "rels":
                res.append((k, v))
        return res

    def show(self, level=0):
        """Pretty-print the Node structure"""
        res = (level * " ") + "Node(" + ",".join([f'{k}="{v}"' for k, v in self.attrs()])
        if len(self.rels) > 0:
            res += "\n" + "\n".join([rel.show(level + 5) for rel in self.rels])
        return res + ")"

    def to_pyrealb(self):
        """Transform to a pyrealb format appropriate for realizing an English sentence.
        The transformation relies on the value of the 'pred' attribute."""
        if self.pred.endswith("-verb"):  # create an S from a verb
            verb=self.pred[:-5]
            if self.tense=="pres": t="p"
            elif self.tense=="past": t="ps"
            else:
                print("bad tense:"+self.tense,file=sys.stderr)
                t = "p"
            if self.voice=="passive":
                vp=VP(V("be").t(t),V(verb).t("pp"),[self.rels[i].to_pyrealb() for i in range(1,len(self.rels))])
            elif self.voice=="active":
                vp=VP(V(verb).t(t),[self.rels[i].to_pyrealb() for i in range(1,len(self.rels))])
            else:
                print("bad voice:"+self.voice,file=sys.stderr)
                vp=VP(V(verb).t(t),[self.rels[i].to_pyrealb() for i in range(1,len(self.rels))])
            return S(self.rels[0].to_pyrealb(),vp)
        if self.pred.endswith("-np"): # create an NP from possibly many words separated by dashes
            parts=self.pred.split("-")
            np=NP(D("a" if hasattr(self,"det") and self.det=="indef" else "the"),
                  [get_terminal(part) for part in parts[:-1]],  # add all words
                  [rel.to_pyrealb() for rel in self.rels])      # process embedded rels
            if hasattr(self,"num") and self.num!="sg":np.n("p")
            if hasattr(self,"prep"): # add a preposition if present
                return PP(P(self.prep),np)
            return np
        if self.pred.startswith("exhibit") or self.pred.endswith("-description") or self.pred.endswith("period-time"):
            q=Q("*"+self.pred+"*")  # create a reference to the database (unfortunately not available)
            if hasattr(self, "prep"):
                return PP(P(self.prep),q)
            return q
        if self.pred in ["and","or"]: # create a coordinate sentence
            return S(CP(C(self.pred),[n.to_pyrealb() for n in self.rels]))
        if self.pred==";": # create an S with 2 parts separated by a semi-colon
            return S(SP(self.rels[0].to_pyrealb()).a(";"),
                     SP(self.rels[1].to_pyrealb()))
        if self.pred in ["like","unlike"]:  # create a comparison
            return S(PP(P(self.pred),self.rels[0].to_pyrealb()).a(","),
                     SP(self.rels[1].to_pyrealb()))
        if self.pred == "elab-rel": # ignore this relation
            return self.rels[0].to_pyrealb()
        if self.pred=="pro3n":  # special pronoun
            return Pro("it")
        if self.pred=="pro2":
            return Pro("you")
        return get_terminal(self.pred)

def show_exhibit(exhibitElement, trace=False):
    """Process the logical forms of an exhibit XML element"""
    print("Exhibit:", exhibitElement.get("id"))
    # split the original text into sentences at the full stop, followed by spaces and a capital letter
    orig=re.split(r"(?<=\.)\s+(?=[A-Z])", exhibitElement.find("text").text)
    i=0
    for lf in exhibitElement.findall("./logical-forms/lf"):
        node=Node(lf.find("node"))
        if trace: print(node.show())
        pyr=node.to_pyrealb()
        if trace: print(pyr.toSource(0))
        print("orig:" + (orig[i] if i<len(orig) else "***")) # show original
        print("gen :"+str(pyr))                              # show generated sentence
        i+=1
    print("---")

def process(fileName,trace=False):
    tree = ET.parse(fileName)
    for exhibitElement in tree.getroot().findall("exhibit"):
        show_exhibit(exhibitElement,trace)

loadEn()
# launch on the file containing the example in the paper
process("example.xml",True)

#  Process all files in the directory
# import os
# methodiusDir=os.path.expanduser("~/Downloads/methodius-corpus2016-05-20-1610/")
#
# for i in range(1,501):
#     file=f'{methodiusDir}exhibit-chain{i}.xml'
#     print("*****:"+file,False)
#     process(file)
#     print()
