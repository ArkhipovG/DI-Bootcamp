import math


# Exercise 1
def insert_item_at_index(lst, item, index):
    lst.insert(index, item)
    return lst


my_list = [1, 2, 3, 4, 5]
print(insert_item_at_index(my_list, 16, 0))
print("-------")


# Exercise 2

def count_spaces(input_string):
    space_count = input_string.count(' ')
    return space_count


print(count_spaces("Hello World"))
print("-------")


# Exercise 3
def count_upper_lower(input_string):
    upper_count = sum(1 for char in input_string if char.isupper())
    lower_count = sum(1 for char in input_string if char.islower())
    return upper_count, lower_count


print(count_upper_lower("Hello World"))
print("-------")


# Exercise 4
def sum_of_array(array):
    total = 0
    for num in array:
        total += num
    return total


print(sum_of_array(my_list))
print("-------")


# Exercise 5
def find_max(lst):
    max_num = 0
    for num in lst:
        if num > max_num:
            max_num = num
    return max_num


print(find_max(my_list))
print("-------")


# Exercise 6
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(4))
print("-------")


# Exercise 7
def list_count(lst, element):
    count = 0
    for item in lst:
        if item == element:
            count += 1
    return count


print(list_count(['a', 'a', 't', 'o'], 'a'))
print("-------")


# Exercise 8
def norm(lst):
    sum_of_squares = sum(x ** 2 for x in lst)
    l2_norm = math.sqrt(sum_of_squares)
    return l2_norm


print(norm([1, 2, 2]))
print("-------")


# Exercises 9
def is_mono(array):
    increasing = decreasing = True

    for i in range(1, len(array)):
        if array[i] < array[i - 1]:
            increasing = False
            break

    for i in range(1, len(array)):
        if array[i] > array[i - 1]:
            decreasing = False
            break

    return increasing or decreasing


print(is_mono([7, 6, 5, 5, 2, 0]))
print(is_mono([2, 3, 3, 3]))
print(is_mono([1, 2, 0, 4]))
print("-------")


# Exercise 10
def longest_word(lst):
    longest = ''

    for word in lst:
        if len(word) > len(longest):
            longest = word

    return longest


print(longest_word(["apple", "banana", "cherry"]))
print("-------")


# Exercise 11
def separate_ints_strs(lst):
    integer_list = []
    string_list = []

    for item in lst:
        if isinstance(item, int):
            integer_list.append(item)
        elif isinstance(item, str):
            string_list.append(item)

    return integer_list, string_list


mixed_list = [1, 'hello', 2, 'world', 3, 'python']
integers, strings = separate_ints_strs(mixed_list)
print("Integers:", integers)
print("Strings:", strings)
print("-----")


# Exercise 12
def is_palindrome(word):
    reversed_word = word[::-1]

    if word.lower() == reversed_word.lower():
        print(f"{word} is palindrome")
    else:
        print(f"{word} is not palindrome")


is_palindrome("radar")
is_palindrome("John")
is_palindrome("Radar")
print("-----")


# Exercise 13
def sum_over_k(input_string, k):
    total_sum = 0
    wordslist = [word.strip() for word in input_string.split(' ')]
    print(wordslist)

    for word in wordslist:
        if len(word) >= k:
            total_sum += 1
    return total_sum


print(sum_over_k('Do or do not there is no try', 3))
print("-----")


# Exercise 14
def dict_avg(dict):
    dict_sum = 0
    for key, value in dict.items():
        dict_sum += value

    dict_average = dict_sum / len(dict)

    return dict_average


print(dict_avg({'a': 1, 'b': 2, 'c': 8, 'd': 1}))
print("-----")


# Exercise 15
def common_div(a, b):
    a_divisors = [num for num in range(2, a + 1) if a % num == 0]
    print(a_divisors)
    b_divisors = [num for num in range(2, b + 1) if b % num == 0]
    print(b_divisors)
    common_divisors = [num for num in a_divisors if num in b_divisors]
    return common_divisors


print(common_div(10, 20))
print("-----")


# Exercise 16
def is_prime(number):
    number_divisors = [num for num in range(2, number + 1) if number % num == 0]
    if len(number_divisors) == 1:
        return True


print(is_prime(10))
print("-----")


# Exercise 17
def weird_print(lst):
    weird_list = []
    for i, num in enumerate(lst):
        if i % 2 == 0 and num % 2 == 0:
            weird_list.append(num)

    return weird_list


print(weird_print([1, 2, 2, 3, 4, 5]))
print("-----")


# Exercise 18
def type_count(**kwargs):
    count_dict = {}

    for arg_name, arg_value in kwargs.items():
        arg_type = type(arg_value).__name__
        count_dict[arg_type] = count_dict.get(arg_type, 0) + 1

    for type_name, count in count_dict.items():
        print(f"{type_name}: {count}", end=", ")


type_count(a=1, b='string', c=1.0, d=True, e=False)
print("-----")


# Exercise 19
def my_split(input_string, separator=" "):
    result = []
    word = ""

    for char in input_string:
        if char == separator:
            if word:
                result.append(word)
                word = ""
        else:
            word += char

    if word:
        result.append(word)

    return result


print(my_split("Hello world! How are you?"))
print(my_split("Hello world! How are you?", 'o'))
print("-----")


# Exercise 20
def convert_pass(word):
    password = '*' * len(word)
    return password

print(convert_pass("mypassword"))
