from context import pyrealb
from pyrealb import *
import random,re

## dOpt options to show only the date    
dateOptions={"hour":False,"minute":False,"second":False,"det":False,"day":False}

### Pre-realizer code...
#$  q::(str,bool)->Terminal
##  format a litteral 
def q(term,lower=False):
    if lower:term=term.lower()
    if isinstance(term,Q):term=term.lemma
    m=re.fullmatch(r'"?(\d{4}-\d{2}-\d{2})"?',term)
    if m!=None:
        ## HACK: on ajoute le TimeZone (de Montréal) pour obtenir la date locale
        ##  dans le browser -05:00 semble fonctionner, mais avec Node il faut -06:00 
        return DT(m.group(1)+"T00:00:00-06:00").dOpt(dateOptions)
    m=re.fullmatch(r'"(.*)"',term)
    if m!=None:
        return Q(m.group(1).replace("_"," "))
    m=re.fullmatch(r'"(\d+(.\d+)?)"\s*\((.*?)\)',term)
    if m!=None:
        return NP(NO(m.group(1)).dOpt({"mprecision": 0}),Q(m.group(3)))
    ## HACK: patch a few things...
    return Q(term.replace("_language","").replace("_"," ").replace('"','\\"'))

## names of predicates for which the object should be put in lower case
lowerCaseObject = set(["bird","bodyStyle","course","dishVariation","engine","genre","industry",
                        "ingredient","instrument","mainIngredient","material","mediaType",
                        "occupation","product","service","servingTemperature",
                        "status","type"])

#$  groupTerms:: ([Node],String) -> Constituent
##  combine many objects sharing a subject and predicate  
def groupTerms(terms,pred):
    toLower=pred in lowerCaseObject or re.fullmatch(r"(\d\w\w)Runway(.*)",pred)!=None
    if len(terms)>1:
        return CP([C("and")]+[q(term.subj,toLower) for term in terms])
    return q(terms[0].subj,toLower)

## used in "nationality" realizer to deal with special frequent cases
countries={"United_States":"American","Canada":"Canadian","France":"French","Mexico":"Mexican"}

## help functions to simplify somewhat the notation for prepositional phrases in templates
##   they are prefixed with _ to avoid nameclash with Python keywords and operators
## combine the tuple given by star arg with the first param 
def _pp(p,o)   : return PP([P(p),*o])
## use star to allow more than two parameters to _pp
def _above(*o) : return _pp("above",o)
def _as(*o)    : return _pp("as"  ,o)
def _at(*o)    : return _pp("at"  ,o)
def _by(*o)    : return _pp("by"  ,o)
def _during(*o): return _pp("during",o)
def _for(*o)   : return _pp("for" ,o)
def _from(*o)  : return _pp("from",o)
def _in(*o)    : return _pp("in"  ,o)
def _inside(*o): return _pp("inside",o)
def _into(*o)  : return _pp("into",o)
def _of(*o)    : return _pp("of"  ,o)
def _on(*o)    : return _pp("on"  ,o)
def _out(*o)   : return _pp("out" ,o)
def _to(*o)    : return _pp("to"  ,o)
def _with(*o)  : return _pp("with",o)

def number(n,o): return VP(V("have"),NP(D("the"),Q(n),N("number"),o))
 
