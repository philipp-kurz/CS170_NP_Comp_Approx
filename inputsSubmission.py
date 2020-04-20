import networkx as nx
import parse as p
from random import random, choice

G = nx.Graph()
path = "inputsSubmission/"
inputs = {"25.in": 25, "50.in": 50, "100.in": 100}

for filename, size in inputs.items():
    G.add_nodes_from(range(size))
    while not nx.is_connected(G):
        start = choice(list(G.nodes()))
        end = choice(list(nx.non_neighbors(G, start)))
        weight = round(random() * 100, 3)
        G.add_edge(start, end)
        G[start][end]['weight'] = weight
    print("=== " + filename + " ===")
    print("Graph has " + str(len(list(G.nodes()))) + " nodes and " + str(len(list(G.edges()))) + " edges.")
    print("Graph is connected: " + str(nx.is_connected(G)))
    print("Write to file: " + path + filename)
    p.write_input_file(G, path + filename)
    G.clear()
    print()





