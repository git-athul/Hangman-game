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
    


# pytest guard

if __name__ == '__main__':

    # Input conditions
    def guess_checker(guess, guess_list):

        # No repetitive guesses
        # guess should not be a set element in guess_list
        while set(guess) & set(guess_list) != set():
            print(f"Already guessed '{guess}'", end=" ")
            guess = input("Enter another guess: ")

        # One letter guesses
        while len(guess) != 1:
            print("Enter one letter only.", end=" ")
            guess = input("Enter another guess: ")

        # Only alphabets
        while guess.isalpha()==False:
            print("Enter alphabets only.", end=" ")
            guess = input("Enter another guess: ")

        # Only lower-case
        while guess.isupper():
            print("Enter lower-case only.", end=" ")
            guess = input("Enter another guess: ")


        return guess

    


    print("""
    Welcome to hangman!
    You have to guess the secret word with in 10 tries.
    """)


    secret_word = get_secret_word()
    guesslist = ""
    formatter = "Guesses left :{:^3}   Word:{:^15}    Guessed:{:<10}"


    for i in range(10):
        print(formatter.format(10-i, mask_word(secret_word, guesslist), guesslist))

        if secret_word is mask_word(secret_word, guesslist):
            print("Congratulations!")
            break

        newguess = input("Enter next guess: ")
        guess_checker(newguess, guesslist)

        guesslist += newguess

    print(f"Too bad! The secret word was '{secret_word}'")

