import random
import sys



def histogram(word_list):
    dict_histogram = {}
    for word in word_list:
        # word = word.rstrip()
        # if word not in dict_histogram.keys():
        #     dict_histogram[word] = 1
        # else:
        #     dict_histogram[word] += 1
        dict_histogram[word] = dict_histogram.get(word, 0) + 1

    return dict_histogram


def unique_words(histogram):
    # keys = histogram.keys()
    return len(histogram.keys())
    

def frequency(histogram, word):
    return histogram.get(word, 0) 


if __name__ == "__main__":
    filename = open('./dracula.txt')
    lines = filename.read().split(' ')
    hist = histogram(lines)
    # print(hist)
    unique_words(hist)
    print(frequency(hist, "I"))