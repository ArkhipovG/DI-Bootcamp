# Exercise 1
def display_message():
    print("We are learning Data Analysis")

display_message()

# Exersise 2
def favorite_book(title):
    print("One of my favorite books is", title)

favorite_book("Harry Potter and the Philosopher’s Stone")

# Exercises 3
def describe_city(city, country):
    exceptions = ['Hague', 'Vatican', 'Netherlands', 'Philippines', 'Congo']
    if city in exceptions and country in exceptions:
        print(f"The {city} is in the {country}")
    elif city in exceptions and country not in exceptions:
        print(f"The {city} is in {country}")
    elif city not in exceptions and country in exceptions:
        print(f"{city} is in the {country}")
    else:
        print(city, "is in", country)


describe_city("Tel-Aviv", "Israel")
describe_city("Hague", "Netherlands")
describe_city("Vatican", "Italy")
describe_city("Manila", "Philippines")

# Exercises 4
import random
def compare_numbers(user_number):
    random_number = random.randint(1, 100)
    if user_number == random_number:
        return print(f"Success! You guessed the right number: {user_number}")
    else:
        return print(f"Fail! The random number was {random_number} and your number was {user_number}")

compare_numbers(12)

# Exercise 5
def make_shirt(size, text):
    print(f"The size of the shirt is {size} and the text is '{text}'")

make_shirt("S", "I love programming")

def make_shirt(size =  "L", text = "I love Python"):
    print(f"The size of the shirt is {size} and the text is '{text}'")

make_shirt()
make_shirt("M")
make_shirt("S","I love Apple computers")
make_shirt(size = "XXXXL", text = "I am a big dude")

# Exercise 6
magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

def show_magicians():
    for magician in magician_names:
        print(magician)

show_magicians()

def make_great():
    for i in range(len(magician_names)):
        magician_names[i] = 'The Great ' + magician_names[i]

make_great()
show_magicians()

# Exercise 7
def get_random_temp(month):
    if month in [12, 1, 2]:
        return round(random.uniform(-10.0, 16.0), 1)
    elif month in [3, 4, 5]:
        return round(random.uniform(0.0, 23.0), 1)
    elif month in [6, 7, 8]:
        return round(random.uniform(16.0, 32.0), 1)
    elif month in [9, 10, 11]:
        return round(random.uniform(0.0, 23.0), 1)
    else:
        return None

print(get_random_temp(3))

def main():
    month = int(input("Type a month: "))
    temp = get_random_temp(month)
    print(f"The temperature right now is {temp} degrees Celsius")
    if temp < 0:
        print("Brrr, that’s freezing! Wear some extra layers today to stay warm.")
    elif 0 <= temp < 16:
        print("Quite chilly! Don’t forget your coat when heading out.")
    elif 16 <= temp <= 23:
        print("Enjoy the pleasant weather! It's a good time to take a leisurely stroll.")
    elif 24 <= temp <= 32:
        print("It's warm out there! Stay hydrated and apply sunscreen if you'll be out in the sun.")
    elif 33 <= temp <= 40:
        print("It's hot! Find shade or stay indoors during the hottest parts of the day to avoid heat exhaustion.")

main()

# Exercise 8

data = [
    {
        "question": "What is Baby Yoda's real name?",
        "answer": "Grogu"
    },
    {
        "question": "Where did Obi-Wan take Luke after his birth?",
        "answer": "Tatooine"
    },
    {
        "question": "What year did the first Star Wars movie come out?",
        "answer": "1977"
    },
    {
        "question": "Who built C-3PO?",
        "answer": "Anakin Skywalker"
    },
    {
        "question": "Anakin Skywalker grew up to be who?",
        "answer": "Darth Vader"
    },
    {
        "question": "What species is Chewbacca?",
        "answer": "Wookiee"
    }
]


def quiz():
    answer = "yes"
    while answer == "yes":
        correct_answers = []
        incorrect_answers = []
        incorrect_answers_and_questions = {}

        for i in data:
            print(i['question'])
            user_answer = input()
            if user_answer.lower() == i['answer'].lower():
                correct_answers.append(user_answer)
                print("Correct")
            else:
                incorrect_answers_and_questions[i['question']] = user_answer, i['answer']
                incorrect_answers.append(user_answer)

                print("Incorrect")

        print(f"You got {len(correct_answers)} correct answers and {len(incorrect_answers)} incorrect")

        for question, answer in incorrect_answers_and_questions.items():
            print(f"You answer wrong on the question '{question}', incorrect/correct answers: {answer}")



        if len(incorrect_answers) > 3:
            print("Do you want to play again? (yes/no)")
            answer = input()
        else:
            answer = "no"
            print("You win!")

quiz()
