import sys,re
import xml.etree.ElementTree as ET
from pyrealb import *

#   Generate descriptions of Museum artefacts from the XML logical form described in
#       https://aclanthology.org/L16-1273/
#   Amy Isard. 2016. The Methodius Corpus of Rhetorical Discourse Structures and Generated Texts.
#   In Proceedings of the Tenth International Conference on Language Resources and Evaluation (LREC'16),
#   pages 1732–1736, Portorož, Slovenia. European Language Resources Association (ELRA).

#   The corpus (500 files containing 10 exhibits each)
#      is freely available at https://www.inf.ed.ac.uk/research/isdd/admin/package?view=1&id=197
#   The file "example.xml" is the example described in the paper.
#   The program has been tested on the full corpus. It regenerates the same sentence, but sometimes
#   with a slighly different word ordering which does not affect the meaning.

#   The XML format is first transformed into a Python structure built using the Node class constructor
#   whose method "to_pyrealb" creates the structure for realization.

#   The logical forms make reference to information in a database which was not available in the
#   original corpus.
#       For example: "exhibit41-exhibit-depicts" corresponding to "an athlete preparing to perform a jump"

#   Fortunately, Amy Isard provided an XSL file from which the keys with the
#   corresponding text could be extracted
#   This is the content "canned.tsv" file with the following fields
#        key \t string \t part-of-speech tag


# read the "canned text" file
canned = {}
for line in open("canned.tsv",encoding="utf-8").readlines():
    k,t,pos=line.split("\t")
    canned[k.strip()]={"text":t.strip(),"pos":pos.strip()}

def sort_const(terms):
    """Sort constituents within an NP"""
    t_order = {"D": 0, "A": 1, "N": 2, "V": 3}
    if len(terms)<2:return terms
    return sorted(terms,
                  key=lambda t:t_order[t.constType] if t.constType in t_order else 4)

