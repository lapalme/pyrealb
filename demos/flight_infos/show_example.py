# Sentence realization using Python string manipulation from ATIS data
# this code uses a similar organization as the one in realize_example.py
# in which the functions starting with "show..." are named "realize..."

from Entities import flight_fields, Entities
from typing import Callable


def show(prefix: str, entities: Entities, fields: list[str], parent=None) -> [str]:
    res = []
    for f in fields:
        val = entities.grab_value(f, parent)
        if len(val) > 0:
            res.append(val)
    if len(res) > 0 and len(prefix) > 0:
        res.insert(0, prefix)
    return res


def show_loc(prefix: str, entities: Entities, parent: str = None) -> [str]:
    return show(prefix, entities,
                ["city_name", "state_name", "state_code", "country_name",
                 "airport_name", "airport_code"],
                parent)


def show_date(entities: Entities, parent: str = None) -> [str]:
    return show("", entities,
                ["date_relative", "today_relative", "day_name", "month_name", "day_number", "year"],
                parent)


def show_time(entities: Entities, parent: str = None) -> [str]:
    res = []
    if entities.has_entity("start_time", parent) and entities.has_entity("end_time", parent):
        res.append(f'between {entities.grab_value("start_time", parent)} and ' +
                   entities.grab_value("end_time", parent))
    res.extend(show("", entities, ["start_time", "time_relative", "time",
                                   "period_of_day", "period_mod", "end_time"], parent))
    return res


def show_common(entities: Entities, res: list[str]) -> None:
    def date_time(kind, verb):
        if entities.has_role(kind + "_date") or entities.has_role(kind + "_time"):
            res.append(verb)
            res.extend(show_date(entities, kind + "_date"))
            res.extend(show_time(entities, kind + "_time"))

    res.extend(show_loc("from", entities, "fromloc"))
    res.extend(show_loc("to", entities, "toloc"))
    res.extend(show_loc("stopping in", entities, "stoploc"))
    date_time("depart", "departing on")
    date_time("arrive", "arriving at")
    date_time("return", "returning")
    res.extend(show("on", entities, ["airline_name", "airline_code",
                                     "airport_name", "airport_code",
                                     "aircraft_code",
                                     "flight_number", "flight_code"]))
    res.extend(show("serving", entities, ["city_name", "meal", "meal_description", "meal_code"]))
    res.extend(show("with", entities, ["fare_basis_code"]))
    res.extend(show("at", entities, ["airport_name"]))


