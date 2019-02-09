# test_hangman.py

import hangman

# 1. Secret word should have atleast 6 letters
# 2. Secret word should have no punctuation
# 3. Secret word should not be a proper noun

def test_secret_word_6_letters():
    assert all(hangman.get_secret_word("./test_data/1.words") == "policeman" for _ in range(100))

def test_secret_word_no_punctuation():
    assert all(hangman.get_secret_word("./test_data/2.words") == "fireman" for _ in range(100))

def test_secret_word_no_proper_nouns():
    assert all(hangman.get_secret_word("./test_data/3.words") == "policeman" for _ in range(100))


# 1. Masking entire word when not guessed.
# 2. Unmasking entire word when fully guessed.
# 3. Unmasking for words with repetitive letters. Not masking for wrong guesses.
    
def test_mask_word():
    word = "gangman"
    guess = " "
    assert hangman.mask_word(word, guess) == "*******"

def test_mask_word_guessed():
    words = ["python", "tigers","whales"]
    assert all([hangman.mask_word(i, i) == i for i in words])


def test_mask_word_repetitive():
    words = ["deadpool", "batman","greenlantern" ]
    guess = [ "kvwvkod", "qwewqa", "zxyxzen"]
    masks = ["d**d*oo*", "*a**a*" ,"**een**n*e*n"]

    assert all([hangman.mask_word(words[i], guess[i]) == masks[i] for i in range(len(words)) ])
