from random import randint

filename = "/Users/studentlaptop_719_1/Dev/CS1.2/CS-12-Intro-to-Data-Structures/words.txt"

my_file = open(filename, "r")

lines = my_file.readlines()

my_file.close()

print(lines)

random_index = randint(0, len(lines)-1)
print(lines[random_index])