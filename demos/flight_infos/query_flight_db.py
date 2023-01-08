# Query the flightDB.json which contains the following fileds of information about US flights
#
# Some "simplifications" on query processing are applied:
#  - only direct flights
#  - some relative time information (e.g. next Thursday) are not taken into account
#  - the fares are a simplistic function of the distance and the day of the week
#  - there is no information about ground_service, ground_fare, aircraft, airport,
#           distance from the airport to downtown, quantity, meal, city
#
# The main entry point is
#       "process_intent" which is called with the intent and entities extracted by RASA
# When called as a main,
#       "process_examples_by_intent" is called with the entities from the {training|test}.json files

import json, re, os
from typing import Optional, Union, Callable, Tuple

from pyrealb import *

from Entities import Entities, Entity
import realize_example

from flight_time import day_numbers, days_int, int_days, months, numbers, process_time_period
from Flights import Flights, Flight, group_flights, match_flights, flights, airports, airlines

debug = True  # show extracted entities and information used for querying the database

# type of information extracted from entities
Infos = dict[str, Union[str, int, Tuple[int, int]]]

# current day and town
today = 1  # Monday


# matching information
def airport_code(name: str) -> Optional[str]:
    # find airport code from name
    if name is None or name in airports: return name
    name = name.lower()
    for code in airports:
        if name in airports[code]["city"].lower() or name in airports[code]["name"].lower():
            return code
    return None


here = airport_code("Chicago")


def airline_code(name: str) -> Optional[str]:
    # find airline code from name
    if name is None or name in airlines: return name
    name = name.lower()
    for code in airlines:
        if name in airlines[code].lower():
            return code
    return None


def find_flights(infos: Infos) -> list[Flight]:
    # simple-minded approach to flight matching
    orig = airport_code(infos.get("origin"))
    if orig is None and infos.get("origin") is not None:
        print("@@@ could not find origin:", infos.get("origin"))
    dest = airport_code(infos.get("destination"))
    if dest is None and infos.get("destination") is not None:
        print("@@@ could not find destination:", infos.get("destination"))
    # add default airport when both are not specified (but leave it when both are not specified)
    if orig is None and dest is not None:
        orig = here
    elif orig is not None and dest is None:
        dest = here
    air_code = airline_code(infos.get("airline"))
    if air_code is None and infos.get("airline") is not None:
        print("@@@ could not find airline:", infos.get("airline"))
    return match_flights(flights, orig, dest, air_code,
                         infos["flight_number"] if "flight_number" in infos else None,
                         infos["orig_time_rng"], infos["dest_time_rng"],
                         infos["days"] if "days" in infos else None)


def show_airlines(flights: Flights) -> list[str]:
    res = []
    rlines = group_flights(flights, "AIRLINE")
    for rline in rlines:
        # show total number of flights
        res.append(S(NP(NO(len(rline)), N("flight")),
                     PP(P("by"), Q(airlines[rline[0]["AIRLINE"]]))).realize())
        orig_dests = group_flights(flights, lambda f: f["ORIGIN_AIRPORT"] + "=>" + f["DESTINATION_AIRPORT"])
        for orig_dest in orig_dests:
            # show origin and destination and number of flights
            res.append(S(PP(P("from"), Q(airports[orig_dest[0]["ORIGIN_AIRPORT"]]["city"])),
                         PP(P("to"), Q(airports[orig_dest[0]["DESTINATION_AIRPORT"]]["city"])).a(":"),
                         NP(NO(len(orig_dest)), N("flight"))).realize())
    return res


def answer_nb_flights(entities: Entities, flights: Union[Flights, list[Flight]] = None) -> str:
    nb = 0 if flights is None else len(flights)
    if nb == 0:
        s = oneOf(lambda: S(Pro("there"),
                            VP(V("be").n("p"),
                               NP(D("no"), N("flight").n("p")))),
                  lambda: S(NP(D("no"), N("flight").n("p")),
                            VP(V("be").t("ps"),
                               V("find").t("pp"))))
    else:
        s = S(Pro("there"),
              VP(V("be").n("s" if nb == 1 else "p"),
                 NP(NO(nb), N("flight"))))
        # add default origin and destination if they are not specified
        orig = entities.get_value("city_name", "fromloc")
        dest = entities.get_value("city_name", "toloc")
        if orig == "" and dest != "":
            entities.append(Entity({"entity": "city_name", "value": airports[here]["city"], "role": "fromloc"}))
        elif orig != "" and dest == "":
            entities.append(Entity({"entity": "city_name", "value": airports[here]["city"], "role": "toloc"}))
    return s.add(realize_example.realize_common(entities)).realize()


