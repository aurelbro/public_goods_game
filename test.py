# -*- coding: utf-8 -*-

from copy import deepcopy
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon
a=np.array([[2.,3.,2.],[4.,5.,6.]])
b=np.array([[.2,.35,.64], [1.3,6.2,9.845]])
#print(a[0])
#print(a!=b)
#print(a[:,0])

A=[0.,1.,0.,1.,0.,0.,1.,1.,1.,1.,1.]
C=[ A[i] for i in range(len(A)) if (A[i]==1) ]
#print(C)
#print(12./10)

import numpy as np
B=np.array([1.,2.5,6.3,4.4])
C=np.array([1.,2.5,6.3,4.4])
#print(np.argmin(B))
#print(np.argmax(B))
#print(B/C)

#from scipy.stats import binom
#prob = binom.cdf(x, n, p)
#print(prob)

#print(2<=5<=4)
#a=[[2.,3.,2.],[4,5,6],[7,8,9]]
 #b=deepcopy(a)
#print(a[0]!=b[0])
#print(a/b)
#print(type(B))
#print(a[0:4:2])
#print( np.mean(a[0:2],axis=0)[1] )

def fermi_function(x, beta):
  return(1./(1 + np.exp(- beta * x)))

x = np.linspace(-3, 3, 30)
y = fermi_function(x,0.1)
plt.plot(x, y)

plt.show()
#import math
#from scipy.stats import powerlaw
#r = powerlaw.rvs(2, loc=0, scale='infinity', size=10)
#print(r)

#s = np.random.pareto(1, 10)+1
#print(s)