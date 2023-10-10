from pyrealb import *
from Realizer import Realizer


class Francais(Realizer):
    def __init__(self):
        super().__init__()
        loadFr()
        addToLexicon({"pub":{"N":{"g":"m","tab":"n3"}}});
        addToLexicon({"centre-ville":{"N":{"g":"m","tab":"n3"}}});
        addToLexicon({"adapté":{"A":{"tab":"n28"}}});
        addToLexicon({"classé":{"A":{"tab":"n28"}}});
        self.allPlaces=["endroit","institution","entreprise","établissement","restaurant"];
        self.and_conj = C("et")

    def realize(self, fields, phrase_type):
        loadFr()
        return super().realize(fields, phrase_type)

    def advice(self, fields):
        # "name":[  "Alimentum", ... ],
        name = Q(fields["name"]) if "name" in fields else NP(D("le"), N(oneOf("restaurant", "établissement")))
        # "eatType":[ "coffee shop", "pub", "restaurant" ]
        eatType = NP(D("un"), N(("café" if fields["eatType"]=="coffee shop" else fields["eatType"]))
                              if "eatType" in fields else oneOf(self.allPlaces))
        # "near":[ "Yippee Noodle Bar", ... ],
        near = PP(P("près"), P("de"), Q(fields["near"])) if "near" in fields else None
        # "area":[ "riverside", "city centre" ],
        area = None
        food = None
        priceRange = None
        if "area" in fields:
            area = oneOf(lambda: PP(P("à"),NP(D("le"),N("bord"),P("de"),NP(D("le"),N("rivière")))),
                         lambda: PP(P("dans"),NP(D("le"),N("quartier"),Q("Riverside")))) \
                if fields["area"] == "riverside" \
                else PP(P("à"),NP(D("le"),N("centre-ville")))

        # "food":[ "Chinese", "English", "Fast food", "French", "Indian", "Italian", "Japanese" ],
        foodFr = {"Chinese": "chinois", "English": "anglais",
                  "French": "français", "Indian": "indien",
                  "Italian": "italien", "Japanese": "japonais"}
        if "food" in fields:
            fo = fields["food"]
            if fo == "Fast food":
                food_kind = Q("de la restauration rapide")
            else:
                food_kind = NP(D("un"),N("cuisine"),A(foodFr[fo]))
            serve = V(oneOf("servir","offrir","proposer","présenter"))
            food = oneOf(lambda: SP(Pro("qui"), serve, food_kind),
                         lambda: VP(serve.t("pr"), food_kind))

        # "priceRange":[ "cheap", "high", "less than £20", "moderate", "more than £30", "£20-25" ],
        priceRangeFr=  {"cheap":A("abordable"),
                        "high":A("élevé"),
                        "less than £20":Q("moins de £20"),
                        "moderate":A("modéré"),
                        "more than £30":Q("plus de £30"),
                        "£20-25":Q("£20-25")};
        if "priceRange" in fields:
            pr = fields["priceRange"]
            priceRange = PP(P("avec"),NP(D("un"),N("prix").n("p"),P("de"),priceRangeFr[pr])) \
                if pr.find("£") >= 0 \
                else PP(P("à"),NP(priceRangeFr[pr],N("prix").n("p")))

        return S(name, VP(V("être"), eatType, near, area, food, priceRange))

    def customer_rating(self, fields):
        # "customer rating":[ "5 out of 5", "average", "1 out of 5", "low", "3 out of 5", "high" ]
        customerRatingFr = {"5 out of 5": Q("5 sur 5"), "average": A("moyen"),
                            "1 out of 5": Q("1 sur 5"), "low": A("bas"), "3 out of 5": Q("3 sur 5"),
                            "high": A("élevé")}
        if "rating" in fields:
            cr = customerRatingFr[fields["rating"]]
            return oneOf(lambda: S(Pro("lui").c("nom"),
                                   VP(V("obtenir"),NP(D("un"),N("classement"),cr))),
                         lambda: S(NP(D("le"),N("client").n("p")),
                                   VP(Pro("me*coi"),V("donner"),
                                      NP(D("un"),N("classement"),cr))),
                         lambda: S(Pro("lui").c("nom"),VP(V("être"),A("classé"),cr))
                        )

    def family_friendly(self, fields):
        # "familyFriendly":[ "yes", "no" ],
        if "familyFriendly" in fields:
            return S(oneOf(lambda: Pro("lui").c("nom"),
                           lambda: NP(D("le"), N(oneOf(self.allPlaces))),
                           lambda: NP(D("le"),N(oneOf(self.allPlaces)))
                           ),
                     VP(V("être"),
                        A(oneOf("adapté", "approprié")),
                        PP(P("pour"), NP(D("le"), N("enfant").n("p"))))) \
                .typ({"neg": fields["familyFriendly"] == "no"})
