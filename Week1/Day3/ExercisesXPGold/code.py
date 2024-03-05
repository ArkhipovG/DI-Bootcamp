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
