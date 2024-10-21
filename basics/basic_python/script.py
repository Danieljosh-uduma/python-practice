# variables
name = 'josh'
age = 12
grade = 7.4
tall = True

# python keywords
"""
if, while, except, help, try, elis, else match, def etc.
"""

# Expression and statement
"""
an expression is any line of code that returns a value.
statement is an operation on a value
you can have multiple statement in a line just separated by a semi colon
"""

name = 'josh' ; print(name)

# comment
# indentation
# data type

age = 32; print(type(age) == int)
print(isinstance(name, int))

# type casting
"""
int(), str(), float(), bool()
complex(), list(), dict(), range(), set(), tuple()
"""

# assignment operators
"""
=, +=, -=, *=, /=, **=, %=, //=
"""
# arithmetic operators
"""
+, -, /, *, **, %, //
"""
# comparison operator
"""
>, <, >=, <=, ==, !=
"""
# boolean operators
"""
not, or, and
"""
# bitwise operator
# identity operator
"""
is
"""
# membership operator
"""
in
"""
# ternary operators
def is_adult(age):
    if age > 18:
        return True
    else:
        return False
    
def is_adult2(age):
    return True if age > 18 else False


com = 9 + 4j
print(type(com))

