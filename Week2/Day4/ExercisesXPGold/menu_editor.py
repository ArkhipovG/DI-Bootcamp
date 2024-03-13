from menu_manager import MenuManager

def load_manager():
    return MenuManager()

def show_user_menu():
    print("MENU")
    print("(a)- Add an item")
    print("(d)- Delete an item")
    print("(v)- View the menu")
    print("(x)- Exit")


def add_item_to_menu(manager):
    name = input("Enter item name: ")
    price = float(input("Enter item price: "))
    manager.add_item(name, price)
    print(f"{name} was added successfully.")

def remove_item_from_menu(manager):
    name = input("Enter item name to remove: ")
    if manager.remove_item(name):
        print(f"{name} was deleted successfully.")
    else:
        print(f"Error: {name} not found in the menu.")

def show_restaurant_menu(manager):
    print("Restaurant Menu:")
    for item in manager.menu['items']:
        print(f"{item['name']}: ${item['price']}")

def main():
    manager = load_manager()
    while True:
        show_user_menu()
        choice = input(": ")
        if choice == "a":
            add_item_to_menu(manager)
        elif choice == "d":
            remove_item_from_menu(manager)
        elif choice == "v":
            show_restaurant_menu(manager)
        elif choice == "x":
            manager.save_to_file()
            print("Menu saved.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

main()

