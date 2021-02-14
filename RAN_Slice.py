# Import Statements
from graph_tool.all import *
import math
import random
from matplotlib import pyplot as plt

# Function defined to create an RAN Slice

def setRANSliceProperties(ranSlices):

    # Creating Properties for the RAN Slices
    # --------------------------------------

    graphProp = ranSlices[0].new_graph_property("string")
    ranSlices[0].gp.graphName = graphProp

    # Giving the VNF Functions a Resource Capacity Property
    resourceCapacityProp = ranSlices[0].new_vertex_property("int")
    ranSlices[0].vertex_properties.resourceCapacity = resourceCapacityProp

    # Giving the VNF Functions a Resource Property
    resourceProp = ranSlices[0].new_vertex_property("int")
    ranSlices[0].vertex_properties.resources = resourceProp

    # Giving the VNF Functions a Bandwidth Property
    capacityProp = ranSlices[0].new_edge_property("int")
    ranSlices[0].edge_properties.bandwidth = capacityProp

    # Giving the Substrate Vertices a Resource Capacity Property
    binaryMappingVar = ranSlices[0].new_vertex_property("int")
    ranSlices[0].vertex_properties.binaryMappingVar = binaryMappingVar

    totalResource = ranSlices[0].new_vertex_property("int")
    ranSlices[0].vertex_properties.totalResourcesAcc = totalResource

    vertexDegree = ranSlices[0].new_vertex_property("int")
    ranSlices[0].vertex_properties.degree = vertexDegree


# Function to Set the Properties for the VNF Functions
def setVNFFunctionProperties(ranSlices, resList):

    loopIter = 0

    # Setting up the Graph Properties
    ranSlices[0].gp.graphName = "RAN1"
    
    # Setting up the Vertex Properties
    for vnfFunction in ranSlices[0].vertices():
        ranSlices[0].vertex_properties.resourceCapacity[vnfFunction] = -1   
        ranSlices[0].vertex_properties.resources[vnfFunction] = resList[loopIter]
        ranSlices[0].vertex_properties.binaryMappingVar[vnfFunction] = 0
        ranSlices[0].vertex_properties.degree[vnfFunction] = len(ranSlices[0].get_all_neighbors(vnfFunction))
        loopIter += 1
    
    # Setting up the totalResources per vertex
    for vnfFunction in ranSlices[0].vertices():
        resAcc = ranSlices[0].vp.resourceCapacity[vnfFunction]
        
        for vnfFunctionNeighbor in vnfFunction.all_neighbors():
            resAcc += ranSlices[0].vp.resourceCapacity[vnfFunctionNeighbor]
        
        ranSlices[0].vp.totalResourcesAcc[vnfFunction] = resAcc
    
    # Setting uy the Edge Properties
    for vnfEdge in ranSlices[0].edges():
        ranSlices[0].edge_properties.bandwidth[vnfEdge] = 3