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
    


# Import-guard / pytest-guard

if __name__ == '__main__':

    # Input conditions
    def guess_checker(guess, guess_list):
        # If guess makes any condition FALSE, loop runs


        cond1 = len(guess) ==1  
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
            if cond1 is False:
                print("Enter one letter only.", end=" ")
            else:    
                if cond2 is False:
                    print(f"Already guessed '{guess}'.", end=" ")
                    
                if cond3 is False:
                    print("Guess should be a alphabets.", end=" ")
                    
                elif cond4 is False:
                    print("Guess should be a lowercase.", end=" ")
                

            guess = input("Enter another guess: ")

            # Updating conditions
            
            cond1 = set(guess) & set(guess_list) == set()
            cond2 = len(guess) ==1  
            cond3 = guess.isalpha()
            cond4 = guess.islower()
            conditions = [cond1, cond2, cond3, cond4]
            
        return guess

    


    print("""
    Welcome to hangman!
    You have to guess the secret word with in 10 tries.
    """)


    secret_word = get_secret_word()
    guesslist = ""
    formatter = "\nGuesses left :{:^3}   Word:{:^15}    Guessed:{:<10}"


    for i in range(10):
        print(  formatter.format( 10-i, mask_word(secret_word, guesslist),"".join(sorted( set(guesslist) )) )  )

        if secret_word is mask_word(secret_word, guesslist):
            print("Congratulations!")
            break

        newguess = input("Enter next guess: ")
        newguess = guess_checker(newguess, guesslist)

        guesslist += newguess

    print(f"Too bad! The secret word was '{secret_word}'")

