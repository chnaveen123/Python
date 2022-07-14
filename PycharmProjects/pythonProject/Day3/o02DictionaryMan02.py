print("{:-^40}".format("get"))
fruits = {'apple' : 200, 'orange' : 100, 'watermelon':150, 'guava' : 10}
print(fruits)

print(fruits['guava'])

print(fruits.get('grapes'))
print(fruits.get('grapes', 'Invalid key, please enter valid key'))

print("{:*^40}".format("keys"))
print(fruits)
k = fruits.keys()
print(k)

print("*" * 40)

for i in k:
    print(i, end=" ")
print()

print("*" * 40)

for k in fruits.keys():
    print(k + " => " + str(fruits[k]))
print("*" * 40)

for x in fruits.keys():
    print(f"{x} => {fruits[x]}")

print("{:*^40}".format("values"))
print(fruits)
print(fruits.values())

print("{:*^40}".format("set default"))
fruits.setdefault('mango','tasty')
print(fruits)
fruits.setdefault('graph', 50)
del fruits['mango']
print(fruits)

print("{:*^40}".format("fromkeys"))


cities = ['hyd','blr','chn','kol','mob','pun']
print(cities)
print(type(cities))

res1 = dict.fromkeys(cities)
print(res1)
res2 = dict.fromkeys(cities, 24)
print(res2)

print("{:*^40}".format("pop"))

veg = {'crt' : 25, 'bns' : 50, 'tmt' : 60, 'onions' : 20}
print(veg)

res = veg.pop('tmt')
print(res)
print(veg)


print("{:*^40}".format("popitem"))

veg = {'crt' : 25, 'bns' : 50, 'tmt' : 60, 'onions' : 20}
res2 = veg.popitem()
print(res2)
print(veg)
res3 = veg.popitem()
print(res3)
print(veg)