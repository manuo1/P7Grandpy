import requests

from .api_config.settings import (GOOGLE_MAPS_API_PRIVATE_KEY as private_key,
                                    GOOGLE_MAPS_API_PUBLIC_KEY as public_key)
from .constants import GOOGLE_MAPS_STATIC_API_URL as url
from .constants import GOOGLE_MAPS_STATIC_PARAMATERS as params


class GoogleMapsStatic:
    def __init__(self):
        pass

    def get_map_url_for(self, google_data):
        """get the url of a static map with google maps static api."""
        lat = str(google_data['lat'])
        lng = str(google_data['lng'])
        google_map_url = ''
        params["markers"] = lat + ',' + lng
        params['key'] = private_key
        try:
            server_response = requests.get(url=url, params=params)
        except requests.ConnectionError:
            pass
        if server_response.url:
            google_map_url = server_response.url
            google_map_url = google_map_url.replace(private_key, public_key)
        return google_map_url
