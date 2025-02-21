import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..','src')))

from pyrealb import *
load("en")

def test_conjugation_en_0():
    assert (
V("admit").t('p').pe(3).realize()   
    ) == 'admits',\
    'admit:p3'


def test_conjugation_en_1():
    assert (
V("admit").t('ps').realize()   
    ) == 'admitted',\
    'admit:ps'


def test_conjugation_en_2():
    assert (
V("admit").t('pp').realize()   
    ) == 'admitted',\
    'admit:pp'


def test_conjugation_en_3():
    assert (
V("admit").t('pr').realize()   
    ) == 'admitting',\
    'admit:pr'


def test_conjugation_en_4():
    assert (
V("arise").t('p').pe(3).realize()   
    ) == 'arises',\
    'arise:p3'


def test_conjugation_en_5():
    assert (
V("arise").t('ps').realize()   
    ) == 'arose',\
    'arise:ps'


def test_conjugation_en_6():
    assert (
V("arise").t('pp').realize()   
    ) == 'arisen',\
    'arise:pp'


def test_conjugation_en_7():
    assert (
V("arise").t('pr').realize()   
    ) == 'arising',\
    'arise:pr'


def test_conjugation_en_8():
    assert (
V("awake").t('p').pe(3).realize()   
    ) == 'awakes',\
    'awake:p3'


def test_conjugation_en_9():
    assert (
V("awake").t('ps').realize()   
    ) == 'awoke',\
    'awake:ps'


def test_conjugation_en_10():
    assert (
V("awake").t('pp').realize()   
    ) == 'awoke',\
    'awake:pp'


def test_conjugation_en_11():
    assert (
V("awake").t('pr').realize()   
    ) == 'awaking',\
    'awake:pr'


def test_conjugation_en_12():
    assert (
V("ban").t('p').pe(3).realize()   
    ) == 'bans',\
    'ban:p3'


def test_conjugation_en_13():
    assert (
V("ban").t('ps').realize()   
    ) == 'banned',\
    'ban:ps'


def test_conjugation_en_14():
    assert (
V("ban").t('pp').realize()   
    ) == 'banned',\
    'ban:pp'


def test_conjugation_en_15():
    assert (
V("ban").t('pr').realize()   
    ) == 'banning',\
    'ban:pr'


def test_conjugation_en_16():
    assert (
V("bar").t('p').pe(3).realize()   
    ) == 'bars',\
    'bar:p3'


def test_conjugation_en_17():
    assert (
V("bar").t('ps').realize()   
    ) == 'barred',\
    'bar:ps'


def test_conjugation_en_18():
    assert (
V("bar").t('pp').realize()   
    ) == 'barred',\
    'bar:pp'


def test_conjugation_en_19():
    assert (
V("bar").t('pr').realize()   
    ) == 'barring',\
    'bar:pr'


def test_conjugation_en_20():
    assert (
V("be").t('pp').realize()   
    ) == 'been',\
    'be:pp'


def test_conjugation_en_21():
    assert (
V("be").t('pr').realize()   
    ) == 'being',\
    'be:pr'


def test_conjugation_en_22():
    assert (
V("bear").t('p').pe(3).realize()   
    ) == 'bears',\
    'bear:p3'


def test_conjugation_en_23():
    assert (
V("bear").t('ps').realize()   
    ) == 'bore',\
    'bear:ps'


def test_conjugation_en_24():
    assert (
V("bear").t('pp').realize()   
    ) == 'borne',\
    'bear:pp'


def test_conjugation_en_25():
    assert (
V("bear").t('pr').realize()   
    ) == 'bearing',\
    'bear:pr'


def test_conjugation_en_26():
    assert (
V("beat").t('p').pe(3).realize()   
    ) == 'beats',\
    'beat:p3'


def test_conjugation_en_27():
    assert (
V("beat").t('ps').realize()   
    ) == 'beat',\
    'beat:ps'


def test_conjugation_en_28():
    assert (
V("beat").t('pp').realize()   
    ) == 'beaten',\
    'beat:pp'


def test_conjugation_en_29():
    assert (
V("beat").t('pr').realize()   
    ) == 'beating',\
    'beat:pr'


def test_conjugation_en_30():
    assert (
V("become").t('p').pe(3).realize()   
    ) == 'becomes',\
    'become:p3'


def test_conjugation_en_31():
    assert (
V("become").t('ps').realize()   
    ) == 'became',\
    'become:ps'


def test_conjugation_en_32():
    assert (
V("become").t('pp').realize()   
    ) == 'become',\
    'become:pp'


def test_conjugation_en_33():
    assert (
V("become").t('pr').realize()   
    ) == 'becoming',\
    'become:pr'


def test_conjugation_en_34():
    assert (
V("beg").t('p').pe(3).realize()   
    ) == 'begs',\
    'beg:p3'


def test_conjugation_en_35():
    assert (
V("beg").t('ps').realize()   
    ) == 'begged',\
    'beg:ps'


def test_conjugation_en_36():
    assert (
V("beg").t('pp').realize()   
    ) == 'begged',\
    'beg:pp'


def test_conjugation_en_37():
    assert (
V("beg").t('pr').realize()   
    ) == 'begging',\
    'beg:pr'


def test_conjugation_en_38():
    assert (
V("begin").t('p').pe(3).realize()   
    ) == 'begins',\
    'begin:p3'


def test_conjugation_en_39():
    assert (
V("begin").t('ps').realize()   
    ) == 'began',\
    'begin:ps'


def test_conjugation_en_40():
    assert (
V("begin").t('pp').realize()   
    ) == 'begun',\
    'begin:pp'


def test_conjugation_en_41():
    assert (
V("begin").t('pr').realize()   
    ) == 'beginning',\
    'begin:pr'


def test_conjugation_en_42():
    assert (
V("bet").t('p').pe(3).realize()   
    ) == 'bets',\
    'bet:p3'


def test_conjugation_en_43():
    assert (
V("bet").t('ps').realize()   
    ) == 'bet',\
    'bet:ps'


def test_conjugation_en_44():
    assert (
V("bet").t('pp').realize()   
    ) == 'bet',\
    'bet:pp'


def test_conjugation_en_45():
    assert (
V("bet").t('pr').realize()   
    ) == 'betting',\
    'bet:pr'


def test_conjugation_en_46():
    assert (
V("bid").t('p').pe(3).realize()   
    ) == 'bids',\
    'bid:p3'


def test_conjugation_en_47():
    assert (
V("bid").t('ps').realize()   
    ) == 'bade',\
    'bid:ps'


def test_conjugation_en_48():
    assert (
V("bid").t('pp').realize()   
    ) == 'bid',\
    'bid:pp'


def test_conjugation_en_49():
    assert (
V("bid").t('pr').realize()   
    ) == 'bidding',\
    'bid:pr'


def test_conjugation_en_50():
    assert (
V("bind").t('p').pe(3).realize()   
    ) == 'binds',\
    'bind:p3'


def test_conjugation_en_51():
    assert (
V("bind").t('ps').realize()   
    ) == 'bound',\
    'bind:ps'


def test_conjugation_en_52():
    assert (
V("bind").t('pp').realize()   
    ) == 'bound',\
    'bind:pp'


def test_conjugation_en_53():
    assert (
V("bind").t('pr').realize()   
    ) == 'binding',\
    'bind:pr'


def test_conjugation_en_54():
    assert (
V("bite").t('p').pe(3).realize()   
    ) == 'bites',\
    'bite:p3'


def test_conjugation_en_55():
    assert (
V("bite").t('ps').realize()   
    ) == 'bit',\
    'bite:ps'


def test_conjugation_en_56():
    assert (
V("bite").t('pp').realize()   
    ) == 'bitten',\
    'bite:pp'


def test_conjugation_en_57():
    assert (
V("bite").t('pr').realize()   
    ) == 'biting',\
    'bite:pr'


def test_conjugation_en_58():
    assert (
V("bleed").t('p').pe(3).realize()   
    ) == 'bleeds',\
    'bleed:p3'


def test_conjugation_en_59():
    assert (
V("bleed").t('ps').realize()   
    ) == 'bled',\
    'bleed:ps'


def test_conjugation_en_60():
    assert (
V("bleed").t('pp').realize()   
    ) == 'bled',\
    'bleed:pp'


def test_conjugation_en_61():
    assert (
V("bleed").t('pr').realize()   
    ) == 'bleeding',\
    'bleed:pr'


def test_conjugation_en_62():
    assert (
V("blow").t('p').pe(3).realize()   
    ) == 'blows',\
    'blow:p3'


def test_conjugation_en_63():
    assert (
V("blow").t('ps').realize()   
    ) == 'blew',\
    'blow:ps'


def test_conjugation_en_64():
    assert (
V("blow").t('pp').realize()   
    ) == 'blown',\
    'blow:pp'


def test_conjugation_en_65():
    assert (
V("blow").t('pr').realize()   
    ) == 'blowing',\
    'blow:pr'


def test_conjugation_en_66():
    assert (
V("break").t('p').pe(3).realize()   
    ) == 'breaks',\
    'break:p3'


def test_conjugation_en_67():
    assert (
V("break").t('ps').realize()   
    ) == 'broke',\
    'break:ps'


def test_conjugation_en_68():
    assert (
V("break").t('pp').realize()   
    ) == 'broken',\
    'break:pp'


def test_conjugation_en_69():
    assert (
V("break").t('pr').realize()   
    ) == 'breaking',\
    'break:pr'


def test_conjugation_en_70():
    assert (
V("breed").t('p').pe(3).realize()   
    ) == 'breeds',\
    'breed:p3'


def test_conjugation_en_71():
    assert (
V("breed").t('ps').realize()   
    ) == 'bred',\
    'breed:ps'


def test_conjugation_en_72():
    assert (
V("breed").t('pp').realize()   
    ) == 'bred',\
    'breed:pp'


def test_conjugation_en_73():
    assert (
V("breed").t('pr').realize()   
    ) == 'breeding',\
    'breed:pr'


def test_conjugation_en_74():
    assert (
V("bring").t('p').pe(3).realize()   
    ) == 'brings',\
    'bring:p3'


def test_conjugation_en_75():
    assert (
V("bring").t('ps').realize()   
    ) == 'brought',\
    'bring:ps'


def test_conjugation_en_76():
    assert (
V("bring").t('pp').realize()   
    ) == 'brought',\
    'bring:pp'


def test_conjugation_en_77():
    assert (
V("bring").t('pr').realize()   
    ) == 'bringing',\
    'bring:pr'


def test_conjugation_en_78():
    assert (
V("build").t('p').pe(3).realize()   
    ) == 'builds',\
    'build:p3'


def test_conjugation_en_79():
    assert (
V("build").t('ps').realize()   
    ) == 'built',\
    'build:ps'


def test_conjugation_en_80():
    assert (
V("build").t('pp').realize()   
    ) == 'built',\
    'build:pp'


def test_conjugation_en_81():
    assert (
V("build").t('pr').realize()   
    ) == 'building',\
    'build:pr'


def test_conjugation_en_82():
    assert (
V("burst").t('p').pe(3).realize()   
    ) == 'bursts',\
    'burst:p3'


def test_conjugation_en_83():
    assert (
V("burst").t('ps').realize()   
    ) == 'burst',\
    'burst:ps'


def test_conjugation_en_84():
    assert (
V("burst").t('pp').realize()   
    ) == 'burst',\
    'burst:pp'


def test_conjugation_en_85():
    assert (
V("burst").t('pr').realize()   
    ) == 'bursting',\
    'burst:pr'


def test_conjugation_en_86():
    assert (
V("buy").t('p').pe(3).realize()   
    ) == 'buys',\
    'buy:p3'


def test_conjugation_en_87():
    assert (
V("buy").t('ps').realize()   
    ) == 'bought',\
    'buy:ps'


def test_conjugation_en_88():
    assert (
V("buy").t('pp').realize()   
    ) == 'bought',\
    'buy:pp'


def test_conjugation_en_89():
    assert (
V("buy").t('pr').realize()   
    ) == 'buying',\
    'buy:pr'


def test_conjugation_en_90():
    assert (
V("can").t('p').pe(3).realize()   
    ) == 'can',\
    'can:p3'


def test_conjugation_en_91():
    assert (
V("can").t('ps').realize()   
    ) == 'could',\
    'can:ps'


def test_conjugation_en_92():
    assert (
V("cast").t('p').pe(3).realize()   
    ) == 'casts',\
    'cast:p3'


def test_conjugation_en_93():
    assert (
V("cast").t('ps').realize()   
    ) == 'cast',\
    'cast:ps'


def test_conjugation_en_94():
    assert (
V("cast").t('pp').realize()   
    ) == 'cast',\
    'cast:pp'


def test_conjugation_en_95():
    assert (
V("cast").t('pr').realize()   
    ) == 'casting',\
    'cast:pr'


def test_conjugation_en_96():
    assert (
V("catch").t('p').pe(3).realize()   
    ) == 'catches',\
    'catch:p3'


def test_conjugation_en_97():
    assert (
V("catch").t('ps').realize()   
    ) == 'caught',\
    'catch:ps'


def test_conjugation_en_98():
    assert (
V("catch").t('pp').realize()   
    ) == 'caught',\
    'catch:pp'


def test_conjugation_en_99():
    assert (
V("catch").t('pr').realize()   
    ) == 'catching',\
    'catch:pr'


def test_conjugation_en_100():
    assert (
V("chat").t('p').pe(3).realize()   
    ) == 'chats',\
    'chat:p3'


def test_conjugation_en_101():
    assert (
V("chat").t('ps').realize()   
    ) == 'chatted',\
    'chat:ps'


def test_conjugation_en_102():
    assert (
V("chat").t('pp').realize()   
    ) == 'chatted',\
    'chat:pp'


def test_conjugation_en_103():
    assert (
V("chat").t('pr').realize()   
    ) == 'chatting',\
    'chat:pr'


def test_conjugation_en_104():
    assert (
V("choose").t('p').pe(3).realize()   
    ) == 'chooses',\
    'choose:p3'


