"""

a = int(input("enter 1st value"))
b = int(input("enter 2nd value"))
c = int(input("enter 3rd value"))

if (a >= b and a >= c):
    print("a is the greatest")
elif (b >= a and b >= c):
    print("b is the greatest")
else :
    print("c is the greatest")


"""

i = 0
while(i < 10):
    print(i, end=" ")
    i += 1
print()

print("_" * 20)

print(f"i :{i}")
while(True):
    print(i, end=" ")
    i -= 1
    if i < 0:
        break
print()