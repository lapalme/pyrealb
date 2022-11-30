# Query the flightDB.json
# ideally this would be called from the entities extracted by RASA
# but when called as a main we "trick" the system, by using the
# entities from the {training|test}.json files

import json, re, os
from typing import Optional, Union, Callable, Any

from pyrealb import *

if __name__ == "__main__":
    import Entities_module
    import realize_example
else:
    from . import Entities_module
    from . import realize_example
Entities = Entities_module.Entities

Flight = dict[str, Union[int, str, tuple[int, int]]]
""" typical information about a flight
{
      "MONTH": 1,
      "DAY": 1,
      "DAY_OF_WEEK": 4,
      "AIRLINE": "DL",
      "FLIGHT_NUMBER": "2336",
      "ORIGIN_AIRPORT": "DEN",
      "DESTINATION_AIRPORT": "ATL",
      "SCHEDULED_DEPARTURE": "0030",
      "DISTANCE": "1199",
      "SCHEDULED_ARRIVAL": "0523"
    },
"""
pwd = os.path.dirname(__file__)
db = json.load(open(os.path.join(pwd,"..","..","Flight Data","flightDB.json"), "r", encoding="utf-8"))
airports: dict[str, dict[str, str]] = db["airports"]
airlines: dict[str, str] = db["airlines"]
flights: list[Flight] = db["flights"]


# matching information
def airport_code(name: str) -> Optional[str]:
    # find airport code from name
    if name is None or name in airports: return name
    name = name.lower()
    for code in airports:
        if name in airports[code]["city"].lower() or name in airports[code]["name"].lower():
            return code
    return None


def airline_code(name: str) -> Optional[str]:
    # find airline code from name
    if name is None or name in airlines: return name
    name = name.lower()
    for code in airlines:
        if name in airlines[code].lower():
            return code
    return None


def time_match(hour_rng: tuple[int, int], hour: int) -> bool:
    # implements a closed interval, not a Python range
    if hour_rng is None: return True
    return hour_rng[0] <= hour <= hour_rng[1]


