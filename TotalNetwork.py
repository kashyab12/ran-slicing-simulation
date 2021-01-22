import Substrate as sbs
import RAN_Slice as ran
import Algorithms as algo
import random
from graph_tool.all import *

# Substrate Global Variables
numSubsNodes = 360
sbsTowers = []
resCapList = []
sbsTowerEdges = []

# RAN Global Variables
ranSlices = []
vnfFunctions = []
resList = []
vnfEdges = []
numRnSlices = 1
numVnfFunctions = 600

def randomDegreeSbs():
    return random.randint(1, numSubsNodes - 1)

def randomDegreeVnf():
    return random.randint(1, numVnfFunctions - 1)


substrateNetwork = random_graph(numSubsNodes, randomDegreeSbs, directed=False, parallel_edges=False, self_loops=False, random=True)

for idx in range(numSubsNodes):
    resCapList.append(5)

# Setting up the Substrate Network

sbs.setSbsNetworkProperties(substrateNetwork)
# sbs.createSbsTowers(substrateNetwork, numSubsNodes, sbsTowers)
sbs.setSbsTowerProperties(substrateNetwork, numSubsNodes, sbsTowers, resCapList)
# sbs.createSbsTowerConnections(substrateNetwork,  numSubsNodes, sbsTowerEdges)

graph_draw(substrateNetwork, output="sbs.png", vertex_text = substrateNetwork.vp.get("resourceCapacity"))

for loopIter in range(numRnSlices):
    ranSlices.append(random_graph(numVnfFunctions, randomDegreeVnf, directed=False, parallel_edges=False, self_loops=False, random=True))

for idx in range(numVnfFunctions):
    resList.append(random.randint(2, 4))


# Setting up the RAN Slice
# ran.createRANSlices(ranSlices, numRnSlices)
# ran.setRANSliceProperties(ranSlices)
# ran.createVNFFunctions(ranSlices, numVnfFunctions, vnfFunctions)
# ran.setVNFFunctionProperties(ranSlices, numVnfFunctions, vnfFunctions, resList)
# ran.createVNFConnections(ranSlices, numVnfFunctions, vnfEdges)

# graph_draw(ranSlices[0], output="ran.png")

# # Creating the Total Network
# totalNetwork = Graph(directed=False)
# totalNetwork = graph_union(totalNetwork, substrateNetwork, include = True, internal_props=True)
# totalNetwork = graph_union(totalNetwork, ranSlices[0], include = True, internal_props=True)

# # Testing the Created Network
# graph_draw(totalNetwork, vertex_text = totalNetwork.vertex_properties.get("resources"), output="test_total_one.png", output_size= (1920, 1080))

# # Testing Algorithm One
# numberOfMappings = algo.algorithmOne(totalNetwork, resList, resCapList, substrateNetwork)
# graph_draw(totalNetwork, vertex_text = totalNetwork.vertex_properties.get("resourceCapacity"), output="algo_one.png", inline_scale=10)
# graph_draw(totalNetwork, vertex_text = totalNetwork.vertex_properties.get("resources"), output="algo_one_two.png", inline_scale=10)

# print(numberOfMappings)

