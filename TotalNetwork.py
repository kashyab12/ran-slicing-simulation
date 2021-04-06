import Substrate as sbs
import RAN_Slice as ran
import AlgorithmOne as algoOne
import AlgorithmTwo as algoTwo
import AlgorithmThree as algoThree
import AlgorithmFour as algoFour
from graph_tool.all import *
import random

# Substrate Global Variables
numSubsNodes = 25
resCapList = []
resCtPerSbs = 4
substrateNetwork = 0

# RAN Global Variables
ranSlices = 0
resList = []
numRnSlices = 1
numVnfFunctions = 60
resCtPerVnf = 2
vnfCncList = []
vnfTotalAccList = []

# Other Global
totalNetwork = 0

def createSbsNetwork(numSubsNodes= 10, resCapList = [], resCtPerSbs=4, connectivity=2): # Default Parameters
    # substrateNetwork = random_graph(numSubsNodes, randomDegreeSbs, directed=False, parallel_edges=False, self_loops=False, random=True)
    # substrateNetwork = complete_graph(numSubsNodes, self_loops=False, directed=False)
    substrateNetwork = circular_graph(numSubsNodes, k= connectivity, self_loops=False, directed=False)

    for idx in range(numSubsNodes):
        resCapList.append(random.randint(resCtPerSbs, resCtPerSbs+2)) #+2

    sbs.setSbsNetworkProperties(substrateNetwork)
    sbs.setSbsTowerProperties(substrateNetwork, resCapList)
    graph_draw(substrateNetwork, output="Graph-Figures/sbs.png", vertex_text = substrateNetwork.vp.get("resourceCapacity"))
    
    return substrateNetwork;

# Setting up the RAN Slice

def createRANSlice(numRnSlices = 1, numVnfFunctions = 10, resList = [], resCtPerVnf = 2, connectivity = 2):

    # for loopIter in range(numRnSlices):
    # ranSlices.append(random_graph(numVnfFunctions, randomDegreeVnf, directed=False, parallel_edges=False, self_loops=False, random=True))

    ranSlices = Graph(directed=False)
    networkSlices = []

    numVnfFunctions *= numRnSlices

    for loopIter in range(numRnSlices):

        ranSlice = circular_graph(numVnfFunctions, k= connectivity, self_loops=False, directed=False)

        for idx in range(numVnfFunctions):
            resList.append(random.randint(resCtPerVnf, resCtPerVnf+2)) # +2

        ran.setRANSliceProperties(ranSlice)
        ran.setVNFFunctionProperties(ranSlice, resList, loopIter)
        networkSlices.append(ranSlice)

    for slices in networkSlices:
        graph_union(ranSlices, slices, include = True, internal_props=True)


    graph_draw(ranSlices, output="Graph-Figures/ran.png")
    
    return ranSlices;

def createTotalNetwork(substrateNetwork, ranSlices,  vnfCncList = [], vnfTotalAccList = []) :
    # Creating the Total Network
    totalNetwork = Graph(directed=False)
    totalNetwork = graph_union(totalNetwork, substrateNetwork, include = True, internal_props=True)
    totalNetwork = graph_union(totalNetwork, ranSlices, include = True, internal_props=True)

    # Testing the Created Network
    graph_draw(totalNetwork, vertex_text = totalNetwork.vertex_properties.get("resources"), output="Graph-Figures/test_total_one.png", output_size= (1920, 1080))

    vnfCncList = getUpdatedCncList(totalNetwork)
    vnfTotalAccList = getUpdatedResourcesAcc(totalNetwork)
        
    return totalNetwork;


# Can only find if the 

def getUpdatedResourcesAcc(totalNetwork, layer = "RAN"):

    resAccList = []

    if layer == "RAN":

        vnfList = getLayerList(totalNetwork)

        # updating the total resources Acc

        for node in vnfList:
            resAcc = totalNetwork.vp.resources[node]
                
            for neighborNode in node.all_neighbors():
                if totalNetwork.vp.binaryMappingVar[neighborNode] >= 0:
                    resAcc += totalNetwork.vp.resources[neighborNode]
                
            totalNetwork.vp.totalResourcesAcc[node] = resAcc
            resAccList.append(resAcc)

        
    elif layer == "Substrate": # Substrate Towers

        sbsList = getLayerList(totalNetwork, layer = "Substrate")

        # Updating Total Resources for Sbs

        for node in sbsList:
            resAcc = totalNetwork.vp.resourceCapacity[node]
                
            for neighborNode in node.all_neighbors():
                if totalNetwork.vp.binaryMappingVar[neighborNode] < 0:
                    resAcc += totalNetwork.vp.resourceCapacity[neighborNode]
                
            totalNetwork.vp.totalResourcesAcc[node] = resAcc
            resAccList.append(resAcc)
    else:
        print("Wrong Layer name entered for the getUpdatesResourcesAcc Function")

    return resAccList;


def resetNetwork(totalNetwork, substrateNetwork, ranSlices):

    eraseMappedEdges = find_edge(totalNetwork, totalNetwork.ep.bandwidth, 0)
    # Removing all the mapped Edges
    for mappedEdge in eraseMappedEdges:
        totalNetwork.remove_edge(mappedEdge)

    # Resetting the connections
    totalNetwork = Graph(directed=False)
    totalNetwork = graph_union(totalNetwork, substrateNetwork, include = True, internal_props=True)
    totalNetwork = graph_union(totalNetwork, ranSlices, include = True, internal_props=True)

