def greet(name):
    return f'Hello {name.title()}, How are you doing today?'

name = input('Enter your name: ')
msg = greet
print(msg(name))