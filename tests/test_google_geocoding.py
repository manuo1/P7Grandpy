
from grandpy.data_search.google_geocoding import GoogleGeocoding
from .constants import ANSW_REQUEST_GET_GEOCODING_API


def test_if_find_location_in_message_function_work(monkeypatch):
    message = 'test'

    class MockRequestsGet:
        def __init__(self, url, params):
            self.status_code = 200
        def json(self):
            return ANSW_REQUEST_GET_GEOCODING_API

    monkeypatch.setattr('requests.get', MockRequestsGet)
    assert GoogleGeocoding.find_location_in_message(
        GoogleGeocoding, message) == (
        {'address': 'test address', 'lat': 99, 'lng': 99, 'status': 'ok'} )
