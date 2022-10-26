# import relevant modules
import random

# define the Hangman Class:
class Hangman:
    
    def __init__(self,word_list,num_lives):
        self.word_list=word_list
        self.num_lives=5
        self.word = random.choice(word_list)
        self.word_guessed= ['_'] * len(self.word)
        self.num_letters=len(list(set(self.word)))
        self.list_of_guesses=[]
    
    def check_guess(self,guess):
    # This function checks if the guessed letter is in the word
        guess= guess.lower()
        if guess in self.word:
            print("Good guess! " + guess + " is in the word.")
            return()
        else:
            print("Sorry, " + guess + " is not in the word. Try again.")
        return()

    def ask_for_input(self):
        #This function requests an input, returns the input if correctly formatted, 
        # else asks for a new guess.
        while True:
        # Request input from user of a single letter
            guess=input("please enter a single letter")
        #checks that input is alphabetical AND of length 1. Escapes if both conditions met
            if len(guess)!=1 or guess.isalpha() != 1:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses+=guess
                

# Create word list
word_list = ["lingon", "raspberry", "cherry","rambutan","guava"]

# Create instance of Hangman Class, passing word list to it.
test_instance=Hangman(word_list,5)

test_instance.ask_for_input()