def test_conjugation_en_105():
    assert (
V("choose").t('ps').realize()   
    ) == 'chose',\
    'choose:ps'


def test_conjugation_en_106():
    assert (
V("choose").t('pp').realize()   
    ) == 'chosen',\
    'choose:pp'


def test_conjugation_en_107():
    assert (
V("choose").t('pr').realize()   
    ) == 'choosing',\
    'choose:pr'


def test_conjugation_en_108():
    assert (
V("chop").t('p').pe(3).realize()   
    ) == 'chops',\
    'chop:p3'


def test_conjugation_en_109():
    assert (
V("chop").t('ps').realize()   
    ) == 'chopped',\
    'chop:ps'


def test_conjugation_en_110():
    assert (
V("chop").t('pp').realize()   
    ) == 'chopped',\
    'chop:pp'


def test_conjugation_en_111():
    assert (
V("chop").t('pr').realize()   
    ) == 'chopping',\
    'chop:pr'


def test_conjugation_en_112():
    assert (
V("cling").t('p').pe(3).realize()   
    ) == 'clings',\
    'cling:p3'


def test_conjugation_en_113():
    assert (
V("cling").t('ps').realize()   
    ) == 'clung',\
    'cling:ps'


def test_conjugation_en_114():
    assert (
V("cling").t('pp').realize()   
    ) == 'clung',\
    'cling:pp'


def test_conjugation_en_115():
    assert (
V("cling").t('pr').realize()   
    ) == 'clinging',\
    'cling:pr'


def test_conjugation_en_116():
    assert (
V("come").t('p').pe(3).realize()   
    ) == 'comes',\
    'come:p3'


def test_conjugation_en_117():
    assert (
V("come").t('ps').realize()   
    ) == 'came',\
    'come:ps'


def test_conjugation_en_118():
    assert (
V("come").t('pp').realize()   
    ) == 'come',\
    'come:pp'


def test_conjugation_en_119():
    assert (
V("come").t('pr').realize()   
    ) == 'coming',\
    'come:pr'


def test_conjugation_en_120():
    assert (
V("commit").t('p').pe(3).realize()   
    ) == 'commits',\
    'commit:p3'


def test_conjugation_en_121():
    assert (
V("commit").t('ps').realize()   
    ) == 'committed',\
    'commit:ps'


def test_conjugation_en_122():
    assert (
V("commit").t('pp').realize()   
    ) == 'committed',\
    'commit:pp'


def test_conjugation_en_123():
    assert (
V("commit").t('pr').realize()   
    ) == 'committing',\
    'commit:pr'


def test_conjugation_en_124():
    assert (
V("compel").t('p').pe(3).realize()   
    ) == 'compels',\
    'compel:p3'


def test_conjugation_en_125():
    assert (
V("compel").t('ps').realize()   
    ) == 'compelled',\
    'compel:ps'


def test_conjugation_en_126():
    assert (
V("compel").t('pp').realize()   
    ) == 'compelled',\
    'compel:pp'


def test_conjugation_en_127():
    assert (
V("compel").t('pr').realize()   
    ) == 'compelling',\
    'compel:pr'


def test_conjugation_en_128():
    assert (
V("confer").t('p').pe(3).realize()   
    ) == 'confers',\
    'confer:p3'


def test_conjugation_en_129():
    assert (
V("confer").t('ps').realize()   
    ) == 'conferred',\
    'confer:ps'


def test_conjugation_en_130():
    assert (
V("confer").t('pp').realize()   
    ) == 'conferred',\
    'confer:pp'


def test_conjugation_en_131():
    assert (
V("confer").t('pr').realize()   
    ) == 'conferring',\
    'confer:pr'


def test_conjugation_en_132():
    assert (
V("creep").t('p').pe(3).realize()   
    ) == 'creeps',\
    'creep:p3'


def test_conjugation_en_133():
    assert (
V("creep").t('ps').realize()   
    ) == 'crept',\
    'creep:ps'


def test_conjugation_en_134():
    assert (
V("creep").t('pp').realize()   
    ) == 'crept',\
    'creep:pp'


def test_conjugation_en_135():
    assert (
V("creep").t('pr').realize()   
    ) == 'creeping',\
    'creep:pr'


def test_conjugation_en_136():
    assert (
V("crop").t('p').pe(3).realize()   
    ) == 'crops',\
    'crop:p3'


def test_conjugation_en_137():
    assert (
V("crop").t('ps').realize()   
    ) == 'cropped',\
    'crop:ps'


def test_conjugation_en_138():
    assert (
V("crop").t('pp').realize()   
    ) == 'cropped',\
    'crop:pp'


def test_conjugation_en_139():
    assert (
V("crop").t('pr').realize()   
    ) == 'cropping',\
    'crop:pr'


def test_conjugation_en_140():
    assert (
V("cut").t('p').pe(3).realize()   
    ) == 'cuts',\
    'cut:p3'


def test_conjugation_en_141():
    assert (
V("cut").t('ps').realize()   
    ) == 'cut',\
    'cut:ps'


def test_conjugation_en_142():
    assert (
V("cut").t('pp').realize()   
    ) == 'cut',\
    'cut:pp'


def test_conjugation_en_143():
    assert (
V("cut").t('pr').realize()   
    ) == 'cutting',\
    'cut:pr'


def test_conjugation_en_144():
    assert (
V("deal").t('p').pe(3).realize()   
    ) == 'deals',\
    'deal:p3'


def test_conjugation_en_145():
    assert (
V("deal").t('ps').realize()   
    ) == 'dealt',\
    'deal:ps'


def test_conjugation_en_146():
    assert (
V("deal").t('pp').realize()   
    ) == 'dealt',\
    'deal:pp'


def test_conjugation_en_147():
    assert (
V("deal").t('pr').realize()   
    ) == 'dealing',\
    'deal:pr'


def test_conjugation_en_148():
    assert (
V("deter").t('p').pe(3).realize()   
    ) == 'deters',\
    'deter:p3'


def test_conjugation_en_149():
    assert (
V("deter").t('ps').realize()   
    ) == 'deterred',\
    'deter:ps'


def test_conjugation_en_150():
    assert (
V("deter").t('pp').realize()   
    ) == 'deterred',\
    'deter:pp'


def test_conjugation_en_151():
    assert (
V("deter").t('pr').realize()   
    ) == 'deterring',\
    'deter:pr'


def test_conjugation_en_152():
    assert (
V("dig").t('p').pe(3).realize()   
    ) == 'digs',\
    'dig:p3'


def test_conjugation_en_153():
    assert (
V("dig").t('ps').realize()   
    ) == 'dug',\
    'dig:ps'


def test_conjugation_en_154():
    assert (
V("dig").t('pp').realize()   
    ) == 'dug',\
    'dig:pp'


def test_conjugation_en_155():
    assert (
V("dig").t('pr').realize()   
    ) == 'digging',\
    'dig:pr'


def test_conjugation_en_156():
    assert (
V("dip").t('p').pe(3).realize()   
    ) == 'dips',\
    'dip:p3'


def test_conjugation_en_157():
    assert (
V("dip").t('ps').realize()   
    ) == 'dipped',\
    'dip:ps'


def test_conjugation_en_158():
    assert (
V("dip").t('pp').realize()   
    ) == 'dipped',\
    'dip:pp'


def test_conjugation_en_159():
    assert (
V("dip").t('pr').realize()   
    ) == 'dipping',\
    'dip:pr'


def test_conjugation_en_160():
    assert (
V("do").t('p').pe(3).realize()   
    ) == 'does',\
    'do:p3'


def test_conjugation_en_161():
    assert (
V("do").t('ps').realize()   
    ) == 'did',\
    'do:ps'


def test_conjugation_en_162():
    assert (
V("do").t('pp').realize()   
    ) == 'done',\
    'do:pp'


def test_conjugation_en_163():
    assert (
V("do").t('pr').realize()   
    ) == 'doing',\
    'do:pr'


def test_conjugation_en_164():
    assert (
V("drag").t('p').pe(3).realize()   
    ) == 'drags',\
    'drag:p3'


def test_conjugation_en_165():
    assert (
V("drag").t('ps').realize()   
    ) == 'dragged',\
    'drag:ps'


def test_conjugation_en_166():
    assert (
V("drag").t('pp').realize()   
    ) == 'dragged',\
    'drag:pp'


def test_conjugation_en_167():
    assert (
V("drag").t('pr').realize()   
    ) == 'dragging',\
    'drag:pr'


def test_conjugation_en_168():
    assert (
V("draw").t('p').pe(3).realize()   
    ) == 'draws',\
    'draw:p3'


def test_conjugation_en_169():
    assert (
V("draw").t('ps').realize()   
    ) == 'drew',\
    'draw:ps'


def test_conjugation_en_170():
    assert (
V("draw").t('pp').realize()   
    ) == 'drawn',\
    'draw:pp'


def test_conjugation_en_171():
    assert (
V("draw").t('pr').realize()   
    ) == 'drawing',\
    'draw:pr'


def test_conjugation_en_172():
    assert (
V("drink").t('p').pe(3).realize()   
    ) == 'drinks',\
    'drink:p3'


def test_conjugation_en_173():
    assert (
V("drink").t('ps').realize()   
    ) == 'drank',\
    'drink:ps'


def test_conjugation_en_174():
    assert (
V("drink").t('pp').realize()   
    ) == 'drunk',\
    'drink:pp'


def test_conjugation_en_175():
    assert (
V("drink").t('pr').realize()   
    ) == 'drinking',\
    'drink:pr'


def test_conjugation_en_176():
    assert (
V("drive").t('p').pe(3).realize()   
    ) == 'drives',\
    'drive:p3'


def test_conjugation_en_177():
    assert (
V("drive").t('ps').realize()   
    ) == 'drove',\
    'drive:ps'


def test_conjugation_en_178():
    assert (
V("drive").t('pp').realize()   
    ) == 'driven',\
    'drive:pp'


def test_conjugation_en_179():
    assert (
V("drive").t('pr').realize()   
    ) == 'driving',\
    'drive:pr'


def test_conjugation_en_180():
    assert (
V("drop").t('p').pe(3).realize()   
    ) == 'drops',\
    'drop:p3'


def test_conjugation_en_181():
    assert (
V("drop").t('ps').realize()   
    ) == 'dropped',\
    'drop:ps'


def test_conjugation_en_182():
    assert (
V("drop").t('pp').realize()   
    ) == 'dropped',\
    'drop:pp'


def test_conjugation_en_183():
    assert (
V("drop").t('pr').realize()   
    ) == 'dropping',\
    'drop:pr'


def test_conjugation_en_184():
    assert (
V("drug").t('p').pe(3).realize()   
    ) == 'drugs',\
    'drug:p3'


def test_conjugation_en_185():
    assert (
V("drug").t('ps').realize()   
    ) == 'drugged',\
    'drug:ps'


def test_conjugation_en_186():
    assert (
V("drug").t('pp').realize()   
    ) == 'drugged',\
    'drug:pp'


def test_conjugation_en_187():
    assert (
V("drug").t('pr').realize()   
    ) == 'drugging',\
    'drug:pr'


def test_conjugation_en_188():
    assert (
V("eat").t('p').pe(3).realize()   
    ) == 'eats',\
    'eat:p3'


def test_conjugation_en_189():
    assert (
V("eat").t('ps').realize()   
    ) == 'ate',\
    'eat:ps'


def test_conjugation_en_190():
    assert (
V("eat").t('pp').realize()   
    ) == 'eaten',\
    'eat:pp'


def test_conjugation_en_191():
    assert (
V("eat").t('pr').realize()   
    ) == 'eating',\
    'eat:pr'


def test_conjugation_en_192():
    assert (
V("echo").t('p').pe(3).realize()   
    ) == 'echoes',\
    'echo:p3'


def test_conjugation_en_193():
    assert (
V("echo").t('ps').realize()   
    ) == 'echoed',\
    'echo:ps'


def test_conjugation_en_194():
    assert (
V("echo").t('pp').realize()   
    ) == 'echoed',\
    'echo:pp'


def test_conjugation_en_195():
    assert (
V("echo").t('pr').realize()   
    ) == 'echoing',\
    'echo:pr'


def test_conjugation_en_196():
    assert (
V("equip").t('p').pe(3).realize()   
    ) == 'equips',\
    'equip:p3'


def test_conjugation_en_197():
    assert (
V("equip").t('ps').realize()   
    ) == 'equipped',\
    'equip:ps'


def test_conjugation_en_198():
    assert (
V("equip").t('pp').realize()   
    ) == 'equipped',\
    'equip:pp'


def test_conjugation_en_199():
    assert (
V("equip").t('pr').realize()   
    ) == 'equipping',\
    'equip:pr'


def test_conjugation_en_200():
    assert (
V("expel").t('p').pe(3).realize()   
    ) == 'expels',\
    'expel:p3'


def test_conjugation_en_201():
    assert (
V("expel").t('ps').realize()   
    ) == 'expelled',\
    'expel:ps'


def test_conjugation_en_202():
    assert (
V("expel").t('pp').realize()   
    ) == 'expelled',\
    'expel:pp'


def test_conjugation_en_203():
    assert (
V("expel").t('pr').realize()   
    ) == 'expelling',\
    'expel:pr'


def test_conjugation_en_204():
    assert (
V("fall").t('p').pe(3).realize()   
    ) == 'falls',\
    'fall:p3'


def test_conjugation_en_205():
    assert (
V("fall").t('ps').realize()   
    ) == 'fell',\
    'fall:ps'


def test_conjugation_en_206():
    assert (
V("fall").t('pp').realize()   
    ) == 'fallen',\
    'fall:pp'


def test_conjugation_en_207():
    assert (
V("fall").t('pr').realize()   
    ) == 'falling',\
    'fall:pr'


def test_conjugation_en_208():
    assert (
V("fan").t('p').pe(3).realize()   
    ) == 'fans',\
    'fan:p3'


def test_conjugation_en_209():
    assert (
V("fan").t('ps').realize()   
    ) == 'fanned',\
    'fan:ps'


def test_conjugation_en_210():
    assert (
V("fan").t('pp').realize()   
    ) == 'fanned',\
    'fan:pp'


