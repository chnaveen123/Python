fruits = [
    ('apple', 280),
    ('orange',80),
    ('grapes',160),
    ('pineapple',70),
    ('watermelon',140),
    ('guava',90),
    ('strawberry',350)
]

print(fruits)

price = ["fruit" for fruit in fruits]
print(price)

print("*" *  40)

price = [fruit for fruit in fruits]
print(price)

print("*" *  40)
price = [fruit[0] for fruit in fruits]
print(price)
print("*" *  40)
price = [fruit[1] for fruit in fruits]
print(price)
print("*" *  40)
price = [fruit[1] * 0.9 for fruit in fruits]
print(price)


print("*" *  40)

price = [fruit[1] * 0.75 for fruit in fruits]
print(price)

print("*" * 40)

price = [(fruit[0],fruit[1] * 0.9,fruit[1] * 0.750) for fruit in fruits]
print(price)





