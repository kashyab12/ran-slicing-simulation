import networkx as nx
import matplotlib.pyplot as pypt
import random
import math

#---------------------------------------- Creating a substrate network -------------------------------------------------
subsOne = nx.Graph()
substrateUpperBound = random.randint(5,15)

#Create Random Nummber of Substrate Nodes
loopCtr = 2
for loopCtr in range(1, substrateUpperBound + 1):
    subsOne.add_node(loopCtr, resources = random.randint(4, 10))

totalConnections = 0

for i in range(1, substrateUpperBound):
    totalConnections += i

substrateEdgeConnection = random.randint(1, totalConnections)

while(subsOne.number_of_edges() <= substrateEdgeConnection):

    tempGraphOne = random.randint(1, substrateUpperBound)
    tempGraphTwo = random.randint(1, substrateUpperBound)

    if tempGraphOne != tempGraphTwo and subsOne.has_edge(tempGraphOne, tempGraphTwo) == 0:
        subsOne.add_edge(tempGraphOne, tempGraphTwo, weight = random.randint(5, 30))
    # if tempGraphOne != tempGraphTwo and subsOne.has_edge(tempGraphOne, tempGraphTwo)==0:

#---------------------------------------- Creating n number of RAN Slices -------------------------------------------------

ranSlices = []

for ctr in range(1, randint())



layout = nx.circular_layout(subsOne)
nx.draw(subsOne, with_labels = 1)
nx.draw_networkx_edge_labels(subsOne, layout)
pypt.show()