import pickle
import glob, os
import pathlib
from parse import read_output_file, read_input_file
from utils import is_valid_network, average_pairwise_distance

os.chdir("outputs/")
files = []
for file in glob.glob("*.out"):
    files.append(file)
os.chdir("../")
scores = {}

path = str(pathlib.Path().absolute())
count = 1
for file in files:
    print(str(count) + "/" + str(len(files)))
    count += 1
    name = file.replace(".out","")
    input =  path + "/inputs/" + name + ".in"
    output = path + "/outputs/" + name + ".out"
    G = read_input_file(input)
    T = read_output_file(output, G)
    score = average_pairwise_distance(T)
    scores[name] = score

pickle.dump(scores, open('scores.obj', 'wb'))