from flask import Flask, jsonify, render_template, request

from grandpy.data_search.google_geocoding import GoogleGeocoding
from grandpy.data_search.google_maps_static import GoogleMapsStatic
from grandpy.data_search.parser import Parser
from grandpy.data_search.wikipedia_description import WikipediaDescription
from grandpy.data_search.wikipedia_geosearch import WikipediaGeosearch
from grandpy.grandpy_answers.answer import Answer

grandpy_app = Flask(__name__)


@grandpy_app.route('/')
def index():
    """routing the index page."""
    return render_template('index.html')


@grandpy_app.route('/newUserMessage', methods=['POST'])
def newUserMessage():
    """routing the user message from ajax, return grandpy's answer."""
    google_data = {}
    wikipedia_data = {}
    user_message = request.form['newUserMessage']
    answer = Answer()
    """checks the user message"""
    if not user_message:
        return jsonify(answer.stops_because('blank_new_user_message'))
    if user_message == 'nonallowed_characters':
        return jsonify(answer.stops_because('nonallowed_characters'))
    """uses the parser to remove unnecessary parts of the user message"""
    parser = Parser()
    cleaned_message = parser.clean_the_message(user_message)
    if not cleaned_message:
        return jsonify(answer.stops_because('cant_find_location'))
    """get address and coordinates of the location in the user's message"""
    google_geocoding = GoogleGeocoding()
    google_data = google_geocoding.find_location_in_message(cleaned_message)
    if not google_data['status'] == 'ok':
        return jsonify(answer.stops_because('cant_find_location'))
    """get the map url for location coordinates"""
    google_maps_static = GoogleMapsStatic()
    google_data['map_url'] = google_maps_static.get_map_url_for(google_data)
    if not google_data['map_url']:
        return jsonify(answer.stops_because('cant_find_location'))
    """get name, wikipedia page_id and url for location coordinates"""
    wikipedia_geosearch = WikipediaGeosearch()
    wikipedia_data = wikipedia_geosearch.get_data(google_data)
    if not wikipedia_data['status'] == 'ok':
        return jsonify(answer.stops_because('cant_find_location'))
    """get description about the location"""
    wikipedia_description = WikipediaDescription()
    wikipedia_data['description'] = wikipedia_description.get_data(
        wikipedia_data
    )
    if not wikipedia_data['description']:
        return jsonify(answer.stops_because('cant_find_location'))
    """
    if all location data is available, build grandpy's answer
    """
    grandpy_answer = answer.builds_with_data(google_data, wikipedia_data)
    return jsonify(grandpy_answer)

"""
if __name__ == "__main__":
    #grandpy_app.run(debug=True)
    grandpy_app.run()
"""
