va1 = [x ** 2 for x in range(1,11)]

print(va1)

va2 = (x ** 2 for x in range(1,11))

print(va2)

print("-" * 40)
from sys import getsizeof

val1 = [x ** 2 for x in range(1,100)]
val2 = ( x ** 2 for x in range(1,100))
print(val1)
print(val2)

print(getsizeof(val1))
print(getsizeof(val2))
