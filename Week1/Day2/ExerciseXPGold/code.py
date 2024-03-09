import random

# Exercise 1
list1 = [1, 2, 3]
list2 = [4, 5, 6]

concatenated_list = [*list1, *list2]

print("Concatenated list:", concatenated_list)

# Exercise 2
for num in range(1500, 2500 + 1):
    if num % 5 == 0 and num % 7 == 0:
        print(num)


# Exercise 3
names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']

user_name = input("Enter your name: ")

if user_name in names:
    print("Index of first occurrence of", user_name + ":", names.index(user_name))
else:
    print("Name not found in the list.")


# Exercise 4
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

greatest_number = max(number1, number2, number3)

print("The greatest number is:", greatest_number)


# Exercise 5
alphabet = 'abcdefghijklmnopqrstuvwxyz'

vowels = 'aeiou'

for letter in alphabet:
    if letter in vowels:
        print(f"{letter} is a vowel.")
    else:
        print(f"{letter} is a consonant.")


# Exercise 6
words = []
for i in range(7):
    word = input(f"Enter word {i+1}: ")
    words.append(word)

letter = input("Enter a single character: ")

for word in words:
    if letter in word:
        print(f"The index of '{letter}' in '{word}' is:", word.index(letter))
    else:
        print(f"The letter '{letter}' doesn't exist in the word '{word}'.")


# Exercise 7
numbers = list(range(1, 1000001))

print("Minimum number:", min(numbers))
print("Maximum number:", max(numbers))
print("Sum of the numbers:", sum(numbers))


# Exercise 8
input_numbers = input("Enter a sequence of comma-separated numbers: ")

numbers_list = input_numbers.split(',')

numbers_tuple = tuple(numbers_list)

print("List:", numbers_list)
print("Tuple:", numbers_tuple)


# Exercise 9
games_won = 0
games_lost = 0

while True:
    user_guess = int(input("Guess a number from 1 to 9 (or enter 0 to quit): "))

    if user_guess == 0:
        break

    random_number = random.randint(1, 9)

    if user_guess == random_number:
        print("Winner!")
        games_won += 1
    else:
        print("Better luck next time. The number was:", random_number)
        games_lost += 1

print("Total games won:", games_won)
print("Total games lost:", games_lost)