#### switch for precedence, isHuman, vp pattern
## precedence between 0 and 100 used for sorting predicates before realization
## isHuman : boolean indicating if this predicate applies to a human (useful for pronominalzation)
#$ realizers::{str :  (int, bool, [Constituent->Phrase] | str)
sentencePatterns = {
    "abbreviation":(50,False,[
         lambda   o:VP(V("be"),V("abbreviate").t("pp"),_by(o)),
    ]),
    "academicStaffSize":(50,False,[
         lambda   o:VP(V("have"),D("a"),oneOf(A("academic"),Q("")),N("staff"),_of(NO(o.lemma)))
    ]),
    "academicDiscipline":(50,False,[	
        lambda o:VP(V("be"),NP(N("part"),_of(NP(D("the"),A("academic"),N("discipline"),_of(o))))),	
    ]),
    "activeYearsEndDate":(70,True,"activeYearsEndYear"),
    "activeYearsEndYear":(70,True,[
        lambda o:VP(V("end").t("ps"),NP(D("my").g("m"),N("career"),_in(o))),
    ]),
    "activeYearsStartDate":(30,True,"activeYearsStartYear"),
    "activeYearsStartYear":(30,True,[
        lambda o:VP(V("start").t("ps"),NP(D("my").g("m"),N("career"),_in(o))),
    ]),
    "address":(20,False,"location"),
    "affiliation":(20,False,[	
         lambda   o:VP(V("be"),V("affiliate").t("pp"),oneOf(_with(o),_to(o))),
    ]),	
    # "affiliations":(20,True,"affiliation"),
    "almaMater":(20,True,[	
        lambda o:VP(V("graduate").t("ps"),_from(o)) ,	
        lambda o:VP(V("be").t("ps"),V("award").t("pp"),NP(D("a"),N("degree")),_from(o)) ,	
        lambda o:VP(V("earn").t("ps"),NP(D("a"),N("degree")),_from(o)) ,	
    ]),	
    "alternativeName":(1,True,[	
        lambda o:VP(V("be"),Adv("also"),V("call").t("pp"),o),	
    ]),
    "anthem":(50,False,[
        lambda o:VP(V("have"),o,_as(N("anthem")))
    ]),	
    "apoapsis":(30,False,[
        lambda o:VP(V("have"),NP(D("a"),Q("apoapsis"),_of(o)))
    ]),
    "areaOfLand":(50,False,[
        lambda o:VP(V(oneOf("cover","have")),NP(D("a"),N("land"),N("area"),_of(o))),
    ]),
    "areaOfWater":(50,False,[
        lambda o:VP(V(oneOf("cover","have")),NP(D("a"),N("water"),N("area"),_of(o))),
    ]),
    "areaTotal":(50,False,[
        lambda o:VP(V("have"),NP(D("a"),A("total"),N("area"),_of(o)))
    ]),
    "architect":(45,False,[
        lambda o:VP(V("be").t("ps"),V("design").t("pp"),_by(NP(D("the"),N("architect"),o)))
    ]),
    "architecturalStyle":(40,False,[
        lambda o:VP(V("be"),_in(NP(D("the"),A("architectural"),N("style"),o)))
    ]),
    "areaCode":(60,False,[
        lambda o:VP(V("have"),NP(D("the"),N("area"),N("code"),o)),
    ]),
    "assembly":(50,False,[
        lambda o:VP(V("be"),V("assemble").t("pp"),_in(o)),
    ]),
    "associatedBand/associatedMusicalArtist":(50,True,[    
        lambda o:VP(V(oneOf("play","perform")),_with(o)),    
    ]),
    "associatedRocket":(50,False,[ # $$$$ last
        lambda o:VP(V("be"),V("associate").t("pp"),_with(D("the"),N("rocket"),o))
    ]),    
    "author":(40,True,[    
        lambda o:VP(V("be").t("ps"),V("write").t("pp"),_by(o)),    
    ]),    
    "averageSpeed":(60,False,[
        lambda o:VP(V("have"),NP(D("a"),N("average"),N("speed"),_of(o))),
    ]),
    "award":(53,True,"awards"),
    "awards":(53,True,[	
        lambda o:VP(V("have"),V("be").t("pp"),V("award").t("pp"),o),	
        lambda o:VP(V("win").t("ps"),o),	
    ]),
    "background":(30,True,[
        lambda o:VP(V("have"),NP(D("a"),N("background"),_of(o))),
        lambda o:PP(P("with"),NP(D("a"),N("background"),_of(o))),
    ]),
    "backupPilot":(23,False,[	
        lambda o:VP(V("have"),_as(oneOf(D("my").g("n"),Q("")),N("back-up"),N("pilot")),o),	
        lambda o:VP(V("include").t("ps"),_as(N("back-up"),N("pilot"),o)),	
    ]),	
    "battle":(50,True,[
        lambda o:VP(V("be").t("ps"),V("involve").t("pp"),_in(NP(D("the"),N("battle"),_of(o)))),
        lambda o:VP(V("be").t("ps"),NP(N("part"),_of(o))),
    ]),
    "bird":(50,False,[	
        lambda o:VP(V("have"),o,_as(A("official"),N("bird"))),	
    ]),	
    "birthDate":(2,True,[	
        lambda o:VP(V("be").t("ps"),V("born").t("pp"),_on(o)),	
    ]),
    "birthName":(2,True,[
        lambda o:VP(V("be").t("ps"),Adv(oneOf("first","originally")),V("name").t("pp"),o), 
    ]),
    "birthPlace":(3,True,[	
        lambda o:VP(V("be").t("ps"),V("born").t("pp"),_in(o)),	
    ]),	
    "birthYear":(2,True,"birthPlace"),
    "bodyStyle":(50,False,[
        lambda o:VP(V("be"),D("a"),o)
    ]),
    "broadcastedBy":(40,False,[
        lambda o:VP(V("be").t("ps"),V("broadcast").t("pp"),_by(o)),
    ]),
    "builder":(10,False,[
        lambda o:VP(V("be"),V(oneOf("build","make")).t("pp"),_by(o))
    ]),
    "buildingStartDate":(15,False,[
        lambda o:VP(V("open").t("ps"),_on(o)),
        lambda o:VP(V("be").t("ps"),V("begin").t("pp"),_on(o)),
    ]),
    "campus":(21,False,[	
        lambda o:VP(V("be"),V("locate").t("pp"),_in(o)),
        lambda o:_in(o),
    ]),	
    "capital":(30,False,[	
         lambda o:VP(V("have"),o,Adv("as"),N("capital")) ,
         lambda o:_with(D("a"),N("capital"),_in(o)),
    ]),	
    "category":(10,False,[	
        lambda o:VP(V("be"),V("categorize").t("pp"),_as(o)),	
        lambda o:VP(V("fall"),P("under"),D("the"),N("category"),_of(o)),	
    ]),
    "chairman":(50,True,[
        lambda o:VP(V("have"),o,P("as"),N("chairman")),
        lambda o:VP(V("be"),V("chair").t("pp"),_by(o)),	
    ]),	
    "champions":(50,False,[
        lambda o:VP(Pro("where"),o,V("be").t("ps").n("p"),N("champion").n("p"))
    ]),
    "city":(30,False,[	
        lambda o:VP(V("be"),_from(o)),	
        lambda o:VP(V("be"),V("locate").t("pp"),_in(o)),	
    ]),	
    "cityServed":(50,False,[	
        lambda o:VP(V("serve"),o),	
    ]),
    "class":(50,False,[
        lambda o:VP(V("be"),NP(D("a"),o)),
    ]),	
    "club":(50,True,[	
        lambda o:VP(V("play").t("ps"),_for(o)),	
        lambda o:VP(V("be"),NP(D("a"),N("player"),_for(o))),	
    ]),
    "coach":(50,True,[
        lambda o:VP(V("be"),V(oneOf("manage","coach")).t("pp"),_by(o)),
    ]),
    "codenCode":(50,False,[
        lambda o:VP(V("have"),NP(D("the"),Q("CODEN"),N("code"),_of(o)))
    ]),
    "commander":(21,True,[	
        lambda o:VP(V("be"),V("command").t("pp"),_by(o)),	
    ]),	
    "compete in":(50,True,[	
        lambda o:VP(V("compete"),_in(o)),	
        lambda o:VP(V("be"),N("part"),_of(o)),	
    ]),
    "completionDate":(60,False,[	
        lambda o:VP(V("be").t("ps"),V("complete").t("pp"),_in(o)),	
    ]),
    "cost":(40,False,[
        lambda o:VP(V("cost"),o),
    ]),	
    "country":(40,False,"city"),
    "countryOrigin":(10,True,[
        lambda o:VP(V("originate").t("ps"),_in(o))
    ]),
    "countySeat":(40,False,[
        lambda o:VP(V("be"),NP(D("the"),N("county"),N("seat"),_of(o))),
    ]),
    "course":(20,False,[
        lambda o:VP(V("be"),NP(D("a"),o)),
    ]),
    "creator":(50,False,[
        lambda o:VP(V("be").t("ps"),V("create").t("pp"),_by(o)),	
    ]),	
    "crewMembers":(50,False,[	
        lambda o:VP(V("have"),o,_as(N("crew"),N("member").n("p"))),	
    ]),	
    "currency":(60,False,[
        lambda o:VP(V("have"),o,_as(oneOf(Q(""),A("national")),N("currency"))),
    ]),
    "currentclub":(50,True,"club"),
    "dateOfRetirement":(90,True,[	
        lambda o:VP(V("retire").t("ps"),_on(o)),	
        lambda o:VP(V("go").t("ps"),P("into"),N("retirement"),_on(o)),	
    ]),	
    "dean":(20,False,[	
        lambda o:VP(V("be"),V("lead").t("pp"),_by(o)),	
    ]),	
    "deathDate":(99,True,[	
        lambda o:VP(V("die").t("ps"),_on(o)),	
        lambda o:VP(V("pass").t("ps"),Adv("away"),_on(o)),	
    ]),	
    "deathPlace":(100,True,[	
        lambda o:VP(V("die").t("ps"),_in(o)),	
        lambda o:VP(V("pass").t("ps"),Adv("away"),_in(o)),	
    ]),
    "debutTeam":(30,True,[
        lambda o:VP(Adv("first"),V("play").t("ps"),_with(o)),
    ]),	
    "dedicatedTo":(10,False,[	
        lambda o:VP(V("be"),V("dedicate").t("pp"),_to(o)),	
    ]),	
    "demonym":(50,False,[	
        lambda o:VP(V("be"),V("inhabit").t("pp"),_by(o)),	
    ]),
    "density":(50,False,[
        lambda o:VP(V("have"),NP(D("a"),N("density"),_of(o)))
    ]),
    "derivative":(50,False,[
        lambda o:VP(V("derive").t("ps"),_into(o))
    ]),
    "designer":(25,False,[	
        lambda o:VP(V("be").t("ps"),V("design").t("pp"),_by(o)),	
        lambda o:_by(D("my").g("n"),N("designer"),o),
    ]),
    "diameter":(40,False,[
        lambda o:VP(V("have"),NP(D("a"),N("diameter"),_of(o))),
        lambda o:VP(V("be"),o,_in(N("diameter"))),
    ]),
    # "discover":(20,False,"discovery"),
    # "discoverer":(20,False,"discovery"),
    "discoverer":(20,False,[
        lambda o:VP(V("be").t("ps"),V("discover").t("pp"),_by(o))
    ]),
    "dishVariation":(50,False,[
        lambda o:VP(V("be"),NP(D("a"),N("variation"),_of(o))),	
    ]),
    "division":(40,False,[
        lambda o:VP(V("have"),NP(D("a"),o,N("division")))
    ]),
    "doctoralStudent":(50,True,[
        lambda o:VP(V("supervise").t("ps"),o),
    ]),
    "draftTeam":(20,True,[
        lambda o:VP(V("be").t("ps"),V("draft").t("pp"),_by(o)),
    ]),
    "editor":(42,False,[    
        lambda o:VP(V("be").t("ps"),V("edit").t("ps"),_by(o)),    
    ]),    
    "elevationAboveTheSeaLevel":(48,False,[
        lambda o:VP(V("be"),oneOf(V("locate").t("pp"),A("situated")),
                    NP(NO(o.lemma),N("metre"),_above(N("sea"),N("level"))))
    ]),
    "elevationAboveTheSeaLevelInMetres":(48,False,"elevationAboveTheSeaLevel"),
    "engine":(50,False,[
        lambda o:VP(V("have"),NP(D("a"),o)) if isinstance(o,Terminal) and o.lemma.endswith("engine")
                 else VP(V("have"),NP(D("a"),o,N("engine")))
    ]),
    "epoch":(50,False,[
        lambda o:VP(V("have"),NP(D("a"),N("epoch"),N("date"),_of(o))),
    ]),
    "escapeVelocity":(50,False,[
        lambda o:(VP(V("have"),NP(D("a"),N("escape"),N("velocity"),_of(o))))
    ]),
    "established":(20,False,[	
        lambda o:VP(V("be").t("ps"),V("establish").t("pp"),_in(o)),	
        lambda o:VP(V("be").t("ps"),V("found").t("pp"),_in(o)),	
    ]),	
    "ethnicGroup":(50,False,[	
        lambda o:VP(V("have"),NP(D("a"),A("ethnic"),N("group"),_of(o))),
    ]),
    "family":(50,False,[
        lambda o:VP(V("belong"),_to(D("the"),N("family"),_of(o))),
        lambda o:VP(V("be"),N("part"),_of(D("the"),o,N("family")))
    ]),
    "finalFlight":(75,False,[
        lambda o:VP(V("make").t("ps"),D("my"),oneOf(D("last"),A("final")),N("flight"),_on(o)),
    ]),
    "floorCount":(50,False,[	
        lambda o:VP(V("have"),NP(NO(o.lemma),N("floor"))),	
    ]),
    "followedBy":(50,False,[	
        lambda o:VP(V("be"),V("follow").t("pp"),_by(o)),	
    ]),
    "formerName":(2,False,[
        lambda o:VP(V("be").t("ps"),Adv("formerly"),V("know").t("pp"),_as(o)),    
    ]),    
    "formerTeam":(2,True,[
        lambda o:VP(V("start").t("ps"),_with(o)),    
        lambda o:VP(V("play").t("ps"),Adv("formerly"),_with(o)),    
    ]),
    "founder":(2,False,[
        lambda o:VP(V("be").t("ps"),V(oneOf("create","found")).t("pp"),_by(o)),    
    ]),   
    "foundingDate":(2,False,[
        lambda o:VP(V("be").t("ps"),V(oneOf("create","found")).t("pp"),_on(o)),    
    ]),    
    "foundationPlace":(3,False,[    
        lambda o:VP(V("be").t("ps"),V(oneOf("create","found")).t("pp"),_in(o)),    
    ]),    
    "fullName":(3,False,[    
        lambda o:VP(A("full"),N("name"),V("be"),o),    
    ]),    
    "genre":(50,True,[	
        lambda o:VP(V(oneOf("play","perform")),o),	
    ]),
    "governingBody":(50,False,[
        lambda o:VP(V("be"),V("govern").t("pp"),_by(o)),
    ]),	
    "ground":(50,True,[	
        lambda o:VP(V("play"),_in(o)),	
    ]),	
    ## "has to its (.*)": voir genSentComp
    "height":(50,True,[
        lambda o:VP(V("have"),NP(D("a"),N("height"),_of(o),Q("m"))),
        lambda o:VP(V("be"),o,Q("m"),A("tall"))
    ]),
    "higher":(55,False,[	
        lambda o:VP(V("be"),A("high").f("su"),_of(o)),	
    ]),	
    "inaugurationDate":(10,False,[
        lambda o:VP(V("be").t("ps"),V("inaugurate").t("pp"),_on(o)),
    ]),
    "industry":(50,False,[
        lambda o:VP(V("be"),_in(NP(D("the"),o))),
    ]),	
    "ingredient":(25,False,[	
        lambda o:VP(V("contain"),o),    
        lambda o:VP(V("have"),o,P("as"),N("ingredient")),    
    ]),
    "inOfficeWhileMonarch":(50,True,[    
        lambda o:VP(V("serve").t("ps"),_during(NP(D("the"),N("reign"),_of(o)))),    
    ]),
    "inOfficeWhilePresident":(50,True,[    
        lambda o:VP(V("serve").t("ps"),
                    SP(C("while"),o,VP(V("be").t("ps"),N("president").cap(True)))),    
    ]),
    "inOfficeWhilePrimeMinister":(50,True,[    
        lambda o:VP(V("serve").t("ps"),
                    SP(C("while"),o,VP(V("be").t("ps"),A("prime").cap(True),N("minister").cap(True)))),    
    ]),
    "inOfficeWhileVicePresident":(50,True,[    
        lambda o:VP(V("serve").t("ps"),
                    SP(C("while"),o,VP(V("be").t("ps"),P("vice").cap(True),N("president").cap(True)))),    
    ]),
    "instrument":(50,True,[
        lambda o:(VP(V("be"),NP(D("a"),N("singer"))) if o.lemma=="Singing"
                  else VP(V("play"),NP(D("the"),o)))
    ]),
    "isPartOf":(50,False,[    
        lambda o:VP(V("be"),NP(D("a"),N("part"),_of(o))),    
    ]),
    "isPartOfMilitaryConflict":(50,False,[    
        lambda o:VP(V("be"),_during(NP(D("the"),o,N("conflict")))),    
    ]),
    "isbnNumber":(50,False,[    
        lambda o:number("ISBN",o),    
    ]),
    "issnNumber":(50,False,[    
        lambda o:number("ISSN",o),    
    ]),
    "keyPerson":(40,True,"leader"),
    "language":(50,True,[	
        lambda o:VP(V("speak"),o),
    ]),	
    "largestCity":(32,False,[	
        lambda o:VP(V("have"),o,Adv("as"),D("my").g("n"),A("large").f("su"),N("city")),
    ]),
    "launchSite":(30,False,[
        lambda o:VP(V("be").t("ps"),V("launch").t("pp"),_from(o)),
    ]),	
    "leader":(40,False,[
        lambda o:VP(V("be"),V("lead").t("pp"),_by(o)),	
        lambda o:VP(V("have"),o,_as(N("leader"))),	
        lambda o:VP(V("be"),V("run").t("pp"),_by(o)),
    ]),
    "leaderParty":(42,False,[
        lambda o:VP(V("lead").t("pr"),N("party"),V("be"),o),
    ]),	
    "leaderTitle":(41,False,[	
        lambda o:VP(V("be"),V("lead").t("pp"),_by(o)),	
        lambda o:VP(V("be"),V("govern").t("pp"),_by(o)),	
    ]),	
    "league":(50,True,[	
        lambda o:VP(V(oneOf("be","play","compete")),_in(NP(D("the"),o,N("league")))),	
    ]),
    "length":(30,False,[
        lambda o:VP(V("have"),NP(D("a"),N("length"),_of(o))),
        lambda o:VP(V("measure"),o),
    ]),	
    "LCCN_number":(50,False,[	
        lambda o:number("LCCN",o),	
    ]),
    "location":(30,False,[	
        lambda o:VP(V("be"),V("locate").t("pp"),_in(o)),	
        lambda o:VP(V("be"),V("locate").t("pp"),_inside(o)),	
        lambda o:VP(V("be"),V("base").t("pp"),_in(o)),
    ]),
    "locationIdentifier":(50,False,[	
        lambda o:VP(V("have"),NP(D("the"),N("location"),Q("identifier"),o)),	
    ]),
    # "locationCity":(30,False,"location"),
    "maidenFlight":(25,False,[
        lambda o:VP(V("make").t("ps"),D("my"),A(oneOf("first","maiden")),N("flight"),_on(o)),
    ]),
    "mainIngredient":(45,False,[	
        lambda o:VP(V("contain"),Adv("mainly"),o),	
    ]),
    "manager":(20,False,[
        lambda o:VP(V("be"),V("manage").t("pp"),_by(o)),	
        lambda o:VP(V("have"),o,Adv("as"),N("manager")),
    ]),
    "manufacturer":(40,False,[
        lambda o:VP(V("be"),V("manufacture").t("pp"),_by(o)),
    ]),
    "mass":(50,False,[
        lambda o:VP(V("have"),NP(D("a"),N("mass"),_of(o))),
        lambda o:VP(V("weight"),o)
    ]),	
    "material":(50,False,[    
        lambda o:VP(V("be"),V("make").t("pp"),_of(o)),    
        lambda o:VP(V("be"),V("build").t("pp"),_out(P("of"),o)),    
    ]),    
    "mediaType":(40,False,[    
        lambda o:VP(V("be"),A("available"),_in(o)),    
        lambda o:VP(V("appear").t("ps"),_in(o)),    
    ]),    
    "militaryBranch":(30,True,[	
        lambda o:VP(V("serve").t("ps"),_in(o)),    
        lambda o:VP(V("be").t("ps"),NP(D("a"),N("member"),_of(o))),    
    ]),
    "mission":(22,True,[	
        lambda o:VP(V("be").t("ps"),D("a"),N("crew"),N("member"),_of(o)),	
        lambda o:VP(V("become").t("ps"),N("member"),_of(o)),
    ]),
    "municipality":(30,False,"city"),	
    "musicFusionGenre":(50,False,[
        lambda o:VP(V("be"),D("a"),A("musical"),N("fusion"),_of(o)),
    ]),	
    "nationality":(1,True,[	
            lambda o:VP(V("be"),NP(D("a"),N(countries[o.lemma]))) 
                             if isinstance(o,Terminal) and o.lemma in countries else
                     VP(V("be"),NP(D("a"),N("citizen"),P("of"),o)),
            lambda o:NP(D("a"),N(countries[o.lemma])) 
                             if isinstance(o,Terminal) and o.lemma in countries else 
                        NP(D("a"),N("citizen"),P("of"),o),
            lambda o:VP(V("live"),_in(o)),	
    ]),	
    "netIncome":(21,False,[	
        lambda o:VP(V("earn").t("ps"),NP(NO(o.lemma),N("dollar"))),	
        lambda o:VP(V("have").t("ps"),NP(D("a"),N("revenue"),_of(NP(NO(o.lemma),N("dollar"))))),	
    ]),
    "nickname":(30,True,[
        lambda o:VP(V("have"),NP(D("the"),N("nickname"),o)),
        lambda o:VP(V("be"),Adv("also"),V("nickname").t("pp"),o),
    ]),
    # "numberOf(.*)": voir genSentComp
    "occupation":(50,True,[	
        lambda o:VP(V("be").t("ps"),NP(D("a"),o)),	
        lambda o:VP(V("serve").t("ps"),_as(D("a"),o)),	
        lambda o:VP(V("go").t("ps"),P("on"),P("to"),V("work").t("b"),P("as"),NP(D("a"),o)),	
    ]),
    "oclcNumber":(50,False,[	
        lambda o:number("OCLC",o),	
    ]),
    "office":(30,True,[
        lambda o:VP(V("work").t("ps"),_at(o))
    ]),
    "officialLanguage":(40,False,[
        lambda o:VP(V("have"),o,_as(NP(A("official"),N("language")))),
    ]),	
    "operatingOrganisation":(50,False,"operator"),
    "operator":(51,True,[	
        lambda o:VP(V("be"),V("operate").t("pp"),_by(o)),	
    ]),	
    "orbitalPeriod":(30,False,[
        lambda o:VP(V("have"),NP(D("a"),A("orbital"),N("period"),_of(o)))
    ]),
    "order":(30,False,[
        lambda o:VP(V("be"),NP(oneOf(N("part"),Q("")),_of(NP(D("the"),N("order"),_of(o))))),
    ]),
    "origin":(2,True,[
        lambda o:VP(V("be"),_from(o))
    ]),
    "owner":(30,False,[
        lambda o:VP(V("be"),V("own").t("pp"),_by(o))
    ]),
    "parentCompany":(30,False,"owner"),
    "party":(40,True,[
        lambda o:VP(V("be"),NP(D("a"),N("member"),_of(o))),
        lambda o:VP(V("belong"),_to(NP(D("the"),N("party"),o))),
    ]),
    "periapsis":(30,False,[
        lambda o:VP(V("have"),NP(D("a"),Q("periapsis"),_of(o)))
    ]),
    "populationDensity":(40,False,[
        lambda o:VP(V("have"),NP(D("a"),N("population"),N("density"),_of(o))),
    ]),
    "powerType":(50,False,[
        lambda o:VP(V("be"),V("power").t("pp"),_by(NP(D("a"),o,N("engine"))))
    ]),
    "precededBy":(50,False,[	
        lambda o:VP(V("be"),V("precede").t("pp"),_by(o)),	
    ]),
    "president":(20,True,[
        lambda o:VP(V("be"),V("preside").t("pp"),_by(o)),	
        lambda o:VP(V("have"),o,Adv("as"),N("president")),
    ]),	
    "product":(50,False,[	
        lambda o:VP(V("offer"),N("product").n("p"),D("such"),D("as"),o),	
        lambda o:VP(V("be"),D("a"),N("manufacturer"),_of(o)),	
        lambda o:VP(V("produce"),o),	
    ]),
    "productionStartYear":(30,False,[
        lambda o:VP(N("production"),V("start").t("ps"),_in(o)),
    ]),
    "position":(40,False,[
        lambda o:VP(V(oneOf("play","compete")),_in(o)),
    ]),
    "publisher":(45,False,[
        lambda o:VP(V("be"),V("publish").t("pp"),_by(o))
    ]),
    "recordLabel":(45,True,[
        lambda o:VP(V("record"),_for(o)),
        lambda o:VP(V("be").t(oneOf("p","ps")),V("sign").t("pp"),_by(o)).typ({"perf":oneOf(True,False)})
    ]),	
    "region":(35,True,"city"),    
    "regionServed":(50,True,[    
        lambda o:VP(V("provide"),NP(D("my"),N("service").n("p"),_in(o))),    
    ]),    
    "relatedMeanOfTransportation":(50,False,[    
        lambda o:VP(V("be"),NP(D("a"),V("relate").t("pp"),N("mean"),
                               _of(N("transportation"),P("with"),o))),    
    ]),    
    "representative":(50,False,[	
        lambda o:VP(V("be"),V("represent").t("pp"),_by(o)),	
    ]),
    "residence":(50,True,[
        lambda o:VP(V(oneOf("live","reside")),_in(o)),
    ]),
    "river":(50,False,[
        lambda o:VP(V("have"),NP(D("a"),N("river"),o)),
    ]),
    "rotationPeriod":(50,True,[
        lambda o:VP(V("have"),NP(D("a"),N("rotation"),N("period"),_of(o)))
    ]),
    "runwayLength":(50,False,[    
        lambda o:VP(V("have"),NP(D("a"),N("runway"),N("length"),_of(NP(NO(o.lemma),N("metre"))))),    
    ]),    
    "runwayName":(49,False,[    
        lambda o:VP(V("have"),NP(D("a"),N("runway"),V("name").t("pp"),o)),    
    ]),    
    "season":(50,True,[    
        lambda o:VP(V("play").t("ps"),_in(NP(D("the"),o,N("season")))),    
    ]),    
    "selectedByNasa":(21,True,[	
        lambda o:VP(V("be").t("ps"),V(oneOf("choose","hire","select")).t("pp"),_by(Q("NASA"),P("in"),o)),	
        lambda o:VP(V("join").t("ps"),Q("NASA"),_in(o)),	
    ]),	
    "senators":(50,False,[	
        lambda o:_with(o,P("as"),N("senator")),
        lambda o:SP(Pro("which").pe(3),VP(V("have"),o,P("as"),N("senator"))),
    ]),
    "series":(50,False,[
        lambda o:VP(V("be"),NP(D("a"),N("character"),_in(o)))
    ]),	
    "service":(50,False,[	
        lambda o:VP(V("operate"),_in(NP(D("the"),N("area"),_of(o)))),	
        lambda o:VP(V("be"),A("active"),_in(NP(D("the"),N("area"),_of(o)))),	
    ]),
    "servingTemperature":(50,False,[
        lambda o:VP(V("shall").t("ps"),V("be").t("b"),V("serve").t("pp"),o)
    ]),
    "shipBeam":(50,False,[    
        lambda o:VP(V("have"),NP(D("a"),N("ship"),N("beam"),_of(o))),    
    ]),    
    "shipDisplacement":(50,False,[    
        lambda o:VP(V("have"),NP(D("a"),N("ship"),N("displacement"),_of(o))),    
    ]),    
    "spokenIn":(50,False,[	
        lambda o:VP(V("be"),V("speak").t("pp"),_in(o)),	
    ]),
    "spouse":(30,True,[
        lambda o:VP(V("be"),V("marry").t("pp"),_to(o))
    ]),
    "starring":(35,False,[	
        lambda o:VP(V("star").t("ps"),o),	
    ]),	
    "state":(31,False,"city"),
    "status":(95,True,[	
        lambda o:VP(V("be"),Adv("now"),oneOf(D("a"),Q("")),o),	
    ]),	
    "stylisticOrigin":(50,False,[
        lambda o:VP(V("originate"),_from(o)),	
        lambda o:VP(V("be"),V("derive").t("pp"),_from(o)),	
    ]),	
    "successor":(60,True,[
        lambda o:VP(V("be").t("ps"),V("succeed").t("pp"),_by(o)),
    ]),
    "tenant":(50,False,[
        lambda o:VP(V("be"),NP(D("the"),N("tenant"),_of(o))),
    ]),
    "temperature":(50,False,[
        lambda o:VP(V("have"),NP(D("a"),N("temperature"),_of(o)))
    ]),
    "timeInSpace":(24,True,[	
        lambda o:VP(V("spend").t("ps"),o,_in(N("space"))),	
    ]),
    "title":(95,True,"status"),
    "topSpeed":(50,False,[
        lambda o:VP(V("have"),NP(D("a"),N("top"),N("speed"),_of(o)))
    ]),
    "transmission":(50,False,[
        lambda o:VP(V("have"),NP(D("a"),o,N("transmission"))),
    ]),	
    "type":(10,False,[	
        lambda o:VP(V("be"),NP(D("a"),o)),
        lambda o:VP(V("be"),NP(D("a"),N("kind"),P("of"),o)),
    ]),
    "unit":(30,True,[
        lambda o:VP(V("serve").t("ps"),_in(o))
    ]),
    "utcOffset":(20,False,[
        lambda o:VP(V("have"),NP(D("a"),Q("UTC offset"),_of(o))),
    ]),
    "wasGivenTheTechnicalCampusStatusBy":(25,False,[
        lambda o:VP(V("be").t("ps"),V("give").t("pp"),
                    NP(D("the"),A("technical"),N("campus"),N("status"),_by(o))),
    ]),
    "weight":(50,True,[
        lambda o:VP(V("have"),NP(D("a"),N("weight"),_of(o))),
        lambda o:VP(V("weight"),o)
    ]),
    "wheelBase":(50,False,[
        lambda o:VP(V("have"),NP(D("a"),N("wheelbase"),_of(o)))
    ]),
    "writer":(40,True,"author"),
    "youthclub":(30,True,[
        lambda o:VP(V("belong"),_to(NP(D("the"),N("youth"),N("club"),o)))
    ]),
}

