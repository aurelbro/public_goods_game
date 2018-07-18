# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 15:24:07 2018

@author: Aurélien
"""

Z = 1000                      # number of players
N = 10                        # number of players per random group
# r = 4.5                     # benefit
c = 1                         # cost
# mu = 0.1                       # mutation rate
# Beta_imit = 10                     # selection stength
# Beta_follow=1.0
# number of games played before we launch the evolution process
number_of_games = 100
# maximum number of strategies changed during an evolution process
nI = 5
S = [0, 1]                    # set of strategies
# fc = 0.5
# M = 0                          # necessary threshold for the benefit being shared
number_of_generations = 10000

# importations

#from math import exp, log
import numpy as np
#import matplotlib.pyplot as plt
import sys
import csv
import time
import os
from copy import deepcopy
from scipy.stats import expon

def usage():
    print("usage : folder, r, mu, beta_imit, beta_follow, fc, M")


numberOfArgs = len(sys.argv)
if(numberOfArgs < 8):
    usage()
    exit(-1)

folder = sys.argv[1]
r = float(sys.argv[2])
mu = float(sys.argv[3])
Beta_imit = float(sys.argv[4])
Beta_follow = float(sys.argv[5])
fc = float(sys.argv[6])
M = int(sys.argv[7])
run_number = int(sys.argv[8])

#print("gotten run_number = %d" % run_number)
# set the seed of the random number generator
new_seed = np.random.randint(100000)
np.random.seed(new_seed)
#seed = np.random.randint(1,10000)

# auxiliary functions


def indicator_function(boolean):
    if (boolean):
        return 1
    return 0


def fermi_function_imit(i, j, W):
    return(1./(1 + np.exp(- Beta_imit * (W[j-1] - W[i-1]))))

def fermi_function_follow(i, j, W):
    return(1./(1 + np.exp(- Beta_follow * (W[j-1] - W[i-1]))))

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

def values_of_fermi_function_with_strength(tab):            # calculation of all the transitions probabilities with respect to strengths
    l=len(tab)
    mat=[[0]*l for k in range (l)]
    for i in range(l):
        for j in range(l):
            mat[i][j]= fermi_function_follow(i, j, tab)
    return(mat)

strengths= np.ones(Z)
following= values_of_fermi_function_with_strength(strengths)   
# print(Payoffs)

# game simulation function


def complete_game(A):
    W = np.zeros(Z)
    number_of_groups = Z//N
    groups = [i for i in range(1, Z+1)]

    for i in range(number_of_games):
        # on mélange aléatoirement groups
        np.random.shuffle(groups)
        tabel_c = [0]*number_of_groups
        C = [0]*Z
        for k in range(number_of_groups):
            # print("len(A) = %d" % len(A))
            # for l in range(N):
                # print(groups[k*N+l]-1)
            n=np.random.randint(N)
            for m in range(N):
                b = np.random.random()
                if (b < following[groups[k*N+m]-1][groups[k*N+n]-1]):            #in each group, test if m player will follow the leader
                    C[groups[k*N+m] - 1] = A[0][groups[k*N+n] - 1]                    
                else:
                    C[groups[k*N+m] - 1] = A[0][groups[k*N+m] - 1]
               
            tabel_c[k] = number_of_cooperators(
                [C[groups[k*N+l] - 1] for l in range(N)])
            for j in range(N):
                W[groups[k*N:(k+1)*N][j]-1] = W[groups[k*N:(k+1)*N][j]-1] + \
                    Payoffs[tabel_c[k]][indicator_function(
                        C[groups[k*N+j]-1] == 0)]

    # W, tableau des payoffs alimenté à chaque étape
    W = W/number_of_games
    return W   


# evolution function
def evolution(A, W):
    l = len(S)
    B = deepcopy(A)
    for k in range(nI):

        a = np.random.random()

        if (a < 1-mu):
            i = np.random.randint(1, Z+1)
            j = np.random.randint(1, Z+1)
            while (j == i):
                j = np.random.randint(1, Z+1)
            b = np.random.random()
            if (b < fermi_function_imit(i, j, W)):
                B[0][i-1] = B[0][j-1]
                B[1][i-1] = B[1][i-1] + np.random.normal(0,0.05,1)
        else:
            i = np.random.randint(1, Z+1)
            mutation = np.random.randint(1, l+1)
            B[0][i-1] = S[mutation - 1]
            B[1][i-1] += np.random.normal(0,0.05,1)
    return(B)


# main function
# def main_4(A, number_of_rounds):

    #tab = np.zeros(number_of_rounds)
    #tab[0] = number_of_cooperators(A)
    #print(0, tab[0])
    #W = complete_game(A)
    # for i in range(1, number_of_rounds):
    #    B = evolution(A, W)
    #    C = [W[j] for j in range(len(A)) if (B[j] == 1)]
    #    D = [W[j] for j in range(len(A)) if (B[j] == 0)]
    #    print(i, "c:" + str(sum(C)/number_of_cooperators(B)),
    #          "d:"+str(sum(D)/(len(A)-number_of_cooperators(B))))
    #    if (B != A):
    #        A = B
    #        tab[i] = number_of_cooperators(A)
    # print(i,tab[i])
    #        W = complete_game(A)
    #    else:
    #        tab[i] = number_of_cooperators(A)
    # print(i,tab[i])
    #plt.plot(np.arange(1, number_of_rounds+1), tab)
    # plt.show()


# def main_2(A, number_of_rounds):
    # if(numberOfArgs < 6):
    #    usage()
    #    exit(-1)
    #tab = np.zeros(number_of_rounds)
    #tab[0] = number_of_cooperators(A)
    # print(0, tab[0])
    #W = complete_game(A)
    # for i in range(1, number_of_rounds):
    #    B = evolution(A, W)
    #    C = [W[j] for j in range(len(A)) if (A[j] == 1)]
    #    D = [W[j] for j in range(len(A)) if (A[j] == 0)]
    #    print(i, "c:" + str(sum(C)/number_of_cooperators(B)),
    #          "d:"+str(sum(D)/(len(A)-number_of_cooperators(B))))
    #    if (B != A):
    #        A = B
    #        tab[i] = number_of_cooperators(A)
    #print(i, tab[i])
    #        W = complete_game(A)
    #    else:
    #        tab[i] = number_of_cooperators(A)
    # return tab


#A = [0]*int(round(Z*(1-fc))) + [1]*int(round(Z*fc))

#main(A, 5000)

#a = main_2(A, number_of_generations)


# def main_3(A, number_of_rounds):

#    tab = np.zeros(number_of_rounds)
#    for i in range(number_of_rounds):
#        tab[i] = number_of_cooperators(A)
#        W = complete_game(A)
#        C = [W[j] for j in range(len(A)) if (A[j] == 1)]
#        D = [W[j] for j in range(len(A)) if (A[j] == 0)]
#        print(i, "c:" + str(sum(C)/number_of_cooperators(A)),
#              "d:"+str(sum(D)/(len(A)-number_of_cooperators(A))))
#        B = evolution(A, W)
#    plt.plot(np.arange(1, number_of_rounds+1), tab)
#    plt.show()


def main(A, number_of_rounds):

    tab = np.zeros((2*number_of_rounds,Z))
    W= complete_game(A)
    for i in range(number_of_rounds):
        tab[i]=A[0]
        tab[i+1]=A[1]
        B = evolution(A, W)
        A = B
        W = complete_game(A)
    return tab



A = [ [0]*int(round(Z*(1-fc))) + [1]*int(round(Z*fc)), strengths ]
a = main(A, number_of_generations)
#date = "run%04d" % seed # time.strftime("%Y%m%d-%H-%M-%S")
date = time.strftime("%Y%m%d-%H-%M-%S") + ("_%05d_" % new_seed)

parameters = "r=%02d_mu=%.2f_Beta_imit=%.1f_Beta_follow=%.1f_fc=%.2f_M=%02d.tsv" % (
    r, mu, Beta_imit, Beta_follow, fc, M)
subfolder = parameters.strip(".tsv")
subfolder = folder + "/" + subfolder
if not os.path.exists(subfolder):
    os.mkdir(subfolder)
with open(subfolder + "/" + date + parameters, 'w') as fhOut:
    writer = csv.writer(fhOut, delimiter='\t', lineterminator='\n')
    writer.writerow(a)
    #writer.writerow(a[1])
    #writer.writerow(a[2])