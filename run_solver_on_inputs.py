import glob, os
import solver
import sys
from time import localtime, strftime

def getTime():
    return strftime("%Y-%m-%d %H:%M:%S", localtime())

loop = False
if len(sys.argv) >= 2:
    if sys.argv[1] == "True":
        loop = True
os.chdir("inputs/")
files = []
for file in glob.glob("*.in"):
    files.append(file)
os.chdir("../")

print(getTime() + " - Started.")
if loop:
    while True:
        count = 0
        for file in files:
            res = solver.main(file)
            if res[1]:
                count += 1
        print(getTime() + " - Updated " + str(count) + "/" + str(len(files)) + " outputs.")
else:
    for file in files:
        solver.main(file)