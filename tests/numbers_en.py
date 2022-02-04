from context import pyrealb
from pyrealb.all import *
from test import test


def numbers_en():
    loadEn()
    nums = [
        (NO(1000), "1,000", "1000 => 1,000"),
        (NO(1000000), "1,000,000", "1000000 => 1,000,000"),
        (NO(1000.1), "1,000.10", "1000.1 => 1,000.10"),
        (NO(1.038503437530), "1.04", "1.038503437530 => 1.04"),
        (NO(2135454), "2,135,454", "2135454 => 2,135,454"),
        (NO(1000.156), "1,000.16", "1000.156 => 1,000.16"),
        (NO(99999999999), "99,999,999,999", "99999999999 => 99,999,999,999"),
        (NO(15.48), "15.48", "15.48 => 15.48"),
        (NP(NO(15.48),N("pound")), "15.48 pounds", "1. Accord avec le nombre"),
        (NP(NO(1.45),N("pound")), "1.45 pounds", "2. Accord avec le nombre"),
        (NP(NO(1),N("pound")), "1 pound", "3.a Accord avec le nombre"),
        (NP(NO(0.988),N("pound")), "0.99 pounds", "3. Accord avec le nombre"),
        (NP(NO(-12),N("pound")), "-12 pounds", "4. Accord avec le nombre"),
        (NP(NO(2),N("pound")), "2 pounds", "5. Accord avec le nombre"),
        (NP(NO("0.5485894"),N("pound")), "0.55 pounds", "6. Accord avec le nombre"),
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
    test("English dates","en",numbers_en)
