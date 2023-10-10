from pyrealb import *
from Realizer import Realizer

class English(Realizer):
    def __init__(self):
        super().__init__()
        loadEn()
        addToLexicon({"coffee shop":{"N":{"tab":"n1"}}})
        self.allPlaces=["place","arena","venue","establishment","restaurant"]
        self.and_conj = C("and")

    def realize(self,fields,phrase_type):
        loadEn()
        return super().realize(fields,phrase_type)

    def advice(self,fields):
        # "name":[  "Alimentum", ... ],
        name = Q(fields["name"]) if "name" in fields else NP(D("the"), N(oneOf("restaurant", "establishment")))
        # "eatType":[ "coffee shop", "pub", "restaurant" ]
        eatType = NP(D("a"), N(fields["eatType"] if "eatType" in fields else  oneOf(self.allPlaces)))
        # "near":[ "Yippee Noodle Bar", ... ],
        near = PP(P("near"), Q(fields["near"])) if "near" in fields else None
        # "area":[ "riverside", "city centre" ],
        area = None
        food = None
        priceRange = None
        if "area" in fields:
            area = oneOf(lambda: PP(P("on"), NP(D("the"), N("riverside"))),
                         lambda: PP(P("in"), NP(D("the"), N("riverside"), N("area")))) \
                   if fields["area"] == "riverside" \
                   else PP(P("in"), NP(D("the"), N("city"), N("centre")))

        # "food":[ "Chinese", "English", "Fast food", "French", "Indian", "Italian", "Japanese" ],
        if "food" in fields:
            fo = fields["food"]
            if fo == "Fast food": fo = "fast"
            food = Q(fo)
            npFood = NP(food, N("food"))
            serve = V(oneOf("serve", "provide", "have", "offer"))
            food = oneOf(lambda: SP(Pro("that"), serve, npFood),
                         lambda: VP(serve.t("pr"), npFood))

        # "priceRange":[ "cheap", "high", "less than £20", "moderate", "more than £30", "£20-25" ],
        if "priceRange" in fields:
            pr = fields["priceRange"]
            priceRange = PP(P("with"), N("price").n("p"), Q(pr)) \
                         if pr.find("£") >= 0 \
                         else PP(P("with"), NP(A(pr), N("price").n("p")))

        return S(name, VP(V("be"), eatType, near, area, food, priceRange))
    
    def customer_rating(self, fields):
        # "customer rating":[ "5 out of 5", "average", "1 out of 5", "low", "3 out of 5", "high" ]
        if "rating" in fields:
            cr = fields["rating"]
            return S(Pro("I").g("n"),
                     VP(V("have"),
                        oneOf(lambda:NP(D("a"),Q(cr),oneOf(N("customer"),Q("")),N("rating")),
                              lambda:NP(D("a"),oneOf(N("customer"),Q("")),N("rating"),P("of"),Q(cr)))))

    def family_friendly(self, fields):
        # "familyFriendly":[ "yes", "no" ],
        if "familyFriendly" in fields:
            return S(oneOf(lambda:Pro("I").g("n"),
                           lambda:NP(D("the"),N(oneOf(self.allPlaces))),
                           lambda:Pro("I").n("p")
                          ),
                     VP(V("be"),
                        NP(oneOf(N("family").lier(),N("kid")),A("friendly").pos("post"))))\
                           .typ({"neg":fields["familyFriendly"]=="no"})
