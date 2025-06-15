from pyrealb import *

import json,textwrap,re,os
from datetime import datetime, timedelta
from WeatherInfo import WeatherInfo

from Realization.Sky_Condition import sky_condition
from Realization.Precipitation import precipitation
from Realization.Wind import wind
from Realization.Temperature import temperature
from Realization.UV_index import uv_index
from Realization.English import English
from Realization.Francais import Francais

## each of these function return a string corresponding to a paragraph

def forecast_regions(wInfo,lang):
    return "\n".join(wInfo.get_region_names(lang.code))+"\n"

def forecast_period(wInfo,period,lang):
    sents=filter(lambda l:l is not None,[
        sky_condition(wInfo, period,lang),
        precipitation(wInfo, period,lang),
        wind(wInfo, period,lang),
        temperature(wInfo, period,lang),
        uv_index(wInfo, period,lang)
    ])
    return " ".join(sents)

def forecast_text(wInfo,lang):
    paragraphs=[]
    for period in wInfo.get_periods():
        if lang=="en" : wInfo.show_data(period)
        paragraphs.append(
            textwrap.fill(
                lang.periodNames[period](wInfo.get_issue_date()+timedelta(days=1)).cap(True).realize()
                          +" : "+forecast_period(wInfo, period, lang)
                        ,width=70,subsequent_indent=" ")
            )
    return "\n".join(paragraphs)

def generate_bulletin(wInfo,lang):
    load(lang.code)
    text=[
        lang.communication_header(wInfo),
        lang.title_block(wInfo),
        forecast_regions(wInfo,lang),
        forecast_text(wInfo,lang),
        lang.end_statement(),
    ]    
    return "\n".join(line for line in text if line is not None)

##  compare three periods only and display result and  original in parallel 
def compare_with_orig(wInfo,lang):
    load(lang.code)
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

    print(pcpn(N("flurry").n("p"),"begin","p","morning",2,N("foot")).realize())
    print(pcpn(N("rain"),"begin","p","evening",1,N("inch")).realize())
    print(pcpn(N("snow"),"stop","pr","evening").realize())
    print(pcpn(NP(V("freeze").t("pr"),N("drizzle")),"start","f","morning").realize())

compare=False
if __name__ == '__main__':
    # paperExample()
    en = English()
    fr = Francais()
    for line in open(os.path.abspath(os.path.join(os.path.dirname(__file__),"weather-data.jsonl")),"r",encoding="utf-8"):
        wInfo=WeatherInfo(json.loads(line))
        # if wInfo.data["id"]!="fpto12-2018-07-18-2000-r1209c":continue  # example used in the paper
        if compare:
            print(compare_with_orig(wInfo,en),"\n")
            print(compare_with_orig(wInfo,fr),"\n")
        else:
            print(generate_bulletin(wInfo,en),"\n")
            print(generate_bulletin(wInfo,fr),"\n")
        # break
