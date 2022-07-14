def outerFun(gname):
    guest = f"Mr.{gname}"

    def innerFun():
        print(f"Hello {guest}")

    return innerFun()

outerFun("Naveen")

print("-" * 40)

def outerFun(gname):
    guest = f"Mr.{gname}"

    def innerFun():
        print(f"Hello {guest}")

    return innerFun

outerFun("Naveen") ()
print("-" * 40)
inrFun = outerFun("Rahul")
inrFun()

print("-" * 40)

print(outerFun.__name__)
print(outerFun("sehwag").__name__)
print("-" * 40)

inrFun = outerFun("Dhoni")
print("-" * 40)

print("Before the inner Fun call")

inrFun()
