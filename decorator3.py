#decoration with @ symbol
#modern way
import time
def decoration(func):
    def inner(*args):
        start= time.time()
        func(*args)
        end = time.time()
        print((end-start)*1000)
    return inner

@decoration
def add(a, b):
    for i in range(1, 100):
        print(a+b)
add(1, 2)
@decoration
def multiply(a , b):
    for i in range(1, 100):
        print(a*b)
multiply(2, 2)

