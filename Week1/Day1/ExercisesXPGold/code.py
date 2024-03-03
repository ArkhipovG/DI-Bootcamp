#Task1
print("Hello World!\n"*4 + "I love python\n"*4)

#Task2
input_month =int(input("Enter a month: "))
if input_month <1 or input_month >12:
    print("Invalid")
elif input_month in [3,4,5]:
    print("Spring")
elif input_month in [6,7,8]:
    print("Summer")
elif input_month in [9,10,11]:
    print("Autumn")
elif input_month in [12,1,2]:
    print("Winter")



