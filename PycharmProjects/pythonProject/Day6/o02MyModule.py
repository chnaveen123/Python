gname = "Sachin Tendulkar"

sports = ['cricket', 'tennis','soccer','hockey','football','swimming']

runs = {'odi' : 28500, 'test': 21000, 't20': 2300}

def greet(name):
    print(f"Greetings {name}, Welcome to the Event")

def addMe(x, y):
    return x + y

class Player:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        print(f"Name = {self.name}\nAge= {self.age}")


