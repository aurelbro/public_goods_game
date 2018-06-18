import matplotlib
matplotlib.use('Agg')
import csv
import matplotlib.pyplot as plt
import numpy as np
import sys
import os
number_of_generations = 6000


def usage():
    print("usage : folder")


numberOfArgs = len(sys.argv)
# print(numberOfArgs)
if(numberOfArgs < 2):
    usage()
    exit(-1)


folder_1 = sys.argv[1]

for folder in os.listdir(folder_1):
    if (os.path.exists(folder_1 + "/" + folder + "/merge_result.dat")):
        os.remove(folder_1 + "/" + folder + "/merge_result.dat")
    if (os.path.exists(folder_1 + "/" + folder + "/graphical_representation.pdf")):
        os.remove(folder_1 + "/" + folder + "/graphical_representation.pdf")
    plt.figure(figsize=(20, 10), dpi=150)
    complete_list = []
    complete_list_2 = []
    for file in os.listdir(folder_1 + "/" + folder):
        with open(folder_1 + "/" + folder + "/" + file, "r") as file:
            reader = csv.reader(file, delimiter='\t')
            line1=csvreader.next(reader)
        #for row in reader:
            line = map(float, line1)#row)
            plt.plot(np.arange(1, number_of_generations+1),
                     line, linestyle='-.', linewidth=0.05 , color="gray")
            complete_list.append(line)
            line2=csvreader.next(reader)
        #for row in reader:
            line2= map(float, line2) #row)
            plt.plot(np.arange(1, number_of_generations+1),
                     line2, linestyle='-.', linewidth=0.05 , color="orangered")
            complete_list_2.append(line2)
            # plt.show()
    plt.title(folder.strip(".tsv"))
    plt.xlabel("Number of generations")
    plt.ylabel("Number of cooperators")
    axes = plt.gca()
    axes.set_ylim(-10, 1010)
    mean = np.mean(np.array(complete_list), axis=0)
    # print(mean)
    mean_2 = np.mean(np.array(complete_list_2), axis=0)
    plt.plot(np.arange(1, number_of_generations+1),
             mean, 'black', linewidth=2)
    plt.plot(np.arange(1, number_of_generations+1),
         mean_2, 'red', linewidth=2)
    plt.savefig(folder_1 + "/" + folder +
                "/graphical_representation.pdf")
    plt.close()
    print(folder)
