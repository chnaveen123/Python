def greet():
    print("welcoe Mr.sachin to the event")

def greetGuest(gstName):
    print(f"Welcome Mr.{gstName} to the event")

def greetGuestCity(gstName, city='ranchi'):
    print(f"welcome Mr.{gstName} from {city} to the event")


greet()
print("-" *40)
gstName = "Naveen"
greetGuest(gstName)
print("-" *40)
greetGuestCity('Sachine', 'mumbai')
greetGuestCity('Naveen', 'mumbai')
print("-" *40)
greetGuestCity('Dhoni')


print("-" *40)

def enroll(fname,lname,dob, qlf,cno,adr,adhrno):
    print(fname, lname, dob, qlf, cno, adr, adhrno)


enroll(dob = "23/02/1998",
lname = "chiruveru",
fname = "Naveen",
adhrno = 123456789101,
adr = "abchdefgh",
qlf = "degree",
cno = 567239847)

print("-" *40)

def multiplyMe(x, y):
    return x * y

print(f"the product of the 10 and 20 is {multiplyMe(10,20)}")

print("-" *40)

def greet():
    return("hello world")
print(greet())

print("-" *40)

def fun(n):
    print(n, end= " ")
    if n == 1:
        return  n
    fun(n - 1)
fun(10)


print("-" *40)

def fun(n):
    if n == 1:
        return n
    else:
        return n * fun(n-1)

print(fun(5))






