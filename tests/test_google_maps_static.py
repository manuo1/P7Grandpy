
from grandpy.data_search.google_maps_static import GoogleMapsStatic

def test_if_get_map_url_for_function_work(monkeypatch):
    google_data = {
    'address': 'test_address',
    'lat': 99,
    'lng': 99,
    'status': 'ok'}
    class MockRequestsGet:
        def __init__(self, url, params):
            self.status_code = 200
            self.url = 'https://maps.googleapis.com/test'

    monkeypatch.setattr('requests.get', MockRequestsGet)

    assert GoogleMapsStatic.get_map_url_for(
        GoogleMapsStatic, google_data) == (
            'https://maps.googleapis.com/test' )