def test_conjugation_en_211():
    assert (
V("fan").t('pr').realize()   
    ) == 'fanning',\
    'fan:pr'


def test_conjugation_en_212():
    assert (
V("feed").t('p').pe(3).realize()   
    ) == 'feeds',\
    'feed:p3'


def test_conjugation_en_213():
    assert (
V("feed").t('ps').realize()   
    ) == 'fed',\
    'feed:ps'


def test_conjugation_en_214():
    assert (
V("feed").t('pp').realize()   
    ) == 'fed',\
    'feed:pp'


def test_conjugation_en_215():
    assert (
V("feed").t('pr').realize()   
    ) == 'feeding',\
    'feed:pr'


def test_conjugation_en_216():
    assert (
V("feel").t('p').pe(3).realize()   
    ) == 'feels',\
    'feel:p3'


def test_conjugation_en_217():
    assert (
V("feel").t('ps').realize()   
    ) == 'felt',\
    'feel:ps'


def test_conjugation_en_218():
    assert (
V("feel").t('pp').realize()   
    ) == 'felt',\
    'feel:pp'


def test_conjugation_en_219():
    assert (
V("feel").t('pr').realize()   
    ) == 'feeling',\
    'feel:pr'


def test_conjugation_en_220():
    assert (
V("fight").t('p').pe(3).realize()   
    ) == 'fights',\
    'fight:p3'


def test_conjugation_en_221():
    assert (
V("fight").t('ps').realize()   
    ) == 'fought',\
    'fight:ps'


def test_conjugation_en_222():
    assert (
V("fight").t('pp').realize()   
    ) == 'fought',\
    'fight:pp'


def test_conjugation_en_223():
    assert (
V("fight").t('pr').realize()   
    ) == 'fighting',\
    'fight:pr'


def test_conjugation_en_224():
    assert (
V("find").t('p').pe(3).realize()   
    ) == 'finds',\
    'find:p3'


def test_conjugation_en_225():
    assert (
V("find").t('ps').realize()   
    ) == 'found',\
    'find:ps'


def test_conjugation_en_226():
    assert (
V("find").t('pp').realize()   
    ) == 'found',\
    'find:pp'


def test_conjugation_en_227():
    assert (
V("find").t('pr').realize()   
    ) == 'finding',\
    'find:pr'


def test_conjugation_en_228():
    assert (
V("fit").t('p').pe(3).realize()   
    ) == 'fits',\
    'fit:p3'


def test_conjugation_en_229():
    assert (
V("fit").t('ps').realize()   
    ) == 'fitted',\
    'fit:ps'


def test_conjugation_en_230():
    assert (
V("fit").t('pp').realize()   
    ) == 'fitted',\
    'fit:pp'


def test_conjugation_en_231():
    assert (
V("fit").t('pr').realize()   
    ) == 'fitting',\
    'fit:pr'


def test_conjugation_en_232():
    assert (
V("flee").t('p').pe(3).realize()   
    ) == 'flees',\
    'flee:p3'


def test_conjugation_en_233():
    assert (
V("flee").t('ps').realize()   
    ) == 'fled',\
    'flee:ps'


def test_conjugation_en_234():
    assert (
V("flee").t('pp').realize()   
    ) == 'fled',\
    'flee:pp'


def test_conjugation_en_235():
    assert (
V("flee").t('pr').realize()   
    ) == 'fleeing',\
    'flee:pr'


def test_conjugation_en_236():
    assert (
V("fling").t('p').pe(3).realize()   
    ) == 'flings',\
    'fling:p3'


def test_conjugation_en_237():
    assert (
V("fling").t('ps').realize()   
    ) == 'flung',\
    'fling:ps'


def test_conjugation_en_238():
    assert (
V("fling").t('pp').realize()   
    ) == 'flung',\
    'fling:pp'


def test_conjugation_en_239():
    assert (
V("fling").t('pr').realize()   
    ) == 'flinging',\
    'fling:pr'


def test_conjugation_en_240():
    assert (
V("fly").t('p').pe(3).realize()   
    ) == 'flies',\
    'fly:p3'


def test_conjugation_en_241():
    assert (
V("fly").t('ps').realize()   
    ) == 'flew',\
    'fly:ps'


def test_conjugation_en_242():
    assert (
V("fly").t('pp').realize()   
    ) == 'flown',\
    'fly:pp'


def test_conjugation_en_243():
    assert (
V("fly").t('pr').realize()   
    ) == 'flying',\
    'fly:pr'


def test_conjugation_en_244():
    assert (
V("forbid").t('p').pe(3).realize()   
    ) == 'forbids',\
    'forbid:p3'


def test_conjugation_en_245():
    assert (
V("forbid").t('ps').realize()   
    ) == 'forbad',\
    'forbid:ps'


def test_conjugation_en_246():
    assert (
V("forbid").t('pp').realize()   
    ) == 'forbidden',\
    'forbid:pp'


def test_conjugation_en_247():
    assert (
V("forbid").t('pr').realize()   
    ) == 'forbidding',\
    'forbid:pr'


def test_conjugation_en_248():
    assert (
V("forget").t('p').pe(3).realize()   
    ) == 'forgets',\
    'forget:p3'


def test_conjugation_en_249():
    assert (
V("forget").t('ps').realize()   
    ) == 'forgot',\
    'forget:ps'


def test_conjugation_en_250():
    assert (
V("forget").t('pp').realize()   
    ) == 'forgotten',\
    'forget:pp'


def test_conjugation_en_251():
    assert (
V("forget").t('pr').realize()   
    ) == 'forgetting',\
    'forget:pr'


def test_conjugation_en_252():
    assert (
V("forgive").t('p').pe(3).realize()   
    ) == 'forgives',\
    'forgive:p3'


def test_conjugation_en_253():
    assert (
V("forgive").t('ps').realize()   
    ) == 'forgave',\
    'forgive:ps'


def test_conjugation_en_254():
    assert (
V("forgive").t('pp').realize()   
    ) == 'forgiven',\
    'forgive:pp'


def test_conjugation_en_255():
    assert (
V("forgive").t('pr').realize()   
    ) == 'forgiving',\
    'forgive:pr'


def test_conjugation_en_256():
    assert (
V("free").t('p').pe(3).realize()   
    ) == 'frees',\
    'free:p3'


def test_conjugation_en_257():
    assert (
V("free").t('ps').realize()   
    ) == 'freed',\
    'free:ps'


def test_conjugation_en_258():
    assert (
V("free").t('pp').realize()   
    ) == 'freed',\
    'free:pp'


def test_conjugation_en_259():
    assert (
V("free").t('pr').realize()   
    ) == 'freeing',\
    'free:pr'


def test_conjugation_en_260():
    assert (
V("freeze").t('p').pe(3).realize()   
    ) == 'freezes',\
    'freeze:p3'


def test_conjugation_en_261():
    assert (
V("freeze").t('ps').realize()   
    ) == 'froze',\
    'freeze:ps'


def test_conjugation_en_262():
    assert (
V("freeze").t('pp').realize()   
    ) == 'frozen',\
    'freeze:pp'


def test_conjugation_en_263():
    assert (
V("freeze").t('pr').realize()   
    ) == 'freezing',\
    'freeze:pr'


def test_conjugation_en_264():
    assert (
V("fulfill").t('p').pe(3).realize()   
    ) == 'fulfils',\
    'fulfill:p3'


def test_conjugation_en_265():
    assert (
V("fulfill").t('ps').realize()   
    ) == 'fulfilled',\
    'fulfill:ps'


def test_conjugation_en_266():
    assert (
V("fulfill").t('pp').realize()   
    ) == 'fulfilled',\
    'fulfill:pp'


def test_conjugation_en_267():
    assert (
V("fulfill").t('pr').realize()   
    ) == 'fulfilling',\
    'fulfill:pr'


def test_conjugation_en_268():
    assert (
V("get").t('p').pe(3).realize()   
    ) == 'gets',\
    'get:p3'


def test_conjugation_en_269():
    assert (
V("get").t('ps').realize()   
    ) == 'got',\
    'get:ps'


def test_conjugation_en_270():
    assert (
V("get").t('pp').realize()   
    ) == 'gotten',\
    'get:pp'


def test_conjugation_en_271():
    assert (
V("get").t('pr').realize()   
    ) == 'getting',\
    'get:pr'


def test_conjugation_en_272():
    assert (
V("give").t('p').pe(3).realize()   
    ) == 'gives',\
    'give:p3'


def test_conjugation_en_273():
    assert (
V("give").t('ps').realize()   
    ) == 'gave',\
    'give:ps'


def test_conjugation_en_274():
    assert (
V("give").t('pp').realize()   
    ) == 'given',\
    'give:pp'


def test_conjugation_en_275():
    assert (
V("give").t('pr').realize()   
    ) == 'giving',\
    'give:pr'


def test_conjugation_en_276():
    assert (
V("go").t('p').pe(3).realize()   
    ) == 'goes',\
    'go:p3'


def test_conjugation_en_277():
    assert (
V("go").t('ps').realize()   
    ) == 'went',\
    'go:ps'


def test_conjugation_en_278():
    assert (
V("go").t('pp').realize()   
    ) == 'gone',\
    'go:pp'


def test_conjugation_en_279():
    assert (
V("go").t('pr').realize()   
    ) == 'going',\
    'go:pr'


def test_conjugation_en_280():
    assert (
V("grab").t('p').pe(3).realize()   
    ) == 'grabs',\
    'grab:p3'


def test_conjugation_en_281():
    assert (
V("grab").t('ps').realize()   
    ) == 'grabbed',\
    'grab:ps'


def test_conjugation_en_282():
    assert (
V("grab").t('pp').realize()   
    ) == 'grabbed',\
    'grab:pp'


def test_conjugation_en_283():
    assert (
V("grab").t('pr').realize()   
    ) == 'grabbing',\
    'grab:pr'


def test_conjugation_en_284():
    assert (
V("grin").t('p').pe(3).realize()   
    ) == 'grins',\
    'grin:p3'


def test_conjugation_en_285():
    assert (
V("grin").t('ps').realize()   
    ) == 'grinned',\
    'grin:ps'


def test_conjugation_en_286():
    assert (
V("grin").t('pp').realize()   
    ) == 'grinned',\
    'grin:pp'


def test_conjugation_en_287():
    assert (
V("grin").t('pr').realize()   
    ) == 'grinning',\
    'grin:pr'


def test_conjugation_en_288():
    assert (
V("grind").t('p').pe(3).realize()   
    ) == 'grinds',\
    'grind:p3'


def test_conjugation_en_289():
    assert (
V("grind").t('ps').realize()   
    ) == 'ground',\
    'grind:ps'


def test_conjugation_en_290():
    assert (
V("grind").t('pp').realize()   
    ) == 'ground',\
    'grind:pp'


def test_conjugation_en_291():
    assert (
V("grind").t('pr').realize()   
    ) == 'grinding',\
    'grind:pr'


def test_conjugation_en_292():
    assert (
V("grip").t('p').pe(3).realize()   
    ) == 'grips',\
    'grip:p3'


def test_conjugation_en_293():
    assert (
V("grip").t('ps').realize()   
    ) == 'gripped',\
    'grip:ps'


def test_conjugation_en_294():
    assert (
V("grip").t('pp').realize()   
    ) == 'gripped',\
    'grip:pp'


def test_conjugation_en_295():
    assert (
V("grip").t('pr').realize()   
    ) == 'gripping',\
    'grip:pr'


def test_conjugation_en_296():
    assert (
V("grow").t('p').pe(3).realize()   
    ) == 'grows',\
    'grow:p3'


def test_conjugation_en_297():
    assert (
V("grow").t('ps').realize()   
    ) == 'grew',\
    'grow:ps'


def test_conjugation_en_298():
    assert (
V("grow").t('pp').realize()   
    ) == 'grown',\
    'grow:pp'


def test_conjugation_en_299():
    assert (
V("grow").t('pr').realize()   
    ) == 'growing',\
    'grow:pr'


def test_conjugation_en_300():
    assert (
V("handicap").t('p').pe(3).realize()   
    ) == 'handicaps',\
    'handicap:p3'


def test_conjugation_en_301():
    assert (
V("handicap").t('ps').realize()   
    ) == 'handicapped',\
    'handicap:ps'


def test_conjugation_en_302():
    assert (
V("handicap").t('pp').realize()   
    ) == 'handicapped',\
    'handicap:pp'


def test_conjugation_en_303():
    assert (
V("handicap").t('pr').realize()   
    ) == 'handicapping',\
    'handicap:pr'


def test_conjugation_en_304():
    assert (
V("have").t('p').pe(3).realize()   
    ) == 'has',\
    'have:p3'


def test_conjugation_en_305():
    assert (
V("have").t('ps').realize()   
    ) == 'had',\
    'have:ps'


def test_conjugation_en_306():
    assert (
V("have").t('pp').realize()   
    ) == 'had',\
    'have:pp'


def test_conjugation_en_307():
    assert (
V("have").t('pr').realize()   
    ) == 'having',\
    'have:pr'


def test_conjugation_en_308():
    assert (
V("hear").t('p').pe(3).realize()   
    ) == 'hears',\
    'hear:p3'


def test_conjugation_en_309():
    assert (
V("hear").t('ps').realize()   
    ) == 'heard',\
    'hear:ps'


def test_conjugation_en_310():
    assert (
V("hear").t('pp').realize()   
    ) == 'heard',\
    'hear:pp'


def test_conjugation_en_311():
    assert (
V("hear").t('pr').realize()   
    ) == 'hearing',\
    'hear:pr'


def test_conjugation_en_312():
    assert (
V("hide").t('p').pe(3).realize()   
    ) == 'hides',\
    'hide:p3'


def test_conjugation_en_313():
    assert (
V("hide").t('ps').realize()   
    ) == 'hid',\
    'hide:ps'


def test_conjugation_en_314():
    assert (
V("hide").t('pp').realize()   
    ) == 'hidden',\
    'hide:pp'


def test_conjugation_en_315():
    assert (
V("hide").t('pr').realize()   
    ) == 'hiding',\
    'hide:pr'


