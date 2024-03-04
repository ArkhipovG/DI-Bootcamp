#Challenge1
number = int(input("Enter a number: "))
length = int(input("Enter the length: "))

multiples = []
for i in range(1, length + 1):
    multiples.append(number * i)

print(f"The list of multiples of {number} with length {length} is:")
print(multiples)

#Challenge2
user_word = input("Enter a word: ")

new_word = ""

for i in range(len(user_word)):
    if i == len(user_word) - 1 or user_word[i] != user_word[i + 1]:
        new_word += user_word[i]

print("The new word with consecutive duplicate letters removed is:", new_word)

