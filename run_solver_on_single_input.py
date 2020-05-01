import glob, os
import solver
import sys
from time import localtime, strftime
import pickle

def getTime():
    return strftime("%Y-%m-%d %H:%M:%S", localtime())

file = sys.argv[1]

updates = {}
try:
    updates = open('updates.obj', 'rb')
except:
    pickle.dump(updates, open('updates.obj', 'wb'))
updates = pickle.load(open('updates.obj', 'rb'))
firstPositions = pickle.load(open("firstPositions.obj", 'rb'))


iteration = 1
while True:
    iteration += 1

    if file[:-3] in firstPositions:
        print()
        print("Output already optimal, will exit.")
        sys.exit()

    res = solver.main(file)

    if res[1]:
        if res[0] not in updates:
            updates[res[0]] = 0
        updates[res[0]] += 1
    print(str(iteration) + " " + file + " - Updated:  " + str(res[1]) + " - Score: " + str(res[2]))
    pickle.dump(updates, open('updates.obj', 'wb'))





