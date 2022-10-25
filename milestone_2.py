# import relevant modules
import random

# Create word list
word_list = ["lingon", "raspberry", "cherry","rambutan","guava"]
print(word_list)

# Choose a random word from the list of possible words
word = random.choice(word_list)
print(word)

# Request input from user of a single letter
guess=input("please enter a single letter")

# while loop to ensure only a single element is input for the guess
while len(guess) != 1:
    print("hey! I said a single letter!")
    guess=input("please enter a single letter")

print('thanks!')

# Checkl that the guess is an alphabetical
if guess.isalpha==1:
    print("good guess!")
else:
    print("Oops! That is not a valid input.")

