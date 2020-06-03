import os
import sys
from operator import itemgetter
# Your code here

ignore = ['"', ':', ';', ',', '.', '-', '+', '=', '/',
          '\\', '|', '[', ']', '{', '}', '(', ')', '*', '^', '&']


def histo(filename):
    my_dict = {}
    # Open file and read
    with open(os.path.join(sys.path[0], filename)) as f:
        # Read file
        words = f.read()
        f.close()
    words = words.split()
    # Loop through words
    for word in words:
        if not word:
            continue
        # Remove ignored characters
        word = "".join(i.lower() for i in word if not i in ignore)
        if not word in my_dict.keys():
            my_dict[word] = 1
        else:
            my_dict[word] += 1

    items = list(my_dict.items())
    items.sort(key=lambda e: (-e[1], e[0]))
    print(items)

    for tup in items:
        print(f'{tup[0]:20} {"#" * tup[1]}')


histo('robin.txt')
