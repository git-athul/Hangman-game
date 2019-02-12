# hangman.py

import random
import time

# finds secret_word that satisfies certain conditions
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


# finds indices of 'element' from 'string'
def indices(string,element):
    count = 1
    ind = []
    for i in string:
        if i == element:
            ind.append(count)
        count += 1
    return ind

# masks letters in 's_word' unless they are in 'guessed'
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



# checks condition 1: One letter guesses
def check_cond1(guessed):
    if len(guessed) == 1:
        return True
    return "Only a single letter is allowed", False

# checks condition 2: No repetitive guesses
def check_cond2(guessed, guess_list):
    if guessed in guess_list:
        return True
    return "Already guessed {}".format(guessed), False

# checks condition 3: Only alphabets
def check_cond3(guessed):
    if guessed.isalpha():
        return True
    return "Only alphabets are allowed", False

# changes uppercase to lowercase
def upper_to_lower(guess):
    if guess.isupper():
        return guess.islower()
    return guess


# guess checker
def guess_checker(guessed, guess_list):
    c1 = check_cond1(guessed)
    c2 = check_cond2(guessed, guess_list)
    c3 = check_cond3(guessed)
    c4 = upper_to_lower(guessed)

    conditions = [c1, c2, c3, c4]

    for i in conditions:
        if i:
            return i
        break
    return "", True
        

# checks whether a guess is right or wrong; and collects wrong guess
def wrong_guess(s_word,guessed):
    if set(s_word) & set(guessed) == set(): 
        return guessed
    else:
        return ""    



    
# Import-guard / pytest-guard

if __name__ == '__main__':

    # Input conditions
    print("""
    Welcome to hangman!
    You have to guess the secret-word with in 6 wrong tries.""")


    secret_word = get_secret_word()
    print("    Secret-word is a {} letter word.\n".format(len(secret_word)))

    wrong_guesses = ""
    guesslist = ""
    formatter = "\nWord: {:^15}    Life:{:^12}   Guessed: {:<10}"

    game_won = "no"
    
    while not len(wrong_guesses) == 6:
        newguess = input("Enter a guess: ")
        # Checking conditions
        newguess = guess_checker(newguess, guesslist)
        
        wrong_guesses += wrong_guess(secret_word,newguess)
        life = (6 - len(wrong_guesses) )*" \u2665"

        guesslist += newguess
        guessed = "".join(sorted( set(guesslist) ))

        print(  formatter.format( mask_word(secret_word, guesslist), life, guessed )  )

        if secret_word == mask_word(secret_word, guesslist):
            print("\n\nCongratulations!")
            game_won = "yes"
            break

    if game_won == "no":
        time.sleep(0.5)    
        print("\nToo bad! The secret word was '{}'".format(secret_word))

    
