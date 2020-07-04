import time
#code without decoration
#
#
#
#

def add(a, b):
    start= time.time()
    for i in range(1, 100):
        print(a+b)
    end = time.time()
    print((end-start)*1000)


def multiply(a , b):
    start = time.time()
    for i in range(1, 100):
        print(a*b)
    end = time.time()
    print((end-start)*1000)
add(2, 2)
multiply(2, 2)