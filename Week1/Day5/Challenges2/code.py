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

