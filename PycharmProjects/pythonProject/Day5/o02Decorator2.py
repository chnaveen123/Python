def doubleMesh(fnc):

    def helper(*args):

        print("=" * 40)

        fnc(*args)

        print("#" * 40)

    return helper

"""def starSingle(fnc):

    def helper(*args):
        print("*" * 40)
        fnc(*args)
        print("-" * 40)
    return helper
"""


@doubleMesh
def fun1():
    print("fun1........")


@doubleMesh

def fun2(x):
    print(f"fun2......{x}")

@doubleMesh
def fun3(x,y):
    print(f"fun3......{x,y}")

@doubleMesh
def fun4(x,y,z):
    print(f"fun4....{x,y,z}")

fun1()
fun2(5)

fun3(21,25)
fun4(10,11,12)

print("  " * 40)

print("$" * 40)
print("  " * 40)


def doubleMesh(fnc):
    def helper(*args):
        print("=" * 40)
        fnc(*args)
        print("#" * 40)

    return helper


def starSingle(fnc):
    def helper(*args):
        print("*" * 40)
        fnc(*args)
        print("-" * 40)

    return helper


def fun2(x):
    print(f"fun2 called....:{x}")


funlogger = doubleMesh(fun2)
funlog = starSingle(funlogger)
funlog(10)