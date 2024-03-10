import math
import random


# Exercise 1
class Circle:
    def __init__(self, radius=1.0):
        self.radius = radius

    def perimeter(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * self.radius ** 2

    def print_definition(self):
        print(f"A circle is a closed curve where all points are equidistant from a fixed point called the center.")
        print(f"It is defined by its radius, which is the distance from the center to any point on the circle.")


circle = Circle(3)
print("Perimeter:", circle.perimeter())
print("Area:", circle.area())
circle.print_definition()
print("------")


# Exercise 2
class MyList:
    def __init__(self, lst):
        self.lst = lst

    def reverse(self):
        return self.lst[::-1]

    def sort(self):
        return sorted(self.lst)

    def random_list(self):
        randlist = [random.randint(1, 26) for _ in range(len(self.lst))]
        return randlist


flist = MyList(['a', 'g', 's', 'b', 'w'])
print(flist.reverse())
print(flist.sort())
print(flist.random_list())
print("------")


# Exercise 3
class MenuManager:
    def __init__(self, menu):
        self.menu = menu

    def add_item(self, name, price, spice, gluten):
        return self.menu.append({'name': name, 'price': price, "spice level": spice, "gluten index": gluten})

    def show_menu(self):
        for item in self.menu:
            print(item)

    def update_item(self, name, price, spice, gluten):
        is_changed = False
        for item in self.menu:
            if name in item['name']:
                item['price'] = price
                item["spice level"] = spice
                item["gluten index"] = gluten
                is_changed = True

        if not is_changed:
            print(f"{name} is not in the menu")

    def delete_item(self, name):
        is_deleted = False
        for item in self.menu:
            if name in item['name']:
                self.menu.remove(item)
                is_deleted = True

        if not is_deleted:
            print(f"{name} is not in the menu")


fmenu = [{'name': 'Soup', 'price': 10, "spice level": "B", "gluten index": False},
         {'name': 'Hamburger', 'price': 15, "spice level": 'A', "gluten index": False},
         {'name': 'Salad', 'price': 18, "spice level": 'A', "gluten index": False},
         {'name': 'French Fries', 'price': 5, "spice level": 'C', "gluten index": False},
         {'name': 'Beef bourguignon', 'price': 25, "spice level": 'B', "gluten index": False}
         ]
my_menu = MenuManager(fmenu)
my_menu.add_item("Pizza Margherita", 12, 'A', False)
my_menu.show_menu()
print("------")
my_menu.update_item('Hamburger', 12, 'B', False)
my_menu.show_menu()
print("------")
my_menu.update_item('Cheeseburger', 12, 'B', False)
print("------")
my_menu.delete_item('Hamburger')
my_menu.show_menu()
print("------")
my_menu.delete_item('Cheeseburger')
