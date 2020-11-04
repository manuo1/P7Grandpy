import requests

from .api_config.settings import GOOGLE_MAPS_API_PRIVATE_KEY as api_key
from .constants import GOOGLE_GEOCODING_API_URL as url
from .constants import GOOGLE_GEOCODING_PARAMATERS as params


class GoogleGeocoding:
    def __init__(self):
        pass

    def find_location_in_message(self, message):
        """get from googlemaps geocoding API address and coordinates."""
        google_data = {'status': 'problem'}
        message = message.replace(" ", "+")
        params['address'] = message
        params['key'] = api_key
        try:
            server_response = requests.get(url=url, params=params)
            data = server_response.json()
        except requests.ConnectionError:
            pass
        if data["status"] == "OK":
            data = data["results"][0]
            google_data = {
                "address": data["formatted_address"],
                "lat": round(data["geometry"]["location"]["lat"], 6),
                "lng": round(data["geometry"]["location"]["lng"], 6),
            }
            if all(google_data.values()):
                google_data['status'] = 'ok'
        return google_data