## predicates that can be combined using only their complements
predicateGroups = [
         ["birthDate","birthPlace"],
         ["deathDate","deathPlace"],
         ["foundingDate","foundationPlace"],
         ["numberOfStudents","academicStaffSize","numberOfPostgraduateStudents"],
         ["orbitalPeriod","periapsis","apoapsis"],
        ]
## add indirect realizers to this list
headRs={}
for r in sentencePatterns:
    (_,_,rr)=sentencePatterns[r]
    if isinstance(rr,str):
        if rr in headRs:
            headRs[rr].append(r)
        else:
            headRs[rr]=[r]
for r in headRs:
    predicateGroups.append([r]+headRs[r])
# print("\n".join([str(p) for p in predicateGroups]))

## taken from https://www.geeksforgeeks.org/python-split-camelcase-string-to-individual-strings/
#$  camel_case_split:: str -> [str]
def camel_case_split(s): 
    return list(map(str.lower,re.findall(r'([A-Z]+|[A-Z]?[a-z]+)(?=[A-Z]|\b)', s)))

def getPrecedence(p):
    # special cases (the same as in getSentPattern)
    if p.startswith("hasToIts "):return 30
    if p.startswith("numberOf"):return 21
    if "Runway" in p: return 30+int(p[0])
    if p in sentencePatterns: return sentencePatterns[p][0]
    return 50

