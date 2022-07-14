
"""for i in range(1,6):
    for k in range(5,i,-1):
        print(" ",end="")

    for j in range(1, i+1):
        print(j,end=" ")
    print()
"""






st = "Hello World"

print(st.find("l",5))
print(st.index("W"))


"""st = "naveen"
print(st.upper())"""




print(''.join(reversed(st)))


"""r=[]
for i in range(1,len(st)+1):
    r.append(st[len(st)-i])
print(r)
print("".join(r))"""


a = "helowrd"
b = "HELOWRD"
print(st)
resTbl = (st.maketrans(a,b))
print(resTbl)

print(st.translate(resTbl))

print("*".center(20,"-"))
print(st[::-1])
print("*".center(20,"-"))

str = "*naveen*"

print(str.strip("*"))
print(str.rstrip("*"))
print(str.lstrip("*"))

print("*".center(20,"-"))

print(str.zfill(50))

print("*".center(20,"-"))


format = "welcome %s, Your rating of %s, what a  player"
values = ("Naveen", "superb")
print(format % values)
format = "welcome %s, Your rating of %.3f, what a  player"

print(format % ("naveen",4))
print(format % ("naveen",4.2))
print(format % ("naveen",4.234567))
print(format % ("naveen",4.26744567))


print("*".center(20,"-"))
from math import pi, e
print(f"{pi} and elures constant {e}")
print("*".center(20,"-"))

fullName = ["naveen","chiruveru"]
print(fullName)
print("{name}".format(name=fullName))
print("Mr.{name}".format(name=fullName))
print("*".center(20,"-"))


from math import pi
print("{}".format(pi))
print("{:>010.2f}".format(pi))


print("Alignment".center(40,"-"))
print("{:-^40}".format("Alighment"))