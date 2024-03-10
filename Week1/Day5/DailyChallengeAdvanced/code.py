import random

list_of_numbers = [random.randint(0, 10000) for _ in range(20000)]

target_number = 3728

compliment_list = []
unique_couples_dict = {}
list_couples = []

for num in list_of_numbers:
    compliment_list.append(target_number - num)

for num in compliment_list:
    if num in list_of_numbers:
        unique_couples_dict[num] = target_number - num
        list_couples.append([num, target_number - num])

print("Number of pairs summing to target_number:", len(list_couples))
print("Number of unique pairs:", len(unique_couples_dict))
print("Number of same couples: ", len(list_couples) - len(unique_couples_dict))
