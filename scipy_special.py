from scipy.special import expit, logit, softmax
print(expit(2)) #sigmoid(2)
print("logit",logit(0.8)) #inverse sigmoid(1.36)
print("softmax",softmax([5,7,3]))

print("#----------------scipy.special----------------#")
from scipy import special
import numpy as np
#compute cube root of each elements
print("Cube root of elements[64,125,729]: ",special.cbrt(np.array([64,125,729])))
print("Comput 10**x: ", special.exp10([3,5]))
print('''Combinations: special.comb(n,m), where
      n = no of objects
      m = no of object picked(order doesn't matters)''')
print("combinations:", special.comb(10,3) )
print('''permutations: special.perm(n,m)
      n = no of objects
      m = no of object picked (order matters)''')
print("permutations:", special.perm(10,4) )