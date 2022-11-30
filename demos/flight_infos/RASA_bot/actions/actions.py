# RASA custom action according to
# https://rasa.com/docs/rasa/custom-actions

from typing import Any

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

# specific to flight_infos demo
from response import realize_example
from response import query_flight_db
from response import Entities_module
Entity = Entities_module.Entity
Entities = Entities_module.Entities

import os

class GiveFlightInfo(Action):

    def name(self) -> str:
        return "give_flight_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict[str, Any]) -> list[dict[str, Any]]:
                
        message=tracker.latest_message
        intent = message["intent"]["name"]
        # show found information in the console
        print("** Intent:",intent,":",message.get("text"),"\n"+"\n".join(str(Entity(e)) for e in message["entities"]))
        print(realize_example.realize_example(intent,Entities(message["entities"])))
        # send the answer to the RASA shell or web chat bot
        dispatcher.utter_message(text=query_flight_db.process_intent(intent,message["entities"]))
        return []
