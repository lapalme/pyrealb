import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..','src')))

from pyrealb import *
load("fr")

def test_numbers_fr_0():
    assert (
NO("1000").realize()   
    ) == '1\xa0000',\
    '1000 => 1\xa0000'


def test_numbers_fr_1():
    assert (
NO("1000000").realize()   
    ) == '1\xa0000\xa0000',\
    '1000000 => 1\xa0000\xa0000'


def test_numbers_fr_2():
    assert (
NO("1000.1").realize()   
    ) == '1\xa0000,10',\
    '1000.1 => 1\xa0000,10'


def test_numbers_fr_3():
    assert (
NO("1.03850343753").realize()   
    ) == '1,04',\
    '1.038503437530 => 1,04'


def test_numbers_fr_4():
    assert (
NO("2135454").realize()   
    ) == '2\xa0135\xa0454',\
    '2135454 => 2\xa0135\xa0454'


def test_numbers_fr_5():
    assert (
NO("1000.156").realize()   
    ) == '1\xa0000,16',\
    '1000.156 => 1\xa0000,16'


def test_numbers_fr_6():
    assert (
NO("99999999999").realize()   
    ) == '99\xa0999\xa0999\xa0999',\
    '99999999999 => 99\xa0999\xa0999\xa0999'


def test_numbers_fr_7():
    assert (
NO("15.48").realize()   
    ) == '15,48',\
    '15.48 => 15,48'


def test_numbers_fr_8():
    assert (
NP(NO("15.48"),
   N("livre")).realize()   
    ) == '15,48 livres',\
    '1. Accord avec le nombre'


def test_numbers_fr_9():
    assert (
NP(NO("1.45"),
   N("livre")).realize()   
    ) == '1,45 livre',\
    '2. Accord avec le nombre'


def test_numbers_fr_10():
    assert (
NP(NO("0.988"),
   N("livre")).realize()   
    ) == '0,99 livre',\
    '3. Accord avec le nombre'


def test_numbers_fr_11():
    assert (
NP(NO("-12"),
   N("livre")).realize()   
    ) == '-12 livres',\
    '4. Accord avec le nombre'


def test_numbers_fr_12():
    assert (
NP(NO("2"),
   N("livre")).realize()   
    ) == '2 livres',\
    '5. Accord avec le nombre'


def test_numbers_fr_13():
    assert (
NP(NO("0.5485894"),
   N("livre")).realize()   
    ) == '0,55 livre',\
    '6. Accord avec le nombre'

