class Farm:
    def __init__(self, farm_name):
        self.farm_name = farm_name
        self.animals = {}

    def add_animal(self, new_animal, number_of_animals=1):
        if new_animal in self.animals.keys():
            self.animals[new_animal] += number_of_animals
        else:
            self.animals[new_animal] = number_of_animals

    def get_info(self):
        info = f"{self.farm_name}'s farm\n \n"
        for animal, count in self.animals.items():
            info += f"{animal} : {count}\n"
        info += "\n   E-I-E-I-0!"
        return info

    def get_animal_types(self):
        return list(self.animals.keys())

    def get_short_info(self):
        sorted_animals = sorted(self.animals.keys())
        short_info = f"{self.farm_name}'s farm has "
        for i, animal in enumerate(sorted_animals):
            if self.animals[animal] > 1 and i < len(sorted_animals) - 2:
                short_info += f"{animal}s, "
            elif self.animals[animal] == 1 and i < len(sorted_animals) - 2:
                short_info += f"{animal}, "
            elif self.animals[animal] > 1 and i == len(sorted_animals) - 2:
                short_info += f"{animal}s "
            elif self.animals[animal] == 1 and i == len(sorted_animals) - 2:
                short_info += f"{animal} "
            elif self.animals[animal] > 1 and i == len(sorted_animals) - 1:
                short_info += f"and {animal}s"
            elif self.animals[animal] == 1 and i == len(sorted_animals) - 1:
                short_info += f"and {animal}"

        return short_info


macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('chicken')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())
print(macdonald.get_animal_types())
print(macdonald.get_short_info())
