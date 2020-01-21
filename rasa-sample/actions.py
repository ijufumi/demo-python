from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionHelloWorld(Action):
    state_map = {}

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        state = tracker.current_state()
        print("current_state: {}".format(state))
        sender_id = state["sender_id"]
        if sender_id not in self.state_map:
            self.state_map[sender_id] = 0

        self.state_map[sender_id] += 1

        dispatcher.utter_message(
            text="Hello World!",
            json_message={"data": "hogeohge"},
            # template="<div></div>",
            buttons=[{"title": "OK", "payload": "99!"}])

        print("state: {}".format(self.state_map[sender_id]))

        return []


class ActionCustomButton(Action):
    def name(self) -> Text:
        return "action_custom_button"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(
            text="Which ?",
            buttons=[{"title": "OK", "payload": "1"},
                     {"title": "NG", "payload": "2"},
                     {"title": "Unknown", "payload": "9"}])

        return []


class ActionJsonMessage(Action):
    def name(self) -> Text:
        return "action_json_message"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(
            text="Which ?",
            json_message={"data": {
                "key1": "value1",
                "key2": "value2",
            }}
)

        return []
