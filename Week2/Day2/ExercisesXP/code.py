import random


# Exercise 1
class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())


class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'


class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Siamese(Cat):
    def sing(self, sounds):
        return f'{sounds}'


bengal = Bengal('Bengal', 7)
siamese = Siamese('Siamese', 5)
chartreux = Chartreux('Chartreux', 10)
cats_list = [bengal, siamese, chartreux]

sara_pets = Pets(cats_list)

sara_pets.walk()
print("------")

# Exercise 2
class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f'{self.name} is barking'

    def run_speed(self):
        return f"The speed of {self.name} is {round((self.weight / self.age * 10), 2)}"

    def fight(self, other_dog):
        if self.run_speed() > other_dog.run_speed():
            return f'{self.name} won the fight'
        else:
            return f'{other_dog.name} won the fight'


dog1 = Dog('Bolt', 5, 10)
dog2 = Dog('Lulu', 12, 8)
dog3 = Dog('Beethoven', 10, 15)

print(dog1.bark())
print(dog2.run_speed())
print("------")
print(dog3.fight(dog1))
print("------")
print(dog2.fight(dog3))
print("------")
print(dog1.fight(dog2))
print("------")

# Exercise 3
class PetDog(Dog):
    def __init__(self, name, age, weight, trained=False):
        super().__init__(name, age, weight)
        self.trained = trained

    def train(self):
        print(self.bark())
        self.trained = True

    def play(self, *dog):
        dogs_names = ", ".join(map(str, dog))
        print(f"{self.name}, {dogs_names} all plays together")

    def do_a_trick(self):
        num = random.randint(1, 4)
        if self.trained:
            if num == 1:
                print(f"{self.name} is does a barrel roll")
            elif num == 2:
                print(f"{self.name} stands on his back legs")
            elif num == 3:
                print(f"{self.name} shakes your hand")
            elif num == 4:
                print(f"{self.name} plays dead")


dog1 = PetDog('Bolt', 5, 10)
dog2 = PetDog('Lulu', 12, 8)
dog3 = PetDog('Beethoven', 10, 15)

dog1.play(dog2.name, dog3.name)
print("------")
dog1.train()
print("------")
dog1.do_a_trick()
print("------")


# Exercise 4
class Family:
    def __init__(self, members, last_name):
        self.members = members
        self.last_name = last_name

    def born(self, **kwargs):
        self.members.append(dict(kwargs, age=0, is_child=True))
        print("Congratulations on the birth of your baby!")

    def is_18(self, name):
        for member in self.members:
            if member['name'] == name and member['age'] > 18:
                return True
            elif member['name'] == name and member['age'] < 18:
                return False

    def family_presentation(self):
        print(f"The family's last name is {self.last_name}")
        for member in self.members:
            for key, value in sorted(member.items(), reverse=True):
                print("{}: {}".format(key, value))
            print("---")


my_family = Family(
    [
        {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False},
        {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False}
    ],
    "Arkhipov")

my_family.born(name="Frank", gender="Male")
print("------")
my_family.is_18("Sarah")
my_family.is_18("Frank")
my_family.family_presentation()
print("------")

# Exercise 5
class TheIncredibles(Family):

    def use_power(self, name):
        try:
            for member in incredible_family.members:
                if member['name'] == name and self.is_18(name):
                    print(f"The power of {name} is {member['power']}")
                elif member['name'] == name and not self.is_18(name):
                    raise Exception(f"{member['name']} is under 18")
        except Exception as e:
            print(e)

    def incredible_presentation(self):
        print(f"Here is our powerful family")
        self.family_presentation()


incredible_family = TheIncredibles(
    [
        {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False, 'power': 'fly',
         'incredible_name': 'MikeFly'},
        {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False, 'power': 'read minds',
         'incredible_name': 'SuperWoman'}
    ],
    "Arkhipov"
)
incredible_family.born(name="Baby Jack", gender="Male", power="Unknown Power")
incredible_family.use_power("Sarah")
incredible_family.use_power("Jack")
print("------")
incredible_family.incredible_presentation()
