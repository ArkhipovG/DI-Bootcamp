import os
import json
dir_path = os.path.dirname(os.path.realpath(__file__))

class MenuManager:
    def __init__(self):
        self.load_menu()


    def load_menu(self):
        with open('restaurant_menu.json', 'r') as file:
            self.menu = json.load(file)


    def add_item(self, name, price):
        self.menu['items'].append({'name': name, 'price': price})

    def remove_item(self, name):
        for item in self.menu['items']:
            if item['name'] == name:
                self.menu['items'].remove(item)
                return True
        return False

    def save_to_file(self):
        with open('restaurant_menu.json', 'w') as file:
            json.dump(self.menu, file)


manager = MenuManager()