from pyrealb import *
from Realizer import Realizer,_pp
import random

## use star to allow more than two parameters to _pp
def _a(*o): return _pp("à", o)
def _a_l_interieur(*o): return _pp("à", NP(D("le"),N("intérieur"),P("de"),o))
def _au_dessus(*o): return AdvP(Adv("au-dessus"), _de(o))
def _avec(*o): return _pp("avec", o)
def _comme(*o): return _pp("comme", o)
def _dans(*o): return _pp("dans", o)
def _de(*o): return _pp("de", o)
def _durant(*o): return _pp("durant", o)
def _en(*o): return _pp("en",o)
def _hors_de(*o): return _pp("hors", P("de"), o)
def _par(*o): return _pp("par", o)
def _pour(*o): return _pp("pour", o)
def _sur(*o): return _pp("sur", o)
def _vers(*o): return _pp("vers", o)

def number(n, o): return VP(V("avoir"), NP(D("le"), N("numéro"), Q(n), o))

## used in "nationality" realizer to deal with special frequent cases
# countries = {"United_States": "Americain", "Canada": "Canadien", "France": "Français", "Mexico": "Mexicain"}

# countries to translate in French
#    english : (preposition, gender, number, franch name, inhabitant)
countries = {
    'Brazil' : ("à","m","s","Brésil","Brésilien"),
    'Brussels' : ("à","m","s","Bruxelles","Bruxellois"),
    'California' : ("en","f","s","Californie","Californien"),
    "Canada"  : ("à","m","s", "Canada", "Canadien"),
    'Denmark' : ("à", "m","s", "Danemark", "Danois"),
    'England' : ("en", "f", "s", "Angleterre", "Anglais"),
    "France"  : ("en", "f", "s", "France", "Français"),
    'India'   : ("à", "f","p", "Indes", "Indien"),
    "Mexico"  : ("à", "m","s", "Mexique", "Mexicain"),
    'Philippines' : ("à", "f","p","Philippines","Philippin"),
    'Romania' : ("en", "f","s", "Roumanie","Roumain"),
    'Spain' :  ("en", "f", "s", "Espagne", "Espagnol"),
    'Switzerland' : ("en", "f", "s", '"Suisse', "Suisse"),
    'Turkey' : ("en", "f", "s", "Turquie", "Turc"),
    "United States": ("à", "m", "p", "États-Unis", "Américain")
}

def pp_place(lemma):
    (prep, g, n, name, inhabitant) = countries[lemma]
    if prep=="à":
        return PP(P("à"),NP(D("le"),N(name)))
    else:
        PP(P("en"), N(name))


def place(o):
    if not isinstance(o,tuple):
        if isinstance(o,Q):
            return pp_place(o.lemma) if o.lemma in countries else _a(o)
        return o
    o0 = o[0]
    if not isinstance(o0,Q): return o
    res = pp_place(o0.lemma) if o0.lemma in countries else _a(o0)
    if len(o)==1:
        return res
    else: # HACK : make tuple of rest of arguments
        return tuple([res]+list(o[1:]))

def habite(o):
    if not isinstance(o,Terminal):return o
    if o.lemma in countries:
        (prep,g,n,name,inhabitant) = countries[o.lemma]
        if random.choice([True,False]):
            v = oneOf("habiter","vivre")
            VP(V(v),pp_place(o.lemma))
        else:
            return VP(V("être"),NP(D("un"),N(inhabitant)))
    else:
        return VP(V("habiter"),PP(P("en"),o))


