import networkx as nx
import matplotlib.pyplot as ppt

G = nx.complete_graph(20)

nx.draw(G)
ppt.show()