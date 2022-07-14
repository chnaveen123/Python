
import threading
import os

def job1():
    print("job1 is set to thread:{}".format(threading.currentThread().name))