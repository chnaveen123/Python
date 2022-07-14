def begin_end(fun):
    def inner_fun(*args):
        print("session started")
        fun(*args)
        print("session ended")
    return inner_fun


class StartStop:
    def __int__(self,func):
        self.func=func
    def __call__(self, *args, **kwargs):
         return self.func(*args, **kwargs)





