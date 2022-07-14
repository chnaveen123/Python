d1 = dict()
print(d1)
print(type(d1))

d2 = {}
print(type(d2))

print("*" * 40)

d3 = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4}
print(d3)
print(type(d3))

print("*" * 40)
d4 = dict([('name', 'naveen'), ('runs', 150),('opp', 'pak')])
print(d4)
print(type(d4))
print("*" * 40)

d5 = dict(name = 'naveen', runs = 200, oppn = 'MI', venue = 'hyd', year = 2022)
print(d5)
print(type(d5))
print("*" * 40)

print(f"Name : {d5['name']}")
print(f"runs : {d5['runs']}")
print(f"venue : {d5['venue']}")
d5['overs'] = 15
print(d5)

d5['runs'] = 151

print(d5)
print("*" * 40)
d5['age'] = None

print(d5)

del d5['age']

print(d5)

print("*" * 40)

d5['year'] = 2021
d5['runs'] = 131
print(d5)
print(d5['name'])

print("*" * 40)

print(d5.get('age'))



