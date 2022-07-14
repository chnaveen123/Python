def funlogger(fnc):
    def helper(*args):
        print("Logged into the service")
        print(fnc(*args))
        print("logged out of the service")
    return helper
@funlogger
def add(x, y):
    print("Add function called")
    return x + y


@funlogger
def sub(x,y):
    print("sub function called")
    return x - y

@funlogger
def mul(x, y):
    print("mul function called")
    return x * y

add(10,20)
sub(20,10)
mul(5,6)