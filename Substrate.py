from graph_tool.all import *
import matplotlib.pyplot as ppt
import random
import TotalNetwork as tn

def setSbsNetworkProperties(substrateNetwork):
    # Creating Properties for the Substrate Network
    # ---------------------------------------------

    graphProp = substrateNetwork.new_vertex_property("string")
    substrateNetwork.vp.graphName = graphProp

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

    

def setSbsTowerProperties(substrateNetwork, resCapList, band = tn.sbsBandValue, sbsNodes = []):

    loopIter = 0

    if len(sbsNodes) != 0:
        for node in sbsNodes:
            substrateNetwork.vp.graphName[node] = "Substrate"
            substrateNetwork.vp.resourceCapacity[node] = tn.resCtPerSbs + tn.randUpBoundSbs
            substrateNetwork.vp.resources[node] = -1
            substrateNetwork.vp.binaryMappingVar[node] = -1
            substrateNetwork.vp.degree[node] = len(substrateNetwork.get_all_neighbors(node))
            loopIter += 1

        # Setting up the totalResources per vertex
        for node in sbsNodes:
            resAcc = substrateNetwork.vp.resourceCapacity[node]
            
            for neighborNode in node.all_neighbors():
                resAcc += substrateNetwork.vp.resourceCapacity[neighborNode]
            
            substrateNetwork.vp.totalResourcesAcc[node] = resAcc
        
        # Setting up Edge Properties

        newEdges = find_edge(substrateNetwork, substrateNetwork.ep.bandwidth, 0)

        for edges in newEdges:
            if substrateNetwork.vp.binaryMappingVar[edges.target()] == -1 and substrateNetwork.vp.binaryMappingVar[edges.source()] == -1:
                substrateNetwork.edge_properties.bandwidth[edges] = band

    else:
        # Setting up Vertex Properties

        for sbsTower in substrateNetwork.vertices():
            substrateNetwork.vp.graphName[sbsTower] = "Substrate"
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
            substrateNetwork.edge_properties.bandwidth[sbsEdges] = band

        