cdef int Z = 1000                      # number of players
cdef int N = 10                        # number of players per random group
cdef int r = 12                         # benefit
cdef int c = 1                         # cost
cdef int mu = 0                        # mutation rate
cdef float Beta = 10                     # selection stength
# number of games played before we launch the evolution process
cdef int number_of_games = 100
# maximum number of strategies changed during an evolution process
cdef int nI = 2
cdef int[] S = [0, 1]                     # set of strategies


# importations
from random import *
from math import exp, log
import numpy as np
import matplotlib.pyplot as plt


# auxiliary functions
def indicator_function(bool boolean):
    if (boolean):
        return 1
    return 0


def prob_of_changing_strategy(int i, int j, float[] W):
    return(1./(1 + exp(- Beta * (W[j-1] - W[i-1]))))


def number_of_cooperators(int [] t):
    return(sum(t))


def tabel_payoff(int n):
    cdef int[] payoff = [0]*2
    payoff[0] = n*r/N - c
    payoff[1] = n*r/N
    return payoff


# tableau des paiements possbles dans un mini-jeu
Payoffs = [tabel_payoff(n) for n in range(N+1)]
# print(Payoffs)

# game simulation function


def complete_game(float[] A):
    W = np.zeros(Z)
    cdef int number_of_groups = Z//N
    cdef int[] groups = [i for i in range(1, Z+1)]
    cdef int i,j,k
    for i in range(number_of_games):
        # on mélange aléatoirement groups
        shuffle(groups)
        tabel_c = [0]*number_of_groups
        for k in range(number_of_groups):
            tabel_c[k] = number_of_cooperators(
                [A[groups[k*N+l]-1] for l in range(N)])
            for j in range(N):
                W[groups[k*N:(k+1)*N][j]-1] = W[groups[k*N:(k+1)*N][j]-1] + \
                    Payoffs[tabel_c[k]][indicator_function(
                        A[groups[k*N+j]-1] == 0)]

    # W, tableau des payoffs alimenté à chaque étape
    W = W/number_of_games
    return W


# evolution function
def evolution(int[] A, float[] W):
    cdef int l = len(S)
    cdef int k
    cdef float a,b
    for k in range(nI):

        a = random()

        if (a < 1-mu):
            i = randint(1, Z)
            j = randint(1, Z)
            while (j == i):
                j = randint(1, Z)
            b = random()
            if (b < prob_of_changing_strategy(i, j, W)):
                A[i-1] = A[j-1]

        else:
            i = randint(1, Z)
            mutation = randint(1, l)
            A[i-1] = S[mutation - 1]

    return(A)


# main function
def main(int [] A, int number_of_rounds):
    tab = np.zeros(number_of_rounds)
    tab[0] = number_of_cooperators(A)
    print(0, tab[0])
    W = complete_game(A)
    for i in range(1, number_of_rounds):
        B = evolution(A, W)
        if (B != A):
            A = B
            tab[i] = number_of_cooperators(A)
            # print(i,tab[i])
            W = complete_game(A)
        else:
            tab[i] = number_of_cooperators(A)
            # print(i,tab[i])
    plt.plot(np.arange(1, number_of_rounds+1), tab)
    plt.title("number of cooperators at each round")
    plt.show()


def main_2(int[] A, int number_of_rounds):
    tab = np.zeros(number_of_rounds)
    tab[0] = number_of_cooperators(A)
    # print(0, tab[0])
    W = complete_game(A)
    for i in range(1, number_of_rounds):
        B = evolution(A, W)
        if (B != A):
            A = B
            tab[i] = number_of_cooperators(A)
            # print(i,tab[i])
            W = complete_game(A)
        else:
            tab[i] = number_of_cooperators(A)
    return(tab[number_of_rounds-1])


# test
# import time
# debut=time.time()
# main([0]*500 + [1]*500, 100000)
# fin=time.time()
# print(fin)
# heat_map_results = np.zeros((9, 100))
# for i in range(9):
 #   for j in range(100):
  #      heat_map_results[i, j] = main_2([0]*(100+i) + [1]*(900-i), 100)


# plt.imshow(heat_map_results, cmap='hot')
# plt.show()


plt.hist( [main_2([0]*800 + [1]*200, 100) for j in range(100)] )
plt.title("200 cooperators initially")
plt.xlabel("number of final cooperators")
plt.ylabel("Percentage")
plt.show()