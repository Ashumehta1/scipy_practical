from scipy.optimize import root
from math import cos
def equations(x):
    return x + cos(x)

myroot=root(equations,5)
print(myroot.x)