class Francais(Realizer):
    def __init__(self):
        loadFr()
        addToLexicon("catégoriser",{"V":{"aux":"av", "tab":"v36", "pat":["tdir"]}})
        addToLexicon("compétitionner",{"V":{"aux":"av", "tab":"v36", "pat":["intr"]}})
        # ensure that all countries are in the French lexicnn
        for country in countries:
            (_,g,n,name,_) = countries[country]
            addToLexicon(name,{"N":{"g":g,"n":n,"tab":"nI"}})
        self.v_be = V("être")
        self.conj_and = C("et")
        self.pro_I = lambda: Pro("je") # as it will be modified create a new instance at each call
        self.def_det = D("le")
        self.undef_det = D("un")
        super().__init__()
    

    def realize(self,graph,show):
        loadFr()
        return super().realize(graph,show)

    #### switch for precedence, isHuman, vp pattern
    ## precedence between 0 and 100 used for sorting predicates before realization
    ## isHuman : boolean indicating if this predicate applies to a human (useful for pronominalzation)
    # $ realizers::{str :  (int, bool, [Constituent->Phrase] | str)
    sentencePatterns = {
        "abbreviation": (50, False, [
            lambda o: VP(V("être"), V("abréger").t("pp"), _en(o)),
        ]),
        "academicStaffSize": (50, False, [
            lambda o: VP(V("avoir"), D("un"), N("personnel"), oneOf(A("académique"), Q("")),
                         _de(NP(NO(o.lemma),N("personne"))))
        ]),
        "academicDiscipline": (50, False, [
            lambda o: VP(V("faire"), NP(N("partie"), _de(NP(D("le"), A("académique"), N("discipline"), _de(o))))),
        ]),
        "activeYearsEndDate": (70, True, "activeYearsEndYear"),
        "activeYearsEndYear": (70, True, [
            lambda o: VP(V("terminer").t("ps"), NP(D("mon").g("m"), N("carrière"), _en(o))),
        ]),
        "activeYearsStartDate": (30, True, "activeYearsStartYear"),
        "activeYearsStartYear": (30, True, [
            lambda o: VP(V("débuter").t("ps"), NP(D("mon").g("m"), N("carrière"), _en(o))),
        ]),
        "address": (20, False, "location"),
        "affiliation": (20, False, [
            lambda o: VP(V("être"), V("affilier").t("pp"), oneOf(_avec(o), _a(o))),
        ]),
        # "affiliations":(20,True,"affiliation"),
        "almaMater": (20, True, [
            lambda o: VP(V("obtenir").t("pc"), NP(D("mon"),N("diplôme")), _de(o)),
            lambda o: VP(V("terminer").t("pc"), NP(D("mon"), N("étude").n("p")), _a(o)),
            lambda o: VP(V("mériter").t("pc"), NP(D("un"), N("diplôme")), _de(o)).typ({"refl":True}),
        ]),
        "alternativeName": (1, True, [
            lambda o: VP(V("être"), Adv("aussi"), V("appeler").t("pp"), o),
        ]),
        "anthem": (50, False, [
            lambda o: VP(V("avoir"), o, _comme(N("hymne")))
        ]),
        "apoapsis": (30, False, [
            lambda o: VP(V("avoir"), NP(D("un"), Q("apoastre"), _de(o)))
        ]),
        "areaOfLand": (50, False, [
            lambda o: VP(V(oneOf("couvrir", "avoir")), NP(D("un"), N("superficie"), _de(o))),
        ]),
        "areaOfWater": (50, False, [
            lambda o: VP(V(oneOf("couvrir", "avoir")), NP(D("un"), N("superficie"), A("maritime"), _de(o))),
        ]),
        "areaTotal": (50, False, [
            lambda o: VP(V("avoir"), NP(D("un"), N("surface"), A("total"), _de(o)))
        ]),
        "architect": (45, False, [
            lambda o: VP(V("être").t("pc"), V("concevoir").t("pp"), _par(NP(D("le"), N("architecte"), o)))
        ]),
        "architecturalStyle": (40, False, [
            lambda o: VP(V("être"), _dans(NP(D("le"), N("style"), A("architectural"), o)))
        ]),
        "areaCode": (60, False, [
            lambda o: VP(V("avoir"), NP(D("le"), N("code"), A("régional"), o)),
        ]),
        "assembly": (50, False, [
            lambda o: VP(V("être"), V("assembler").t("pp"), _dans(o)),
        ]),
        "associatedBand/associatedMusicalArtist": (50, True, [
            lambda o: VP(V("jouer"), _avec(o)),
            lambda o: VP(V("produire"), _avec(o)).typ({"refl":True})
        ]),
        "associatedRocket": (50, False, [  # $$$$ last
            lambda o: VP(V("être"), V("associer").t("pp"), _avec(D("le"), N("fusée"), o))
        ]),
        "author": (40, True, [
            lambda o: VP(V("être").t("pc"), V("écrire").t("pp"), _par(o)),
        ]),
        "averageSpeed": (60, False, [
            lambda o: VP(V("avoir"), NP(D("un"), N("vitesse"), A("moyen"), _de(o))),
        ]),
        "award": (53, True, "awards"),
        "awards": (53, True, [
            lambda o: VP(V(oneOf("gagner","obtenir")).t("pc"), o),
        ]),
        "background": (30, True, [
            lambda o: VP(V("avoir"), NP(D("un"), N("formation"), _de(o))),
            lambda o: PP(P("avec"), NP(D("un"), N("formation"), _de(o))),
        ]),
        "backupPilot": (23, False, [
            lambda o: VP(V("avoir"), o, _comme(oneOf(D("mon").g("n"), Q("")), N("pilote"), PP(P("de"), N("réserve")))),
            lambda o: VP(V("compter").t("pc"), o,C("comme"),N("pilote"), PP(P("de"),N("réserve"))),
        ]),
        "battle": (50, True, [
            lambda o: VP(V("être").t("pc"), V("impliquer").t("pp"), _dans(NP(D("le"), N("bataille"), _de(o)))),
            lambda o: VP(V("faire").t("pc"), NP(N("partie"), _de(o))),
        ]),
        "bird": (50, False, [
            lambda o: VP(V("avoir"), o, _comme( N("oiseau"),A("officiel"))),
        ]),
        "birthDate": (2, True, [
            lambda o: VP(V("être").t("p"), V("naître").t("pp"), D("le"), o),
        ]),
        "birthName": (2, True, [
            lambda o: VP(V("être").t("ps"), Adv(oneOf("d'abord", "originalement")), V("nommer").t("pp"), o),
        ]),
        "birthPlace": (3, True, [
            lambda o: VP(V("être").t("p"), V("naître").t("pp"), place(o)),
        ]),
        "birthYear": (2, True, "birthDate"),
        "bodyStyle": (50, False, [
            lambda o: VP(V("être"), D("un"), o)
        ]),
        "broadcastedBy": (40, False, [
            lambda o: VP(V("être").t("pc"), V("diffuser").t("pp"), _par(o)),
        ]),
        "builder": (10, False, [
            lambda o: VP(V("être"), V(oneOf("construire", "ériger")).t("pp"), _par(o))
        ]),
        "buildingStartDate": (15, False, [
            lambda o: VP(V("ouvrir").t("pc"), _en(o)),
            lambda o: VP(V("être").t("pc"), V("débuter").t("pp"), _en(o)),
        ]),
        "campus": (21, False, [
            lambda o: VP(V("être"), V("situer").t("pp"), place(o)),
            lambda o: _dans(o),
        ]),
        "capital": (30, False, [
            lambda o: VP(V("avoir"), o, Adv("comme"), N("capitale")),
         ]),
        "category": (10, False, [
            lambda o: VP(V("être"), V("catégoriser").t("pp"), _comme(o)),
            lambda o: VP(V("tomber"), P("dans"), NP(D("le"), N("catégorie"), _de(o))),
        ]),
        "chairman": (50, True, [
            lambda o: VP(V("avoir"), o, P("comme"), N("président")),
            lambda o: VP(V("être"), V("présider").t("pp"), _par(o)),
        ]),
        "champions": (50, False, [
            lambda o: VP(Pro("où"), o, V("être").t("pc").n("p"), N("champion").n("p"))
        ]),
        "city": (30, False, [
            lambda o: VP(V("être"), place(o)),
            lambda o: VP(V("être"), V("situer").t("pp"), place(o)),
        ]),
        "cityServed": (50, False, [
            lambda o: VP(V("servir"), o),
        ]),
        "class": (50, False, [
            lambda o: VP(V("être"), NP(D("un"), o)),
        ]),
        "club": (50, True, [
            lambda o: VP(V("jouer").t("pc"), _pour(o)),
            lambda o: VP(V("être"), NP(D("un"), N("joueur"), _pour(o))),
        ]),
        "coach": (50, True, [
            lambda o: VP(V("être"), V(oneOf("gérer", "entraîner")).t("pp"), _par(o)),
        ]),
        "codenCode": (50, False, [
            lambda o: VP(V("avoir"), NP(D("le"), N("code"), Q("CODEN"), o))
        ]),
        "commander": (21, True, [
            lambda o: VP(V("être"), V("commander").t("pp"), _par(o)),
        ]),
        "compete in": (50, True, [
            lambda o: VP(V("compétionner"), _dans(o)),
            lambda o: VP(V("faire"), N("partie"), _de(o)),
        ]),
        "completionDate": (60, False, [
            lambda o: VP(V("être").t("pc"), V("compléter").t("pp"), _en(o)),
        ]),
        "cost": (40, False, [
            lambda o: VP(V("coûter"), o),
        ]),
        "country": (40, False, "city"),
        "countryOrigin": (10, True, [
            lambda o: VP(V("provenir").t("pc"), _de(o))
        ]),
        "countySeat": (40, False, [
            lambda o: VP(V("être"), NP(D("le"), N("siège"),
                                       PP(P("de"), NP(D("le"),N("comté")), _de(o)))),
        ]),
        "course": (20, False, [
            lambda o: VP(V("être"), NP(D("un"), o)),
        ]),
        "creator": (50, False, [
            lambda o: VP(V("être").t("pc"), V("créer").t("pp"), _par(o)),
        ]),
        "crewMembers": (50, False, [
            lambda o: VP(V("avoir"), o, _comme(N("membre").n("p"), PP(P("de"), N("équipage")))),
        ]),
        "currency": (60, False, [
            lambda o: VP(V("avoir"), o, _comme(oneOf(Q(""), A("national")), N("monnaie"))),
        ]),
        "currentclub": (50, True, "club"),
        "dateOfRetirement": (90, True, [
            lambda o: VP(V("prendre").t("pc"), NP(D("mon"),N("retraite")), _en(o)),
            lambda o: VP(V("partir").t("pc"), P("à"),NP(D("le"), N("retraite")), _en(o)),
        ]),
        "dean": (20, False, [
            lambda o: VP(V("être"), V("diriger").t("pp"), _par(o)),
        ]),
        "deathDate": (99, True, [
            lambda o: VP(V("mourir").t("pc"), D("le"),o),
            lambda o: VP(V("décéder").t("pc"), D("le"),o),
        ]),
        "deathPlace": (100, True, [
            lambda o: VP(V("mourir").t("pc"), _a(o)),
            lambda o: VP(V("décéder").t("pc"), _a(o)),
        ]),
        "debutTeam": (30, True, [
            lambda o: VP(Adv("d'abord"), V("jouer").t("pc"), _avec(o)),
        ]),
        "dedicatedTo": (10, False, [
            lambda o: VP(V("être"), V("vouer").t("pp"), _a(o)),
        ]),
        "demonym": (50, False, [
            lambda o: VP(V("être"), V("habiter").t("pp"), _par(o)),
        ]),
        "density": (50, False, [
            lambda o: VP(V("avoir"), NP(D("un"), N("densité"), _de(o)))
        ]),
        "derivative": (50, False, [
            lambda o: VP(V("dériver").t("pc"), _de(o))
        ]),
        "designer": (25, False, [
            lambda o: VP(V("être").t("pc"), V("concevoir").t("pp"), _par(o)),
            lambda o: _par(D("mon").g("n"), N("concepteur"), o),
        ]),
        "diameter": (40, False, [
            lambda o: VP(V("avoir"), NP(D("un"), N("diamètre"), _de(o))),
            lambda o: VP(V("être"), o, _de(N("diamètre"))),
        ]),
        # "discover":(20,False,"discovery"),
        # "discoverer":(20,False,"discovery"),
        "discoverer": (20, False, [
            lambda o: VP(V("être").t("pc"), V("découvrir").t("pp"), _par(o))
        ]),
        "dishVariation": (50, False, [
            lambda o: VP(V("être"), NP(D("un"), N("variation"), _de(o))),
        ]),
        "division": (40, False, [
            lambda o: VP(V("avoir"), NP(D("un"), o, _comme(N("division"))))
        ]),
        "doctoralStudent": (50, True, [
            lambda o: VP(V("superviser").t("pc"), o),
        ]),
        "draftTeam": (20, True, [
            lambda o: VP(V("être").t("pc"), V("sélectionner").t("pp"), _par(o)),
        ]),
        "editor": (42, False, [
            lambda o: VP(V("être").t("pc"), V("éditer").t("pp"), _par(o)),
        ]),
        "elevationAboveTheSeaLevel": (48, False, [
            lambda o: VP(V("être"), A("situé"),
                         _a(NP(NO(o.lemma), N("mètre"),
                            _au_dessus(NP(D("le"),N("niveau"), PP(P("de"), NP(D("le"), N("mer"))))))))
        ]),
        "elevationAboveTheSeaLevelInFeet": (48, False, [
            lambda o: VP(V("être"), A("situé"),
                         _a(NP(NO(o.lemma), N("pied"),
                            _au_dessus(NP(D("le"),N("niveau"), PP(P("de"), NP(D("le"), N("mer"))))))))
        ]),
        "elevationAboveTheSeaLevelInMetres": (48, False, "elevationAboveTheSeaLevel"),
        "engine": (50, False, [
            lambda o: VP(V("avoir"), NP(D("un"), N("moteur"),
                         Q(o.lemma[:-6]) if isinstance(o, Terminal) and o.lemma.endswith("engine") else o))
        ]),
        "epoch": (50, False, [
            lambda o: VP(V("avoir"), NP(D("un"), N("date"), Q("epoch"), _de(o))),
        ]),
        "escapeVelocity": (50, False, [
            lambda o: (VP(V("avoir"), NP(D("un"), N("vitesse"), _de(N("échappement")), _de(o))))
        ]),
        "established": (20, False, [
            lambda o: VP(V("être").t("pc"), V("établir").t("pp"), _dans(o)),
            lambda o: VP(V("être").t("pc"), V("créer").t("pp"), _dans(o)),
        ]),
        "ethnicGroup": (50, False, [
            lambda o: VP(V("avoir"), NP(D("un"), N("groupe"), A("ethnique"), _de(o))),
        ]),
        "family": (50, False, [
            lambda o: VP(V("appartenir"), _a(D("le"), N("famille"), _de(o))),
            lambda o: VP(V("faire"), N("partie"), _de(D("le"), N("famille"), o))
        ]),
        "finalFlight": (75, False, [
            lambda o: VP(V("effectuer").t("pc"), D("mon"), oneOf(A("dernier"), A("final")), N("vol"), _sur(o)),
        ]),
        "floorCount": (50, False, [
            lambda o: VP(V("compter"), NP(NO(o.lemma), N("étage"))),
        ]),
        "followedBy": (50, False, [
            lambda o: VP(V("être"), V("suivre").t("pp"), _par(o)),
        ]),
        "formerName": (2, False, [
            lambda o: VP(V("être").t("ps"), Adv("précédemment"), V("connaître").t("pp"), _comme(o)),
        ]),
        "formerTeam": (2, True, [
            lambda o: VP(V("débuter").t("pc"), _avec(o)),
            lambda o: VP(V("jouer").t("pc"), Adv("précédemment"), _avec(o)),
        ]),
        "founder": (2, False, [
            lambda o: VP(V("être").t("pc"), V(oneOf("créer", "fonder")).t("pp"), _par(o)),
        ]),
        "foundingDate": (2, False, [
            lambda o: VP(V("être").t("pc"), V(oneOf("créer", "fonder")).t("pp"), _en(o)),
        ]),
        "foundationPlace": (3, False, [
            lambda o: VP(V("être").t("pc"), V(oneOf("créer", "fonder")).t("pp"), place(o)),
        ]),
        "fullName": (3, False, [
            lambda o: VP(N("nom"),A("complet"),V("être").t("pr"), o),
        ]),
        "genre": (50, True, [
            lambda o: VP(V(oneOf("jouer", "faire")), _de(D("le"),o)),
        ]),
        "governingBody": (50, False, [
            lambda o: VP(V("être"), V("gouverner").t("pp"), _par(o)),
        ]),
        "ground": (50, True, [
            lambda o: VP(V("jouer"), _dans(o)),
        ]),
        ## "has to its (.*)": voir genSentComp
        "height": (50, True, [
            lambda o: VP(V("avoir"), NP(D("un"), N("hauteur"), _de(o), Q("m"))),
            lambda o: VP(V("mesurer"), o, Q("m"))
        ]),
        "higher": (55, False, [
            lambda o: VP(V("être"), A("grand").f("su"), _de(o)),
        ]),
        "inaugurationDate": (10, False, [
            lambda o: VP(V("être").t("pc"), V("inaugurer").t("pp"), _en(o)),
        ]),
        "industry": (50, False, [
            lambda o: VP(V("être"), _dans(NP(D("le"), o))),
        ]),
        "ingredient": (25, False, [
            lambda o: VP(V("contenir"), o),
            lambda o: VP(V("avoir"), o, P("comme"), N("ingrédient")),
        ]),
        "inOfficeWhileMonarch": (50, True, [
            lambda o: VP(V("servir").t("pc"), _durant(NP(D("le"), N("règne"), _de(o)))),
        ]),
        "inOfficeWhilePresident": (50, True, [
            lambda o: VP(V("servir").t("pc"),
                         SP(P("pendant"),C("que"), o, VP(V("être").t("i"), N("président").cap(True)))),
        ]),
        "inOfficeWhilePrimeMinister": (50, True, [
            lambda o: VP(V("servir").t("pc"),
                         SP(P("pendant"),C("que"), o, VP(V("être").t("i"), A("premier").lier(True), N("ministre")))),
        ]),
        "inOfficeWhileVicePresident": (50, True, [
            lambda o: VP(V("servir").t("pc"),
                         SP(P("pendant"),C("que"), o, VP(V("être").t("i"), N("vice").lier(True), N("président")))),
        ]),
        "instrument": (50, True, [
            lambda o: (VP(V("être"), NP(D("un"), N("chanteur"))) if o.lemma == "Singing"
                       else VP(V("jouer"), NP(D("le"), o)))
        ]),
        "isPartOf": (50, False, [
            lambda o: VP(V("être"), NP(D("un"), N("partie"), _de(o))),
        ]),
        "isPartOfMilitaryConflict": (50, False, [
            lambda o: VP(V("être"), _durant(NP(D("le"), N("conflit"),_de(o)))),
        ]),
        "isbnNumber": (50, False, [
            lambda o: number("ISBN", o),
        ]),
        "issnNumber": (50, False, [
            lambda o: number("ISSN", o),
        ]),
        "keyPerson": (40, True, "leader"),
        "language": (50, True, [
            lambda o: VP(V("parler"), o),
        ]),
        "largestCity": (32, False, [
            lambda o: VP(V("avoir"), o, Adv("comme"), NP(D("mon").g("n"), A("grand").f("su"), N("ville"))),
        ]),
        "launchSite": (30, False, [
            lambda o: VP(V("être").t("pc"), V("lancer").t("pp"), _de(o)),
        ]),
        "leader": (40, False, [
            lambda o: VP(V("être"), V(oneOf("mener","diriger")).t("pp"), _par(o)),
            lambda o: VP(V("avoir"), o, _comme(N(oneOf("chef","dirigeant")))),
        ]),
        "leaderParty": (42, False, [
            lambda o: VP(V("mener").t("pr"), NP(D("le"),N("parti"), o)),
        ]),
        "leaderTitle": (41, False, [
            lambda o: VP(V("être"), V("mener").t("pp"), _par(o)),
            lambda o: VP(V("être"), V("gouverner").t("pp"), _par(o)),
        ]),
        "league": (50, True, [
            lambda o: VP(V(oneOf("être", "jouer", "compétitionner")), _dans(NP(D("le"), N("ligue"), o))),
        ]),
        "length": (30, False, [
            lambda o: VP(V("avoir"), NP(D("un"), N("longueur"), _de(o))),
            lambda o: VP(V("mesurer"), o),
        ]),
        "LCCN_number": (50, False, [
            lambda o: number("LCCN", o),
        ]),
        "location": (30, False, [
            lambda o: VP(V("être"), V("situer").t("pp"), place(o)),
            lambda o: VP(Pro("me*refl"),V("situer").t("p"), place(o)),
        ]),
        "locationIdentifier": (50, False, [
            lambda o: VP(V("avoir"), NP(D("le"), N("identificateur"), PP(P("de"),N("lieu"),o))),
        ]),
        # "locationCity":(30,False,"location"),
        "maidenFlight": (25, False, [
            lambda o: VP(V("réussir").t("pc"), D("mon"), A(oneOf("premier", "inaugural")), N("vol"), _sur(o)),
        ]),
        "mainIngredient": (45, False, [
            lambda o: VP(V("contenir"), Adv("surtout"), o),
        ]),
        "manager": (20, False, [
            lambda o: VP(V("être"), V("gérer").t("pp"), _par(o)),
            lambda o: VP(V("avoir"), o, Adv("comme"), N("gérant")),
        ]),
        "manufacturer": (40, False, [
            lambda o: VP(V("être"), V("manufacturer").t("pp"), _par(o)),
        ]),
        "mass": (50, False, [
            lambda o: VP(V("avoir"), NP(D("un"), N("masse"), _de(o))),
            lambda o: VP(V("peser"), o)
        ]),
        "material": (50, False, [
            lambda o: VP(V("être"), V("faire").t("pp"), _de(o)),
            lambda o: VP(V("être"), V("construire").t("pp"), _hors_de(P("de"), o)),
        ]),
        "mediaType": (40, False, [
            lambda o: VP(V("être"), A("disponible"), _en(o)),
            lambda o: VP(V("paraître").t("pc"), _en(o)),
        ]),
        "militaryBranch": (30, True, [
            lambda o: VP(V("servir").t("pc"), _dans(o)),
            lambda o: VP(V("être").t("pc"), NP(D("un"), N("membre"), _de(o))),
        ]),
        "mission": (22, True, [
            lambda o: VP(V("être").t("pc"), D("un"), N("membre"),
                         _de(NP(D("le"),N("équipe"), P("de"), o))),
            lambda o: VP(V("devenir").t("pc"), N("membre"), _de(o)),
        ]),
        "municipality": (30, False, "city"),
        "musicFusionGenre": (50, False, [
            lambda o: VP(V("être"), NP(D("un"), N("fusion"), A("musical"), _de(o))),
        ]),
        "nationality": (1, True, [
            lambda o : habite(o)
        ]),
        "netIncome": (21, False, [
            lambda o: VP(V("gagner").t("pc"), NP(NO(o.lemma), N("dollar"))),
            lambda o: VP(V("avoir").t("pc"), NP(D("un"), N("revenu"), _de(NP(NO(o.lemma), N("dollar"))))),
        ]),
        "nickname": (30, True, [
            lambda o: VP(V("avoir"), NP(D("le"), N("surnom"), o)),
            lambda o: VP(V("être"), Adv("aussi"), V("surnommer").t("pp"), o),
        ]),
        # "numberOf(.*)": voir genSentComp
        "occupation": (50, True, [
            lambda o: VP(V("être").t("pc"), NP(D("un"), o)),
            lambda o: VP(V("servir").t("pc"), _comme(D("un"), o)),
            lambda o: VP(V("continuer").t("pc"),  P("à"), V("travailler").t("b"), P("comme"), NP(D("un"), o)),
        ]),
        "oclcNumber": (50, False, [
            lambda o: number("OCLC", o),
        ]),
        "office": (30, True, [
            lambda o: VP(V("travailler").t("pc"), _a(o))
        ]),
        "officialLanguage": (40, False, [
            lambda o: VP(V("avoir"), o, _comme(NP( N("langue"),A("officiel")))),
        ]),
        "operatingOrganisation": (50, False, "operator"),
        "operator": (51, True, [
            lambda o: VP(V("être"), V("opérer").t("pp"), _par(o)),
        ]),
        "orbitalPeriod": (30, False, [
            lambda o: VP(V("avoir"), NP(D("un"), N("période"), A("orbital"), _de(o)))
        ]),
        "order": (30, False, [
            lambda o: VP(V("être"), NP(oneOf(N("partie"), Q("")), _de(NP(D("le"), N("ordre"), _de(o))))),
        ]),
        "origin": (2, True, [
            lambda o: VP(V("venir"), _de(o))
        ]),
        "owner": (30, False, [
            lambda o: VP(V("être"), V("détenir").t("pp"), _par(o))
        ]),
        "parentCompany": (30, False, "owner"),
        "party": (40, True, [
            lambda o: VP(V("être"), NP(D("un"), N("membre"), _de(o))),
            lambda o: VP(V("appartenir"), _a(NP(D("le"), N("parti"), o))),
        ]),
        "periapsis": (30, False, [
            lambda o: VP(V("avoir"), NP(D("un"), Q("périastre"), _de(o)))
        ]),
        "populationDensity": (40, False, [
            lambda o: VP(V("avoir"), NP(D("un"), N("densité"),PP(P("de"), N("population"), _de(o)))),
        ]),
        "powerType": (50, False, [
            lambda o: VP(V("être"), V("actionner").t("pp"), _par(NP(D("un"), N("moteur"), o)))
        ]),
        "precededBy": (50, False, [
            lambda o: VP(V("être"), V("précéder").t("pp"), _par(o)),
        ]),
        "president": (20, True, [
            lambda o: VP(V("être"), V("présider").t("pp"), _par(o)),
            lambda o: VP(V("avoir"), o, Adv("comme"), N("président")),
        ]),
        "product": (50, False, [
            lambda o: VP(V("offrir"), NP(D("un"),N("produit")).n("p"),  Adv("comme"), o),
            lambda o: VP(V("être"), NP(D("un"), N("manufacturier"), _de(o))),
            lambda o: VP(V("produire"), o),
        ]),
        "productionStartYear": (30, False, [
            lambda o: VP(V("débuter").t("pc"),NP(D("mon"),N("production"), _en(o))),
        ]),
        "position": (40, False, [
            lambda o: VP(V(oneOf("jouer", "compétitionner")), _comme(o)),
        ]),
        "publisher": (45, False, [
            lambda o: VP(V("être"), V("publier").t("pp"), _par(o))
        ]),
        "recordLabel": (45, True, [
            lambda o: VP(V("enregistrer"), _pour(o)),
            lambda o: VP(V("être").t("pc"), V("engager").t("pp"), _par(o))
        ]),
        "region": (35, True, "city"),
        "regionServed": (50, True, [
            lambda o: VP(V("offrir"), NP(D("mon"), N("service").n("p"), _dans(o))),
        ]),
        "relatedMeanOfTransportation": (50, False, [
            lambda o: VP(V("être"), NP(D("un"), N("moyen"), A("alternatif"),
                                       _de(N("transport"), _pour(o)))),
        ]),
        "representative": (50, False, [
            lambda o: VP(V("être"), V("représenter").t("pp"), _par(o)),
        ]),
        "residence": (50, True, [
            lambda o: VP(V(oneOf("vivre", "résider")), place(o)),
        ]),
        "river": (50, False, [
            lambda o: VP(V("avoir"), NP(D("le"), N("rivière"), o)),
        ]),
        "rotationPeriod": (50, True, [
            lambda o: VP(V("avoir"), NP(D("un"), N("période"), _de(N("rotation"), P("de"), o)))
        ]),
        "runwayLength": (50, False, [
            lambda o: VP(V("avoir"), NP(D("un"), NP(N("piste"), PP(P("de"), N("atterrissage"),
                                                                   _de(NP(NO(o.lemma), N("mètre"))))))),
        ]),
        "runwayName": (49, False, [
            lambda o: VP(V("avoir"), NP(D("un"),N("piste"),PP(P("de"),N("atterrissage")), V("nommer").t("pp"), o)),
        ]),
        "season": (50, True, [
            lambda o: VP(V("jouer").t("pc"), _dans(NP(D("le"), o, N("saison")))),
        ]),
        "selectedByNasa": (21, True, [
            lambda o: VP(V("être").t("pc"), V(oneOf("choisir", "engager", "sélectionner")).t("pp"),
                         _par(Q("NASA"), _en(o))),
            lambda o: VP(V("joindre").t("pc"), Q("NASA"), _en(o)),
        ]),
        "senators": (50, False, [
            lambda o: _avec(o, P("comme"), N("sénateur")),
            lambda o: SP(Pro("qui"), VP(V("avoir"), o, P("comme"), N("sénateur"))),
        ]),
        "series": (50, False, [
            lambda o: VP(V("être"), NP(D("un"), N("personnage"), _de(o)))
        ]),
        "service": (50, False, [
            lambda o: VP(V("opérer"), _dans(NP(D("le"), N("région"), _de(o)))),
            lambda o: VP(V("être"), A("actif"), _dans(NP(D("le"), N("région"), _de(o)))),
        ]),
        "servingTemperature": (50, False, [
            lambda o: VP(V("devoir").t("p"), V("être").t("b"), V("servir").t("pp"), _a(o))
        ]),
        "shipBeam": (50, False, [
            lambda o: VP(V("avoir"), NP(D("un"), N("poutre"), _de(N("navire"), P("de"), o))),
        ]),
        "shipDisplacement": (50, False, [
            lambda o: VP(V("avoir"), NP(D("un"), N("tirant"), _de(N("eau"), P("de"), o))),
        ]),
        "spokenIn": (50, False, [
            lambda o: VP(V("être"), V("parler").t("pp"), place(o)),
        ]),
        "spouse": (30, True, [
            lambda o: VP(V("être"), V("marier").t("pp"), _a(o)),
            lambda o: VP(V("avoir"),o,_comme(N("conjoint")))
        ]),
        "starring": (35, False, [
            lambda o: VP(V("mettre").t("pr"), o, PP(P("en"),N("vedette"))),
        ]),
        "state": (31, False, "city"),
        "status": (95, True, [
            lambda o: VP(V("être"), Adv("maintenant"),
                         V("décéder").t("pp") if o.lemma == 'deceased'
                         else PP(P("à"),NP(D("le"),N("retraite"))) if o.lemma == "retired"
                         else o),
        ]),
        "stylisticOrigin": (50, False, [
            lambda o: VP(V("provenir"), _de(o)),
            lambda o: VP(V("être"), V("dériver").t("pp"), _de(o)),
        ]),
        "successor": (60, True, [
            lambda o: VP(V("être").t("pc"), V("succéder").t("pp"), _par(o)),
        ]),
        "tenant": (50, False, [
            lambda o: VP(V("être"), NP(D("le"), N("locataire"), _de(o))),
        ]),
        "temperature": (50, False, [
            lambda o: VP(V("avoir"), NP(D("un"), N("température"), _de(o)))
        ]),
        "timeInSpace": (24, True, [
            lambda o: VP(V("passer").t("pc"), o, _dans(D("le"), N("espace"))),
        ]),
        "title": (95, True, "status"),
        "topSpeed": (50, False, [
            lambda o: VP(V("avoir"), NP(D("un"), N("vitesse"), P("de"), N("pointe"), _de(o)))
        ]),
        "transmission": (50, False, [
            lambda o: VP(V("avoir"), NP(D("un"), N("transmission"), o)),
        ]),
        "type": (10, False, [
            lambda o: VP(V("être"), NP(D("un"), o)),
            lambda o: VP(V("être"), NP(D("un"), N("sorte"), P("de"), o)),
        ]),
        "unit": (30, True, [
            lambda o: VP(V("servir").t("pc"), _dans(o))
        ]),
        "utcOffset": (20, False, [
            lambda o: VP(V("avoir"), NP(D("un"), Q("UTC offset"), _de(o))),
        ]),
        "wasGivenTheTechnicalCampusStatusBy": (25, False, [
            lambda o: VP(V("être").t("ps"), V("accorder").t("pp"),
                         NP(D("le"), N("statut"),
                            PP(P("de"),NP(D("le"),N("campus"), A("technique"))), _par(o))),
        ]),
        "weight": (50, True, [
            lambda o: VP(V("avoir"), NP(D("un"), N("poids"), _de(o))),
            lambda o: VP(V("peser"), o)
        ]),
        "wheelBase": (50, False, [
            lambda o: VP(V("avoir"), NP(D("un"), N("empattement"), _de(o)))
        ]),
        "writer": (40, True, "author"),
        "youthclub": (30, True, [
            lambda o: VP(V("appartenir"), _a(NP(D("le"), N("club"), N("jeunesse"), o)))
        ]),
    }

    def rel_pro(self,_isHuman):
        return Pro("qui")

    def direction(self,dir):
        return (50, False, [lambda o: VP(V("avoir"), o, _a(D("le").g("f"), Q(dir)))])

    def number_of(self,entities):
        return (50, False, [lambda o: VP(V("avoir"), NP(NO(o.lemma), entities))])

    def runway(self,no, type):
        precedence = 30 + int(no[0])
        ranks = ["0th","1st","2nd","3rd","4th","5th"]
        rank = ranks.index(no) if no in ranks else no
        runway_no = NP(N("numéro"),Q(rank))
        if type == "Number":
            return (precedence, False, [lambda o: VP(V("avoir"), o, _comme(NP(N("piste"),runway_no)))])
        if type.startswith("Length"):
            unit = type[6:]
            return (precedence, False,
                    [lambda o: VP(V("avoir"), NP(D("mon"), N("piste"), runway_no,
                                                _de(NO(o.lemma), N("mètre" if unit == "Metre" else "pied"))))])
        if type == "SurfaceType":
            return (precedence, False,
                    [lambda o: VP(V("avoir"), NP(D("mon"), N("piste"), runway_no), _en(o))])
        print("@@@ strange runway:%s,%s" % (no, type))
        return None

