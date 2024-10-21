"""
docstring 
i am happy
ytrreeeeeee
"""

# variable 
name = 'josh'
age = 12
height = 1.67
online = True

print(type(name))

MyName = 'josh'
myName = 'josh'
my_name = 'josh daniel josh'

print(my_name.capitalize())
print(my_name.upper())
print(my_name.title())
print(my_name.title())
print(my_name.count(myName))
print(my_name.split())



# words = input('Enter Words: ')
# words = words.split()
# length = len(words)
# print(length)

'''
arithmetic operators
+,-,/,*,**,//,%
comparison
>,<,>=,<=,==,!=
logic
or, and , not
'''
print(False or True)
print(True and False)
print(not(True))

names = ['josh', 'emeka', 'ude']
print(names[2][1])
print(my_name[0])

word = names[0][3]+names[0][1]+names[2][0]+names[0][2]+names[1][0]
print(word.upper())

names.append('mark')
print(names)
names.pop()
print(names)
names.insert(1, 'mick')
print(names)
names.remove('josh')
print(names)

my_dict= {
    'names': ['josh', 'ude', 'emek'],
    'age': [12, 5, 2],
    'height': [1.67, 1.98, 1.05]
}

print(my_dict['names'][0][0])

my_dict['names'][0] = 'mike'
print(my_dict['names'][0])

if True:
    print('hello friend')
if False:
    print('bad friend')

age = 19
gender = 'female'

if age > 18:
    print('welcome user')
if gender == 'male':
    print('welcome user')

if not(age > 18) and gender == 'male':
    print('WELCOME BRO')
elif age < 18:
    print('you must be above 18')
elif gender != 'male':
    print('you must be male')
else:
    print('your age is low and you must be male')

for i in range(10):
    print(i)