# Enums
# readable names that is bound to a constant value
from enum import Enum

class State(Enum):
    inactive = 0
    active = 1
    
print(State.active)
print(State.active.value)
print(State(1))
print(State['active'])
print(State['active'].value)
print(list(State))
print(len(State))




