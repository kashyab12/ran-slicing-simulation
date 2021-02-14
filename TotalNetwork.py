import Substrate as sbs
import RAN_Slice as ran
import Algorithms as algo
import random
from graph_tool.all import *

# Substrate Global Variables
numSubsNodes = 50
resCapList = []

# RAN Global Variables
ranSlices = []
resList = []
numRnSlices = 1 
numVnfFunctions = 20
vnfCncList = []

def randomDegreeSbs():
    return random.randint(1, numSubsNodes - 1)

def randomDegreeVnf():
    return random.randint(1, numVnfFunctions - 1)

# Setting up the Substrate Network

substrateNetwork = random_graph(numSubsNodes, randomDegreeSbs, directed=False, parallel_edges=False, self_loops=False, random=True)

for idx in range(numSubsNodes):
    resCapList.append(5)

sbs.setSbsNetworkProperties(substrateNetwork)
sbs.setSbsTowerProperties(substrateNetwork, resCapList)
graph_draw(substrateNetwork, output="sbs.png", vertex_text = substrateNetwork.vp.get("resourceCapacity"))

# Setting up the RAN Slice

for loopIter in range(numRnSlices):
    ranSlices.append(random_graph(numVnfFunctions, randomDegreeVnf, directed=False, parallel_edges=False, self_loops=False, random=True))

for idx in range(numVnfFunctions):
    resList.append(random.randint(2, 4))

ran.setRANSliceProperties(ranSlices)
ran.setVNFFunctionProperties(ranSlices, resList)

graph_draw(ranSlices[0], output="ran.png")

# # Creating the Total Network
totalNetwork = Graph(directed=False)
totalNetwork = graph_union(totalNetwork, substrateNetwork, include = True, internal_props=True)
totalNetwork = graph_union(totalNetwork, ranSlices[0], include = True, internal_props=True)

# # Testing the Created Network
graph_draw(totalNetwork, vertex_text = totalNetwork.vertex_properties.get("resources"), output="test_total_one.png", output_size= (1920, 1080))

# Testing Algorithm One (Max and Min) 
maxGreedyMapping = algo.algorithmOne(totalNetwork, resList, resCapList, True)
graph_draw(totalNetwork, vertex_text = totalNetwork.vertex_properties.get("resourceCapacity"), output="algo_one_max.png", inline_scale=10)
graph_draw(totalNetwork, vertex_text = totalNetwork.vertex_properties.get("resources"), output="algo_one_two_max.png", inline_scale=10)

eraseMappedEdges = find_edge(totalNetwork, totalNetwork.ep.bandwidth, 0)

# Removing all the mapped Edges
for mappedEdge in eraseMappedEdges:
    totalNetwork.remove_edge(mappedEdge)

# Resetting the connections
totalNetwork = Graph(directed=False)
totalNetwork = graph_union(totalNetwork, substrateNetwork, include = True, internal_props=True)
totalNetwork = graph_union(totalNetwork, ranSlices[0], include = True, internal_props=True)

# Trying with min to see a difference
minGreedyMapping = algo.algorithmOne(totalNetwork, resList, resCapList, False)
graph_draw(totalNetwork, vertex_text = totalNetwork.vertex_properties.get("resourceCapacity"), output="algo_one_min.png", inline_scale=10)
graph_draw(totalNetwork, vertex_text = totalNetwork.vertex_properties.get("resources"), output="algo_one_two_min.png", inline_scale=10)

# Outputting the values for the Algorithm
print("Algo One Mapping considering max. resources" + str(maxGreedyMapping))
print("Algo One Mapping considering min. resources" + str(minGreedyMapping))