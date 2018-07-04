import csv
import sys
import os
import numpy as np
import matplotlib.pyplot as plt
#import seaborn as sns


#folder = sys.argv[1]

def creation_column(r_par, mu_par, beta_imit, beta_follow, fc_par, M_par):
    foldername = "simulations_with_leadership_egalitarian/r=%02d_mu=%.2f_Beta_imit=%.1f_Beta_follow=%.1f_fc=%.2f_M=%02d" % (r_par,mu_par, beta_imit, beta_follow, fc_par, M_par)
    #print foldername

    complete_list = []
    for file in os.listdir(foldername):
        if file.endswith(".tsv"):
            # print file
            with open(foldername + "/" + file, "r") as file:
                reader=csv.reader(file, delimiter='\t')
                #if (len(complete_list)<88):
                row=next(reader)
                    #for row in reader:
                line = map(float,row)
                complete_list.append(line[5999])
    #print(len(complete_list))
    res = np.histogram(complete_list, bins=[0,100,200,300,400,500,600,700,800,900,1000])
    #print res[0]
    return res[0]

def hist(r_par, mu_par, beta_imit, beta_follow, M_par):
    fc_init = [0.10, 0.30, 0.50, 0.70, 0.90]
    fc_final= [0,100,200,300,400,500,600,700,800,900,1000]
    hist_mat = np.zeros((10, len(fc_init)))
    for i in range(len(fc_init)):
       hist_mat[:,i]= creation_column(r_par, mu_par, beta_imit, beta_follow, fc_init[i], M_par)
    #print hist_mat
    
    if not os.path.exists("simulations_with_leadership_egalitarian/r=%02d_mu=%.2f_Beta_imit=%.1f_Beta_follow=%.1f_M=%02d" % (r_par, mu_par, beta_imit, beta_follow, M_par)):
        os.makedirs("simulations_with_leadership_egalitarian/r=%02d_mu=%.2f_Beta_imit=%.1f_Beta_follow=%.1f_M=%02d" % (r_par, mu_par, beta_imit, beta_follow, M_par))
    filename="simulations_with_leadership_egalitarian/r=%02d_mu=%.2f_Beta_imit=%.1f_Beta_follow=%.1f_M=%02d/heatmap" % (r_par, mu_par, beta_imit, beta_follow, M_par)
    np.save(filename, hist_mat)

    return

def plot_hist(r_par, mu_par, beta_imit, beta_follow, M_par):

    filename="simulations_with_leadership_egalitarian/r=%02d_mu=%.2f_Beta_imit=%.1f_Beta_follow=%.1f_M=%02d/heatmap.npy" % (r_par, mu_par, beta_imit, beta_follow, M_par)
    hist_mat=np.load(filename)


    #sns.heatmap(hist_mat)
    plt.matshow(hist_mat/10)
    axes=plt.gca()
    axes.xaxis.set_ticklabels(['', '10%', '30%', '50%', '70%', '90%'])
    axes.yaxis.set_ticklabels(['','0-10%', '20-30%', '40-50%', '60-70%', '80-90%'])
    axes.set_xlabel('part of cooperators at the beginning')
    axes.set_ylabel('part of cooperators at the end')
    axes.xaxis.set_label_position('bottom')
    axes.xaxis.set_ticks_position('bottom')
    plt.title("r="+str(r_par)+" mu="+str(mu_par)+" Beta_imit="+str(beta_imit)+" Beta_follow="+str(beta_follow)+" M="+str(M_par))
    plt.colorbar()
    plt.show()
    #H, xedges, yedges = np.histogram2d( x, y, bins=[[-0.0,0.05,0.2,0.4,0.6,0.8,0.95,1.01],10])
    #print(xedges)
    #print(yedges)
    ##plt.figure()
    ##plt.plot(x, y, 'ro')
    ##plt.grid(True)

    #plt.figure()
    #myextent  =[xedges[0],xedges[-1],yedges[0],yedges[-1]]
    #plt.imshow(H.T,origin='low',extent=myextent,interpolation='nearest',aspect='auto')
    ##plt.plot(x,y,'ro')
    


#for r_par in [8,10,12,14]:
#    for mu_par in [0.00,0.01,0.02]:
#        for beta_par in [0.1,1.0,10.0]:
#            for M_par in [0,2,4,6,8,10]:
#                hist(r_par, mu_par, beta_par, M_par)


hist(5,0.0,10.0,0.1,10)
plot_hist(5,0.0,10.0,0.1,10)