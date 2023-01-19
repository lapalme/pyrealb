import os, json
from flight_time import time_match, check_day, int_days
from typing import Union, Callable
from pyrealb import *


def show_time(time: str) -> str:
    return f'{time[:2]}:{time[2:]}'


class Flight:
    #     each flight has the following fields
    # {
    #       "MONTH": 1,
    #       "DAY": 1,
    #       "DAY_OF_WEEK": 4,
    #       "AIRLINE": "DL",
    #       "FLIGHT_NUMBER": "2336",
    #       "ORIGIN_AIRPORT": "DEN",
    #       "DESTINATION_AIRPORT": "ATL",
    #       "SCHEDULED_DEPARTURE": "0030",
    #       "DISTANCE": "1199",
    #       "SCHEDULED_ARRIVAL": "0523"
    #       "COST": 1234  # added by selectFlights.py
    #     },
    def __init__(self, obj):
        self.flight = obj
        # so that flight numbers are sorted correctly
        self.flight["FLIGHT_NUMBER"] = int(self.flight["FLIGHT_NUMBER"])

    def __getitem__(self, item):
        return self.flight[item]

    def show(self, show) -> str:
        airline = self.flight["AIRLINE"]
        res = [f'{airlines[airline].ljust(9) if "airline" in show else airline}{self.flight["FLIGHT_NUMBER"]:<4}']
        if "city" in show:
            res.append(airports[self.flight["ORIGIN_AIRPORT"]]["city"])
        res.append(show_time(self.flight["SCHEDULED_DEPARTURE"]))
        res.append("=>")
        if "city" in show:
            res.append(airports[self.flight["DESTINATION_AIRPORT"]]["city"])
        res.append(show_time(self.flight["SCHEDULED_ARRIVAL"]))
        if "week_day" in show:
            res.append(int_days[self.flight["DAY_OF_WEEK"]])
        if "day" in show:
            res.append(str(self.flight["DAY"]))
        if "cost" in show:
            res.append(": %5d $" % self.flight["COST"])
        return " ".join(res)


# Originally we had defined a class for Flights, but it turned out to be simpler to define
# Flights as list[Flight], because this list can be grouped many times and used as a list (index, iterated...)
Flights = list[Flight]
Flight_groups = dict[str, list[Flight]]


def show_flights(flights: Flights, show_params) -> list[str]:
    limit = 5
    nb = len(flights)
    res = []
    if nb > 0:
        if nb <= limit:
            for f in flights:
                res.append(f.show(show_params))
        else:  # regroup by Airline
            rlines = group_flights(flights, "AIRLINE")
            for (rline, flights) in sorted(rlines.items()):
                res.append(S(NP(NO(len(flights)), N("flight")),
                             PP(P("by"), Q(airlines[rline]))).realize())
                fl_numbers = group_flights(flights, "FLIGHT_NUMBER")  # regroup by flight number
                # show_groups(fl_numbers,"FLIGHT_NUMBER")
                for (fl_number, flights) in sorted(fl_numbers.items()):
                    days = set(fl["DAY_OF_WEEK"] for fl in flights)
                    s = S(Q(flights[0].show({"default"})))
                    if len(days) == 7:
                        s.add(A("everyday"))
                    elif len(days) == 6:
                        for i in range(1, 8):
                            if i not in days:
                                s.add(AP(A("everyday"), P("except"), N(int_days[i])))
                                break
                    elif len(days) == 5 and {1, 2, 3, 4, 5} == days:
                        s.add(NP(D("every"), N("weekday")))
                    else:
                        s.add(PP(P("on"), CP(C("or"), [N(int_days[d]) for d in sorted(days)])))
                    res.append(s.realize())
    return res


def match_flights(flights: Flights, orig, dest, air_code, flight_number, orig_time_rng, dest_time_rng, days) \
        -> list[Flight]:
    # find matching flights by looking at all flights
    res = []
    for flight in flights:
        if all((orig is None or orig == flight["ORIGIN_AIRPORT"],
                dest is None or dest == flight["DESTINATION_AIRPORT"],
                air_code is None or air_code == flight["AIRLINE"],
                flight_number is None or flight_number == flight["FLIGHT_NUMBER"],
                orig_time_rng is None or time_match(orig_time_rng,
                                                    int(flight["SCHEDULED_DEPARTURE"][0:2])),
                dest_time_rng is None or time_match(dest_time_rng,
                                                    int(flight["SCHEDULED_ARRIVAL"][0:2])),
                days is None or check_day(flight["DAY_OF_WEEK"], days)
        )): res.append(flight)
    return res


def group_flights(flights: Flights, by: Union[str, Callable[[Flight], str]]) -> Flight_groups:
    # Group flights by a given field or by a grouping function or string corresponding to a field of a flight
    groups: Flight_groups = {}
    if isinstance(by, str):
        field = by
        by = lambda f: f[field]
    for flight in flights:
        group_id = by(flight)
        if group_id not in groups:
            groups[group_id] = []
        groups[group_id].append(flight)
    return groups


def show_groups(groups:Flight_groups, field:str):
    print(f"By {field} : {sum(len(v) for v in groups.values())} flights in {len(groups.keys())} groups")
    for (key, flights) in groups.items():
        print(f"{key}:{len(flights)}")
    print("----")


# load data base
pwd = os.path.dirname(__file__)
db = json.load(open(os.path.join(pwd, "Flight Data", "flightDB.json"), "r", encoding="utf-8"))
airports: dict[str, dict[str, str]] = db["airports"]
airlines: dict[str, str] = db["airlines"]
flights:Flights = [Flight(f) for f in db["flights"]]