def test_conjugation_en_316():
    assert (
V("hit").t('p').pe(3).realize()   
    ) == 'hits',\
    'hit:p3'


def test_conjugation_en_317():
    assert (
V("hit").t('ps').realize()   
    ) == 'hit',\
    'hit:ps'


def test_conjugation_en_318():
    assert (
V("hit").t('pp').realize()   
    ) == 'hit',\
    'hit:pp'


def test_conjugation_en_319():
    assert (
V("hit").t('pr').realize()   
    ) == 'hitting',\
    'hit:pr'


def test_conjugation_en_320():
    assert (
V("hold").t('p').pe(3).realize()   
    ) == 'holds',\
    'hold:p3'


def test_conjugation_en_321():
    assert (
V("hold").t('ps').realize()   
    ) == 'held',\
    'hold:ps'


def test_conjugation_en_322():
    assert (
V("hold").t('pp').realize()   
    ) == 'held',\
    'hold:pp'


def test_conjugation_en_323():
    assert (
V("hold").t('pr').realize()   
    ) == 'holding',\
    'hold:pr'


def test_conjugation_en_324():
    assert (
V("hug").t('p').pe(3).realize()   
    ) == 'hugs',\
    'hug:p3'


def test_conjugation_en_325():
    assert (
V("hug").t('ps').realize()   
    ) == 'hugged',\
    'hug:ps'


def test_conjugation_en_326():
    assert (
V("hug").t('pp').realize()   
    ) == 'hugged',\
    'hug:pp'


def test_conjugation_en_327():
    assert (
V("hug").t('pr').realize()   
    ) == 'hugging',\
    'hug:pr'


def test_conjugation_en_328():
    assert (
V("hurt").t('p').pe(3).realize()   
    ) == 'hurts',\
    'hurt:p3'


def test_conjugation_en_329():
    assert (
V("hurt").t('ps').realize()   
    ) == 'hurt',\
    'hurt:ps'


def test_conjugation_en_330():
    assert (
V("hurt").t('pp').realize()   
    ) == 'hurt',\
    'hurt:pp'


def test_conjugation_en_331():
    assert (
V("hurt").t('pr').realize()   
    ) == 'hurting',\
    'hurt:pr'


def test_conjugation_en_332():
    assert (
V("incur").t('p').pe(3).realize()   
    ) == 'incurs',\
    'incur:p3'


def test_conjugation_en_333():
    assert (
V("incur").t('ps').realize()   
    ) == 'incurred',\
    'incur:ps'


def test_conjugation_en_334():
    assert (
V("incur").t('pp').realize()   
    ) == 'incurred',\
    'incur:pp'


def test_conjugation_en_335():
    assert (
V("incur").t('pr').realize()   
    ) == 'incurring',\
    'incur:pr'


def test_conjugation_en_336():
    assert (
V("install").t('p').pe(3).realize()   
    ) == 'installs',\
    'install:p3'


def test_conjugation_en_337():
    assert (
V("install").t('ps').realize()   
    ) == 'installed',\
    'install:ps'


def test_conjugation_en_338():
    assert (
V("install").t('pp').realize()   
    ) == 'installed',\
    'install:pp'


def test_conjugation_en_339():
    assert (
V("install").t('pr').realize()   
    ) == 'installing',\
    'install:pr'


def test_conjugation_en_340():
    assert (
V("keep").t('p').pe(3).realize()   
    ) == 'keeps',\
    'keep:p3'


def test_conjugation_en_341():
    assert (
V("keep").t('ps').realize()   
    ) == 'kept',\
    'keep:ps'


def test_conjugation_en_342():
    assert (
V("keep").t('pp').realize()   
    ) == 'kept',\
    'keep:pp'


def test_conjugation_en_343():
    assert (
V("keep").t('pr').realize()   
    ) == 'keeping',\
    'keep:pr'


def test_conjugation_en_344():
    assert (
V("knit").t('p').pe(3).realize()   
    ) == 'knits',\
    'knit:p3'


def test_conjugation_en_345():
    assert (
V("knit").t('ps').realize()   
    ) == 'knit',\
    'knit:ps'


def test_conjugation_en_346():
    assert (
V("knit").t('pp').realize()   
    ) == 'knit',\
    'knit:pp'


def test_conjugation_en_347():
    assert (
V("knit").t('pr').realize()   
    ) == 'knitting',\
    'knit:pr'


def test_conjugation_en_348():
    assert (
V("know").t('p').pe(3).realize()   
    ) == 'knows',\
    'know:p3'


def test_conjugation_en_349():
    assert (
V("know").t('ps').realize()   
    ) == 'knew',\
    'know:ps'


def test_conjugation_en_350():
    assert (
V("know").t('pp').realize()   
    ) == 'known',\
    'know:pp'


def test_conjugation_en_351():
    assert (
V("know").t('pr').realize()   
    ) == 'knowing',\
    'know:pr'


def test_conjugation_en_352():
    assert (
V("lay").t('p').pe(3).realize()   
    ) == 'lays',\
    'lay:p3'


def test_conjugation_en_353():
    assert (
V("lay").t('ps').realize()   
    ) == 'laid',\
    'lay:ps'


def test_conjugation_en_354():
    assert (
V("lay").t('pp').realize()   
    ) == 'laid',\
    'lay:pp'


def test_conjugation_en_355():
    assert (
V("lay").t('pr').realize()   
    ) == 'laying',\
    'lay:pr'


def test_conjugation_en_356():
    assert (
V("lead").t('p').pe(3).realize()   
    ) == 'leads',\
    'lead:p3'


def test_conjugation_en_357():
    assert (
V("lead").t('ps').realize()   
    ) == 'led',\
    'lead:ps'


def test_conjugation_en_358():
    assert (
V("lead").t('pp').realize()   
    ) == 'led',\
    'lead:pp'


def test_conjugation_en_359():
    assert (
V("lead").t('pr').realize()   
    ) == 'leading',\
    'lead:pr'


def test_conjugation_en_360():
    assert (
V("leave").t('p').pe(3).realize()   
    ) == 'leaves',\
    'leave:p3'


def test_conjugation_en_361():
    assert (
V("leave").t('ps').realize()   
    ) == 'left',\
    'leave:ps'


def test_conjugation_en_362():
    assert (
V("leave").t('pp').realize()   
    ) == 'left',\
    'leave:pp'


def test_conjugation_en_363():
    assert (
V("leave").t('pr').realize()   
    ) == 'leaving',\
    'leave:pr'


def test_conjugation_en_364():
    assert (
V("lend").t('p').pe(3).realize()   
    ) == 'lends',\
    'lend:p3'


def test_conjugation_en_365():
    assert (
V("lend").t('ps').realize()   
    ) == 'lent',\
    'lend:ps'


def test_conjugation_en_366():
    assert (
V("lend").t('pp').realize()   
    ) == 'lent',\
    'lend:pp'


def test_conjugation_en_367():
    assert (
V("lend").t('pr').realize()   
    ) == 'lending',\
    'lend:pr'


def test_conjugation_en_368():
    assert (
V("let").t('p').pe(3).realize()   
    ) == 'lets',\
    'let:p3'


def test_conjugation_en_369():
    assert (
V("let").t('ps').realize()   
    ) == 'let',\
    'let:ps'


def test_conjugation_en_370():
    assert (
V("let").t('pp').realize()   
    ) == 'let',\
    'let:pp'


def test_conjugation_en_371():
    assert (
V("let").t('pr').realize()   
    ) == 'letting',\
    'let:pr'


def test_conjugation_en_372():
    assert (
V("lose").t('p').pe(3).realize()   
    ) == 'loses',\
    'lose:p3'


def test_conjugation_en_373():
    assert (
V("lose").t('ps').realize()   
    ) == 'lost',\
    'lose:ps'


def test_conjugation_en_374():
    assert (
V("lose").t('pp').realize()   
    ) == 'lost',\
    'lose:pp'


def test_conjugation_en_375():
    assert (
V("lose").t('pr').realize()   
    ) == 'losing',\
    'lose:pr'


def test_conjugation_en_376():
    assert (
V("make").t('p').pe(3).realize()   
    ) == 'makes',\
    'make:p3'


def test_conjugation_en_377():
    assert (
V("make").t('ps').realize()   
    ) == 'made',\
    'make:ps'


def test_conjugation_en_378():
    assert (
V("make").t('pp').realize()   
    ) == 'made',\
    'make:pp'


def test_conjugation_en_379():
    assert (
V("make").t('pr').realize()   
    ) == 'making',\
    'make:pr'


def test_conjugation_en_380():
    assert (
V("map").t('p').pe(3).realize()   
    ) == 'maps',\
    'map:p3'


def test_conjugation_en_381():
    assert (
V("map").t('ps').realize()   
    ) == 'mapped',\
    'map:ps'


def test_conjugation_en_382():
    assert (
V("map").t('pp').realize()   
    ) == 'mapped',\
    'map:pp'


def test_conjugation_en_383():
    assert (
V("map").t('pr').realize()   
    ) == 'mapping',\
    'map:pr'


def test_conjugation_en_384():
    assert (
V("mean").t('p').pe(3).realize()   
    ) == 'means',\
    'mean:p3'


def test_conjugation_en_385():
    assert (
V("mean").t('ps').realize()   
    ) == 'meant',\
    'mean:ps'


def test_conjugation_en_386():
    assert (
V("mean").t('pp').realize()   
    ) == 'meant',\
    'mean:pp'


def test_conjugation_en_387():
    assert (
V("mean").t('pr').realize()   
    ) == 'meaning',\
    'mean:pr'


def test_conjugation_en_388():
    assert (
V("meet").t('p').pe(3).realize()   
    ) == 'meets',\
    'meet:p3'


def test_conjugation_en_389():
    assert (
V("meet").t('ps').realize()   
    ) == 'met',\
    'meet:ps'


def test_conjugation_en_390():
    assert (
V("meet").t('pp').realize()   
    ) == 'met',\
    'meet:pp'


def test_conjugation_en_391():
    assert (
V("meet").t('pr').realize()   
    ) == 'meeting',\
    'meet:pr'


def test_conjugation_en_392():
    assert (
V("mistake").t('p').pe(3).realize()   
    ) == 'mistakes',\
    'mistake:p3'


def test_conjugation_en_393():
    assert (
V("mistake").t('ps').realize()   
    ) == 'mistook',\
    'mistake:ps'


def test_conjugation_en_394():
    assert (
V("mistake").t('pp').realize()   
    ) == 'mistaken',\
    'mistake:pp'


def test_conjugation_en_395():
    assert (
V("mistake").t('pr').realize()   
    ) == 'mistaking',\
    'mistake:pr'


def test_conjugation_en_396():
    assert (
V("nod").t('p').pe(3).realize()   
    ) == 'nods',\
    'nod:p3'


def test_conjugation_en_397():
    assert (
V("nod").t('ps').realize()   
    ) == 'nodded',\
    'nod:ps'


def test_conjugation_en_398():
    assert (
V("nod").t('pp').realize()   
    ) == 'nodded',\
    'nod:pp'


def test_conjugation_en_399():
    assert (
V("nod").t('pr').realize()   
    ) == 'nodding',\
    'nod:pr'


def test_conjugation_en_400():
    assert (
V("offset").t('p').pe(3).realize()   
    ) == 'offsets',\
    'offset:p3'


def test_conjugation_en_401():
    assert (
V("offset").t('ps').realize()   
    ) == 'offset',\
    'offset:ps'


def test_conjugation_en_402():
    assert (
V("offset").t('pp').realize()   
    ) == 'offset',\
    'offset:pp'


def test_conjugation_en_403():
    assert (
V("offset").t('pr').realize()   
    ) == 'offsetting',\
    'offset:pr'


def test_conjugation_en_404():
    assert (
V("omit").t('p').pe(3).realize()   
    ) == 'omits',\
    'omit:p3'


def test_conjugation_en_405():
    assert (
V("omit").t('ps').realize()   
    ) == 'omitted',\
    'omit:ps'


def test_conjugation_en_406():
    assert (
V("omit").t('pp').realize()   
    ) == 'omitted',\
    'omit:pp'


def test_conjugation_en_407():
    assert (
V("omit").t('pr').realize()   
    ) == 'omitting',\
    'omit:pr'


def test_conjugation_en_408():
    assert (
V("overcome").t('p').pe(3).realize()   
    ) == 'overcomes',\
    'overcome:p3'


def test_conjugation_en_409():
    assert (
V("overcome").t('ps').realize()   
    ) == 'overcame',\
    'overcome:ps'


def test_conjugation_en_410():
    assert (
V("overcome").t('pp').realize()   
    ) == 'overcome',\
    'overcome:pp'


def test_conjugation_en_411():
    assert (
V("overcome").t('pr').realize()   
    ) == 'overcoming',\
    'overcome:pr'


def test_conjugation_en_412():
    assert (
V("overtake").t('p').pe(3).realize()   
    ) == 'overtakes',\
    'overtake:p3'


def test_conjugation_en_413():
    assert (
V("overtake").t('ps').realize()   
    ) == 'overtook',\
    'overtake:ps'


def test_conjugation_en_414():
    assert (
V("overtake").t('pp').realize()   
    ) == 'overtaken',\
    'overtake:pp'


def test_conjugation_en_415():
    assert (
V("overtake").t('pr').realize()   
    ) == 'overtaking',\
    'overtake:pr'


def test_conjugation_en_416():
    assert (
V("pat").t('p').pe(3).realize()   
    ) == 'pats',\
    'pat:p3'


def test_conjugation_en_417():
    assert (
V("pat").t('ps').realize()   
    ) == 'patted',\
    'pat:ps'


def test_conjugation_en_418():
    assert (
V("pat").t('pp').realize()   
    ) == 'patted',\
    'pat:pp'


def test_conjugation_en_419():
    assert (
V("pat").t('pr').realize()   
    ) == 'patting',\
    'pat:pr'


def test_conjugation_en_420():
    assert (
V("permit").t('p').pe(3).realize()   
    ) == 'permits',\
    'permit:p3'


