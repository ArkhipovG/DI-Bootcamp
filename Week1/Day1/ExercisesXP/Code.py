#Exercise1
print("Hello World!\n" * 4)

#Exercise2
result = (99**3)*8
print(result)

#Exercise3
print(5 < 3) #False
print(3 == 3) #True
print(3 == "3") #False
# print("3" > 3) #TypeError
print("Hello" == "hello") #False

#Exercise4
computer_brand = "Apple"
print(f"I have an {computer_brand} computer")

#Exercise5
name = "Gregory"
age = 27
shoe_size = 42
info  = f"My name is {name} and I am {age} years old. My shoe size is {shoe_size}"
print(info)

#Exercise6
a = 12
b = 2
if a > b:
    print("Hello world!")

#Exercise7
selected_number = int(input("Enter a number: "))
if selected_number % 2 == 0:
    print("Even")
else:
    print("Odd")

#Exercise8
my_name = "Gregory"
your_name = str(input("Enter your name: "))
if your_name == my_name:
    print("We are namesakes!")
else:
    print("We are not namesakes!")

#Exercise9
min_hight = 145
your_hight = int(input("Enter your hight in cm: "))
if your_hight >= min_hight:
    print("You are tall enough to ride")
else:
    print("You need to grow some more to ride")

