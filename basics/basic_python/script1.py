# strings
# concatenation

name = 'josh'
name += ' is my name'
print(name) # append to a string

# casting, str()
# docstring
print("""
      i am a good boy,
      and i am 39 years old
      
      leave me
      """)#

# string methods
print(name.upper())
print(name.title())
print(name.islower())
print(name.capitalize())


# global functions
print(len(name))
print('os' in name)

# escaping characters '\'
print("my name is \"josh\"")

# string slicing and index
print(name[0])
print(name[-1])
# range (slicing)
print(name[0:3])


# boolean
# True or False

online = True
print('yes' if online else 'no')

# type 
print(type(online) == bool)

# global func 'any', 'all'
good = True
bad = False

character = any([good, bad])
print(character)
character = all([good, bad])
print(character)


# number data types
# int, float, complex 

num = 2 + 3j
num1 = complex(5, 2)
print(num, num1)
print(num1.real, num1.imag)

# built-in functions for number
# abs() absolute value
# round() round-up or down

print(round(6.9845, 1))
print(round(6.9845, 2))