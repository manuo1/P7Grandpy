
from grandpy.grandpy_answers.answer import Answer
from grandpy.grandpy_answers.constants import (
    ANWS_BLANK, ANWS_CANT_FIND, ANWS_NONALLOWED,
    INTRO_NAME, INTRO_ADDRESS, INTRO_MAP, INTRO_DESCRIPTION, INTRO_MAX_SIZE)
from .constants import (
    TEST_GOOGLE_DATA as google_data,
    TEST_WIKIPEDIA_DATA as wikipedia_data)

def test_if_stops_because_function_work():
    """
    test whether grandpy's reply in case of a problem contains
    one of the planned texts.
    """
    answer1 = Answer.stops_because(Answer, 'blank_new_user_message')
    answer2 = Answer.stops_because(Answer, 'nonallowed_characters')
    answer3 = Answer.stops_because(Answer, 'cant_find_location')
    assert ( answer1['grandpyMessage'] in ANWS_BLANK
            and answer2['grandpyMessage'] in ANWS_NONALLOWED
            and answer3['grandpyMessage'] in ANWS_CANT_FIND )

def test_if_builds_with_data_function_work():
    """
    check if grandpy's answer contains all the expected data
    """
    answer = Answer.builds_with_data(Answer, google_data, wikipedia_data)
    assert ( answer['status'] == 'ok'
        and answer['grandpyMessage']['intro_name'] in INTRO_NAME
        and answer['grandpyMessage']['intro_address'] in INTRO_ADDRESS
        and answer['grandpyMessage']['intro_map'] in INTRO_MAP
        and answer['grandpyMessage']['intro_description'] in INTRO_DESCRIPTION
        and answer['grandpyMessage']['name'] == wikipedia_data['name']
        and answer['grandpyMessage']['address'] == google_data['address']
        and answer['grandpyMessage']['map_url'] == google_data['map_url']
        and answer['grandpyMessage']['description_first_part'] == (
            wikipedia_data['description'][:INTRO_MAX_SIZE-1])
        and answer['grandpyMessage']['description_collapsible_part'] == (
            wikipedia_data['description'][INTRO_MAX_SIZE-1:])
        and answer['grandpyMessage']['wikipedia_url'] == (
            wikipedia_data['wikipedia_url'])
)
