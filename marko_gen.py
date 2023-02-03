import json
import nltk
from nltk.corpus import words


def get_words_and_write_to_file(file_name):
    nltk.download('words')
    word_list = list(set(words.words()))
    with open(file_name, 'w') as f:
        json.dump(word_list, f)


get_words_and_write_to_file('words.json')
