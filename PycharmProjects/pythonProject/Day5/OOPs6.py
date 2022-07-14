class Player:

    def __init__(self, name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"name = {self.name}\nAge = {self.age}"

    def __repr__(self):
        return f"name = {self.name}\nAge = {self.age}"


pl1 = Player("Sourav",35)
print(str(pl1))

print("-" * 40)
print(pl1.__str__())

print("-" * 40)
print(pl1)

print("-" * 40)
print(repr(pl1))