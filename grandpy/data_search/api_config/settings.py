import os

import yaml

FILE_PATH = os.path.dirname(os.path.abspath(__file__))

try:
    """get, if it exists, the google maps development api key."""
    with open(os.path.join(FILE_PATH, "dev_google_maps_api_key.yaml")):
        GOOGLE_MAPS_API_KEY_FILE = os.path.join(
            FILE_PATH, "dev_google_maps_api_key.yaml"
        )
except IOError:
    try:
        """if there is no google maps api development key file, get the prod's
        one."""
        with open(os.path.join(FILE_PATH, "prod_google_maps_api_key.yaml")):
            GOOGLE_MAPS_API_KEY_FILE = os.path.join(
                FILE_PATH, "prod_google_maps_api_key.yaml"
            )
    except IOError:
        print('Error! The file containing the Google api key cannot be found.')
        quit()

with open(GOOGLE_MAPS_API_KEY_FILE) as file:
    DATA = yaml.load(file, Loader=yaml.FullLoader)
    GOOGLE_MAPS_API_PUBLIC_KEY = DATA['api_key_public']
    GOOGLE_MAPS_API_PRIVATE_KEY = DATA['api_key_private']
