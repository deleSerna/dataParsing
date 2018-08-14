from rasa_core.actions import Action
from rasa_core.events import SlotSet

class ActionStoreName(Action):
    """Stores the users name in a slot"""

    def name(self):
        return "action_store_name"

    def run(self, dispatcher, tracker, domain):

        person_name = next(tracker.get_latest_entity_values('name'), None)

        # if no name was extracted, use the whole user utterance
        # in future this will be stored in a `name_unconfirmed` slot and the
        # user will be asked to confirm their name
        if not person_name:
            person_name = tracker.latest_message.text
        print "hereeeee"
        print person_name
        return [SlotSet('person_name', person_name)]  

