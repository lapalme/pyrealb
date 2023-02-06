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
#       "process_intent_conversation" which is called from ngl_server.py with the intent and entities extracted by RASA
# When called as a main,
#       "process_examples_by_intent" is called with the entities from the {training|test}.json files

import json, re
from typing import Optional, Union, Callable, Tuple
from pyrealb import *

from Entities import Entities
from flight_time import day_numbers, days_int, int_days, months, numbers, process_time_period
from Flights import Flights, Flight, show_flights, group_flights, match_flights, flights, airports, airlines

debug = False  # show extracted entities and information used for querying the database

# extracted information (by extract_flight_info and process_time_period in flight_time.py) used for matching flights
# { "origin" : <city name>, "destination": <city name>,
#   "airline": <airline name>, "flight_number": <flight id>,
#   "[{depart|arrive}_time.]time_relative": str, "date_relative": str,
#   "days": int|set(int), "month":str, "date":int, "year": int,
#   "orig_time_rng":int|Tuple[int] "dest_time_rng":int|Tuple[int]
# }
Info = dict[str, Union[str, int, Tuple[int, int]]]

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


def find_flights(info: Info) -> list[Flight]:
    # simple-minded approach to flight matching
    orig = airport_code(info.get("origin"))
    if orig is None and info.get("origin") is not None:
        print("@@@ could not find origin:", info.get("origin"))
    dest = airport_code(info.get("destination"))
    if dest is None and info.get("destination") is not None:
        print("@@@ could not find destination:", info.get("destination"))
    # add default airport when both are not specified (but leave it when both are not specified)
    if orig is None and dest is not None:
        orig = here
    elif orig is not None and dest is None:
        dest = here
    air_code = airline_code(info.get("airline"))
    if air_code is None and info.get("airline") is not None:
        print("@@@ could not find airline:", info.get("airline"))
    return match_flights(flights, orig, dest, air_code,
                         info["flight_number"] if "flight_number" in info else None,
                         info["orig_time_rng"], info["dest_time_rng"],
                         info["days"] if "days" in info else None)


def show_airlines(flights: Flights) -> list[str]:
    res = []
    for (airline, flights) in group_flights(flights, "AIRLINE").items():
        # show total number of flights
        res.append(S(NP(NO(len(flights)), N("flight")),
                     PP(P("by"), Q(airlines[airline]))).realize())
        # orig_dests = group_flights(flights, lambda f: f["ORIGIN_AIRPORT"] + "=>" + f["DESTINATION_AIRPORT"])
        for (orig, o_flights) in sorted(group_flights(flights, "ORIGIN_AIRPORT").items()):
            s = S(PP(NO(len(o_flights)), P("from"), airports[orig]["city"]).a(":")).b("- ")
            cp = CP()
            for (dest, d_flights) in sorted(group_flights(o_flights, "DESTINATION_AIRPORT").items()):
                cp.add(NP(NO(len(d_flights)), N("flight"),
                          PP(P("to"), Q(airports[dest]["city"]))))
            res.append(s.add(cp).realize())
    return res


def answer_nb_flights(info:Info, flights: Flights) -> str:
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
    if "origin" not in info and "destination" in info:
        info["origin"] = airports[here]["city"]
    elif "origin" in info and "destination" not in info:
        info["destination"] = airports[here]["city"]
    # add flight details
    details = []
    if "origin" in info:
        details.append(PP(P("from"),Q(info["origin"].title())))
    if "destination" in info:
        details.append(PP(P("to"),Q(info["destination"].title())))
    if "airline" in info:
        details.append(PP(P("by"),Q(info["airline"])))
    if "days" in info and isinstance(info["days"],int) and (1 <= info["days"] <= 7):
        details.append(PP(P("on"),N(int_days[info["days"]])))
    return s.add(details).realize()


