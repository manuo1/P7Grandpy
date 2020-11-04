
from grandpy.data_search.parser import Parser

"""
tests the simple functions of the parser
"""
def test_if_replace_accents_function_work():
    assert Parser.replace_accents(
                Parser, 'àãáâéèêëîïùüûôö') == ('aaaaeeeeiiuuuoo')

def test_if_remove_special_characters_function_work():
    assert Parser.remove_special_characters(
                Parser,"O!#$%&'()*+,-./:;<=>?@[]^_`k") == (
                'O                          k')

def test_if_remove_short_words_function_work():
    assert Parser.remove_short_words(Parser,'try if it work') == 'try work'

def test_if_remove_stopwords_function_work():
    assert Parser.remove_stopwords(
                Parser,
                'grandpy hello cinquantaine malgre world quarante voila')== (
                'hello world')
"""
mock for the complete cleaning function
"""
def mock_replace_accents(Parser):
    return "salut grandpy ! ou se trouve openclassrooms ?"

def mock_remove_special_characters(Parser):
    return "salut grandpy ou se trouve openclassrooms "

def mock_remove_short_words(Parser):
    return "salut grandpy trouve openclassrooms "

def mock_remove_stopwords(Parser):
    return "trouve openclassrooms"
"""
test of the complete cleaning function with the mok
"""
def test_if_clean_the_message_function_work(monkeypatch):
    monkeypatch.setattr(
                    'grandpy.data_search.parser.Parser.replace_accents',
                    mock_replace_accents)
    monkeypatch.setattr(
                    'grandpy.data_search.parser.Parser.remove_special_characters',
                    mock_remove_special_characters)
    monkeypatch.setattr(
                    'grandpy.data_search.parser.Parser.remove_short_words',
                    mock_remove_short_words)
    monkeypatch.setattr(
                    'grandpy.data_search.parser.Parser.remove_stopwords',
                    mock_remove_stopwords)
    assert Parser.clean_the_message(
                    Parser,"Salut GrandPy ! Où se trouve OpenClassrooms ?") == (
                    "trouve openclassrooms")
