from pyrealb import *
from Realizer import Realizer,_pp

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

## used in "nationality" realizer to deal with special frequent cases
countries = {"United_States": "American", "Canada": "Canadian", "France": "French", "Mexico": "Mexican"}

class English(Realizer):
    def __init__(self):
        loadEn()
        self.v_be = V("be")
        self.conj_and = C("and")
        self.pro_I = lambda: Pro("I") # as it will be modified create a new instance at each call
        self.def_det = D("the")
        self.undef_det = D("a")
        super().__init__()


    def realize(self,graph,show):
        loadEn()
        return super().realize(graph,show)

    #### switch for precedence, isHuman, vp pattern
    ## precedence between 0 and 100 used for sorting predicates before realization
    ## isHuman : boolean indicating if this predicate applies to a human (useful for pronominalzation)
    # $ realizers::{str :  (int, bool, [Constituent->Phrase] | str)
    sentencePatterns = {
        "abbreviation": (50, False, [
            lambda o: VP(V("be"), V("abbreviate").t("pp"), _by(o)),
        ]),
        "academicStaffSize": (50, False, [
            lambda o: VP(V("have"), D("a"), oneOf(A("academic"), Q("")), N("staff"), _of(NO(o.lemma)))
        ]),
        "academicDiscipline": (50, False, [
            lambda o: VP(V("be"), NP(N("part"), _of(NP(D("the"), A("academic"), N("discipline"), _of(o))))),
        ]),
        "activeYearsEndDate": (70, True, "activeYearsEndYear"),
        "activeYearsEndYear": (70, True, [
            lambda o: VP(V("end").t("ps"), NP(D("my").g("m"), N("career"), _in(o))),
        ]),
        "activeYearsStartDate": (30, True, "activeYearsStartYear"),
        "activeYearsStartYear": (30, True, [
            lambda o: VP(V("start").t("ps"), NP(D("my").g("m"), N("career"), _in(o))),
        ]),
        "addedToTheNationalRegisterOfHistoricPlaces": (20, False, [
            lambda o: VP(V("be").t("ps"),V("add").t("pp"),
                         _to(NP(D("the"),A("national"),N("registry"),_of(NP(A("historic"),N("place")).n("p")))),
                         _in(o))
        ]),
        "address": (20, False, "location"),
        "affiliation": (20, False, [
            lambda o: VP(V("be"), V("affiliate").t("pp"), oneOf(_with(o), _to(o))),
        ]),
        # "affiliations":(20,True,"affiliation"),
        "almaMater": (20, True, [
            lambda o: VP(V("graduate").t("ps"), _from(o)),
            lambda o: VP(V("be").t("ps"), V("award").t("pp"), NP(D("a"), N("degree")), _from(o)),
            lambda o: VP(V("earn").t("ps"), NP(D("a"), N("degree")), _from(o)),
        ]),
        "alternativeName": (1, True, [
            lambda o: VP(V("be"), Adv("also"), V("call").t("pp"), o),
        ]),
        "anthem": (50, False, [
            lambda o: VP(V("have"), o, _as(N("anthem")))
        ]),
        "apoapsis": (30, False, [
            lambda o: VP(V("have"), NP(D("a"), Q("apoapsis"), _of(o)))
        ]),
        "areaOfLand": (50, False, [
            lambda o: VP(V(oneOf("cover", "have")), NP(D("a"), N("land"), N("area"), _of(o))),
        ]),
        "areaOfWater": (50, False, [
            lambda o: VP(V(oneOf("cover", "have")), NP(D("a"), N("water"), N("area"), _of(o))),
        ]),
        "areaTotal": (50, False, [
            lambda o: VP(V("have"), NP(D("a"), A("total"), N("area"), _of(o)))
        ]),
        "architect": (45, False, [
            lambda o: VP(V("be").t("ps"), V("design").t("pp"), _by(NP(D("the"), N("architect"), o)))
        ]),
        "architecturalStyle": (40, False, [
            lambda o: VP(V("be"), _in(NP(D("the"), A("architectural"), N("style"), o)))
        ]),
        "areaCode": (60, False, [
            lambda o: VP(V("have"), NP(D("the"), N("area"), N("code"), o)),
        ]),
        "assembly": (50, False, [
            lambda o: VP(V("be"), V("assemble").t("pp"), _in(o)),
        ]),
        "associatedBand/associatedMusicalArtist": (50, True, [
            lambda o: VP(V(oneOf("play", "perform")), _with(o)),
        ]),
        "associatedRocket": (50, False, [  # $$$$ last
            lambda o: VP(V("be"), V("associate").t("pp"), _with(D("the"), N("rocket"), o))
        ]),
        "author": (40, True, [
            lambda o: VP(V("be").t("ps"), V("write").t("pp"), _by(o)),
        ]),
        "averageSpeed": (60, False, [
            lambda o: VP(V("have"), NP(D("a"), N("average"), N("speed"), _of(o))),
        ]),
        "award": (53, True, "awards"),
        "awards": (53, True, [
            lambda o: VP(V("have"), V("be").t("pp"), V("award").t("pp"), o),
            lambda o: VP(V("win").t("ps"), o),
        ]),
        "background": (30, True, [
            lambda o: VP(V("have"), NP(D("a"), N("background"), _of(o))),
            lambda o: PP(P("with"), NP(D("a"), N("background"), _of(o))),
        ]),
        "backupPilot": (23, False, [
            lambda o: VP(V("have"), _as(oneOf(D("my").g("n"), Q("")), N("back-up"), N("pilot")), o),
            lambda o: VP(V("include").t("ps"), _as(N("back-up"), N("pilot"), o)),
        ]),
        "battle": (50, True, [
            lambda o: VP(V("be").t("ps"), V("involve").t("pp"), _in(NP(D("the"), N("battle"), _of(o)))),
            lambda o: VP(V("be").t("ps"), NP(N("part"), _of(o))),
        ]),
        "bird": (50, False, [
            lambda o: VP(V("have"), o, _as(A("official"), N("bird"))),
        ]),
        "birthDate": (2, True, [
            lambda o: VP(V("be").t("ps"), V("born").t("pp"), _on(o)),
        ]),
        "birthName": (2, True, [
            lambda o: VP(V("be").t("ps"), Adv(oneOf("first", "originally")), V("name").t("pp"), o),
        ]),
        "birthPlace": (3, True, [
            lambda o: VP(V("be").t("ps"), V("born").t("pp"), _in(o)),
        ]),
        "birthYear": (2, True, "birthPlace"),
        "bodyStyle": (50, False, [
            lambda o: VP(V("be"), D("a"), o)
        ]),
        "broadcastedBy": (40, False, [
            lambda o: VP(V("be").t("ps"), V("broadcast").t("pp"), _by(o)),
        ]),
        "builder": (10, False, [
            lambda o: VP(V("be"), V(oneOf("build", "make")).t("pp"), _by(o))
        ]),
        "buildingStartDate": (15, False, [
            lambda o: VP(V("open").t("ps"), _on(o)),
            lambda o: VP(V("be").t("ps"), V("begin").t("pp"), _on(o)),
        ]),
        "campus": (21, False, [
            lambda o: VP(V("be"), V("locate").t("pp"), _in(o)),
            lambda o: _in(o),
        ]),
        "capital": (30, False, [
            lambda o: VP(V("have"), o, Adv("as"), N("capital")),
            lambda o: _with(D("a"), N("capital"), _in(o)),
        ]),
        "category": (10, False, [
            lambda o: VP(V("be"), V("categorize").t("pp"), _as(o)),
            lambda o: VP(V("fall"), P("under"), D("the"), N("category"), _of(o)),
        ]),
        "chairman": (50, True, [
            lambda o: VP(V("have"), o, P("as"), N("chairman")),
            lambda o: VP(V("be"), V("chair").t("pp"), _by(o)),
        ]),
        "champions": (50, False, [
            lambda o: VP(Pro("where"), o, V("be").t("ps").n("p"), N("champion").n("p"))
        ]),
        "city": (30, False, [
            lambda o: VP(V("be"), _from(o)),
            lambda o: VP(V("be"), V("locate").t("pp"), _in(o)),
        ]),
        "cityServed": (50, False, [
            lambda o: VP(V("serve"), o),
        ]),
        "class": (50, False, [
            lambda o: VP(V("be"), NP(D("a"), o)),
        ]),
        "club": (50, True, [
            lambda o: VP(V("play").t("ps"), _for(o)),
            lambda o: VP(V("be"), NP(D("a"), N("player"), _for(o))),
        ]),
        "coach": (50, True, [
            lambda o: VP(V("be"), V(oneOf("manage", "coach")).t("pp"), _by(o)),
        ]),
        "codenCode": (50, False, [
            lambda o: VP(V("have"), NP(D("the"), Q("CODEN"), N("code"), _of(o)))
        ]),
        "commander": (21, True, [
            lambda o: VP(V("be"), V("command").t("pp"), _by(o)),
        ]),
        "comparable": (20, False,[
            lambda o: VP(V("be"),A("comparable"),_to(o))
        ]),
        "competeIn": (50, True, [
            lambda o: VP(V("compete"), _in(o)),
            lambda o: VP(V("be"), N("part"), _of(o)),
        ]),
        "completionDate": (60, False, [
            lambda o: VP(V("be").t("ps"), V("complete").t("pp"), _in(o)),
        ]),
        "cost": (40, False, [
            lambda o: VP(V("cost"), o),
        ]),
        "country": (40, False, "city"),
        "countryOrigin": (10, True, [
            lambda o: VP(V("originate").t("ps"), _in(o))
        ]),
        "countySeat": (40, False, [
            lambda o: VP(V("be"), NP(D("the"), N("county"), N("seat"), _of(o))),
        ]),
        "course": (20, False, [
            lambda o: VP(V("be"), NP(D("a"), o)),
        ]),
        "creator": (50, False, [
            lambda o: VP(V("be").t("ps"), V("create").t("pp"), _by(o)),
        ]),
        "crewMembers": (50, False, [
            lambda o: VP(V("have"), o, _as(N("crew"), N("member").n("p"))),
        ]),
        "currency": (60, False, [
            lambda o: VP(V("have"), o, _as(oneOf(Q(""), A("national")), N("currency"))),
        ]),
        "currentclub": (50, True, "club"),
        "dateOfRetirement": (90, True, [
            lambda o: VP(V("retire").t("ps"), _on(o)),
            lambda o: VP(V("go").t("ps"), P("into"), N("retirement"), _on(o)),
        ]),
        "dean": (20, False, [
            lambda o: VP(V("be"), V("lead").t("pp"), _by(o)),
        ]),
        "deathDate": (99, True, [
            lambda o: VP(V("die").t("ps"), _on(o)),
            lambda o: VP(V("pass").t("ps"), Adv("away"), _on(o)),
        ]),
        "deathPlace": (100, True, [
            lambda o: VP(V("die").t("ps"), _in(o)),
            lambda o: VP(V("pass").t("ps"), Adv("away"), _in(o)),
        ]),
        "debutTeam": (30, True, [
            lambda o: VP(Adv("first"), V("play").t("ps"), _with(o)),
        ]),
        "dedicatedTo": (10, False, [
            lambda o: VP(V("be"), V("dedicate").t("pp"), _to(o)),
        ]),
        "demonym": (50, False, [
            lambda o: VP(V("be"), V("inhabit").t("pp"), _by(o)),
        ]),
        "density": (50, False, [
            lambda o: VP(V("have"), NP(D("a"), N("density"), _of(o)))
        ]),
        "derivative": (50, False, [
            lambda o: VP(V("derive").t("ps"), _into(o))
        ]),
        "designer": (25, False, [
            lambda o: VP(V("be").t("ps"), V("design").t("pp"), _by(o)),
            # lambda o: _by(D("my").g("n"), N("designer"), o),
        ]),
        "diameter": (40, False, [
            lambda o: VP(V("have"), NP(D("a"), N("diameter"), _of(o))),
            lambda o: VP(V("be"), o, _in(N("diameter"))),
        ]),
        "director": (25, False, [
            lambda o: VP(V("be").t("ps"), V("manage").t("pp"), _by(o)),
            lambda o: VP(V("have"),o, _as(N("director"))),
        ]),
        # "discover":(20,False,"discovery"),
        # "discoverer":(20,False,"discovery"),
        "discoverer": (20, False, [
            lambda o: VP(V("be").t("ps"), V("discover").t("pp"), _by(o))
        ]),
        "dishVariation": (50, False, [
            lambda o: VP(V("be"), NP(D("a"), N("variation"), _of(o))),
        ]),
        "division": (40, False, [
            lambda o: VP(V("have"), NP(D("a"), o, N("division")))
        ]),
        "doctoralStudent": (50, True, [
            lambda o: VP(V("supervise").t("ps"), o),
        ]),
        "draftTeam": (20, True, [
            lambda o: VP(V("be").t("ps"), V("draft").t("pp"), _by(o)),
        ]),
        "editor": (42, False, [
            lambda o: VP(V("be").t("ps"), V("edit").t("ps"), _by(o)),
        ]),
        "elevationAboveTheSeaLevel": (48, False, [
            lambda o: VP(V("be"), oneOf(V("locate").t("pp"), A("situated")),
                         NP(NO(o.lemma), N("metre"), _above(N("sea"), N("level"))))
        ]),
        "elevationAboveTheSeaLevelInFeet": (48, False, [
            lambda o: VP(V("be"), oneOf(V("locate").t("pp"), A("situated")),
                         NP(NO(o.lemma), N("foot"), _above(N("sea"), N("level"))))
        ]),
        "elevationAboveTheSeaLevelInMetres": (48, False, "elevationAboveTheSeaLevel"),
        "engine": (50, False, [
            lambda o: VP(V("have"), NP(D("a"), o)) if isinstance(o, Terminal) and o.lemma.endswith("engine")
            else VP(V("have"), NP(D("a"), o, N("engine")))
        ]),
        "epoch": (50, False, [
            lambda o: VP(V("have"), NP(D("a"), N("epoch"), N("date"), _of(o))),
        ]),
        "escapeVelocity": (50, False, [
            lambda o: (VP(V("have"), NP(D("a"), N("escape"), N("velocity"), _of(o))))
        ]),
        "established": (20, False, [
            lambda o: VP(V("be").t("ps"), V("establish").t("pp"), _in(o)),
            lambda o: VP(V("be").t("ps"), V("found").t("pp"), _in(o)),
        ]),
        "ethnicGroup": (50, False, [
            lambda o: VP(V("have"), NP(D("a"), A("ethnic"), N("group"), _of(o))),
        ]),
        "family": (50, False, [
            lambda o: VP(V("belong"), _to(D("the"), N("family"), _of(o))),
            lambda o: VP(V("be"), N("part"), _of(D("the"), o, N("family")))
        ]),
        "finalFlight": (75, False, [
            lambda o: VP(V("make").t("ps"), D("my"), oneOf(D("last"), A("final")), N("flight"), _on(o)),
        ]),
        "floorArea": (50, False, [
            lambda o: VP(V("have"), NP(o,_as(N("floor"),N("area"))))
        ]),
        "floorCount": (50, False, [
            lambda o: VP(V("have"), NP(NO(o.lemma), N("floor"))),
        ]),
        "followedBy": (50, False, [
            lambda o: VP(V("be"), V("follow").t("pp"), _by(o)),
        ]),
        "formerName": (2, False, [
            lambda o: VP(V("be").t("ps"), Adv("formerly"), V("know").t("pp"), _as(o)),
        ]),
        "formerTeam": (2, True, [
            lambda o: VP(V("start").t("ps"), _with(o)),
            lambda o: VP(V("play").t("ps"), Adv("formerly"), _with(o)),
        ]),
        "foundedBy": (2, False, "founder"),
        "founder": (2, False, [
            lambda o: VP(V("be").t("ps"), V(oneOf("create", "found")).t("pp"), _by(o)),
        ]),
        "foundingDate": (2, False, [
            lambda o: VP(V("be").t("ps"), V(oneOf("create", "found")).t("pp"), _on(o)),
        ]),
        "foundationPlace": (3, False, [
            lambda o: VP(V("be").t("ps"), V(oneOf("create", "found")).t("pp"), _in(o)),
        ]),
        "fullName": (3, False, [
            lambda o: VP(A("full"), N("name"), V("be"), o),
        ]),
        "genre": (50, True, [
            lambda o: VP(V(oneOf("play", "perform")), o),
        ]),
        "governingBody": (50, False, [
            lambda o: VP(V("be"), V("govern").t("pp"), _by(o)),
        ]),
        "ground": (50, True, [
            lambda o: VP(V("play"), _in(o)),
        ]),
        ## "has to its (.*)": voir genSentComp
        "headquarter": (25, False, [
            lambda o: VP(V("have"),NP(D("my"),N("headquarters"), _in(o))),
        ]),
        "height": (50, True, [
            lambda o: VP(V("have"), NP(D("a"), N("height"), _of(o), Q("m"))),
            lambda o: VP(V("be"), o, Q("m"), A("tall"))
        ]),
        "higher": (55, False, [
            lambda o: VP(V("be"), A("high").f("su"), _of(o)),
        ]),
        "icaoLocationIdentifier": (50, False, "locationIdentifier"),
        "inaugurationDate": (10, False, [
            lambda o: VP(V("be").t("ps"), V("inaugurate").t("pp"), _on(o)),
        ]),
        "industry": (50, False, [
            lambda o: VP(V("be"), _in(NP(D("the"), o))),
        ]),
        "ingredient": (25, False, [
            lambda o: VP(V("contain"), o),
            lambda o: VP(V("have"), o, P("as"), N("ingredient")),
        ]),
        "inOfficeWhileMonarch": (50, True, [
            lambda o: VP(V("serve").t("ps"), _during(NP(D("the"), N("reign"), _of(o)))),
        ]),
        "inOfficeWhilePresident": (50, True, [
            lambda o: VP(V("serve").t("ps"),
                         SP(C("while"), o, VP(V("be").t("ps"), N("president").cap(True)))),
        ]),
        "inOfficeWhilePrimeMinister": (50, True, [
            lambda o: VP(V("serve").t("ps"),
                         SP(C("while"), o, VP(V("be").t("ps"), A("prime").cap(True), N("minister").cap(True)))),
        ]),
        "inOfficeWhileVicePresident": (50, True, [
            lambda o: VP(V("serve").t("ps"),
                         SP(C("while"), o, VP(V("be").t("ps"), P("vice").cap(True), N("president").cap(True)))),
        ]),
        "instrument": (50, True, [
            lambda o: (VP(V("be"), NP(D("a"), N("singer"))) if o.lemma == "Singing"
                       else VP(V("play"), NP(D("the"), o)))
        ]),
        "isPartOf": (50, False, [
            lambda o: VP(V("be"), NP(D("a"), N("part"), _of(o))),
        ]),
        "isPartOfMilitaryConflict": (50, False, [
            lambda o: VP(V("be"), _during(NP(D("the"), o, N("conflict")))),
        ]),
        "isbnNumber": (50, False, [
            lambda o: number("ISBN", o),
        ]),
        "issnNumber": (50, False, [
            lambda o: number("ISSN", o),
        ]),
        "keyPerson": (40, True, "leader"),
        "language": (50, True, [
            lambda o: VP(V("speak"), o),
        ]),
        "largestCity": (32, False, [
            lambda o: VP(V("have"), o, Adv("as"), D("my").g("n"), A("large").f("su"), N("city")),
        ]),
        "latinName": (20,False, [
            lambda o: NP(o,VP(V("be").t("pr"),NP(D("my"),N("name"),A("Latin")))).b(","),
            lambda o: VP(V("have").t("pr"),o,_as(NP(N("name"),A("Latin"))))
        ]),
        "launchSite": (30, False, [
            lambda o: VP(V("be").t("ps"), V("launch").t("pp"), _from(o)),
        ]),
        "leader": (40, False, [
            lambda o: VP(V("be"), V("lead").t("pp"), _by(o)),
            lambda o: VP(V("have"), o, _as(N("leader"))),
            lambda o: VP(V("be"), V("run").t("pp"), _by(o)),
        ]),
        "leaderParty": (42, False, [
            lambda o: VP(V("lead").t("pr"), N("party"), V("be"), o),
        ]),
        "leaderTitle": (41, False, [
            lambda o: VP(V("be"), V("lead").t("pp"), _by(o)),
            lambda o: VP(V("be"), V("govern").t("pp"), _by(o)),
        ]),
        "league": (50, True, [
            lambda o: VP(V(oneOf("be", "play", "compete")), _in(NP(D("the"), o, N("league")))),
        ]),
        "legislature": (25, False,[
            lambda o : VP(V("have"), o, _as(N("legislature")))
        ]),
        "length": (30, False, [
            lambda o: VP(V("have"), NP(D("a"), N("length"), _of(o))),
            lambda o: VP(V("measure"), o),
        ]),
        "LCCN_number": (50, False, [
            lambda o: number("LCCN", o),
        ]),
        "location": (30, False, [
            lambda o: VP(V("be"), V("locate").t("pp"), _in(o)),
            lambda o: VP(V("be"), V("locate").t("pp"), _inside(o)),
            lambda o: VP(V("be"), V("base").t("pp"), _in(o)),
        ]),
        "locationIdentifier": (50, False, [
            lambda o: VP(V("have"), NP(D("the"), N("location"), Q("identifier"), o)),
        ]),
        # "locationCity":(30,False,"location"),
        "maidenFlight": (25, False, [
            lambda o: VP(V("make").t("ps"), D("my"), A(oneOf("first", "maiden")), N("flight"), _on(o)),
        ]),
        "mainIngredient": (45, False, [
            lambda o: VP(V("contain"), Adv("mainly"), o),
        ]),
        "manager": (20, False, [
            lambda o: VP(V("be"), V("manage").t("pp"), _by(o)),
            lambda o: VP(V("have"), o, Adv("as"), N("manager")),
        ]),
        "manufacturer": (40, False, [
            lambda o: VP(V("be"), V("manufacture").t("pp"), _by(o)),
        ]),
        "mass": (50, False, [
            lambda o: VP(V("have"), NP(D("a"), N("mass"), _of(o))),
            lambda o: VP(V("weight"), o)
        ]),
        "material": (50, False, [
            lambda o: VP(V("be"), V("make").t("pp"), _of(o)),
            lambda o: VP(V("be"), V("build").t("pp"), _out(P("of"), o)),
        ]),
        "mediaType": (40, False, [
            lambda o: VP(V("be"), A("available"), _in(o)),
            lambda o: VP(V("appear").t("ps"), _in(o)),
        ]),
        "militaryBranch": (30, True, [
            lambda o: VP(V("serve").t("ps"), _in(o)),
            lambda o: VP(V("be").t("ps"), NP(D("a"), N("member"), _of(o))),
        ]),
        "mission": (22, True, [
            lambda o: VP(V("be").t("ps"), D("a"), N("crew"), N("member"), _of(o)),
            lambda o: VP(V("become").t("ps"), N("member"), _of(o)),
        ]),
        "municipality": (30, False, "city"),
        "musicFusionGenre": (50, False, [
            lambda o: VP(V("be"), D("a"), A("musical"), N("fusion"), _of(o)),
        ]),
        "nationality": (1, True, [
            lambda o: VP(V("be"), NP(D("a"), N(countries[o.lemma])))
                if isinstance(o, Terminal) and o.lemma in countries
                else VP(V("be"), NP(D("a"), N("citizen"), P("of"), o)),
            lambda o: NP(D("a"), N(countries[o.lemma]))
                if isinstance(o, Terminal) and o.lemma in countries
                else NP(D("a"), N("citizen"), P("of"), o),
            lambda o: VP(V("live"), _in(o)),
        ]),
        "nativeName": (1,False,[
            lambda o : AP(Adv("originally"),oneOf(V("name").t("pp"),None),o).b(",")
        ]),
        "netIncome": (21, False, [
            lambda o: VP(V("earn").t("ps"), NP(NO(o.lemma), N("dollar"))),
            lambda o: VP(V("have").t("ps"), NP(D("a"), N("revenue"), _of(NP(NO(o.lemma), N("dollar"))))),
        ]),
        "nickname": (30, True, [
            lambda o: VP(V("have"), NP(D("the"), N("nickname"), o)),
            lambda o: VP(V("be"), Adv("also"), V("nickname").t("pp"), o),
        ]),
        # "numberOf(.*)": voir genSentComp
        "occupation": (50, True, [
            lambda o: VP(V("be").t("ps"), NP(D("a"), o)),
            lambda o: VP(V("serve").t("ps"), _as(D("a"), o)),
            lambda o: VP(V("go").t("ps"), P("on"), P("to"), V("work").t("b"), P("as"), NP(D("a"), o)),
        ]),
        "oclcNumber": (50, False, [
            lambda o: number("OCLC", o),
        ]),
        "office": (30, True, [
            lambda o: VP(V("work").t("ps"), _at(o))
        ]),
        "officialLanguage": (40, False, [
            lambda o: VP(V("have"), o, _as(NP(A("official"), N("language")))),
        ]),
        "operatingIncome": (21, False, "netIncome"),
        "operatingOrganisation": (50, False, "operator"),
        "operator": (51, True, [
            lambda o: VP(V("be"), V("operate").t("pp"), _by(o)),
        ]),
        "orbitalPeriod": (30, False, [
            lambda o: VP(V("have"), NP(D("a"), A("orbital"), N("period"), _of(o)))
        ]),
        "order": (30, False, [
            lambda o: VP(V("be"), NP(oneOf(N("part"), Q("")), _of(NP(D("the"), N("order"), _of(o))))),
        ]),
        "origin": (2, True, [
            lambda o: VP(V("be"), _from(o))
        ]),
        "owner": (30, False, [
            lambda o: VP(V("be"), V("own").t("pp"), _by(o))
        ]),
        "parentCompany": (30, False, "owner"),
        "party": (40, True, [
            lambda o: VP(V("be"), NP(D("a"), N("member"), _of(o))),
            lambda o: VP(V("belong"), _to(NP(D("the"), N("party"), o))),
        ]),
        "periapsis": (30, False, [
            lambda o: VP(V("have"), NP(D("a"), Q("periapsis"), _of(o)))
        ]),
        "populationDensity": (40, False, [
            lambda o: VP(V("have"), NP(D("a"), N("population"), N("density"), _of(o))),
        ]),
        "powerType": (50, False, [
            lambda o: VP(V("be"), V("power").t("pp"), _by(NP(D("a"), o, N("engine"))))
        ]),
        "precededBy": (50, False, [
            lambda o: VP(V("be"), V("precede").t("pp"), _by(o)),
        ]),
        "predecessor": (20, True, [
            lambda o: VP(V("succeed").t("ps"),o)
        ]),
        "president": (20, True, [
            lambda o: VP(V("be"), V("preside").t("pp"), _by(o)),
            lambda o: VP(V("have"), o, Adv("as"), N("president")),
        ]),
        "product": (50, False, [
            lambda o: VP(V("offer"), N("product").n("p"), D("such"), Adv("as"), o),
            lambda o: VP(V("be"), D("a"), N("manufacturer"), _of(o)),
            lambda o: VP(V("produce"), o),
        ]),
        "productionStartYear": (30, False, [
            lambda o: VP(N("production"), V("start").t("ps"), _in(o)),
        ]),
        "position": (40, False, [
            lambda o: VP(V(oneOf("play", "compete")), _in(o)),
        ]),
        "publisher": (45, False, [
            lambda o: VP(V("be"), V("publish").t("pp"), _by(o))
        ]),
        "recordLabel": (45, True, [
            lambda o: VP(V("record"), _for(o)),
            lambda o: VP(V("be").t(oneOf("p", "ps")), V("sign").t("pp"), _by(o)).typ({"perf": oneOf(True, False)})
        ]),
        "region": (35, True, "city"),
        "regionServed": (50, True, [
            lambda o: VP(V("provide"), NP(D("my"), N("service").n("p"), _in(o))),
        ]),
        "relatedMeanOfTransportation": (50, False, [
            lambda o: VP(V("be"), NP(D("a"), V("relate").t("pp"), N("mean"),
                                     _of(N("transportation"), P("with"), o))),
        ]),
        "representative": (50, False, [
            lambda o: VP(V("be"), V("represent").t("pp"), _by(o)),
        ]),
        "residence": (50, True, [
            lambda o: VP(V(oneOf("live", "reside")), _in(o)),
        ]),
        "river": (50, False, [
            lambda o: VP(V("have"), NP(D("a"), N("river"), o)),
        ]),
        "rotationPeriod": (50, True, [
            lambda o: VP(V("have"), NP(D("a"), N("rotation"), N("period"), _of(o)))
        ]),
        "runwayLength": (50, False, [
            lambda o: VP(V("have"), NP(D("a"), N("runway"), N("length"), _of(NP(NO(o.lemma), N("metre"))))),
        ]),
        "runwayName": (49, False, [
            lambda o: VP(V("have"), NP(D("a"), N("runway"), V("name").t("pp"), o)),
        ]),
        "season": (50, True, [
            lambda o: VP(V("play").t("ps"), _in(NP(D("the"), o, N("season")))),
        ]),
        "selectedByNasa": (21, True, [
            lambda o: VP(V("be").t("ps"), V(oneOf("choose", "hire", "select")).t("pp"), _by(Q("NASA"), P("in"), o)),
            lambda o: VP(V("join").t("ps"), Q("NASA"), _in(o)),
        ]),
        "senators": (50, False, [
            lambda o: _with(o, P("as"), N("senator")),
            lambda o: SP(Pro("which").pe(3), VP(V("have"), o, P("as"), N("senator"))),
        ]),
        "series": (50, False, [
            lambda o: VP(V("be"), NP(D("a"), N("character"), _in(o)))
        ]),
        "service": (50, False, [
            lambda o: VP(V("operate"), _in(NP(D("the"), N("area"), _of(o)))),
            lambda o: VP(V("be"), A("active"), _in(NP(D("the"), N("area"), _of(o)))),
        ]),
        "servingTemperature": (50, False, [
            lambda o: VP(V("shall").t("ps"), V("be").t("b"), V("serve").t("pp"), o)
        ]),
        "shipBeam": (50, False, [
            lambda o: VP(V("have"), NP(D("a"), N("ship"), N("beam"), _of(o))),
        ]),
        "shipDisplacement": (50, False, [
            lambda o: VP(V("have"), NP(D("a"), N("ship"), N("displacement"), _of(o))),
        ]),
        "significantBuilding": (30, True, [
            lambda o: VP(V("design").t("pc"), o.a(','), NP(D("a"), N("building"), A("significant")))
        ]),
        "spokenIn": (50, False, [
            lambda o: VP(V("be"), V("speak").t("pp"), _in(o)),
        ]),
        "spouse": (30, True, [
            lambda o: VP(V("be"), V("marry").t("pp"), _to(o))
        ]),
        "starring": (35, False, [
            lambda o: VP(V("star").t("ps"), o),
        ]),
        "state": (31, False, "city"),
        "status": (95, True, [
            lambda o: VP(V("be"), Adv("now"), oneOf(D("a"), Q("")), o),
        ]),
        "stylisticOrigin": (50, False, [
            lambda o: VP(V("originate"), _from(o)),
            lambda o: VP(V("be"), V("derive").t("pp"), _from(o)),
        ]),
        "subsidiary": (10, False, [
            lambda o: VP(V("have"),o,_as(N("subsidiary")))
        ]),
        "successor": (60, True, [
            lambda o: VP(V("be").t("ps"), V("succeed").t("pp"), _by(o)),
        ]),
        "tenant": (50, False, [
            lambda o: VP(V("be"), NP(D("the"), N("tenant"), _of(o))),
        ]),
        "temperature": (50, False, [
            lambda o: VP(V("have"), NP(D("a"), N("temperature"), _of(o)))
        ]),
        "timeInSpace": (24, True, [
            lambda o: VP(V("spend").t("ps"), o, _in(N("space"))),
        ]),
        "title": (95, True, "status"),
        "topSpeed": (50, False, [
            lambda o: VP(V("have"), NP(D("a"), N("top"), N("speed"), _of(o)))
        ]),
        "transmission": (50, False, [
            lambda o: VP(V("have"), NP(D("a"), o, N("transmission"))),
        ]),
        "type": (10, False, [
            lambda o: VP(V("be"), NP(D("a"), o)),
            lambda o: VP(V("be"), NP(D("a"), N("kind"), P("of"), o)),
        ]),
        "unit": (30, True, [
            lambda o: VP(V("serve").t("ps"), _in(o))
        ]),
        "utcOffset": (20, False, [
            lambda o: VP(V("have"), NP(D("a"), Q("UTC offset"), _of(o))),
        ]),
        "wasGivenTheTechnicalCampusStatusBy": (25, False, [
            lambda o: VP(V("be").t("ps"), V("give").t("pp"),
                         NP(D("the"), A("technical"), N("campus"), N("status"), _by(o))),
        ]),
        "weight": (50, True, [
            lambda o: VP(V("have"), NP(D("a"), N("weight"), _of(o))),
            lambda o: VP(V("weight"), o)
        ]),
        "wheelBase": (50, False, [
            lambda o: VP(V("have"), NP(D("a"), N("wheelbase"), _of(o)))
        ]),
        "writer": (40, True, "author"),
        "yearOfConstruction": (1, False, [
            lambda o: VP(V("be").t("ps"),V("build").t("pp"), _in(o)),
        ]),
        "youthclub": (30, True, [
            lambda o: VP(V("belong"), _to(NP(D("the"), N("youth"), N("club"), o)))
        ]),
    }

    def rel_pro(self,isHuman):
        return Pro("who" if isHuman else "that")

    def direction(self,dir):
        return (50, False, [lambda o: VP(V("have"), o, _to(D("my").g("n"), Q(dir)))])

    def number_of(self,entities):
        return (50, False, [lambda o: VP(V("have"), NP(NO(o.lemma), entities))])

    def runway(self,no, type):
        precedence = 30 + int(no[0])
        if type == "Number":
            return (precedence, False, [lambda o: VP(V("have"), o, _as(Q(no), N("runway")))])
        if type.startswith("Length"):
            unit = type[6:]
            return (precedence, False,
                    [lambda o: VP(V("have"), NP(D("a"), Q(no), N("runway"),
                                                _of(NO(o.lemma), N("metre" if unit == "Metre" else "foot"))))])
        if type == "SurfaceType":
            return (precedence, False,
                    [lambda o: VP(V("have"), NP(D("my"), Q(no), N("runway")), _in(o))])
        print("@@@ strange runway:%s,%s" % (no, type))
        return None
