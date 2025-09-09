import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.vq import kmeans2

# np.random.multivariate_normal(mean, cov, size)

a=np.random.multivariate_normal([0,2],[[2,1],[1,1.5]],size=200)
b=np.random.multivariate_normal([2,6],[[1,-1],[-1,5]],size=400)
c=np.random.multivariate_normal([6,7],[[3,2],[2,3]],size=250)
z=np.concatenate((a,b,c),axis=0)
np.random.shuffle(z)
plt.scatter(z[:,0],z[:,1])
plt.show()