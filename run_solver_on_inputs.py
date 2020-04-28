import glob, os
import solver
os.chdir("inputs/")
files = []
for file in glob.glob("*.in"):
    files.append(file)
print(len(files))

for file in files:
    solver.main(file)