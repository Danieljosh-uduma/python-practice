# list comprehension

num = [1, 2, 3, 4]
num_sq = [x**2 for x in num]

print(num_sq)

# polymorphism
class Dog:
    def talk(self):
        print('woof')
        
class Cat:
    def talk(self):
        print('meow')
        

# operator overloading
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __gt__(self, other):
        return True if self.age > other.age else False
p1 = person('josh',12)
p2 = person('niels',13)
print(p1 > p2)