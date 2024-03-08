import random

list_of_numbers = [random.randint(0, 10000) for _ in range(20000)]
target_number = 3728
set_of_couples = set()
for number in list_of_numbers:
    for i in list_of_numbers:
       if number + list_of_numbers[i] == target_number:
           set_of_couples.add((number, list_of_numbers[i]))


print(len(set_of_couples))