def flight_cost(flight: Flight) -> int:
    # make up a cost for a flight
    # cost = fixed cost (100$) + 0.20$ per mile + 200$ on Friday, Saturday and Sunday
    dist = int(flight["DISTANCE"])
    day = flight["DAY_OF_WEEK"]
    return 100 + (dist // 5 * 5) + (200 if day > 4 else 0)


def check_day(flight_day: int, wanted_days: Union[set[int], int]) -> bool:
    if type(wanted_days) is set:
        return flight_day in wanted_days
    return flight_day == wanted_days


# simple-minded approach to flight matching
def find_flights(infos: Flight) -> list[Flight]:
    orig = airport_code(infos.get("origin"))
    if orig is None and infos.get("origin") is not None:
        print("@@@ could not find origin:", infos.get("origin"))
    dest = airport_code(infos.get("destination"))
    if dest is None and infos.get("destination") is not None:
        print("@@@ could not find destination:", infos.get("destination"))
    air_code = airline_code(infos.get("airline"))
    if air_code is None and infos.get("airline") is not None:
        print("@@@ could not find airline:", infos.get("airline"))
    ## find matching flights by looking at all flights
    res = []
    for flight in flights:
        if all((
                orig is None or orig == flight["ORIGIN_AIRPORT"],
                dest is None or dest == flight["DESTINATION_AIRPORT"],
                air_code is None or air_code == flight["AIRLINE"],
                "flight_number" not in infos or infos["flight_number"] == ["FLIGHT_NUMBER"],
                "orig_time_rng" not in infos or time_match(infos["orig_time_rng"], int(flight["SCHEDULED_DEPARTURE"][0:2])),
                "dest_time_rng" not in infos or time_match(infos["dest_time_rng"], int(flight["SCHEDULED_ARRIVAL"][0:2])),
                "days" not in infos or check_day(flight["DAY_OF_WEEK"], infos["days"])
        )): res.append(flight)
    return res


def show_time(time: str) -> str:
    return f'{time[:2]}:{time[2:]}'


# days number used in flightDB
int_days: list[str] = ["*no day*", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
days_int: dict[str, int] = {"monday": 1, "tuesday": 2, "wednesday": 3, "thursday": 4, "friday": 5, "saturday": 6,
                            "sunday": 7}


def show_flight(flight: Flight, show_cost: bool = False) -> str:
    return f'{airlines[flight["AIRLINE"]]:<8} {flight["FLIGHT_NUMBER"]:<4}' + \
           f' {airports[flight["ORIGIN_AIRPORT"]]["city"]} {show_time(flight["SCHEDULED_DEPARTURE"])}' + \
           f' => {airports[flight["DESTINATION_AIRPORT"]]["city"]} {show_time(flight["SCHEDULED_ARRIVAL"])}' + \
           f' {int_days[flight["DAY_OF_WEEK"]]} {flight["DAY"]}' + \
           (" : %5d $" % flight_cost(flight) if show_cost else "")


def show_flights(flights: list[Flight], show_cost: bool = False) -> list[str]:
    limit=5
    nb = len(flights)
    res = []
    if nb > 0:  # simplify output when debugging
        for f in flights[:limit]:
            res.append(show_flight(f, show_cost))
        if nb>5:
            res.append(f"... {nb-limit} others")
    return res


def answer_nb_flights(entities: Entities, flights: list[Flight]) -> str:
    nb = len(flights)
    return S(Pro("there"),
             VP(V("be").n("s" if nb == 1 else "p"),
                NP(NO(nb), N("flight")),
                realize_example.realize_common(entities))).realize()


value_ent_role_re = re.compile(r'\[(?P<val>.*?)](\((?P<ent0>.*?)\)|{"entity":"(?P<ent>.*?)","role":"(?P<role>.*?)"})')


def parse_hour(s: str) -> Optional[int]:
    if re.match(r"12(\d+)? pm|noon|mealtime", s): return 12  # very special cases
    m = re.match(r"(\d+)(( o'clock)?( [ap]m)?)?",s)
    if m is None:
        print("@@@ parse_hour: cannot parse:", s)
        return None
    h = int(m[1])
    if h >= 100: h = h // 100
    if m[4] is not None and "pm" in m[4]: h += 12
    if h > 23:
        print("@@@ parse_hour: strange hour", h)
    return h


periods_of_day: dict[str, tuple[int, int]] = {
    "night": (0, 6), "early": (5, 9), "morning": (6, 12), "mornings": (6, 12), "am": (6, 12),
    "noon": (11, 13), "afternoon": (12, 18), "pm": (12, 18), "late afternoon": (16, 19),
    "evening": (18, 24), "midnight": (23, 23)}


def process_time_period(time_infos: dict[str, str], time_relative: Optional[str]) -> Optional[tuple[int, int]]:
    # print(time_relative,time_infos)
    if "time" in time_infos:
        hour = parse_hour(time_infos["time"])
        if time_relative is not None:
            if time_relative in ["before", "by", "no later than", "prior to"]:
                return (0, hour)
            elif time_relative in ["after", "later"]:
                return (hour, 24)
            elif time_relative in ["around", "about"]:
                return (hour - 2, hour + 2)
            elif time_relative == "close":
                return (hour - 1, hour + 1)
            else:
                print("@@@ unknown time_relative:", time_relative)
    elif "period_of_day" in time_infos:
        value = time_infos["period_of_day"]
        if value in periods_of_day:
            return periods_of_day[value]
        else:
            print("@@@ strange period_of_day", value)
    elif "start_time" in time_infos and "end_time" in time_infos:
        return (parse_hour(time_infos["start_time"]), parse_hour(time_infos["end_time"]))
    return None


def extract_flight_infos(entities: Entities) -> Flight:
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
        elif entity == "airline_name":
            infos["airline"] = value
        elif entity == "flight_number":
            infos["flight_number"] = value
        elif entity == "time_relative":
            infos["time_relative"] = value
        elif role == "depart_time":
            orig_time[entity] = value
        elif role == "arrive_time":
            dest_time[entity] = value
        elif entity == "day_name" and role == "depart_date":
            value = value.lower()
            if value in days_int:
                infos["days"] = days_int[value]
            else:
                print("@@@ unknown day_name:", value)
    infos["orig_time_rng"] = process_time_period(orig_time, infos.get("time_relative"))
    infos["dest_time_rng"] = process_time_period(dest_time, infos.get("time_relative"))
    return infos


def show_no_flight() -> list[str]:
    return [S(NP(D("no"), N("flight").n("p")),
              VP(V("be").t("ps"),
                 V("find").t("pp"))).realize()]


########
#   intent processing

def process_flight(entities: Entities) -> list[str]:
    # query the database
    flights = find_flights(extract_flight_infos(entities))
    # realize the answer followed by the table of flights
    ## HACK: change " 0 flights" by "no flights" in the final realization
    return [
        answer_nb_flights(entities, flights).replace(" 0 flights", " no flights"),
        *show_flights(flights)
    ]


def process_airfare(entities: Entities) -> list[str]:
    ##  extract specific about fares
    cost_relative = None
    if entities.has_entity("cost_relative"):
        cost_relative = entities.get_value("cost_relative")
    # query the database
    flights = find_flights(extract_flight_infos(entities))
    if len(flights) == 0:
        return show_no_flight()
    else:
        # find costs of flights
        if cost_relative is None:
            return show_flights(flights, True)
        else:
            if cost_relative in ["cheapest", "lowest", "least expensive"]:
                return show_flights([min(flights, key=flight_cost)], True)
            elif cost_relative in ["highest", "most expensive"]:
                return show_flights([max(flights, key=flight_cost)], True)
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
        return show_no_flight()
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

# this is the entry point for RASA
def process_intent(intent, entity_list:list[dict[str,Any]]) -> str:
    entities=Entities(entity_list)
    if intent in ["flight", "flight_no"]:
        return "\n".join(process_flight(entities))
    elif intent in ["airfare", "flight+airfare"]:
        return "\n".join(process_airfare(entities))
    elif intent == "airline":
        return "\n".join(process_airline(entities))
    elif intent == "abbreviation":
        return "\n".join(process_abbreviation(entities))
    elif intent == "day_name":
        return "\n".join(process_day_name(entities))
    elif intent in ["ground_service", "capacity", "distance", "aircraft",
                    "ground_fare", "meal", "quantity", "city", "airport"]:
        return "%s information not in database" % intent
    else:
        return "@@@ intent not yet implemented:" + intent


def process_examples_by_intent(examples: dict[str, list[tuple[str, Entities]]]) -> None:
    def do_all_exs(intent: str, fn: Callable[[Entities], list[str]], exs: list[tuple[str, Entities]]):
        for txt, entities in exs:
            ## print the original text by replacing entities by their value
            print("%s : %s" % (intent, value_ent_role_re.sub(r"\g<val>", txt)))
            print("\n".join(fn(entities)))
            print("----")

    ## process intents in decreasing numer of examples:
    for intent, exs in sorted(examples.items(), key=lambda x: len(x[1]), reverse=True):
        print(NP(NO(len(examples[intent])), N("example"), PP(P("for"), Q(intent))).realize())
        if intent in ["flight", "flight_no"]:
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
    ## single example for débugging...
    example = json.loads("""
      {
        "text": "i need a flight from atlanta to san francisco on saturday",
        "intent": "flight",
        "entities": [
          {
            "start": 21,
            "end": 28,
            "value": "atlanta",
            "entity": "city_name",
            "role": "fromloc"
          },
          {
            "start": 32,
            "end": 45,
            "value": "san francisco",
            "entity": "city_name",
            "role": "toloc"
          },
          {
            "start": 49,
            "end": 57,
            "value": "saturday",
            "entity": "day_name",
            "role": "depart_date"
          }
        ]
      }
    """)
    print(process_intent(example["intent"],example["entities"]))
    #
    # examples: dict[str, list[tuple[str, Entities]]] = {}
    # file_name = os.path.join(pwd,"..","..","Examples","test.json")
    # print("processing", file_name)
    # common_examples = json.load(open(file_name, "r", encoding="utf-8"))["rasa_nlu_data"]["common_examples"]
    # for e in common_examples:
    #     intent = e["intent"]
    #     if intent not in examples: examples[intent] = []
    #     examples[e["intent"]].append((e["text"], Entities(e["entities"])))
    # process_examples_by_intent(examples)
