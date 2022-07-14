
from threading import Thread

from time import sleep

def fun(args,thname):
    for i in range(args):
        print("iterating....")
        sleep(args)
    print("Thread exiting")

thread1 = Thread(target=fun,args=(1,"t1"))
thread2 = Thread(target=fun, args=(2,"t2"))

thread1.start()
thread2.start()

print(__name__ + "Exiting")