def test_conjugation_en_421():
    assert (
V("permit").t('ps').realize()   
    ) == 'permitted',\
    'permit:ps'


def test_conjugation_en_422():
    assert (
V("permit").t('pp').realize()   
    ) == 'permitted',\
    'permit:pp'


def test_conjugation_en_423():
    assert (
V("permit").t('pr').realize()   
    ) == 'permitting',\
    'permit:pr'


def test_conjugation_en_424():
    assert (
V("pin").t('p').pe(3).realize()   
    ) == 'pins',\
    'pin:p3'


def test_conjugation_en_425():
    assert (
V("pin").t('ps').realize()   
    ) == 'pinned',\
    'pin:ps'


def test_conjugation_en_426():
    assert (
V("pin").t('pp').realize()   
    ) == 'pinned',\
    'pin:pp'


def test_conjugation_en_427():
    assert (
V("pin").t('pr').realize()   
    ) == 'pinning',\
    'pin:pr'


def test_conjugation_en_428():
    assert (
V("plan").t('p').pe(3).realize()   
    ) == 'plans',\
    'plan:p3'


def test_conjugation_en_429():
    assert (
V("plan").t('ps').realize()   
    ) == 'planned',\
    'plan:ps'


def test_conjugation_en_430():
    assert (
V("plan").t('pp').realize()   
    ) == 'planned',\
    'plan:pp'


def test_conjugation_en_431():
    assert (
V("plan").t('pr').realize()   
    ) == 'planning',\
    'plan:pr'


def test_conjugation_en_432():
    assert (
V("plot").t('p').pe(3).realize()   
    ) == 'plots',\
    'plot:p3'


def test_conjugation_en_433():
    assert (
V("plot").t('ps').realize()   
    ) == 'plotted',\
    'plot:ps'


def test_conjugation_en_434():
    assert (
V("plot").t('pp').realize()   
    ) == 'plotted',\
    'plot:pp'


def test_conjugation_en_435():
    assert (
V("plot").t('pr').realize()   
    ) == 'plotting',\
    'plot:pr'


def test_conjugation_en_436():
    assert (
V("plug").t('p').pe(3).realize()   
    ) == 'plugs',\
    'plug:p3'


def test_conjugation_en_437():
    assert (
V("plug").t('ps').realize()   
    ) == 'plugged',\
    'plug:ps'


def test_conjugation_en_438():
    assert (
V("plug").t('pp').realize()   
    ) == 'plugged',\
    'plug:pp'


def test_conjugation_en_439():
    assert (
V("plug").t('pr').realize()   
    ) == 'plugging',\
    'plug:pr'


def test_conjugation_en_440():
    assert (
V("pop").t('p').pe(3).realize()   
    ) == 'pops',\
    'pop:p3'


def test_conjugation_en_441():
    assert (
V("pop").t('ps').realize()   
    ) == 'popped',\
    'pop:ps'


def test_conjugation_en_442():
    assert (
V("pop").t('pp').realize()   
    ) == 'popped',\
    'pop:pp'


def test_conjugation_en_443():
    assert (
V("pop").t('pr').realize()   
    ) == 'popping',\
    'pop:pr'


def test_conjugation_en_444():
    assert (
V("prefer").t('p').pe(3).realize()   
    ) == 'prefers',\
    'prefer:p3'


def test_conjugation_en_445():
    assert (
V("prefer").t('ps').realize()   
    ) == 'preferred',\
    'prefer:ps'


def test_conjugation_en_446():
    assert (
V("prefer").t('pp').realize()   
    ) == 'preferred',\
    'prefer:pp'


def test_conjugation_en_447():
    assert (
V("prefer").t('pr').realize()   
    ) == 'preferring',\
    'prefer:pr'


def test_conjugation_en_448():
    assert (
V("prop").t('p').pe(3).realize()   
    ) == 'props',\
    'prop:p3'


def test_conjugation_en_449():
    assert (
V("prop").t('ps').realize()   
    ) == 'propped',\
    'prop:ps'


def test_conjugation_en_450():
    assert (
V("prop").t('pp').realize()   
    ) == 'propped',\
    'prop:pp'


def test_conjugation_en_451():
    assert (
V("prop").t('pr').realize()   
    ) == 'propping',\
    'prop:pr'


def test_conjugation_en_452():
    assert (
V("put").t('p').pe(3).realize()   
    ) == 'puts',\
    'put:p3'


def test_conjugation_en_453():
    assert (
V("put").t('ps').realize()   
    ) == 'put',\
    'put:ps'


def test_conjugation_en_454():
    assert (
V("put").t('pp').realize()   
    ) == 'put',\
    'put:pp'


def test_conjugation_en_455():
    assert (
V("put").t('pr').realize()   
    ) == 'putting',\
    'put:pr'


def test_conjugation_en_456():
    assert (
V("quit").t('p').pe(3).realize()   
    ) == 'quits',\
    'quit:p3'


def test_conjugation_en_457():
    assert (
V("quit").t('ps').realize()   
    ) == 'quit',\
    'quit:ps'


def test_conjugation_en_458():
    assert (
V("quit").t('pp').realize()   
    ) == 'quit',\
    'quit:pp'


def test_conjugation_en_459():
    assert (
V("quit").t('pr').realize()   
    ) == 'quitting',\
    'quit:pr'


def test_conjugation_en_460():
    assert (
V("read").t('p').pe(3).realize()   
    ) == 'reads',\
    'read:p3'


def test_conjugation_en_461():
    assert (
V("read").t('ps').realize()   
    ) == 'read',\
    'read:ps'


def test_conjugation_en_462():
    assert (
V("read").t('pp').realize()   
    ) == 'read',\
    'read:pp'


def test_conjugation_en_463():
    assert (
V("read").t('pr').realize()   
    ) == 'reading',\
    'read:pr'


def test_conjugation_en_464():
    assert (
V("rebuild").t('p').pe(3).realize()   
    ) == 'rebuilds',\
    'rebuild:p3'


def test_conjugation_en_465():
    assert (
V("rebuild").t('ps').realize()   
    ) == 'rebuilt',\
    'rebuild:ps'


def test_conjugation_en_466():
    assert (
V("rebuild").t('pp').realize()   
    ) == 'rebuilt',\
    'rebuild:pp'


def test_conjugation_en_467():
    assert (
V("rebuild").t('pr').realize()   
    ) == 'rebuilding',\
    'rebuild:pr'


def test_conjugation_en_468():
    assert (
V("regret").t('p').pe(3).realize()   
    ) == 'regrets',\
    'regret:p3'


def test_conjugation_en_469():
    assert (
V("regret").t('ps').realize()   
    ) == 'regretted',\
    'regret:ps'


def test_conjugation_en_470():
    assert (
V("regret").t('pp').realize()   
    ) == 'regretted',\
    'regret:pp'


def test_conjugation_en_471():
    assert (
V("regret").t('pr').realize()   
    ) == 'regretting',\
    'regret:pr'


def test_conjugation_en_472():
    assert (
V("repay").t('p').pe(3).realize()   
    ) == 'repays',\
    'repay:p3'


def test_conjugation_en_473():
    assert (
V("repay").t('ps').realize()   
    ) == 'repaid',\
    'repay:ps'


def test_conjugation_en_474():
    assert (
V("repay").t('pp').realize()   
    ) == 'repaid',\
    'repay:pp'


def test_conjugation_en_475():
    assert (
V("repay").t('pr').realize()   
    ) == 'repaying',\
    'repay:pr'


def test_conjugation_en_476():
    assert (
V("rid").t('p').pe(3).realize()   
    ) == 'rids',\
    'rid:p3'


def test_conjugation_en_477():
    assert (
V("rid").t('ps').realize()   
    ) == 'rid',\
    'rid:ps'


def test_conjugation_en_478():
    assert (
V("rid").t('pp').realize()   
    ) == 'rid',\
    'rid:pp'


def test_conjugation_en_479():
    assert (
V("rid").t('pr').realize()   
    ) == 'ridding',\
    'rid:pr'


def test_conjugation_en_480():
    assert (
V("ride").t('p').pe(3).realize()   
    ) == 'rides',\
    'ride:p3'


def test_conjugation_en_481():
    assert (
V("ride").t('ps').realize()   
    ) == 'rode',\
    'ride:ps'


def test_conjugation_en_482():
    assert (
V("ride").t('pp').realize()   
    ) == 'ridden',\
    'ride:pp'


def test_conjugation_en_483():
    assert (
V("ride").t('pr').realize()   
    ) == 'riding',\
    'ride:pr'


def test_conjugation_en_484():
    assert (
V("rip").t('p').pe(3).realize()   
    ) == 'rips',\
    'rip:p3'


def test_conjugation_en_485():
    assert (
V("rip").t('ps').realize()   
    ) == 'ripped',\
    'rip:ps'


def test_conjugation_en_486():
    assert (
V("rip").t('pp').realize()   
    ) == 'ripped',\
    'rip:pp'


def test_conjugation_en_487():
    assert (
V("rip").t('pr').realize()   
    ) == 'ripping',\
    'rip:pr'


def test_conjugation_en_488():
    assert (
V("rise").t('p').pe(3).realize()   
    ) == 'rises',\
    'rise:p3'


def test_conjugation_en_489():
    assert (
V("rise").t('ps').realize()   
    ) == 'rose',\
    'rise:ps'


def test_conjugation_en_490():
    assert (
V("rise").t('pp').realize()   
    ) == 'risen',\
    'rise:pp'


def test_conjugation_en_491():
    assert (
V("rise").t('pr').realize()   
    ) == 'rising',\
    'rise:pr'


def test_conjugation_en_492():
    assert (
V("rob").t('p').pe(3).realize()   
    ) == 'robs',\
    'rob:p3'


def test_conjugation_en_493():
    assert (
V("rob").t('ps').realize()   
    ) == 'robbed',\
    'rob:ps'


def test_conjugation_en_494():
    assert (
V("rob").t('pp').realize()   
    ) == 'robbed',\
    'rob:pp'


def test_conjugation_en_495():
    assert (
V("rob").t('pr').realize()   
    ) == 'robbing',\
    'rob:pr'


def test_conjugation_en_496():
    assert (
V("rub").t('p').pe(3).realize()   
    ) == 'rubs',\
    'rub:p3'


def test_conjugation_en_497():
    assert (
V("rub").t('ps').realize()   
    ) == 'rubbed',\
    'rub:ps'


def test_conjugation_en_498():
    assert (
V("rub").t('pp').realize()   
    ) == 'rubbed',\
    'rub:pp'


def test_conjugation_en_499():
    assert (
V("rub").t('pr').realize()   
    ) == 'rubbing',\
    'rub:pr'


def test_conjugation_en_500():
    assert (
V("run").t('p').pe(3).realize()   
    ) == 'runs',\
    'run:p3'


def test_conjugation_en_501():
    assert (
V("run").t('ps').realize()   
    ) == 'ran',\
    'run:ps'


def test_conjugation_en_502():
    assert (
V("run").t('pp').realize()   
    ) == 'run',\
    'run:pp'


def test_conjugation_en_503():
    assert (
V("run").t('pr').realize()   
    ) == 'running',\
    'run:pr'


def test_conjugation_en_504():
    assert (
V("say").t('p').pe(3).realize()   
    ) == 'says',\
    'say:p3'


def test_conjugation_en_505():
    assert (
V("say").t('ps').realize()   
    ) == 'said',\
    'say:ps'


def test_conjugation_en_506():
    assert (
V("say").t('pp').realize()   
    ) == 'said',\
    'say:pp'


def test_conjugation_en_507():
    assert (
V("say").t('pr').realize()   
    ) == 'saying',\
    'say:pr'


def test_conjugation_en_508():
    assert (
V("scan").t('p').pe(3).realize()   
    ) == 'scans',\
    'scan:p3'


def test_conjugation_en_509():
    assert (
V("scan").t('ps').realize()   
    ) == 'scanned',\
    'scan:ps'


def test_conjugation_en_510():
    assert (
V("scan").t('pp').realize()   
    ) == 'scanned',\
    'scan:pp'


def test_conjugation_en_511():
    assert (
V("scan").t('pr').realize()   
    ) == 'scanning',\
    'scan:pr'


def test_conjugation_en_512():
    assert (
V("scar").t('p').pe(3).realize()   
    ) == 'scars',\
    'scar:p3'


def test_conjugation_en_513():
    assert (
V("scar").t('ps').realize()   
    ) == 'scarred',\
    'scar:ps'


def test_conjugation_en_514():
    assert (
V("scar").t('pp').realize()   
    ) == 'scarred',\
    'scar:pp'


def test_conjugation_en_515():
    assert (
V("scar").t('pr').realize()   
    ) == 'scarring',\
    'scar:pr'


def test_conjugation_en_516():
    assert (
V("see").t('p').pe(3).realize()   
    ) == 'sees',\
    'see:p3'


def test_conjugation_en_517():
    assert (
V("see").t('ps').realize()   
    ) == 'saw',\
    'see:ps'


def test_conjugation_en_518():
    assert (
V("see").t('pp').realize()   
    ) == 'seen',\
    'see:pp'


def test_conjugation_en_519():
    assert (
V("see").t('pr').realize()   
    ) == 'seeing',\
    'see:pr'


def test_conjugation_en_520():
    assert (
V("seek").t('p').pe(3).realize()   
    ) == 'seeks',\
    'seek:p3'


def test_conjugation_en_521():
    assert (
V("seek").t('ps').realize()   
    ) == 'sought',\
    'seek:ps'


def test_conjugation_en_522():
    assert (
V("seek").t('pp').realize()   
    ) == 'sought',\
    'seek:pp'


def test_conjugation_en_523():
    assert (
V("seek").t('pr').realize()   
    ) == 'seeking',\
    'seek:pr'


def test_conjugation_en_524():
    assert (
V("sell").t('p').pe(3).realize()   
    ) == 'sells',\
    'sell:p3'


def test_conjugation_en_525():
    assert (
V("sell").t('ps').realize()   
    ) == 'sold',\
    'sell:ps'