def extract_flight_infos(entities: Entities) -> Infos:
    infos = {}
    orig_time = {}
    dest_time = {}
    for e in entities:
        value = e.get_value()
        entity = e.get_entity()
        role = e.get_role()
        if entity == "city_name":
            if role == "fromloc":
                infos["origin"] = value
            elif role == "toloc":
                infos["destination"] = value
        elif entity == "airport_code":
            if value in airports:
                if role == "fromloc":
                    infos["origin"] = airports[value]["city"]
                elif role == "toloc":
                    infos["destination"] = airports[value]["city"]
            else:
                print("@@@ unknown airport_code", role, value)
        elif entity == "airline_name":
            infos["airline"] = value
        elif entity == "flight_number":
            infos["flight_number"] = value
        elif entity == "time_relative":
            if role == "depart_time":
                infos["depart_time.time_relative"] = value
            elif role == "arrive_time":
                infos["arrive_time.time_relative"] = value
            else:
                infos["time_relative"] = value
        elif entity == "date_relative":
            infos["date_relative"] = value  # current ignored in further processing
        elif role == "depart_time":
            orig_time[entity] = value
        elif role == "arrive_time":
            dest_time[entity] = value
        elif role == "depart_date":
            if entity == "day_name":
                value = value.lower()
                if value.endswith(" 's"):
                    value = value[:-3]  # e.g. sunday 's =>sunday
                elif value.endswith("s"):
                    value = value[:-1]  # e.g. mondays => monday
                if value in days_int:
                    infos["days"] = days_int[value]
                elif value == "weekday":
                    infos["days"] = {1, 2, 3, 4, 5}
                else:
                    print("@@@ unknown day_name:", value)
            elif entity == "month_name":
                value = value.lower()
                if value in months:
                    infos["month"] = months.index(value)
                else:
                    print("@@@ unknown month", value)
            elif entity == "day_number":
                value = value.lower()
                if value in day_numbers:
                    infos["date"] = day_numbers.index(value)
                elif value in numbers:
                    infos["date"] = numbers.index(value)
                else:
                    print("@@@ unknown day_number", value)
            elif entity == "today_relative":
                if value in ["today", "this", "tonight"]:
                    infos["days"] = today
                elif value == "tomorrow":
                    infos["days"] = today % 7 + 1
                elif value == "the day after tomorrow":
                    infos["days"] = today % 7 + 2  # TODO: check this more carefully
                else:
                    print("@@@ unknown today_relative", value)
            elif entity == "year":
                infos["year"] = value
            else:
                print("@@@ unknown entity for depart_date", entity, value)
    infos["orig_time_rng"] = process_time_period(orig_time,
                                                 infos.get("depart_time.time_relative",
                                                           infos.get("time_relative")))
    infos["dest_time_rng"] = process_time_period(dest_time,
                                                 infos.get("arrive_time.time_relative",
                                                           infos.get("time_relative")))
    if debug: print("Infos:", infos)
    return infos


########
#   intent processing

def process_flight(entities: Entities) -> list[str]:
    if entities.has_entity("cost_relative"):  # fix bad intent....
        return process_airfare(entities)
    # query the database
    infos = extract_flight_infos(entities)
    flights = find_flights(infos)
    if "origin" not in infos and "destination" not in infos:
        return show_airlines(flights)
    else:
        # realize the number of flights followed by the table of flights
        return [
            answer_nb_flights(entities, flights),
            *[f.show() for f in flights]
        ]


