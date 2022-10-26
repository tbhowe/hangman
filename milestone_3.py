# import relevant modules
import random

# define functions for use in the Hangman script

def check_guess(guess):
    # This function checks if the guessed letter is in the word
    guess= guess.lower()
    if guess in word:
        print("Good guess! " + guess + " is in the word.")
        return()
    else:
        print("Sorry, " + guess + " is not in the word. Try again.")
        return()

def ask_for_input():
    #This function requests an input, returns the input if correctly formatted, 
    # else asks for a new guess.
    while True:
        # Request input from user of a single letter
        guess=input("please enter a single letter")
        #checks that input is alphabetical AND of length 1. Escapes if both conditions met
        if len(guess)==1 and guess.isalpha() == 1:
            print('thanks!')
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
    #Checks whether guess is in the word
    check_guess(guess)
    #returns guess
    return(guess)




# Start of main Hangman script	

# Create word list
word_list = ["lingon", "raspberry", "cherry","rambutan","guava"]

# Choose a random word from the list of possible words
word = random.choice(word_list)

ask_for_input()


