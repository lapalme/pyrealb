from pyrealb import *

from Realization.common import get_max_term, get_min_term, get_term_at

def temperature(wInfo,period,lang):
    temperature_terms=wInfo.get_temperature(period)
    if temperature_terms is None : return None
    maxTemp=get_max_term(temperature_terms,0).infos[0]
    minTemp=get_min_term(temperature_terms,0).infos[0]
    dn= "night" if period in ["tonight","tomorrow_night"] else "day"
    tempVals=wInfo.get_temperature_values(period)
    periodName=lang.periodNames[period](wInfo.get_issue_date())
    # checking for an abnormal temperature trend, either
    #     positive change of least 3°C during the night
    #     negative change of last 3°C during the day
    (t1,t2,i1)=(maxTemp,minTemp,tempVals.index(minTemp)) if dn=="night" else\
               (minTemp,maxTemp,tempVals.index(maxTemp))
    # print("dn=",dn,"t1=",t1,"t2=",t2)
    if t1 >= t2+3:                       # abnormal change time
        if i1 <=1 :
            return lang.pyrAbnormal(dn,"a")(t1, periodName).realize()
        else:
            if i1 < 6:        # abnormality occurs during the first 6 hours of the period
                rest=tempVals[i1:]
                if all([abs(t-t1)<=2 for t in rest]):
                    # c) remains +/- 2 for the rest of the period
                    return lang.pyrAbnormal(dn,"c")(t1,periodName).realize()
                elif any([t-t1>2 for t in rest]):
                    # d) rises more than 2 for the rest 
                    return lang.pyrAbnormal(dn,"d")(t1,periodName).realize()
                elif any([t1-t>2 for t in rest]):
                    # e) falls more than 2 for the rest (this should never happen!!!)
                    return lang.pyrAbnormal(dn,"e")(t1,periodName).realize()
            else:
                # b) low temperature after the beginning (but no special case)
                return lang.pyrAbnormal(dn,"b")(t1,lang.pyrTemp(t2)).realize()
    # normal case 
    res=[S(lang.high,lang.pyrTemp(maxTemp)).realize()]   # output maximum temperature
    if minTemp < maxTemp-2:             # output minimum if it differs significantly from the maximum
        res.append(S(lang.low,lang.pyrTemp(minTemp)).realize())
    return " ".join(res)

if __name__ == '__main__':
    ## exercise all abnormal messages
    from English import English
    from Francais import Francais
    for lang in [English(),Francais()]:
        print(f"-- {lang.code} --")
        load(lang.code)
        for dn in ["night","day"]:
            for kind in "abcde":
                if kind == "b":
                    print(dn,kind,":",lang.pyrAbnormal(dn,kind)(3,NO(8)).realize())
                else:
                    print(dn,kind,":",lang.pyrAbnormal(dn,kind)(4,Adv("today" if lang.code=="en" else
                                                                      "aujourd'hui")).realize())