def show_intent(intent: str, entities: Entities) -> [str]:
    def flight() -> [str]:
        entities.grab_value("flight")  # ignore this redundant field for a flight intent...
        res = show("show", entities, flight_fields)
        res.append("flights")
        res.extend(show("at", entities, ["cost_relative", "fare_amount"]))
        show_common(entities, res)
        return res

    def airfare() -> [str]:
        res = show("what is a", entities, flight_fields)
        res.append("fare")
        res.extend(show("", entities, ["cost_relative", "fare_amount"]))
        show_common(entities, res)
        return res

    def ground_service() -> [str]:
        res = ["what is the"]
        if entities.has_entity("transport_type"):
            res.extend(show("", entities, ["transport_type"]))
        else:
            res.append("ground service")
        res.extend(show_loc("in", entities, None))
        res.extend(show_date(entities, None))
        res.extend(show_time(entities, None))
        show_common(entities, res)
        return res

    def airline() -> [str]:
        if len(entities) == 1:
            if entities.has_entity("airline_code"):
                res = [f'which airline is {entities.grab_value("airline_code")}']
            elif entities.has_entity("city_name"):
                res = [f'which airline serves {entities.grab_value("city_name")}']
            else:
                res = show("Show", entities, flight_fields)
                res.append("flights")
        else:
            res = ["List"]
            res.extend(show("", entities, flight_fields))
            res.append("flights")
        show_common(entities, res)
        return res

    def abbreviation() -> [str]:
        if len(entities) == 0:
            res = ["explain the fare codes"]
        elif len(entities) == 1:
            first = entities[0].get_entity()
            value = entities.grab_value(first)
            if first.endswith("code"):
                res = [f'explain the meaning of the '
                       f'{value} {first.replace("_", " ")}']
            else:
                res = [f'explain {value} code']
        else:
            res = [f'what does mean the abbreviation']
        show_common(entities, res)
        return res

    def aircraft() -> [str]:
        res = ["what is the"]
        res.extend(show("", entities, flight_fields))
        res.append("plane")
        show_common(entities, res)
        return res

    def flight_time() -> [str]:
        val = entities.grab_value("flight_time")
        if len(val) > 0:
            if val.endswith("s"):
                res = ["what are the", val]
            else:
                res = ["what is the", val]
        else:
            res = ["what is the connection time"]
            if len(entities) > 0:
                res.append("in")
        res.extend(show("", entities, flight_fields))
        show_common(entities, res)
        return res

    def quantity() -> [str]:
        res = ["how many"]
        res.extend(show("", entities, flight_fields))
        res.append("flights")
        res.extend(show("in", entities, ["class_type"]))
        show_common(entities, res)
        return res

    def distance() -> [str]:
        res = [f'what is the distance']
        show_common(entities, res)
        return res

    def airport() -> [str]:
        if len(entities) == 0:
            res = ["airports"]
        else:
            val = entities.grab_value("airport_name")
            if len(val) > 0:
                res = [f'describe {val if val.endswith("airport") else (val + " airport")}']
            else:
                val = entities.grab_value("city_name")
                res = ["what is the"]
                res.extend(show("", entities, ["mod"]))
                res.append(f"airport at {val}")
                res.extend(show("", entities, ["state_code", "state_name"]))
        show_common(entities, res)
        return res

    def city() -> [str]:
        res = [f'show cities']
        show_common(entities, res)
        return res

    def ground_fare() -> [str]:
        res = [f'how much']
        val = entities.grab_value("transport_type")
        if len(entities) > 0:
            res.append(
                f'for a {val if len(val) > 0 else "ground transportation"} in {entities.grab_value("city_name")}')
        show_common(entities, res)
        return res

    def capacity() -> [str]:
        res = ["what is the"]
        res.extend(show("", entities, flight_fields))
        res.append("seating capacity")
        show_common(entities, res)
        return res

    def flight_no() -> [str]:
        res = ["what is the flight number"]
        if len(entities) > 0:
            res.extend(show("for the", entities, flight_fields))
            res.append("flight")
        show_common(entities, res)
        return res

    def day_name() -> [str]:
        res = ["what day of the week is flight"]
        show_common(entities, res)
        return res

    def restriction() -> [str]:
        res = [f'what are the']
        res.extend(show("", entities, ["restriction_code"]))
        res.append("restrictions on")
        res.extend(show("", entities, flight_fields))
        res.append("flights")
        show_common(entities, res)
        return res

    def meal() -> [str]:
        res = [f'are there flights']
        show_common(entities, res)
        return res

    def cheapest() -> [str]:
        res = [f'what is the {entities.grab_value("cost_relative")} flight']
        show_common(entities, res)
        return res

    intents: dict[str, Callable[[], list[str]]] = {
        "flight": flight, "airfare": airfare, "ground_service": ground_service,
        "airline": airline, "abbreviation": abbreviation, "aircraft": aircraft,
        "flight_time": flight_time, "quantity": quantity, "distance": distance,
        "airport": airport, "city": city, "ground_fare": ground_fare, "capacity": capacity,
        "flight_no": flight_no, "day_name": day_name, "restriction": restriction,
        "meal": meal, "cheapest": cheapest}
    if intent in intents:
        return intents[intent]()
    return f'TODO:{intent}'


def show_intents(intent: str, entities: Entities) -> [str]:
    if entities.has_entity("or"):
        res = []
        for es in entities.split("or"):
            res.extend(show_intent(intent, es))
            res.append("or")
        return res[:-1]
    return show_intent(intent, entities)


def show_example(intent: str, entities: Entities, _showSource: bool = False) -> str:
    intents = intent.split("+")
    res = show_intents(intents[0], entities)
    if len(intents) > 1:
        res.append("and" if len(intents) == 2 else ",")
        res.extend(show_intents(intents[1], entities))
        if len(intents) == 3:
            res.append("and")
            res.extend(show_intents(intents[2], entities))
    return " ".join(r for r in res if len(r) > 0)
