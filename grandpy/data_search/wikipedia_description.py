import requests

from .constants import WIKIPEDIA_API_URL as url
from .constants import WIKIPEDIA_EXTRACT_INTRO_PARAMETERS as params


class WikipediaDescription:
    def __init__(self):
        pass

    def get_data(self, wikipedia_data):
        """get from wikipedia API short description."""
        description = ''
        page_id = wikipedia_data['page_id']
        params['pageids'] = page_id
        try:
            server_response = requests.get(url=url, params=params)
            data = server_response.json()
        except requests.ConnectionError:
            pass
        if data['query']['pages'][str(page_id)]['extract']:
            description = data['query']['pages'][str(page_id)]['extract']
        return description
