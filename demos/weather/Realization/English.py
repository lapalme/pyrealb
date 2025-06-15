from pyrealb import *
import datetime
dayOnly={"day":True,"year": False, "month": False, "date": False,
         "hour":False,"minute":False, "second": False, "det":False}

class English:
    def __init__(self):
        self.code="en"
        load("en")
        addToLexicon({"gust": {"N": {"tab": "n5"}, "V": {"tab": "v1"}}})
        addToLexicon({"cloudiness": {"N": {"tab": "n2"}}})
        addToLexicon({"cent": {"N": {"tab": "n1"}}})
        # used by common.py
        self.dayPeriods=[
            (0,5,lambda:NP(N("night"))),
            (5,9,lambda:NP(Adv("early"),N("morning"))),
            (9,12,lambda:NP(N("morning"))),
            (12,18,lambda:NP(N("afternoon"))),
            (18,24,lambda:NP(N("tonight")))
        ]
        self.periodNames = {
            "today":   lambda _:N("today"),
            "tonight": lambda _:N("tonight"),
            "tomorrow": lambda d:DT(d).dOpt(dayOnly),
            "tomorrow_night":lambda d:NP(DT(d).dOpt(dayOnly),N("night"))
        }

        # used by Sky_condition.py
        self.sky_condition_terminology = { ## types of sky conditions
            "c1":(lambda:AP(A("sunny")),lambda:AP(A("clear"))),
            "c2":(lambda:AP(Adv("mainly"),A("sunny")),lambda:NP(Q("a"),D("few"),N("cloud").n("p"))),
            "c3":(lambda:NP(D("a"),N("mix"),PP(P("of"),CP(C("and"),N("sun"),N("cloud").n("p")))),),
            "c4":(lambda:AP(Adv("mainly"),A("cloudy")),),
            "c5":(lambda:AP(A("cloudy")),),
            "c6":(lambda:AP(A("overcast")),),
            "c7":(lambda:NP(V("increase").t("pr"),N("cloudiness")),),
            "c8":(lambda:NP(N("clearing")),),
        }

        # used by Precipitation.py
        self.precipitationTypes = {
            "showers":lambda:N("shower").n("p"),
            "flurries":lambda:N("flurry").n("p"),
            "wet-flurries":lambda:NP(A("wet"),N("flurry").n("p")),
            "blizzard":lambda:N("blizzard"),
            "snow-squalls":lambda:NP(N("snow"),N("squall").n("p")),
            "drizzle":lambda:N("drizzle"),
            "freezing-drizzle" :lambda:NP(V("freeze").t("pr"),N("drizzle")),
            "ice-crystals" :lambda:NP(N("ice"),N("crystal").n("p")),
            "hail":lambda:N("hail"),
            "ice-pellets":lambda:NP(N("ice"),N("pellet").n("p")),
            "snow":lambda:N("snow"),
            "wet-snow" :lambda:NP(A("wet"),N("snow")),
            "thunderstorm":lambda:N("thunderstorm"),
            "rain":lambda:N("rain"),
            "freezing-rain":lambda:NP(V("freeze").t("pr"),N("rain")),
            "blowing-snow" :lambda:NP(V("blow").t("pr"),N("snow")),
        }
        self.start = V("begin")
        self.end   = V("end")

        # used by Wind.py
        ### Pubpro sec 2.3.4
        ## vents : start end direction modif? speed value exception?
        # e | nil | n | ne | nw | w | ely | nly | nely | nwly | wly | sly| sely | swly | sly | sely | sw | vrbl
        self.pyrWindDirection = {
            "e":    lambda:Adv("east"),
            "n":    lambda:Adv("north"),
            "ne":   lambda:Adv("northeast"),
            "nw":   lambda:Adv("northwest"),
            "w":    lambda:Adv("west"),
            "ely":  lambda:Adv("easterly"),
            "nly":  lambda:Adv("northerly"),
            "nely": lambda:A("northeasterly"),
            "nwly": lambda:A("northwesterly"),
            "wly":  lambda:Adv("westerly"),
            "sly":  lambda:Adv("southerly"),
            "sely": lambda:A("southeasterly"),
            "swly": lambda:A("southwesterly"),
            "se":   lambda:Adv("southeast"),
            "s":    lambda:Adv("south"),
            "sw":   lambda:Adv("southwest"),
        }

        # used by Temperature.py
        self.high = Adv("high")
        self.low  = Adv("low")
        # used by UV_index.py
        self.uv_index = Q("UV index")
        self.or_ = C("or")

        #### UV_index values: info taken from
        #  https://www.canada.ca/en/environment-climate-change/services/weather-health/uv-index-sun-safety/about.html
        #      Low (0-2), Moderate (3-5), High (6-7), Very High (8-10), and Extreme (11+)
        self.uv_ranges = [(2, lambda: A("low")),
                          (5, lambda: A("moderate")),
                          (7, lambda: A("high")),
                          (10, lambda: AP(Adv("very"), A("high"))),
                          (1000, lambda: A("extreme"))]


    #### end of English constructor

    # used by common.py
    def pyrHour(self,h):
        h = h % 24
        if 0 <= h <6:
            return PP(P("during"), NP(D("the"), N("night")))
        if 6 <= h < 11:
            return PP(P("in"), NP(D("the"), N("morning")))
        if 11 <= h < 14:
            return PP(P("around"), N("noon"))
        if 14 <= h < 18:
            return PP(P("in"), NP(D("the"), N("afternoon")))
        if 18 <= h < 24:
            return PP(P("in"), NP(D("the"), N("evening")))

    def pyrDayPeriod(self,hour):
        isTomorrow = hour > 23
        hour = hour % 24
        for (s, e, pyrExp) in self.dayPeriods:
            if s <= hour < e:
                exp = pyrExp()
                if isTomorrow:
                    return exp.add(N("tomorrow"),
                                   1 if s == 5 else 0)
                return (N("tonight") if s == 18 else exp.add(D("this"), 0))

    # used by precipitation.py
    def probability(self, prob_val):
        return NP(NO(prob_val),Q("percent"),N("chance").n("s"),P("of"))

    def amount(self, pyrAmount):
        return pyrAmount.add(N("amount"), 0)

    # used by Wind.py
    def significant_speed_change(self,wSpeed):
        return VP(V("increase").t("pr"),PP(P("to"),NO(wSpeed)))

    def significant_direction_change(self,wDir):
        return VP(V("become").t("pr"),self.pyrWindDirection[wDir]())

    def wind_speed_dir(self,wSpeed,wDir):
        return NP(N("wind"),self.pyrWindDirection[wDir](),NO(wSpeed),Q("km/h"))


    def wind_gust(self,gust):
        return VP(V("gust").t("pr"),PP(P("to"),NO(gust.infos[1])))

    # used by Temperature.py
    def pyrTemp(self,val):
        if val == 0: return N("zero")
        if val < 0: return AdvP(A("minus"), NO(abs(val)))
        if val <= 5: return AP(A("plus"), NO(val))
        return NO(val)

    def temp_trend(self, trend, goalTemp, when):
        return S(N("temperature"),
                VP(V(trend).t("pr"),
                   PP(P("to"),self.pyrTemp(goalTemp)),when))

    def pyrAbnormal(self,dn,kind):
        if dn == "night":
            if kind == "a": return lambda t,_:self.temp_trend("rise",t,PP(P("by"),N("morning")))
            if kind == "b": return lambda t,u:S(Adv("low"),u.a(","),P("with"),self.temp_trend("rise",t,PP(P("by"),
                                                                                                   N("morning"))))
            if kind == "c": return lambda t,p:self.temp_trend("rise",t,p).add(AdvP(Adv("then"),A("steady")))
            if kind == "d": return lambda t,p:self.temp_trend("rise",t,p).add(AdvP(Adv("then"),V("rise").t("pr"),Adv("slowly")))
            if kind == "e": return lambda t,p:self.temp_trend("rise",t,p).add(AdvP(Adv("then"),V("fall").t("pr")))
        if dn == "day":
            if kind == "a": return lambda t,_:self.temp_trend("fall",t,PP(P("by"),N("afternoon")))
            if kind == "b": return lambda t,u:S(Adv("high"),u.a(","),P("with"),self.temp_trend("fall",t,PP(P("by"),N("afternoon"))))
            if kind == "c": return lambda t,p:self.temp_trend("fall",t,p).add(AdvP(Adv("then"),A("steady")))
            if kind == "d": return lambda t,p:self.temp_trend("fall",t,p).add(AdvP(Adv("then"),V("fall").t("pr"),Adv("slowly")))
            if kind == "e": return lambda t,p:self.temp_trend("fall",t,p).add(AdvP(Adv("then"),V("rise").t("pr")))
        print("*** pyrAbnormal: bad parameters:",dn,kind)

    #
    #  filler for line alignment with Francais.py
    #


    # used by Bulletin.py
    def title_block(self, wInfo):
        issueDate = wInfo.get_issue_date()
        noSecond = {"second": False}
        s1=S(NP(N("forecast").n("p")),
             VP(V("issue").t("pp"),
                PP(P("by"),Q("pyrealb"),
                   DT(issueDate).dOpt(noSecond),
                   P("for"),CP(C("and"),
                               N("today"),
                               DT(issueDate+datetime.timedelta(days=1)).dOpt({"rtime":issueDate})))))
        s2=S(NP(D("the"),D("next"),V("schedule").t("pp"),N("forecast").n("p")),
             VP(V("be").t("f"),V("issue").t("pp"),
                DT(wInfo.get_next_issue_date()).dOpt(noSecond)))
        return "\n".join([s1.realize(), s2.realize()])

    def communication_header(self, wInfo):
        return "WEATHER BULLETIN: %s"%wInfo.get_header()[0]

    def end_statement(self):
        return "END"

if __name__ == '__main__':
    lang = English()
    for h in range(1, 40, 3):
        print(" %2d : %s : %s" % (h, lang.pyrHour(h).realize(),
                                  lang.pyrDayPeriod(h).realize()))
