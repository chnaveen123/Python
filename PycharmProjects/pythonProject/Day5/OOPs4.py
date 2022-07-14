class Player:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def get_details(self):
        print(f"Name = {self.name}\nAge={self.age}")

pl1 = Player("sachin", 38)
pl1.get_details()

print("-" * 40)

pl2 = Player("Naveen",25)
pl2.get_details()

print("-" * 40)
Player.team = "India"

print(f"player : {Player.team}")
print(f"pl1 : {pl1.team}")
print(f"pl2 : {pl2.team}")







