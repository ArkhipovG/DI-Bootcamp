# Exercise 1
def get_full_name(first_name="", middle_name="", last_name=""):
    if middle_name != "":
        print(first_name.title(), middle_name.title(), last_name.title())
    else:
        print(first_name.title(), last_name.title())


get_full_name(first_name="john", middle_name="hooker", last_name="lee")
get_full_name(first_name="bruce", last_name="lee")

# Exercise 2
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', ' ': '/'
}


def text_to_morse(text):
    morse_code = ''
    for char in text.upper():
        if char in MORSE_CODE_DICT:
            morse_code += MORSE_CODE_DICT[char] + ' '
        else:
            morse_code += '/ '
    return morse_code.rstrip()


def morse_to_text(morse_code):
    text = ''
    morse_code += ' '
    morse_char = ''
    for symbol in morse_code:
        if symbol != ' ':
            morse_char += symbol
        else:
            if morse_char in MORSE_CODE_DICT.values():
                text += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(morse_char)]
            else:
                text += ' '
            morse_char = ''
    return text


text = "HELLO WORLD"
morse_code = text_to_morse(text)
print("Text to Morse Code:", morse_code)

decoded_text = morse_to_text(morse_code)
print("Morse Code to Text:", decoded_text)


# Exercise 3
def box_printer(*word):
    list_of_strings = []
    if word not in list_of_strings:
        list_of_strings.extend(word)

    longest_word = ''
    for word in list_of_strings:
        if len(word) > len(longest_word):
            longest_word = word

    print("*" * (len(longest_word) + 3))
    for word in list_of_strings:
        print(f"*{word} {" " * (len(longest_word) - (len(word)))}*")
    print("*" * (len(longest_word) + 3))


box_printer("Hello", "World", "in", "reallylongword", 'a', "frame")


# Exercises 4
# Purpose of the function is sorting the list in ascending order
def insertion_sort(alist):
    for index in range(1, len(alist)):

        currentvalue = alist[index]  # In the first iteration currentvalue = 26 (second in the list)
        position = index  # In the first iteration position is 1

        while position > 0 and alist[position - 1] > currentvalue:
            # Checking if previous position is bigger than current and its not first in the list
            alist[position] = alist[position - 1]
            # If yes then changing currentvalue with previous
            position = position - 1
            # And position also changes to previous


        alist[position] = currentvalue
        # If "while" condition isn't True then value in the list changes with currentvalue
        # and for in loop become to the next step


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
insertion_sort(alist)
print(alist)
