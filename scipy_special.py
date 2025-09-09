from scipy.special import expit, logit, softmax
print(expit(2))
print("logit",logit(0.8))
print("softmax",softmax([5,7,3]))