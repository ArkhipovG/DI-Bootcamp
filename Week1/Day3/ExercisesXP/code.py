# Exercise 1
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

first_dict = dict(zip(keys, values))
print(first_dict)

# Exercise 2
age = int
name = str
family = {}
total_cost = 0
while name != "quit" :
    name = input("Enter the name (Enter 'quit' if you finished): \n")
    if name != "quit":
        age = int(input(f"Enter the age of {name}: \n"))
        family[name] = age

for key, value in family.items():
    if age != 0 and age > 0:
        if age < 3:
            total_cost += 0
        elif age in range(3, 13):
            total_cost += 10
        elif age > 12:
            total_cost += 15

print(family)
print(f"Your total price is ${total_cost}")

# Exercise 3
brand = {
    'name': 'Zara',
    'creation_date': 1975,
    'creator_name': "Amancio Ortega Gaona",
    'type_of_clothes': ['men', 'women', 'children', 'home'],
    'international_competitors': ['Gap', 'H&M', 'Benetton'],
    'number_stores': 7000,
    'major_color': {
        'France': 'blue',
        'Spain': 'red',
        'US': ['pink', 'green']
    }
}

print(brand['number_stores'])
print('------------')

brand['number_stores'] = 2
print(brand['number_stores'])
print('------------')

for value in brand['type_of_clothes']:
    if value != 'home':
        print(value)
print('------------')

brand['country_creation'] = 'Spain'
print(brand['country_creation'])
print('------------')

if 'international_competitors' in brand.keys():
    brand['international_competitors'].append('Desigual')

print(brand['international_competitors'])
print('------------')

del brand['creation_date']

print(brand['international_competitors'][-1])
print('------------')

print(brand['major_color']['US'])
print('------------')

print(len(brand))
print('------------')

print(brand.keys())
print('------------')

more_of_zara = {
    'creation_date': 1975,
    'number_stores': 10000
}

brand.update(more_of_zara)
print(brand)
print('------------')

print(brand['number_stores']) # it will print 10000
print('------------')

# Exercise 4
users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
disney_users_A = {}
disney_users_B = {}
disney_users_C = {}

for user in users:
    disney_users_A[user] = users.index(user)

print(disney_users_A)
print('------------')

for user in users:
    disney_users_B[users.index(user)] = user

print(disney_users_B)
print('------------')

users.sort()
for user in users:
    disney_users_C[user] = users.index(user)

print(disney_users_C)
print('------------')

disney_users_A_recreated = {}

for key in disney_users_A:
    if 'i' in key and (key.startswith('M') or key.startswith('P')):
        disney_users_A_recreated[key] = disney_users_A[key]

print(disney_users_A_recreated)
