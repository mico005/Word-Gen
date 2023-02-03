import json
import random



def randomize_word_letters(word):
    word_list = list(word)
    random.shuffle(word_list)

    return "".join(word_list)


def randomize_words_in_file(file_name):
    with open(file_name, 'r') as f:
        word_list = json.load(f)
    randomized_word_list = [randomize_word_letters(word) for word in word_list]
    with open('randomized_words.json', 'w') as f:

        json.dump(randomized_word_list, f)


randomize_words_in_file('words.json')
