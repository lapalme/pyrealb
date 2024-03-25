from pyrealb import *
from Realizer import Realizer,_pp
from LexicalChoices import LexicalChoices

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

def _vpas(v): # create a simili passive verb
    return [V("be"), V(v).t("pp")]

def number(n,o):
    return VP(V("have"),NP(D("the"),Q(n),N("number"),o))


class English(Realizer,LexicalChoices):
    def __init__(self):
        loadEn()
        # self.lang = "en"
        # these attributes are used in Realizer
        # self.v_be = V("be")
        # self.conj_and = C("and")
        # self.pro_I = lambda: Pro("I") # as it will be modified create a new instance at each call
        # self.def_det = D("the")
        # self.undef_det = D("a")
        addToLexicon("last",{"Adv":{"tab":"b1"}}) # should be as Adv in the lexicon (as for first)...
        addToLexicon({"subgenre":{"N":{"tab":"n1"}}})
        addToLexicon("layout",{"N":{"tab":"n1"}}) # should replace lay-out !!
        super().__init__()

    ## used in "nationality" realizer to deal with special frequent cases
    countries = {"United_States": "American", "Canada": "Canadian", "France": "French", "Mexico": "Mexican"}

    @property
    def lang(self): return "en"

    @property
    def v_be(self): return V("be")

    @property
    def conj_and(self): return C("and")

    @property
    def pro_I(self): return lambda: Pro("I") # as it will be modified create a new instance at each call

    @property
    def def_det(self): return D("the")

    @property
    def undef_det(self): return D("a")

    def realize(self,graph,show):
        loadEn()
        return super().realize(graph,show)

    #### switch for precedence, isHuman, vp pattern
    ## precedence between 0 and 100 used for sorting predicates before realization
    ## isHuman : boolean indicating if this predicate applies to a human (useful for pronominalzation)
    # $ realizers::{str :  (int, bool, [Constituent->Phrase] | str)
    @property
    def sentence_patterns(self): return {
        "abbreviation": (50, False, [
            lambda o: VP(_vpas("abbreviate"), _by(o)),
        ]),
        "academicStaffSize": (50, False, [
            lambda o: VP(V("have"), D("a"), oneOf(A("academic"), Q("")), N("staff"), _of(Q(o.lemma)))
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
            lambda o: VP(_vpas("affiliate"), oneOf(_with(o), _to(o))),
        ]),
        "aircraftFighter":(50,False,[
            lambda o : VP(V(oneOf("have","use")),o,_as(NP(N("aircraft"),N("fighter"))))
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
        # "areaCode": (60, False, [
        #     lambda o: VP(V("have"), NP(D("the"), N("area"), N("code"), o)),
        # ]),
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
        "artist": (40, False, [
            lambda o: VP(V("be"),V("perform").t("pp"), _by(o)),
        ]),
        "assembly": (50, False, [
            lambda o: VP(_vpas("assemble"), _in(o)),
        ]),
        "associatedBand/associatedMusicalArtist": (50, True, [
            lambda o: VP(V(oneOf("play", "perform")), _with(o)),
        ]),
        "associatedRocket": (50, False, [  # $$$$ last
            lambda o: VP(_vpas("associate"), _with(D("the"), N("rocket"), o))
        ]),
        "attackAircraft": (50, False, [
            lambda o: VP(V("use"), NP(D("the"), o, _as(NP(N("attack"),N("aircraft"))))),
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
            lambda o: VP(_vpas(oneOf("build", "make")), _by(o))
        ]),
        "buildingStartDate": (15, False, [
            lambda o: VP(V("open").t("ps"), _on(o)),
            lambda o: VP(V("be").t("ps"), V("begin").t("pp"), _on(o)),
        ]),
        "campus": (21, False, [
            lambda o: VP(_vpas("locate"), _in(o)),
            lambda o: _in(o),
        ]),
        "capital": (30, False, [
            lambda o: VP(V("have"), o, Adv("as"), N("capital")),
            lambda o: _with(D("a"), N("capital"), _in(o)),
        ]),
        "category": (10, False, [
            lambda o: VP(_vpas("categorize"), _as(o)),
            lambda o: VP(V("fall"), P("under"), D("the"), N("category"), _of(o)),
        ]),
        "chairman": (50, True, [
            lambda o: VP(V("have"), o, P("as"), N("chairman")),
            lambda o: VP(_vpas("chair"), _by(o)),
        ]),
        "champions": (50, False, [
            lambda o: VP(Pro("where"), o, V("be").t("ps").n("p"), N("champion").n("p"))
        ]),
        "cinematography": (30, True, [
            lambda o: VP(V("have"),o,_as(NP(A("photographic"),N("director"))))
        ]),
        "citizenship" : (40, True, "residence"),
        "city": (30, False, [
            lambda o: VP(V("be"), _from(o)),
            lambda o: VP(_vpas("locate"), _in(o)),
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
            lambda o: VP(_vpas(oneOf("manage", "coach")), _by(o)),
        ]),
        # "codenCode": (50, False, [
        #     lambda o: VP(V("have"), NP(D("the"), Q("CODEN"), N("code"), _of(o)))
        # ]),
        "commander": (21, True, [
            lambda o: VP(_vpas("command"), _by(o)),
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
        "creator": (20, False, [
            lambda o: VP(V("be").t("ps"), V("create").t("pp"), _by(o)),
        ]),
        "crewMembers": (50, False, [
            lambda o: VP(V("have"), o, _as(N("crew"), N("member").n("p"))),
        ]),
        "currency": (60, False, [
            lambda o: VP(V("have"), o, _as(oneOf(Q(""), A("national")), N("currency"))),
        ]),
        "currentclub": (50, True, "club"),
        "currentTenants":(50,False,[
            lambda o: VP(Adv("currently"),V("house"),D("the"),o)
        ]),
        "dateOfRetirement": (90, True, [
            lambda o: VP(V("retire").t("ps"), _on(o)),
            lambda o: VP(V("go").t("ps"), P("into"), N("retirement"), _on(o)),
        ]),
        "dean": (20, False, [
            lambda o: VP(_vpas("lead"), _by(o)),
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
            lambda o: VP(_vpas("dedicate"), _to(o)),
        ]),
        "demonym": (50, False, [
            lambda o: VP(_vpas("inhabit"), _by(o)),
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
        "designCompany": (25, False, "designer"),
        "diameter": (40, False, [
            lambda o: VP(V("have"), NP(D("a"), N("diameter"), _of(o))),
            lambda o: VP(V("be"), o, _in(N("diameter"))),
        ]),
        "director": (25, False, [
            lambda o: VP(_vpas("direct"), _by(o)),
            lambda o: VP(V("have"),o, _as(N("director"))),
        ]),
        # "discover":(20,False,"discovery"),
        # "discoverer":(20,False,"discovery"),
        "discoverer": (20, False, [
            lambda o: VP(V("be").t("ps"), V("discover").t("pp"), _by(o))
        ]),
        "distributor": (60, False, [
            lambda o: VP(V("be").t("ps"), V("distribute").t("pp"), _by(o))
        ]),
        "dishVariation": (50, False, [
            lambda o: VP(V("be"), NP(D("a"), N("variation"), _of(o))),
        ]),
        "district": (30, False, [
            lambda o : VP(V("be"),_in(NP(D("the"),o,N("district"))))
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
        "editing": (42, False, "editor"),
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
        "firstAired" : (30,False,[
            lambda o: VP(V("be").t("ps"),Adv("first"),V("air").t("pp"),_on(o))
        ]),
        "floorArea": (50, False, [
            lambda o: VP(V("have"), NP(o,_as(N("floor"),N("area"))))
        ]),
        "floorCount": (50, False, [
            lambda o: VP(V("have"), NP(NO(o.lemma), N("floor"))),
        ]),
        "followedBy": (50, False, [
            lambda o: VP(_vpas("follow"), _by(o)),
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
        "governmentType": (50, False, "governingBody"),
        "governingBody": (50, False, [
            lambda o: VP(_vpas("govern"), _by(o)),
        ]),
        "gross":(60, False,[
            lambda o: VP(V("gross").t("ps"),NP(NO(o.lemma),N("dollar")))
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
        "influencedBy":(50, True, [
            lambda o: VP(V("be").t("ps"),V("influence").t("pp"),_by(o))
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
        "knownFor":(30, True,[
            lambda o: VP(V("be"),V("know").t("pp"),_for(o))
        ]),
        "language": (50, True, [
            lambda o: VP(V("speak"), o),
        ]),
        "largestCity": (32, False, [
            lambda o: VP(V("have"), o, Adv("as"), D("my").g("n"), A("large").f("su"), N("city")),
        ]),
        "lastAired" : (40,False,[
            lambda o: VP(V("be").t("ps"),Adv("last"),V("air").t("pp"),_on(o))
        ]),
        "latinName": (20,False, [
            lambda o: NP(o,VP(V("be").t("pr"),NP(D("my"),N("name"),A("Latin")))).b(","),
            lambda o: VP(V("have").t("pr"),o,_as(NP(N("name"),A("Latin"))))
        ]),
        "launchSite": (30, False, [
            lambda o: VP(V("be").t("ps"), V("launch").t("pp"), _from(o)),
        ]),
        "layout": (30,False,[
            lambda o: VP(V("have"),NP(D("a"),o,N("layout")))
        ]),
        "leader": (40, False, [
            lambda o: VP(_vpas("lead"), _by(o)),
            lambda o: VP(V("have"), o, _as(N("leader"))),
            lambda o: VP(_vpas("run"), _by(o)),
        ]),
        "leaderParty": (42, False, [
            lambda o: VP(V("lead").t("pr"), N("party"), V("be"), o),
        ]),
        "leaderTitle": (41, False, [
            lambda o: VP(_vpas("lead"), _by(o)),
            lambda o: VP(_vpas("govern"), _by(o)),
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
            lambda o: VP(_vpas("locate"), _in(o)),
            lambda o: VP(_vpas("locate"), _inside(o)),
            lambda o: VP(_vpas("base"), _in(o)),
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
            lambda o: VP(_vpas("manage"), _by(o)),
            lambda o: VP(V("have"), o, Adv("as"), N("manager")),
        ]),
        "manufacturer": (40, False, [
            lambda o: VP(_vpas("manufacture"), _by(o)),
        ]),
        "mass": (50, False, [
            lambda o: VP(V("have"), NP(D("a"), N("mass"), _of(o))),
            lambda o: VP(V("weight"), o)
        ]),
        "material": (50, False, [
            lambda o: VP(_vpas("make"), _of(o)),
            lambda o: VP(_vpas("build"), _out(P("of"), o)),
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
        "musicComposer": (30, False, [
            lambda o: VP(V("be").t("pp"), V("compose").t("pp"), _by(o)),
        ]),
        "musicFusionGenre": (50, False, [
            lambda o: VP(V("be"), D("a"), A("musical"), N("fusion"), _of(o)),
        ]),
        "musicSubgenre": (30, False, [
            lambda o: VP(V("have"),o,_as(N("subgenre")))
        ]),
        "nationality": (1, True, [
            lambda o: VP(V("be"), NP(D("a"), N(English.countries[o.lemma])))
                if isinstance(o, Terminal) and o.lemma in English.countries
                else VP(V("be"), NP(D("a"), N("citizen"), P("of"), o)),
            lambda o: NP(D("a"), N(English.countries[o.lemma]))
                if isinstance(o, Terminal) and o.lemma in English.countries
                else NP(D("a"), N("citizen"), P("of"), o),
            lambda o: VP(V("live"), _in(o)),
        ]),
        "NationalRegisterOfHistoricPlacesReferenceNumber":(10,False,[
            lambda o: number("National Register Of Historic Places Reference",o)
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
            lambda o: VP(_vpas("operate"), _by(o)),
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
            lambda o: VP(_vpas("own"), _by(o))
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
            lambda o: VP(_vpas("power"), _by(NP(D("a"), o, N("engine"))))
        ]),
        "position": (40, False, [
            lambda o: VP(V(oneOf("play", "compete")), _in(o)),
        ]),
        "precededBy": (50, False, [
            lambda o: VP(_vpas("precede"), _by(o)),
        ]),
        "predecessor": (20, True, [
            lambda o: VP(V("succeed").t("ps"),o)
        ]),
        "president": (20, True, [
            lambda o: VP(_vpas("preside"), _by(o)),
            lambda o: VP(V("have"), o, Adv("as"), N("president")),
        ]),
        "producer": (50, False, [
            lambda o: VP(V("be"),V("produce").t("pp"), _by(o))
        ]),
        "product": (50, False, [
            lambda o: VP(V("offer"), N("product").n("p"), D("such"), Adv("as"), o),
            lambda o: VP(V("be"), D("a"), N("manufacturer"), _of(o)),
            lambda o: VP(V("produce"), o),
        ]),
        "productionStartYear": (30, False, [
            lambda o: VP(N("production"), V("start").t("ps"), _in(o)),
        ]),
        "professionalField": (40, False, [
            lambda o: VP(V("work"), _in(o)),
        ]),
        "publisher": (45, False, [
            lambda o: VP(_vpas("publish"), _by(o))
        ]),
        "recordedIn":(20, False,[
            lambda o: VP(V("be").t("ps"),V("record").t("pp"),_in(o))
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
        "releaseDate": (40, False, [
            lambda o: VP(V("be").t("ps"), V("release").t("pp"), _on(o))
        ]),
        "religion": (50,False, [
            lambda o: VP(V("have"),o,_as(NP(D("a"),N("religion")))),
            lambda o: VP(V("have"),_as(N("religion")),o)
        ]),
        "representative": (50, False, [
            lambda o: VP(_vpas("represent"), _by(o)),
        ]),
        "residence": (40, True, [
            lambda o: VP(V(oneOf("live", "reside")), _in(o)),
        ]),
        "revenue" : (40, False,[
            lambda o: VP(V("have"),
                         NP(D("a"),N("revenue"),A("annual"),_of(NP(NO(o.lemma),N("dollar")))))
        ]),
        "river": (50, False, [
            lambda o: VP(V("have"), NP(D("a"), N("river"), o)),
        ]),
        "rotationPeriod": (50, True, [
            lambda o: VP(V("have"), NP(D("a"), N("rotation"), N("period"), _of(o)))
        ]),
        "runtime":(50, False, [
            lambda o: VP(V("run"),_for(NP(NO(o.lemma),N("minute"))))
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
            lambda o: VP(V("design").t("ps"), o.a(','), NP(D("a"), N("building"), A("significant")))
        ]),
        "site": (20, False, [
            lambda o: VP(V("be"),V("locate").t("pp"),_at(o))
        ]),
        "spokenIn": (50, False, [
            lambda o: VP(_vpas("speak"), _in(o)),
        ]),
        "spouse": (30, True, [
            lambda o: VP(_vpas("marry"), _to(o))
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
            lambda o: VP(_vpas("derive"), _from(o)),
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
        "timeZone": (42, False, [
            lambda o: VP(V("be"),A("situated"),_in(o))
        ]),
        "title": (95, True, "status"),
        "topSpeed": (50, False, [
            lambda o: VP(V("have"), NP(D("a"), N("top"), N("speed"), _of(o)))
        ]),
        "transmission": (50, False, [
            lambda o: VP(V("have"), NP(D("a"), o, N("transmission"))),
        ]),
        "transportAircraft": (50, False, [
            lambda o: VP(V("have"), NP(D("the"), o, _as(NP(N("transport"),N("aircraft"))))),
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
        "wheelbase": (50, False, [
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

    ## mapping of Wikidata property names to WebNLG property names
    ##  the value in comments shows the number of occurrences in "D2T-2-FA_Wikidata_Factual.xml
    @property
    def wikidata_properties(self): return {
        'AcademicDegree': "academicDiscipline",  # 30
        'Affiliation': "affiliation",  # 10
        'Anthem': "have_as anthem",  # 1
        'ArchivesAt': "be archived at_",  # 39
        'BloodType': "have_blood type",  # 6
        'CauseOfDeath': "die.ps_of",  # 106
        'CommissionedBy': "be commissioned by_",  # 1
        'Consecrator': "be consecrated by_",  # 5
        'Creator': "creator",  # 2
        'DateOfBirth': "birthDate",  # 534
        'DateOfDeath': "deathDate",  # 253
        'DepictedBy': "be depicted by_",  # 19
        'DifferentFrom': "be different from_",  # 19
        'Employer': "affiliation",  # 175
        'EndOfWorkPeriod': "activeYearsEndYear",  # 45
        'EthnicGroup': "ethnicGroup",  # 48
        'EyeColor': "have_eyes",  # 6
        'Family': "family",  # 53
        'FieldOfWork': "professionalField",  # 179
        'Genre': "genre",  # 136
        'HairColor': "have_hair",  # 5
        'HasChild': "have_as child",  # 333
        'HasFather': "have_as father",  # 281
        'HasGodparent': "have_as godparent",  # 3
        'HasMother': "have_as mother",  # 205
        'HasPet': "have_as pet",  # 4
        'HasWorksInTheCollectionOf': "have works in the collection of _",  # 80
        'InfluencedBy': "be influenced by_",  # 51
        'Instrument': "instrument",  # 78
        'InterestedIn': "be interested in _",  # 9
        'Lifestyle': "have_lifestyle",  # 6
        'MannerOfDeath': "die.ps of_",  # 78
        'Mass': "mass",  # 134
        'MedicalCondition': "have_as medical condition",  # 35
        'MilitaryRank': "militaryBranch",  # 33
        'Movement': "genre",  # 52
        'NamedAfter': "be named after_",  # 4
        'NativeLanguage': "language",  # 174
        'Nickname': "nickname",  # 29
        'NobleTitle': "title",  # 24
        'NominatedFor': "nominate.pp_for",  # 90
        'NotableWork': "knownFor",  # 175
        'NumberOfChildren': "have_children",  # 55
        'Occupation': "occupation",  # 1150
        'OfficialName': "fullName",  # 1
        'OwnerOf': "owner",  # 16
        'PartOf': "isPartOf",  # 15
        'ParticipantIn': "competeIn",  # 320
        'Penalty': "have penalty_",  # 2
        'PlaceOfBirth': "birthPlace",  # 647
        'PlaceOfBurial': "deathPlace",  # 138
        'PlaceOfDeath': "deathPlace",  # 329
        'PositionHeld': "position",  # 340
        'PresentInWork': "be present in _",  # 4
        'Pseudonym': "nickname",  # 41
        'Relative': "have_as relative",  # 37
        'ReligionOrWorldview': "religion",  # 120
        'ReligiousOrder': "religion",  # 6
        'RepresentedBy': "be represented by_",  # 4
        'ShortName': "nickname",  # 1
        'Sibling': "have_as sibling",  # 201
        'SocialClassification': "class",  # 6
        'Sponsor': "be sponsored by_",  # 6
        'Sport': "competeIn",  # 188
        'Spouse': "spouse",  # 324
        'Student': "be student of_",  # 49
        'StudentOf': "doctoralStudent",  # 86
        'SupportedSportsTeam': "support_",  # 4
        'TimePeriod': "timeInSpace",  # 9
        'UnmarriedPartner': "spouse",  # 47
        'VehicleNormallyUsed': "drive_",  # 1
        'Wears': "wear_",  # 3
        'WorkLocation': "location",  # 151
        'WritingLanguage': "language",  # 138
    }

    def rel_pro(self,isHuman):
        return Pro("who" if isHuman else "that")

    def direction(self,dir):
        return (50, False, [lambda o: VP(V("have"), o, _to(D("my").g("n"), Q(dir)))])

    def number_of(self,entities):
        return (50, False, [lambda o: VP(V("have"), NP(NO(o.lemma), entities))])

    def fix_language(self,term):
        return term.replace("_language","")

    def runway(self,no, type):
        precedence = 30 + int(no[0])
        if type == "Number":
            return (precedence, False, [lambda o: VP(V("have"), o, _as(Q(no), N("runway")))])
        if type.startswith("Length"):
            unit = type[6:]
            return (precedence, False,
                    [lambda o: VP(V("have"), NP(D("a"), Q(no), N("runway"),
                                                _of(NP(NO(o.lemma), N("metre" if unit == "Metre" else "foot")))))])
        if type == "SurfaceType":
            return (precedence, False,
                    [lambda o: VP(V("have"), NP(D("my"), Q(no), N("runway")), _in(o))])
        print("@@@ strange runway:%s,%s" % (no, type))
        return None

    def code(self,type):
        return  (60, False, [lambda o: VP(V("have"), NP(D("the"), Q(type), N("code"), o))])

if __name__ == '__main__':
    for pat in sorted(English().sentence_patterns.keys()):
        print(pat)