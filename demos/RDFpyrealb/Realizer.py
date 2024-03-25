from pyrealb import *
import re, random
from rqDBPedia import isA, getGender
from LexicalChoices import LexicalChoices

## taken from https://www.geeksforgeeks.org/python-split-camelcase-string-to-individual-strings/
# $  camel_case_split:: str -> [str]
def camel_case_split(s):
    return list(map(str.lower, re.findall(r'([A-Z]+|[A-Z]?[a-z]+)(?=[A-Z]|\b)', s)))

## help functions to simplify somewhat the notation for prepositional phrases in templates
##   they are prefixed with _ to avoid nameclash with Python keywords and operators
## combine the tuple given by star arg with the first param
def _pp(p, *o): # create a Prepositional phrase
    return PP(P(p), o)

class Realizer(LexicalChoices):
    nbDefaultRealizers=0
    ## dOpt options to show only the date
    dateOptions={"hour":False,"minute":False,"second":False,"det":False,"day":False}
    ## names of predicates for which the object should be put in lower case
    lowerCaseObject = {"bird", "bodyStyle", "category", "class","course", "dishVariation", "engine", "genre",
                       "industry","ingredient","instrument", "layout", "mainIngredient", "material",
                       "mediaType", "occupation", "product", "servingTemperature", "status", "type"}
    categoriesHuman = {"SportsTeam":False, "Astronaut":True, "Airport":False, "Athlete":True, "City":False,
                       "MusicalWork":False, "Scientist":True, "Monument":False, "Artist":True, "Company":False,
                       "University":False, "Politician":True, "WrittenWork":False, "Film":False,
                       "Food":False, "CelestialBody":False, "ComicsCharacter":True,
                       "MeanOfTransportation":False, "Building":False, "WikiData human":True}

    def __init__(self):
        self.currentCategory = None # will be filled at each realization
        ## predicates that can be combined using only their complements
        self.predicateGroups = [
            ["birthDate", "birthYear", "birthPlace"],
            ["builder","buildingStartDate"],
            ["deathDate", "deathPlace"],
            ["firstAired","lastAired"],
            ["foundingDate", "foundationPlace"],
            ["numberOfStudents", "academicStaffSize", "numberOfPostgraduateStudents"],
            ["addedToTheNationalRegisterOfHistoricPlaces","NationalRegisterOfHistoricPlacesReferenceNumber"],
            ["orbitalPeriod", "periapsis", "apoapsis"],
            ["operator","operatingIncome","operatingOrganization"],
            ["runwayLength","runwayName"]
        ]
        ## add indirect realizers to this list
        headRs = {}
        for r in self.sentence_patterns:
            (_, _, rr) = self.sentence_patterns[r]
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
        m=re.fullmatch(r'"?(\d{4}-\d{2}-\d{2})"?',term) # check for a date
        if m is not None:
            return DT(m.group(1)+"T00:00:00-06:00").dOpt(Realizer.dateOptions)
        m=re.fullmatch(r'"(.*)"',term) # remove outer quotes
        if m is not None:
            return Q(m.group(1).replace("_"," "))
        m=re.fullmatch(r'"(\d+(.\d+)?)"\s*\((.*?)\)',term) # number followed by "unit" in parentheses
        if m is not None:
            return NP(NO(m.group(1)).dOpt({"mprecision": 0}),Q(m.group(3)))
        ## HACK: patch still a few things...
        term = self.fix_language(term)
        return Q(term.replace("_"," ").replace('"','\\"'))


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
        if p in self.sentence_patterns:
            return self.sentence_patterns[p][0]
        return 50

    def property_with_underscore(self,p):
        m = re.fullmatch(r"(.*?)(\..*?)?( .*?)?_(.*?)",p)
        if len(m[1]) > 0:
            before = V(m[1])
            if m[2] is not None:
                before.t(m[2][1:])
            if m[3] is not None:
                before = [before,Q(m[3])]
        else:
            before = None
        after  = Q(m[4]) if len(m[4])>0 else None
        return (50, True, [lambda o : VP(before,o,after)])


    def getSentPatterns(self,p):
        # special cases...
        # HACK for GEM2024 (only for English...)
        if p in self.wikidata_properties:
            p = self.wikidata_properties[p]
            if '_' in p:
                return self.property_with_underscore(p)
        if p.startswith("hasToIts"):
            return self.direction(p[8:].lower())
        m = re.fullmatch(r'numberOf(.*)', p)
        if m is not None:
            entities = Q(" ".join(camel_case_split(m.group(1))))
            return self.number_of(entities)
        m = re.fullmatch(r"(\d\w\w)Runway(.*)", p)
        if m is not None:
            return self.runway(m.group(1), m.group(2))
        m = re.fullmatch(r"(.*)Code",p)
        if m is not None:
            return self.code(m.group(1))
        if p in self.sentence_patterns:
            (prec, isHuman, pats) = self.sentence_patterns[p]
            if isinstance(pats, str): # deal with a single level of indirection (does not check circularity!!)
                (prec, isHuman, pats) = self.sentence_patterns[pats]
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
            re.fullmatch(r"(\d\w\w)Runway(.*)", p) or p in self.sentence_patterns


    def isHuman(self,p):
        if p in self.sentence_patterns: return self.sentence_patterns[p][1]
        return False

    #############
    ##  start of the realization

    def inSameGroup(self, p1, p2):
        if p1.startswith("has to its ") and p2.startswith("has to its "):
            return True
        for g in self.predicateGroups:
            if p1 in g and p2 in g: return True
        return False

    def addToLastObject(self, phrase, newObj):
        if phrase.isA("S") or phrase.isA("SP"):
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

    def getPro(self, subject, _pred):
        g = getGender(subject)
        if g is None:
            if self.currentCategory in Realizer.categoriesHuman:
                if Realizer.categoriesHuman[self.currentCategory]: g = "male" # masculine by default...
            else:
                print(f"@@@ unknown category: {self.currentCategory}")
        return self.pro_I().g("n" if g is None else "f" if g == "female" else "m")

    #$ realize:: (Graph) -> str
    def realize(self,graph,show):
        res=[]
        self.currentCategory = graph.category
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
    (prec, isHuman, pats) = realizer.sentence_patterns[p]
    if realizer.lang == "en":
        print("%s [%d]" % (p, prec), end="")
    if isHuman:
        if realizer.lang == "en":print(" [human]", end="")
    if isinstance(pats, str):
        if realizer.lang == "en":print(" => " + pats)
        (prec, _, pats) = realizer.sentence_patterns[pats]
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

    for p in sorted(english.sentence_patterns):
        showRealizations(english,p, s(), o())
        showRealizations(francais,p, s(), o())
    print("\nNB en patterns:%d" % len(english.sentence_patterns))
    print("NB fr patterns:%d\n" % len(francais.sentence_patterns))

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