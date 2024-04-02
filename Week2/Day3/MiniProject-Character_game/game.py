class Character:
    def __init__(self, name):
        self.name = name
        self.life = 20
        self.attack = 10
        print(f"A new character named {self.name} has been created.")

    def basic_attack(self, other):
        print(f"{self.name} attacks {other.name}!")
        other.life -= self.attack


class Druid(Character):
    def __init__(self, name):
        super().__init__(name)
        print("I am a Druid!")

    def meditate(self):
        print(f"{self.name} meditates and gains inner strength.")
        self.life += 10
        self.attack -= 2

    def animal_help(self):
        print(f"{self.name} calls upon the animals for help!")
        self.attack += 5

    def fight(self, other):
        print(f"{self.name} engages in combat with {other.name}!")
        damage = 0.75 * self.life + 0.75 * self.attack
        other.life -= damage


class Warrior(Character):
    def __init__(self, name):
        super().__init__(name)
        print("I am a Warrior!")

    def brawl(self, other):
        print(f"{self.name} engages in a brawl with {other.name}!")
        other.life -= 2 * self.attack
        self.life += 0.5 * self.attack

    def train(self):
        print(f"{self.name} trains hard and gets stronger!")
        self.attack += 2
        self.life += 2

    def roar(self, other):
        print(f"{self.name} lets out a mighty roar against {other.name}!")
        other.attack -= 3


class Mage(Character):
    def __init__(self, name):
        super().__init__(name)
        print("I am a Mage!")

    def curse(self, other):
        print(f"{self.name} curses {other.name}, weakening their attacks!")
        other.attack -= 2

    def summon(self):
        print(f"{self.name} summons magical energies to boost their attack!")
        self.attack += 3

    def cast_spell(self, other):
        print(f"{self.name} casts a spell on {other.name}!")
        damage = min(other.life, other.attack) // 2
        other.life -= damage


# Example usage:

druid = Druid("Eldara")
warrior = Warrior("Grom")
mage = Mage("Merlin")

druid.basic_attack(warrior)
warrior.brawl(druid)
mage.cast_spell(warrior)
druid.fight(warrior)
warrior.roar(druid)
mage.curse(warrior)
druid.meditate()
warrior.train()
mage.summon()
