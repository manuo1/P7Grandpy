import random

from .constants import (ANSWER_TO_PROBLEM, INTRO_ADDRESS, INTRO_DESCRIPTION,
                        INTRO_MAP, INTRO_MAX_SIZE, INTRO_NAME,
                        ANWS_BLANK, ANWS_CANT_FIND, ANWS_NONALLOWED)


class Answer:
    def __init__(self):
        pass

    def stops_because(self, problem):
        """return an answer to each problem during the search for the answer
        data."""
        answers_list = globals()[ANSWER_TO_PROBLEM[problem]]
        answer = {
            'status': 'problem',
            'grandpyMessage': random.choice(answers_list),
        }
        return answer

    def builds_with_data(self, google_data, wikipedia_data):
        """
        build grandpy answer with location data.
        """
        description = wikipedia_data['description']
        description_first_part = description
        description_collapsible_part = ''
        """if the description is too long, split the message"""
        if len(description) > INTRO_MAX_SIZE:
            description_first_part = description[: INTRO_MAX_SIZE - 1]
            description_collapsible_part = description[INTRO_MAX_SIZE - 1:]
        """includes all parts of the answer"""
        answer = {
            'intro_name': random.choice(INTRO_NAME),
            'name': wikipedia_data['name'],
            'intro_address': random.choice(INTRO_ADDRESS),
            'address': google_data['address'],
            'intro_map': random.choice(INTRO_MAP),
            'map_url': google_data['map_url'],
            'intro_description': random.choice(INTRO_DESCRIPTION),
            'description_first_part': description_first_part,
            'description_collapsible_part': description_collapsible_part,
            'wikipedia_url': wikipedia_data['wikipedia_url'],
        }
        answer = {'status': 'ok', 'grandpyMessage': answer}
        return answer
