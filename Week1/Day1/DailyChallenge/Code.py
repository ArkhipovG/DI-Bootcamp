#Task1
user_input = input("Please enter a string of exactly 10 characters: ")

if len(user_input) < 10:
    print("String not long enough")
elif len(user_input) > 10:
    print("String too long")
else:
    print("Perfect string")

#Task2
first_character = user_input[0]
last_character = user_input[-1]
print(f"First character is:  {first_character}")
print(f"Last character is: {last_character}")

#Task3
print("Constructing the string character by character:")
for i in range(1, len(user_input) + 1):
        print(user_input[:i])

#Task4
import random
shuffled_list = list(user_input)
random.shuffle(shuffled_list)
shuffled_string = ''.join(shuffled_list)

print("Newly jumbled string:", shuffled_string)