class Node:
    def __init__(self, node,fileName,id):
        """Traverse the XML structure to select relevant information from XML attributes.
        Inner nodes are saved as the values of the list 'rels'."""
        self.fileName=fileName
        self.id=id
        for name in node.attrib:
            if name != "id":
                setattr(self, name, node.get(name))
        self.rels = []
        for rel in node.findall("rel"):
            n=Node(rel.find("node"),fileName,id)
            if not hasattr(n,"idref"): # ignore node with idref
                self.rels.append(n)
            subnode=rel.find("rel/node")
            if subnode is not None:
                self.rels.append(Node(subnode,fileName,id))

    def add_n(self,constituent):
        """Add number information to a constituent"""
        if constituent is None: return None
        if hasattr(self,"num"):
            if self.num=="sg":constituent.n("s")
            elif self.num=="pl":constituent.n("p")
        return constituent


    def get_terminal(self,s):
        """ Return an appropriate terminal by looking at the pyrealb lexicon entry"""
        infos = getLemma(s)
        if infos is None: return Q(s)  # quote an unknown word
        if "A" in infos: return self.add_n(A(s))
        if "N" in infos: return self.add_n(N(s))
        if "Pro" in infos: return self.add_n(Pro(s))
        if "D" in infos: return self.add_n(D(s))
        if "P" in infos: return P(s)
        if "Adv" in infos: return Adv(s)
        if "C" in infos:return C(s)
        self.error("strange pred:" + s)
        return Q(s)

    def show(self, level=0):
        """Pretty-print the Node structure"""
        res = (level * " ") + "Node(" + ",".join([f'{k}="{v}"' for k, v in self.__dict__.items()
                                                  if k not in ["rels","fileName","id"]])
        if len(self.rels) > 0:
            res +=  "".join([",\n"+rel.show(level + 5) for rel in self.rels])
        return res + ")"

    def error(self,message):
        """Output error message and raise an exception (only useful during debugging)"""
        print("Error:%s File:%s %s "%(message,self.fileName,self.id),file=sys.stderr)
        print(self.show(),file=sys.stderr)
        raise Exception(message)

    def verb_topyrealb(self,subject,complements):
        """Create a sentence from a subject and complements"""
        verb = self.pred[:-5]
        if self.tense == "pres":
            t = "p"
        elif self.tense == "past":
            t = "ps"
        else:
            self.error("bad tense:" + self.tense)
            t = "p"
        if self.voice == "passive":
            vp = VP(V("be").t(t), V(verb).t("pp"), complements)
        elif self.voice == "active":
            vp = VP(V(verb).t(t), complements)
        else:
            self.error("bad voice:" + self.voice)
            vp = VP(V(verb).t(t), complements)
        return S(subject, self.add_n(vp))

    def rels_topyrealb(self,start=0):
        """Process all relations from index start"""
        return [self.rels[i].to_pyrealb() for i in range(start,len(self.rels))]

    def to_pyrealb(self):
        """Transform to a pyrealb format appropriate for realizing an English sentence.
        The transformation relies on the value of the 'pred' attribute."""
        if self.pred.endswith("-verb"):  # create an S from a verb
            return self.verb_topyrealb(self.rels[0].to_pyrealb(),self.rels_topyrealb(1))
        if self.pred.endswith("-np"): # create an NP from possibly many words separated by dashes
            if self.pred in canned:
                parts=canned[self.pred]["text"].split("_")
                pos=canned[self.pred]["pos"]
            else:
                self.error("not in canned text:"+self.pred)
                parts=self.pred.split("-")[:-1]
                pos="N"
            det=D("the")
            if pos=="NNP": det=None
            elif hasattr(self,"det"):
                if self.det=="indef":det=D("a")
                elif self.det=="def":det=D("the")
                elif self.det=="dem-prox":det=D("this")
                else: det=D(self.det)
            np=NP(self.add_n(det),
                  sort_const([self.get_terminal(part) for part in parts]+ # add all words
                              self.rels_topyrealb()))      # process embedded rels
            if hasattr(self,"prep"): # add a preposition if present
                return PP(P(self.prep),np)
            return np
        if self.pred.startswith("exhibit") or self.pred.endswith("-description") or self.pred.endswith("period-time"):
            if self.pred in canned:
                q=Q(canned[self.pred]["text"].replace("_"," "))
            else:
                self.error("not in canned text:"+self.pred)
                q=Q("*"+self.pred+"*")  # unknown string
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
        if self.pred == "elab-rel": # create a relative
            if self.rels[0].pred.endswith("-verb"):
                return self.rels[0].verb_topyrealb(Pro("which"),self.rels[0].rels_topyrealb())
            else:
                return SP(Pro("which"),self.rels_topyrealb())
        if self.pred=="pro3n":  # special pronouns
            return self.add_n(Pro("I").g("n"))
        if self.pred=="pro2":
            return self.add_n(Pro("you"))
        if self.pred=="other":
            return self.add_n(D("other"))
        return self.get_terminal(self.pred)

def process_exhibit(exhibitElement, fileName,trace=False):
    """Process the logical forms of an exhibit XML element"""
    print("Exhibit:", exhibitElement.get("id"), fileName)
    # split the original text into sentences at the full stop, followed by at least 2 spaces and a capital letter
    orig=re.split(r"(?<=\.)\s\s+(?=[A-Z])", exhibitElement.find("text").text)
    i=0
    for lf in exhibitElement.findall("./logical-forms/lf"):
        node=Node(lf.find("node"),fileName,exhibitElement.get("id"))
        if trace: print(node.show())
        pyr=node.to_pyrealb()
        if trace: print(pyr.toSource(0))
        sent1=orig[i] if i<len(orig) else "***"
        sent2=str(pyr)
        print("orig:"+sent1) # show original
        print("gen :"+sent2)                              # show generated sentence
        i+=1
    print("---")

def process(fileName,trace=False):
    tree = ET.parse(fileName)
    for exhibitElement in tree.getroot().findall("exhibit"):
        process_exhibit(exhibitElement,fileName,trace)


loadEn()

onlyExample = True
if onlyExample:
    # realize info from the file containing the example in the paper
    process("example.xml",True)
else:
    # realize info from all files in the directory
    import os
    methodiusDir=os.path.expanduser("~/Downloads/methodius-corpus2016-05-20-1610/")
    for i in range(1,501):
        file=f'{methodiusDir}exhibit-chain{i}.xml'
        print("*****:"+file)
        process(file,False)
        print()

