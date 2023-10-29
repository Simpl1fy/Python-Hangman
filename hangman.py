import random
from words import words
import string

def get_valid_words(words):
    word = random.choice(words)
    if '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    randomWord = get_valid_words(words)
    letters_word = set(randomWord)
    alphabets = set(string.ascii_uppercase)
    usedLetter = set()

    userLetter = input("Enter a letter: ")
    if userLetter in alphabets - usedLetter:
        usedLetter.add(userLetter)
        if userLetter in letters_word:
            letters_word.remove(userLetter)
            print(usedLetter)
    
    elif userLetter in usedLetter:
        print("You have already used that letter. Please try again!")
    
    else:
        print("That is not a letter, Please try again!")


hangman()
