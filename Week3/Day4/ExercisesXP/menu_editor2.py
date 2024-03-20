import psycopg2

from menu_manager2 import MenuManager
from menu_items import MenuItem


def show_user_menu():
    print("MENU")
    print("(v) - View an item")
    print("(a)- Add an item")
    print("(d)- Delete an item")
    print("(u)- Update an item")
    print("(s)- Show the menu")
    print("(x)- Exit")


def add_item_to_menu():
    name = input("Enter item name: ")
    price = int(input("Enter item price: "))
    item = MenuItem(name=name, price=price)
    item.save()


def remove_item_from_menu():
    name = input("Enter item name: ")
    tuple = MenuManager.get_by_name(name)
    item = MenuItem(name=tuple[1], price=tuple[2])
    item.delete()


def update_item_from_menu():
    name = input("Enter updating item name: ")
    tuple = MenuManager.get_by_name(name)
    item = MenuItem(name=tuple[1], price=tuple[2])
    new_name = input("Enter new item name: ")
    new_price = int(input("Enter new item price: "))
    item.update(new_name, new_price)


def show_restaurant_menu():
    print(MenuManager.all_items())


def view_item():
    print(MenuManager.get_by_name(input("Enter item to view: ")))


def main():
    while True:
        show_user_menu()
        choice = input(": ")
        if choice == "a":
            add_item_to_menu()
        elif choice == "d":
            remove_item_from_menu()
        elif choice == "s":
            show_restaurant_menu()
        elif choice == "u":
            update_item_from_menu()
        elif choice == "v":
            view_item()
        elif choice == "x":
            break
        else:
            print("Invalid choice. Please enter a valid option.")


main()
