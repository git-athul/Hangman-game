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



# Import-guard / pytest-guard

if __name__ == '__main__':

    # Input conditions
    def guess_checker(guess, guess_list):
        # If 'guess' makes any of the condition FALSE, loop runs


        cond1 = len(guess) == 1  
        # One letter guesses 
        
        cond2 = set(guess) & set(guess_list) == set()
        # No repetitive guesses
        # guess should not be a set element in guess_list

        cond3 = guess.isalpha()
        # Only alphabets

        cond4 = guess.islower()
        # Only lower-case

        conditions = [cond1, cond2, cond3, cond4]

        while not all(conditions):
            # Primary condition
            if cond1 is False:
                print("Enter one letter only.", end=" ")
            else:
                # Secondary conditions
                if cond2 is False:
                    print(f"Already guessed '{guess}'.", end=" ")

                if cond3 is False:
                    print("Guess should be a alphabet.", end=" ")

                elif cond4 is False:
                    print("Guess should be a lowercase.", end=" ")
                

            guess = input("Enter another guess: ")

            
            # Updating conditions

            cond1 = len(guess) ==1  
            cond2 = set(guess) & set(guess_list) == set()
            cond3 = guess.isalpha()
            cond4 = guess.islower()
            conditions = [cond1, cond2, cond3, cond4]

            # Loops runs until all the conditions are satisfied
            
        return guess

    


    print("""
    Welcome to hangman!
    You have to guess the secret-word with in 10 tries.""")


    secret_word = get_secret_word()
    print(f"    Secret-word is a {len(secret_word)} letter word.\n")
    
    guesslist = ""
    formatter = "\nGuesses left:{:^3}   Word:{:^15}    Guessed:{:<10}"


    for i in range(10):
        newguess = input("Enter a guess: ")
        # Checking conditions
        newguess = guess_checker(newguess, guesslist)

        guesslist += newguess
        guessed = "".join(sorted( set(guesslist) ))

        print(  formatter.format( 9-i, mask_word(secret_word, guesslist),guessed )  )

        if secret_word is mask_word(secret_word, guesslist):
            print("\n\nCongratulations!")
            break

    time.sleep(0.5)    
    print(f"\nToo bad! The secret word was '{secret_word}'")

