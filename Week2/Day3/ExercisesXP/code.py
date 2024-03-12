import random
import string
import datetime


# Exercise 1
class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self):
        if self.amount > 1:
            return f'{self.amount} {self.currency}s'
        else:
            return f'{self.amount} {self.currency}'

    def __int__(self):
        return int(self.amount)

    def __repr__(self):
        if self.amount > 1:
            return f'{self.amount} {self.currency}s'
        else:
            return f'{self.amount} {self.currency}'

    def __add__(self, other):
        if isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
            return self.amount + other.amount
        else:
            return self.amount + other

    def __iadd__(self, other):
        if isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
            self.amount += other.amount
        else:
            self.amount += other
        return self


c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

print(str(c1))
print(str(c3))
print(int(c4))
print(repr(c4))
print(c1 + c2)
print(c1 + 12)
c1 += c2
c3 += 66
print(c1)
print(c3)


# print(c1 + c3)
# TypeError: Cannot add between Currency type <dollar> and <shekel>


# Exercise 3
def generate_random_string(length=5):
    letters = string.ascii_letters
    random_string = ''.join(random.choice(letters) for _ in range(length))
    return random_string


random_string = generate_random_string()
print(random_string)

# Exercise 4

today = datetime.datetime.today()
print(today)


# Exercise 5
def days_until_january_first():
    today = datetime.datetime.today()
    first_jan = datetime.datetime.strptime('01/01/2025', "%d/%m/%Y")
    until_january_first = first_jan - today
    print(f"The 1st of January is in  {until_january_first}")


days_until_january_first()


# Exercise 6
def days_and_minutes():
    birthdate_str = input("Enter your birthdate (DD/MM/YYYY): ")
    birthdate = datetime.datetime.strptime(birthdate_str, "%d/%m/%Y")

    total_days = today - birthdate
    total_minutes = total_days.total_seconds() / 60
    print(f" You lived {total_days.days} days")
    print(f" You lived {round(total_minutes, 2)} minutes")


days_and_minutes()

from faker import Faker

fake = Faker()

users = []

# Function to add user to the list
def add_user():
    user = {
        'name': fake.name(),
        'address': fake.address(),
        'language_code': random.choice(['en', 'fr', 'es'])  # Example of random language code selection
    }
    users.append(user)

# Test the function by adding 10 users
for _ in range(10):
    add_user()

# Print the list of users
for user in users:
    print(user)