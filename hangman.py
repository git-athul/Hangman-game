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


def indices(string,element):
    count = 1
    ind = []
    for i in string:
        if i == element:
            ind.append(count)
        count += 1
    return ind


def mask_word(s_word,guessed):
    mask = []
    for i in range(len(s_word)):
        mask.append("*")
        
    for i in guessed:
        for j in s_word:
            if i==j:
                for k in indices(s_word,i):
                    mask[k-1]=i
    return "".join(mask)



def number_of_guesses(guessed):
    return len(guessed)
    


print("""
Welcome to hangman!
You have to guess the secret word with in 10 tries.
""")


secret_word = get_secret_word()
guesslist = ""
formatter = "Guesses left :{:^3}   Word:{:^15}    Guessed:{:<10}"


for i in range(10):
    print(formatter.format(10-i, mask_word(secret_word, guesslist), guesslist))
    newguess = input("Enter next guess: ")
    guesslist += newguess

