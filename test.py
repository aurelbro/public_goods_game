from copy import deepcopy
import numpy as np
a=np.array([[2.,3.,2.],[4.,5.,6.]])
b=np.array([[.2,.35,.64], [1.3,6.2,9.845]])
print(a[0])
#print(a!=b)
#print(a[:,0])

A=[0.,1.,0.,1.,0.,0.,1.,1.,1.,1.,1.]
C=[ A[i] for i in range(len(A)) if (A[i]==1) ]
#print(C)
#print(12./10)

import numpy as np
B=np.array([1.,2.5,6.3,4.4])
C=np.array([1.,2.5,6.3,4.4])
print(B/C)

#from scipy.stats import binom
#prob = binom.cdf(x, n, p)
#print(prob)

#print(2<=5<=4)
a=[[2.,3.,2.],[4,5,6]]
b=deepcopy(a)
print(a[0]!=b[0])
print(a/b)