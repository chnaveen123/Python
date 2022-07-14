def dec_with_arg(name1,name2,name3):
    def outer_fun(fun):
        def inner_fun(*args):
            print("print 2 player names", name1, name2)
            fun(*args)
            print("getting the name of 3rd player" , name3)
        return inner_fun
    return outer_fun


