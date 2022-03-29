from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
import requests
import random


class ActionGetMonster(Action):
   def name(self) -> Text:
        return "action_get_monster"
   def run(self, dispatcher, tracker, domain):
       rating = tracker.get_slot('rating')
       current = requests.get(
           ('https://www.dnd5eapi.co/api/monsters/?challenge_rating={}').format(rating)).json()
       random_index = random.randrange(current['count'])
       random_monster = current['results'][random_index]['index']
       monster_detail = requests.get(
           ('https://www.dnd5eapi.co/api/monsters/{}').format(random_monster)).json()
       response = """Prepare to face the {}.""".format(
           monster_detail['name'])
       dispatcher.utter_message(response)
