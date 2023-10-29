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
    randomWord.upper()
    letters_word = set(randomWord)
    alphabets = set(string.ascii_uppercase)
    used_Letter = set()
    lives = 10

    while len(letters_word) > 0 and lives > 0:

        # This statement is to print the guessed letters by the user
        print('Letters guessed = ', ' '.join(used_Letter))

        # We need to tell the user how much correct letters he have typed
        word_list = [letter if letter in used_Letter else '-' for letter in randomWord]
        print('Current Word = ', ' '.join(word_list))

        user_Letter = (input("Enter a letter: ")).upper()
        if user_Letter in (alphabets - used_Letter):        # checking If the user guess is letter or not which is not in used_letters
            used_Letter.add(user_Letter)        # if previous condition is satisfied we add the user letter to used letter
            if user_Letter in letters_word:
                letters_word.remove(user_Letter)    # if the user guess is part of the random number we remove the letter from the letter array
            
            else:
                lives -= 1
                print('Your letter', user_Letter, 'is not in the word.')
                print('You have ',lives, ' remaining. Keep on trying!')
        
        elif user_Letter in used_Letter:
            print("You have already used that letter. Please try again!")
        
        else:
            print("That is not a letter, Please try again!")
        
    if lives == 0:
        print('You died!')
    else:
        print('You guessed the word ', randomWord.lower(), 'with ', lives, ' remaining')


hangman()
