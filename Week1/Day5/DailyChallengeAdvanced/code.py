import random

list_of_numbers = [random.randint(0, 10000) for _ in range(20000)]

target_number = 3728

compliment_list = []
pair_count = 0

for num in list_of_numbers:
    compliment_list.append(target_number - num)


for num in compliment_list:
    if num in list_of_numbers:
        pair_count += 1

print("Number of pairs summing to target_number:", pair_count)
