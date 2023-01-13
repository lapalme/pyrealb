# Sentence realization using pyrealb from ATIS data
# this code uses a similar organization as the one in show_example.py
# in which the functions starting with "realize..." are named "show..."
import re
from typing import Callable, Optional
from pyrealb import *
from Entities import flight_fields, Entities

loadEn()


def get_terminal(val: str, entity: str) -> Terminal:
    if entity.endswith("_code"):  # upper case for codes
        val = val.upper()
    elif entity.endswith("_name"):  # title case for names
        val = val.title()
    lemma = getLemma(val)  # check if the value exists in the dictionary
    if lemma is not None:
        if "N" in lemma: return N(val)
        if "A" in lemma: return A(val)
        if "Adv" in lemma: return Adv(val)
    return Q(val)  # if not found, return a Quoted string


def realize(phrase: Phrase, entities: Entities, fields: list[str], role: Optional[str] = None) -> Constituent:
    res = []
    for f in fields:
        val = entities.grab_value(f, role)
        if len(val) > 0:
            res.append(get_terminal(val, f))
    return phrase(*res) if len(res) > 0 else None


def realize_loc(phrase: Phrase, entities: Entities, role: Optional[str]) -> Constituent:
    return realize(phrase, entities,
                   ["city_name", "state_name", "state_code", "country_name",
                    "airport_name", "airport_code"], role)


def realize_date(entities: Entities, role: Optional[str]) -> Constituent:
    return realize(SP, entities,
                   ["date_relative", "today_relative", "day_name", "month_name",
                    "day_number", "year"], role)


def realize_time(entities: Entities, role: Optional[str]) -> [Constituent]:
    res = []
    if entities.has_entity("start_time", role) and entities.has_entity("end_time", role):
        res.append(PP(P("between"),
                      CP(C("and"),
                         entities.grab_value("start_time", role),
                         entities.grab_value("end_time", role))))
    res.append(realize(SP, entities, ["start_time", "time_relative", "time",
                                      "period_of_day", "period_mod", "end_time"], role))
    return res


def pp(prep: str) -> Callable[[Constituent], Phrase]:
    return lambda *x: PP(P(prep), list(x))


def realize_common(entities: Entities) -> [Constituent]:
    def date_time(kind, vp):
        if entities.has_role(kind + "_date") or entities.has_role(kind + "_time"):
            return vp([realize_date(entities, kind + "_date"),
                       realize_time(entities, kind + "_time")])

    return [
        realize_loc(pp("from"), entities, "fromloc"),
        realize_loc(pp("to"), entities, "toloc"),
        realize_loc(lambda *x: VP(V("stop").t("pr"), P("in"), list(x)), entities, "stoploc"),
        date_time("depart", lambda x: VP(V("depart").t("pr"), P("on"), x)),
        date_time("arrive", lambda x: VP(V("arrive").t("pr"), P("at"), x)),
        date_time("return", lambda x: VP(V("return"), x)),
        realize(pp("on"), entities, ["airline_name", "airline_code",
                                     "airport_name", "airport_code",
                                     "aircraft_code",
                                     "flight_number", "flight_code"]),
        realize(lambda *x: VP(V("serve").t("pr"), list(x)), entities,
                ["city_name", "meal", "meal_description", "meal_code"]),
        realize(pp("with"), entities, ["fare_basis_code"]),
        realize(pp("at"), entities, ["airport_name"])
    ]


