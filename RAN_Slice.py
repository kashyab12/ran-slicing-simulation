# Import Statements
from graph_tool.all import *
import math
import random
from matplotlib import pyplot as plt
import TotalNetwork as tn

# Function defined to create an RAN Slice

def setRANSliceProperties(ranSlices):

    # Creating Properties for the RAN Slices
    # --------------------------------------

    graphProp = ranSlices.new_vertex_property("string")
    ranSlices.vp.graphName = graphProp

    # Giving the VNF Functions a Resource Capacity Property
    resourceCapacityProp = ranSlices.new_vertex_property("int")
    ranSlices.vertex_properties.resourceCapacity = resourceCapacityProp

    # Giving the VNF Functions a Resource Property
    resourceProp = ranSlices.new_vertex_property("int")
    ranSlices.vertex_properties.resources = resourceProp

    # Giving the VNF Functions a Bandwidth Property
    capacityProp = ranSlices.new_edge_property("int")
    ranSlices.edge_properties.bandwidth = capacityProp

    # Giving the Substrate Vertices a Resource Capacity Property
    binaryMappingVar = ranSlices.new_vertex_property("int")
    ranSlices.vertex_properties.binaryMappingVar = binaryMappingVar

    totalResource = ranSlices.new_vertex_property("int")
    ranSlices.vertex_properties.totalResourcesAcc = totalResource

    vertexDegree = ranSlices.new_vertex_property("int")
    ranSlices.vertex_properties.degree = vertexDegree


# Function to Set the Properties for the VNF Functions
def setVNFFunctionProperties(ranSlices, resList, sliceNumber = 1, vnfList = [], band = 2):

    loopIter = 0

    if vnfList:
        # Setting up the Vertex Properties
        for vnfFunction in vnfList:
            ranSlices.vp.graphName[vnfFunction] = "RAN" + str(sliceNumber)
            ranSlices.vertex_properties.resourceCapacity[vnfFunction] = -1   
            ranSlices.vertex_properties.resources[vnfFunction] = tn.resCtPerVnf + tn.randUpBoundVnf
            ranSlices.vertex_properties.binaryMappingVar[vnfFunction] = 0
            ranSlices.vertex_properties.degree[vnfFunction] = len(ranSlices.get_all_neighbors(vnfFunction))
            loopIter += 1
        
        # Setting up the totalResources per vertex
        for vnfFunction in vnfList:
            resAcc = ranSlices.vp.resources[vnfFunction]
                
            for vnfFunctionNeighbor in vnfFunction.all_neighbors():
                resAcc += ranSlices.vp.resources[vnfFunctionNeighbor]
                
            ranSlices.vp.totalResourcesAcc[vnfFunction] = resAcc
        
        new_edges = find_edge(ranSlices, ranSlices.ep.bandwidth, 0)

        # Setting uy the Edge Properties
        for vnfEdge in new_edges:
            if ranSlices.vp.binaryMappingVar[vnfEdge.source()] != 1 and ranSlices.vp.binaryMappingVar[vnfEdge.target()] != 1:
                ranSlices.edge_properties.bandwidth[vnfEdge] = band

    else:
        # Setting up the Vertex Properties
        for vnfFunction in ranSlices.vertices():
            ranSlices.vp.graphName[vnfFunction] = "RAN" + str(sliceNumber)
            ranSlices.vertex_properties.resourceCapacity[vnfFunction] = -1   
            ranSlices.vertex_properties.resources[vnfFunction] = resList[loopIter]
            ranSlices.vertex_properties.binaryMappingVar[vnfFunction] = 0
            ranSlices.vertex_properties.degree[vnfFunction] = len(ranSlices.get_all_neighbors(vnfFunction))
            loopIter += 1
        
        # Setting up the totalResources per vertex
        for vnfFunction in ranSlices.vertices():
            resAcc = ranSlices.vp.resources[vnfFunction]
                
            for vnfFunctionNeighbor in vnfFunction.all_neighbors():
                resAcc += ranSlices.vp.resources[vnfFunctionNeighbor]
                
            ranSlices.vp.totalResourcesAcc[vnfFunction] = resAcc
        
        # Setting uy the Edge Properties
        for vnfEdge in ranSlices.edges():
            ranSlices.edge_properties.bandwidth[vnfEdge] = band