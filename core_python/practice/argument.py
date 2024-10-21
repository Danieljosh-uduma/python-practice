import argparse

parser = argparse.ArgumentParser(
    description='get name from the user'
)

parser.add_argument('-n', '--name', metavar='name', required=True, help='write your name')

user = parser.parse_args()


print('hello', user.name)