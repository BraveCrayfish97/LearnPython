#decoration but without the @
#using old/traditional way
import time
def decoration(func):
    def inner(*args):
        start= time.time()
        func(*args)
        end = time.time()
        print((end-start)*1000)
    return inner


def add(a, b):
    for i in range(1, 100):
        print(a+b)
func1 = decoration(add)
func1(2, 3)

def multiply(a , b):
    for i in range(1, 100):
        print(a*b)

func2 = decoration(multiply)
func2(2, 2)
