from scipy.special import expit, logit, softmax
print(expit(2)) #sigmoid(2)
print("logit",logit(0.8)) #inverse sigmoid(1.36)
print("softmax",softmax([5,7,3]))

print("#----------------scipy.special----------------#")
from scipy import special
import numpy as np
#compute cube root of each elements
print("Cube root of elements[64,125,729]: ",special.cbrt(np.array([64,125,729])))