import json,re,random,os
from collections import Counter

# get information from the flight database
flightDB=json.load(open(os.path.dirname(__file__)+"/flightDB.json","r",encoding="utf-8"))
airlines=[flightDB["airlines"][key].lower() for key in flightDB["airlines"]]
# print(airlines)
cities  =[flightDB["airports"][airport]["city"].lower() for airport in flightDB["airports"]]
airport_codes=list(flightDB["airports"].keys())
# print(cities)

# ensure that cities and airlines are ones that are in the database...
def changeCitiesAirlines(entities):
    # check cities
    cityMap={}
    newCities=random.sample(cities,4) # sample 3 different cities
    iCity=0                           # index in city replacement
    for entity in entities: # find systematic replacements
        if entity["entity"] == "city_name":
            if entity["value"] not in cityMap:
                cityMap[entity["value"]]=newCities[iCity]
                iCity+=1
    for entity in entities:
        if entity["entity"]=="city_name":
            entity["value"]=cityMap[entity["value"]]
        elif entity["entity"]=="airline_name":
            entity["value"]=random.choice(airlines)
        elif entity["entity"]=="airport_code":
            entity["value"]=random.choice(airport_codes)

# Parse all examples from the {train|test}.json files and compute statistics
# if change is True :
#    change the names of airlines and airports to the ones in flightDB.json
#    adjust the text and the start and end position of entities
def parse_example(example, change, allIntents=None, all_entities=None, allRoles=None, allValues=None):
    text = example["text"]
    entities = example["entities"]
    if change:
        changeCitiesAirlines(entities)
    newText = ""
    entitySet=set()
    last = 0
    shift = 0  # differences in length between old and new values
    if len(entities) > 0:
        for e in entities:
            newText += text[last:e["start"]]
            entity = e["entity"] # save values of fields
            value = e["value"]
            start = e["start"]
            end   = e["end"]
            if allValues is not None:
                allValues[value] += 1
            newText+=f'[{value}]'
            if change:
                e["start"] += shift
                shift += len(value) - (end - start)
                e["end"] += shift
            if "role" not in e:
                newText += f'({entity})'
                role = None
            else:
                role = e["role"]
                newText += f'{{"entity":"{entity}","role":"{role}"}}'
                if allRoles is not None:
                    allRoles[role] += 1
            if all_entities is not None:
                if entity not in all_entities:
                    all_entities[entity]=[1,set()]
                else:
                    all_entities[entity][0] += 1
                if role is not None:
                    all_entities[entity][1].add(role)
            entitySet.add(entity)
            last = end
    newText += text[last:]
    if allIntents is not None:
        intent = example["intent"]
        if intent not in allIntents:
            allIntents[intent] = []
        allIntents[intent].append((newText, entitySet))
    if change:
        example["text"] = newText

#  show statistics on the file
if __name__ == '__main__':
    inputFN = "data/train.json"
    inputF = open(inputFN, "r", encoding="utf-8")
    data = json.load(inputF)
    allIntents = {}  # {str:[[str,set(str)]} : [(texte avec entités annotées,ensemble d'entités)]
    allEntities = {} # {str: [int,set(str)]}  : [(nombre d'occurrences,ensemble de roles)]
    allValues = Counter()
    allRoles = Counter()
    examples=data["rasa_nlu_data"]["common_examples"]
    for example in examples:
        parse_example(examples,True,allIntents,allEntities,allRoles,allValues)
    ### print statistics...
    print("FILE:%s [%d examples]"%(inputF.name,len(examples)))
    print("\nALL INTENTS")
    for (n,i) in sorted([(len(ins),i) for (i,ins) in allIntents.items()],reverse=True):
        print("%5d:%s"%(n,i))
    print("\nALL ENTITIES")
    for (e,[n,roles]) in sorted(allEntities.items()):
        print("%-30s:%5d:%s"%(e,n,", ".join(role for role in roles)))
    print("\nALL ROLES")
    for (e,n) in sorted(allRoles.items()):
        print("%-30s:%5d"%(e,n))
    print("\nALL VALUES")
    for (e,n) in sorted(allValues.items()):
        print("%-30s:%5d"%(e,n))

