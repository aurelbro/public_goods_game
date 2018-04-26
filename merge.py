# import csv
# /home/aurelien/istc/public_goods_game/experimentsimport pandas as pd
import csv
import os
import sys


def usage():
    print("usage : folder")


numberOfArgs = len(sys.argv)
print(numberOfArgs)
if(numberOfArgs < 2):
    usage()
    exit(-1)

folder = sys.argv[1]

# c = pd.read_csv(
# '/home/aurelien/istc/public_goods_game/experiments/exemple.tsv')
# print(c)
# print(c[1])
# d = pd.read_csv(
# '/home/aurelien/istc/public_goods_game/experiments/exemple_2.tsv')
# c = pd.concat([a, b])
# c.to_csv("/home/aurelien/istc/public_goods_game/experiments/merge_exemple_2.tsv", index=False)


# import csv
# with open('/home/aurelien/istc/public_goods_game/experiments/merge_exemple_5.tsv', 'a') as f:
# writer = csv.writer(f, delimiter='\t', lineterminator='\n')
# writer.writerow(
# c)


# I prefer this solution using the csv module from the standard library and the with statement to avoid leaving the file open.

# The key point is using 'a' for appending when you open the file.

# a = pd.read_table(
# '/home/aurelien/istc/public_goods_game/experiments/exemple.tsv')
# b = pd.read_table(
# '/home/aurelien/istc/public_goods_game/experiments/exemple_2.tsv')exemple_7.tsv", 'w')

file = open(folder + "/merge_result.dat", "w")
writer = csv.writer(file, delimiter="\t")

for filename in os.listdir(folder):
    if(filename.endswith(".tsv")):
        print(filename)
        fd = open(folder+"/"+filename, "rt")
        rd = csv.reader(fd, delimiter="\t")
        for row in rd:
            writer.writerow(row)

    # c = pd.concat([a, b], join='outer')
# c.to_csv("/home/aurelien/istc/public_goods_game/experiments/merge_exemple.csv", index=False)

# import csv
# fields = ['first', 'second', 'third']
# with open('/home/aurelien/istc/public_goods_game/experiments/merge_exemple_3.tsv', 'a') as f:
#   writer = csv.writer(f)
#  writer.writerow(c)
# file.close()
