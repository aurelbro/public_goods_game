# -*- coding: utf-8 -*-
import numpy as np
import os
import csv
import matplotlib
import matplotlib.pyplot as plt
#np.random.seed(0)
#import seaborn as sns
#sns.set()
# uniform_data = np.random.rand(10, 12)
# ax = sns.heatmap(uniform_data)
# data = [[][]

# for file in os.listdir(folder):
#   with open(folder + "/" + file, "r") as file:
#      reader = csv.reader(file, delimiter='\t')

#     for row in reader:
#        line = map(float, row)
#       data.append(line)

#import plotly.plotly as py
#import plotly.graph_objs as go

#trace = go.Heatmap(z=[[1, 20, 30],
#                      [20, 1, 60],
#                      [30, 60, 1]])
#data = [trace]
#py.plot(data, filename='basic-heatmap')

def heatmap(r_par, beta_follow, fc_par, M_par):
    foldername = "simulations_with_leadership_exponential_roulette_wheel_death/r=%02d_Beta_follow=%.1f_fc=%.2f_M=%02d" % (r_par, beta_follow, fc_par, M_par)
    matr=np.zeros((10000, 10))
    matrix=np.zeros((10,10000, 10))
    c=0                                       # creation of the matrix
    for file in os.listdir(foldername):                           # pour chaque fichier: 
        if file.endswith(".tsv"):
          #c+=1
          with open(foldername + "/" + file, "r") as file:
                reader=csv.reader(file, delimiter='\t')
                row=next(reader)
                row=next(reader)
                #row=next(reader)
                #matr=[0]*6000
                #print(row[0]) 
                #print(type(row[0]))               
                #line=[float(i) for i in row[0]]
                for i in range(10000):
                  a=row[i].strip('[]')
                  a=a.split(' ')
                #if ('' in line):
                  while ('' in a):
                    a.remove('')
                #line=[i in line if i!="''"]
                #print(type(line))
                #line=line.split(']')
                #line=map(list, row[0])
                #print(line)
                  matr[i]=map(float, a)                             # line[i] contient le tableau de la repartition des C à la i eme generation
                #print(matr[0:2])
                #print(matr)
                #print(np.mean(matr[0:2],axis=0))
                #matrix=np.zeros((600,5))
                for j in range(100):
                    matrix[c][j]=np.mean(matr[100*j:100*(j+1)],axis=0)
                #print(matrix)
                c+=1
                #print(np.mean(matrix[0:2],axis=0))
                #line=list(line)
                #print(matrix[0::600])
                #for k in range(600):
                #  mat[k]=np.mean(matrix[k::600],axis=0)
                #print(mat)
                #print(row[1])
                #cats = []
                #the line below appends AND casts data from the csv
                #cats = [map(float, c[0:]) for c in row]
                #print(cats)
                #line = map(float,row)
                #for i in range(len(row)):
                 #   for j in range(5):
                #      mat[i][j]+= row[i][j]
    #print(matrix[9])
    mat=np.zeros((100,10))
    #print(matrix[0][60])
    for k in range(100):
      mat[k]= np.mean(np.transpose(np.column_stack((matrix[j][k] for j in range(10)))), axis=0)
    #print(mat)
    #for i in range(600):
    #  mat[i]= np.mean(np.concatenate(matrix[j][i] for j in range(10)),axis=0)
    mat=np.transpose(mat)
    plt.matshow(mat)
    axes=plt.gca()
    #axes.xaxis.set_ticklabels(['', '10%', '30%', '50%', '70%', '90%'])
    axes.yaxis.set_ticklabels(['','first decile', 'third decile', 'fifth decile ', 'seventh decile', 'ninth decile'])
    axes.set_xlabel('part of cooperators in each strength interval in function of time')
    axes.set_ylabel('strength interval')
    axes.xaxis.set_label_position('bottom')
    axes.xaxis.set_ticks_position('bottom')
    plt.clim(0.075,0.125)
    plt.title("r="+str(r_par)+" Beta_follow="+str(beta_follow)+" fc="+str(fc_par)+" M="+str(M_par))
    plt.colorbar()
    plt.show()

heatmap(3,1.,0.70,4)