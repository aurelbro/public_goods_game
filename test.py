a = [[2, 3, 2], [4, 5, 6]]
b = [[2, 3, 2], [4, 5, 6]]
#print(a != b)

A = [0., 1., 0., 1., 0., 0., 1., 1., 1., 1., 1.]
C = [A[i] for i in range(len(A)) if (A[i] == 1)]
# print(C)
# print(12./10)

import numpy as np
B = np.array([1., 2.5, 6.3, 4.4])
C = np.array([1., 2.5, 6.3, 4.4])
#print(B != C)
import matplotlib.pyplot as plt
r = 8.
N = 10
c = 1
M = 0
A = [0]*5+[1]*5


def tabel_payoff(n):
    payoff = [0]*2
    if (n >= M):
        payoff[0] = n*r/N - c
        payoff[1] = n*r/N
    else:
        payoff[0] = -c
        payoff[1] = 0
    return payoff


Payoffs = [tabel_payoff(n) for n in range(N+1)]
# print(Payoffs)

from scipy.stats import binom
#print(binom.cdf(0, 9, 0.6))
#print(binom.pmf(5, 9, 0.6))

for fc in [0.573, 0.574]:
    print(3*(8./10)*binom.pmf(3, 9, fc)+(8./10)*(1-binom.cdf(2, 9, fc))-1)
