---
title: Generation of weather bulletins in French and English
author: Guy Lapalme
description: Realize French and English weather bulletins from MeteoCode in the style of Environment Canada
keywords: text generation, weather bulletin, French, English
---

<center style="font-size:3em; font-family: 'Open Sans'; font-weight: bold">Generation of weather bulletins in French and English</center>
<center><a href="mailto:lapalme@iro.umontreal.ca">Guy Lapalme</a><br/>RALI-DIRO<br/>Université de Montréal<br/>June 2025</center>


This a _pure Python version_ of the [jsRealB Weather demo](https://github.com/rali-udem/jsRealB/tree/master/demos/Weather)

# Context of the application

The input of the application is set of meteorological information (e.g., precipitations, temperature, wind, UV index, ...) provided by [Environment and Climate Change Canada](https://www.canada.ca/en/environment-climate-change.html "Environment and Climate Change Canada - Canada.ca") (ECCC). Unlike usual data-to-text applications, this information is machine generated: it is created by a numerical weather model which outputs data for ranges of hours after the time the bulletin is expected to be issued. ECCC emits three _regular_ bulletins each day (morning, midday and evening) for hundreds of regions of Canada. A bulletin gives the predictions for the current day or evening and the next day. These bulletins are generated in both English and French.

For the purpose of this demo, we extracted a subset of the global information for regions of Ontario and Québec for 2018 and 2019 which is nevertheless illustrative of the natural language generation problems encountered in this context. We converted the Meteocode, an internal data format of ECCC, to [JSON](https://www.json.org/json-en.html "JSON") in which time indications are _shifted_, so that they appear in local time while, in the original, they were in UTC.

For example, given this input in JSON:

```json
{
 "id":"fpto12-2018-07-18-2000-r1209c",
 "fr":"Armstrong - Auden - parc Wabakimi\n... original bulletin in French",
 "en":"Armstrong - Auden - Wabakimi Park\n... original bulletin in English",
 "header":["regular","2018-07-18T16:00:00","next","2018-07-19T05:30:00"],
 "names-en":["Armstrong - Auden - Wabakimi Park","Nakina - Aroland - Pagwa"],
 "names-fr":["Armstrong - Auden - parc Wabakimi","Nakina - Aroland - Pagwa"],
 "sky-cover":[[-58,-52,8,8], [-52,-49,8,2], [-49,-39,2,2], [-39,-35,2,9], [-35,-21,9,9], [-21,-17,8,8], [-17,-14,8,2], [-14,-5,7,7], [-5,-1,7,1], [-1,18,1,1], [18,20,3,3], [20,29,5,5], [29,35,2,2], [35,39,2,8], [39,42,8,8], [42,48,8,8], [48,54,7,7]],
 "temperatures":[[-55,-52,24], [-52,-49,21], [-49,-46,17], [-46,-43,16], [-43,-40,18], [-40,-37,20], [-37,-34,22], [-34,-31,21], [-31,-28,18], [-28,-25,14], [-25,-22,12], [-22,-19,10], [-19,-16,12], [-16,-13,15], [-13,-10,17], [-10,-7,20], [-7,-4,18], [-4,-1,15], [-1,2,11], [2,5,6], [5,8,12], [8,11,20], [11,14,26], [14,16,26], [16,18,28], [18,20,26], [20,23,20], [23,26,14], [26,29,14], [29,32,15], [32,35,23], [35,38,28], [38,41,25], [41,44,23], [44,47,18], [47,50,15], [50,53,14], [53,56,15], [56,59,19], [59,62,23], [62,65,23], [65,68,20], [68,71,18], [71,74,16], [74,77,15], [77,80,16], [80,83,17], [83,86,22], [86,89,24], [89,92,21], [92,95,17], [95,98,13], [98,101,10], [101,104,12], [104,107,18], [107,110,23], [110,113,25], [113,116,22], [116,119,17], [119,122,13], [122,125,11], [125,128,13], [128,131,18], [131,134,22], [134,137,22], [137,140,20], [140,143,17], [143,146,14], [146,149,13], [149,152,13], [152,155,17], [155,158,20], [158,161,21], [161,164,19], [164,167,16], [167,170,13], [170,173,11], [173,176,11], [176,179,16], [179,182,19], [182,185,21], [185,188,19], [188,191,15], [191,194,11], [194,197,10], [197,200,11], [200,203,17], [203,206,21], [206,209,24], [209,212,20], [212,215,16], [215,218,13], [218,221,11], [221,224,13]],
 "precipitation-type":[[-35, -21, "showers", [-27,-21,"thunderstorm"]], [-21,-17,"drizzle"], [20, 29, "showers", [20,29,"thunderstorm"]], [39, 48, "showers", [39,48,"thunderstorm"]]],
 "precipitation-accumulation":[[56,59,"rain",2], [59,62,"rain",4], [62,65,"rain",3], [65,68,"rain",6], [68,71,"rain",3], [71,74,"rain",1,2], [74,77,"rain",0,1], [77,80,"rain",1,2]],
 "precipitation-probability":[[-54,-35,0], [-35,-21,80], [-21,-17,30], [-17,15,0], [15,20,10], [20,29,30], [29,39,10], [39,42,30], [42,48,30], [48,54,20]],
 "wind":[[-60,-51,"sw","speed",20], [-51,-45,"sw","speed",15], [-45,-36,"sw","speed",10], [-36,-30,"w","speed",20], [-30,-27,"nw","speed",20], [-27,-24,"nw","speed",15], [-24,-6,"n","speed",15], [-6,0,"nw","speed",10], [0,9,"nil","speed",5], [9,12,"sw","speed",10], [12,20,"w","speed",20], [20,24,"sw","speed",15], [24,36,"sw","speed",10], [36,44,"sw","speed",20], [44,48,"sw","speed",10], [48,56,"nil","speed",5], [56,59,"nil","speed",5], [59,68,"ne","speed",20], [68,77,"ne","speed",15], [77,86,"n","speed",20], [86,95,"ne","speed",15], [95,110,"n","speed",10], [110,122,"ne","speed",10], [122,146,"se","speed",10], [146,152,"w","speed",10], [152,197,"nw","speed",10], [197,203,"w","speed",10], [203,215,"nw","speed",10], [215,224,"w","speed",10]]
 "uv-index":[[-36,-34,6.3], [-12,-10,6.7], [12,14,7.2], [36,38,7.7]],
}
```

here is the evening bulletin realized by **pyrealb** in English and French.

    WEATHER BULLETIN: regular
    Forecasts issued by pyrealb on Wednesday, July 18, 2018 at 4 p.m. for today and tomorrow at 4 p.m.
    The next scheduled forecasts will be issued on Thursday, July 19, 2018 at 5:30 a.m.
    Armstrong - Auden - Wabakimi Park
    Nakina - Aroland - Pagwa
    
    Tonight : Clear.  A few clouds.  A mix of sun and clouds.  30 percent
     chance of showers.  Wind west 20 km/h around noon.  Becoming
     southwest in the evening.  Low 14, with temperature rising to 28 by
     morning.
    Thursday : Mainly sunny.  Increasing cloudiness tomorrow morning.
     Mainly cloudy.  30 percent chance of showers.  Wind southwest 20 km/h
     around noon.  High 28.  Low 15.  UV index 8 or very high.
    Thursday night : Mainly cloudy.  30 percent chance of showers.  Wind
     southwest 20 km/h around noon.  Low 14, with temperature rising to 23
     by morning.
    END 
    
    BULLETIN MÉTÉOROLOGIQUE: régulier
    Prévisions émises par pyrealb le mercredi 18 juillet 2018 à 16 h pour aujourd'hui et demain à 16 h. 
    Les prochaines prévisions seront émises le jeudi 19 juillet 2018 à 5 h 30. 
    Armstrong - Auden - parc Wabakimi
    Nakina - Aroland - Pagwa
    
    Ce soir et cette nuit : Dégagé.  Quelques nuages.  Partiellement
     couvert.  30 pour cent de probabilité d'averses.  Vents de l'ouest de
     20 km/h vers midi.  Devenant du sud-ouest dans la soirée.  Minimum
     14, températures à la hausse pour atteindre 28 en matinée.
    Jeudi : Généralement ensoleillé.  Ennuagement demain matin.
     Généralement nuageux.  30 pour cent de probabilité d'averses.  Vents
     du sud-ouest de 20 km/h vers midi.  Maximum 28.  Minimum 15.  Indice
     UV 8 ou très élevé.
    Jeudi soir et nuit : Généralement nuageux.  30 pour cent de
     probabilité d'averses.  Vents du sud-ouest de 20 km/h vers midi.
     Minimum 14, températures à la hausse pour atteindre 23 en matinée.
    FIN 

This program does not reproduce verbatim the output of the system used by ECCC because we simplified it for didactic purposes. Our goal is to illustrate a use of the **pyrealb** realizer in an interesting context, in fact, [weather information is one of the most successful _real-life_ applications of Natural Language Generation (NLG)](https://ehudreiter.com/2017/05/09/weathergov/ "You Need to Understand your Corpora! The Weathergov Example – Ehud Reiter's Blog").

This document outlines the organization of the system and should be read in conjunction with the [Python source code on the `pyrealb` GitHub](https://github.com/lapalme/pyrealb/tree/main/demos/weather). Only excerpts are shown here to emphasize the aspects of the text generation that are more challenging. We take for granted that the reader can understand Python code and is familiar with the constituent notation used as input for **pyrealb**.

## Separating information processing from linguistic realization

One advantage of using **pyrealb** is to allow a clear separation between _What to say_ and _How to say it_ through the use of syntactic constructions that can be built incrementally by program and easily parameterized. The syntactic patterns are then realized and formatted into syntactically correct English and French taking care of subject-verb agreements, verb conjugation, noun declension and proper spacing between punctuation.

Internally, the notation used as input specification calls Python class constructors. The Python objects built by these calls can then be realized by **pyrealb**.

For example, the following Python expression creates a data structure which is _realized_ using `.realize()` to produce `Flurries begin in the morning, amount 2 feet.`

```python
S(N("flurry").n("p"),                              # type of precipitation
  VP(V("begin").t("p"),                            # action
     CP(PP(P("in"),NP(D("the"),N("morning")))),    # moment of action
        NP(N("amount"),NP(NO("2"),N("foot")))))    # quantity
```

The notation mimics the conventional constituent syntactic notation for syntactic trees for _phrases_ such as `S` for sentence, `VP` for Verb Phrase, etc. or _terminals_ such as `N` for Noun, `V` for verbs, etc. The dot notation is used for modifiers (`n` for number, `t` for tense). See [**pyrealb** documentation](https://github.com/lapalme/pyrealb/blob/main/docs/documentation.html) for more details.

As can be seen in this example, each word is specified with its lemma, i.e. the basic form found in a dictionary. The realization process takes care of the grammatical _details_ which are nevertheless important for readers: plural forms, verb conjugation, agreement between the subject and the verb and between a number and the noun, proper punctuation between parts of a coordination, if present.

It might be argued that the `pyrealb` notation is more verbose than the realized sentence, but this expression can be modularized into a function with parameters that can be called in different contexts to produce many grammatically correct variations. For example, the above example can be _abstracted_ into the following function:

```python
def pcpn(type,action,tense,moment,quantity=None,unit=None):
  return S(type,
           VP(V(action).t(tense),
              CP(PP(P("in"),NP(D("the"),N(moment))),
                 None if quantity==None else NP(N("amount"),NP(NO(quantity),unit)))))
```

which can be called in various ways, as is shown in this table (the first line is equivalent to our example):


| pyrealb expression | Realized text |
| :----------------------------------------------------------- | ----------------------------------------------- |
| `pcpn(N("flurry").n("p"),"begin","p","morning",2,N("foot"))` | `Flurries begin in the morning, amount 2 feet.` |
| `pcpn(N("rain"),"begin","p","evening",1,N("inch"))` | `Rain begins in the evening, amount 1 inch.`    |
| `pcpn(N("snow"),"stop","pr","evening"),"en")`                | `Snow stopping in the evening.`                 |
| `pcpn(NP(V("freeze").t("pr"),N("drizzle")),"start","f","morning")` | `Freezing drizzle will start in the morning.`   |


In a way, the **pyrealb** notation might be viewed as an *smart* formatting specification language that can  format strings and numbers, but that also takes care of grammatical features that are essential for producing publication quality texts. As we will show later, **pyrealb** can also realize French sentences when the appropriate French lemma are given. It can also deal with the proper wording of numbers and dates. Although not shown here, **pyrealb** can also produce HTML tags so that it can be embedded in web pages, the **pyrealb** demos shows many use cases of HTML formatting combined with graphics. It is even possible to realize bilingual sentences in which some parts are in English and others in French.


## Weather data organization

We now outline the JSON data organization for a given weather bulletin used as input for our demonstration program in terms of Python data structures (see the first code block above for an example):

*   administrative information:
    *   `header` : issue `datetime`, next-issue `datetime`
    *   `names-en`: list of English region names to which the forecast applies
    *   `names-fr`: list of French region names to which the forecast applies
*   weather information : list of values of which the first two are the _starting hour_ and _ending hour_ relative to 0h of the issue datetime, when they are negative, they refer to historical data; the other values (described below depending on the type of information). For `precipitation-type` and `wind`, a value can be a list of values which describes an exceptional phenomenon (e.g., gust within a wind period) that occurs during this period.

    *   `precipitation-type`: e.g. rain, snow, ...;
    *   `precipitation-accumulation` : type (e.g., rain, snow), amount (in cm for `snow` or mm for `rain`)
    *   `precipitation-probability` : type (e.g. rain, snow), value of prob in percentage
    *   `sky-cover` : sky cover between 0 (no cover) and 10 (full cover)
    *   `temperatures`: values of temperature in Celsius
    *   `uv-index` : value between 0 and 10 of UV index
    *   `wind` : speed of the wind
*   auxiliary information for the purpose of the demo

    *   `en` : original bulletin in English to ease comparison of generated text with the issued forecast
    *   `fr` : original bulletin in French to ease comparison of generated text with the issued forecast
    *   `id` : id of the original data, to ease debugging of the data conversion program.

# Bilingual data organization

In this type of application, it is necessary that the same information be conveyed in both languages. In order to achieve this goal, we clearly separate the linguistic part from the selection and organization of the data. Moreover, in order to help with a fully parallel linguistic expression between English and French, we organize language dependent information in two classes, `English` and `Francais`, for which attributes and methods build  **pyrealb** expressions that can be realized into equivalent formulations in both English and French.  Most text generation methods will be parameterized by an instance of one of these two classes, so that calling the attribute or the method will produce the linguistic expression in the chosen language. 

The following table illustrates the structure of these classes: lines 1 to 17 show the constructor which loads the appropriate language and then adds some specialized words to the corresponding pyrealb lexicon. Lines 9 to 15 show how to express periods of a day given the hour number, see the source code for the other attributes. Lines 19 to 35 define functions to generate a temperature trend and a period of the day, see the source code for the other methods. The source code of the `English` and `Francais` classes is *aligned*, each corresponding attribute and method starting at the same line number in both files.

As modifications to a data structure are permanent, it is important to create a new data structure at each use. The simplest way to achieve this is to create a function (e.g., a `lambda` in Python) that returns a new structure at each call such as in lines 10 to 14.

<table>
<tr>
<td style="width:400px;font-size:smaller">


```python
class English:
    def __init__(self):
        self.code="en"
        load("en")
        addToLexicon({"gust":{"N":{"tab":"n5"},"V":{"tab":"v1"}}})
        addToLexicon({"cloudiness":{"N":{"tab":"n2"}}})
        addToLexicon({"cent":{"N":{"tab":"n1"}}})
        
        self.dayPeriods=[
            (0,5,lambda:NP(N("night"))),
            (5,9,lambda:NP(Adv("early"),N("morning"))),
            (9,12,lambda:NP(N("morning"))),
            (12,18,lambda:NP(N("afternoon"))),
            (18,24,lambda:NP(N("tonight")))
        ]
        self.periodNames = {...}
        # other attributes
        ...
    def temp_trend(self, trend, goalTemp, when):
        return S(N("temperature"),
                VP(V(trend).t("pr"),
                   PP(P("to"),self.pyrTemp(goalTemp)),when))
    
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

    # other methods
```

</td>
<td style="width:400px;font-size:smaller">


```python
class Francais:
    def __init__(self):
        self.code = "fr"
        load("fr")
        addToLexicon("ennuagement",{"N":{"g":"m","tab":"n3"}})
        addToLexicon("verglaçant",{"A":{"tab":"n28"}})

        
        self.dayPeriods=[
            (0,5,lambda:NP(N("nuit"))),
            (5,9,lambda:PP(P("en"),NP(N("début"),PP(P("de"),N("matinée"))))),
            (9,12,lambda:NP(N("matin"))),
            (12,18,lambda:NP(N("après-midi"))),
            (18,24,lambda:NP(N("soir")))
        ]
        self.periodNames = {...}
        # autres attributs
        ...
    def temp_trend(self, trend, goalTemp, when):
        return S(NP(N("température").n("p"),
                    PP(P("à"),NP(D("le"),N(trend)))),
                    PP(P("pour"),V("atteindre").t("b"),self.pyrTemp(goalTemp),when))
    
    def pyrDayPeriod(self,hour):
        isTomorrow = hour > 23
        hour = hour % 24
        for (s, e, pyrExp) in self.dayPeriods:
            if s <= hour < e:
                exp = pyrExp()
                if isTomorrow:
                    if s == 0 : return NP(D("le"),N("nuit"),A("prochain"))
                    return exp.add(N("demain"),0)  # e.g demain matin, demain soir...
                return exp.add(D("ce"),1 if s== 5 else 0)
		
    # autres méthodes
```

</td>
</tr>
</table>

# Bulletin generation (`Bulletin.py`)

As shown in the sample given above, a weather bulletin is composed of standardized block of information some of which are created using simple attributes  (`communication_header`,`forecast_regions` and `end_statement`), but others (`title_block` and `forecast_text`) use more complex constructions. All these functions return a string that can be split over many lines, if it is too long or `None` in which case it is ignored in the output.

```python
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
```

This function can be called as follows to print an English and a French weather bulletin from the weather information given by `wInfo`.

```swift
print(generate_bulletin(wInfo,English()))
print(generate_bulletin(wInfo,Francais()))
```

To illustrate interesting NLG issues, we describe `forecast_text` which creates 3 paragraphs for each forecasting period. A paragraph starts with the name of the period (which will be explained later) and then the text realized by `forecast_period`. The string is formatted similarly to the original bulletin.

```python
def forecast_text(wInfo,lang):
    paragraphs=[]
    for period in wInfo.get_periods():
        paragraphs.append(
            textwrap.fill(
                lang.periodNames[period](wInfo.get_issue_date()+timedelta(days=1)).cap(True).realize()
                          +" : "+forecast_period(wInfo, period, lang)
                        ,width=70,subsequent_indent=" ")
            )
    return "\n".join(paragraphs)
```

A period is described as a list of sentences dealing with different weather aspects when they are relevant according to the data for the given period: conditions of the sky (clear, cloudy, etc.), precipitations (quantity of snow or rain), wind (direction and speed), temperature (levels, variations within the period) and the value of the UV index. When the data is not _relevant_ for the period, these functions return `None` which is ignored in the final realization.

```python
def forecast_period(wInfo,period,lang):
    sents=filter(lambda l:l!=None,[
        sky_condition(wInfo, period, lang),
        precipitation(wInfo, period, lang),
        wind(wInfo, period, lang),
        temperature(wInfo, period, lang),
        uv_index(wInfo, period, lang)
    ])
    return " ".join(sents)
```

For realization, these functions use **pyrealb** templates for each type of information. We now give a detailed example of a generation template and how it is used for realizing a string in either French or English.

## Access to the weather information (`WeatherInfo.py`)

The `WeatherInfo` class gives access to the content of the JSON file. Its constructor reads the JSON file from which is extracted a list of `WeatherTerm` instances having three fields: `start` hour, `end` hour and `infos` a list of values. The list of terms only contains terms that intersect the appropriate period according to the following table:

```python
issue_time_to_periods = {
    "morning":{"today":(5,18),"tonight":(18,30),"tomorrow":(30,42)},
    "midday":{"today":(12,18),"tonight":(18,30),"tomorrow":(30,42)},
    "evening":{"tonight":(16,30),"tomorrow":(30,42),"tomorrow_night":(42,54)},
}
```

For example, in an `evening` bulletin, for the `tomorrow` period only terms that have an ending time greater or equal than 30 and a starting time less than 42 are returned. If a given information is not found or if not values intersect the given range, `None` is returned.

For the `tomorrow` period of the above bulletin, these terms can be visualized as follows:

```
tomorrow ( +6h,+18h) :: fpto12-2018-07-18-2000-r1209c :: 2018-07-18 16:00:00
precipitation-type        : [+15h,⧺0h):[showers, [+15h,⧺0h):[thunderstorm]]
precipitation-probability : [+5h,+15h):[10], [+15h,+18h):[30]
sky-cover                 : [+5h,+11h):[2, 2], [+11h,+15h):[2, 8], [+15h,+18h):[8, 8]
temperatures              : [+5h,+8h):[15], [+8h,+11h):[23], [+11h,+14h):[28], [+14h,+17h):[25], [+17h,+20h):[23]
uv-index                  : [+12h,+14h):[7.7]
wind                      : [+0h,+12h):[sw, speed, 10], [+12h,+20h):[sw, speed, 20]
```

The semi-open time intervals are indicated by hour modulo 24 prefixed with + for the next day and ⧺ for the day after tomorrow. The first line give the period name, its time interval, its id and the issue time. Then are given the (non `None`) field names with the terms with time intervals that intersect the period interval. Each term is shown with its time interval followed by its lists of values, some of which can be terms themselves (e.g. `thunderstorm` in `precipitation-type`)

Access to the information in `WeatherInfo` is performed with functions such as the following which returns only relevant terms for the period:

```python
def get_precipitation_probabilities(self,period):
    if "precipitation-probability" not in self.data: return None
    return self.select_terms(period, self.data["precipitation-probability"])
```

## Sky condition (`Realization.Sky_Condition.py`)

This indicates the general weather conditions, such as :

    Mainly sunny. Increasing cloudiness tomorrow morning.
    Généralement ensoleillé. Ennuagement demain matin.

Different ways of realizing sky conditions are given in the following language attribute. Below we show only the one defined in the `English` constructor, but the counterpart in `Francais` is similar: a condition is associated with a pair whose first component expresses this condition during the day and the second during the night. For example, *no cover* (`"c1"`)  will correspond to `sunny` during the day, but `clear` during the night. If only one value is given for the tuple, then the first value is always used; e.g., `cloudy` is used for both the day and the night. 

```python
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
```

This attribute is used in the context of the following function which loops over the _sky cover terms_ and depending on the values of the sky covering at the start and end of the period to determine the appropriate expression to use. Some care is taken not to repeat the same expression for different terms. All **pyrealb** expressions are added to a list whose elements are realized and concatenated. If the name of the `period` is `today` or `tomorrow`, the first element of the tuple is chosen otherwise the second is used.

```python
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
             ...
        elif valStart in [0, 1, 2, 3] and valEnd in [7, 8, 9, 10]:
            addNoRepeat("c7", dayNight, lang.pyrDayPeriod(sc_term.start))
        elif (valStart in [7, 8, 9, 10] and valEnd in [0, 1, 2, 3]) or \
                (valStart in [5, 6] and valEnd in [0, 1]):
            addNoRepeat("c8", dayNight, lang.pyrDayPeriod(sc_term.start))
    return " ".join(S(pyrExpr).realize() for pyrExpr in pyrExprs)
```

## Precipitation (`Realization.Precipitation.py`)

For information about rain or snow, for example:

    30 percent chances of showers ending during the night.
    30 pour cent de probabilités d'averses finissant durant la nuit.

The French and English realizations of the many precipitation types are given in a table given as attributes of the language class. Here is an extract of the `English` constructor.

```python
    self.precipitationTypes = {
        "showers":lambda:N("shower").n("p"),
        "flurries":lambda:N("flurry").n("p"),
        "wet-flurries":lambda:NP(A("wet"),N("flurry").n("p")),
        "blizzard":lambda:N("blizzard"),
        ...
        "rain":lambda:N("rain"),
        "freezing-rain":lambda:NP(V("freeze").t("pr"),N("rain")),
        "blowing-snow" :lambda:NP(V("blow").t("pr"),N("snow")),
    }
```

A precipitation amount is realized when the probability, in increments of 10%, is between 30% and 70%, but different than 50%. When it is 80% or more, the beginning or ending is given. The amount is given when it is significant (at least 2 cm of snow or at least 25 mm of rain). Only probability terms that are more than 30% are realized. Note that this algorithm, like all others, is language independent, linguistic expression coming attributes and methods defined in the object of the `lang` parameter.

```python
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
```

## Wind (`Realization.Wind.py`)

Information about the wind speed and directions are realized such as the following:

    Wind west around noon. Becoming southwest in the evening.
    Vents de l'ouest vers midi. Devenant du sud-ouest dans la soirée.

Wind direction realizations are given in a table in language class attribute. Here is the one in `English`.

```python
    self.pyrWindDirection = {
        "e":    lambda:Adv("east"),
        "n":    lambda:Adv("north"),
        "ne":   lambda:Adv("northeast"),
         ....
      	 "s":    lambda:Adv("south"),
        "sw":   lambda:Adv("southwest"),
    }
```

Wind terms are scanned to realize the ones with wind speed of more than 15 km/h. When a wind speed changes by more than 20 km/h or if it changes direction then an appropriate realization is emitted. If a gust is detected during the period, it is also expressed. The expression is built incrementally by starting with an empty `S()` to which an `NP` and possibly a `VP` or an indication of the time are added.

```python
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
```

## Temperature (`Realization.Temperature.py`)

Temperatures can be described very simply such as:

    High 28. Low 15.
    Maximum 28. Minimum 15.

or with a trend when there is a significant difference in temperatures: negative change of at least 3°C during the daytime or a positive change of at least 3°C during nighttime:

    Temperature rising to 28 by morning.
    Températures à la hausse pour atteindre 28 en matinée.

This achieved with this

```python
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
    if t1 >= t2+3:                       # abnormal change time
        if i1 <= 1 :
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
```

The value of a temperature is indicated using the conventions of ECCC, add a qualifier `plus` when it is less or equal to 5, and `minus` when it is below 0. Here the method defined in `English`.

```python
    def pyrTemp(self,val):
        if val == 0: return N("zero")
        if val < 0: return AdvP(A("minus"), NO(abs(val)))
        if val <= 5: return AP(A("plus"), NO(val))
        return NO(val)
```

The first code block shows the the trend expression in both `English` and `Francais` and _abnormal_ situations are encoded using the following method for `English`:

```python
    def pyrAbnormal(self,dn,kind):
        if dn == "night":
            if kind == "a": return lambda t,_:self.temp_trend("rise",t,PP(P("by"),N("morning")))
            ...
            if kind == "e": return lambda t,p:self.temp_trend("rise",t,p).add(AdvP(Adv("then"),V("fall").t("pr")))
        if dn == "day":
            if kind == "a": return lambda t,_:self.temp_trend("fall",t,PP(P("by"),N("afternoon")))
            ...
          	if kind == "e": return lambda t,p:self.temp_trend("fall",t,p).add(AdvP(Adv("then"),V("rise").t("pr")))
        print("*** pyrAbnormal: bad parameters:",dn,kind)
```

## UV index (`Realization.UV_index.py`)

UV index information, a number which ranges from a low of zero to a high of 11+, is only given for bulletin during a day period in the following way:

    UV index 8 or very high.
    Indice UV 8 ou très élevé.

The language dependent information defined as attributes of the language classes.

```python
        self.uv_index = Q("UV index")
        self.or_ = C("or")
				self.uv_ranges = [(2, lambda: A("low")),
                          (5, lambda: A("moderate")),
                          (7, lambda: A("high")),
                          (10, lambda: AP(Adv("very"), A("high"))),
                          (1000, lambda: A("extreme"))]
```

Its realization is simple matter of outputting its rounded value and if it is greater than 0\. The English or French realization is obtained by searching a table [according to the guidelines of ECCC](https://www.canada.ca/en/environment-climate-change/services/weather-health/uv-index-sun-safety/about.html "About the UV index - Canada.ca"). This achieved with the following language independent code

```python
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
```

## Conclusion

This document has shown how to generate bilingual documents from a single source of information using **pyrealb** in conjunction with the data manipulation all in Python. Although the input data and the generated documents are simpler than what would be used in a real-life context, the essential organization of the system should stay the same as the framework is extensible.

[Guy Lapalme](mailto:lapalme@iro.umontreal.ca)