import os
import random

#Exercise 1
dir_path = os.path.dirname(os.path.realpath(__file__))



def get_words_from_file():
    with open(os.path.join(dir_path + '/sowpods.txt')) as sowpods:
        list_of_words = sowpods.read().splitlines()
        return list_of_words


def get_random_sentence(length):
    return ' '.join(random.choice(get_words_from_file()) for i in range(length)).lower()


def main():
    print("This program asks the user for sentence length an then printing the generated sentence.")
    input_str = input('How long the sentence should be? (Acceptable values are between 2 and 20)\n')
    if input_str.isdigit():
        length = int(input_str)
        if 2 <= length <= 20:
            sentence = get_random_sentence(length)
            print(sentence)
        else:
            print(ValueError("It's not valid"))


    else:
        print(ValueError("It's not valid"))


main()



