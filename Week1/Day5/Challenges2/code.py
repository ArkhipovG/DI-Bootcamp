# Exercise 1
def draw_christmas_tree():
    rows = int(input("Enter how many tree rows you want: "))
    for i in range(1, rows + 1):
        # Print leading spaces
        for j in range(rows - i):
            print(" ", end="")
        # Print stars
        for k in range(2 * i - 1):
            print("*", end="")
        print()


draw_christmas_tree()


def draw_right_triangle():
    rows = int(input("Enter how many triangle rows you want: "))
    for i in range(1, rows + 1):
        # Print leading spaces
        for j in range(rows - i):
            print(" ", end="")
        # Print stars
        for k in range(i):
            print("*", end="")
        print()


draw_right_triangle()


def draw_doubled_right_triangle():
    rows = int(input("Enter how many triangle rows you want: "))
    for i in range(1, rows + 1):
        for j in range(i):
            print("*", end="")
        print()

    for i in range(rows, 0, -1):
        for j in range(rows - i):
            print(" ", end="")
        for k in range(i):
            print("*", end="")
        print()


draw_doubled_right_triangle()

# Exercise 2

my_list = [2, 24, 12, 354, 233]
for i in range(len(my_list) - 1):
    # Loop through each element in the list except the last one,
    # i iterates from 0 to 3.

    minimum = i
    # Set the index of the minimum element to the current index.

    for j in range( i + 1, len(my_list)):
        # Loop through the remaining elements in the list starting from i + 1.

        if(my_list[j] < my_list[minimum]):
            # Compare the current element with the minimum element

            minimum = j
            # If the current element is smaller, update the index of the minimum element.

            if(minimum != i):
                my_list[i], my_list[minimum] = my_list[minimum], my_list[i]
                # If the index of the minimum element is not the same as the current index,
                # swap the elements at positions i and minimum.

print(my_list)