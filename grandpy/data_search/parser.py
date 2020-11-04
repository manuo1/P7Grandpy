import re

from .constants import ACCENTS_DICT, STOPWORDS


class Parser:
    def __init__(self):
        pass

    def clean_the_message(self, message):
        """removes unnecessary elements from the user's message."""
        message = message.lower()
        message = self.replace_accents(message)
        message = self.remove_special_characters(message)
        message = self.remove_short_words(message)
        message = self.remove_stopwords(message)
        return message

    def replace_accents(self, message):
        """replace the accented letters with the unaccented letter."""
        for (char, accented_chars) in ACCENTS_DICT.items():
            for accented_char in accented_chars:
                message = message.replace(accented_char, char)
        return message

    def remove_special_characters(self, message):
        """remove all characters that are not simple letters and numbers."""
        message = re.sub("[^a-zA-Z0-9]", " ", message)
        return message

    def remove_short_words(self, message):
        """remove words smaller than 3 letters, keep numbers."""
        words_list = message.split()
        message = ''
        for word in words_list:
            if word.isdigit():
                message = message + ' ' + word
            else:
                if len(word) > 2:
                    message = message + ' ' + word
        message = message[1:]
        return message

    def remove_stopwords(self, message):
        """removes words that are in the stopwords list."""
        words_list = message.split()
        message = ''
        for word in words_list:
            if word not in STOPWORDS:
                message = message + ' ' + word
        message = message[1:]
        return message
