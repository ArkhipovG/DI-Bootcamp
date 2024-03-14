from anagram_checker import AnagramChecker


def load_anagram_checker():
    return AnagramChecker()


def show_menu():
    print("Menu")
    print("(i) - Input a word")
    print("(x) - Exit")


def get_anagrams(user):
    word = input("Enter a word: ")
    if user.is_valid_word(word):
        user.get_anagram(word)
    else:
        print("Invalid word, try again")


def main():
    user = load_anagram_checker()
    while True:
        show_menu()
        choice = input(": ")
        if choice == "i":
            get_anagrams(user)
            print("----------")
        elif choice == "x":
            print("Thanks for playing, goodbye!")
            break
        else:
            print("Invalid choice")


main()
