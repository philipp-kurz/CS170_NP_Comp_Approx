import glob, os
import solver
import sys
from time import localtime, strftime
import pickle

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

updates = {}
try:
    scoresFile = open('updates.obj', 'rb')
except:
    pickle.dump(updates, open('updates.obj', 'wb'))
updates = pickle.load(open('updates.obj', 'rb'))
firstPositions = pickle.load(open("firstPositions.obj", 'rb'))

if loop:
    stored_exception = None

    while True:
        sys.stdout.write(getTime() + " - Started: 0000")
        improved = 0
        count = 0
        skipped = 0
        for i in range(len(files)):
            file = files[i]
            if file in firstPositions:
                skipped += 1
                continue
            try:
                count += 1
                for _ in range(4):
                    sys.stdout.write("\b")
                sys.stdout.write(str(count).zfill(4))
                sys.stdout.flush()
                res = solver.main(file)
                if res[1]:
                    if res[0] not in updates:
                        updates[res[0]] = 0
                    updates[res[0]] += 1
                    improved += 1
            except KeyboardInterrupt:
                stored_exception = sys.exc_info()
                i -= 1
                count -= 1
                for _ in range(13):
                    sys.stdout.write("\b")
                sys.stdout.write("Interrupted - Started: 0000")
                sys.stdout.flush()
        for _ in range(13):
            sys.stdout.write("\b")
        sys.stdout.write("Updated " + str(improved) + "/" + str(len(files)) + " outputs. Skipped "
                         + str(skipped) + "\n")
        sys.stdout.flush()

        if stored_exception:
            break

else:
    for file in files:
        solver.main(file)

pickle.dump(updates, open('updates.obj', 'wb'))