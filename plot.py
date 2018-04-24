import csv
import matplotlib.pyplot as plt
import numpy as np
import sys

number_of_generations = 100000


def usage():
    print("usage : folder")


numberOfArgs = len(sys.argv)
print(numberOfArgs)
if(numberOfArgs < 2):
    usage()
    exit(-1)

folder = sys.argv[1]

with open(folder + "/exemple.tsv") as tsvfile:
    reader = csv.reader(tsvfile, delimiter='\t')
    for row in reader:
        plt.plot(np.arange(1, number_of_generations+1), map(float, row))
        plt.show()

#np.savetxt('/home/aurelien/Documents/test.txt', a)
#plt.title("500 cooperators, no mutation, r=12")
#plt.xlabel("Number of generations")
#plt.ylabel("Number of cooperators")
#axes = plt.gca()
#axes.set_ylim(0, 1000)
# plt.show()
#plt.savefig('experiments/test_%d_%.2f_%g_%j_%i.png' % (r, mu, Beta, fc, M))


#time.strftime("%d %B %H:%M:%S")
