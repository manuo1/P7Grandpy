import requests

from .constants import WIKIPEDIA_API_URL as url
from .constants import WIKIPEDIA_GEOSEARCH_PARAMATERS as params
from .constants import WIKIPEDIA_URL_PAGEID as page_id_url


class WikipediaGeosearch:
    def __init__(self):
        pass

    def get_data(self, google_geocoding_data):
        """get from wikipedia API name (title), page_id & url page."""
        lat = str(google_geocoding_data['lat'])
        lng = str(google_geocoding_data['lng'])
        wikipedia_data = {'status': 'problem'}
        params["gscoord"] = lat + '|' + lng
        try:
            server_response = requests.get(url=url, params=params)
            data = server_response.json()
        except requests.ConnectionError:
            pass
        if data['query']['geosearch']:
            data = data['query']['geosearch'][0]
            wikipedia_data = {
                'name': data['title'],
                'page_id': data['pageid'],
                'wikipedia_url': (page_id_url + str(data['pageid'])),
            }
            if all(wikipedia_data.values()):
                wikipedia_data['status'] = 'ok'
        return wikipedia_data
