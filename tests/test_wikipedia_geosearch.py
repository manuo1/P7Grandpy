
from grandpy.data_search.wikipedia_geosearch import WikipediaGeosearch
from .constants import ANSW_REQUEST_GET_WIKIPEDIA_GEOSEARCH


def test_if_get_data_function_work(monkeypatch):
    google_geocoding_data = {'lat': 99, 'lng': 99}

    class MockRequestsGet:
        def __init__(self, url, params):
            self.status_code = 200
        def json(self):
            return ANSW_REQUEST_GET_WIKIPEDIA_GEOSEARCH

    monkeypatch.setattr('requests.get', MockRequestsGet)
    assert WikipediaGeosearch.get_data(
        WikipediaGeosearch, google_geocoding_data) == ({
            'name': 'test name',
            'page_id': 999999,
            'wikipedia_url': 'https://fr.wikipedia.org/wiki?curid=999999',
            'status': 'ok'})
