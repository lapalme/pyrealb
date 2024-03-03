from pyrealb import *
import re, random
from rqDBPedia import isA, getGender

## taken from https://www.geeksforgeeks.org/python-split-camelcase-string-to-individual-strings/
# $  camel_case_split:: str -> [str]
def camel_case_split(s):
    return list(map(str.lower, re.findall(r'([A-Z]+|[A-Z]?[a-z]+)(?=[A-Z]|\b)', s)))

## help functions to simplify somewhat the notation for prepositional phrases in templates
##   they are prefixed with _ to avoid nameclash with Python keywords and operators
## combine the tuple given by star arg with the first param
def _pp(p, *o):
    return PP(P(p), o)

class Realizer:
    nbDefaultRealizers=0
    ## dOpt options to show only the date
    dateOptions={"hour":False,"minute":False,"second":False,"det":False,"day":False}
    ## names of predicates for which the object should be put in lower case
    lowerCaseObject = {"bird", "bodyStyle", "course", "dishVariation", "engine", "genre", "industry", "ingredient",
                       "instrument", "mainIngredient", "material", "mediaType", "occupation", "product", "service",
                       "servingTemperature", "status", "type"}

    def __init__(self):
        ## predicates that can be combined using only their complements
        self.predicateGroups = [
            ["birthDate", "birthPlace"],
            ["deathDate", "deathPlace"],
            ["foundingDate", "foundationPlace"],
            ["numberOfStudents", "academicStaffSize", "numberOfPostgraduateStudents"],
            ["addedToTheNationalRegisterOfHistoricPlaces","NationalRegisterOfHistoricPlacesReferenceNumber"],
            ["orbitalPeriod", "periapsis", "apoapsis"],
        ]
        ## add indirect realizers to this list
        headRs = {}
        for r in self.sentencePatterns:
            (_, _, rr) = self.sentencePatterns[r]
            if isinstance(rr, str):
                if rr in headRs:
                    headRs[rr].append(r)
                else:
                    headRs[rr] = [r]
        for r in headRs:
            self.predicateGroups.append([r] + headRs[r])



    ##  format a litteral
    def q(self,term,lower=False):
        if lower:term=term.lower()
        if isinstance(term,Terminal):term=term.lemma
        m=re.fullmatch(r'"?(\d{4}-\d{2}-\d{2})"?',term)
        if m is not None:
            return DT(m.group(1)+"T00:00:00-06:00").dOpt(Realizer.dateOptions)
        m=re.fullmatch(r'"(.*)"',term)
        if m!=None:
            return Q(m.group(1).replace("_"," "))
        m=re.fullmatch(r'"(\d+(.\d+)?)"\s*\((.*?)\)',term)
        if m!=None:
            return NP(NO(m.group(1)).dOpt({"mprecision": 0}),Q(m.group(3)))
        ## HACK: patch a few things...
        return Q(term.replace("_language","").replace("_"," ").replace('"','\\"'))


    ##  combine many objects sharing a subject and predicate
    def groupTerms(self,terms,pred):
        toLower=pred in Realizer.lowerCaseObject or re.fullmatch(r"(\d\w\w)Runway(.*)",pred) is not None
        if len(terms)>1:
            return CP(self.conj_and,[self.q(term.subj,toLower) for term in terms])
        return self.q(terms[0].subj,toLower)

    def getPrecedence(self,p):
        # special cases (the same as in getSentPattern)
        if p.startswith("hasToIts "):return 30
        if p.startswith("numberOf"):return 21
        if "Runway" in p: return 30+int(p[0])
        if p in self.sentencePatterns:
            return self.sentencePatterns[p][0]
        return 50

    def getSentPatterns(self,p):
        # special cases...
        if p.startswith("hasToIts"):
            return self.direction(p[8:].lower())
        m = re.fullmatch(r'numberOf(.*)', p)
        if m != None:
            entities = Q(" ".join(camel_case_split(m.group(1))))
            return self.number_of(entities)
        m = re.fullmatch(r"(\d\w\w)Runway(.*)", p)
        if m != None:
            return self.runway(m.group(1), m.group(2))
        if p in self.sentencePatterns:
            (prec, isHuman, pats) = self.sentencePatterns[p]
            if isinstance(pats, str):
                (prec, isHuman, pats) = self.sentencePatterns[pats]  # deal with indirection (does not check circularity!!)
            return (prec, isHuman, pats)
        # if p in modifiedPredicates:  ## check for "old" predicates for the 2017 test set
        #     return getSentPatterns(modifiedPredicates[p])
        return self.getDefaultPattern(p)


    def getDefaultPattern(self,p):
        print("@@@ Default realizer for: " + p)
        self.nbDefaultRealizers += 1
        if " " not in p and re.match(r'[A-Z]+[a-z]|[a-z]+[A-Z]', p):  # check for dromadaryCase or CamelCase
            p = " ".join(camel_case_split(p))
        # HACK: empty .en to indicate use of default template
        return (50, None, [lambda o: VP(self.q(p), self.v_be, o).en("")])


    ## check if p is a defined pattern
    def hasPattern(self,p):
        return p.startswith("hasToIts") or re.fullmatch(r'numberOf(.*)', p) is not None or \
            re.fullmatch(r"(\d\w\w)Runway(.*)", p) or p in self.sentencePatterns


    def isHuman(self,p):
        if p in self.sentencePatterns: return self.sentencePatterns[p][1]
        return None

    #############
    ##  start of the realization

    def inSameGroup(self, p1, p2):
        if p1.startswith("has to its ") and p2.startswith("has to its "):
            return True
        for g in self.predicateGroups:
            if p1 in g and p2 in g: return True
        return False

    def addToLastObject(self, phrase, newObj):
        if phrase.isA("S","SP"):
            vp = phrase.elements[-1]
            if vp.isA("VP"):
                vp.add(newObj, None, True)  # HACK: insert directly in the VP without keeping track of .add(...)
                return
        print("addToLastObject: unrecognized structure")
        print(phrase.toSource(0))
        print("---")
        print(newObj.toSource(0))
        print("====")

    ## if an object has a single triple, merge it with the current one using a subordinate
    def combineObjects(self, graph, objects, objNodes):
        if len(objNodes) == 1:  # look for a simple definition of the object
            # print("objNodes",objNodes)
            subPredObj = graph.getASubPredObj(objNodes[0].subj)
            if subPredObj is not None:
                p1 = subPredObj[0]
                # print("p1",p1)
                (prec, isHuman, pats) = self.getSentPatterns(p1)
                pat = random.choice(pats)
                grouped = pat(self.groupTerms(subPredObj[1], p1))
                if grouped.isA("VP") and len(grouped.elements) > 2:
                    ## do not add "that is" when the group starts with V("be"),V("...")
                    elem0 = grouped.elements[0]
                    elem1 = grouped.elements[1]
                    if elem0.isA("V") and elem0.lemma == self.v_be.lemma and \
                            elem1.isA("V") and elem1.props["t"] == "pp":
                        del grouped.elements[0]
                        objects = SP(objects, grouped)
                        graph.delNode(objNodes[0].subj)
                        return objects
                objects = NP(objects, self.rel_pro(isHuman), grouped)
                graph.delNode(objNodes[0].subj)
        return objects

    def getVP(self, graph,p, predObj):
        (prec, _, pats) = self.getSentPatterns(p)  # $ getSentPatterns::str ->  (int, [Constituent->Phrase] )
        # (prec,_,pats)=getDefaultPattern(p)  #$ getSentPatterns::str ->  (int, [Constituent->Phrase] )
        objNodes = predObj[p]
        objects = self.combineObjects(graph,self.groupTerms(objNodes, p), objNodes)
        pat = random.choice(pats)
        return pat(objects)

    def getPro(self, subject, pred):
        g = getGender(subject)
        return self.pro_I().g("n" if g == None else "f" if g == "female" else "m")

    #$ realize:: (Graph) -> str
    def realize(self,graph,show):
        res=[]
        while len(graph.subjects)>0: ## watch out: graph.subjects might be changed within the loop
            node=graph.subjects.pop(0)
            predObj=node.predObj
            preds = list(predObj)  ## get the list of predicates
            nb=len(preds)
            if nb==1:
                res.append(S(self.q(node.subj),self.getVP(graph,preds[0],predObj)))
            else:
                if nb>3: # split sentences into two when more than 3 triples
                    nb1=nb//2+1
                    ranges=[(1,nb1),(nb1+1,nb)]
                else:
                    ranges=[(1,nb)]
                j=0
                pro = self.getPro(node.subj,preds[0])
                for (r1,r2) in ranges:
                    vp = self.getVP(graph,preds[j],predObj)
                    if j==0:
                        subj = self.q(node.subj)
                    elif vp.getProp("en") is not None:
                        subj = self.def_det # for the default template
                    else:
                        subj = pro
                    exp0 = S(subj,vp)
                    cp=CP(self.conj_and,exp0)
                    expi=exp0
                    for i in range(r1,r2):
                        if self.inSameGroup(preds[i-1],preds[i]):
                            ## only add the complement
                            self.addToLastObject(expi,self.getVP(graph,preds[i],predObj).elements[-1])
                        else:
                            pro = self.getPro(node.subj,preds[i])
                            vp = self.getVP(graph,preds[i],predObj)
                            expi = S(pro if i<r2-1 else Q(""),vp)
                            cp.add(expi,None,True) # HACK: insert directly in the CP without keeping track of .add(...)
                        j=i+1 # to set the start of the preds index for the next rng loop step
                    res.append(S(cp))
        if show:
            print("\n".join([r.toSource(0) for r in res]))
        return " ".join([r.realize() for r in res])


