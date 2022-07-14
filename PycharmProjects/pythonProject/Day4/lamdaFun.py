"""def addMe(x,y):
    return x + y
a = addMe(x,y)
print(a(10,20))"""

b = lambda x, y : x + y
res = b(10,20)
print(f"res : {res}")

print("*" * 40)

l = list(range(1,11))

print(f"l : {l}")

res = list(map(lambda x: x**2,l))
print(f"res:{res}")

print("*" * 40)
temp = (23,30,25,32,36,42,40,38,20,18)
lst = list(map(lambda x: x / 1.8 + 32, temp))

print(lst)
print("*" * 40)

dollars = [12,30,25,38]
rupees = list(map(lambda x : x*75.8,dollars))
print(rupees)
print("*" * 40)
months = ['feb','mar','jan','apr','jun','may','aug','jul','oct','nov','sep','dec']
print(months)

from calendar import month_name

def month(name):
    l= []
    for i in list(month_name):
        l.append(i[0:3].lower())
    return l.index(name)
strmnths = sorted(months, key=month)
print(month("jan"))

print("*" * 40)

from calendar import month_name
def month(name):
    l= list(month_name)
    print(l)
    for i in range(len(l)):
        if name.lower() in l[i].lower():
            print(f"{name} is the {i} month")
month("aug")



