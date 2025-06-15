from pyrealb import *

def sky_condition(mc, period, lang):
    previous_conditions = []
    pyrExprs = []

    def addNoRepeat(c, dn, period=None):  # avoid generating same sentence twice
        if c not in previous_conditions:
            if len(lang.sky_condition_terminology[c]) == 1: dn = 0
            pyrExpr = lang.sky_condition_terminology[c][dn]()
            if period is not None: pyrExpr.add(period)
            pyrExprs.append(pyrExpr)
            previous_conditions.append(c)

    sc_terms = mc.get_sky_cover(period)
    if sc_terms is None: return None
    for sc_term in sc_terms:
        valStart = sc_term.infos[0]
        valEnd = sc_term.infos[1]
        dayNight = 0 if period in ["today", "tomorrow"] else 1
        if valStart == valEnd:
            if valStart in [0, 1]:
                addNoRepeat("c1", dayNight)
            if valStart in [2, 3]:
                addNoRepeat("c2", dayNight)
            if valStart in [4, 5, 6]:
                addNoRepeat("c3", dayNight)
            if valStart in [7, 8]:
                addNoRepeat("c4", dayNight)
            if valStart in [9]:
                addNoRepeat("c5", dayNight)
            if valStart in [10]:
                addNoRepeat("c6", dayNight)
        elif valStart in [0, 1, 2, 3] and valEnd in [7, 8, 9, 10]:
            addNoRepeat("c7", dayNight, lang.pyrDayPeriod(sc_term.start))
        elif (valStart in [7, 8, 9, 10] and valEnd in [0, 1, 2, 3]) or \
                (valStart in [5, 6] and valEnd in [0, 1]):
            addNoRepeat("c8", dayNight, lang.pyrDayPeriod(sc_term.start))
    return " ".join(S(pyrExpr).realize() for pyrExpr in pyrExprs)


if __name__ == '__main__':
    from English import English
    from Francais import Francais
    ## exercise all sky_condition_terminology expressions
    for lang in [English(),Francais()]:
        load(lang.code)
        print(f"-- {lang.code} --")
        for c,pyrExprs in lang.sky_condition_terminology.items():
                print(c,":",", ".join(pyrExpr().realize() for pyrExpr in pyrExprs))