def process_airfare(entities: Entities) -> list[str]:
    #  extract specific about fares
    cost_relative = None
    if entities.has_entity("cost_relative"):
        cost_relative = entities.get_value("cost_relative")
    # query the database
    flights = find_flights(extract_flight_infos(entities))
    if len(flights) == 0:
        return [answer_nb_flights(entities, None)]
    else:
        # find costs of flights
        if cost_relative is None:
            return [f.show({"airline", "city", "week_day", "day", "cost"}) for f in flights]
        else:
            if cost_relative in ["cheapest", "lowest", "lowest price", "lowest cost", "least expensive"]:
                return [min(flights, key=Flight.cost).show({"airline", "city", "week_day", "day", "cost"})]
            elif cost_relative in ["highest", "most expensive"]:
                return [max(flights, key=Flight.cost).show({"airline", "city", "week_day", "day", "cost"})]
            elif cost_relative in ["under", "less"] and entities.has_entity("fare_amount"):
                amount = entities.get_value("fare_amount")
                m = re.match(r"(\d+)(\s+dollar)?", amount)
                if m is None:
                    return ["@@@ strange amount", amount]
                else:
                    amount = int(m[1])
                    fl = [f for f in flights if f.cost() <= amount]
                    return ["Under %d: " % amount + answer_nb_flights(entities, fl),
                            *[f.show({"airline", "city", "week_day", "day", "cost"}) for f in fl]]
            else:
                return ["@@@ unprocessed cost_relative", cost_relative]


def process_airline(entities: Entities) -> list[str]:
    if entities.has_entity("airline_code"):
        value = entities.get_value("airline_code")
        code = value.upper()
        return [S(Q(airlines[code]) if code in airlines else NP(D("no"), N("airline").n("p")),
                  VP(V("have"),
                     NP(D("the"), N("code"), Q(value)))).realize()]
    flights = find_flights(extract_flight_infos(entities))
    if len(flights) == 0:
        return [answer_nb_flights(entities, [])]
    else:
        als = {airlines[f["AIRLINE"]] for f in flights}
        return [CP(C("and"), list(map(Q, als))).realize()]


def process_abbreviation(entities: Entities) -> list[str]:
    if entities.has_entity("airline_code"):
        value = entities.get_value("airline_code")
        code = value.upper()
        return [S(Q(airlines[code]) if code in airlines else NP(D("no"), N("airline").n("p")),
                  VP(V("have"),
                     NP(D("the"), N("airline"), N("code"), Q(value)))).realize()]
    elif entities.has_entity("airport_code"):
        value = entities.get_value("airport_code")
        code = value.upper()
        return [S(Q(airports[code]["name"]) if code in airports else NP(D("no"), N("airport").n("p")),
                  VP(V("have"),
                     NP(D("the"), N("airport"), N("code"), Q(value)))).realize()]
    elif len(entities) > 0:
        value = entities[0].get_value()
        codes = list(map(Q, value.split("_")[:-1]))
        return [S(NP(D("no"), N("definition")),
                  PP(P("for"), codes, Q(value))).realize()]
    else:
        return ["no abbreviation found"]


def process_day_name(entities: Entities) -> list[str]:
    flights = find_flights(extract_flight_infos(entities))
    days = sorted({f["DAY_OF_WEEK"] for f in flights})
    return [CP(C("and"), list(map(lambda d: N(int_days[d]), days))).realize()]


def process_simple_response(intent: str) -> str:
    if intent == "greet":
        return f"{int_days[today]} in {airports[here]['city']}: " + \
               oneOf(lambda: S(Pro("I").pe(2),
                               VP(V("want"), V("know").t("b-to"),
                                  NP(D("the"), N("thing")),
                                  PP(P("about"), N("flight").n("p")))).typ({"int": "wad"}).b("hello, ").realize(),
                     lambda: S(Q("hi").a(","),
                               D("any"), N("flight"), N("information")).a("?").realize())
    if intent == "goodbye":
        return S(Q("bye").a(","),
                 Pro("I").pe(1),
                 VP(V("hope"),
                    SP(NP(D("this"), N("information")),
                       VP(V("be").t("ps"),
                          A("useful"))))).realize()
    if intent == "bot_challenge":
        return S(Pro("I").pe(1),
                 VP(V('be'),
                    NP(D("a"), Q("bot"),
                       CP(C("and"),
                          VP(V("power"), PP(P("by"), Q("RASA"))),
                          VP(V("realize"), PP(P("with"), Q("pyrealb")))).t("pp")))).realize()
    return "@@@ intent not yet implemented:" + intent


