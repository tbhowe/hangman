# import relevant modules
import random

# define the Hangman Class:
class Hangman:
    
    def __init__(self,word_list,num_lives):
        self.word_list=word_list
        self.num_lives=5
        self.word = random.choice(word_list)
        self.word_guessed= [''] * len(self.word)
        self.num_letters=len(list(set(self.word)))
        self.list_of_guesses=[]


# # Create word list
# word_list = ["lingon", "raspberry", "cherry","rambutan","guava"]

# # Create instance of Hangman Class, passing word list to it.
# test_instance=Hangman(word_list,5)