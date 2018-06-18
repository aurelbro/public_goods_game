import csv
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import sys
import os

number_of_generations = 6000


def usage():
    print("usage : folder")


numberOfArgs = len(sys.argv)
# print(numberOfArgs)
if (numberOfArgs < 2):
    usage()
    exit(-1)

folder = sys.argv[1]
if (os.path.exists(folder + "/merge_result.dat")):
    os.remove(folder + "/merge_result.dat")
if (os.path.exists(folder + "/graphical_representation.pdf")):
    os.remove(folder + "/graphical_representation.pdf")
plt.figure(figsize=(20, 10), dpi=150)
complete_list = []
complete_list_2 = []
for file in os.listdir(folder):
    with open(folder + "/" + file, "r") as file:
        reader = csv.reader(file, delimiter='\t')
        line1=reader.next()#reader)
        #for row in reader:
        line = map(float, line1)#row)
        plt.plot(np.arange(1, number_of_generations+1),
                     line, linestyle='-.', linewidth=0.05 , color="red")
        complete_list.append(line)
        line2=reader.next() #reader)
        #for row in reader:
        line2= map(float, line2) #row)
        plt.plot(np.arange(1, number_of_generations+1),
                     line2, linestyle='-.', linewidth=0.05 , color="fuchsia")
        complete_list_2.append(line2)
    # plt.show()
plt.title(folder.strip(".tsv"))
plt.xlabel("Number of generations")
plt.ylabel("Number of cooperators")
axes = plt.gca()
axes.set_ylim(-10, 1010)
mean = np.mean(np.array(complete_list), axis=0)
print(mean)
mean_2 = np.mean(np.array(complete_list_2), axis=0)
plt.plot(np.arange(1, number_of_generations+1),
         mean, 'black', linewidth=4)
plt.plot(np.arange(1, number_of_generations+1),
         mean_2, 'blue', linewidth=4)
plt.savefig(folder + "/graphical_representation.pdf")

# np.savetxt('/home/aurelien/Documents/test.txt', a)

# plt.xlabel("Number of generations")
# plt.ylabel("Number of cooperators")
# axes = plt.gca()
# axes.set_ylim(0, 1000)
# plt.show()
# plt.savefig('experiments/test_%d_%.2f_.png' % (r, mu, Beta, fc, M))


# time.strftime("%d %B %H:%M:%S")
