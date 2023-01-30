import random
import re


def generate_pattern():
    pattern = ""
    pattern_length = random.randint(2, 10)
    for i in range(pattern_length):
        pattern += random.choice("vcn")
    return pattern


def generate_word(vowels="aeiou", consonants="bcdfghjklmnpqrstvwxyz", nasals="mn", pattern=None):
    vowel = vowels if vowels else "aeiou"
    consonant = consonants if consonants else "bcdfghjklmnpqrstvwxyz"
    nasal = nasals if nasals else "mn"
    word = ""
    pattern = pattern if pattern else generate_pattern()
    pattern_length = len(pattern)
    for i in range(pattern_length):
        if pattern[i] == "v":
            word += random.choice(vowel)
        elif pattern[i] == "c":
            word += random.choice(consonant)
        elif pattern[i] == "n":
            word += random.choice(nasal)
    if re.search(r"["+vowel+"]{2,}", word) or re.search(r"["+consonant+"]{2,}", word) or re.search(r"["+nasal+"]{2,}", word):
        word = generate_word(vowel, consonant, nasal)
    return word


def generate_word_list(num_words, vowels="aeiou", consonants="bcdfghjklmnpqrstvwxyz", nasals="mn", pattern=None):
    word_list = []
    while len(word_list) < num_words:
        new_word = generate_word(vowels, consonants, nasals, pattern)
        if new_word not in word_list:
            word_list.append(new_word)
    return list(set(word_list))


result = generate_word_list(1000)

print(result)
print(len(result))
