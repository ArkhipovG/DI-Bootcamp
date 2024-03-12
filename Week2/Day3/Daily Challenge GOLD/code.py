
def get_user_input():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    score = int(input("Enter score: "))
    return name, age, score


data = [get_user_input() for _ in range(5)]


data.sort(key=lambda x: (x[0], x[1], x[2]))


print(data)


