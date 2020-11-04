
from grandpy.data_search.wikipedia_description import WikipediaDescription
from .constants import ANSW_REQUEST_GET_WIKIPEDIA_DESCRIPTION

def test_if_get_data_function_work(monkeypatch):
    wikipedia_data = {'page_id': 999999}

    class MockRequestsGet:
        def __init__(self, url, params):
            self.status_code = 200
        def json(self):
            return ANSW_REQUEST_GET_WIKIPEDIA_DESCRIPTION

    monkeypatch.setattr('requests.get', MockRequestsGet)
    assert WikipediaDescription.get_data(
        WikipediaDescription, wikipedia_data) == ('test description')
