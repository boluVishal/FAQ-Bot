import logging

from rasa_core_sdk import Action, Tracker
from rasa_core_sdk.forms import FormAction
from rasa_core_sdk.events import SlotSet, UserUtteranceReverted,ConversationPaused


logger = logging.getLogger(__name__)
class ActionFaqs(Action):
    """Returns the chitchat utterance dependent on the intent"""

    def name(self):
        return "action_faqs"

    def run(self, dispatcher, tracker, domain):
        intent = tracker.latest_message['intent'].get('name')

        # retrieve the correct chitchat utterance dependent on the intent
        if intent in ['ask_faq_platform', 'ask_faq_languages', 'ask_faq_tutorialcore', 'ask_faq_tutorialnlu',
                      'ask_faq_opensource', 'ask_faq_voice', 'ask_faq_slots', 'ask_faq_channels',
                      'ask_faq_differencecorenlu', 'ask_faq_python_version']:
            dispatcher.utter_template('utter_' + intent, tracker)
        return []
