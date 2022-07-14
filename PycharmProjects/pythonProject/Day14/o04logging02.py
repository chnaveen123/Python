
import logging

logging.basicConfig(level=logging.INFO)

def multiplyMe(x,y):
    return x * y

i = int(input("Enter NUm 1 :"))
j = int(input("Enter NUm 2 :"))

logging.info("product of {0} and {1} is {2}".format(i,j,multiplyMe(i,j)))
