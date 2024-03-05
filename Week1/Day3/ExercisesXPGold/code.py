# Exercise 1
birthdays = {
    "Alice": "1990/05/15",
    "Bob": "1985/10/25",
    "Charlie": "1992/02/08",
    "David": "1988/09/17",
    "Eve": "1995/12/30"
}

print("Welcome! You can look up the birthdays of the people in the list!")
person_name = input("Enter a person's name to look up their birthday:\n")

if person_name in birthdays.keys():
    print(f"The birthday of {person_name} is {birthdays[person_name]}.")
else:
    print(f"Sorry, there's no birthday information available for {person_name}.")

# Exercise 2
birthdays = {
    "Alice": "1990/05/15",
    "Bob": "1985/10/25",
    "Charlie": "1992/02/08",
    "David": "1988/09/17",
    "Eve": "1995/12/30"
}

print("Welcome! You can look up the birthdays of the people in the following list:")

for name in birthdays.keys():
    print(name)

person_name = input("Enter a person's name to look up their birthday:\n")

if person_name in birthdays.keys():
    print(f"The birthday of {person_name} is {birthdays[person_name]}.")
else:
    print(f"Sorry, we don’t have the birthday information for {person_name}.")

# Exercise 3
birthdays = {
    "Alice": "1990/05/15",
    "Bob": "1985/10/25",
    "Charlie": "1992/02/08",
    "David": "1988/09/17",
    "Eve": "1995/12/30"
}

print("Welcome! You can look up the birthdays of the people in the following list:")

for name in birthdays.keys():
    print(name)

add_new_birthday = input("Would you like to add a new birthday? (yes/no):\n")

if add_new_birthday.lower() == "yes":
    new_name = input("Enter the person's name:\n")
    new_birthday = input("Enter the person's birthday (YYYY/MM/DD):\n")
    birthdays[new_name] = new_birthday

person_name = input("Enter a person's name to look up their birthday:\n")

if person_name in birthdays.keys():
    print(f"The birthday of {person_name} is {birthdays[person_name]}.")
else:
    print(f"Sorry, we don’t have the birthday information for {person_name}.")

# Exercise 4
items = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

for item, price in items.items():
    print(f"The price of {item} is ${price}.")

items = {
    "banana": {"price": 4 , "stock":10},
    "apple": {"price": 2, "stock":5},
    "orange": {"price": 1.5 , "stock":24},
    "pear": {"price": 3 , "stock":1}
}

new_items = {
    "banana": {"price": 4, "stock": 10},
    "apple": {"price": 2, "stock": 5},
    "orange": {"price": 1.5, "stock": 24},
    "pear": {"price": 3, "stock": 1}
}

total_cost = 0

for item, info in items.items():
    total_cost += info["price"] * info["stock"]

print("Total cost to buy everything in stock:", total_cost)
