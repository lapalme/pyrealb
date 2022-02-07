from pyrealb import *

from Realization.common import realize, jsrDayPeriod, jsrHour, get_max_term, get_min_term, get_term_at

#### UV_index values: info taken from
#  https://www.canada.ca/en/environment-climate-change/services/weather-health/uv-index-sun-safety/about.html
#      Low (0-2), Moderate (3-5), High (6-7), Very High (8-10), and Extreme (11+)
uv_ranges= [(2,   {"en":lambda:A("low"),                     "fr":lambda:A("bas")}), 
            (5,   {"en":lambda:A("moderate"),                "fr":lambda:A("modéré")}), 
            (7,   {"en":lambda:A("high"),                    "fr":lambda:A("élevé")}), 
            (10,  {"en":lambda:AP(Adv("very"), A("high")),   "fr":lambda:AP(Adv("très"),A("élevé"))}), 
            (1000,{"en":lambda:A("extreme"),                 "fr":lambda:A("extrême")})]

def uv_index(wInfo,period,lang):
    if period in ["tonight","tomorrow_night"]:      # no UV index during the night
        return None
    uvi_terms=wInfo.get_uv_index(period)
    if uvi_terms is None:return None 
    uvVal=uvi_terms[0].infos[0]                     # consider only the first uvi_term
    if uvVal<1: return None                         # too low
    uvVal=round(uvVal)
    if uvVal==0:return None
    for high,expr in uv_ranges:
        if uvVal<=high:
            return realize(NP(Q("UV index" if lang=="en" else "indice UV"),
                              NO(uvVal),C("or" if lang=="en" else "ou"),expr[lang]()),
                           lang)
    return None


if __name__ == '__main__':
    def showEnFr(jsrExprEN,jsrExprFR):
        loadEn()
        print(realize(jsrExprEN(),"en",False))
        loadFr()
        print(realize(jsrExprFR(),"fr",False))
## exercise all kinds of uv_ranges
    for i in range(0,len(uv_ranges)):
        (val,jsrEnFr)=uv_ranges[i]
        showEnFr(lambda:NP(Q("UV"),N("index"),NO(val),C("or"),jsrEnFr["en"]()),
                 lambda:NP(N("indice"),Q("UV"),NO(val),C("ou"),jsrEnFr["fr"]()))
        