def runway(no,type):
    precedence=30+int(no[0])
    if type=="Number":
        return (precedence,False,[lambda o:VP(V("have"),o,_as(Q(no),N("runway")))])
    if type.startswith("Length"):
        unit=type[6:]
        return (precedence,False,
                [lambda o:VP(V("have"),NP(D("a"),Q(no),N("runway"),
                                 _of(NO(o.lemma),N("metre" if unit=="Metre" else "foot"))))])
    if type=="SurfaceType":
        return (precedence,False,
                [lambda o:VP(V("have"),NP(D("my"),Q(no),N("runway")),_in(o))])
    print ("@@@ strange runway:%s,%s"%(no,type))
    return None
#
#####
##    the main function:
##      given a predicate, returns a list of sentence patterns
##                  i.e a lambda comprising a VP with an embedded object

nbDefaultRealizers=0

def getNbDefaultRealizers():
    global nbDefaultRealizers
    return nbDefaultRealizers

### modified predicates names that should never occur now, 
### but useful when processing the test data set for 2017 for diminishing the number of use of
###      the default template, but does not change the score much
### table created from challenge2020_train_dev/property_revised_mapping.csv
modifiedPredicates = {
    "added to the National Register of Historic Places":"addedToTheNationalRegisterOfHistoricPlaces",
    "affiliations":"affiliation",
    "alternativeName":"alternativeName",
    "compete in":"competeIn",
    "battles":"battle",
    "CODEN_code":"codenCode",
    "LibraryofCongressClassification":"libraryofCongressClassification",
    "backup pilot":"backupPilot",
    "deathDate":"deathDate",
    "EISSN_number":"eissnNumber",
    "elevationAboveTheSeaLevel_(in_metres)":"elevationAboveTheSeaLevel",
    "elevationAboveTheSeaLevel_(in_feet)":"elevationAboveTheSeaLevelInFeet",
    "elevationAboveTheSeaLevel_(in_metres)":"elevationAboveTheSeaLevelInMetres",
    "ethnicGroup":"ethnicGroup",
    "was given the 'Technical Campus' status by":"wasGivenTheTechnicalCampusStatusBy",
    "fullname":"fullName",
    "headquarters":"headquarter",
    "hometown":"origin",
    "IATA_Location_Identifier":"iataLocationIdentifier",
    "ICAO_Location_Identifier":"icaoLocationIdentifier",
    "mainIngredients":"mainIngredient",
    "ISBN_number":"isbnNumber",
    "ISSN_number":"issnNumber",
    "languages":"language",
    # "LCCN_number":"lccnNumber", # was not changed
    "leaderName":"leader",
    "mainIngredients":"mainIngredient",
    "was a crew member of":"mission",
    "has to its north":"hasToItsNorth",
    "has to its northeast":"hasToItsNortheast",
    "has to its northwest":"hasToItsNorthwest",
    "ReferenceNumber in the National Register of Historic Places":"NationalRegisterOfHistoricPlacesReferenceNumber",
    "OCLC_number":"oclcNumber",
    "office (workedAt, workedAs)":"office",
    "placeOfBirth":"birthPlace",
    "placeOfDeath":"deathPlace",
    "1st_runway_LengthFeet":"1stRunwayLengthFeet",
    "1st_runway_LengthMetre":"1stRunwayLengthMetre",
    "1st_runway_Number":"1stRunwayNumber",
    "1st_runway_SurfaceType":"1stRunwaySurfaceType",
    "2nd_runway_SurfaceType":"2ndRunwaySurfaceType",
    "3rd_runway_LengthFeet":"3rdRunwayLengthFeet",
    "3rd_runway_SurfaceType":"3rdRunwaySurfaceType",
    "4th_runway_LengthFeet":"4thRunwayLengthFeet",
    "4th_runway_SurfaceType":"4thRunwaySurfaceType",
    "5th_runway_Number":"5thRunwayNumber",
    "5th_runway_SurfaceType":"5thRunwaySurfaceType",
    "was awarded":"ribbonAward",
    "was selected by NASA":"selectedByNasa",
    "has to its southeast":"hasToItsSoutheast",
    "has to its southwest":"hasToItsSouthwest",
    "sportsGoverningBody":"sportGoverningBody",
    "isPartOf":"isPartOf",
    "sportsGoverningBody":"sportGoverningBody",
    "UTCOffset":"utcOffset",
    "has to its west":"hasToItsWest",
    "served as Chief of the Astronaut Office in":"servedAsChiefOfTheAstronautOfficeIn",
}

