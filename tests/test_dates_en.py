import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..','src')))

from pyrealb import *
load("en")

import datetime

theDate="2015-01-01T11:25:45"
date=datetime.datetime.strptime(theDate,"%Y-%m-%dT%H:%M:%S")
exp=DT(theDate)
rtimeOption = {"rtime":date,"hour":False,"minute":False,"second":False}

def test_dates_en_1():
    assert (
DT("2015-01-01T11:25:45").realize()   
    ) == 'on Thursday, January 1, 2015 at 11:25:45 a.m.',\
    'Full info'


def test_dates_en_2():
    assert (
DT("2015-01-01T11:25:45").dOpt({'day': False, 'date': True}).realize()   
    ) == 'on January 1, 2015 at 11:25:45 a.m.',\
    'Without week day'


def test_dates_en_3():
    assert (
DT("2015-01-01T11:25:45").dOpt({'day': False, 'month': False, 'year': False}).realize()   
    ) == 'on the 1 at 11:25:45 a.m.',\
    'Without day, month and year'


def test_dates_en_4():
    assert (
DT("2015-01-01T11:25:45").dOpt({'year': False}).realize()   
    ) == 'on Thursday, January 1 at 11:25:45 a.m.',\
    'Without year'


def test_dates_en_5():
    assert (
DT("2015-01-01T11:25:45").dOpt({'year': False, 'month': False, 'date': False, 'day': False}).realize()   
    ) == 'at 11:25:45 a.m.',\
    'Only time'


def test_dates_en_6():
    assert (
DT("2015-01-01T11:25:45").dOpt({'year': False, 'month': False, 'date': False, 'day': False, 'minute': False, 'second': False}).realize()   
    ) == 'at 11 a.m.',\
    'Only hour'


def test_dates_en_7():
    assert (
DT("2015-01-01T11:25:45").dOpt({'year': False, 'month': False, 'date': False, 'day': False, 'second': False}).realize()   
    ) == 'at 11:25 a.m.',\
    'Only hour and minute'


def test_dates_en_8():
    assert (
DT("2015-01-01T11:25:45").dOpt({'month': False, 'date': False, 'day': False, 'hour': False, 'minute': False, 'second': False}).realize()   
    ) == 'in 2015',\
    'Only year'


def test_dates_en_9():
    assert (
DT("2015-01-01T11:25:45").dOpt({'date': False, 'day': False, 'hour': False, 'minute': False, 'second': False}).realize()   
    ) == 'on January 2015',\
    'Only month and year'


def test_dates_en_10():
    assert (
DT("2015-01-01T11:25:45").dOpt({'year': False, 'month': False, 'date': False, 'hour': False, 'minute': False, 'second': False}).realize()   
    ) == 'on Thursday',\
    'Only weekday'


def test_dates_en_11():
    assert (
DT("2015-01-04T11:00:00").dOpt({'minute': False, 'second': False}).realize()   
    ) == 'on Sunday, January 4, 2015 at 11 a.m.',\
    'Full info without 0 minutes and 0 seconds'


def test_dates_en_12():
    assert (
DT("2015-01-01T11:25:45").nat(False).realize()   
    ) == 'Thursday 1/1/2015 11:25:45 a.m.',\
    'Full info'


def test_dates_en_13():
    assert (
DT("2015-01-01T11:25:45").dOpt({'day': False, 'date': True}).nat(False).realize()   
    ) == '1/1/2015 11:25:45 a.m.',\
    'Without week day'


def test_dates_en_14():
    assert (
DT("2015-01-01T11:25:45").dOpt({'day': False, 'month': False, 'year': False}).nat(False).realize()   
    ) == '1 11:25:45 a.m.',\
    'Without day, month and year'


def test_dates_en_15():
    assert (
DT("2015-01-01T11:25:45").dOpt({'year': False}).nat(False).realize()   
    ) == 'Thursday 1/1 11:25:45 a.m.',\
    'Without year'


def test_dates_en_16():
    assert (
DT("2015-01-01T11:25:45").dOpt({'year': False, 'month': False, 'date': False, 'day': False}).nat(False).realize()   
    ) == '11:25:45 a.m.',\
    'Only time'


def test_dates_en_17():
    assert (
DT("2015-01-01T11:25:45").dOpt({'year': False, 'month': False, 'date': False, 'day': False, 'minute': False, 'second': False}).nat(False).realize()   
    ) == '11 a.m.',\
    'Only hour'


def test_dates_en_18():
    assert (
DT("2015-01-01T11:25:45").dOpt({'year': False, 'month': False, 'date': False, 'day': False, 'second': False}).nat(False).realize()   
    ) == '11:25 a.m.',\
    'Only hour and minute'


def test_dates_en_19():
    assert (
DT("2015-01-01T11:25:45").dOpt({'month': False, 'date': False, 'day': False, 'hour': False, 'minute': False, 'second': False}).nat(False).realize()   
    ) == '2015',\
    'Only year'


def test_dates_en_20():
    assert (
DT("2015-01-01T11:25:45").dOpt({'date': False, 'day': False, 'hour': False, 'minute': False, 'second': False}).nat(False).realize()   
    ) == '1/2015',\
    'Only month and year'


def test_dates_en_21():
    assert (
DT("2015-01-01T11:25:45").dOpt({'year': False, 'month': False, 'day': False, 'hour': False, 'minute': False, 'second': False}).nat(False).realize()   
    ) == '1',\
    'Only date'


def test_dates_en_22():
    assert (
DT("2014-12-31 11:25:45").dOpt({'rtime': datetime.datetime(2015, 1, 1, 11, 25, 45), 'hour': False, 'minute': False, 'second': False}).realize()   
    ) == 'yesterday',\
    'one day before'


def test_dates_en_23():
    assert (
DT("2014-12-30 11:25:45").dOpt({'rtime': datetime.datetime(2015, 1, 1, 11, 25, 45), 'hour': False, 'minute': False, 'second': False}).realize()   
    ) == 'last Tuesday',\
    'two days before'


def test_dates_en_24():
    assert (
DT("2014-12-22 11:25:45").dOpt({'rtime': datetime.datetime(2015, 1, 1, 11, 25, 45), 'hour': False, 'minute': False, 'second': False}).realize()   
    ) == '10 days ago',\
    'since 10 days'


def test_dates_en_25():
    assert (
DT("2015-01-01 11:25:45").dOpt({'rtime': datetime.datetime(2015, 1, 1, 11, 25, 45), 'hour': False, 'minute': False, 'second': False}).realize()   
    ) == 'today',\
    'same day'


def test_dates_en_26():
    assert (
DT("2015-01-02 11:25:45").dOpt({'rtime': datetime.datetime(2015, 1, 1, 11, 25, 45), 'hour': False, 'minute': False, 'second': False}).realize()   
    ) == 'tomorrow',\
    'one day after'


def test_dates_en_27():
    assert (
DT("2015-01-05 11:25:45").dOpt({'rtime': datetime.datetime(2015, 1, 1, 11, 25, 45), 'hour': False, 'minute': False, 'second': False}).realize()   
    ) == 'Monday',\
    'four days after'


def test_dates_en_28():
    assert (
DT("2015-01-11 11:25:45").dOpt({'rtime': datetime.datetime(2015, 1, 1, 11, 25, 45), 'hour': False, 'minute': False, 'second': False}).realize()   
    ) == 'in 10 days',\
    '10 days after'

