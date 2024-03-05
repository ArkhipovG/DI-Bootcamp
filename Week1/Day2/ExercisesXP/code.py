#Exercise1
my_fav_numbers = {7,88,24,23,10}
my_fav_numbers.add(33)
my_fav_numbers.add(16)
print(my_fav_numbers)
my_fav_numbers.remove(10) #we can delete last number only if we know what is last number
print(my_fav_numbers)
friend_fav_numbers={21,9,3,15}
our_fav_numbers = friend_fav_numbers.union(my_fav_numbers)
print(our_fav_numbers)
print("---------")

#Exercise2
sample_tuple = (1,2,3,4,5,6,7,8,9) #it is not possible to add more integers to a tuple

#Exercise3
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
basket.remove("Blueberries")
basket.append("Kiwi")
basket.insert(0, "Apples")
print(basket.count("Apples"))
print(basket)
print("---------")

#Exercise4
float = 1.5
float_list = [float]
while float < 5:
    float = float + 0.5
    float_list.append(float)
print(float_list)
print("---------")
#Exercise5
for i in range(1,21):
    print(i)
print("---------")

for i in range(1,21):
    if i % 2 == 0:
        print(i)
print("---------")

#Exercise6
my_name = "Gregory"
user_name = ""

while user_name != my_name:
    user_name = (input("What is your name? "))
    user_name = user_name.capitalize()
print("We are namesakes!")

#Exercise7
user_fav_fruits = input("What kind of fruit do you like? \nPlease separate the fruits with a single space\n")
user_fav_fruits = user_fav_fruits.lower()
list_fruits = user_fav_fruits.split()

chosen_fruit = input("Choose any fruit: ")
chosen_fruit = chosen_fruit.lower()
if chosen_fruit in list_fruits:
    print("You chose one of your favorite fruits! Enjoy!”")
else:
    print("You chose a new fruit. I hope you enjoy")

#Exercise8
list_of_toppings = []
topping = ""
while topping != "quit":
    topping = (input("What topping do you want to add? "))
    if topping != "quit":
        list_of_toppings.append(topping)
        print("Okay, I will add " + topping + " to your pizza")

cost_of_pizza = 10 + (2.5*len(list_of_toppings))
print(f"Your pizza will be with {', '.join(list_of_toppings)} and will cost ${cost_of_pizza}")

#Exercise9
total_ticket_price = 0
age = int
while age != 0:
    age = int(input("Enter the age of each person \nEnter 0 if you finish\n"))
    if age != 0 and age > 0:
        if age < 3:
            total_ticket_price += 0
        elif age in range(3, 13):
            total_ticket_price += 10
        elif age > 12:
            total_ticket_price += 15

print(f"Your total price is ${total_ticket_price}")


names = ["Alice", "Bob", "Charlie", "David", "Emma", "Frank"]

allowed_names = []

for name in names:
    age = int(input(f"How old is {name}? "))
    if 16 <= age <= 21:
        allowed_names.append(name)

print("Teenagers allowed to watch the movie:")
for name in allowed_names:
    print(name)

#Exercise 10
sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]

while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")

finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    finished_sandwiches.append(current_sandwich)

for sandwich in finished_sandwiches:
    print(f"I made your {sandwich.lower()}")
