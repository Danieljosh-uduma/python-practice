# classes

class Animal: # parent class
    def walk(self):
        print('walking...')


# init function (constructor)
# child class
class Dog(Animal): # inheritance
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def bark(self):
        return 'woof!'
    
class Cat(Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def meow(self):
        return 'meow!'
    