import networkx as nx
import matplotlib.pyplot as plt
import sys
import pathlib
from parse import read_input_file

input_name = sys.argv[1]
path = str(pathlib.Path().absolute()) + "/inputs/" + input_name + '.in'
G = read_input_file(path)
nx.draw(G, pos=nx.spring_layout(G))
nx.draw_networkx_labels(G, pos=nx.spring_layout(G))
# nx.draw_networkx_edge_labels(G, pos=nx.spring_layout(G))
plt.savefig("filename.png")
