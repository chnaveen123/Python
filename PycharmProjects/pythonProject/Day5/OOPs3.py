class Player:

    def __init__(self,name,age):
        self.name = name
        self.age = age
        print("player Initialized")

    def get_details(self):
        print(f"name = {self.name}\nage = {self.age}")


pl1 = Player("Dhoni",38)
pl1.get_details()

print("-" * 40)

pl2 = Player("Naveen",25)
pl2.get_details()

print("-" * 40)
print(pl1.__dict__)

print("-" * 40)
print(pl2.__dict__)

print("-" * 40)
pl2.runs = 200

print("-" * 40)
print(pl1.__dict__)
print(pl2.__dict__)




