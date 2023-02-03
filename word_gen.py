import random


def remove_double_consonants(word, vowels="aeiou", consonants="bcdfghjklmnpqrstvwxyz"):
    i = 0
    while i < len(word) - 1:
        if word[i] in consonants and word[i + 1] == word[i]:
            if i == 0 and word[i + 1] == word[i]:
                word = word[1:]
            elif (i > 0 and i < len(word) - 2 and word[i + 1] == word[i] and
                  word[i:i + 3] != "ngg" and (word[i - 1] not in vowels) and (word[i + 2] not in vowels)):
                word = word[:i + 1] + word[i + 2:]
                i -= 1
            elif i == len(word) - 2 and word[i + 1] == word[i]:
                word = word[:-1]
        i += 1
    return word


def replace_uu_ii(word):
    word = word.replace("uu", "oo")
    word = word.replace("ii", "y")
    return word


def generate_syllable(vowels="aeiou", consonants="bcdfghjklmnpqrstvwxyz", pattern=None):
    vowel = vowels if vowels else "aeiou"
    consonant = consonants if consonants else "bcdfghjklmnpqrstvwxyz"
    syllable = ""
    pattern = pattern if pattern else "vc"
    for letter in pattern:
        if letter == "v":
            syllable += random.choice(vowel)
        elif letter == "c":
            syllable += random.choice(consonant)
    return syllable


def generate_word(syllables, vowels="aeiou", consonants="bcdfghjklmnpqrstvwxyz", pattern=None):
    word = ""
    syllables = syllables if syllables > 0 else random.randint(1, 10)
    for i in range(syllables):
        word += generate_syllable(vowels, consonants, pattern)
    word = remove_double_consonants(word, consonants)
    word = replace_uu_ii(word)
    return word


def generate_word_list(num_words, syllables, vowels="aeiou", consonants="bcdfghjklmnpqrstvwxyz", pattern=None):
    word_list = []
    while len(word_list) < num_words:
        new_word = generate_word(syllables, vowels, consonants, pattern)
        if new_word not in word_list:
            word_list.append(new_word)
    return list(set(word_list))
