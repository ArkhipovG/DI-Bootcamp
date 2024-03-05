import datetime

birthdate_str = input("Enter your birthdate (DD/MM/YYYY): ")

birthdate = datetime.datetime.strptime(birthdate_str, "%d/%m/%Y")

today = datetime.datetime.today()
age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

is_leap_year = (birthdate.year % 4 == 0 and birthdate.year % 100 != 0) or (birthdate.year % 400 == 0)

if age > 0:
    last_digit = int(str(age)[-1])
    nubmer_of_spaces_start = (11 - last_digit) // 2
    nubmer_of_spaces_end = 11 - last_digit - nubmer_of_spaces_start
    print("    " + "_" * nubmer_of_spaces_start + "i" * last_digit + "_" * nubmer_of_spaces_end)
print("   |:H:a:p:p:y:|")
print(" __|___________|__")
print("|^^^^^^^^^^^^^^^^^|")
print("|:B:i:r:t:h:d:a:y:|")
print("|                 |")
print("~~~~~~~~~~~~~~~~~~~")


if is_leap_year:
    if age > 0:
        last_digit = int(str(age)[-1])
        nubmer_of_spaces_start = (11 - last_digit) // 2
        nubmer_of_spaces_end = 11 - last_digit - nubmer_of_spaces_start
        print("    " + "_" * nubmer_of_spaces_start + "i" * last_digit + "_" * nubmer_of_spaces_end)
    print("   |:H:a:p:p:y:|")
    print(" __|___________|__")
    print("|^^^^^^^^^^^^^^^^^|")
    print("|:B:i:r:t:h:d:a:y:|")
    print("|                 |")
    print("~~~~~~~~~~~~~~~~~~~")

