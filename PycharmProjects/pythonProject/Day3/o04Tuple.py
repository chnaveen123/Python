print(tuple(range(1,5)))

print("-"*40)

t = (1,2,3,4,5,6,7.9,'eight', 'nine', 'ten')
print(t[7])
print(t[0:5])
print(t[-1])
print(t[-1:-6:-1])
print("-"*40)

t = (1,2,3,1,2,1,1,2,3,4,2,1,2,1,3,1,2,5)
print(type(t))
print(t.count(1))
print(t.count(2))
print(t.count(3))
print(len(t))
print("-"*40)

print(t.index(2))
print(t.index(3))
print(t.index(3,4))
print(t.index(3,9))

print(t[1])
print("-"*40)

from collections import namedtuple

nmdTpl = namedtuple("students", "studid sname age clas gender")
stud = nmdTpl(studid = 10, sname = "Glen", age = 15, clas = 9, gender = "M")
print(stud)

print(stud.studid)
print(stud.sname)
print(stud.age)
print(stud.clas)
print(stud.gender)

print("-"*40)
print(stud)

print("-"*40)

stud1 = nmdTpl(studid = 25, sname = "memi", age = 20, clas = 12, gender = "FM")
print(stud1)

print(stud1.studid)
print(stud1.sname)
print(stud1.age)
print(stud1.clas)
print(stud1.gender)

