import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..','src')))

from pyrealb import *
load("en")

def test_numbers_en_0():
    assert (
NO("1000").realize()   
    ) == '1,000',\
    '1000 => 1,000'


def test_numbers_en_1():
    assert (
NO("1000000").realize()   
    ) == '1,000,000',\
    '1000000 => 1,000,000'


def test_numbers_en_2():
    assert (
NO("1000.1").realize()   
    ) == '1,000.10',\
    '1000.1 => 1,000.10'


def test_numbers_en_3():
    assert (
NO("1.03850343753").realize()   
    ) == '1.04',\
    '1.038503437530 => 1.04'


def test_numbers_en_4():
    assert (
NO("2135454").realize()   
    ) == '2,135,454',\
    '2135454 => 2,135,454'


def test_numbers_en_5():
    assert (
NO("1000.156").realize()   
    ) == '1,000.16',\
    '1000.156 => 1,000.16'


def test_numbers_en_6():
    assert (
NO("99999999999").realize()   
    ) == '99,999,999,999',\
    '99999999999 => 99,999,999,999'


def test_numbers_en_7():
    assert (
NO("15.48").realize()   
    ) == '15.48',\
    '15.48 => 15.48'


def test_numbers_en_8():
    assert (
NP(NO("15.48"),
   N("pound")).realize()   
    ) == '15.48 pounds',\
    '1. Accord avec le nombre'


def test_numbers_en_9():
    assert (
NP(NO("1.45"),
   N("pound")).realize()   
    ) == '1.45 pounds',\
    '2. Accord avec le nombre'


def test_numbers_en_10():
    assert (
NP(NO("1"),
   N("pound")).realize()   
    ) == '1 pound',\
    '3.a Accord avec le nombre'


def test_numbers_en_11():
    assert (
NP(NO("0.988"),
   N("pound")).realize()   
    ) == '0.99 pounds',\
    '3. Accord avec le nombre'


def test_numbers_en_12():
    assert (
NP(NO("-12"),
   N("pound")).realize()   
    ) == '-12 pounds',\
    '4. Accord avec le nombre'


def test_numbers_en_13():
    assert (
NP(NO("2"),
   N("pound")).realize()   
    ) == '2 pounds',\
    '5. Accord avec le nombre'


def test_numbers_en_14():
    assert (
NP(NO("0.5485894"),
   N("pound")).realize()   
    ) == '0.55 pounds',\
    '6. Accord avec le nombre'