def test_conjugation_en_526():
    assert (
V("sell").t('pp').realize()   
    ) == 'sold',\
    'sell:pp'


def test_conjugation_en_527():
    assert (
V("sell").t('pr').realize()   
    ) == 'selling',\
    'sell:pr'


def test_conjugation_en_528():
    assert (
V("send").t('p').pe(3).realize()   
    ) == 'sends',\
    'send:p3'


def test_conjugation_en_529():
    assert (
V("send").t('ps').realize()   
    ) == 'sent',\
    'send:ps'


def test_conjugation_en_530():
    assert (
V("send").t('pp').realize()   
    ) == 'sent',\
    'send:pp'


def test_conjugation_en_531():
    assert (
V("send").t('pr').realize()   
    ) == 'sending',\
    'send:pr'


def test_conjugation_en_532():
    assert (
V("set").t('p').pe(3).realize()   
    ) == 'sets',\
    'set:p3'


def test_conjugation_en_533():
    assert (
V("set").t('ps').realize()   
    ) == 'set',\
    'set:ps'


def test_conjugation_en_534():
    assert (
V("set").t('pp').realize()   
    ) == 'set',\
    'set:pp'


def test_conjugation_en_535():
    assert (
V("set").t('pr').realize()   
    ) == 'setting',\
    'set:pr'


def test_conjugation_en_536():
    assert (
V("shake").t('p').pe(3).realize()   
    ) == 'shakes',\
    'shake:p3'


def test_conjugation_en_537():
    assert (
V("shake").t('ps').realize()   
    ) == 'shook',\
    'shake:ps'


def test_conjugation_en_538():
    assert (
V("shake").t('pp').realize()   
    ) == 'shaken',\
    'shake:pp'


def test_conjugation_en_539():
    assert (
V("shake").t('pr').realize()   
    ) == 'shaking',\
    'shake:pr'


def test_conjugation_en_540():
    assert (
V("shed").t('p').pe(3).realize()   
    ) == 'sheds',\
    'shed:p3'


def test_conjugation_en_541():
    assert (
V("shed").t('ps').realize()   
    ) == 'shed',\
    'shed:ps'


def test_conjugation_en_542():
    assert (
V("shed").t('pp').realize()   
    ) == 'shed',\
    'shed:pp'


def test_conjugation_en_543():
    assert (
V("shed").t('pr').realize()   
    ) == 'shedding',\
    'shed:pr'


def test_conjugation_en_544():
    assert (
V("ship").t('p').pe(3).realize()   
    ) == 'ships',\
    'ship:p3'


def test_conjugation_en_545():
    assert (
V("ship").t('ps').realize()   
    ) == 'shipped',\
    'ship:ps'


def test_conjugation_en_546():
    assert (
V("ship").t('pp').realize()   
    ) == 'shipped',\
    'ship:pp'


def test_conjugation_en_547():
    assert (
V("ship").t('pr').realize()   
    ) == 'shipping',\
    'ship:pr'


def test_conjugation_en_548():
    assert (
V("shoot").t('p').pe(3).realize()   
    ) == 'shoots',\
    'shoot:p3'


def test_conjugation_en_549():
    assert (
V("shoot").t('ps').realize()   
    ) == 'shot',\
    'shoot:ps'


def test_conjugation_en_550():
    assert (
V("shoot").t('pp').realize()   
    ) == 'shot',\
    'shoot:pp'


def test_conjugation_en_551():
    assert (
V("shoot").t('pr').realize()   
    ) == 'shooting',\
    'shoot:pr'


def test_conjugation_en_552():
    assert (
V("shop").t('p').pe(3).realize()   
    ) == 'shops',\
    'shop:p3'


def test_conjugation_en_553():
    assert (
V("shop").t('ps').realize()   
    ) == 'shopped',\
    'shop:ps'


def test_conjugation_en_554():
    assert (
V("shop").t('pp').realize()   
    ) == 'shopped',\
    'shop:pp'


def test_conjugation_en_555():
    assert (
V("shop").t('pr').realize()   
    ) == 'shopping',\
    'shop:pr'


def test_conjugation_en_556():
    assert (
V("show").t('p').pe(3).realize()   
    ) == 'shows',\
    'show:p3'


def test_conjugation_en_557():
    assert (
V("show").t('ps').realize()   
    ) == 'showed',\
    'show:ps'


def test_conjugation_en_558():
    assert (
V("show").t('pp').realize()   
    ) == 'shown',\
    'show:pp'


def test_conjugation_en_559():
    assert (
V("show").t('pr').realize()   
    ) == 'showing',\
    'show:pr'


def test_conjugation_en_560():
    assert (
V("shrink").t('p').pe(3).realize()   
    ) == 'shrinks',\
    'shrink:p3'


def test_conjugation_en_561():
    assert (
V("shrink").t('ps').realize()   
    ) == 'shrank',\
    'shrink:ps'


def test_conjugation_en_562():
    assert (
V("shrink").t('pp').realize()   
    ) == 'shrunk',\
    'shrink:pp'


def test_conjugation_en_563():
    assert (
V("shrink").t('pr').realize()   
    ) == 'shrinking',\
    'shrink:pr'


def test_conjugation_en_564():
    assert (
V("shrug").t('p').pe(3).realize()   
    ) == 'shrugs',\
    'shrug:p3'


def test_conjugation_en_565():
    assert (
V("shrug").t('ps').realize()   
    ) == 'shrugged',\
    'shrug:ps'


def test_conjugation_en_566():
    assert (
V("shrug").t('pp').realize()   
    ) == 'shrugged',\
    'shrug:pp'


def test_conjugation_en_567():
    assert (
V("shrug").t('pr').realize()   
    ) == 'shrugging',\
    'shrug:pr'


def test_conjugation_en_568():
    assert (
V("shut").t('p').pe(3).realize()   
    ) == 'shuts',\
    'shut:p3'


def test_conjugation_en_569():
    assert (
V("shut").t('ps').realize()   
    ) == 'shut',\
    'shut:ps'


def test_conjugation_en_570():
    assert (
V("shut").t('pp').realize()   
    ) == 'shut',\
    'shut:pp'


def test_conjugation_en_571():
    assert (
V("shut").t('pr').realize()   
    ) == 'shutting',\
    'shut:pr'


def test_conjugation_en_572():
    assert (
V("sing").t('p').pe(3).realize()   
    ) == 'sings',\
    'sing:p3'


def test_conjugation_en_573():
    assert (
V("sing").t('ps').realize()   
    ) == 'sang',\
    'sing:ps'


def test_conjugation_en_574():
    assert (
V("sing").t('pp').realize()   
    ) == 'sung',\
    'sing:pp'


def test_conjugation_en_575():
    assert (
V("sing").t('pr').realize()   
    ) == 'singing',\
    'sing:pr'


def test_conjugation_en_576():
    assert (
V("sink").t('p').pe(3).realize()   
    ) == 'sinks',\
    'sink:p3'


def test_conjugation_en_577():
    assert (
V("sink").t('ps').realize()   
    ) == 'sank',\
    'sink:ps'


def test_conjugation_en_578():
    assert (
V("sink").t('pp').realize()   
    ) == 'sunk',\
    'sink:pp'


def test_conjugation_en_579():
    assert (
V("sink").t('pr').realize()   
    ) == 'sinking',\
    'sink:pr'


def test_conjugation_en_580():
    assert (
V("sip").t('p').pe(3).realize()   
    ) == 'sips',\
    'sip:p3'


def test_conjugation_en_581():
    assert (
V("sip").t('ps').realize()   
    ) == 'sipped',\
    'sip:ps'


def test_conjugation_en_582():
    assert (
V("sip").t('pp').realize()   
    ) == 'sipped',\
    'sip:pp'


def test_conjugation_en_583():
    assert (
V("sip").t('pr').realize()   
    ) == 'sipping',\
    'sip:pr'


def test_conjugation_en_584():
    assert (
V("sit").t('p').pe(3).realize()   
    ) == 'sits',\
    'sit:p3'


def test_conjugation_en_585():
    assert (
V("sit").t('ps').realize()   
    ) == 'sat',\
    'sit:ps'


def test_conjugation_en_586():
    assert (
V("sit").t('pp').realize()   
    ) == 'sat',\
    'sit:pp'


def test_conjugation_en_587():
    assert (
V("sit").t('pr').realize()   
    ) == 'sitting',\
    'sit:pr'


def test_conjugation_en_588():
    assert (
V("slam").t('p').pe(3).realize()   
    ) == 'slams',\
    'slam:p3'


def test_conjugation_en_589():
    assert (
V("slam").t('ps').realize()   
    ) == 'slammed',\
    'slam:ps'


def test_conjugation_en_590():
    assert (
V("slam").t('pp').realize()   
    ) == 'slammed',\
    'slam:pp'


def test_conjugation_en_591():
    assert (
V("slam").t('pr').realize()   
    ) == 'slamming',\
    'slam:pr'


def test_conjugation_en_592():
    assert (
V("slap").t('p').pe(3).realize()   
    ) == 'slaps',\
    'slap:p3'


def test_conjugation_en_593():
    assert (
V("slap").t('ps').realize()   
    ) == 'slapped',\
    'slap:ps'


def test_conjugation_en_594():
    assert (
V("slap").t('pp').realize()   
    ) == 'slapped',\
    'slap:pp'


def test_conjugation_en_595():
    assert (
V("slap").t('pr').realize()   
    ) == 'slapping',\
    'slap:pr'


def test_conjugation_en_596():
    assert (
V("sleep").t('p').pe(3).realize()   
    ) == 'sleeps',\
    'sleep:p3'


def test_conjugation_en_597():
    assert (
V("sleep").t('ps').realize()   
    ) == 'slept',\
    'sleep:ps'


def test_conjugation_en_598():
    assert (
V("sleep").t('pp').realize()   
    ) == 'slept',\
    'sleep:pp'


def test_conjugation_en_599():
    assert (
V("sleep").t('pr').realize()   
    ) == 'sleeping',\
    'sleep:pr'


def test_conjugation_en_600():
    assert (
V("slide").t('p').pe(3).realize()   
    ) == 'slides',\
    'slide:p3'


def test_conjugation_en_601():
    assert (
V("slide").t('ps').realize()   
    ) == 'slid',\
    'slide:ps'


def test_conjugation_en_602():
    assert (
V("slide").t('pp').realize()   
    ) == 'slid',\
    'slide:pp'


def test_conjugation_en_603():
    assert (
V("slide").t('pr').realize()   
    ) == 'sliding',\
    'slide:pr'


def test_conjugation_en_604():
    assert (
V("slip").t('p').pe(3).realize()   
    ) == 'slips',\
    'slip:p3'


def test_conjugation_en_605():
    assert (
V("slip").t('ps').realize()   
    ) == 'slipped',\
    'slip:ps'


def test_conjugation_en_606():
    assert (
V("slip").t('pp').realize()   
    ) == 'slipped',\
    'slip:pp'


def test_conjugation_en_607():
    assert (
V("slip").t('pr').realize()   
    ) == 'slipping',\
    'slip:pr'


def test_conjugation_en_608():
    assert (
V("snap").t('p').pe(3).realize()   
    ) == 'snaps',\
    'snap:p3'


def test_conjugation_en_609():
    assert (
V("snap").t('ps').realize()   
    ) == 'snapped',\
    'snap:ps'


def test_conjugation_en_610():
    assert (
V("snap").t('pp').realize()   
    ) == 'snapped',\
    'snap:pp'


def test_conjugation_en_611():
    assert (
V("snap").t('pr').realize()   
    ) == 'snapping',\
    'snap:pr'


def test_conjugation_en_612():
    assert (
V("speak").t('p').pe(3).realize()   
    ) == 'speaks',\
    'speak:p3'


def test_conjugation_en_613():
    assert (
V("speak").t('ps').realize()   
    ) == 'spoke',\
    'speak:ps'


def test_conjugation_en_614():
    assert (
V("speak").t('pp').realize()   
    ) == 'spoken',\
    'speak:pp'


def test_conjugation_en_615():
    assert (
V("speak").t('pr').realize()   
    ) == 'speaking',\
    'speak:pr'


def test_conjugation_en_616():
    assert (
V("spend").t('p').pe(3).realize()   
    ) == 'spends',\
    'spend:p3'


def test_conjugation_en_617():
    assert (
V("spend").t('ps').realize()   
    ) == 'spent',\
    'spend:ps'


def test_conjugation_en_618():
    assert (
V("spend").t('pp').realize()   
    ) == 'spent',\
    'spend:pp'


def test_conjugation_en_619():
    assert (
V("spend").t('pr').realize()   
    ) == 'spending',\
    'spend:pr'


def test_conjugation_en_620():
    assert (
V("spin").t('p').pe(3).realize()   
    ) == 'spins',\
    'spin:p3'


def test_conjugation_en_621():
    assert (
V("spin").t('ps').realize()   
    ) == 'spun',\
    'spin:ps'


def test_conjugation_en_622():
    assert (
V("spin").t('pp').realize()   
    ) == 'spun',\
    'spin:pp'


def test_conjugation_en_623():
    assert (
V("spin").t('pr').realize()   
    ) == 'spinning',\
    'spin:pr'


def test_conjugation_en_624():
    assert (
V("spit").t('p').pe(3).realize()   
    ) == 'spits',\
    'spit:p3'


def test_conjugation_en_625():
    assert (
V("spit").t('ps').realize()   
    ) == 'spat',\
    'spit:ps'


def test_conjugation_en_626():
    assert (
V("spit").t('pp').realize()   
    ) == 'spat',\
    'spit:pp'


def test_conjugation_en_627():
    assert (
V("spit").t('pr').realize()   
    ) == 'spitting',\
    'spit:pr'


def test_conjugation_en_628():
    assert (
V("split").t('p').pe(3).realize()   
    ) == 'splits',\
    'split:p3'


def test_conjugation_en_629():
    assert (
V("split").t('ps').realize()   
    ) == 'split',\
    'split:ps'


def test_conjugation_en_630():
    assert (
V("split").t('pp').realize()   
    ) == 'split',\
    'split:pp'


