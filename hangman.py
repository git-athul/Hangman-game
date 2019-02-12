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
    for i in s_word:
        mask.append("*")
        
    for i in guessed:
        for j in s_word:
            if i==j:
                for k in indices(s_word,i):
                    mask[k-1]=i
    return "".join(mask)



# checks input-condition 1: One letter guesses
def check_cond1(guessed):
    if len(guessed) == 1:
        return "",True
    return "Only a single letter is allowed", False

# checks input-condition 2: No repetitive guesses
def check_cond2(guessed, guess_list):
    if not guessed in guess_list:
        return "",True
    return "Already guessed '{}'".format(guessed), False

# checks input-condition 3: Only alphabets
def check_cond3(guessed):
    if guessed.isalpha():
        return "",True
    return "Only alphabets are allowed", False

# input-condition 4: changes uppercase to lowercase
def upper_to_lower(guess):
    if guess.isupper():
        return guess.lower()
    return guess


# guess_evaluator: checks all the input-conditions
def guess_evaluator(guessed, guess_list):
    guessed = upper_to_lower(guessed)
    
    if not check_cond1(guessed)[1]:
        return check_cond1(guessed)
    if not check_cond2(guessed, guess_list)[1]:
        return check_cond2(guessed, guess_list)
    if not check_cond3(guessed)[1]:
        return check_cond3(guessed)
    
    return "", True


# guess_manager: prints string for failed input-condition and asks for new input
def guess_manager(guessed, guess_list):
    while not guess_evaluator(guessed, guess_list)[1]:
        print( guess_evaluator(guessed, guess_list)[0] )
        guessed = input("Enter another guess: ")
    return guessed    
    

# wrong_guess: returns the number of wrong guesses
def wrong_guesses(s_word,guess_list):
    count = 0
    for i in guess_list:
        if i not in s_word:
            count +=1
    return count



def playloop(secret_word):
    formatter = "\nWord: {:^15}    Life:{:<12}   Guessed: {:<10}"
    guesslist = ""
    game_won = "no"

    # Game losses when 6 guesses are wrong
    while not wrong_guesses(secret_word, guesslist) == 6:
        newguess = input("Enter a guess: ")
        newguess = guess_manager(newguess, guesslist) # Checking conditions

        guesslist += newguess                         # guesslist updates
        guesslist = "".join(sorted(set(guesslist)))   # sorting guesslist

        life = (6 - wrong_guesses(secret_word,guesslist) )*" \u2665"
        
        print(  formatter.format( mask_word(secret_word, guesslist), life, guesslist )  )

        if secret_word == mask_word(secret_word, guesslist):
            print("\n\nCongratulations!")
            game_won = "yes"
            break

    if game_won == "no":
        time.sleep(0.5)    
        print("\nToo bad! The secret word was '{}'".format(secret_word))

        
def main():
    secret_word = get_secret_word()
    
    print("""
    Welcome to hangman!
    You have to guess the secret-word before 6 wrong tries.
    Secret-word have {} letters.
    """.format(len(secret_word)) )

    playloop(secret_word)

    
# import-guard
if __name__ == '__main__':
    main()
