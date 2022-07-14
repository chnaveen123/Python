
def StartStopwitharguement(name1,name2,name3):
    def outer_fun(fun):
        def inner_fun(*args):
            fun(*args)
        return inner_fun
    return outer_fun
