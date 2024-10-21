# functions can also be an objects

def sit():
    return 'i am sitting'

val = sit
print(val())

num = lambda a: a * 2

x = num
print(x(6))


# passing functions as arguments
def add(a, b):
    return a + b

def minus(a, b):
    return a - b

def ans(func):
    val = func(2, 5)
    return val

new = ans
print(new(add))


#
def sum(x):
    def add(y):
        return x+y
    
    return add

n = sum(2)
print(n(5))



def name(func):
    return func

def greet():
    return 'josh'

greet = name(greet)
print(greet())


def decor(func):
    def wrapper():
        val = func()
        if val == True:
            return 1
        else:
            return 2
    return wrapper

def dd():
    return True

dd = decor(dd)
print(dd())
print(decor.__annotations__)