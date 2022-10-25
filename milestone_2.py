# import relevant modules
import random

word_list = ["lingon", "raspberry", "cherry","rambutan","guava"]
print(word_list)

word = random.choice(word_list)

print(word)


guess=input('please enter a single letter')

while len(guess) != 1:
    print('hey! I said a single letter!')
    guess=input('please enter a single letter')

print('thanks!')

