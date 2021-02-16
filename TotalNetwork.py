import Substrate as sbs
import RAN_Slice as ran
import AlgorithmOne as algoOne
import AlgorithmTwo as algoTwo
import AlgorithmThree as algoThree
from graph_tool.all import *
import random

# Substrate Global Variables
numSubsNodes = 50
resCapList = []

# RAN Global Variables
ranSlices = []
resList = []
numRnSlices = 1 
numVnfFunctions = 100
vnfCncList = []
vnfTotalAccList = []

def randomDegreeSbs():
    return random.randint(1, numSubsNodes - 1)

def randomDegreeVnf():
    return random.randint(1, numVnfFunctions - 1)

# Setting up the Substrate Network

def createSbsNetwork():
    # substrateNetwork = random_graph(numSubsNodes, randomDegreeSbs, directed=False, parallel_edges=False, self_loops=False, random=True)
    # substrateNetwork = complete_graph(numSubsNodes, self_loops=False, directed=False)
    substrateNetwork = circular_graph(numSubsNodes, self_loops=False, directed=False)

    for idx in range(numSubsNodes):
        resCapList.append(4)

    sbs.setSbsNetworkProperties(substrateNetwork)
    sbs.setSbsTowerProperties(substrateNetwork, resCapList)
    graph_draw(substrateNetwork, output="sbs.png", vertex_text = substrateNetwork.vp.get("resourceCapacity"))

# Setting up the RAN Slice

def createRANSlice():

    # for loopIter in range(numRnSlices):
    # ranSlices.append(random_graph(numVnfFunctions, randomDegreeVnf, directed=False, parallel_edges=False, self_loops=False, random=True))

    for loopIter in range(numRnSlices):
        ranSlices.append(circular_graph(numVnfFunctions, self_loops=False, directed=False))

    for idx in range(numVnfFunctions):
        resList.append(2)

    ran.setRANSliceProperties(ranSlices)
    ran.setVNFFunctionProperties(ranSlices, resList)

    # Populating VNF Cnc List
    ranSlice = find_vertex(totalNetwork, totalNetwork.vp.graphName, "RAN1")

    for vnfFunction in ranSlice:
        vnfCncList.append(totalNetwork.vp.degree[vnfFunction])

    # Populating Total Acc VNF List
    for vnfFunction in ranSlice:
        vnfTotalAccList.append(totalNetwork.vp.totalResoucesAcc[vnfFunction])

    graph_draw(ranSlices[0], output="ran.png")

def createTotalNetwork() :
    # Creating the Total Network
    totalNetwork = Graph(directed=False)
    totalNetwork = graph_union(totalNetwork, substrateNetwork, include = True, internal_props=True)
    totalNetwork = graph_union(totalNetwork, ranSlices[0], include = True, internal_props=True)
    # Testing the Created Network
    graph_draw(totalNetwork, vertex_text = totalNetwork.vertex_properties.get("resources"), output="test_total_one.png", output_size= (1920, 1080))

def resetNetwork():

    eraseMappedEdges = find_edge(totalNetwork, totalNetwork.ep.bandwidth, 0)
    # Removing all the mapped Edges
    for mappedEdge in eraseMappedEdges:
        totalNetwork.remove_edge(mappedEdge)

    # Resetting the connections
    totalNetwork = Graph(directed=False)
    totalNetwork = graph_union(totalNetwork, substrateNetwork, include = True, internal_props=True)
    totalNetwork = graph_union(totalNetwork, ranSlices[0], include = True, internal_props=True)

def algoOneTest():
    
    # Testing Algorithm One 
    maxGreedyMapping = algoOne.algorithmOne(totalNetwork, resList, resCapList, True)
    graph_draw(totalNetwork, vertex_text = totalNetwork.vertex_properties.get("resourceCapacity"), output="algo_one_sbs.png", inline_scale=10)
    graph_draw(totalNetwork, vertex_text = totalNetwork.vertex_properties.get("resources"), output="algo_one_vnf.png", inline_scale=10)

    resetNetwork()

    # Trying with min to see a difference
    minGreedyMapping = algoOne.algorithmOne(totalNetwork, resList, resCapList, False)
    graph_draw(totalNetwork, vertex_text = totalNetwork.vertex_properties.get("resourceCapacity"), output="algo_one.two_sbs.png", inline_scale=10)
    graph_draw(totalNetwork, vertex_text = totalNetwork.vertex_properties.get("resources"), output="algo_one.two_vnf.png", inline_scale=10)

    # Outputting the values for the Algorithm
    print("Algo One Mapping considering max. resources" + str(maxGreedyMapping))
    print("Algo One Mapping considering min. resources" + str(minGreedyMapping))

    resetNetwork()

#   ALgorithm Two

def algoTwoTest():

    neighborhoodMapping = algoTwo.algorithmTwo(totalNetwork, vnfCncList)
    graph_draw(totalNetwork, vertex_text = totalNetwork.vertex_properties.get("resourceCapacity"), output="algo_two_sbs.png", inline_scale=10)
    graph_draw(totalNetwork, vertex_text = totalNetwork.vertex_properties.get("resources"), output="algo_two_vnf.png", inline_scale=10)
    print("Algo Two Mapping - " + str(neighborhoodMapping))

    resetNetwork()

# Algorithm Three

def algoThreeTest():
    neighborhoodMappingTwo = algoThree.algorithmThree(totalNetwork, vnfTotalAccList)
    graph_draw(totalNetwork, vertex_text = totalNetwork.vertex_properties.get("resourceCapacity"), output="algo_three_sbs.png", inline_scale=10)
    graph_draw(totalNetwork, vertex_text = totalNetwork.vertex_properties.get("resources"), output="algo_three_vnf.png", inline_scale=10)
    print("Algo Three Mapping - " + str(neighborhoodMappingTwo))

    resetNetwork()