"""
FILE:data/test.json [893 examples]
All intents
  632:flight
   48:airfare
   38:airline
   36:ground_service
   33:abbreviation
   21:capacity
   18:airport
   12:flight+airfare
   10:distance
    9:aircraft
    8:flight_no
    7:ground_fare
    6:meal
    6:city
    3:quantity
    2:day_name
    1:flight_time
    1:flight_no+airline
    1:flight+airline
    1:airfare+flight

All entities
aircraft_code                 :   33:
airline_code                  :   34:
airline_name                  :  101:
airport_code                  :   19:stoploc, fromloc, toloc
airport_name                  :   36:fromloc, toloc
booking_class                 :    1:
city_name                     : 1497:stoploc, fromloc, toloc
class_type                    :   24:
compartment                   :    1:
connect                       :    6:
cost_relative                 :   37:
country_name                  :    1:toloc
date_relative                 :   22:depart_date, arrive_date, return_date
day_name                      :  227:depart_date, arrive_date, return_date
day_number                    :   61:depart_date, arrive_date
days_code                     :    1:
economy                       :    6:
end_time                      :   11:arrive_time, depart_time
fare_amount                   :    2:
fare_basis_code               :   17:
flight                        :    1:
flight_days                   :   10:
flight_mod                    :   24:
flight_number                 :   11:
flight_stop                   :   21:
flight_time                   :    1:
meal                          :   16:
meal_code                     :    1:
meal_description              :   10:
mod                           :    2:
month_name                    :   62:depart_date, arrive_date
or                            :    3:
period_mod                    :    5:depart_time
period_of_day                 :  140:arrive_time, depart_time
restriction_code              :    4:
round_trip                    :   73:
start_time                    :   11:arrive_time, depart_time
state_code                    :   42:fromloc, toloc
state_name                    :   54:fromloc, toloc
time                          :   91:arrive_time, depart_time
time_relative                 :   96:arrive_time, depart_time
today_relative                :    9:depart_date
transport_type                :   10:
year                          :    3:depart_date

All roles
arrive_date                   :   25
arrive_time                   :   87
depart_date                   :  352
depart_time                   :  263
fromloc                       :  761
return_date                   :    5
stoploc                       :   21
toloc                         :  770
All values
1 pm                          :    3
10 am                         :   10
10 pm                         :    3
12 pm                         :    1
1200                          :    1
1201 am                       :    1
1205 pm                       :    1
1207                          :    1
1500                          :    2
1700                          :    1
1800                          :    1
19                            :    1
1993                          :    1
1994                          :    2
2 pm                          :    2
200 dollars                   :    1
230 pm                        :    2
3 pm                          :    8
300 dollars                   :    1
320                           :    1
382                           :    1
4                             :    1
4 o'clock                     :    1
4 o'clock pm                  :    1
4 pm                          :    2
419 pm                        :    1
468                           :    1
486                           :    1
5                             :    1
5 pm                          :   14
6                             :    1
6 am                          :    1
6 pm                          :   17
608                           :    1
630 pm                        :    1
639                           :    1
665 673                       :    1
7 am                          :    1
7 pm                          :    8
72s                           :    2
733                           :    2
73s                           :    3
757                           :    4
8                             :    6
8 am                          :    4
8 pm                          :    3
811                           :    1
9                             :    1
9 am                          :    5
9 pm                          :    8
950 am                        :    1
DEN                           :    1
LAX                           :    1
LGA                           :    1
ORD                           :    2
PHL                           :    1
SEA                           :    1
SFO                           :    2
aa                            :    1
about                         :    1
after                         :   35
afternoon                     :   25
am                            :    3
american                      :   35
ap 20                         :    1
ap 57                         :    2
ap58                          :    1
april                         :   22
arizona                       :    8
arizona nevada                :    1
around                        :   14
as                            :    5
atlanta                       :  163
back                          :    1
be1                           :    2
before                        :   39
bh                            :    5
bn                            :    1
boston airport                :    1
breakfast                     :    2
bwi                           :    1
by                            :    2
california                    :   18
canada                        :    1
car                           :    3
charlotte airport             :    3
cheapest                      :   28
chicago                       :  165
close                         :    1
closest                       :    1
coach                         :    8
connecting                    :    4
d9s                           :    3
daily                         :   10
dallas fort worth airport     :    1
day after                     :    1
dc                            :   42
dc10                          :    1
dc9                           :    1
december                      :    6
delta                         :   13
denver                        :  182
denver airport                :    1
departure times               :    1
dh8                           :    1
dinner                        :    5
direct                        :    2
dl                            :    3
dtw                           :    2
dulles                        :    1
earliest                      :    2
earliest arriving             :    5
early                         :   10
economy                       :    6
eighth                        :    5
evening                       :   20
f                             :    3
february                      :    2
fifth                         :    3
first                         :    9
first class                   :   17
flight                        :    1
florida                       :    2
friday                        :   21
h                             :    2
hp                            :    5
indiana                       :    4
indianapolis airport          :    1
j31                           :    1
jfk                           :    6
july                          :    3
june                          :   27
kennedy airport               :    1
kw                            :    1
l10                           :    2
l1011                         :    1
la guardia                    :    5
la guardia airport            :    2
las vegas airport             :    1
last                          :    3
late                          :    1
late afternoon                :    1
later                         :    1
latest                        :    3
lax                           :    1
least expensive               :    1
limousine                     :    5
los angeles                   :  165
los angeles international     :    1
love field                    :    2
lowest                        :    5
lunch                         :    1
m                             :    2
m80                           :    9
may                           :    2
meal                          :    2
meals                         :   14
memphis airport               :    1
michigan                      :    3
midnight                      :    2
milwaukee airport             :    1
minnesota                     :    2
monday                        :   38
mondays                       :    2
morning                       :   62
mornings                      :    1
most expensive                :    1
nashville airport             :    1
nevada                        :    2
new york                      :  318
newark airport                :    2
next                          :   20
night                         :   10
ninth                         :    3
no later than                 :    2
nonstop                       :   21
noon                          :    9
north carolina                :    2
not                           :    1
not exceeding                 :    1
ohio                          :    3
one way                       :   22
ontario airport               :    1
or                            :    3
philadelphia                  :  174
phoenix airport               :    2
pittsburgh airport            :    1
pm                            :    3
prior to                      :    1
q                             :    3
qo                            :    1
quebec                        :    3
red eye                       :    1
return                        :    1
round trip                    :   47
round trips                   :    2
sa                            :    1
salt lake city airport        :    1
san francisco                 :  172
san francisco international   :    1
san francisco international airport:    1
saturday                      :   47
saturdays                     :    1
sb                            :    1
seattle                       :  158
seventeenth                   :    3
seventh                       :    5
shortest                      :    5
sixteenth                     :    2
sixth                         :   10
snack                         :    1
snacks                        :    1
sunday                        :   21
tacoma airport                :    1
taxi                          :    1
taxi service                  :    1
tennessee                     :    1
tenth                         :    5
texas                         :    1
the following day             :    1
thirteenth                    :    1
this                          :    1
thursday                      :   20
today                         :    4
tomorrow                      :    4
toronto international         :    2
toronto international airport :    1
tuesday                       :   27
twa                           :    7
twelfth                       :    2
twenty eighth                 :    2
twenty fifth                  :    2
twenty first                  :    3
twenty second                 :    1
twenty seventh                :    4
twenty sixth                  :    1
twenty third                  :    1
twenty three                  :    1
ua                            :    1
under                         :    1
united                        :   15
us                            :    9
us air                        :   20
utah                          :    3
virgin                        :   18
washington                    :    1
wednesday                     :   50
weekday                       :    2
wn                            :    1
y                             :    1
yx                            :    1
"""