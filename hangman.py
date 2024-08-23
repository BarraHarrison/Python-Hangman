import random
import string # import string for alphabet set
from words import words

def get_valid_word(words):
    word = random.choice(words) # randomly chooses word from the list
    while "-" in word or " " in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 10 

    # Getting the user input
    while len(word_letters) > 0 and lives > 0:
        # Letters used
        print("You have", lives, "lives left and you have used these letters: ", " ".join(used_letters))

        # What the current word is
        word_list = [letter if letter in used_letters else "-" for letter in word]
        print("Current word: ", " ".join(word_list))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives = lives - 1 # Takes away a life if you are wrong
                print("Uh-Oh! This letter is not in the word.")

        elif user_letter in used_letters:
            print("You have already used that character. Please try again.")

        else:
            print("Invalid character. Please try again.")

    # When len(word_letters) == 0 or when lives == 0
    if lives == 0:
        print("You lost! The word was", word)
    else:
        print(f"Congratulations! You've guessed the word {word} correctly.")
    



hangman()