def extract_flight_info(entities: Entities) -> Info:
    info = {}
    orig_time = {}
    dest_time = {}
    for e in entities:
        value = e.get_value()
        entity = e.get_entity()
        role = e.get_role()
        if entity == "city_name":
            if role == "fromloc":
                info["origin"] = value
            elif role == "toloc":
                info["destination"] = value
        elif entity == "airport_code":
            if value in airports:
                if role == "fromloc":
                    info["origin"] = airports[value]["city"]
                elif role == "toloc":
                    info["destination"] = airports[value]["city"]
            else:
                print("@@@ unknown airport_code", role, value)
        elif entity == "airport_name":
            if any(airports[code]["name"].lower() == value.lower() for code in airports):
                if role == "fromloc":
                    info["origin"] = value
                elif role == "toloc":
                    info["destination"] = value
                else:
                    print("@@@ unknown airport_name role", role, value)
            else:
                print("@@@ unknown airport_name", role, value)
        elif entity == "airline_name":
            info["airline"] = value
        elif entity == "flight_number":
            info["flight_number"] = value
        elif entity == "time_relative":
            if role == "depart_time":
                info["depart_time.time_relative"] = value
            elif role == "arrive_time":
                info["arrive_time.time_relative"] = value
            else:
                info["time_relative"] = value
        elif entity == "date_relative":
            info["date_relative"] = value  # currently ignored in further processing
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
                    info["days"] = days_int[value]
                elif value == "weekday":
                    info["days"] = {1, 2, 3, 4, 5}
                else:
                    print("@@@ unknown day_name:", value)
            elif entity == "month_name":
                value = value.lower()
                if value in months:
                    info["month"] = months.index(value)
                else:
                    print("@@@ unknown month", value)
            elif entity == "day_number":
                value = value.lower()
                if value in day_numbers:
                    info["date"] = day_numbers.index(value)
                elif value in numbers:
                    info["date"] = numbers.index(value)
                else:
                    print("@@@ unknown day_number", value)
            elif entity == "today_relative":
                if value in ["today", "this", "tonight"]:
                    info["days"] = today
                elif value == "tomorrow":
                    info["days"] = today % 7 + 1
                elif value == "the day after tomorrow":
                    info["days"] = today % 7 + 2  # TODO: check this more carefully
                else:
                    print("@@@ unknown today_relative", value)
            elif entity == "year":
                info["year"] = value
            else:
                print("@@@ unknown entity for depart_date", entity, value)
    info["orig_time_rng"] = process_time_period(orig_time,
                                                info.get("depart_time.time_relative",
                                                         info.get("time_relative")))
    info["dest_time_rng"] = process_time_period(dest_time,
                                                info.get("arrive_time.time_relative",
                                                         info.get("time_relative")))
    if debug: print("info:", info)
    return info


########
#   intent processing


def process_flight(_entities: Entities, info:Info) -> list[str]:  # version with single turn
    flights = find_flights(info)
    if "origin" not in info and "destination" not in info:
        return show_airlines(flights)
    # realize the number of flights followed by the table of flights
    return [
        answer_nb_flights(info, flights),
        *show_flights(flights,{"airline", "city", "week_day"})
    ]


def process_airfare(entities: Entities, info:Info) -> list[str]:
    #  extract specific about fares
    cost_relative = entities.get_value("cost_relative").lower() if entities.has_entity("cost_relative") else None
    # query the database
    flights = find_flights(info)
    if len(flights) == 0:
        return [answer_nb_flights(info,[])]
    else:
        # find costs of flights
        if cost_relative is None:
            return [f.show({"airline", "city", "week_day", "cost"}) for f in flights]
        else:
            if cost_relative in ["cheapest", "lowest", "lowest price", "lowest cost", "least expensive"]:
                return [
                    S(NP(D("the"), Adv("least"), A("expensive"), N("flight")), VP(V("be"))).a(":").realize(),
                    min(flights, key=lambda f:f["COST"]).show({"airline", "city", "week_day", "cost"}),
                ]
            elif cost_relative in ["highest", "most expensive"]:
                return [
                    S(NP(D("the"), A("expensive").f("su"), N("flight")), VP(V("be"))).a(":").realize(),
                    max(flights, key=lambda f:f["COST"]).show({"airline", "city", "week_day", "cost"})
                ]
            elif cost_relative in ["under", "less"] and entities.has_entity("fare_amount"):
                amount = entities.get_value("fare_amount")
                m = re.match(r"(\d+)(\s+dollar)?", amount)
                if m is None:
                    return ["@@@ strange amount", amount]
                else:
                    amount = int(m[1])
                    fl = [f for f in flights if f["COST"] <= amount]
                    return ["Under %d: " % amount + answer_nb_flights(info, fl),
                            *[f.show({"airline", "city", "week_day", "cost"}) for f in fl]]
            else:
                return ["@@@ unprocessed cost_relative", cost_relative]


def process_airline(entities: Entities, info:Info) -> list[str]:
    if entities.has_entity("airline_code"):
        value = entities.get_value("airline_code")
        code = value.upper()
        return [S(Q(airlines[code]) if code in airlines else NP(D("no"), N("airline").n("p")),
                  VP(V("have"),
                     NP(D("the"), N("code"), Q(value)))).realize()]
    flights = find_flights(info)
    if len(flights) == 0:
        return [answer_nb_flights(info, [])]
    else:
        als = {airlines[f["AIRLINE"]] for f in flights}
        return [CP(C("and"), list(map(Q, als))).realize()]


def process_abbreviation(entities: Entities, _info:Info) -> list[str]:
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


