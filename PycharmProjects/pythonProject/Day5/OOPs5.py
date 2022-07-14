class Player:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def get_details(self):
        print(f"Name = {self.name}\nAge={self.age}")


    @classmethod
    def CreatePlayer(cls,fname,lname,age):
        return cls(f"{fname} {lname}",age)

pl1 = Player("Kohli", 33)
pl1.get_details()

print("-" * 40)

pl2 = Player.CreatePlayer("Sachin","Tendulkar", 40)
pl2.get_details()








