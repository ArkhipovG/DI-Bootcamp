import random


def get_age(year, month, day):
    current_year = 2024
    current_month = 3

    age = current_year - year
    if current_month < month or (current_month == month and day > 0):
        age -= 1

    return age


def can_retire(gender, date_of_birth):
    year, month, day = map(int, date_of_birth.split('/'))

    age = get_age(year, month, day)

    if gender == 'm':
        return age >= 67
    elif gender == 'f':
        return age >= 62
    else:
        return False


print(can_retire('m', '1970/05/15'))
print(can_retire('f', '1960/08/20'))


# Exercise 2

def weird_sum(x):
    x_str = str(x)
    x_list = [x_str, x_str * 2, x_str * 3, x_str * 4]
    int_list = [int(x) for x in x_list]
    return sum(int_list)


print(weird_sum(3))


# Exercise 3
def throw_dice():
    return random.randint(1, 6)


def throw_until_doubles():
    throws = 0
    while True:
        throws += 1
        dice1 = throw_dice()
        dice2 = throw_dice()
        if dice1 == dice2:
            return throws


def main():
    throws_collection = []

    for _ in range(100):
        throws = throw_until_doubles()
        throws_collection.append(throws)

    total_throws = sum(throws_collection)
    average_throws = round(total_throws / 100, 2)

    print("Total throws:", total_throws)
    print("Average throws to reach doubles:", average_throws)


main()