def process_day_name(_entities: Entities, info:Info) -> list[str]:
    flights = find_flights(info)
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


# manage conversation data
conversation_intent:Optional[str] = None
conversation_context:Info = {}


def ask_details(answer_nb:str) -> list[str]:
    details = []
    if "origin" not in conversation_context:
        details.append(NP(N("departure"),N("city")))
    if "destination" not in conversation_context:
        details.append(NP(N("destination")))
    if "days" not in conversation_context:
        details.append(NP(N("weekday"),PP(P("of"),N("departure"))))
    if "airline" not in conversation_context:
        details.append(NP(V("prefer").t("pp"),N("airline")))
    if len(details) == 0:
        return []
    if len(details) == 1:
        return [
            answer_nb,
            S(Pro("I").pe(2), VP(V("specify"), D("my").pe(2),details))
              .typ({"mod": "poss", "int": "yon"}).realize()
        ]
    return [
        answer_nb,
        S(S(Pro("I").pe(2), VP(V("give"), NP(Adv("more"), N("detail").n("p"))))
            .typ({"mod": "poss", "int": "yon"}),
          S(D("such"), Adv("as"),D("my").pe(2),CP(C("or"),details))).realize()
    ]


def definite_response(response) -> str:
    global conversation_context, conversation_intent
    conversation_intent = None
    conversation_context.clear()
    return "\n".join(response)


def process_intent_conversation(intent:str,entities:Entities) -> str:
    if intent in ["greet", "goodbye", "bot_challenge"]:
        return process_simple_response(intent)
    elif intent in ["ground_service", "capacity", "distance", "aircraft",
                    "ground_fare", "meal", "quantity", "city", "airport"]:
        return "%s information not in database" % intent
    global conversation_context,conversation_intent
    info = extract_flight_info(entities)
    if conversation_context:  # continue current conversation
        print("process_flight_multi: entities:", entities)
        print("context", conversation_context, conversation_intent)
        conversation_context.update(info)
        info = conversation_context
        print("updated context", conversation_context)
        intent = conversation_intent
    else:  # start new conversation
        conversation_intent = intent
        conversation_context = info
    if intent in ["flight", "flight_no", "flight_time"]:
        response = process_flight(entities,info)
    elif intent in ["airfare", "flight+airfare"]:
        response = process_airfare(entities,info)
    elif intent == "airline":
        response = process_airline(entities,info)
    elif intent == "abbreviation":
        response = process_abbreviation(entities,info)
    elif intent == "day_name":
        response = process_day_name(entities,info)
    else:
        return "@@@ intent not yet implemented:" + intent
    if len(response) < 5:
        return definite_response(response)
    else:
        details = ask_details(answer_nb_flights(info, find_flights(info)))
        if len(details) == 0:  # no further details needed
            return definite_response(response)
        conversation_intent = intent
        return "\n".join(details)


RASA_limit = 0  # to limit responses to those that are longer than allowed by RASA (900 in nlg_server.py)


def process_examples_by_intent(examples: dict[str, list[tuple[str, Entities]]]) -> None:
    value_ent_role_re = re.compile(
        r'\[(?P<val>.*?)](\((?P<ent0>.*?)\)|{"entity":"(?P<ent>.*?)","role":"(?P<role>.*?)"})')

    def do_all_exs(intent: str, fn: Callable[[Entities,Info], list[str]], exs: list[tuple[str, Entities]]):
        nb = 0
        for txt, entities in exs:
            if debug: print("Entities:", entities)
            info = extract_flight_info(entities)
            response = "\n".join(fn(entities,info))
            if len(response) > RASA_limit:
                # print the original text by replacing entities by their value
                print("** %s : %s" % (intent, value_ent_role_re.sub(r"\g<val>", txt)))
                print(response)
                print("----", len(response))
                nb += 1
        if RASA_limit > 0:
            print(nb, "long responses")

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
    if True:
        example = json.loads("""
        {
        "text": "what is the minimum connection time for san francisco international airport",
        "intent": "flight_time",
        "entities": [
          {
            "start": 40,
            "end": 75,
            "value": "san francisco international airport",
            "entity": "airport_name",
            "role": "fromloc"
          }
        ]
         }
        """)
        debug = True
        print("Entities:", example["entities"])
        print(process_intent_conversation(example["intent"], Entities(example["entities"])))
    else:
        import os
        examples: dict[str, list[tuple[str, Entities]]] = {}
        pwd = os.path.dirname(__file__)
        file_name = os.path.normpath(os.path.join(pwd, "Examples", "test.json"))
        print("*** Processing", file_name)
        print(f"{int_days[today]} in {airports[here]['city']}")
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
