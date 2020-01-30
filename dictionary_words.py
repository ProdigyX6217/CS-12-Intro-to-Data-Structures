from random import random, randint, choice, sample
import sys

filename = "/Users/studentlaptop_719_1/Dev/CS1.2/CS-12-Intro-to-Data-Structures/words.txt"
my_file = open(filename, "r")
lines = my_file.readlines()

for random_index in lines:
    random_index = randint(0, len(lines)-1)
    rand_item = lines[random_index]
    print(rand_item)

    my_file.close()