def test_conjugation_en_631():
    assert (
V("split").t('pr').realize()   
    ) == 'splitting',\
    'split:pr'


def test_conjugation_en_632():
    assert (
V("spot").t('p').pe(3).realize()   
    ) == 'spots',\
    'spot:p3'


def test_conjugation_en_633():
    assert (
V("spot").t('ps').realize()   
    ) == 'spotted',\
    'spot:ps'


def test_conjugation_en_634():
    assert (
V("spot").t('pp').realize()   
    ) == 'spotted',\
    'spot:pp'


def test_conjugation_en_635():
    assert (
V("spot").t('pr').realize()   
    ) == 'spotting',\
    'spot:pr'


def test_conjugation_en_636():
    assert (
V("spread").t('p').pe(3).realize()   
    ) == 'spreads',\
    'spread:p3'


def test_conjugation_en_637():
    assert (
V("spread").t('ps').realize()   
    ) == 'spread',\
    'spread:ps'


def test_conjugation_en_638():
    assert (
V("spread").t('pp').realize()   
    ) == 'spread',\
    'spread:pp'


def test_conjugation_en_639():
    assert (
V("spread").t('pr').realize()   
    ) == 'spreading',\
    'spread:pr'


def test_conjugation_en_640():
    assert (
V("spring").t('p').pe(3).realize()   
    ) == 'springs',\
    'spring:p3'


def test_conjugation_en_641():
    assert (
V("spring").t('ps').realize()   
    ) == 'sprang',\
    'spring:ps'


def test_conjugation_en_642():
    assert (
V("spring").t('pp').realize()   
    ) == 'sprung',\
    'spring:pp'


def test_conjugation_en_643():
    assert (
V("spring").t('pr').realize()   
    ) == 'springing',\
    'spring:pr'


def test_conjugation_en_644():
    assert (
V("stab").t('p').pe(3).realize()   
    ) == 'stabs',\
    'stab:p3'


def test_conjugation_en_645():
    assert (
V("stab").t('ps').realize()   
    ) == 'stabbed',\
    'stab:ps'


def test_conjugation_en_646():
    assert (
V("stab").t('pp').realize()   
    ) == 'stabbed',\
    'stab:pp'


def test_conjugation_en_647():
    assert (
V("stab").t('pr').realize()   
    ) == 'stabbing',\
    'stab:pr'


def test_conjugation_en_648():
    assert (
V("stand").t('p').pe(3).realize()   
    ) == 'stands',\
    'stand:p3'


def test_conjugation_en_649():
    assert (
V("stand").t('ps').realize()   
    ) == 'stood',\
    'stand:ps'


def test_conjugation_en_650():
    assert (
V("stand").t('pp').realize()   
    ) == 'stood',\
    'stand:pp'


def test_conjugation_en_651():
    assert (
V("stand").t('pr').realize()   
    ) == 'standing',\
    'stand:pr'


def test_conjugation_en_652():
    assert (
V("star").t('p').pe(3).realize()   
    ) == 'stars',\
    'star:p3'


def test_conjugation_en_653():
    assert (
V("star").t('ps').realize()   
    ) == 'starred',\
    'star:ps'


def test_conjugation_en_654():
    assert (
V("star").t('pp').realize()   
    ) == 'starred',\
    'star:pp'


def test_conjugation_en_655():
    assert (
V("star").t('pr').realize()   
    ) == 'starring',\
    'star:pr'


def test_conjugation_en_656():
    assert (
V("steal").t('p').pe(3).realize()   
    ) == 'steals',\
    'steal:p3'


def test_conjugation_en_657():
    assert (
V("steal").t('ps').realize()   
    ) == 'stole',\
    'steal:ps'


def test_conjugation_en_658():
    assert (
V("steal").t('pp').realize()   
    ) == 'stolen',\
    'steal:pp'


def test_conjugation_en_659():
    assert (
V("steal").t('pr').realize()   
    ) == 'stealing',\
    'steal:pr'


def test_conjugation_en_660():
    assert (
V("stem").t('p').pe(3).realize()   
    ) == 'stems',\
    'stem:p3'


def test_conjugation_en_661():
    assert (
V("stem").t('ps').realize()   
    ) == 'stemmed',\
    'stem:ps'


def test_conjugation_en_662():
    assert (
V("stem").t('pp').realize()   
    ) == 'stemmed',\
    'stem:pp'


def test_conjugation_en_663():
    assert (
V("stem").t('pr').realize()   
    ) == 'stemming',\
    'stem:pr'


def test_conjugation_en_664():
    assert (
V("step").t('p').pe(3).realize()   
    ) == 'steps',\
    'step:p3'


def test_conjugation_en_665():
    assert (
V("step").t('ps').realize()   
    ) == 'stepped',\
    'step:ps'


def test_conjugation_en_666():
    assert (
V("step").t('pp').realize()   
    ) == 'stepped',\
    'step:pp'


def test_conjugation_en_667():
    assert (
V("step").t('pr').realize()   
    ) == 'stepping',\
    'step:pr'


def test_conjugation_en_668():
    assert (
V("stick").t('p').pe(3).realize()   
    ) == 'sticks',\
    'stick:p3'


def test_conjugation_en_669():
    assert (
V("stick").t('ps').realize()   
    ) == 'stuck',\
    'stick:ps'


def test_conjugation_en_670():
    assert (
V("stick").t('pp').realize()   
    ) == 'stuck',\
    'stick:pp'


def test_conjugation_en_671():
    assert (
V("stick").t('pr').realize()   
    ) == 'sticking',\
    'stick:pr'


def test_conjugation_en_672():
    assert (
V("stir").t('p').pe(3).realize()   
    ) == 'stirs',\
    'stir:p3'


def test_conjugation_en_673():
    assert (
V("stir").t('ps').realize()   
    ) == 'stirred',\
    'stir:ps'


def test_conjugation_en_674():
    assert (
V("stir").t('pp').realize()   
    ) == 'stirred',\
    'stir:pp'


def test_conjugation_en_675():
    assert (
V("stir").t('pr').realize()   
    ) == 'stirring',\
    'stir:pr'


def test_conjugation_en_676():
    assert (
V("stop").t('p').pe(3).realize()   
    ) == 'stops',\
    'stop:p3'


def test_conjugation_en_677():
    assert (
V("stop").t('ps').realize()   
    ) == 'stopped',\
    'stop:ps'


def test_conjugation_en_678():
    assert (
V("stop").t('pp').realize()   
    ) == 'stopped',\
    'stop:pp'


def test_conjugation_en_679():
    assert (
V("stop").t('pr').realize()   
    ) == 'stopping',\
    'stop:pr'


def test_conjugation_en_680():
    assert (
V("stride").t('p').pe(3).realize()   
    ) == 'strides',\
    'stride:p3'


def test_conjugation_en_681():
    assert (
V("stride").t('ps').realize()   
    ) == 'strode',\
    'stride:ps'


def test_conjugation_en_682():
    assert (
V("stride").t('pp').realize()   
    ) == 'stridden',\
    'stride:pp'


def test_conjugation_en_683():
    assert (
V("stride").t('pr').realize()   
    ) == 'striding',\
    'stride:pr'


def test_conjugation_en_684():
    assert (
V("strike").t('p').pe(3).realize()   
    ) == 'strikes',\
    'strike:p3'


def test_conjugation_en_685():
    assert (
V("strike").t('ps').realize()   
    ) == 'struck',\
    'strike:ps'


def test_conjugation_en_686():
    assert (
V("strike").t('pp').realize()   
    ) == 'struck',\
    'strike:pp'


def test_conjugation_en_687():
    assert (
V("strike").t('pr').realize()   
    ) == 'striking',\
    'strike:pr'


def test_conjugation_en_688():
    assert (
V("strip").t('p').pe(3).realize()   
    ) == 'strips',\
    'strip:p3'


def test_conjugation_en_689():
    assert (
V("strip").t('ps').realize()   
    ) == 'stripped',\
    'strip:ps'


def test_conjugation_en_690():
    assert (
V("strip").t('pp').realize()   
    ) == 'stripped',\
    'strip:pp'


def test_conjugation_en_691():
    assert (
V("strip").t('pr').realize()   
    ) == 'stripping',\
    'strip:pr'


def test_conjugation_en_692():
    assert (
V("submit").t('p').pe(3).realize()   
    ) == 'submits',\
    'submit:p3'


def test_conjugation_en_693():
    assert (
V("submit").t('ps').realize()   
    ) == 'submitted',\
    'submit:ps'


def test_conjugation_en_694():
    assert (
V("submit").t('pp').realize()   
    ) == 'submitted',\
    'submit:pp'


def test_conjugation_en_695():
    assert (
V("submit").t('pr').realize()   
    ) == 'submitting',\
    'submit:pr'


def test_conjugation_en_696():
    assert (
V("sum").t('p').pe(3).realize()   
    ) == 'sums',\
    'sum:p3'


def test_conjugation_en_697():
    assert (
V("sum").t('ps').realize()   
    ) == 'summed',\
    'sum:ps'


def test_conjugation_en_698():
    assert (
V("sum").t('pp').realize()   
    ) == 'summed',\
    'sum:pp'


def test_conjugation_en_699():
    assert (
V("sum").t('pr').realize()   
    ) == 'summing',\
    'sum:pr'


def test_conjugation_en_700():
    assert (
V("swap").t('p').pe(3).realize()   
    ) == 'swaps',\
    'swap:p3'


def test_conjugation_en_701():
    assert (
V("swap").t('ps').realize()   
    ) == 'swapped',\
    'swap:ps'


def test_conjugation_en_702():
    assert (
V("swap").t('pp').realize()   
    ) == 'swapped',\
    'swap:pp'


def test_conjugation_en_703():
    assert (
V("swap").t('pr').realize()   
    ) == 'swapping',\
    'swap:pr'


def test_conjugation_en_704():
    assert (
V("swear").t('p').pe(3).realize()   
    ) == 'swears',\
    'swear:p3'


def test_conjugation_en_705():
    assert (
V("swear").t('ps').realize()   
    ) == 'swore',\
    'swear:ps'


def test_conjugation_en_706():
    assert (
V("swear").t('pp').realize()   
    ) == 'sworn',\
    'swear:pp'


def test_conjugation_en_707():
    assert (
V("swear").t('pr').realize()   
    ) == 'swearing',\
    'swear:pr'


def test_conjugation_en_708():
    assert (
V("sweep").t('p').pe(3).realize()   
    ) == 'sweeps',\
    'sweep:p3'


def test_conjugation_en_709():
    assert (
V("sweep").t('ps').realize()   
    ) == 'swept',\
    'sweep:ps'


def test_conjugation_en_710():
    assert (
V("sweep").t('pp').realize()   
    ) == 'swept',\
    'sweep:pp'


def test_conjugation_en_711():
    assert (
V("sweep").t('pr').realize()   
    ) == 'sweeping',\
    'sweep:pr'


def test_conjugation_en_712():
    assert (
V("swell").t('p').pe(3).realize()   
    ) == 'swells',\
    'swell:p3'


def test_conjugation_en_713():
    assert (
V("swell").t('ps').realize()   
    ) == 'swelled',\
    'swell:ps'


def test_conjugation_en_714():
    assert (
V("swell").t('pp').realize()   
    ) == 'swelled',\
    'swell:pp'


def test_conjugation_en_715():
    assert (
V("swell").t('pr').realize()   
    ) == 'swelling',\
    'swell:pr'


def test_conjugation_en_716():
    assert (
V("swim").t('p').pe(3).realize()   
    ) == 'swims',\
    'swim:p3'


def test_conjugation_en_717():
    assert (
V("swim").t('ps').realize()   
    ) == 'swam',\
    'swim:ps'


def test_conjugation_en_718():
    assert (
V("swim").t('pp').realize()   
    ) == 'swum',\
    'swim:pp'


def test_conjugation_en_719():
    assert (
V("swim").t('pr').realize()   
    ) == 'swimming',\
    'swim:pr'


def test_conjugation_en_720():
    assert (
V("swing").t('p').pe(3).realize()   
    ) == 'swings',\
    'swing:p3'


def test_conjugation_en_721():
    assert (
V("swing").t('ps').realize()   
    ) == 'swung',\
    'swing:ps'


def test_conjugation_en_722():
    assert (
V("swing").t('pp').realize()   
    ) == 'swung',\
    'swing:pp'


def test_conjugation_en_723():
    assert (
V("swing").t('pr').realize()   
    ) == 'swinging',\
    'swing:pr'


def test_conjugation_en_724():
    assert (
V("take").t('p').pe(3).realize()   
    ) == 'takes',\
    'take:p3'


def test_conjugation_en_725():
    assert (
V("take").t('ps').realize()   
    ) == 'took',\
    'take:ps'


def test_conjugation_en_726():
    assert (
V("take").t('pp').realize()   
    ) == 'taken',\
    'take:pp'


def test_conjugation_en_727():
    assert (
V("take").t('pr').realize()   
    ) == 'taking',\
    'take:pr'


def test_conjugation_en_728():
    assert (
V("tap").t('p').pe(3).realize()   
    ) == 'taps',\
    'tap:p3'


def test_conjugation_en_729():
    assert (
V("tap").t('ps').realize()   
    ) == 'tapped',\
    'tap:ps'


def test_conjugation_en_730():
    assert (
V("tap").t('pp').realize()   
    ) == 'tapped',\
    'tap:pp'


def test_conjugation_en_731():
    assert (
V("tap").t('pr').realize()   
    ) == 'tapping',\
    'tap:pr'


def test_conjugation_en_732():
    assert (
V("teach").t('p').pe(3).realize()   
    ) == 'teaches',\
    'teach:p3'


def test_conjugation_en_733():
    assert (
V("teach").t('ps').realize()   
    ) == 'taught',\
    'teach:ps'


def test_conjugation_en_734():
    assert (
V("teach").t('pp').realize()   
    ) == 'taught',\
    'teach:pp'


def test_conjugation_en_735():
    assert (
V("teach").t('pr').realize()   
    ) == 'teaching',\
    'teach:pr'