#$ getSentPatterns::str ->  (int, [Constituent->Phrase] )
def getSentPatterns(p):
    # special cases...
    if p.startswith("hasToIts"):
        direction = p[8:].lower()
        return (50,False,[lambda o:VP(V("have"),o,_to(D("my").g("n"),Q(direction)))])
    m=re.fullmatch(r'numberOf(.*)',p)
    if m!=None:
        entities=Q(" ".join(camel_case_split(m.group(1))))
        return (50,False,[lambda   o:VP(V("have"),NP(NO(o.lemma),entities))])
    m=re.fullmatch(r"(\d\w\w)Runway(.*)",p)
    if m!=None:
        return runway(m.group(1),m.group(2))
    if p in sentencePatterns:
        (prec,isHuman,pats)=sentencePatterns[p]
        if isinstance(pats,str):
            (prec,isHuman,pats)=sentencePatterns[pats] # deal with indirection (does not check circularity!!)
        return (prec,isHuman,pats)
    if p in modifiedPredicates: ## check for "old" predicates for the 2017 test set
        return getSentPatterns(modifiedPredicates[p])
    return getDefaultPattern(p)

def getDefaultPattern(p):
    global nbDefaultRealizers
    print("@@@ Default realizer for: "+p)
    nbDefaultRealizers+=1
    if " " not in p and re.match(r'[A-Z]+[a-z]|[a-z]+[A-Z]',p): # check for dromadaryCase or CamelCase
        p=" ".join(camel_case_split(p))
    return (50,None,[lambda o:VP(q(p),V("be"),o)])

