import os

dir_path = os.path.dirname(os.path.realpath(__file__))


with open(os.path.join(dir_path + '/sowpods.txt')) as sowpods:
    lists_of_words = sowpods.read().lower().splitlines()


class Text:
    def __init__(self, string):
        self.string = string
        self.list_of_words = string.split()

    def frequency(self, input_word):
        count = 0
        for word in self.list_of_words:
            if word == input_word:
                count += 1

        if count == 0:
            return None
        else:
            return count

    def most_common_word(self):
        word_dict = {}
        for word in self.list_of_words:
            if word not in word_dict and word in lists_of_words:
                word_dict[word] = 1
            elif word in lists_of_words:
                word_dict[word] += 1

        most_common_word = max(word_dict, key=word_dict.get)
        return f"Most common word is: {most_common_word}"

    def unique_words(self):
        unique_words = []
        for word in self.list_of_words:
            if word not in unique_words:
                unique_words.append(word)
        return unique_words

    @classmethod
    def from_file(cls, path):
        with open(dir_path + f"/{path}") as file_obj:
            text = file_obj.read()
            return cls(text)


text1 = Text("A good book would sometimes cost as much as a good house.")
print(text1.frequency("good"))
print(text1.most_common_word())
print(text1.unique_words())
print("---------")
text2 = Text.from_file('the_stranger.txt')

print(text2.frequency("good"))
print(text2.most_common_word())
print(text2.unique_words())
