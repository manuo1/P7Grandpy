TEST_GOOGLE_DATA = {
    'address': 'test address', 'lat': 99, 'lng': 99, 'status': 'ok',
    'map_url': ("https://maps.googleapis.com/test")
}
TEST_WIKIPEDIA_DATA = {
    'name': 'test name',
    'page_id': 999999,
    'wikipedia_url': 'https://fr.wikipedia.org/test',
    'status': 'ok',
    'description': ('test description')
}
ANSW_REQUEST_GET_GEOCODING_API = {
    'results': [{
        'formatted_address': 'test address',
        'geometry': {'location': {'lat': 99, 'lng': 99}}}],
    'status': 'OK'
}
ANSW_REQUEST_GET_WIKIPEDIA_GEOSEARCH = {
    'query': { 'geosearch': [{ 'pageid': 999999,'title': 'test name' }]}
}

ANSW_REQUEST_GET_WIKIPEDIA_DESCRIPTION ={
    'query': { 'pages': { '999999': { 'extract': 'test description' }}}}
