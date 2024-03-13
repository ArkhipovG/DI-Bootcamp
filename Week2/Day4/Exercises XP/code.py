import os
import random
dir_path = os.path.dirname(os.path.realpath(__file__))



def get_words_from_file():
    with open(os.path.join(dir_path + '/sowpods.txt')) as sowpods:
        list_of_words = sowpods.read().splitlines()
        return list_of_words


def get_random_sentence(length):
    list_of_words = get_words_from_file()
    return ' '.join(random.choice(list_of_words) for i in range(length)).lower()


def main():
    print("This program asks the user for sentence length an then printing the generated sentence.")
    length = int(input('How long the sentence should be? (Acceptable values are between 2 and 20)\n'))
    if 2 <= length <= 20:
        sentence = get_random_sentence(length)
    else:
        raise ValueError("It's not valid")
    print(sentence)

main()

# Exercise 2


