from pyrealb import *
import datetime
dayOnly={"day":True,"year": False, "month": False, "date": False,
         "hour":False,"minute":False, "second": False, "det":False}

class Francais:
    def __init__(self):
        self.code = "fr"
        load("fr")
        addToLexicon("ennuagement",{"N":{"g":"m","tab":"n3"}})
        addToLexicon("verglaçant",{"A":{"tab":"n28"}})

        # used by common.py
        self.dayPeriods=[
            (0,5,lambda:NP(N("nuit"))),
            (5,9,lambda:PP(P("en"),NP(N("début"),PP(P("de"),N("matinée"))))),
            (9,12,lambda:NP(N("matin"))),
            (12,18,lambda:NP(N("après-midi"))),
            (18,24,lambda:NP(N("soir")))
        ]
        self.periodNames = {
            "today":lambda _:Adv("aujourd'hui"),
            "tonight":lambda _:CP(C("et"),NP(D("ce"),N("soir")),NP(D("ce"),N("nuit"))),
            "tomorrow":lambda d:DT(d).dOpt(dayOnly),
            "tomorrow_night":lambda d:CP(C("et"),NP(DT(d).dOpt(dayOnly),N("soir")),NP(N("nuit")))
        }

        # types of sky conditions
        self.sky_condition_terminology = {
            "c1":(lambda:AP(A("ensoleillé")),lambda:AP(A("dégagé"))),
            "c2":(lambda:AP(Adv("généralement"),A("ensoleillé")),lambda:NP(D("quelque"),N("nuage").n("p"))),
            "c3":(lambda:NP(N("alternance"),CP(C("et"),PP(P("de"),N("soleil")),PP(P("de"),N("nuage").n("p")))),
                  lambda:AP(Adv("partiellement"),A("couvert"))),
            "c4":(lambda:AP(Adv("généralement"),A("nuageux")),),
            "c5":(lambda:AP(A("nuageux")),),
            "c6":(lambda:AP(A("couvert")),),
            "c7":(lambda:NP(N("ennuagement")),),
            "c8":(lambda:NP(N("dégagement")),),
        }
        # used by Precipitation.py
        self.precipitationTypes = {
            "showers":lambda:N("averse").n("p"),
            "flurries":lambda:NP(N("averse").n("p"),PP(P("de"),N("neige"))),
            "wet-flurries":lambda:NP(N("averse").n("p"),PP(P("de"),NP(N("neige"),A("fondant")))),
            "blizzard":lambda:N("blizzard"),
            "snow-squalls":lambda:NP(N("bourrasque").n("p"),PP(P("de"),N("neige"))),
            "drizzle":lambda:N("bruine"),
            "freezing-drizzle" :lambda:NP(N("bruine"),A("verglaçant")),
            "ice-crystals" :lambda:NP(N("cristal").n("p"),PP(P("de"),N("glace"))),
            "hail":lambda:N("grêle"),
            "ice-pellets":lambda:N("grésil"),
            "snow":lambda:N("neige"),
            "wet-snow" :lambda:NP(N("neige"),A("fondant")),
            "thunderstorm":lambda:N("orage").n("p"),
            "rain":lambda:N("pluie"),
            "freezing-rain":lambda:NP(N("pluie"),A("verglaçant")),
            "blowing-snow" :lambda:N("poudrerie"),
        }
        self.start = V("débuter")
        self.end   = V("finir")

        # used by Wind.py
        # ### Pubpro sec 2.3.4
        ## vents : start end direction modif? speed value exception?
        # e | nil | n | ne | nw | w | ely | nly | nely | nwly | wly | sly| sely | swly | sly | sely | sw | vrbl
        self.pyrWindDirection = {
            "e":    lambda:NP(D("le"),N("est")),
            "n":    lambda:NP(D("le"),N("nord")),
            "ne":   lambda:NP(D("le"),N("nord-est")),
            "nw":   lambda:NP(D("le"),N("nord-ouest")),
            "w":    lambda:NP(D("le"),N("ouest")),
            "ely":  lambda:NP(D("le"),N("secteur"),N("est")),
            "nly":  lambda:NP(D("le"),N("secteur"),N("nord")),
            "nely": lambda:NP(D("le"),N("secteur"),N("nord-est")),
            "nwly": lambda:NP(D("le"),N("secteur"),N("nord-ouest")),
            "wly":  lambda:NP(D("le"),N("secteur"),N("ouest")),
            "sly":  lambda:NP(D("le"),N("secteur"),N("sud")),
            "sely": lambda:NP(D("le"),N("secteur"),N("sud-est")),
            "swly": lambda:NP(D("le"),N("secteur"),N("sud-ouest")),
            "se":   lambda:NP(D("le"),N("sud-est")),
            "s":    lambda:NP(D("le"),N("sud")),
            "sw":   lambda:NP(D("le"),N("sud-ouest")),
        }

        # used by Temperature.py
        self.high = N("maximum")
        self.low  = N("minimum")
        # used by UV_index.py
        self.uv_index = Q("indice UV")
        self.or_ = C("ou")

        #### UV_index values: info taken from
        #  https://www.canada.ca/en/environment-climate-change/services/weather-health/uv-index-sun-safety/about.html
        #      Low (0-2), Moderate (3-5), High (6-7), Very High (8-10), and Extreme (11+)
        self.uv_ranges = [(2, lambda: A("bas")),
                          (5, lambda: A("modéré")),
                          (7, lambda: A("élevé")),
                          (10, lambda: AP(Adv("très"), A("élevé"))),
                          (1000, lambda: A("extrême"))]


   #### end of Francais constructor

    # used by common.py
    def pyrHour(self,h):
        h = h % 24
        if h in range(0, 6):
            return PP(P("durant"), NP(D("le"), N("nuit")))
        if h in range(6, 11):
            return NP(D("le"), N("matin"))
        if h in range(11, 14):
            return PP(P("vers"), N("midi"))
        if h in range(14, 18):
            return PP(P("durant"), NP(D("le"), N("après-midi")))
        if h in range(18, 24):
            return PP(P("dans"), NP(D("le"), N("soirée")))

    def pyrDayPeriod(self,hour):
        isTomorrow = hour > 23
        hour = hour % 24
        for (s, e, pyrExp) in self.dayPeriods:
            if s <= hour < e:
                exp = pyrExp()
                if isTomorrow:
                    if s == 0 : return NP(D("le"),N("nuit"),A("prochain"))
                    return exp.add(N("demain"),0)   # e.g demain matin, demain soir...
                return exp.add(D("ce"),1 if s== 5 else 0)

    # used by precipitation.py
    def probability(self,prob_val):
        return NP(NO(prob_val),Q("pour cent"),P("de"),N("probabilité").n("s"),P("de"))

    def amount(self,pyrAmount):
        return pyrAmount.add(N("accumulation"),0).add(P("de"),1)

    # used by Wind.py
    def significant_speed_change(self, wSpeed):
        return VP(V("augmenter").t("pr"),PP(P("à"),NO(wSpeed)))

    def significant_direction_change(self, wDir):
        return VP(V("devenir").t("pr"), PP(P("de"),self.pyrWindDirection[wDir]()))

    def wind_speed_dir(self, wSpeed, wDir):
        return NP(N("vent").n("p"),PP(P("de"),self.pyrWindDirection[wDir]()),
                                   PP(P("de"),NO(wSpeed),Q("km/h")))

    def wind_gust(self, gust):
        return PP(P("avec"),NP(N("rafale").n("p"),P("à"),NO(gust.infos[1])))

    # used by Temperature.py
    def pyrTemp(self,val):
        if val == 0: return N("zéro")
        if val < 0: return AdvP(Adv("moins"), NO(abs(val)))
        if val <= 5: return AdvP(Adv("plus"), NO(val))
        return NO(val)

    def temp_trend(self, trend, goalTemp, when):
        return S(NP(N("température").n("p"),
                    PP(P("à"),NP(D("le"),N(trend)))),
                    PP(P("pour"),V("atteindre").t("b"),self.pyrTemp(goalTemp),when))

    def pyrAbnormal(self,dn,kind):
        if dn == "night":
            if kind == "a": return lambda t,_:self.temp_trend("hausse",t,PP(P("en"),N("matinée")))
            if kind == "b": return lambda t,u:S(N("minimum"),u.a(","),self.temp_trend("hausse",t,PP(P("en"),N("matinée"))))
            if kind == "c": return lambda t,p:self.temp_trend("hausse",t,p).add(PP(P("pour"),Adv("ensuite"),
                                                                         V("demeurer").t("b"),A("stable")))
            if kind == "d": return lambda t,p:self.temp_trend("hausse",t,p).add(NP(C("puis"),(N("hausse"),A("graduel"))))
            if kind == "e": return lambda t,p:self.temp_trend("hausse",t,p).add(PP(P("pour"),Adv("ensuite"),
                                                                         V("être").t("b"),PP(P("à"),
                                                                                             NP(D("le"),N("baisse")))))
        if dn == "day":
            if kind == "a": return lambda t,_:self.temp_trend("baisse",t,PP(P("en"),N("après-midi")))
            if kind == "b": return lambda t,u:S(N("maximum"),u.a(","),self.temp_trend("baisse",t,PP(P("en"),N("après-midi"))))
            if kind == "c": return lambda t,p:self.temp_trend("baisse",t,p).add(PP(P("pour"),Adv("ensuite"),
                                                                         V("demeurer").t("b"),A("stable")))
            if kind == "d": return lambda t,p:self.temp_trend("baisse",t,p).add(NP(C("puis"),N("baisse"),A("graduel")))
            if kind == "e": return lambda t,p:self.temp_trend("baisse",t,p).add(PP(P("pour"),Adv("ensuite"),
                                                                         V("être").t("b"),PP(P("à"),
                                                                                             NP(D("le"),N("hausse")))))
        print("*** pyrAbnormal: mauvais paramètres:", dn, kind)

    # used by Bulletin.py
    def title_block(self,wInfo):
        issueDate = wInfo.get_issue_date()
        noSecond = {"second": False}
        s1 = S(NP(N("prévision").n("p")),
               VP(V("émettre").t("pp"),
                  PP(P("par"), Q("pyrealb"),
                     DT(issueDate).dOpt(noSecond),
                     P("pour"), CP(C("et"),
                                   Adv("aujourd'hui"),
                                   DT(issueDate + datetime.timedelta(days=1)).dOpt({"rtime": issueDate})))))
        s2 = S(NP(D("le"), A("prochain").pos("pre"), N("prévision").n("p")),
               VP(V("être").t("f"), V("émettre").t("pp"),
                  DT(wInfo.get_next_issue_date()).dOpt(noSecond)))
        return "\n".join([s1.realize(),s2.realize()])

    def communication_header(self, wInfo):
        return "BULLETIN MÉTÉOROLOGIQUE: %s" % (wInfo.get_header()[0].replace("regular", "régulier"))

    def end_statement(self):
        return "FIN"

if __name__ == '__main__':
    lang = Francais()
    for h in range(1, 40, 3):
        print(" %2d : %s : %s" % (h, lang.pyrHour(h).realize(),
                                  lang.pyrDayPeriod(h).realize()))
