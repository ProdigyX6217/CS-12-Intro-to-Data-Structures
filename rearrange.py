import random

def rearrange(input):
    print("Enter A String")
    string = input()
    
    string_list = string.split(" ")

    # string_list = string_list[-1::-1]

    # arranged = ' '.join(string_list)

    random.shuffle(string_list)

    print(string_list)

rearrange(input)