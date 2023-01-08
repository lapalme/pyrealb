# process time related infos for flights

import re
from typing import Optional, Union
from pyrealb import *

# precompute list of strings that are used for hours, days and months in entity values
from datetime import datetime

numbers = [NO(n).nat(True).realize().replace("-", " ") for n in range(0, 32)]  # used for hours and days
month_only = {f: False for f in ["year", "day", "date", "hour", "minute", "second", "det"]}
months = [DT(datetime(2022, m, 1)).dOpt(month_only).realize().lower() for m in range(1, 13)]
day_numbers = [NO(n).dOpt({"ord": True}).realize().replace("-", " ") for n in range(0, 32)]

# days number used in flightDB
int_days: list[str] = ["*no day*", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
days_int: dict[str, int] = {"monday": 1, "tuesday": 2, "wednesday": 3, "thursday": 4, "friday": 5, "saturday": 6,
                            "sunday": 7}
periods_of_day: dict[str, tuple[int, int]] = {
    "night": (0, 6), "nights": (0, 6), "nighttime": (0, 6), "early": (5, 9),
    "morning": (6, 12), "mornings": (6, 12), "am": (6, 12),
    "noon": (11, 13), "lunch time": (12, 14),
    "afternoon": (12, 18), "afternoons": (12, 18), "pm": (12, 18), "late afternoon": (16, 19),
    "dinnertime": (18, 20), "evening": (18, 24), "midnight": (23, 23)}


def time_match(hour_rng: tuple[int, int], hour: int) -> bool:
    # implements a closed interval, not a Python range
    if hour_rng[0] is None:
        return hour <= hour_rng[1]
    if hour_rng[1] is None:
        return hour_rng[0] <= hour
    return hour_rng[0] <= hour <= hour_rng[1]


def check_day(flight_day: int, wanted_days: Union[set[int], int]) -> bool:
    if type(wanted_days) is set:
        return flight_day in wanted_days
    return flight_day == wanted_days


def parse_hour(s: str) -> Optional[int]:
    if re.match(r"12(\d+)? pm|noon|mealtime", s): return 12  # very special cases
    if s in numbers: return numbers.index(s)
    m = re.match(r"(\d+)(( o'clock)?( [ap]m)?)?", s)
    if m is None:
        print("@@@ parse_hour: cannot parse:", s)
        return None
    h = int(m[1])
    if h >= 100: h = h // 100
    if m[4] is not None and "pm" in m[4]: h += 12
    if h > 23:
        print("@@@ parse_hour: strange hour", h)
    return h


def process_time_period(time_infos: dict[str, str], time_relative: Optional[str]) -> Optional[tuple[int, int]]:
    # print(time_relative,time_infos)
    if "time" in time_infos:
        if time_infos["time"] in periods_of_day:
            return periods_of_day[time_infos["time"]]
        hour = parse_hour(time_infos["time"])
        if time_relative is not None:
            if time_relative in ["before", "by", "no later than", "prior to", "earlier"]:
                return (0, hour)
            elif time_relative in ["after", "later"]:
                return (hour, 24)
            elif time_relative in ["around", "about", "vicinity", "approximately", "near"]:
                return (hour - 2, hour + 2)
            elif time_relative == "close":
                return (hour - 1, hour + 1)
            else:
                print("@@@ unknown time_relative:", time_relative)
        elif "period_of_day" in time_infos and time_infos["period_of_day"] == "afternoon":
            return (hour + 12, 24)
        else:  # when a precise time is given, accept departure or arrival a little sooner
            return (hour - 1, hour)
    elif "period_of_day" in time_infos:
        value = time_infos["period_of_day"]
        if value in periods_of_day:
            return periods_of_day[value]
        else:
            print("@@@ strange period_of_day", value)
    elif "start_time" in time_infos and "end_time" in time_infos:
        return (parse_hour(time_infos["start_time"]), parse_hour(time_infos["end_time"]))
    return None
