# # Exercise 1
input_sequence = input("Enter a comma-separated sequence of words: ")

words = [word.strip() for word in input_sequence.split(',')]

sorted_words = sorted(words)

output_sequence = ','.join(sorted_words)

print(output_sequence)

# Exercise 2
input_sentence = input("Enter sentence: ")

wordslist = [word.strip() for word in input_sentence.split(' ')]

longest_word = ''

for word in wordslist:
    if len(word) > len(longest_word):
        longest_word = word

print(longest_word)
