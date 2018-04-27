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

folder_1 = sys.argv[1]


for folder in os.listdir(folder_1):
    # python merge.py folder
    file = open(folder_1 + "/" + folder + "/merge_result.dat", "w")
    writer = csv.writer(file, delimiter="\t")

    for filename in os.listdir(folder_1 + "/" + folder):
        if(filename.endswith(".tsv")):
            # print(filename)
            fd = open(folder_1 + "/" + folder+"/"+filename, "rt")
            rd = csv.reader(fd, delimiter="\t")
            for row in rd:
                writer.writerow(row)
