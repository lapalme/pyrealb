from pyrealb import *

from Realization.common import realize, jsrDayPeriod, jsrHour, get_max_term, get_min_term, get_term_at

precipitationTypes = {
    "showers":{"en":lambda:N("shower").n("p"), 
               "fr":lambda:N("averse").n("p")},
    "flurries":{"en":lambda:N("flurry").n("p"), 
                "fr":lambda:NP(N("averse").n("p"),PP(P("de"),N("neige")))},
    "wet-flurries":{"en":lambda:NP(A("wet"),N("flurry").n("p")), 
                    "fr":lambda:NP(N("averse").n("p"),PP(P("de"),N("neige"),A("fondant")))},
    "blizzard":{"en":lambda:N("blizzard"), 
                "fr":lambda:N("blizzard")},
    "snow-squalls":{"en":lambda:NP(N("snow"),N("squall").n("p")), 
                    "fr":lambda:NP(N("bourrasque").n("p"),PP(P("de"),N("neige")))},
    "drizzle":{"en":lambda:N("drizzle"), 
               "fr":lambda:N("bruine")},
    "freezing-drizzle" :{"en":lambda:NP(V("freeze").t("pr"),N("drizzle")), 
                         "fr":lambda:NP(N("bruine"),A("verglaçant"))},
    "ice-crystals" :{"en":lambda:NP(N("ice"),N("crystal").n("p")), 
                     "fr":lambda:NP(N("cristal").n("p"),PP(P("de"),N("glace")))},
    "hail":{"en":lambda:N("hail"), 
            "fr":lambda:N("grêle")},
    "ice-pellets":{"en":lambda:NP(N("ice"),N("pellet").n("p")), 
                   "fr":lambda:N("grésil")},
    "snow":{"en":lambda:N("snow"), 
            "fr":lambda:N("neige")},
    "wet-snow" :{"en":lambda:NP(A("wet"),N("snow")), 
                 "fr":lambda:NP(N("neige"),N("fondant"))},
    "thunderstorm":{"en":lambda:N("thunderstorm"), 
                    "fr":lambda:N("orage").n("p")},
    "rain":{"en":lambda:N("rain"), 
            "fr":lambda:N("pluie")},
    "freezing-rain":{"en":lambda:NP(V("freeze").t("pr"),N("rain")), 
                     "fr":lambda:NP(N("pluie"),A("verglaçant"))},
    "blowing-snow" :{"en":lambda:NP(V("blow").t("pr"),N("snow")), 
                     "fr":lambda:N("poudrerie")},
}

    

# chance of precipitation (COP) is expressed in increment of 10% when between 30% and 70% (but different than 50%...)
# when 80% or more, indicated beginning or ending
# precipitation amount is indicated if 
#          snow >= 2cm 
#          rain >= 25mm 

#### TODO:
# only one reference to COP except when
#          a 6 hour break in precipitation
#          two types of precipitation
#          more than 30% difference


def precipitation(wInfo,period,lang):
    jsrExprs=[]
    prob_terms=wInfo.get_precipitation_probabilities(period)
    type_terms=wInfo.get_precipitation_type(period)
    accum_terms=wInfo.get_precipitation_accumulation(period)
    for prob_term in prob_terms:
        prob_val=round(prob_term.infos[0]/10)*10
        type_term=get_term_at(type_terms,prob_term.start)
        if type_term!=None and prob_val>=30:     # interesting precipitation
            if prob_val <= 70 and prob_val!=50:  # show probability
                if lang=="en":
                    prob=NP(NO(prob_val),Q("percent"),N("chance").n("s"),P("of"))
                else:
                    prob=NP(NO(prob_val),Q("pour cent"),P("de"),N("probabilité").n("s"),P("de"))
                timePeriod=None
            else:                                # probability >= 80% 
                prob=None                        # indicate beginning or ending
                start=prob_term.start
                end=prob_term.end
                if wInfo.is_in_period(start,period):  
                    timePeriod=VP(V("begin" if lang=="en" else "débuter").t("pr"),jsrHour(start%24,lang))
                elif wInfo.is_in_period(end,period):
                    timePeriod=VP(V("end" if lang=="en" else "finir").t("pr"),jsrHour(end%24,lang))
                else:
                    timePeriod=None
            jsrExpr=NP(prob,precipitationTypes[type_term.infos[0]][lang](),timePeriod)            
            amount_term=get_term_at(accum_terms,prob_term.start)
            if amount_term!=None:                 # check for significant amount
                pcpnType=amount_term.infos[0]
                amount=amount_term.infos[1]
                jsrAmount=None
                if pcpnType=="rain" and amount>=25:
                    jsrAmount=NP(NO(round(amount)),Q("mm"))
                elif pcpnType=="snow" and amount>=2:
                    jsrAmount=NP(NO(round(amount)),Q("cm"))
                if jsrAmount!=None:
                    if lang=="en":
                        jsrAmount.add(N("amount"),0)
                    else:
                        jsrAmount.add(N("accumulation"),0).add(P("de"),1)
                    jsrExpr=SP(jsrExpr.a(","),jsrAmount)   
            jsrExprs.append(jsrExpr)
    return " ".join(realize(jsrExpr,lang) for jsrExpr in jsrExprs)

if __name__ == '__main__':
    ## exercise all precipitationTypes expressions
    for pt in precipitationTypes:
        loadEn()
        enR=realize(precipitationTypes[pt]["en"](),"en",False)
        loadFr()
        frR=realize(precipitationTypes[pt]["fr"](),"fr",False)
        print("%-20s : %-20s"%(enR,frR))
