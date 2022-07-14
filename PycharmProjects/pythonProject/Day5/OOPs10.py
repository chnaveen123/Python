class Employee:

    def __init__(self,name):
        self.name = name
        self.tech = ['Python', 'Java', 'J2EE', 'hibernate', 'Angular', 'React']

    def __str__(self):
        return self.__name + " and tech " + ", ".join([vv for v in self.tech])

emp1 = Employee("Mark")
print(emp1)

print("-" * 40)

print(emp1.__dict__)

emp1.Employee__name = "steve"
print(emp1)