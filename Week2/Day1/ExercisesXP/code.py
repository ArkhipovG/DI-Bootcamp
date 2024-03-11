# Exercise 1
class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age


first_cat = Cat("Jordan", 10)
second_cat = Cat("Lebron", 5)
third_cat = Cat("Kobe", 7)

cats = [first_cat, second_cat, third_cat]


def find_oldest(lst):
    oldest = lst[0]
    for cat in lst:
        if cat.age > oldest.age:
            oldest = cat

    print(f"The oldest cat is {oldest.name}, and is {oldest.age} years old.")


find_oldest(cats)
print("--------")


# Exercise 2
class Dog:
    def __init__(self, dog_name, dog_height):
        self.name = dog_name
        self.dog_height = dog_height

    def bark(self):
        print(f"{self.name} goes woof!")

    def jump(self):
        print(f"{self.name} jumps {self.dog_height * 2} cm high!")


davids_dog = Dog("Rex", 50)
print(f"Davids dog name: {davids_dog.name}")
print(f"Davids dog height: {davids_dog.dog_height}")
davids_dog.bark()
davids_dog.jump()

sarahs_dog = Dog("Teacup", 20)
print(f"Sarahs dog name: {sarahs_dog.name}")
print(f"Sarahs dog height: {sarahs_dog.dog_height}")
sarahs_dog.bark()
sarahs_dog.jump()


def bigger_dog(dog1, dog2):
    if dog1.dog_height > dog2.dog_height:
        print(f"{dog1.name} is bigger than {dog2.name}")
    else:
        print(f"{dog2.name} is bigger than {dog1.name}")


bigger_dog(sarahs_dog, davids_dog)
print("--------")


# Exercise 3
class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)


stairway = Song(["There’s a lady who's sure", "all that glitters is gold", "and she’s buying a stairway to heaven"])
stairway.sing_me_a_song()
print("--------")


# Exercise 4
class Zoo:
    def __init__(self, zoo_name):
        self.zoo_animals = []
        self.zoo_name = zoo_name

    def add_animal(self, *new_animal):
        if new_animal not in self.zoo_animals:
            self.zoo_animals.extend(new_animal)

    def get_animals(self):
        animals_string = ', '.join(self.zoo_animals)
        print(f"Animals in zoo: {animals_string}")

    def sell_animal(self, animal_sold):
        if animal_sold in self.zoo_animals:
            self.zoo_animals.remove(animal_sold)

    def sort_animals(self):
        self.zoo_animals.sort()
        grouped_animals = {}

        for animal in self.zoo_animals:
            first_letter = animal[0].lower()

            if first_letter not in grouped_animals:
                grouped_animals[first_letter] = animal
            elif first_letter in grouped_animals and type(grouped_animals[first_letter]) == str:
                grouped_animals[first_letter] = [grouped_animals[first_letter]]
                grouped_animals[first_letter].append(animal)
            elif first_letter in grouped_animals and type(grouped_animals[first_letter]) == list:
                grouped_animals[first_letter].append(animal)

        new_dict = {index + 1: value for index, (key, value) in enumerate(grouped_animals.items())}
        print(new_dict)

        return new_dict

    def get_groups(self):
        sorted_groups = self.sort_animals()
        for key, value in sorted_groups.items():
            print(key, ":", value)


ramat_gan_safari = Zoo("Ramat Gan Safari")
ramat_gan_safari.add_animal("Tiger", "Lion", "Baboon", "Ape", "Cougar", "Cat", "Bear", "Crocodile")
ramat_gan_safari.get_animals()
ramat_gan_safari.sell_animal("Lion")
ramat_gan_safari.get_groups()