"""  Result on "example.xml"
Exhibit: exhibit41 example.xml
Node(pred=";",mood="dcl",
     Node(pred="and",
          Node(pred="be-verb",tense="pres",voice="active",
               Node(pred="this",num="sg"),
               Node(pred="lekythos-np",det="indef",num="sg")),
          Node(pred="create-verb",tense="past",voice="passive",
               Node(pred="pro3n",num="sg"),
               Node(pred="exhibit41-creation-time",prep="in"))),
     Node(pred="and",
          Node(pred="paint-verb",tense="past",voice="passive",
               Node(pred="pro3n",num="sg"),
               Node(pred="red-figure-technique-np",num="sg",prep="with")),
          Node(pred="be-verb",tense="past",voice="active",
               Node(pred="pro3n",num="sg"),
               Node(pred="attica-np",num="sg",prep="from"),
               Node(pred="originally"))))
S(SP(S(CP(C("and"),
          S(Pro("this").n('s'),
            VP(V("be").t('p'),
               NP(D("a").n('s'),
                  Q("lekythos")))),
          S(Pro("I").g('n').n('s'),
            VP(V("be").t('ps'),
               V("create").t('pp'),
               PP(P("in"),
                  Q("between 475 and 470 B.C."))))))).a(';'),
  SP(S(CP(C("and"),
          S(Pro("I").g('n').n('s'),
            VP(V("be").t('ps'),
               V("paint").t('pp'),
               PP(P("with"),
                  NP(D("the").n('s'),
                     A("red").n('s'),
                     N("figure").n('s'),
                     N("technique").n('s'))))),
          S(Pro("I").g('n').n('s'),
            VP(V("be").t('ps'),
               PP(P("from"),
                  NP(Q("Attica"))),
               Adv("originally")))))))
orig:This is a lekythos and it was created in between 475 and 470 B.C.; it was painted with the red figure technique and it was originally from Attica.
gen :This is a lekythos and it was created in between 475 and 470 B.C.; it was painted with the red figure technique and it was from Attica originally. 
Node(pred="unlike",mood="dcl",
     Node(pred="vessel-np",det="def",num="pl",
          Node(pred="elab-rel",
               Node(pred="create-verb",tense="past",voice="passive",
                    Node(pred="archaic-period-np",num="sg",prep="during"))),
          Node(pred="see-verb",tense="past",voice="active",
               Node(pred="pro2")),
          Node(pred="recently"),
          Node(pred="other")),
     Node(pred="create-verb",tense="past",voice="passive",
          Node(pred="lekythos-np",det="dem-prox",num="sg"),
          Node(pred="classical-period-np",num="sg",prep="during")))
S(PP(P("unlike"),
     NP(D("the").n('p'),
        D("other"),
        N("vessel").n('p'),
        S(Pro("which"),
          VP(V("be").t('ps'),
             V("create").t('pp'),
             PP(P("during"),
                NP(D("the").n('s'),
                   A("archaic").n('s'),
                   N("period").n('s'))))),
        S(Pro("you"),
          VP(V("see").t('ps'))),
        Adv("recently"))).a(','),
  SP(S(NP(D("this").n('s'),
          Q("lekythos")),
       VP(V("be").t('ps'),
          V("create").t('pp'),
          PP(P("during"),
             NP(D("the").n('s'),
                A("classical").n('s'),
                N("period").n('s')))))))
orig:Unlike the other vessels you recently saw, which were created during the archaic period, this lekythos was created during the classical period.
gen :Unlike the other vessels which were created during the archaic period you saw recently, this lekythos was created during the classical period. 
Node(pred="depict-verb",mood="dcl",tense="pres",voice="active",
     Node(pred="pro3n",num="sg"),
     Node(pred="exhibit41-exhibit-depicts"))
S(Pro("I").g('n').n('s'),
  VP(V("depict").t('p'),
     Q("an athlete preparing to perform a jump")))
orig:It depicts an athlete preparing to perform a jump.
gen :It depicts an athlete preparing to perform a jump. 
---

"""