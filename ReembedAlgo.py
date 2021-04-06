import multiprocessing
from graph_tool.all import *
import random
import TotalNetwork as totNet
import AlgorithmOne as embedAlgoOne
import AlgorithmTwo as embedAlgoTwo

# Remapping can go two ways
# (1) Able to Remap to a Spot
# (2) Needs to move someone else to get remapped.

# In order to create a Failure Event we must randomly choose a Substrate Tower and Remove it 
def createFailureEvent(totalNetwork):

    failedSet = []
    substrateNetworkNodes = find_vertex(totalNetwork, totalNetwork.vp.graphName, "Substrate")

    # Picking only the Substrates which are embedded to a VNF
    while True:
        failedSubstrateNode = random.choice(substrateNetworkNodes)
        
        isVnfEmbedded = False

        for neighborNode in failedSubstrateNode.all_neighbors():
            if totalNetwork.vp.binaryMappingVar[neighborNode] == 1:
                isVnfEmbedded = True

        if isVnfEmbedded:
            break
        else:
            continue

    failedVnfSet = []

    # Resetting the binaryMappingVar of the connected VNF Functions and total resources acc of the neighbor substrate node.
    for neighborNode in failedSubstrateNode.all_neighbors():
        if totalNetwork.vp.binaryMappingVar[neighborNode] == 1:
            totalNetwork.vp.binaryMappingVar[neighborNode] = 0 # Representing a Failed State
            failedVnfSet.append(neighborNode)
        else:
            totalNetwork.vp.totalResourcesAcc[neighborNode]-= totalNetwork.vp.resourceCapacity[failedSubstrateNode]

    failedSet.append(failedVnfSet)
    failedSet.append(failedSubstrateNode.all_neighbors())

    # Removing the Substrate Node
    totalNetwork.remove_vertex(failedSubstrateNode)

    return failedSet;

def getMappedNeighbors(vertex, totalNetwork):

    mappedNeighbors = []
    
    for neighborNode in vertex.all_neighbors():
        if totalNetwork.vp.binaryMappingVar[neighborNode] == 1:
            mappedNeighbors.append(neighborNode)
        else:
            continue

    return mappedNeighbors;

def getResourceList(totalNetwork, nodeList = [], layer = "ALL"):

    resourceList = []

    if layer != "RAN":
        for graphNode in nodeList:
            resourceList.append(totalNetwork.vp.resourceCapacity[graphNode])

    if layer != "SUBSTRATE":
        for graphNode in nodeList:
            resourceList.append(totalNetwork.vp.resources[graphNode])
    
    return resourceList;


def algorithmOne(totalNetwork):

    failedSet = createFailureEvent(totalNetwork) # Creating a Failure Event and getting the list of failed vnf
    failedVnfSet = failedSet[0]
    failedSbsNeighbors = failedSet[1]
    substrateNetworkNodes = find_vertex(totalNetwork, totalNetwork.vp.graphName, "Substrate") 

    graph_draw(totalNetwork, output="Graph-Figures/failure-algo-one.png", vertex_text = totalNetwork.vp.get("resourceCapacity"))

    resourceList = getResourceList(totalNetwork, failedVnfSet, layer = "RAN")
    resourceCapList = getResourceList(totalNetwork, substrateNetworkNodes, layer="SUBSTRATE")

    # Run Algo One On the Failed Network to Check Which can be Re-embeded without Remapping
    remapCount = embedAlgoOne.algorithmOne(totalNetwork, resourceList, resourceCapList, False)

    print("The Total VNF Failed is equal to -> " + str(len(failedVnfSet)))

    # Check which ones failed the rembedding process i.e. require to push other VNF around in order to embed.

    unembeddedVnf = find_vertex(totalNetwork, totalNetwork.vp.binaryMappingVar, 2) # Getting all the failed VNF




    return remapCount;


    # for failedVnf in failedVnfSet:

    #     mappableSbsNodes = [] # Represents the mappable Substrate after satisfied constraint conditions

    #     # Checking for the Resource Property

    #     for neighborSbsNode in failedSbsNeighbors:
    #         if totalNetwork.vp.resources[failedVnf] <= totalNetwork.vp.resourceCapacity[neighborSbsNode]:
    #             mappableSbsNodes.append(neighborSbsNode)

    #     failedVnfMappedNeighbors = getMappedNeighbors(failedVnf)

    #     if not failedVnfMappedNeighbors:

# Testing Module Code Goes Here --

resCapList = []
resList = []
vnfCncList = []
vnfTotalAccList = []

sbsNet = totNet.createSbsNetwork(numSubsNodes = 10, resCapList = resCapList, connectivity=1)
ranSlice = totNet.createRANSlice(numVnfFunctions = 10, resList=resList)

totalNetwork = totNet.createTotalNetwork(sbsNet, ranSlice, vnfCncList, vnfTotalAccList)

totNet.algoOneTest(totalNetwork, sbsNet, ranSlice, resList, resCapList)


remapCount = algorithmOne(totalNetwork)

print("The Succesfully Reembedded VNF Count is given as -> " + str(remapCount))


                    





