a=[[2,3,2],[4,5,6]]
b=[[2,3,2],[4,5,6]]
print(a!=b)

A=[0.,1.,0.,1.,0.,0.,1.,1.,1.,1.,1.]
C=[ A[i] for i in range(len(A)) if (A[i]==1) ]
print(C)
print(12./10)

import numpy as np
B=np.array([1.,2.5,6.3,4.4])
C=np.array([1.,2.5,6.3,4.4])
print(B!=C)

from scipy.stats import binom
prob = binom.cdf(x, n, p)
print(probS)