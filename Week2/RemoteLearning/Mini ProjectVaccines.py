import random
from faker import Faker
import uuid

fake = Faker()


class Human:
    def __init__(self, id_number, name, age, priority, blood_type):
        self.id_number = id_number
        self.name = name
        self.age = age
        self.priority = priority
        self.blood_type = blood_type
        self.family = []

    def __str__(self):
        return f'Name: {self.name}, Age: {self.age}, Priority: {self.priority}'

    def add_family_member(self, human):
        self.family.append(human)
        human.family.append(self)


# Generating 1000 random humans with unique ID numbers
def generate_humans(num):
    id_numbers = []
    for _ in range(num):
        id_numbers.append(str(uuid.uuid4()))

    humans = []
    for _ in range(num):
        humans.append(Human(id_number=str(id_numbers.pop()),
                            name=fake.name(),
                            age=str(random.randint(18, 90)),
                            priority=random.choice([True, False]),
                            blood_type=random.choice(['A', 'B', 'AB', 'O'])))

    return humans


humans_list = generate_humans(1000)


class Queue:
    def __init__(self):
        self.humans = []

    # Adds a human to the queue
    def add_person(self, human):
        if int(human.age) > 60 or human.priority:
            self.humans.insert(0, human)
        else:
            self.humans.append(human)
        return self.humans

    # Returns the index of a human in the queue
    def find_in_queue(self, human):
        for index, item in enumerate(self.humans):
            if item.id_number == human.id_number:
                return index

    # Swaps person1 with person2.
    def swap(self, person1, person2):
        index1 = self.find_in_queue(person1)
        index2 = self.find_in_queue(person2)
        self.humans[index1] = person2
        self.humans[index2] = person1

    # Returns the next human waiting in the queue and removes him from the queue
    def get_next(self):
        return self.humans.pop(0)

    # Returns the first human with this specific blood type and removes him from the queue
    def get_next_blood_type(self, blood_type):
        for index, item in enumerate(self.humans):
            if item.blood_type == blood_type:
                return self.humans.pop(index)

    # Sort firstly by priority then by age
    def sort_by_age(self):
        return self.humans.sort(key=lambda x: (x.priority, x.age), reverse=True)

    # If the previous person in the queue is a family member, insert current person after the next person
    # from another family
    def rearrange_queue(self):
        rearranged_queue = []
        i = 0
        while i < len(self.humans):
            current_person = self.humans[i]
            if i > 0 and current_person.family and current_person.family[0] == self.humans[i - 1]:
                next_person_index = i + 1
                while next_person_index < len(self.humans) and self.humans[next_person_index].family == current_person.family:
                    next_person_index += 1
                if next_person_index < len(self.humans):
                    rearranged_queue.append(self.humans[next_person_index])
                    i += 1
            rearranged_queue.append(current_person)
            i += 1
        self.humans = rearranged_queue


test_person = Human(id_number='0bf8029e-2b07-4cdb-806c-de0b92cb3432',
                    name="Megan Lee",
                    age='32',
                    priority=True,
                    blood_type='O')

test_person2 = Human(id_number='0bf4324e-3b52-4ihb-456c-kl9j29er6874',
                     name="Frank Ocean",
                     age='54',
                     priority=True,
                     blood_type='A')

queue1 = Queue()
for i in range(10):
    queue1.add_person(random.choice(humans_list))

queue1.sort_by_age()
queue1.add_person(test_person)
queue1.add_person(test_person2)
for i, person in enumerate(queue1.humans):
    print(f"{i + 1}:", person)
print("-------")
print(f"Index of {test_person.name} is {queue1.find_in_queue(test_person)}")
print("-------")
print(f"Next person is: {queue1.get_next()}")
print("-------")
for i, person in enumerate(queue1.humans):
    print(f"{i + 1}:", person)
print("-------")
print(f"Next person with AB blood type is {queue1.get_next_blood_type("AB")}")
print("-------")
queue1.add_person(test_person2)
for i, person in enumerate(queue1.humans):
    print(f"{i + 1}:", person)
print("-------")

test_person.add_family_member(test_person2)
print(f"First member of {test_person.name} family: {test_person.family[0]}")
print("-------")
print(f"First member of {test_person2.name} family: {test_person2.family[0]}")

queue1.rearrange_queue()
for i, person in enumerate(queue1.humans):
    print(f"{i + 1}:", person)
print("-------")
