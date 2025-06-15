from pyrealb import *

def uv_index(wInfo,period,lang):
    if period in ["tonight","tomorrow_night"]:      # no UV index during the night
        return None
    uvi_terms=wInfo.get_uv_index(period)
    if uvi_terms is None:return None 
    uvVal=uvi_terms[0].infos[0]                     # consider only the first uvi_term
    if uvVal<1: return None                         # too low
    uvVal=round(uvVal)
    if uvVal==0:return None
    for high,expr in lang.uv_ranges:
        if uvVal<=high:
            return S(NP(lang.uv_index,NO(uvVal),lang.or_,expr())).realize()
    return None


if __name__ == '__main__':
    ## exercise all kinds of uv_ranges
    from English import English
    from Francais import Francais
    for lang in [English(),Francais()]:
        print(f"-- {lang.code} --")
        load(lang.code)
        for (val,expr) in lang.uv_ranges:
            print(S(lang.uv_index,Q(":"),NO(val),expr()).realize())