def algoOneTest(totalNetwork, substrateNetwork, ranSlices = 1, resList = [], resCapList = []):

    resList = getUpdatedResList(totalNetwork)
    resCapList = getUpdatedResList(totalNetwork, layer = "Substrate")
    
    # Testing Algorithm One 
    maxGreedyMapping = algoOne.algorithmOne(totalNetwork, resList, resCapList, True)
    graph_draw(totalNetwork, vertex_text = totalNetwork.vertex_properties.get("resourceCapacity"), output="Graph-Figures/algo_one_sbs.png", inline_scale=10)
    graph_draw(totalNetwork, vertex_text = totalNetwork.vertex_properties.get("resources"), output="Graph-Figures/algo_one_vnf.png", inline_scale=10)
    
    # Outputting the values for the Algorithm
    print("Algo One Embeddings -  " + str(maxGreedyMapping))

    return maxGreedyMapping;


def getUpdatedResList(totalNetwork, layer = "RAN"):

    resList = []

    if layer == "RAN":

        vnfList = getLayerList(totalNetwork)

        for vnf in vnfList:
            resList.append(totalNetwork.vp.resources[vnf])

    elif layer == "Substrate":  # Substrate Layer
        sbsList = getLayerList(totalNetwork, layer = "Substrate")

        for sbs in sbsList:
            resList.append(totalNetwork.vp.resourceCapacity[sbs])
    
    else:
        print("Wrong layer name enteredfor the getUpdatedResList function")

    return resList;

# Algorithm Two
def algoTwoTest(totalNetwork, vnfCncList = []):

    vnfCncList = getUpdatedCncList(totalNetwork)

    neighborhoodMapping = algoTwo.algorithmTwo(totalNetwork, vnfCncList)
    graph_draw(totalNetwork, vertex_text = totalNetwork.vertex_properties.get("resourceCapacity"), output="Graph-Figures/algo_two_sbs.png", inline_scale=10)
    graph_draw(totalNetwork, vertex_text = totalNetwork.vertex_properties.get("resources"), output="Graph-Figures/algo_two_vnf.png", inline_scale=10)
    print("Algo Two Mapping - " + str(neighborhoodMapping))
    
    return neighborhoodMapping;

def getLayerList(totalNetwork, layer ="RAN"):

    layerList = []

    if layer == "RAN":

        for node in totalNetwork.vertices():
            if totalNetwork.binaryMappingVar[node] >= 0:
                layerList.append(node)

    elif layer == "Substrate":

        for node in totalNetwork.vertices():
            if totalNetwork.binaryMappingVar[node] < 0:
                layerList.append(node)

    else:
        print("Wrong Layer Name Entered for the getLayer Function")

    return layerList;


def getUpdatedCncList(totalNetwork, layer = "RAN"):

    cncList = []

    if layer == 'RAN':
        vnfList = getLayerList(totalNetwork)

        # Updating the Degree

        for node in vnfList:
            vnfNeighborCount = 0

            for neighborNode in node.all_neighbors():
                if totalNetwork.vp.binaryMappingVar[neighborNode] >= 0:
                    vnfNeighborCount += 1

            totalNetwork.vp.degree[node] = vnfNeighborCount
            cncList.append(vnfNeighborCount)

    elif layer == "Substrate":

        sbsList = getLayerList(totalNetwork, layer = "Substrate")

        for node in sbsList:
            sbsNeighborCount = 0

            for neighborNode in node.all_neighbors():
                if totalNetwork.vp.binaryMappingVar[neighborNode] < 0:
                    sbsNeighborCount += 1
            
            totalNetwork.vp.degree[node] = sbsNeighborCount
            cncList.append(sbsNeighborCount)
    
    else:
        print("Wrong Layer Name Given for the getUpdatedCncList function")

    return cncList;

# Algorithm Three

def algoThreeTest(totalNetwork, vnfTotalAccList = []):

    vnfTotalAccList = getUpdatedResourcesAcc(totalNetwork)

    neighborhoodMappingTwo = algoThree.algorithmThree(totalNetwork, vnfTotalAccList)
    graph_draw(totalNetwork, vertex_text = totalNetwork.vertex_properties.get("resourceCapacity"), output="Graph-Figures/algo_three_sbs.png", inline_scale=10)
    graph_draw(totalNetwork, vertex_text = totalNetwork.vertex_properties.get("resources"), output="Graph-Figures/algo_three_vnf.png", inline_scale=10)
    print("Algo Three Mapping - " + str(neighborhoodMappingTwo))
    
    return neighborhoodMappingTwo;

def algoFourTest(totalNetwork, substrateNetwork, ranSlices = 1, resCapList = [], vnfCncList = []):

    resCapList = getResList(totalNetwork, layer = "substrate")
    vnfCncList = getUpdatedCncList(totalNetwork)
    
    # Testing Algorithm One 
    maxGreedyMapping = algoFour.algorithmFour(totalNetwork, resCapList, vnfCncList, True)
    graph_draw(totalNetwork, vertex_text = totalNetwork.vertex_properties.get("resourceCapacity"), output="Graph-Figures/algo_one_sbs.png", inline_scale=10)
    graph_draw(totalNetwork, vertex_text = totalNetwork.vertex_properties.get("resources"), output="Graph-Figures/algo_one_vnf.png", inline_scale=10)
    
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
