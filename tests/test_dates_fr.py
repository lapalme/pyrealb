import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..','src')))

from pyrealb import *
load("fr")

import datetime

theDate="2015-01-01T11:25:45"
date=datetime.datetime.strptime(theDate,"%Y-%m-%dT%H:%M:%S")
exp=DT(theDate)
rtimeOption = {"rtime":date,"hour":False,"minute":False,"second":False}

def test_dates_fr_1():
    assert (
DT("2015-01-01T11:25:45").realize()   
    ) == 'le jeudi 1 janvier 2015 à 11 h 25 min 45 s',\
    'Full info'


def test_dates_fr_2():
    assert (
DT("2015-01-01T11:25:45").dOpt({'day': False, 'date': True}).realize()   
    ) == 'le 1 janvier 2015 à 11 h 25 min 45 s',\
    'Without week day'


def test_dates_fr_3():
    assert (
DT("2015-01-01T11:25:45").dOpt({'day': False, 'month': False, 'year': False}).realize()   
    ) == 'le 1 à 11 h 25 min 45 s',\
    'Without day, month and year'


def test_dates_fr_4():
    assert (
DT("2015-01-01T11:25:45").dOpt({'year': False}).realize()   
    ) == 'le jeudi 1 janvier à 11 h 25 min 45 s',\
    'Without year'


def test_dates_fr_5():
    assert (
DT("2015-01-01T11:25:45").dOpt({'year': False, 'month': False, 'date': False, 'day': False}).realize()   
    ) == 'à 11 h 25 min 45 s',\
    'Only time'


def test_dates_fr_6():
    assert (
DT("2015-01-01T11:25:45").dOpt({'year': False, 'month': False, 'date': False, 'day': False, 'minute': False, 'second': False}).realize()   
    ) == 'à 11 h',\
    'Only hour'


def test_dates_fr_7():
    assert (
DT("2015-01-01T11:25:45").dOpt({'year': False, 'month': False, 'date': False, 'day': False, 'second': False}).realize()   
    ) == 'à 11 h 25',\
    'Only hour and minute'


def test_dates_fr_8():
    assert (
DT("2015-01-01T11:25:45").dOpt({'month': False, 'date': False, 'day': False, 'hour': False, 'minute': False, 'second': False}).realize()   
    ) == 'en 2015',\
    'Only year'


def test_dates_fr_9():
    assert (
DT("2015-01-01T11:25:45").dOpt({'date': False, 'day': False, 'hour': False, 'minute': False, 'second': False}).realize()   
    ) == 'en janvier 2015',\
    'Only month and year'


def test_dates_fr_10():
    assert (
DT("2015-01-01T11:25:45").dOpt({'year': False, 'month': False, 'date': False, 'hour': False, 'minute': False, 'second': False}).realize()   
    ) == 'le jeudi',\
    'Only weekday'


def test_dates_fr_11():
    assert (
DT("2015-01-04T11:00:00").dOpt({'minute': False, 'second': False}).realize()   
    ) == 'le dimanche 4 janvier 2015 à 11 h',\
    'Full info without 0 minutes and 0 seconds'


def test_dates_fr_12():
    assert (
DT("2015-01-01T11:25:45").nat(False).realize()   
    ) == 'jeudi 1/1/2015 11:25:45',\
    'Full info'


def test_dates_fr_13():
    assert (
DT("2015-01-01T11:25:45").dOpt({'day': False, 'date': True}).nat(False).realize()   
    ) == '1/1/2015 11:25:45',\
    'Without week day'


def test_dates_fr_14():
    assert (
DT("2015-01-01T11:25:45").dOpt({'day': False, 'month': False, 'year': False}).nat(False).realize()   
    ) == '1 11:25:45',\
    'Without day, month and year'


def test_dates_fr_15():
    assert (
DT("2015-01-01T11:25:45").dOpt({'year': False}).nat(False).realize()   
    ) == 'jeudi 1/1 11:25:45',\
    'Without year'


def test_dates_fr_16():
    assert (
DT("2015-01-01T11:25:45").dOpt({'year': False, 'month': False, 'date': False, 'day': False}).nat(False).realize()   
    ) == '11:25:45',\
    'Only time'


def test_dates_fr_17():
    assert (
DT("2015-01-01T11:25:45").dOpt({'year': False, 'month': False, 'date': False, 'day': False, 'minute': False, 'second': False}).nat(False).realize()   
    ) == '11',\
    'Only hour'


def test_dates_fr_18():
    assert (
DT("2015-01-01T11:25:45").dOpt({'year': False, 'month': False, 'date': False, 'day': False, 'second': False}).nat(False).realize()   
    ) == '11:25',\
    'Only hour and minute'


def test_dates_fr_19():
    assert (
DT("2015-01-01T11:25:45").dOpt({'month': False, 'date': False, 'day': False, 'hour': False, 'minute': False, 'second': False}).nat(False).realize()   
    ) == '2015',\
    'Only year'


def test_dates_fr_20():
    assert (
DT("2015-01-01T11:25:45").dOpt({'date': False, 'day': False, 'hour': False, 'minute': False, 'second': False}).nat(False).realize()   
    ) == '1/2015',\
    'Only month and year'


def test_dates_fr_21():
    assert (
DT("2015-01-01T11:25:45").dOpt({'year': False, 'month': False, 'day': False, 'hour': False, 'minute': False, 'second': False}).nat(False).realize()   
    ) == '1',\
    'Only date'


def test_dates_fr_22():
    assert (
DT("2014-12-31 11:25:45").dOpt({'rtime': datetime.datetime(2015, 1, 1, 11, 25, 45), 'hour': False, 'minute': False, 'second': False}).realize()   
    ) == 'hier',\
    'one day before'


def test_dates_fr_23():
    assert (
DT("2014-12-30 11:25:45").dOpt({'rtime': datetime.datetime(2015, 1, 1, 11, 25, 45), 'hour': False, 'minute': False, 'second': False}).realize()   
    ) == 'avant-hier',\
    'two days before'


def test_dates_fr_24():
    assert (
DT("2014-12-22 11:25:45").dOpt({'rtime': datetime.datetime(2015, 1, 1, 11, 25, 45), 'hour': False, 'minute': False, 'second': False}).realize()   
    ) == 'il y a 10 jours',\
    'since 10 days'


def test_dates_fr_25():
    assert (
DT("2015-01-01 11:25:45").dOpt({'rtime': datetime.datetime(2015, 1, 1, 11, 25, 45), 'hour': False, 'minute': False, 'second': False}).realize()   
    ) == "aujourd'hui",\
    'same day'


def test_dates_fr_26():
    assert (
DT("2015-01-02 11:25:45").dOpt({'rtime': datetime.datetime(2015, 1, 1, 11, 25, 45), 'hour': False, 'minute': False, 'second': False}).realize()   
    ) == 'demain',\
    'one day after'


def test_dates_fr_27():
    assert (
DT("2015-01-05 11:25:45").dOpt({'rtime': datetime.datetime(2015, 1, 1, 11, 25, 45), 'hour': False, 'minute': False, 'second': False}).realize()   
    ) == 'lundi prochain',\
    'four days after'


def test_dates_fr_28():
    assert (
DT("2015-01-11 11:25:45").dOpt({'rtime': datetime.datetime(2015, 1, 1, 11, 25, 45), 'hour': False, 'minute': False, 'second': False}).realize()   
    ) == 'dans 10 jours',\
    'in 10 days'

