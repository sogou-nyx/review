from enum import Enum, unique

@unique
class Test(Enum):
    A = 1
    B = 2
    C = 3

for k,v in Test.__members__.items():
    print(k, v.value)