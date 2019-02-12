# test_hangman.py

import hangman
# A. Getting secret word
# 1. Secret word should have atleast 6 letters
# 2. Secret word should have no punctuation
# 3. Secret word should not be a proper noun

def test_secret_word_6_letters():
    assert all(hangman.get_secret_word("./test_data/1.words") == "policeman" for _ in range(100))

def test_secret_word_no_punctuation():
    assert all(hangman.get_secret_word("./test_data/2.words") == "fireman" for _ in range(100))

def test_secret_word_no_proper_nouns():
    assert all(hangman.get_secret_word("./test_data/3.words") == "policeman" for _ in range(100))


# B. Masking secret word    
# 1. Masks entire word when not guessed.
# 2. Unmasks entire word when fully guessed.
# 3. Unmasks for words with repetitive letters.
#    Do not masks for wrong guesses.
    
def test_mask_word():
    word = "gangman"
    guess = ""
    assert hangman.mask_word(word, guess) == "*******"

def test_mask_word_guessed():
    words = ["python", "tigers","whales"]
    assert all([hangman.mask_word(i, i) == i for i in words])


def test_mask_word_repetitive():
    words = ["deadpool", "batman","greenlantern" ]
    guess = [ "kvwvkod", "qwewqa", "zxyxzen"]
    masks = ["d**d*oo*", "*a**a*" ,"**een**n*e*n"]

    assert all([ hangman.mask_word(words[i], guess[i]) == masks[i] for i in range(len(words)) ])


# C. Checking inputs
# 1. Condition1:  One letter guesses
# 2. Condition2:  No repetitive guesses

def test_check_cond1():
    guess =[ "you", "we", "them", "u", "i", "v" ]
    result=[False, False, False, True, True, True ]
    assert ([hangman.check_cond1(guess[i]) == result[i] for i in range(len(guess)) ])

def test_check_cond2():
    guess = [ "a", "b", "c", "d", "e", "f"]
    guess_list = "qawbrc"
    result=[False, False, False, True, True, True ]
    assert ([hangman.check_cond2(guess[i], guess_list) == result[i] for i in range(len(guess)) ])



    
# Counting wrong guesses

def test_wrong_guess():
    words = ["python", "tigers","whales","elephant"]
    guess = ["a","u","w","e"]
    result =["a","u","",""]
        
    assert all([ hangman.wrong_guess(words[i],guess[i]) == result[i] for i in range(len(words)) ])



def test_for_congratz():
    words = ["python", "tigers","whales","elephant"]
    assert all([ words[i] == hangman.mask_word(words[i], words[i]) for i in range(len(words)) ])
