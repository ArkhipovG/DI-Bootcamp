list1 = [5, 10, 15, 20, 25, 50, 20]

for i, item in enumerate(list1):
    if item == 20:
        list1[i] = 200
        break

print(list1)

a = 10
b = 20

# c = b
# b = a
# a = c
# a, b = b, a
b, a = a, b

print(a, b)

current_number = 0
while current_number < 10:
    current_number += 1
    print(current_number)
