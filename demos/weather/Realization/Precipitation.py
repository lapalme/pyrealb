from pyrealb import *

from Realization.common import get_term_at

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


def precipitation(wInfo, period, lang):
    pyrExprs = []
    prob_terms = wInfo.get_precipitation_probabilities(period)
    type_terms = wInfo.get_precipitation_type(period)
    accum_terms = wInfo.get_precipitation_accumulation(period)
    for prob_term in prob_terms:
        prob_val = round(prob_term.infos[0] / 10) * 10
        type_term = get_term_at(type_terms, prob_term.start)
        if type_term != None and prob_val >= 30:  # interesting precipitation
            if prob_val <= 70 and prob_val != 50:  # show probability
                prob = lang.probability(prob_val)
                timePeriod = None
            else:  # probability >= 80%
                prob = None  # indicate beginning or ending
                start = prob_term.start
                end = prob_term.end
                if wInfo.is_in_period(start, period):
                    timePeriod = VP(lang.start.t("pr"), lang.pyrHour(start % 24))
                elif wInfo.is_in_period(end, period):
                    timePeriod = VP(lang.end.t("pr"), lang.pyrHour(end % 24))
                else:
                    timePeriod = None
            pyrExpr = NP(prob, lang.precipitationTypes[type_term.infos[0]](), timePeriod)
            amount_term = get_term_at(accum_terms, prob_term.start)
            if amount_term != None:  # check for significant amount
                pcpnType = amount_term.infos[0]
                amount = amount_term.infos[1]
                pyrAmount = None
                if pcpnType == "rain" and amount >= 25:
                    pyrAmount = NP(NO(round(amount)), Q("mm"))
                elif pcpnType == "snow" and amount >= 2:
                    pyrAmount = NP(NO(round(amount)), Q("cm"))
                if pyrAmount != None:
                    pyrAmount = lang.amount(pyrAmount)
                    pyrExpr = SP(pyrExpr.a(","), pyrAmount)
            pyrExprs.append(pyrExpr)
    return " ".join(S(pyrExpr).realize() for pyrExpr in pyrExprs)


if __name__ == '__main__':
    ## exercise all precipitationTypes expressions
    from English import English
    from Francais import Francais
    realisations = {"en":[],"fr":[]}
    for lang in [English(),Francais()]:
        load(lang.code)
        for pt,pyrExp in lang.precipitationTypes.items():
            realisations[lang.code].append(pyrExp().realize())
    for (code,en,fr) in zip(lang.precipitationTypes.keys(),
                            realisations["en"],
                            realisations["fr"]):
        print("%-15s: %-15s : %s"%(code,en,fr) )

