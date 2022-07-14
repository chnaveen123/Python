class Employee:

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        self.tech = ['Python', 'Java', 'J2EE','hibernate','Angular','React']


    def __str__(self):
        return f"Name = {self.name}\nsalary = {self.salary}"

    def __add__(self, other):
        return self.salary + other.salary

    def __len__(self):
        return len(self.tech)

    def __iter__(self):
        return iter(self.tech)

emp1 = Employee("Naveen",45000)
print(emp1)

print("-" * 40)
emp2 = Employee("John", 40000)
print(emp2)

print("-" * 40)
print(emp1 + emp2)

print("-" * 40)
print(len(emp2))

print("-" * 40)
print([t for t in emp1])
