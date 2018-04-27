import csv
import matplotlib.pyplot as plt
import numpy as np
import sys
import os
number_of_generations = 100000


def usage():
    print("usage : folder")


numberOfArgs = len(sys.argv)
# print(numberOfArgs)
if(numberOfArgs < 2):
    usage()
    exit(-1)


folder_1 = sys.argv[1]

for folder in os.listdir(folder_1):
    plt.figure(figsize=(20, 10), dpi=150)
    with open(folder_1 + "/" + folder + "/merge_result.dat", "r") as tsvfile:
        reader = csv.reader(tsvfile, delimiter='\t')
        complete_list = []

        for row in reader:
            line = map(float, row)
            plt.plot(np.arange(1, number_of_generations+1),
                     line, linestyle='-.', linewidth=0.05)
            complete_list.append(line)
            # plt.show()
            plt.title(folder.strip(".tsv"))
            plt.xlabel("Number of generations")
            plt.ylabel("Number of cooperators")
            axes = plt.gca()
            axes.set_ylim(0, 1000)
        mean = np.mean(np.array(complete_list), axis=0)
        print(mean)
        plt.plot(np.arange(1, number_of_generations+1),
                 mean, 'b', linewidth=4)
        plt.savefig(folder_1 + "/" + folder + "/graphical_representation.pdf")
        plt.close()
        print(folder)
