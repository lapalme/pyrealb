from pyrealb import *

### Pubpro sec 2.3.4
## vents : start end direction modif? speed value exception?
# e | nil | n | ne | nw | w | ely | nly | nely | nwly | wly | sly| sely | swly | sly | sely | sw | vrbl
pyrWindDirection = {
    "e":    90,
    "n":    0,
    "ne":   45,
    "nw":   315,
    "w":    290,
    "ely":  90,
    "nly":  0,
    "nely": 45,
    "nwly": 315,
    "wly":  270,
    "sly":  180,
    "sely": 135,
    "swly": 225,
    "se":   135,
    "s":    180,
    "sw":   225,
}


# find the difference between compass directions 
# adapted from https://www.mrexcel.com/board/threads/compass-direction-differences.213199
def dir_diff(dir1,dir2):
    dir1=pyrWindDirection[dir1]
    dir2=pyrWindDirection[dir2]
    if dir1 >180 : dir1-=180
    else: dir1+=180
    if dir2 >180 : dir2-=180
    else: dir2+=180
    return abs(dir1-dir2)

def wind(wInfo,period,lang):
    wind_terms=wInfo.get_wind(period)
    if wind_terms is None:return None
    lastSpeed=None 
    lastDir=None
    pyrExprs=[]
    for wind_term in wind_terms:
        wSpeed = wind_term.infos[2]
        wDir= wind_term.infos[0]
        pyrExpr=S()                                           # current expression
        if wSpeed>=15 and wDir in lang.pyrWindDirection:
            if lastSpeed is not None and abs(wSpeed-lastSpeed)>=20: # significant speed change
                lastSpeed=wSpeed
                pyrExpr.add(lang.significant_speed_change(wSpeed))
            elif lastDir is not None and dir_diff(wDir, lastDir):  # significant direction change
                pyrExpr.add(lang.significant_direction_change(wDir))
                lastDir=wDir
            else:                                            # realize wind and direction
                lastSpeed=wSpeed
                lastDir=wDir
                pyrExpr.add(lang.wind_speed_dir(wSpeed,wDir))
            if len(wind_term.infos)>3:                       # add gusting information
                gust=wind_term.infos[3]
                if gust.infos[0]=='gust':
                    pyrExpr.add(lang.wind_gust(gust))
            else:                                           # add time information
                pyrExpr.add(lang.pyrHour(wind_term.start))
            pyrExprs.append(pyrExpr)                        # add current expression to the list
    return " ".join(S(pyrExpr).realize() for pyrExpr in pyrExprs)


if __name__ == '__main__':
    from English import English
    from Francais import Francais
    for lang in [English(),Francais()]:
        load(lang.code)
        for wd in pyrWindDirection:
            if lang.code == "en":
                print(wd,":",NP(lang.pyrWindDirection[wd](),N("wind")).realize())
            else:
                print(wd,":",NP(N("vent").n("p"),PP(P("de"),lang.pyrWindDirection[wd]())).realize())
        