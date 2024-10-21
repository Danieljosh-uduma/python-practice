# accepting command line argument
import sys
print(sys.argv)

import argparse

parser = argparse.ArgumentParser(
    description='this program prints the color of my dog'
)
parser.add_argument('-c', '--color', metavar='color', required=True, choices={'red', 'blue', 'yellow'}, help='the color to search for')

args = parser.parse_args()

print(args.color)