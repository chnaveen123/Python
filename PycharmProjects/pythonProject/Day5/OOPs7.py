class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"Name = {self.name}\nsalary = {self.salary}"

    def __eq__(self, other):
        return self.salary == other.salary

    def __gt__(self, other):
        return self.salary > other.salary

    def __add__(self, other):
        return self.salary + other.salary

    def __mul__(self, other):
        return self.salary * other.salary

    def __sub__(self, other):
        return self.salary - other.salary

    

emp1 = Employee("Jack", 50000)
print(emp1)

print("-" * 40)
emp2 = Employee("Jill",45000)
print(emp2)

print("-" * 40)
print(emp1 == emp2)

if (emp1 == emp2):
    print("{} salary of {} is equal {} salary of {}".format(emp1.name, emp1.salary, emp2.name, emp2.salary))

else:
    print("{} salary of {} is NOT equal {} salary of {}".format(emp1.name, emp1.salary, emp2.name, emp2.salary))

print("-" * 40)
if (emp1 != emp2):
    print("{} salary of {} is NOT equal {} salary of {}".format(emp1.name, emp1.salary, emp2.name, emp2.salary))

else:
    print("{} salary of {} is equal {} salary of {}".format(emp1.name, emp1.salary, emp2.name, emp2.salary))

print("-" * 40)
if (emp1 > emp2):
    print("{} salary of {} is greater Than {} salary of {}".format(emp1.name, emp1.salary, emp2.name, emp2.salary))

else:

    print("{} salary of {} lessThan {} salary of {}".format(emp1.name, emp1.salary, emp2.name, emp2.salary))




