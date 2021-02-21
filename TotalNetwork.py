import Substrate as sbs
import RAN_Slice as ran
import AlgorithmOne as algoOne
import AlgorithmTwo as algoTwo
import AlgorithmThree as algoThree
import AlgorithmFour as algoFour
from graph_tool.all import *
import random

# Substrate Global Variables
numSubsNodes = 100
resCapList = []
resCtPerSbs = 4
substrateNetwork = 0

# RAN Global Variables
ranSlices = 0
resList = []
numRnSlices = 1
numVnfFunctions = 200
resCtPerVnf = 2
vnfCncList = []
vnfTotalAccList = []

# Other Global
totalNetwork = 0


# def randomDegreeSbs():
#     return random.randint(1, numSubsNodes - 1)

# def randomDegreeVnf():
#     return random.randint(1, numVnfFunctions - 1)

# Setting up the Substrate Network

def createSbsNetwork(numSubsNodes, resCapList, resCtPerSbs, connectivity):
    # substrateNetwork = random_graph(numSubsNodes, randomDegreeSbs, directed=False, parallel_edges=False, self_loops=False, random=True)
    # substrateNetwork = complete_graph(numSubsNodes, self_loops=False, directed=False)
    substrateNetwork = circular_graph(numSubsNodes, k= connectivity, self_loops=False, directed=False)

    for idx in range(numSubsNodes):
        resCapList.append(random.randint(resCtPerSbs, resCtPerSbs+2))

    sbs.setSbsNetworkProperties(substrateNetwork)
    sbs.setSbsTowerProperties(substrateNetwork, resCapList)
    graph_draw(substrateNetwork, output="sbs.png", vertex_text = substrateNetwork.vp.get("resourceCapacity"))
    
    return substrateNetwork;

# Setting up the RAN Slice

def createRANSlice(numRnSlices, numVnfFunctions, resList, resCtPerVnf, connectivity):

    # for loopIter in range(numRnSlices):
    # ranSlices.append(random_graph(numVnfFunctions, randomDegreeVnf, directed=False, parallel_edges=False, self_loops=False, random=True))

    ranSlices = Graph(directed=False)
    networkSlices = []

    for loopIter in range(numRnSlices):

        ranSlice = circular_graph(numVnfFunctions, k= connectivity, self_loops=False, directed=False)

        for idx in range(numVnfFunctions):
            resList.append(random.randint(resCtPerVnf, resCtPerVnf+2))

        ran.setRANSliceProperties(ranSlice)
        ran.setVNFFunctionProperties(ranSlice, resList, loopIter)
        networkSlices.append(ranSlice)

    for slices in networkSlices:
        graph_union(ranSlices, slices, include = True, internal_props=True)

    numVnfFunctions *= numRnSlices

    graph_draw(ranSlices, output="ran.png")
    
    return ranSlices;

def createTotalNetwork(substrateNetwork, ranSlices, vnfCncList, vnfTotalAccList) :
    # Creating the Total Network
    totalNetwork = Graph(directed=False)
    totalNetwork = graph_union(totalNetwork, substrateNetwork, include = True, internal_props=True)
    totalNetwork = graph_union(totalNetwork, ranSlices, include = True, internal_props=True)
    # Testing the Created Network
    graph_draw(totalNetwork, vertex_text = totalNetwork.vertex_properties.get("resources"), output="test_total_one.png", output_size= (1920, 1080))

    # Populating VNF Cnc List
    ranSlice = find_vertex(totalNetwork, totalNetwork.vp.binaryMappingVar, 0)

    for vnfFunction in ranSlice:
        vnfCncList.append(totalNetwork.vp.degree[vnfFunction])

    # Populating Total Acc VNF List
    for vnfFunction in ranSlice:
        vnfTotalAccList.append(totalNetwork.vp.totalResourcesAcc[vnfFunction])
        
    return totalNetwork;

