from graph_tool.all import *
import matplotlib.pyplot as ppt
import random


def setSbsNetworkProperties(substrateNetwork):
    # Creating Properties for the Substrate Network
    # ---------------------------------------------

    graphProp = substrateNetwork.new_graph_property("string")
    substrateNetwork.gp.graphName = graphProp

    # Giving the Substrate Vertices a Resource Capacity Property
    resourceCapacityProp = substrateNetwork.new_vertex_property("int")
    substrateNetwork.vertex_properties.resourceCapacity = resourceCapacityProp

    # Giving the Substrate Vertices a Resource Property
    resourceProp = substrateNetwork.new_vertex_property("int")
    substrateNetwork.vertex_properties.resources = resourceProp

    # Giving the Substrate Vertices a Bandwidth Property
    capacityProp = substrateNetwork.new_edge_property("int")
    substrateNetwork.edge_properties.bandwidth = capacityProp

    # Giving the Substrate Vertices a Resource Capacity Property
    binaryMappingVar = substrateNetwork.new_vertex_property("int")
    substrateNetwork.vertex_properties.binaryMappingVar = binaryMappingVar


# def createSbsTowers(substrateNetwork, numSubsNodes, sbsTowers):

#     # Creating the Substrate Network Towers

#     for idx in range(numSubsNodes):
#         sbsVertex = substrateNetwork.add_vertex()
#         sbsTowers.append(sbsVertex)


def setSbsTowerProperties(substrateNetwork, numSubsNodes, sbsTowers, resCapList):

    loopIter = 0

    # Setting up Graph Property
    substrateNetwork.gp.graphName = "Substrate"

    # Setting up Vertex Properties

    for sbsTower in substrateNetwork.vertices():
        substrateNetwork.vp.resourceCapacity[sbsTower] = resCapList[loopIter]
        substrateNetwork.vp.resources[sbsTower] = -1
        substrateNetwork.vp.binaryMappingVar[sbsTower] = -1
    
    # Setting up Edge Properties

    for sbsEdges in substrateNetwork.edges():
        substrateNetwork.edge_properties.bandwidth[sbsEdges] = 5
    


    # for idx in range(numSubsNodes):
    # # Setting the resource capacity for the Network Towers

    # for idx in range(numSubsNodes):
    #     substrateNetwork.vertex_properties.resourceCapacity[sbsTowers[idx]] = resCapList[idx]

    # # Setting the resource value for the Network Towers

    # for idx in range(numSubsNodes):
    #     substrateNetwork.vertex_properties.resources[sbsTowers[idx]] = -1

    # # Setting the Binary Mapping Variable for the Network Towers

    # for idx in range(numSubsNodes):
    #     substrateNetwork.vertex_properties.binaryMappingVar[sbsTowers[idx]] = -1


# def createSbsTowerConnections(substrateNetwork, numSubsNodes, sbsTowerEdges):

#     # for sbs_connection in sbsTowerConnectionList:
#     #   sbsEdge = substrateNetwork.add_edge(sbs_connection[0], sbs_connection[1])
#     #   sbsTowerEdges.append(sbsEdge)

#     # # Setting the Bandwidth Property on the Connections between the RAN Slices
#     # # !! Hard Coded Value Included within this Loop !!

#     maxEdges = (numSubsNodes * (numSubsNodes - 1)) / 2
#     minEdges = numSubsNodes - 1

#     # randomEdges = random.randint(minEdges, maxEdges)
#     randomEdges = maxEdges
#     counterVar = 0

#     for vertex in substrateNetwork.vertices():
#         randomNode = random.choice(list(substrateNetwork.vertices()))

#         while vertex == randomNode or vertex in randomNode.all_neighbors():
#             randomNode = random.choice(list(substrateNetwork.vertices()))

#         sbsEdge = substrateNetwork.add_edge(vertex, randomNode)
#         sbsTowerEdges.append(sbsEdge)

#         counterVar += 1

#         if counterVar == minEdges:
#             break

#     if minEdges != randomEdges:

#         counter = minEdges

#         while counter < randomEdges:
#             nodeOne = random.choice(list(substrateNetwork.vertices()))
#             nodeTwo = random.choice(list(substrateNetwork.vertices()))

#             if nodeOne != nodeTwo:
#                 if nodeOne in nodeTwo.all_neighbors():
#                     continue
#                 else:
#                     sbsEdge = substrateNetwork.add_edge(nodeOne, nodeTwo)
#                     sbsTowerEdges.append(sbsEdge)
#                     counter += 1
                    
#     for edgeConnection in sbsTowerEdges:
#         substrateNetwork.edge_properties.bandwidth[edgeConnection] = 5

#     return randomEdges