def realize_intent(intent: str, entities: Entities) -> Phrase:
    def flight() -> Phrase:
        entities.grab_value("flight")  # ignore this redundant field for a flight intent...
        return oneOf(
            lambda: S(oneOf(None, Q("please")),
                      VP(V(oneOf("show", "list", "give", "find", "display")).t("ip"),
                         NP(D("a"), realize(AP, entities, flight_fields)), N("flight")).n(oneOf("s", "p")),
                      realize_common(entities)),
            lambda: S(Pro("I").pe(1),
                      VP(V(oneOf("want", "need")), V(oneOf("go", "travel")).t("b-to"),
                         realize(AP, entities, flight_fields),
                         realize_common(entities)))
        )

    def airfare() -> Phrase:
        cost_attributes = realize(AP, entities, flight_fields)
        flight_infos = realize_common(entities)
        return oneOf(
            lambda: S(Pro("what"),
                      VP(V("be"),
                         NP(D("the"),
                            cost_attributes,
                            N(oneOf("cost", "fare", "price")),
                            V(oneOf("go", "fly")).t("b-to"),
                            flight_infos))).a("?"),
            lambda: S(Pro("I").pe(3),
                      VP(V("cost"),
                         V(oneOf("go", "fly")).t("b-to"),
                         cost_attributes, flight_infos)).typ({"int": "muc"}),
            lambda: S(Q("please"),
                      VP(V(oneOf("show", "list", "give", "find", "display")).t("ip"),
                         NP(D("the"),
                            cost_attributes,
                            N(oneOf("cost", "fare", "price")),
                            V(oneOf("go", "fly")).t("b-to"),
                            flight_infos)))
        )

    def ground_service() -> Phrase:
        ground_infos = realize(NP, entities, ["transport_type"]) if entities.has_entity("transport_type") \
            else NP(D("the"), N("ground"), N("service"))
        location_infos = realize_loc(pp("in"), entities, None)
        time_infos = [realize_date(entities, None), realize_time(entities, None)]
        return oneOf(
            S(Pro("I").pe(2),
              oneOf(VP(oneOf([V("find"), P("out"), N("information"), P("about")],
                             [V("tell"), Pro("me").pe(1).c("acc"), P("about")],
                             [V("help"), Pro("me").pe(1).c("acc"), P("with")]),
                       ground_infos, location_infos, time_infos,
                       realize(AP, entities, flight_fields),
                       realize_common(entities)))).typ({"mod": "poss", "int": "yon"})
        )

    def airline() -> Phrase:
        if len(entities) == 1:
            if entities.has_entity("airline_code"):
                return S(oneOf([D("what"), N("airline"), V("be")],
                               [D("what"), V("be"), N("airline")]),
                         get_terminal(entities.grab_value("airline_code"), "_code")).a("?")
            elif entities.has_entity("city_name"):
                return S(D("which"), N("airline"), V("be"),
                         get_terminal(entities.grab_value("city_name"), "_name"))
        return S(V("show").t("ip"), oneOf(None, Pro("me").pe(1).c("dat")),
                 NP(D("a"), N("airline").n(oneOf("s", "p")),
                    SP(Pro("that"),
                       VP(V(oneOf("fly", "go"))),
                       realize(AP, entities, flight_fields),
                       realize_common(entities))))

    def abbreviation() -> Phrase:
        if len(entities) == 0:
            return S(VP(V("explain"),
                        NP(D("the"), N("fare"), N("code").n("p"))))
        elif len(entities) == 1:
            first_entity = entities[0].get_entity()
            value = get_terminal(entities.grab_value(first_entity), first_entity)
            code = Q(first_entity.replace("_", " ")) if first_entity.endswith("code") else N("code")
            return oneOf(
                lambda: S(VP(V("explain").t("ip"),
                             NP(D("the"), N("meaning"), PP(P("of"), value, code)))),
                lambda: S(NP(D("the"), value, code),
                          VP(V("mean"))).typ({"int": "wad"})
            )
        else:
            return S(VP(V("explain"),
                        NP(D("the"), N("abbreviation"), Q(entities.grab_values().replace(",", "")))))

    def aircraft() -> Phrase:
        flight_infos = [
            NP(D("a"), realize(AP, entities, flight_fields), N("flight")).n(oneOf("s", "p")),
            realize_common(entities)
        ]
        return S(NP(D("what"),
                    NP(oneOf(
                        [N(oneOf("type", "kind")), PP(P("of"), N(oneOf("aircraft", "plane")))],
                        N(oneOf("aircraft", "plane")))).n(oneOf("s", "p"))),
                 VP(V("be"), V("use").t("pp"),
                    PP(P(oneOf("on", "for")),
                       flight_infos))).a("?")

    def flight_time() -> Phrase:
        val = entities.grab_value("flight_time")
        if len(val) > 0:
            vals = []
            for v in re.split(r"[ _]", val):
                if v.endswith("s"):
                    n = "p"
                    vals.append(get_terminal(v[:-1], "flight_time"))
                else:
                    n = "s"
                    vals.append(get_terminal(v, "flight_time"))
            return S(NP(D("the"), vals).n(n),
                     VP(V("be"),
                        realize(lambda x: PP(P("for"), NP(D("the"), x, N("flight").n(n))),
                                entities, flight_fields),
                        realize_common(entities))).typ({"int": "wad"})
        else:
            return S(NP(D("the"), N("connection"), N("time")),
                     VP(V("be"),
                        realize(pp("in"), entities, flight_fields),
                        realize_common(entities))).typ({"int": "wad"})

    def quantity() -> Phrase:
        return S(Adv("how"), D("many"),
                 NP(realize(AP, entities, flight_fields),
                    N("flight").n("p"),
                    realize(pp("in"), entities, flight_fields),
                    realize_common(entities)),
                 ).a("?")

    def distance() -> Phrase:
        return oneOf(
            lambda: S(Adv("how"), A("far"),
                      VP(V("be"), Pro("I"),
                         realize_common(entities))).a("?"),
            lambda: S(Adv("how"), A("long"),
                      VP(V("do"), Pro("I"), V("take").t("b"),
                         realize_common(entities))).a("?"),
            lambda: S(NP(D("the"), N("distance")),
                      VP(V("be"),
                         realize_common(entities))).typ({"int": "wad"})
        )

    def airport() -> Phrase:
        if len(entities) == 0:
            return S(VP(V("show").t("ip"),
                        N("airport").n("p")))
        else:
            val = entities.grab_value("airport_name")
            if len(val) > 0:
                return S(VP(V(oneOf("show", "describe")).t("ip"),
                            get_terminal(val, "airport_name"),
                            None if val.endswith("airport") else N("airport")))
            else:
                val = get_terminal(entities.grab_value("city_name"), "city_name")
                return S(Pro("what"),
                         VP(V("be"), D("the"),
                            realize(AP, entities, ["mod", "flight_stop"]),
                            N("airport"),
                            PP(P("in"), val,
                               realize(NP, entities, ["state_code", "state_name"])),
                            realize_common(entities))).a("?")

    def city() -> Phrase:
        if entities.has_entity("airline_name"):
            return S(VP(V("show").t("ip"),
                        NP(D("a"), N("city").n("p")),
                        VP(V("serve").t("pp")),
                        PP(P("by"), get_terminal(entities.grab_value("airline_name"), "airline_name")),
                        realize(AP, entities, flight_fields),
                        realize_common(entities)))
        else:
            return S(Pro("where"),
                     VP(V("be"),
                        realize(NP, entities, ["airport_code", "airport_name"]),
                        realize_common(entities))).a("?")

    def ground_fare() -> Phrase:
        val = entities.grab_value("transport_type")
        return S(Adv("how"), Adv("much"),
                 PP(P("for"),
                    NP(D("a"),
                       [N("ground"), N("transportation")] if len(val) == 0 else get_terminal(val, "transport_type"),
                       PP(P("in"), get_terminal(entities.grab_value("city_name"), "city_name"),
                          realize_common(entities)))
                    )).a("?")

    def capacity() -> Phrase:
        val = entities.grab_value("aircraft_code")
        capacity = NP(D("the"),
                      realize(AP, entities, ["mod"]),
                      oneOf(V("seat").t("pr"), None), N("capacity"))
        if len(val) > 0:
            codePP = [PP(P("on"), D("a"), get_terminal(val, "aircraft_code")),
                      realize_common(entities)]
            return oneOf(
                lambda: S(Adv("how"), D("many"),
                          N(oneOf("passenger", "seat", "people")).n("p"),
                          VP(V("fit"), codePP)).a("?"),
                lambda: S(Pro("what"),
                          VP(V("be"), capacity, codePP)).a("?")
            )
        return S(Pro("what"),
                 VP(V("be"), capacity,
                    PP(P("of"), realize_common(entities)))).a("?")

    def flight_no() -> Phrase:
        return S(Pro("what"),
                 VP(V("be"),
                    NP(D("the"), N("flight"), N("number")),
                    realize(lambda *x: PP(P("for"), D("the"), list(x), N("flight")), entities, flight_fields)),
                 realize_common(entities)).a("?")

    def day_name() -> Phrase:
        return S(Pro("what"), NP(N("day"), PP(P("of"), NP(D("the"), N("week")))),
                 VP(V("be").n("p"),
                    N("flight").n("p"),
                    realize_common(entities))).a("?")

    def restriction() -> Phrase:
        return S(Pro("what"),
                 VP(V("be").n("p"),
                    NP(D("the"), realize(AP, entities, ["restriction_code"]),
                       N("restriction").n("p"),
                       PP(P("on"), realize(AP, entities, flight_fields), N("flight").n("p")),
                       realize_common(entities))))

    def meal() -> Phrase:
        meal = entities.grab_value("meal")
        if len(meal) == 0: meal = "meal"
        meal_term = N("meal").n("p" if meal.endswith("s") else "s")
        return oneOf(
            lambda: S(Pro("I").pe(1),
                      VP(V("get"), NP(D("a"), meal_term),
                         realize_common(entities))).typ({"int": "yon"}),
            lambda: S(Pro("there"),
                      VP(V("be"), NP(D("a"), meal_term),
                         realize_common(entities))).typ({"int": "yon"}),
            lambda: S(V("show").t("ip"),
                      Pro("me").pe(1).c("dat"),
                      NP(D("the"), A("available"), meal_term),
                      realize_common(entities))
        )

    def cheapest() -> Phrase:
        return S(Pro("what"),
                 VP(V("be"),
                    NP(D("the"), Q(entities.grab_value("cost_relative")), N("flight")))).a("?")

    intents: dict[str, Callable[[], Phrase]] = {
        "flight": flight, "airfare": airfare, "ground_service": ground_service,
        "airline": airline, "abbreviation": abbreviation, "aircraft": aircraft,
        "flight_time": flight_time, "quantity": quantity, "distance": distance,
        "airport": airport, "city": city, "ground_fare": ground_fare, "capacity": capacity,
        "flight_no": flight_no, "day_name": day_name, "restriction": restriction,
        "meal": meal, "cheapest": cheapest}
    if intent in intents:
        return intents[intent]()
    return S(Q(f'TODO:{intent}'))


def realize_intents(intent: str, entities: Entities) -> Phrase:
    if entities.has_entity("or"):
        return CP(C("or"), [realize_intent(intent, es) for es in entities.split("or")])
    return realize_intent(intent, entities)


def realize_example(intent: str, entities: Entities, showSource: bool = False) -> str:
    intents = intent.split("+")
    res = realize_intents(intents[0], entities)
    if len(intents) > 1:
        res = CP(C("and"), res,
                 realize_intents(intents[1], entities),
                 realize_intents(intents[2], entities) if len(intents) > 2 else None)
    if showSource: print(res.toSource(0))
    return res.realize()
