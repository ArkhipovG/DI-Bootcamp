import math
import random
# Exercise 1
C = 50
H = 30

input_string = input("Enter comma-separated numbers: ")

numbers = input_string.split(',')

results = [str(int(math.sqrt((2 * C * int(D)) / H))) for D in numbers]

output_string = ','.join(results)

print(output_string)


# Exercise 2
# 1. Store the list of numbers in a variable.
numbers = [3, 47, 99, -80, 22, 97, 54, -23, 5, 7]

# 2. Print the following information:
# a. The list of numbers – printed in a single line
print("a. List of numbers:", numbers)

# b. The list of numbers – sorted in descending order (largest to smallest)
sorted_numbers_desc = sorted(numbers, reverse=True)
print("b. Sorted list (descending order):", sorted_numbers_desc)

# c. The sum of all the numbers
sum_of_numbers = sum(numbers)
print("c. Sum of all numbers:", sum_of_numbers)

# 3. A list containing the first and the last numbers.
first_and_last_numbers = [numbers[0], numbers[-1]]
print("3. List containing the first and last numbers:", first_and_last_numbers)

# 4. A list of all the numbers greater than 50.
greater_than_50 = [num for num in numbers if num > 50]
print("4. Numbers greater than 50:", greater_than_50)

# 5. A list of all the numbers smaller than 10.
smaller_than_10 = [num for num in numbers if num < 10]
print("5. Numbers smaller than 10:", smaller_than_10)

# 6. A list of all the numbers squared
numbers_squared = [num ** 2 for num in numbers]
print("6. Numbers squared:", numbers_squared)

# 7. The numbers without any duplicates – also print how many numbers are in the new list.
unique_numbers = list(set(numbers))
print("7. Numbers without duplicates:", unique_numbers, "(Count:", len(unique_numbers), ")")

# 8. The average of all the numbers.
average_of_numbers = sum_of_numbers / len(numbers)
print("8. Average of all numbers:", average_of_numbers)

# 9. The largest number.
largest_number = max(numbers)
print("9. Largest number:", largest_number)

# 10. The smallest number.
smallest_number = min(numbers)
print("10. Smallest number:", smallest_number)

# 11. Bonus: Find the sum, average, largest, and smallest number without using built-in functions.
sum_bonus = 0
largest_bonus = numbers[0]
smallest_bonus = numbers[0]
for num in numbers:
    sum_bonus += num
    if num > largest_bonus:
        largest_bonus = num
    if num < smallest_bonus:
        smallest_bonus = num
average_bonus = sum_bonus / len(numbers)
print("11. Bonus - Sum:", sum_bonus, "Average:", average_bonus, "Largest:", largest_bonus, "Smallest:", smallest_bonus)

# 12. Bonus: Instead of using pre-defined lists of numbers, ask the user for 10 numbers between -100 and 100.
user_numbers = []
for _ in range(10):
    num = int(input("Enter a number between -100 and 100: "))
    user_numbers.append(num)

# 13. Bonus: Instead of asking the user for 10 integers, generate 10 random integers yourself.
random_numbers = [random.randint(-100, 100) for _ in range(10)]

# 14. Bonus: Instead of always generating 10 integers, let the amount of integers also be random!
random_amount = random.randint(50, 100)
random_numbers_variable_amount = [random.randint(-100, 100) for _ in range(random_amount)]

# 15. Bonus: Will the code work when the number of random numbers is not equal to 10?
# Yes, the code will work when the number of random numbers is not equal to 10.


# Exercise 3
paragraph = """
As advancing technology has rapidly expanded the types and amount of information we can collect,
knowing how to gather, sort, and analyze data has become a crucial part of almost any industry.
You’ll find data analysts in the criminal justice, fashion, food, technology, business, environment,
and public sectors—among many others.
"""

print(paragraph)

# 1. Number of characters
num_characters = len(paragraph)

# 2. Number of sentences
num_sentences = paragraph.count('.') + paragraph.count('!') + paragraph.count('?')

# 3. Number of words
words = paragraph.split()
num_words = len(words)

# 4. Number of unique words
unique_words = set(words)
num_unique_words = len(unique_words)

# Bonus 1: Number of non-whitespace characters
num_non_whitespace = sum(1 for char in paragraph if not char.isspace())

# Bonus 2: Average amount of words per sentence
average_words_per_sentence = num_words / num_sentences

# Bonus 3: Amount of non-unique words
non_unique_words = num_words - num_unique_words

print("Number of characters:", num_characters)
print("Number of sentences:", num_sentences)
print("Number of words:", num_words)
print("Number of unique words:", num_unique_words)
print("Number of non-whitespace characters:", num_non_whitespace)
print("Average amount of words per sentence:", average_words_per_sentence)
print("Amount of non-unique words:", non_unique_words)


# Exercise 4
input_string = input("Enter a sentence: ")

words = input_string.split()

word_freq = {}

for word in words:
    word_freq[word] = word_freq.get(word, 0) + 1

for word, freq in word_freq.items():
    print(f"{word}:{freq}")
