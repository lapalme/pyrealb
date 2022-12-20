# Extract a very small subset of flights to use for answering questions
# The original data is taken from https://www.kaggle.com/datasets/usdot/flight-delays
#  about "2015 Flight Delays and Cancellations" in the USA
#    airlines.csv : only 5 airlines were selected from the 14 in the original
#    airports.csv : only 9 airports were selected from the 322 in the original
# This program creates flightDB.json by selecting  flights from "flights.csv" (592 MB)
# operated by the above selected airlines departing from and arriving in selected airports.
# Only the first complete week of January (4th to 11th) 2015 is kept which
# we consider as sufficient for our small demo.
#
# The selected airlines, airports and flights are combined in flightDB.json (1,8 MB)

import csv,json,os
pwd = os.path.dirname(__file__)

airports={}
with open(os.path.join(pwd,"airports.csv")) as airport_csv:
    airportsReader = csv.reader(airport_csv)
    next(airportsReader)
    for row in airportsReader:
        airports[row[0]]={"name":row[1],"city":row[2]}
print(airports)

airlines={}
with open(os.path.join(pwd,"airlines.csv")) as airline_csv:
    airlinesReader = csv.reader(airline_csv)
    next(airlinesReader)
    for row in airlinesReader:
        airlines[row[0]]=row[1]
print(airlines)

flights=[]
fields = ['MONTH', 'DAY', 'DAY_OF_WEEK', 'AIRLINE', 'FLIGHT_NUMBER', 'ORIGIN_AIRPORT', 'DESTINATION_AIRPORT', 'SCHEDULED_DEPARTURE', 'DISTANCE', 'SCHEDULED_ARRIVAL']
numericfields=['MONTH', 'DAY', 'DAY_OF_WEEK']
with open(os.path.join(pwd,"Original","flights.csv")) as airline_csv:
    airlinesReader = csv.DictReader(airline_csv)
    i=0
    for row in airlinesReader:
        if int(row["DAY"])<4:continue   # skip until the January 4th
        if row["AIRLINE"] in airlines and row["ORIGIN_AIRPORT"] in airports and row["DESTINATION_AIRPORT"] in airports:
            for f in numericfields:
                row[f]=int(row[f])
            flight = {f:row[f] for f in fields}
            # print(flight)
            flights.append(flight)
            i+=1
            if row["DAY"]>10:break

flightDB=open(os.path.join(pwd,"flightDB.json"), "w", encoding="utf-8")
json.dump({
    "airports":airports,
    "airlines":airlines,
    "flights":flights
},flightDB,indent=2)
print("%d flights on %s"%(len(flights),flightDB.name))

