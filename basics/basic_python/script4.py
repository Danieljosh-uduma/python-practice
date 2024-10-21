# functions

def greet(age, name='my friend'):
    print(f'hello {name}. you are {age} years old')
    
age = input('age: ')
greet(age, 'josh')

# parameters and arguments
""" 
parameters are the values accepted by the function inside the function definition
arguments are the values passed into the function when we call it, we can have default argument
"""
greet(age)

def change(val):
    val['age'] = 72

val = {'age': age}
change(val)
print(val)

def chang(val):
    val = 2

val = age
chang(val)
print(val)

# return statement
def score(name, val):
    if val > 50:
        return f'{name} you ae doing great'
    else:
        return f'{name}, i\'m not proud of you'
    
    
print(score('josh', int(age)))


# variable scope

# nested functions 
def shout(phrase):
    def say(word):
        print(word, end=' ')
        
    words = phrase.split()
    for word in words:
        say(word)
        
shout('i need money urgently, so help me')

# global, nonlocal, local
def count():
    count = 0
    
    def increment():
        nonlocal count
        count += 1
        print(count)
    
    for x in range(3):
        increment()
        
count()



# closures
def counter():
    count = 0
    
    def increment():
        nonlocal count
        count += 1
        return count
    
    return increment

increment = counter()
print(increment())
print(increment())
print(increment())
print(increment())

