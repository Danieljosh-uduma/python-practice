import time
import math

def calculate_time(func):
    
    def inner1(*args, **kwargs):
        begin = time.time()
        func(*args, **kwargs)
        end = time.time()
        
        print('time taken: ', func.__name__, end - begin)
        
    return inner1

@calculate_time
def factorial(num):
    time.sleep(2)
    print(math.factorial(num))
    
factorial(4)

def gen(func):
    
    def inner(n):
        val = func(n)
        if val == True:
            return 10101011
        else:
            return 0
    
    return inner

@gen
def pas(n):
    return True if n > 1 else False

print(pas(4))
