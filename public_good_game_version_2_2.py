# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 15:24:07 2018

@author: Aurélien
"""

Z = 1000                      # number of players
N = 10                        # number of players per random group
# r = 12                        # benefit
c = 1                         # cost
# mu = 0                        # mutation rate
# Beta = 10                     # selection stength
# number of games played before we launch the evolution process
number_of_games = 100
# maximum number of strategies changed during an evolution process
nI = 5
S = [0, 1]                    # set of strategies
#fc = 0.5
# M = 0                          # necessary threshold for the benefit being shared
number_of_generations = 100000

# importations
from random import *
from math import exp, log
import numpy as np
import matplotlib.pyplot as plt
import sys
import csv
import time
import os


def usage():
    print("usage : folder, r, mu, beta, fc, M")


numberOfArgs = len(sys.argv)
if(numberOfArgs < 7):
    usage()
    exit(-1)

folder = sys.argv[1]
r = int(sys.argv[2])
mu = float(sys.argv[3])
Beta = float(sys.argv[4])
fc = float(sys.argv[5])
M = int(sys.argv[6])


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
    if (n >= M):
        payoff[0] = n*r/N - c
        payoff[1] = n*r/N
    else:
        payoff[0] = -c
        payoff[1] = 0
    return payoff


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
            # print(i,tab[i])
            W = complete_game(A)
        else:
            tab[i] = number_of_cooperators(A)
            # print(i,tab[i])
    plt.plot(np.arange(1, number_of_rounds+1), tab)
    plt.show()


def main_2(A, number_of_rounds):
    # if(numberOfArgs < 6):
    #    usage()
    #    exit(-1)
    tab = np.zeros(number_of_rounds)
    tab[0] = number_of_cooperators(A)
    # print(0, tab[0])
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
    return tab


# test
#main([0]*500 + [1]*500, 100000)

#plt.hist([main_2([0]*(500) + [1]*(500), 100000) for j in range(100)])
#plt.title("500 cooperators initially")
#plt.xlabel("Number of final cooperators")
# plt.ylabel("Percentage")
# plt.show()


# for j in range(1):
a = main_2([0]*int(Z*(1-fc)) + [1]*int(Z*fc), number_of_generations)
date = time.strftime("%Y%m%d-%H-%M-%S")
parameters = "r=%02d_mu=%.2f_Beta=%.1f_fc=%.2f_M=%02d.tsv" % (
    r, mu, Beta, fc, M)
subfolder = parameters
subfolder = folder + "/" + subfolder
if not os.path.exists(subfolder):
    os.mkdir(subfolder)
with open(subfolder + "/" + date + parameters, 'w') as fhOut:
    writer = csv.writer(fhOut, delimiter='\t', lineterminator='\n')
    writer.writerow(a)


#b = main_2([0]*int(Z*(1-fc)) + [1]*int(Z*fc), number_of_generations)
# with open(folder + "/exemple_2.tsv", 'w') as fhOut:
#    writer = csv.writer(fhOut, delimiter='\t', lineterminator='\n')
#    writer.writerow(b)
#plt.plot(np.arange(1, number_of_generations+1), a)
#np.savetxt('/home/aurelien/Documents/test.txt', a)
#plt.title("500 cooperators, no mutation, r=12")
#plt.xlabel("Number of generations")
#plt.ylabel("Number of cooperators")
#axes = plt.gca()
#axes.set_ylim(0, 1000)
# plt.show()
#plt.savefig('experiments/test_%d_%.2f_%g_%j_%i.png' % (r, mu, Beta, fc, M))
