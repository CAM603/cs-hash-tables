import random
import os
import sys
import re

# Read in all the words in one go
with open(os.path.join(sys.path[0], "input.txt")) as f:
    # Read file
    words = f.read()
    # Split into list of words
    words = words.split()
    f.close()

# TODO: analyze which words can follow other words
# Your code here
my_dict = {}

for i in range(len(words) - 1):
    cur = words[i]
    next = words[i + 1]
    # If word is not yet in the dictionary
    if not cur in my_dict.keys():
        # start the list of can be followed by words
        my_dict[cur] = [next]
    # If it is in the dictionary
    else:
        # append to the list
        my_dict[cur].append(next)

# TODO: construct 5 random sentences
# Your code here

# choose a random word
random_word = random.choice(words)
# loop through words
punc = ['.', '?', '!']
pattern = re.compile('[!, ?, ., "]')


def markov(arr):
    for word in arr:
        print(word, end=" ")
        # If it is a stop word, stop
        if pattern.match(word[-1]):
            return
        else:
            print(random.choice(my_dict[word]), end=" ")


markov(words[10:])
markov(words[30:])
markov(words[50:])
markov(words[60:])
markov(words[80:])
