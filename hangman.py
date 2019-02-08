# hangman.py

import random

def get_secret_word(word_file="/usr/share/dict/words"):
    with open(word_file) as f:
        good_words = []
        for i in f:
            i = i.strip()
            if len(i) <= 6:     # No short words
                continue
            if not i.isalpha(): # No punctuation
                continue
            if i[0].isupper():  # No proper nouns
                continue
            good_words.append(i)
    return random.choice(good_words)


def mask_word(s_word,guessed):
    mask = []
    for i in range(len(s_word)):
        mask.append("*")
        
    for i in guessed:
        for j in s_word:
            if i==j:
                mask[s_word.index(j)]=i

    return "".join(mask)




