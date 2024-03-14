import os
from itertools import permutations

dir_path = os.path.dirname(os.path.realpath(__file__))


class AnagramChecker:
    def __init__(self):
        with open(os.path.join(dir_path + '/sowpods.txt')) as english_words:
            self.words_lists = english_words.read().lower().splitlines()

    def is_valid_word(self, word):
        word = word.strip()
        if len(word.split()) > 1:
            print("Error: Only a single word is allowed.")
        elif not word.isalpha():
            print("Error: The word must contain only alphabetic characters.")
            return False
        elif word not in self.words_lists:
            return False
        else:
            return True

    def get_anagram(self, word):
        anagram_list = []
        if self.is_valid_word(word):
            list_of_letters = list(word.lower())
            all_permutations = list(permutations(list_of_letters))
            for permutation in all_permutations:
                permutation_word = ''.join(permutation)
                if permutation_word in self.words_lists and permutation_word != word:
                    anagram_list.append(permutation_word)
            print(f'YOUR WORD: "{word.upper()}"')
            print("This is a valid English word.")
            if len(anagram_list) >= 1:
                print(f"Anagrams for your word: {",".join(map(str, anagram_list))}.")
            else:
                print(f"But there is no anagrams for your word")
