class Animal:
    def __init__(self):
        print("Animal ")
        self.age = 1

    def eat(self):
        print("Animals eat")

class Bird(Animal):

    def fly(self):
        print("Birds fly")

class Fish(Animal):

    def swim(self):
        print("Fishes swim")


print("-" * 40)
cuckoo = Bird()
Bird.fly()


print("-" * 40)
dolpin = Fish()
dolpin.swim()
dolpin.eat()

