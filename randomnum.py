import random
print('Random Number 1=>',random.random())

print('Random Number 2=>',random.random())
# To generate random numbers
# random.random() generates a random float number between 0.0 and 1.0.

import random
print('Random Number 3=>',random.randint(3, 9))

print('Random Number 4=>',random.randint(3, 9))
# To generate random numbers between 1 and 10
# random.randint() generates a random integer number between the given range.

import random
print('Random Number 5=>',random.choice(['apple', 'banana', 'cherry']))

print('Random Number 6=>',random.choice(['apple', 'banana', 'cherry']))
# To choose a random item from a list
# random.choice() is a function that returns a random item from a list.

import random
print(random.randrange(3, 9))
# To generate a random number between 3 and 9, excluding 9.
# random.randrange() generates a random integer number between the given range.

# shuffle() shuffles the elements
import random
list = [10,6,4,11,1]
random.shuffle(list)
print('Shuffled List=>', list)
# random.shuffle() shuffles the elements of a list in place