def resetNetwork(totalNetwork, substrateNetwork, ranSlices):

    eraseMappedEdges = find_edge(totalNetwork, totalNetwork.ep.bandwidth, 0)
    # Removing all the mapped Edges
    for mappedEdge in eraseMappedEdges:
        totalNetwork.remove_edge(mappedEdge)

    # Resetting the connections
    totalNetwork = Graph(directed=False)
    totalNetwork = graph_union(totalNetwork, substrateNetwork, include = True, internal_props=True)
    totalNetwork = graph_union(totalNetwork, ranSlices, include = True, internal_props=True)

def algoOneTest(totalNetwork, substrateNetwork, ranSlices, resList, resCapList):
    
    # Testing Algorithm One 
    maxGreedyMapping = algoOne.algorithmOne(totalNetwork, resList, resCapList, True)
    graph_draw(totalNetwork, vertex_text = totalNetwork.vertex_properties.get("resourceCapacity"), output="algo_one_sbs.png", inline_scale=10)
    graph_draw(totalNetwork, vertex_text = totalNetwork.vertex_properties.get("resources"), output="algo_one_vnf.png", inline_scale=10)
    
    # Outputting the values for the Algorithm
    print("Algo One Mapping considering max. resources: " + str(maxGreedyMapping))

    return maxGreedyMapping;


# Algorithm Two
def algoTwoTest(totalNetwork, vnfCncList):

    neighborhoodMapping = algoTwo.algorithmTwo(totalNetwork, vnfCncList)
    graph_draw(totalNetwork, vertex_text = totalNetwork.vertex_properties.get("resourceCapacity"), output="algo_two_sbs.png", inline_scale=10)
    graph_draw(totalNetwork, vertex_text = totalNetwork.vertex_properties.get("resources"), output="algo_two_vnf.png", inline_scale=10)
    print("Algo Two Mapping - " + str(neighborhoodMapping))
    
    return neighborhoodMapping;


# Algorithm Three

def algoThreeTest(totalNetwork, vnfTotalAccList):
    neighborhoodMappingTwo = algoThree.algorithmThree(totalNetwork, vnfTotalAccList)
    graph_draw(totalNetwork, vertex_text = totalNetwork.vertex_properties.get("resourceCapacity"), output="algo_three_sbs.png", inline_scale=10)
    graph_draw(totalNetwork, vertex_text = totalNetwork.vertex_properties.get("resources"), output="algo_three_vnf.png", inline_scale=10)
    print("Algo Three Mapping - " + str(neighborhoodMappingTwo))
    
    return neighborhoodMappingTwo;

def algoFourTest(totalNetwork, substrateNetwork, ranSlices, resCapList, vnfCncList):
    
    # Testing Algorithm One 
    maxGreedyMapping = algoFour.algorithmFour(totalNetwork, resCapList, vnfCncList, True)
    graph_draw(totalNetwork, vertex_text = totalNetwork.vertex_properties.get("resourceCapacity"), output="algo_one_sbs.png", inline_scale=10)
    graph_draw(totalNetwork, vertex_text = totalNetwork.vertex_properties.get("resources"), output="algo_one_vnf.png", inline_scale=10)
    
    # Outputting the values for the Algorithm
    print("Algo Four Mapping considering max. connections: " + str(maxGreedyMapping))

    return maxGreedyMapping;


def findTotalSbsMapped(totalNetwork):
    
    totalSbsMapped = 0
    
    sbsNetwork = find_vertex(totalNetwork, totalNetwork.vp.graphName, "Substrate")
    
    for sbsTower in sbsNetwork:
        for edgeConnection in sbsTower.all_edges():
            if totalNetwork.ep.bandwidth[edgeConnection] == 0:
                totalSbsMapped += 1
                break
    
    return totalSbsMapped;

def sbsAvailableRes(totalNetwork):
    
    resAvail = 0
    
    sbsNetwork = find_vertex(totalNetwork, totalNetwork.vp.graphName, "Substrate")
    
    for sbsTower in sbsNetwork:
        resAvail += totalNetwork.vp.resourceCapacity[sbsTower]
    
    return resAvail;