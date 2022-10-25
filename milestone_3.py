# import relevant modules
import random

# Create word list
word_list = ["lingon", "raspberry", "cherry","rambutan","guava"]


# Choose a random word from the list of possible words
word = random.choice(word_list)


while True:
    # Request input from user of a single letter
    guess=input("please enter a single letter")

    #checks that input is alphabetical AND of length 1. Escapes if both conditions met
    if len(guess)==1 and guess.isalpha() == 1:
        print('thanks!')
        break
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")

# Check whether guess is in word

if guess in word:
    print("Good guess! " + guess + " is in the word.")
else:
    print("Sorry, " + guess + " is not in the word. Try again.")



