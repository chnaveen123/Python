def outerFun(gname):
    guest = f"Mr.{gname}"

    def innerFun():
        print(f"Hello {gname}")

    innerFun()

outerFun("Naveen")

print("-" * 40)
def outerFun():
    x = "sachin"
    def innerFun():
        print(f"Hello {x}")
    return innerFun

outerFun()

innerFun = outerFun()
innerFun()

del outerFun
innerFun()


print("-" * 40)

def outerFun():
    x = "sachin"

    def innerFun():
        print(f"Hello {x}")

    return innerFun