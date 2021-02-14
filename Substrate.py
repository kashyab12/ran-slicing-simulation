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

    totalResource = substrateNetwork.new_vertex_property("int")
    substrateNetwork.vertex_properties.totalResourcesAcc = totalResource

    vertexDegree = substrateNetwork.new_vertex_property("int")
    substrateNetwork.vertex_properties.degree = vertexDegree

    

def setSbsTowerProperties(substrateNetwork, resCapList):

    loopIter = 0

    # Setting up Graph Property
    substrateNetwork.gp.graphName = "Substrate"

    # Setting up Vertex Properties

    for sbsTower in substrateNetwork.vertices():
        substrateNetwork.vp.resourceCapacity[sbsTower] = resCapList[loopIter]
        substrateNetwork.vp.resources[sbsTower] = -1
        substrateNetwork.vp.binaryMappingVar[sbsTower] = -1
        substrateNetwork.vp.degree[sbsTower] = len(substrateNetwork.get_all_neighbors(sbsTower))
        loopIter += 1

    # Setting up the totalResources per vertex
    for sbsTower in substrateNetwork.vertices():
        resAcc = substrateNetwork.vp.resourceCapacity[sbsTower]
        
        for sbsTowerNeighbor in sbsTower.all_neighbors():
            resAcc += substrateNetwork.vp.resourceCapacity[sbsTowerNeighbor]
        
        substrateNetwork.vp.totalResourcesAcc[sbsTower] = resAcc
    
    # Setting up Edge Properties

    for sbsEdges in substrateNetwork.edges():
        substrateNetwork.edge_properties.bandwidth[sbsEdges] = 5

        