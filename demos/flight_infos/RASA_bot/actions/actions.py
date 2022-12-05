#  CAUTION: this file is not used in this demo
#  it is left there as an example of how to retrieve information in a custom action

# RASA custom action according to
# https://rasa.com/docs/rasa/custom-actions

from typing import Any

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

# specific to flight_infos demo (path should be updated)
# Strange imports because of the specifics of the RASA loader
# see HACK described in https://forum.rasa.com/t/import-custom-module-in-actions-py/44793/2
from .. import realize_example
from .. import query_flight_db
from .. import Entities_module
Entity = Entities_module.Entity
Entities = Entities_module.Entities

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
