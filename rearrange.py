import random

def rearrange(input):
    print("Enter A String")
    string = input()
    
    string_list = string.split(" ")

    # string_list.reverse()
    random.shuffle(string_list)

    print(string_list)

rearrange(input)


# words = ["dog", "log", "hog", "jog", "hog", "cog"]

#     def random_words():

#       for rand_index in words:
#          rand_index = random.randint(0, len(words) - 1)
#          print(words[rand_index])
#      return True

#     random_words()

#   if __name__ == '__main__':
      