# this is the entry point for RASA
def process_intent(intent: str, entity_list: list[Entity]) -> str:
    entities = Entities(entity_list)
    if intent in ["greet", "goodbye", "bot_challenge"]:
        return process_simple_response(intent)
    if intent in ["flight", "flight_no", "flight_time"]:
        return "\n".join(process_flight(entities))
    if intent in ["airfare", "flight+airfare"]:
        return "\n".join(process_airfare(entities))
    if intent == "airline":
        return "\n".join(process_airline(entities))
    if intent == "abbreviation":
        return "\n".join(process_abbreviation(entities))
    if intent == "day_name":
        return "\n".join(process_day_name(entities))
    if intent in ["ground_service", "capacity", "distance", "aircraft",
                  "ground_fare", "meal", "quantity", "city", "airport"]:
        return "%s information not in database" % intent
    else:
        return "@@@ intent not yet implemented:" + intent


def process_examples_by_intent(examples: dict[str, list[tuple[str, Entities]]]) -> None:
    value_ent_role_re = re.compile(
        r'\[(?P<val>.*?)](\((?P<ent0>.*?)\)|{"entity":"(?P<ent>.*?)","role":"(?P<role>.*?)"})')

    def do_all_exs(intent: str, fn: Callable[[Entities], list[str]], exs: list[tuple[str, Entities]]):
        for txt, entities in exs:
            # print the original text by replacing entities by their value
            print("** %s : %s" % (intent, value_ent_role_re.sub(r"\g<val>", txt)))
            if debug: print("Entities:", entities)
            print("\n".join(fn(entities)))
            print("----")

    # process intents in decreasing numer of examples:
    for intent, exs in sorted(examples.items(), key=lambda x: len(x[1]), reverse=True):
        print(NP(NO(len(examples[intent])), N("example"), PP(P("for"), Q(intent))).realize())
        if intent in ["flight", "flight_no", "flight_time"]:
            do_all_exs(intent, process_flight, exs)
        elif intent in ["airfare", "flight+airfare"]:
            do_all_exs(intent, process_airfare, exs)
        elif intent == "airline":
            do_all_exs(intent, process_airline, exs)
        elif intent == "abbreviation":
            do_all_exs(intent, process_abbreviation, exs)
        elif intent == "day_name":
            do_all_exs(intent, process_day_name, exs)
        elif intent in ["ground_service", "capacity", "distance", "aircraft",
                        "ground_fare", "meal", "quantity", "city", "airport"]:
            print("%s information not in database" % intent)
        else:
            print("@@@ intent not yet implemented:", intent)
        print("=" * 25)


if __name__ == '__main__':
    # single example for débugging... just change the following bool
    if False:
        example = json.loads("""
          {
        "text": "round trip fares from los angeles to philadelphia under 3000 dollars",
        "intent": "flight",
        "entities": [
          {
            "start": 0,
            "end": 10,
            "value": "round trip",
            "entity": "round_trip"
          },
          {
            "start": 37,
            "end": 49,
            "value": "philadelphia",
            "entity": "city_name",
            "role": "toloc"
          }
        ]
         }
        """)
        debug = True
        print("Entities:", example["entities"])
        print(process_intent(example["intent"], example["entities"]))
    else:
        examples: dict[str, list[tuple[str, Entities]]] = {}
        pwd = os.path.dirname(__file__)
        file_name = os.path.normpath(os.path.join(pwd, "Examples", "train.json"))
        print("*** Processing", file_name)
        print(f"{int_days[today]} in {here}")
        common_examples = json.load(open(file_name, "r", encoding="utf-8"))["rasa_nlu_data"]["common_examples"]
        for e in common_examples:
            intent = e["intent"]
            if intent not in examples: examples[intent] = []
            examples[e["intent"]].append((e["text"], Entities(e["entities"])))
        process_examples_by_intent(examples)
        print("Simple responses to intents")
        for intent in ["greet", "greet", "goodbye", "bot_challenge"]:
            print(intent, ":", process_simple_response(intent))
        print("=" * 25)
