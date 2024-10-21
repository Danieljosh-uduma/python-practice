from enum import Enum

class profile(Enum):
    NAME = 'josh'
    AGE = 42
    GRADE = 7
    HEIGHT = 1.67
    

print(profile.NAME, profile.AGE, profile.GRADE)