## check if p is a defined pattern
def hasPattern(p):
    return p.startswith("hasToIts") or re.fullmatch(r'numberOf(.*)',p) !=None or \
           re.fullmatch(r"(\d\w\w)Runway(.*)",p) or p in sentencePatterns or p in modifiedPredicates
        
def isHuman(p):
    if p in sentencePatterns:return sentencePatterns[p][1]
    return None

## unit test of all realizers with dummy subject and object
s = lambda:Q("*S*") # create a dummy subject
o = lambda:Q("*O*") #    "       "   object

def printReal(pat,s,o):
    print("   "+S(s,pat(o)).realize())
    
def showRealizations(p,s,o):
    (prec,isHuman,pats)=sentencePatterns[p]
    print("%s [%d]"%(p,prec),end="")
    if isHuman:
        print(" [human]",end="")
    if isinstance(pats,str):
        print(" => "+pats)
        (prec,_,pats)=sentencePatterns[pats]
    else:
        print()
    for pat in pats:
        printReal(pat,s,o)

if __name__ == '__main__':
    for p in sorted(sentencePatterns):
        showRealizations(p,s(),o())
    print("\nNB patterns:%d"%len(sentencePatterns))
    
    print("** Special cases **")
    printReal(getSentPatterns("numberOfEmployees")[2][0],s(),Q("1234"))
    for country in countries: # to exercise more possibilities
        printReal(getSentPatterns("nationality")[2][0],s(),Q(country))
    printReal(getSentPatterns("unknownPredicateOf")[2][0],s(),o())
    printReal(getSentPatterns("is a kind of")[2][0],s(),o())
    printReal(getSentPatterns("1stRunwaySurfaceType")[2][0],s(),o())
    printReal(getSentPatterns("3rdRunwayLengthFeet")[2][0],s(),o())
    printReal(getSentPatterns("5thRunwayNumber")[2][0],s(),o())
    printReal(getSentPatterns("5th_runway_Number")[2][0],s(),o())
    print("Default realizer was used: %5d times"%nbDefaultRealizers)
    