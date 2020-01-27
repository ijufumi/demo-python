import re
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

import lark_module


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


class ActionConversation(Action):
    def name(self) -> Text:
        return "action_conversation"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        state = tracker.current_state()
        print("current_state: {}".format(state))

        input_text = state['latest_message'].get('text')
        latest_bot = None
        for event in reversed(state['events']):
            if event['event'] == 'bot':
                data = event.get('data', {}).get('custom', {}).get('data', [])
                latest_bot = data[0] if len(data) > 0 else None
                break

        print("latest_bot: {}".format(latest_bot))
        if not latest_bot:
            print("use utter_conversation_1")
            dispatcher.utter_message(template="utter_conversation_1", json_message={"data": {"key1": "value1",
                                                                                             "key2": "value2"}})
        else:
            if latest_bot == 'conversation_1':
                print("use utter_conversation_2")
                dispatcher.utter_message(template="utter_conversation_2", json_message={"data": ["conversation_2"]})
            elif latest_bot == 'conversation_2':
                result = re.match("\\d+", input_text)
                if result:
                    print("use utter_conversation_3")
                    dispatcher.utter_message(template="utter_conversation_3", json_message={"data": ["conversation_3"]})
                else:
                    print("use utter_conversation_2")
                    dispatcher.utter_message(template="utter_conversation_2", json_message={"data": ["conversation_2"]})
            elif latest_bot == 'conversation_3':
                result = re.match("\\d+", input_text)
                if not result:
                    print("use utter_conversation_3")
                    dispatcher.utter_message(template="utter_conversation_3", json_message={"data": ["conversation_3"]})
                else:
                    dispatcher.utter_message(text="Bye", json_message={"data": ["conversation_3"]})
            else:
                dispatcher.utter_message(text="Bye", json_message={"data": ["conversation_3"]})

        return []


class ActionConversation2(Action):
    action_state = {}

    def name(self) -> Text:
        return "action_conversation2"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        state = tracker.current_state()
        sender_id = state.get("sender_id")
        current_action = self.action_state.get(sender_id)
        input_text = state['latest_message'].get('text')
        print("state: {}, current_action: {}".format(state, current_action))
        if current_action:
            result = lark_module.execute(input_text)
            if result:
                dispatcher.utter_message(text=result, json_message={"data": ["step2"]},
                                         elements=[{"data": ["step2"]}])
            else:
                dispatcher.utter_message(text="Bye", json_message={"data": ["step3"]})
        else:
            dispatcher.utter_message(text="Where are you from ?", json_message={"data": ["step3"]})
            self.action_state[sender_id] = "get_start"

        return []
