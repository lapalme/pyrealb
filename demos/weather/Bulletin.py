from pyrealb import *

import json,textwrap,re,os
from datetime import datetime, timedelta
from WeatherInfo import WeatherInfo

from Realization.common import realize, periodNames
from Realization.Title_Block import title_block
from Realization.Sky_Condition import sky_condition
from Realization.Precipitation import precipitation
from Realization.Wind import wind
from Realization.Temperature import temperature
from Realization.UV_index import uv_index

## each of these function return a string corresponding to a paragraph

def communication_header(wInfo,lang):
    if lang=="en":
        return "WEATHER BULLETIN: %s"%wInfo.get_header()[0]
    else:
        return "BULLETIN MÉTÉOROLOGIQUE: %s"%(wInfo.get_header()[0].replace("regular","régulier"))

def forecast_regions(wInfo,lang):
    return "\n".join(wInfo.get_region_names(lang))+"\n"

def forecast_period(wInfo,period,lang):
    sents=filter(lambda l:l is not None,[
        sky_condition(wInfo, period, lang),
        precipitation(wInfo, period, lang),
        wind(wInfo, period, lang),
        temperature(wInfo, period, lang),
        uv_index(wInfo, period, lang)
    ])
    return " ".join(sents)

def forecast_text(wInfo,lang):
    paragraphs=[]
    for period in wInfo.get_periods():
        if lang=="en" : wInfo.show_data(period)
        paragraphs.append(
            textwrap.fill(
                realize(periodNames[period][lang](wInfo.get_issue_date()+timedelta(days=1)).cap(True),lang,False)
                          +" : "+forecast_period(wInfo, period, lang)
                        ,width=70,subsequent_indent=" ")
            )
    return "\n".join(paragraphs)

def end_statement(lang):
    return "END" if lang=="en" else "FIN"

def generate_bulletin(wInfo,lang):
    if lang=="en": loadEn()
    else: loadFr()
    text=[
        communication_header(wInfo,lang),
        title_block(wInfo,lang),
        forecast_regions(wInfo,lang),
        forecast_text(wInfo,lang),
        end_statement(lang),
    ]    
    return "\n".join(line for line in text if line is not None)

##  compare three periods only and display result and  original in parallel 
def compare_with_orig(wInfo,lang):
    if lang=="en": loadEn()
    else: loadFr()
    origB=wInfo.get_ref_bulletin(lang)
    periodSplitRE=re.compile(r"\n(?=[A-Z][-' A-Za-z]+ : )")
    genB = periodSplitRE.split(forecast_text(wInfo,lang))
    genB.insert(0,forecast_regions(wInfo,lang))
    ### output comparison with original
    
    fmt="%-72s|%s"
    res=[fmt%("*** Generated ***" if lang=="en" else "*** Généré ***",
              "*** Original ***")]
    for gen,orig in zip(genB,periodSplitRE.split(origB)):
        genL=gen.split("\n")
        origL=orig.split("\n")
        lg=len(genL)
        lo=len(origL)
        for i in range(0,min(lg,lo)):
            res.append(fmt%(genL[i],origL[i]))
        if lg<lo:
            for i in range(lg,lo):
                res.append(fmt%("",origL[i]))
        elif lg>lo:
            for i in range(lo,lg):
                res.append(fmt%(genL[i],""))
    return "\n"+"\n".join(res)

def paperExample():
    ##  example function used in the paper
    def pcpn(type,action,tense,moment,quantity=None,unit=None):
        return S(type,
                 VP(V(action).t(tense),
                    CP(PP(P("in"),NP(D("the"),N(moment))),
                       None if quantity is None else NP(N("amount"),NP(NO(quantity),unit)))))
    
    print(realize(pcpn(N("flurry").n("p"),"begin","p","morning",2,N("foot")),"en"))
    print(realize(pcpn(N("rain"),"begin","p","evening",1,N("inch")),"en"))
    print(realize(pcpn(N("snow"),"stop","pr","evening"),"en"))
    print(realize(pcpn(NP(V("freeze").t("pr"),N("drizzle")),"start","f","morning"),"en"))

def weatherLexicon():
    loadFr()
    addToLexicon("ennuagement",{"N":{"g":"m","tab":"n3"}})
    addToLexicon("verglaçant",{"A":{"tab":"n28"}})
    
    loadEn()
    addToLexicon({"gust":{"N":{"tab":"n5"},"V":{"tab":"v1"}}})
    addToLexicon({"cloudiness":{"N":{"tab":"n2"}}})
    addToLexicon({"cent":{"N":{"tab":"n1"}}})

compare=False
if __name__ == '__main__':
    # paperExample()
    weatherLexicon()
    for line in open(os.path.abspath(os.path.join(os.path.dirname(__file__),"weather-data.jsonl")),"r",encoding="utf-8"):
        wInfo=WeatherInfo(json.loads(line))
        # if wInfo.data["id"]!="fpto11-2019-01-26-1600-r1116d":continue
        if compare:
            print(compare_with_orig(wInfo,"en"),"\n")
            print(compare_with_orig(wInfo,"fr"),"\n")
        else:
            print(generate_bulletin(wInfo,"en"),"\n")
            print(generate_bulletin(wInfo,"fr"),"\n")
        # break
