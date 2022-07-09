from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
import requests
import random

class get_random_weapon(Action):
   def name(self) -> Text:
        return "get_random_weapon"
   def run(self, dispatcher, tracker, domain):
       current = requests.get(
           ('https://www.dnd5eapi.co/api/equipment-categories/weapon')).json()
       random_index = random.randrange(len(current['equipment']))
       random_item = current['equipment'][random_index]['url']
       print(random_item)
       item_detail = requests.get(
           ('https://www.dnd5eapi.co{}').format(random_item)).json()
       print(item_detail['name'])
       dispatcher.utter_message(response = "utter_sell", item = item_detail['name'])