def printReal(pat, s, o):
    print("   " + S(s, pat(o)).realize())


def showRealizations(realizer,p, s, o):
    load(realizer.lang)
    (prec, isHuman, pats) = realizer.sentencePatterns[p]
    if realizer.lang == "en":
        print("%s [%d]" % (p, prec), end="")
    if isHuman:
        if realizer.lang == "en":print(" [human]", end="")
    if isinstance(pats, str):
        if realizer.lang == "en":print(" => " + pats)
        (prec, _, pats) = realizer.sentencePatterns[pats]
    else:
        if realizer.lang == "en":print()
    for pat in pats:
        printReal(pat, s, o)


if __name__ == '__main__':
    ## unit test of all realizers with dummy subject and object
    s = lambda: Q("*S*")  # create a dummy subject
    o = lambda: Q("*O*")  # "       "   object

    from English import English
    from Francais import Francais
    english = English()
    francais = Francais()
    english.nbDefaultRealizers = 0
    francais.nbDefaultRealizers = 0

    for p in sorted(english.sentencePatterns):
        showRealizations(english,p, s(), o())
        showRealizations(francais,p, s(), o())
    print("\nNB patterns:%d" % len(english.sentencePatterns))
    print("\nNB realizer:%d" % len(francais.sentencePatterns))

    print("** Special cases **")
    for realizer in [english,francais]:
        load(realizer.lang)
        printReal(realizer.getSentPatterns("numberOfEmployees")[2][0], s(), NO(1234))
        for country in realizer.countries:  # to exercise more possibilities
            printReal(realizer.getSentPatterns("nationality")[2][0], s(), Q(country))
        printReal(realizer.getSentPatterns("unknownPredicateOf")[2][0], s(), o())
        printReal(realizer.getSentPatterns("is a kind of")[2][0], s(), o())
        printReal(realizer.getSentPatterns("1stRunwaySurfaceType")[2][0], s(), o())
        printReal(realizer.getSentPatterns("3rdRunwayLengthFeet")[2][0], s(), NO(456))
        printReal(realizer.getSentPatterns("5thRunwayNumber")[2][0], s(), NO(9))
        printReal(realizer.getSentPatterns("5th_runway_Number")[2][0], s(), NO(8))
        print("Default %s realizer was used: %5d times" % (realizer.lang,realizer.nbDefaultRealizers))
        print("-----")