def test_conjugation_en_736():
    assert (
V("tear").t('p').pe(3).realize()   
    ) == 'tears',\
    'tear:p3'


def test_conjugation_en_737():
    assert (
V("tear").t('ps').realize()   
    ) == 'tore',\
    'tear:ps'


def test_conjugation_en_738():
    assert (
V("tear").t('pp').realize()   
    ) == 'torn',\
    'tear:pp'


def test_conjugation_en_739():
    assert (
V("tear").t('pr').realize()   
    ) == 'tearing',\
    'tear:pr'


def test_conjugation_en_740():
    assert (
V("tell").t('p').pe(3).realize()   
    ) == 'tells',\
    'tell:p3'


def test_conjugation_en_741():
    assert (
V("tell").t('ps').realize()   
    ) == 'told',\
    'tell:ps'


def test_conjugation_en_742():
    assert (
V("tell").t('pp').realize()   
    ) == 'told',\
    'tell:pp'


def test_conjugation_en_743():
    assert (
V("tell").t('pr').realize()   
    ) == 'telling',\
    'tell:pr'


def test_conjugation_en_744():
    assert (
V("think").t('p').pe(3).realize()   
    ) == 'thinks',\
    'think:p3'


def test_conjugation_en_745():
    assert (
V("think").t('ps').realize()   
    ) == 'thought',\
    'think:ps'


def test_conjugation_en_746():
    assert (
V("think").t('pp').realize()   
    ) == 'thought',\
    'think:pp'


def test_conjugation_en_747():
    assert (
V("think").t('pr').realize()   
    ) == 'thinking',\
    'think:pr'


def test_conjugation_en_748():
    assert (
V("throw").t('p').pe(3).realize()   
    ) == 'throws',\
    'throw:p3'


def test_conjugation_en_749():
    assert (
V("throw").t('ps').realize()   
    ) == 'threw',\
    'throw:ps'


def test_conjugation_en_750():
    assert (
V("throw").t('pp').realize()   
    ) == 'thrown',\
    'throw:pp'


def test_conjugation_en_751():
    assert (
V("throw").t('pr').realize()   
    ) == 'throwing',\
    'throw:pr'


def test_conjugation_en_752():
    assert (
V("thrust").t('p').pe(3).realize()   
    ) == 'thrusts',\
    'thrust:p3'


def test_conjugation_en_753():
    assert (
V("thrust").t('ps').realize()   
    ) == 'thrust',\
    'thrust:ps'


def test_conjugation_en_754():
    assert (
V("thrust").t('pp').realize()   
    ) == 'thrust',\
    'thrust:pp'


def test_conjugation_en_755():
    assert (
V("thrust").t('pr').realize()   
    ) == 'thrusting',\
    'thrust:pr'


def test_conjugation_en_756():
    assert (
V("tip").t('p').pe(3).realize()   
    ) == 'tips',\
    'tip:p3'


def test_conjugation_en_757():
    assert (
V("tip").t('ps').realize()   
    ) == 'tipped',\
    'tip:ps'


def test_conjugation_en_758():
    assert (
V("tip").t('pp').realize()   
    ) == 'tipped',\
    'tip:pp'


def test_conjugation_en_759():
    assert (
V("tip").t('pr').realize()   
    ) == 'tipping',\
    'tip:pr'


def test_conjugation_en_760():
    assert (
V("top").t('p').pe(3).realize()   
    ) == 'tops',\
    'top:p3'


def test_conjugation_en_761():
    assert (
V("top").t('ps').realize()   
    ) == 'topped',\
    'top:ps'


def test_conjugation_en_762():
    assert (
V("top").t('pp').realize()   
    ) == 'topped',\
    'top:pp'


def test_conjugation_en_763():
    assert (
V("top").t('pr').realize()   
    ) == 'topping',\
    'top:pr'


def test_conjugation_en_764():
    assert (
V("transfer").t('p').pe(3).realize()   
    ) == 'transfers',\
    'transfer:p3'


def test_conjugation_en_765():
    assert (
V("transfer").t('ps').realize()   
    ) == 'transferred',\
    'transfer:ps'


def test_conjugation_en_766():
    assert (
V("transfer").t('pp').realize()   
    ) == 'transferred',\
    'transfer:pp'


def test_conjugation_en_767():
    assert (
V("transfer").t('pr').realize()   
    ) == 'transferring',\
    'transfer:pr'


def test_conjugation_en_768():
    assert (
V("transmit").t('p').pe(3).realize()   
    ) == 'transmits',\
    'transmit:p3'


def test_conjugation_en_769():
    assert (
V("transmit").t('ps').realize()   
    ) == 'transmitted',\
    'transmit:ps'


def test_conjugation_en_770():
    assert (
V("transmit").t('pp').realize()   
    ) == 'transmitted',\
    'transmit:pp'


def test_conjugation_en_771():
    assert (
V("transmit").t('pr').realize()   
    ) == 'transmitting',\
    'transmit:pr'


def test_conjugation_en_772():
    assert (
V("trap").t('p').pe(3).realize()   
    ) == 'traps',\
    'trap:p3'


def test_conjugation_en_773():
    assert (
V("trap").t('ps').realize()   
    ) == 'trapped',\
    'trap:ps'


def test_conjugation_en_774():
    assert (
V("trap").t('pp').realize()   
    ) == 'trapped',\
    'trap:pp'


def test_conjugation_en_775():
    assert (
V("trap").t('pr').realize()   
    ) == 'trapping',\
    'trap:pr'


def test_conjugation_en_776():
    assert (
V("tread").t('p').pe(3).realize()   
    ) == 'treads',\
    'tread:p3'


def test_conjugation_en_777():
    assert (
V("tread").t('ps').realize()   
    ) == 'trod',\
    'tread:ps'


def test_conjugation_en_778():
    assert (
V("tread").t('pp').realize()   
    ) == 'trod',\
    'tread:pp'


def test_conjugation_en_779():
    assert (
V("tread").t('pr').realize()   
    ) == 'treading',\
    'tread:pr'


def test_conjugation_en_780():
    assert (
V("trip").t('p').pe(3).realize()   
    ) == 'trips',\
    'trip:p3'


def test_conjugation_en_781():
    assert (
V("trip").t('ps').realize()   
    ) == 'tripped',\
    'trip:ps'


def test_conjugation_en_782():
    assert (
V("trip").t('pp').realize()   
    ) == 'tripped',\
    'trip:pp'


def test_conjugation_en_783():
    assert (
V("trip").t('pr').realize()   
    ) == 'tripping',\
    'trip:pr'


def test_conjugation_en_784():
    assert (
V("undergo").t('p').pe(3).realize()   
    ) == 'undergoes',\
    'undergo:p3'


def test_conjugation_en_785():
    assert (
V("undergo").t('ps').realize()   
    ) == 'underwent',\
    'undergo:ps'


def test_conjugation_en_786():
    assert (
V("undergo").t('pp').realize()   
    ) == 'undergone',\
    'undergo:pp'


def test_conjugation_en_787():
    assert (
V("undergo").t('pr').realize()   
    ) == 'undergoing',\
    'undergo:pr'


def test_conjugation_en_788():
    assert (
V("understand").t('p').pe(3).realize()   
    ) == 'understands',\
    'understand:p3'


def test_conjugation_en_789():
    assert (
V("understand").t('ps').realize()   
    ) == 'understood',\
    'understand:ps'


def test_conjugation_en_790():
    assert (
V("understand").t('pp').realize()   
    ) == 'understood',\
    'understand:pp'


def test_conjugation_en_791():
    assert (
V("understand").t('pr').realize()   
    ) == 'understanding',\
    'understand:pr'


def test_conjugation_en_792():
    assert (
V("undertake").t('p').pe(3).realize()   
    ) == 'undertakes',\
    'undertake:p3'


def test_conjugation_en_793():
    assert (
V("undertake").t('ps').realize()   
    ) == 'undertook',\
    'undertake:ps'


def test_conjugation_en_794():
    assert (
V("undertake").t('pp').realize()   
    ) == 'undertaken',\
    'undertake:pp'


def test_conjugation_en_795():
    assert (
V("undertake").t('pr').realize()   
    ) == 'undertaking',\
    'undertake:pr'


def test_conjugation_en_796():
    assert (
V("uphold").t('p').pe(3).realize()   
    ) == 'upholds',\
    'uphold:p3'


def test_conjugation_en_797():
    assert (
V("uphold").t('ps').realize()   
    ) == 'upheld',\
    'uphold:ps'


def test_conjugation_en_798():
    assert (
V("uphold").t('pp').realize()   
    ) == 'upheld',\
    'uphold:pp'


def test_conjugation_en_799():
    assert (
V("uphold").t('pr').realize()   
    ) == 'upholding',\
    'uphold:pr'


def test_conjugation_en_800():
    assert (
V("upset").t('p').pe(3).realize()   
    ) == 'upsets',\
    'upset:p3'


def test_conjugation_en_801():
    assert (
V("upset").t('ps').realize()   
    ) == 'upset',\
    'upset:ps'


def test_conjugation_en_802():
    assert (
V("upset").t('pp').realize()   
    ) == 'upset',\
    'upset:pp'


def test_conjugation_en_803():
    assert (
V("upset").t('pr').realize()   
    ) == 'upsetting',\
    'upset:pr'


def test_conjugation_en_804():
    assert (
V("wake").t('p').pe(3).realize()   
    ) == 'wakes',\
    'wake:p3'


def test_conjugation_en_805():
    assert (
V("wake").t('ps').realize()   
    ) == 'woke',\
    'wake:ps'


def test_conjugation_en_806():
    assert (
V("wake").t('pp').realize()   
    ) == 'woken',\
    'wake:pp'


def test_conjugation_en_807():
    assert (
V("wake").t('pr').realize()   
    ) == 'waking',\
    'wake:pr'


def test_conjugation_en_808():
    assert (
V("wear").t('p').pe(3).realize()   
    ) == 'wears',\
    'wear:p3'


def test_conjugation_en_809():
    assert (
V("wear").t('ps').realize()   
    ) == 'wore',\
    'wear:ps'


def test_conjugation_en_810():
    assert (
V("wear").t('pp').realize()   
    ) == 'worn',\
    'wear:pp'


def test_conjugation_en_811():
    assert (
V("wear").t('pr').realize()   
    ) == 'wearing',\
    'wear:pr'


def test_conjugation_en_812():
    assert (
V("weep").t('p').pe(3).realize()   
    ) == 'weeps',\
    'weep:p3'


def test_conjugation_en_813():
    assert (
V("weep").t('ps').realize()   
    ) == 'wept',\
    'weep:ps'


def test_conjugation_en_814():
    assert (
V("weep").t('pp').realize()   
    ) == 'wept',\
    'weep:pp'


def test_conjugation_en_815():
    assert (
V("weep").t('pr').realize()   
    ) == 'weeping',\
    'weep:pr'


def test_conjugation_en_816():
    assert (
V("wet").t('p').pe(3).realize()   
    ) == 'wets',\
    'wet:p3'


def test_conjugation_en_817():
    assert (
V("wet").t('ps').realize()   
    ) == 'wet',\
    'wet:ps'


def test_conjugation_en_818():
    assert (
V("wet").t('pp').realize()   
    ) == 'wet',\
    'wet:pp'


def test_conjugation_en_819():
    assert (
V("wet").t('pr').realize()   
    ) == 'wetting',\
    'wet:pr'


def test_conjugation_en_820():
    assert (
V("whip").t('p').pe(3).realize()   
    ) == 'whips',\
    'whip:p3'


def test_conjugation_en_821():
    assert (
V("whip").t('ps').realize()   
    ) == 'whipped',\
    'whip:ps'


def test_conjugation_en_822():
    assert (
V("whip").t('pp').realize()   
    ) == 'whipped',\
    'whip:pp'


def test_conjugation_en_823():
    assert (
V("whip").t('pr').realize()   
    ) == 'whipping',\
    'whip:pr'


def test_conjugation_en_824():
    assert (
V("win").t('p').pe(3).realize()   
    ) == 'wins',\
    'win:p3'


def test_conjugation_en_825():
    assert (
V("win").t('ps').realize()   
    ) == 'won',\
    'win:ps'


def test_conjugation_en_826():
    assert (
V("win").t('pp').realize()   
    ) == 'won',\
    'win:pp'


def test_conjugation_en_827():
    assert (
V("win").t('pr').realize()   
    ) == 'winning',\
    'win:pr'


def test_conjugation_en_828():
    assert (
V("withdraw").t('p').pe(3).realize()   
    ) == 'withdraws',\
    'withdraw:p3'


def test_conjugation_en_829():
    assert (
V("withdraw").t('ps').realize()   
    ) == 'withdrew',\
    'withdraw:ps'


def test_conjugation_en_830():
    assert (
V("withdraw").t('pp').realize()   
    ) == 'withdrawn',\
    'withdraw:pp'


def test_conjugation_en_831():
    assert (
V("withdraw").t('pr').realize()   
    ) == 'withdrawing',\
    'withdraw:pr'


def test_conjugation_en_832():
    assert (
V("wrap").t('p').pe(3).realize()   
    ) == 'wraps',\
    'wrap:p3'


def test_conjugation_en_833():
    assert (
V("wrap").t('ps').realize()   
    ) == 'wrapped',\
    'wrap:ps'


def test_conjugation_en_834():
    assert (
V("wrap").t('pp').realize()   
    ) == 'wrapped',\
    'wrap:pp'


def test_conjugation_en_835():
    assert (
V("wrap").t('pr').realize()   
    ) == 'wrapping',\
    'wrap:pr'


def test_conjugation_en_836():
    assert (
V("write").t('p').pe(3).realize()   
    ) == 'writes',\
    'write:p3'


def test_conjugation_en_837():
    assert (
V("write").t('ps').realize()   
    ) == 'wrote',\
    'write:ps'


def test_conjugation_en_838():
    assert (
V("write").t('pp').realize()   
    ) == 'written',\
    'write:pp'


def test_conjugation_en_839():
    assert (
V("write").t('pr').realize()   
    ) == 'writing',\
    'write:pr'

