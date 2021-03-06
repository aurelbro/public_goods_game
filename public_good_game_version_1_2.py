# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 14:37:50 2018

@author: Aurélien
"""

Z = 1000                      # number of players
N = 10                       # number of players per random group
r = 12                        # benefit
c = 1                         # cost
mu = 0.01                        # mutation rate
Beta = 10                    # selection stength
# number of games played before we launch the evolution process
number_of_games = 100
# maximum number of strategies changed during an evolution process
nI = 5
S = [0, 1]                     # set of strategies
fc = 0
number_of_generations = 100000

# importations
from random import *
from math import exp, log
import numpy as np
import matplotlib.pyplot as plt


# auxiliary functions
def indicator_function(boolean):
    if (boolean):
        return 1
    return 0


def prob_of_changing_strategy(i, j, W):
    return(1./(1 + exp(- Beta * (W[j-1] - W[i-1]))))


def number_of_cooperators(t):
    return(sum(t))


def tabel_payoff(n):
    payoff = [0]*2
    payoff[0] = n*r/N - c
    payoff[1] = n*r/N
    return payoff


# tableau des paiements possbles dans un mini-jeu
Payoffs = [tabel_payoff(n) for n in range(N+1)]
# print(Payoffs)

# game simulation function


def complete_game(A):
    W = np.zeros(Z)
    number_of_groups = Z//N
    groups = [i for i in range(1, Z+1)]

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
def evolution(A, W):
    l = len(S)
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
def main(A, number_of_rounds):
    tab = np.zeros(number_of_rounds)
    tab[0] = number_of_cooperators(A)
    print(0, tab[0])
    W = complete_game(A)
    for i in range(1, number_of_rounds):
        B = evolution(A, W)
        if (B != A):
            A = B
            tab[i] = number_of_cooperators(A)
            print(i, tab[i])
            W = complete_game(A)
        else:
            tab[i] = number_of_cooperators(A)
            print(i, tab[i])
    plt.plot(np.arange(1, number_of_rounds+1), tab)
    plt.title("number of cooperators at each round")
    plt.show()


def main_2(A, number_of_rounds):
    #print("x")
    tab = np.zeros(number_of_rounds)
    tab[0] = number_of_cooperators(A)
    # print(0, tab[0])
    W = complete_game(A)
    for i in range(1, number_of_rounds):
        B = evolution(A, W)
        if (B != A):
            A = B
            tab[i] = number_of_cooperators(A)
            #print(i, tab[i])
            W = complete_game(A)
        else:
            tab[i] = number_of_cooperators(A)
    #return(tab[number_of_rounds-1])
    return tab

# test
# import time
# debut=time.time()
#main([0]*int(Z*(1-fc)) + [1]*int(Z*fc), number_of_generations)
# fin=time.time()
# print(fin)
# heat_map_results = np.zeros((9, 100))
# for i in range(9):
#   for j in range(100):
#      heat_map_results[i, j] = main_2([0]*(100+i) + [1]*(900-i), 100)


# plt.imshow(heat_map_results, cmap='hot')
# plt.show()


#plt.hist([main_2([0]*int(Z*(1-fc)) + [1]*int(Z*(fc)),
                 #number_of_generations) for j in range(10)])
#plt.title("0 cooperators initially")
#plt.xlabel("Number of final cooperators")
#plt.ylabel("Percentage")
#plt.show()

#main_2([0]*(100) + [1]*(900), 100000)
for j in range(10):
    plt.plot(np.arange(1, number_of_generations+1), main_2([0]*int(Z*(1-fc)) + [1]*int(Z*fc), number_of_generations))
plt.title("0 cooperators initially")
plt.xlabel("Number of final cooperators")
plt.ylabel("Number of occurences")
plt.show()