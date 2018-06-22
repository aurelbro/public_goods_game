import numpy as np
import os
import csv
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

def heatmap(r_par, mu_par, beta_imit, beta_follow, fc_par, M_par):
    foldername = "simulations_with_leadership_exponential_advanced/r=%02d_mu=%.2f_Beta_imit=%.1f_Beta_follow=%.1f_fc=%.2f_M=%02d" % (r_par,mu_par, beta_imit, beta_follow, fc_par, M_par)
    mat=np.zeros((6000, 5))
    for file in os.listdir(foldername):
        if file.endswith(".tsv"):
            with open(foldername + "/" + file, "r") as file:
                reader=csv.reader(file, delimiter='\t')
                row=next(reader)
                line=[0]*6000
                #print(row[0]) 
                #print(type(row[0]))               
                #line=[float(i) for i in row[0]]
                for i in range(6000):
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
                  line[i]=map(float, a)
                matrix=np.zeros(600,5)
                for j in range(600):
                  for k in range(5):
                      matrix[j][k]=np.mean(line[100*j:100*(j+1)],axis=k)
                #print(line)
                #print(line[0])
                #line=list(line)
                #print(line)
                
                #print(row[1])
                #cats = []
                #the line below appends AND casts data from the csv
                #cats = [map(float, c[0:]) for c in row]
                #print(cats)
                #line = map(float,row)
                #for i in range(len(row)):
                 #   for j in range(5):
                #      mat[i][j]+= row[i][j]
    #return mat

heatmap(7,0.00,10.0,0.1,0.70,0)