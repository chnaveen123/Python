class Player:

    def __init__(self):
        self.name = "sachin"
        self.age = 36
        print("Player Initialized")

    def get_details(self):
        print(f"name = {self.name}\nAge = {self.age}")

    def __del__(self):
        print("distructor caled")
pl1 = Player()
pl1.get_details()

del pl1

print("-" * 40)

pl2 = Player()
pl2.name = "Naveen"
pl2.age = 25
pl2.get_details()



