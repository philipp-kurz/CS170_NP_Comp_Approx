import networkx as nx
from parse import read_input_file, write_output_file
from utils import is_valid_network, average_pairwise_distance
import sys
import pathlib
import random
from datetime import datetime
import pickle

random.seed(datetime.now())

# Function to sort the list by second item of tuple
def Sort_Tuple(tup, pos):
    return (sorted(tup, key=lambda x: x[pos]))


def findSpanningTree(G):
    T = nx.Graph()
    n = len(list(G.nodes()))
    visited = [False] * n
    start = random.randrange(n)
    fringe = []
    fringe.append((-1, start))
    while len(fringe) > 0:
        edge = fringe.pop()
        if not visited[edge[1]]:
            visited[edge[1]] = True
            T.add_node(edge[1])
            if edge[0] > -1:
                weight = G.get_edge_data(edge[0], edge[1])['weight']
                T.add_edge(edge[0], edge[1], weight=weight)

            neighbors = list(nx.neighbors(G, edge[1]))
            random.shuffle(neighbors)
            for neighbor in neighbors:
                if not visited[neighbor]:
                    fringe.append((edge[1], neighbor))
    return T

# Returns: T: networkx.Graph
def solve(G):
    T = findSpanningTree(G)
    return T

# Usage: python3 solver.py test.in

def main(filename):
    print(filename, end=": ")
    input_name = filename[0:-3]
    path = str(pathlib.Path().absolute()) + "/" +  input_name + '.in'
    name = input_name
    if name[0:7] == "inputs/":
        name = name[7:]
    G = read_input_file(path)
    T = solve(G)
    # assert is_valid_network(G, T)
    score = average_pairwise_distance(T)
    print("Average  pairwise distance: {}".format(score))

    scores = {}
    try:
        scoresFile = open('scores.obj', 'rb')
    except:
        pickle.dump(scores, open('scores.obj', 'wb'))
    scores = pickle.load(open('scores.obj', 'rb'))

    if name not in scores or score < scores[name]:
        scores[name] = score
    if score == scores[name]:
        print("Found better solution!")
        output_path = str(pathlib.Path().absolute()) + "/outputs/" + name + '.out'
        output_path = output_path.replace("\\inputs", "")
        write_output_file(T, output_path)
    else:
        print("Old solution (" + str(scores[name]) + ") was better!")
    pickle.dump(scores, open('scores.obj', 'wb'))

if __name__ == '__main__':
    assert len(sys.argv) == 2
    sys.exit(main(sys.argv[1]))