string = input("String: ")
character = input("Character: ")
char_count = 0
for char in string:
    if char == character in string:
        char_count += 1

print(char_count)