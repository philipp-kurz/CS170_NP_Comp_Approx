import networkx as nx
from parse import read_input_file, write_output_file
from utils import is_valid_network, average_pairwise_distance
import sys
import pathlib


# Function to sort the list by second item of tuple
def Sort_Tuple(tup, pos):
    return (sorted(tup, key=lambda x: x[pos]))

# Returns: T: networkx.Graph
def solve(G):
    H = G.copy()

    node_degree = G.degree(list(G.nodes()))
    removed = []
    rem_edge_weight_sum = 0
    if len(node_degree) > 2:
        for node in node_degree:
            if node[1] <= 1:
                H.remove_node(node[0])
                removed.append(node[0])
                rem_edge_weight_sum += list(G.edges.data(nbunch=node[0], data='weight', default=1))[0][2]
    # rem_avg = rem_edge_weight_sum / len(removed)
    edges = Sort_Tuple(list(H.edges.data(data='weight')), 2)

    edge_weight_sum = 0
    for edge in edges:
        edge_weight_sum += edge[2]
    if len(edges) > 0:
        avg = edge_weight_sum / len(edges)
    while len(edges) > 0:
        nodes = set(H.nodes())
        edge = edges.pop()
        if edge[2] < avg:
            break
        u = edge[0]
        v = edge[1]
        if u not in nodes or v not in nodes:
            continue
        choice = v if H.degree(v) > H.degree(u) else u

        neighbors = list(nx.neighbors(H, choice))
        cont = False
        for neighbor in neighbors:
            if H.degree(neighbor) == 1:
                cont = True
                break
        if cont:
            continue

        new_H = H.copy()

        new_H.remove_node(choice)
        if nx.is_connected(new_H):
            H = new_H

    T = nx.minimum_spanning_tree(H)
    # for node in removed:
    #     weight = list(G.edges.data(nbunch=node, data='weight', default=1))[0][2]
    #     if weight < avg:
    #         edge = list(G.edges(node))[0]
    #         T.add_edge(edge[0], edge[1])
    return T

# Usage: python3 solver.py test.in

def main(filename):
    print(filename, end=": ")
    input_name = filename[0:-3]
    path = str(pathlib.Path().absolute()) + "/" +  input_name + '.in'

    G = read_input_file(path)
    T = solve(G)
    # assert is_valid_network(G, T)
    print("Average  pairwise distance: {}".format(average_pairwise_distance(T)))
    write_output_file(T, str(pathlib.Path().absolute()) + "/" + input_name + '.out')

if __name__ == '__main__':
    assert len(sys.argv) == 2
    sys.exit(main(sys.argv[1]))