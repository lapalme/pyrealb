from context import pyrealb
from pyrealb import *
from test import test


def numbers_fr():
    loadFr()
    nums = [
        (NO(1000), "1 000", "1000 => 1 000"),
        (NO(1000000), "1 000 000", "1000000 => 1 000 000"),
        (NO(1000.1), "1 000,10", "1000.1 => 1 000,10"),
        (NO(1.038503437530), "1,04", "1.038503437530 => 1,04"),
        (NO(2135454), "2 135 454", "2135454 => 2 135 454"),
        (NO(1000.156), "1 000,16", "1000.156 => 1 000,16"),
        (NO(99999999999), "99 999 999 999", "99999999999 => 99 999 999 999"),
        (NO(15.48), "15,48", "15.48 => 15,48"),
        (NP(NO(15.48),N("livre")), "15,48 livres", "1. Accord avec le nombre"),
        (NP(NO(1.45),N("livre")), "1,45 livre", "2. Accord avec le nombre"),
        (NP(NO(0.988),N("livre")), "0,99 livre", "3. Accord avec le nombre"),
        (NP(NO(-12),N("livre")), "-12 livres", "4. Accord avec le nombre"),
        (NP(NO(2),N("livre")), "2 livres", "5. Accord avec le nombre"),
        (NP(NO("0.5485894"),N("livre")), "0,55 livre", "6. Accord avec le nombre"),
    ]
    tests=[]
    for exp,expected,message in nums:
        tests.append({
            "expression":exp,
            "expected":expected,
            "message":message
        })
    return tests

if __name__ == '__main__':
    test("English dates","en",numbers_fr)
