def funLogger(fnc):
    def helper():
        print("My info logged in a service")
        fnc()
        print("My info logged out of the service")

    return helper
def normalFun():
    print("I shouold call as normal")

funLogger(normalFun)  #NO OUTPUT

funLogger(normalFun) ()
res_fun = funLogger(normalFun)
res_fun()

@funLogger
def basicFun():

    print("I should be called as Basic")
#basicfun = funLogger(basicFun)
basicFun()




