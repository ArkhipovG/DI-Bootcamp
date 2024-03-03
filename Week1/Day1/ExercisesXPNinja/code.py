my_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit,  sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
print(len(my_text))

longest_sentence = ""
input_text = ""
while True:
    input_text =input("Enter a sentence without A letter: ")
    if len(input_text) > len(longest_sentence) and "A" not in input_text:
        longest_sentence = input_text
        print("Congratulations! It is the longest sentence")
    else:
        print("Sorry, you are wrong, try again")

