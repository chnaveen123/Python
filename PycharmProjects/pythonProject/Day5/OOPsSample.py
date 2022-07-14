class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


    def __add__(self, other):
        return self.salary + other.salary

    def __mul__(self, other):
        return self.salary * other.salary

    def __sub__(self, other):
        return self.salary - other.salary

    def __truediv__(self, other):
        return self.salary / other.salary

    def __floordiv__(self, other):
        return self.salary // other.salary

emp1 = Employee("Jack", 50000)
print(emp1)

print("-" * 40)
emp2 = Employee("Jill", 45000)
print(emp2)

print("-" * 40)
print(emp1 + emp2)

print("-" * 40)
print(emp1 - emp2)

print("-" * 40)
print(emp1 * emp2)

print("-" * 40)
print(emp1 / emp2)

print("-" * 40)
print(emp1 // emp2)

