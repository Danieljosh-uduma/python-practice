# user input, input() func.

# control statement
# list

dogs = ['roger', 'syd', 1]
print(1 in dogs)
print(dogs[:2])
dogs[2] = 'hope'
print(dogs)

# methods 
dogs.append('mike')
dogs.extend(['leo', 'jobber'])
dogs += ['hit', 'tee']

print(len(dogs))
print(dogs)

dogs.remove('mike')
print(dogs.pop())
print(dogs)


dogs.insert(2, 'tes')

dogs[1:1] = ['tes1', 'tes2']
dogs.sort(key=str.lower)
print(dogs)

print(sorted(dogs, key=str.lower))


# Tuples
names = ('roger', 'syd')

# immutable data type

# dictionaries
student = {
    'name': 'roger',
    'age': 13,
}

print(student['name'])
student['name'] = 'syd'
print(student.get('name'))
print(student.get('height', 1.67)) # default value 1.67

# pop method 
print(student.pop('age'))
print(student.popitem())
print(student)

student['name'] = 'josh'; student['class'] = 12; student['age'] = 13
student['fav food'] = 'Meat'
print('name' in student)
print(list(student.keys()))
print(list(student.values()))
print(list(student.items()))

del student['class']
stud = student.copy()



# sets
set1 = {'roger', 'syd'}
set2 = {'roger', 'lina', 'kola'}
set3 = {'roger', 'lina', 'kola', 'syd'}

intersect = set1 & set2
union = set1 | set2
diff = set1 - set2
superset = set3 > set2
subset = set1 < set3
print(intersect, union, diff, superset, subset)

# casting
print(list(set3))