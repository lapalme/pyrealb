# A chatbot for flight information

This demo presents a flight information question-answering system connected to a RASA conversation manager that uses `pyrealb` for realizing answers. See the [accompanying text](RASA-INTRO.md) for a quick introduction to the implementation of a conversation bot using RASA. 

RASA is a conversation manager for dealing with interactions with users. It is aimed at businesses that want to streamline the communication with their customers through chatbots that can answer to the most frequently asked questions. RASA parses the input from users in which it identifies specific entities (e.g. names, dates, amounts, etc.); it also determines the conveyed _intent_ (e.g. greeting, order, request for information, etc.) of the message.  This intent is then used to guide the user through some predefined scenarii (dubbed _stories_) to guide the conversation. In order to achieve this goal, RASA uses learning algorithms to determine entities and intent. It is thus important to provide many annotated examples of questions for each intent.

In this document, we first present the data used for the queries in the chatbot and then show how to launch the demo. The main implementation choices are then described focusing on the NLG aspects.

## A corpus of questions and intents over a database
As examples of questions, we use a version of the [Air Travel Information System (ATIS) corpus](https://catalog.ldc.upenn.edu/docs/LDC93S4B/corpus.html) which was originally collected to develop and evaluate speech systems that understand spontaneous speech. The corpus was gathered in a _Wizard of Oz_ experiment in which users were asking about flights, fares, airlines, cities, airports, and ground services for which the information was contained in a relational database. Given the availability of this corpus, the text part (ignoring the speech aspects, e.g. waveform files) has often been used as test for Natural Language Generation (NLG) experiments to try to reproduce the texts from the meticulous data annotations of the different entities in the text.  Of course, these experiments bypass the important _What to say_ step of NLG, but they allow focusing on the _How to say_ step. 

To create a bot that can answer questions in a somewhat realistic database, we extracted 
a subset of flights taken from [2015 Flight Delays and Cancellations](https://www.kaggle.com/datasets/usdot/flight-delays) [592 MB]
* `airlines.csv` : we selected 5 airlines from the 14 in the original
* `airports.csv` : we selected 9 airports from the 322 in the original
* `flightDB.json` : a 1,8 MB file created by `selectFlights.py` that picks flights operated by the selected airlines departing from and arriving in the selected airports. Only flights in the first complete week of January 2015 were kept which we considered as sufficient for our demo. The selected airlines and airports are also included in this file. A _fictive_ cost based on the distance and day of the week is added to each flight.

For training the RASA utterance parser, we use this [version of the dataset](https://github.com/howl-anderson/ATIS_dataset/blob/master/README.en-US.md) slightly modified by `convertJSON.py` so that the roles are indicated as an explicit field instead of being integrated into the entity name as required for RASA 3.0.  The departing and arriving airports and the airlines are changed so that only the ones in `flightDB.json` are used. 

## Launching the RASA bot

**CAUTION**: 
* Because of the need of a special environment (RASA runs only in Python 3.9), it is preferable to test with a copy of the `RASA_bot` directory in a Python 3.9 virtual environment that includes RASA.  
* As our goal was to explore how `pyrealb` could be used as a RASA NLG server, we did not  _tune_ the learning parameters of RASA. This might explain why intent determination is not always _ideal_.

There is already a _vanilla_ pretrained model in the RASA_bot directory. Make sure that you have an appropriate RASA system installed as described in the first five steps of the [accompanying text](RASA-INTRO.md#Initial-install-and-test-of-the-RASA-environment). 


1. `cd RASA_bot`
2. Activate the virtual environment  
     `source ./venv/bin/activate`
3. If some some training examples in the `Examples/train.json` have changed, run `make_training_data.py` and retrain with `rasa train` in the `RASA_bot` directory (be patient!)
4. In a separate console, launch the NLG server with `python3 nlg_server.py` found in the source files of this demo
5. Interact with RASA using one of the following:
   1. the console: `rasa shell` and type questions at the `Your input ->` prompt
      1. to check that the NLG server is working: type `good morning`, it should answer by `Monday in Chicago:...`
      2. type a query such as `show flights by American from Denver to Chicago on Monday`
   2. the RASA chat widget:
      1. in another console, type `rasa run --cors "*"` wait until `Rasa server is up and running.`
      2. launch a local web server, such as `python3 -m http.server 8080` which should be run from the parent directory of RASA_bot
      3. in a browser, load the url `http://127.0.0.1:8080/RASA-Client.html` and type a a query such as `show flights by American from Denver to Chicago on Monday`in the chat box. 
      4. this should display something like, the initial greeting is sent automatically by HTML page:  
      
![](images/RASA_chat_with_server.jpg)
      

## Implementation of the system

###  Structure of the questions in the training corpus
The following is an example of an annotated question (there are 4978 questions in the training corpus and 893 in the test corpus) which associates a tokenized `text` with an `intent` (there are 26 different intents, the most frequent being `flight` which accounts for 70% of all intents in the test corpus) and a list of entities and roles that have been identified in the original question with their positions in the `text`. 

```javascript
    { "text": "i need a nonstop flight from denver to atlanta",
      "intent": "flight",
      "entities": [
            { "start": 9, "end": 16, "value": "nonstop", "entity": "flight_stop" },
            { "start": 29, "end": 35, "value": "denver", "entity": "city_name", role="fromloc" },
            { "start": 39, "end": 46, "value": "atlanta", "entity": "city_name", role="toloc" }
        ]
    }
```
### Re-realization of the questions
Before answering the questions, we decided to realize the original questions using `pyrealb`. We originally felt this step was important to learn how to _juggle_ with the information contained in a question before attempting answering it. As this exercise revealed to be an interesting learning experience, we give some details about it in the following sections.

Our goal is not to reproduce _verbatim_ the original `text`, but to illustrate how the information about the entities 
can be used to realize different well-formed English sentences for the example given previously such as: 

    I need to travel nonstop from Denver to Atlanta. 
    Show a nonstop flight from Denver to Atlanta. 
    Please give a nonstop flight from Denver to Atlanta. 
    List a nonstop flight from Denver to Atlanta. 

We also developed a simple baseline generator using only Python string operations. The above information is then
rendered as:

    show nonstop flights from denver to atlanta

### Organization of the information

An important aspect of a *data to text* system  is the fact that **all the data, and nothing but the data**, should be realized as text. In our case, this means that all `entities` must be _consumed_ once, and only once, when the text is fully rendered. To achieve this, we define a class called `Entities`to manage the list of entities, an entity being itself represented by another class `Entity`. As entities can be repeated we should not use a _dictionary_ of entities.  The following method returns a comma separated list of all values associated with a given entity name taking into account an optional role. It also removes the found entities from the list. It returns an empty string if the entity is not found.

```python
    def grab_value(self, field:str, role:str=None) -> str:
        res=[]
        i=0
        # cannot use a for loop because the list might be changed during iteration
        while i<len(self.entities):
            if self.entities[i].has_entity_role(field, role):
                res.append(self.entities[i].get_value())
                del self.entities[i]
            else:
                i+=1
        return ", ".join(res)
```
This organization allows checking that all entity values have been realized at the end of the generation process.

### Text generation using `pyrealb` (file `realize_example.py`)

The goal is to transform entities into an internal data structure that can be realized as an English sentence by 
`pyrealb`.  For the first sentence above, this means creating a structure equivalent to the following calls:

```python
    S(Pro("I").pe(1),
      VP(V("need"),
         V("travel").t('b-to'),
         AP(Q("nonstop")),
         PP(P("from"),
            Q("Denver")),
         PP(P("to"),
            Q("Atlanta"))))

```

#### `Terminal` realization
`pyrealb` words are instances of the `Terminal` class, so values of entities must be transformed.
The  following function creates a `Terminal` from an entity value guessing its  type from the entity name.

```python
def get_terminal(val:str,entity:str) -> Terminal:
    if entity.endswith("_code"): # upper case for codes
        val=val.upper()
    elif entity.endswith("_name"):  # title case for names
        val=val.title()
    lemma = getLemma(val)  # check lemma type in the dictionary
    if lemma is not None:
        if "N" in lemma: return N(val)
        if "A" in lemma: return A(val)
        if "Adv" in lemma: return Adv(val)
    return Q(val)  # if not found, return a Quoted string
```

#### `Phrase` realization
This is used in the following function that is the _basic block_ of most types of realizations. It builds a list of the terminals corresponding to the fields (entity names) appearing in the entities. These terminals are then used as parameters for the `Phrase` constructor given as first parameter. If no matching field names are found then the function returns `None`, a value ignored by `pyrealb` constructors. 

```python
def realize(phrase:Phrase, entities:Entities, fields:list[str], role:str=None)->Constituent:
    res = []
    for f in fields:
        val = entities.grab_value(f, role)
        if len(val)>0:
            res.append(get_terminal(val,f))
    return phrase(*res) if len(res)>0 else None
```

For example, to create a subordinate phrase combining location information from the entities, this function is used as follows:

```python
def realize_loc(phrase:Phrase, entities:Entities, role: str) -> Constituent:
    return realize(phrase, entities,
                   ["city_name", "state_name", "state_code","country_name",
                    "airport_name", "airport_code"],role)
```
which can be called as follows:

``` python
        realize_loc(pp("from"), entities, "fromloc"),
        realize_loc(pp("to"), entities, "toloc"),
        realize_loc(lambda x: VP(V("stop").t("pr"),P("in"),x), entities, "stoploc")
```
to realize the departure and arrival airports with a possible stop in between.

Similar functions are defined for date and time information.

#### Common flight information realization

Given the fact that almost all requests need general information about flights such as departure, arrival times and places. The following function return a list of `Phrase` combining the values of the relevant entities. Remember that the realization functions return `None` if no relevant entity is found without calling the `Phrase` constructor.

```python
def realize_common(entities:Entities) -> [Constituent]:
    def date_time(kind,vp):
        if entities.has_role(kind+"_date") or entities.has_role(kind+"_time"):
            return vp([realize_date(entities, kind+"_date"),
                       realize_time(entities, kind+"_time")])
 
    return [
        realize_loc(pp("from"), entities, "fromloc"),
        realize_loc(pp("to"), entities, "toloc"),
        realize_loc(lambda x: VP(V("stop").t("pr"),P("in"),x), entities, "stoploc"),
        date_time("depart",lambda x: VP(V("depart").t("pr"),P("on"),x)),
        date_time("arrive",lambda x: VP(V("arrive").t("pr"),P("at"),x)),
        date_time("return",lambda x: VP(V("return"),x)),
        realize(pp("on"), entities, ["airline_name", "airline_code",
                                     "airport_name", "airport_code",
                                     "aircraft_code",
                                     "flight_number","flight_code"]),
        realize(lambda x: VP(V("serve").t("pr"),x), entities,
                ["city_name","meal","meal_description", "meal_code"]),
        realize(pp("with"),entities,["fare_basis_code"]),
        realize(pp("at"),entities,["airport_name"])
    ]

```

Many of these realization functions use the following _helper_ which creates a prepositional phrase with a given preposition.

```python
def pp(prep:str) -> Callable[[Constituent],Phrase]:
    return lambda *x:PP(P(prep),*x)
```
For example, the result of the call to `realize_common` on our running example:

```python
[PP(P("from"),Q("Denver")), PP(P("to"),Q("Atlanta")), None, ...]
```

The list of entities if now left with only the first original element.

#### Questions with a specific _intent_ realization

For each intent, we define a function to create an appropriate `pyrealb` expression that can be realized as a sentence.
We only describe here the content of the function for the _flight_ intent which is by far the most frequently encountered, accounting for 74% of all intents in the training corpus. The other 25 intents are dealt similarly.

Even though not necessary in this application, it is often interesting to allow different formulations for a given semantics. `oneOf` is a `pyrealb` function that randomly returns one of its parameters, it is thus convenient to create alternatives when there are no other constraints. As a Python function normally evaluates its parameters before the call, this would imply creating all alternatives before choosing; this is problematic in our case because realization has side effects, namely modifying the list of entities. So in other to delay evaluation of a parameter until it is _selected_, we _wrap_ it in a `lambda` without parameter. Once `oneOf` has chosen an alternative, it checks if it is a `lambda` and if so, it calls the lambda without parameter and returns the results. This _lambda trick_ is not necessary in the case of _simple_ parameters such as strings, (e.g. for choosing in verb below):

```python
    return oneOf(
        lambda: S(oneOf(None,Q("please")),
                  VP(V(oneOf("show","list", "give","find","display")).t("ip"),
                     NP(D("a"),realize(AP, entities, flight_fields)),N("flight")).n(oneOf("s", "p")),
                  realize_common(entities)),
        lambda: S(Pro("I").pe(1),
                  VP(V(oneOf("want","need")), V(oneOf("go","travel")).t("b-to"),
                     realize(AP,entities,flight_fields),
                     realize_common(entities)))
    )
```
### Baseline generator (file `show_example.py`)

A simplified version of the question realizer using only Python string manipulations was also developed. In this simple use case, this approach seems sufficient for an output without any variation nor capitalization. This type of output is similar in format as the original text and in fact, the BLEU score on the test corpus is higher, thus _better_, with this baseline (42.3) than with the realizer (34.7).

Although the output of the _real_ realizer would most probably be preferred in a production context, the fact that its automatic score is much lower than the baseline is an indication of the limits of these types of scores.

### Answering questions using a flight database

#### Demo Flight Database
As described in the [Corpus description section](#A corpus of questions and intents over a database) in the `Flight Data` directory, we limit the queries to a very small subset of US airports, cities and flights from an existing dataset found in Kaggle in order to create `flightDB.json` which is used for answering the questions according to the _intents_ determined by RASA. 

There are 4,269 flights in the database (between the January 4th and 10th 2015) with the following fields:
```javascript
     {"MONTH": 1,
      "DAY": 4,
      "DAY_OF_WEEK": 7,
      "AIRLINE": "DL",
      "FLIGHT_NUMBER": "2336",
      "ORIGIN_AIRPORT": "DEN",
      "DESTINATION_AIRPORT": "ATL",
      "SCHEDULED_DEPARTURE": "0030",
      "DISTANCE": "1199",
      "SCHEDULED_ARRIVAL": "0523"}
```
Days in the week are coded as Monday=1 through Sunday=7.

Finding and realizing an answer to a question is described in `query_flight_db.py`. When this file is called as a main program, it realizes the answers for all examples in `{test|train}.json`. This allows testing the answering process on many intentions. 

Given the information available in the database, only a subset of intentions are dealt with (_flight_, _airfare_, _airline_, _abbreviation_ and _day_name_) which account for the vast majority of cases. Less frequent intents such as _ground_service_, _capacity_, _meal_ are not currently dealt with.  The _distance_ intent is not dealt with, even though there is an intercity distance information in the database,  because most of the questions ask for the distance between an airport and the nearby city, an information that is not available in our database.

Finding flights that satisfy a query is a relatively straightforward process:`extract_flight_info(entities: Entities) -> Info` maps the list of entities to a structure similar to the flight information in the database. 

`find_flights(info: Info) -> list[Flight]` traverses the list of flights and return the flights that match the values of the fields, an unspecified field  is ignored.

These functions are called from functions dealing with specific intents return list of strings that can either be printed or sent to a RASA process for display. 
For example `process_flight(_entities: Entities, info:Info) -> list[str] ` deals with the _flight_ intent which first realizes a sentence giving the number of flights between two airports reusing the function defined for questions. It then calls another function that returns a list of flights.
The functions for answering questions return list of strings that are either printed separated by a newline or sent to the NLG server of RASA.

## Implementing the RASA NLG server 

As described in [this document](RASA-INTRO.md), it is possible to define an NLG server that will realize an answer given an intent and entities identified by RASA. `nlg_server.py` shows an example that uses `pyrealb` for sentence realization. 
Two important issues to notice:
1. the response must be in JSON: this must be specified in the header and encoding and decoding must be performed before creating the JSON output
2. RASA limits the length of an answer (about 1K bytes) from an NLG server, which is reasonable in the context of a chatbot in which questions and answers should be kept short.  

```python
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json') # <-- the response is in json format
        self.end_headers()

    def do_POST(self):
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length).decode('utf-8') # <--- Gets the data itself
        fields = json.loads(post_data)
        response = fields["response"]
        message = fields["tracker"]["latest_message"]
        intent = message["intent"]["name"]
        entities = message.get("entities",[]) # fields: entity, value
        ## answer using pyrealb
        response_text = query_flight_db.process_intent_conversation(intent,entities)
        # there seems to be an undocumented limit on the length of the response accepted by RASA from an NLG server
        # around 1K, but we use slightly less to take into account the transformation into JSON
        limit = 900
        if len(response_text) > limit:
            last_nl_idx = response_text.rfind("\n",0,limit)  # skip to the last NL before limit
            response_text = response_text[:(last_nl_idx if last_nl_idx > 0 else limit)] + "\n..."
        response_json = json.dumps({"text":response_text}).encode("utf-8")
        self.wfile.write(response_json)
        self._set_response()
        self.wfile.write(json.dumps({"text":query_flight_db.process_intent(intent,entities)}).encode("utf-8"))
```

### Maintaining a conversation context

In the context of a flight information system, it can happen that there are (too) many possible answers for a given query (e.g. `show flights by American`). To avoid information overload for the user, the system only gives the number of flights found and ask for more information such as departure city or weekday for the travel. 

Here is an example of interaction with the RASA shell. The user query, shown here in bold, appears after the prompt `Your input ->`; the following lines are returned by the NLG server which uses `pyrealb` to realize the sentences. When a query would return too many different flights, the NLG server asks the user to be more precise. As the server keeps the context of the current conversation, the user does not have to repeat previously given information. 

Following the first greeting, the system indicates that it considers that the user is in Chicago and that the current day is Monday. This information is added to the context of any query. The second query being quite broad, it would return all flights of the database, so the system ask for details. The answer `American` is tagged by RASA as an airline, so the system indicates that there are still too many flights by this airline. So giving the destination and taking the current city as departure, the system identifies 14 daily flights. Note that similar flights are grouped so that the answer is more convenient for the user.

<pre><code>
Your input ->  <b>good morning</b>                                                     
Monday in Chicago: Hi, any flight information?

Your input ->  <b>show flights</b>                                                     
There are 4,269 flights. 
Can you give more details? such as your departure city, destination, weekday of departure or preferred airline.

Your input ->  <b>American</b>                                                         
There are 816 flights by American. 
Can you give more details? such as your departure city, destination or weekday of departure.

Your input ->  <b>to New York</b>                                                      
There are 14 flights from Chicago to New York by American. 
14 flights by American. 
AA149  19:55 => 23:05 everyday. 
AA198  12:55 => 16:05 everyday.
</code></pre>

Once a complete answer has been returned, the conversation context is reinitialized.

## Conclusion

This demo shows a way to use `pyrealb` to realize sentences (both questions and answers) from data in the form of 
tagged entities. It illustrates how `pyrealb` can be used for implementing an NLG server for generating text for a RASA chatbot.

## Contact: [Guy Lapalme](mailto:lapalme@iro.umontreal.ca)

## File organization
* `calculatebleu.py` : compute BLEU score between strings
* `convert_examples.py` : convert original data by adding roles and ensuring that flights only go between _known_ cities
* `Entities.py` : Python classes that simplify access to and modification of entities
* `flight_time.py` : function for dealing with time information in flights
* `Flights.py` : class for extracted Flight data from the database and list of flights
* `make_training_data.py` : convert `train.json` into yaml NLU files for RASA, in the `RASA_bot` directory
* `nlg_server.py` : RASA NLG server using `pyrealb`
* `parse_examples.py` : parse all examples from the `{train|test}.json` files and compute statistics, it can be parameterized to ensure that only airlines and cities in `flightDB.json` are used 
* `query_flight_db.py` : use information found by RASA and query the flight database and realize an answer. When called as main, call the answer process on the examples from `test.json`
* `RASA-Client.html` : web page to interact using an _official RASA chat widget_
* `RASA-INTRO.md` : introduction to RASA, relating my own experience and serving as a reminder for a simple use of RASA
* `README.md` : this file
* `realize_example.py` : realize an example using `pyrealb`
* `reproduce_examples.py` : main file to realize all examples both using the string based realizer and the one using `pyrealb`
* `requirements.txt` : list of dependencies created by `pip freeze` with Python 3.9.13
* `show_example.py` : realize an example using Python string manipulation, mainly concatenation
* `Examples` directory:
  * `train-orig.json`: [original test data ](https://github.com/howl-anderson/ATIS_dataset/blob/master/README.en-US.md)
  * `train.json`: result created by `convertJSON.py`
  * `test-orig.json`: [original test data ](https://github.com/howl-anderson/ATIS_dataset/blob/master/README.en-US.md)
  * `test.json`: result created by `convertJSON.py`
* `Flight Data` directory:
  * Original Directory from [Kaggle](https://www.kaggle.com/datasets/usdot/flight-delays)
  * `selectFlights.py` : create `flightDB.json` by choosing only a few flights
  * `airlines.csv` : selected airlines (done manually)
  * `airports.csv` : selected airports (done manually)
  * `flightDB.json` : selected airlines, airports and flights
* `images` : images for Markdown files
* `RASA_BOT` directory with already a few configuration files (use a copy for testing):
  * `actions` directory in which the RASA custom action is defined, the RASA action server should be run in this directory.
  * `data` directory : its content is filled by `make_training_data.py`
  * `models` : trained model with default parameters
  * `config.yml` : configuration file for RASA
  * `credentials.yml` : credentials for RASA (especially for making the _chat widget_ available)
  * `domain.yml` : list of all intents (created by `make_training_data.py`)
  * `endpoints.yml` : information for RASA (especially for making the _NLG server_ available)

## Steps for creating data and running the system
1. Select Flight [data](https://www.kaggle.com/datasets/usdot/flight-delays)
   1. select airlines in `airlines.csv`
   2. select airports in `airports.csv`
   3. run `Flight Data/selectFlights.py`
2. Convert [examples](Examples) with `convert_examples.py`
3. Check that the examples can be reproduced with and without `pyrealb` using `reproduce_examples.py`
4. Answer all example questions with `query_flight_db.py`
5. Run with RASA as discussed [above](#Launching-the-RASA-bot)