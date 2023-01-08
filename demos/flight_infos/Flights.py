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
    #     },
    def __init__(self, obj):
        self.flight = obj

    def __getitem__(self, item):
        return self.flight[item]

    def show(self, show=None) -> str:
        if show is None:
            show = {"airline", "city", "week_day", "day"}
        rline = self.flight["AIRLINE"]
        res = [f'{airlines[rline].ljust(9) if "airline" in show else rline}{self.flight["FLIGHT_NUMBER"]:<4}']
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
            res.append(": %5d $" % self.cost())
        return " ".join(res)

    def cost(self) -> int:
        # make up a cost for a flight
        # cost = fixed cost (100$) + 0.20$ per mile + 200$ on Friday, Saturday and Sunday
        dist = int(self.flight["DISTANCE"])
        day = self.flight["DAY_OF_WEEK"]
        return 100 + (dist // 5 * 5) + (200 if day > 4 else 0)


# Originally we had defined a class for Flights, but it turned out to be simpler to define
# Flights as a list of Flight(s), because this list can be grouped many times
Flights = list[Flight]


def show_flights(flights: Flights, show_params=None) -> list[str]:
    limit = 5
    nb = len(flights)
    res = []
    if nb > 0:
        if nb <= limit:
            for f in flights:
                res.append(f.show(show_params))
        else:  # regroup by Airline
            params = {"cost"} if show_params is not None and "cost" in show_params else {}
            rlines = group_flights(flights, "AIRLINE")
            for rline in rlines:
                days = group_flights(rline, "DAY_OF_WEEK")  # regroup by day of the week
                if len(days) == 1:
                    res.append(S(NP(NO(len(rline)), N("flight")),
                                 PP(P("by"), Q(airlines[rline[0]["AIRLINE"]])),
                                 PP(P("on"), N(int_days[rline[0]["DAY_OF_WEEK"]]))).realize())
                    res.append("  " + ", ".join(f.show(params) for f in rline))
                else:
                    res.append(S(NP(NO(len(rline)), N("flight")),
                                 PP(P("by"), Q(airlines[rline[0]["AIRLINE"]]))).realize())
                    for d in days:
                        res.append("  " + int_days[d[0]["DAY_OF_WEEK"]].ljust(9) + ":" +
                                   ", ".join(f.show(params) for f in d))
    return res


def match_flights(flights: Flights, orig, dest, air_code, flight_number, orig_time_rng, dest_time_rng, days) \
        -> list[Flight]:
    # find matching flights by looking at all flights
    res = []
    for flight in flights:
        if all((
                orig is None or orig == flight["ORIGIN_AIRPORT"],
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


def group_flights(flights: list[Flight], by: Union[str, Callable[[Flight], str]]) -> list[list[Flight]]:
    # Group flights by a given field or by a grouping function or string corresponding to a field of a flight
    groups: dict[str, list[Flight]] = {}
    if isinstance(by, str):
        field = by
        by = lambda f: f[field]
    for flight in flights:
        group_id = by(flight)
        if group_id not in groups:
            groups[group_id] = []
        groups[group_id].append(flight)
    return [groups[key] for key in sorted(groups.keys())]


def show_groups(self, field):
    groups = self.group(field)
    print(f"By {field} : {len(self.flights)} flights in {len(groups)} groups")
    for g in groups:
        print(f"{g[0][field]}:{len(g)}")
    print("----")


# load data base
pwd = os.path.dirname(__file__)
db = json.load(open(os.path.join(pwd, "flightDB.json"), "r", encoding="utf-8"))
airports: dict[str, dict[str, str]] = db["airports"]
airlines: dict[str, str] = db["airlines"]
flights = [Flight(f) for f in db["flights"]]
