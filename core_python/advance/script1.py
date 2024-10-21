# lambda

greet = lambda name: f'hello {name}' if name != '' else 'hello my friend'
print(greet(''))

big = lambda a, b: a if a > b else b
print(big(1,2))

# map() , filter() , reduce()

# def double(a):
#     return a*2

# OR
num = [1, 2, 3, 4, 5, 6]
double = lambda a : a * 2

result = map(double, num)
print(list(result))

result = list(map(lambda a: a * 3, num))
print(result)


# filter
isEven = lambda a : a % 2 == 0
result = list(filter(isEven, num))
print(result)

# reduce

expenses = [
    ('dinner', 80),
    ('transport', 120),
]

sum = 0
for expense in expenses:
    sum += expense[1]
    
print(sum)

from functools import reduce

sum = reduce(lambda a, b: a[1] + b[1],  expenses)


# recursion
# factorial

def factorial(n):
    return 1 if n == 0 or n == 1 else n * factorial(n-1)

print(factorial(4))