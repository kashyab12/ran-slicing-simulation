# Import Statements
from graph_tool.all import *
import math
import random
from matplotlib import pyplot as plt

# Function defined to create an RAN Slice


# def createRANSlices(ranSlices, numRnSlices):

#     # Creating the RAN Slices
#     for idx in range(numRnSlices):
#         ranSlices.append(random_graph()


def setRANSliceProperties(ranSlices):

    # Creating Properties for the RAN Slices
    # --------------------------------------

    graphProp = ranSlices[0].new_graph_property("string")
    ranSlices.gp.graphName = graphProp

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


# # Function to create VNF Functions for the respective RAN Slices
# def createVNFFunctions(ranSlices, numVnfFunctions, vnfFunctions):
#     # Creating the VNF Functions
#     for idx in range(numVnfFunctions):
#         ranVertex = ranSlices[0].add_vertex()
#         vnfFunctions.append(ranVertex)

# Function to Set the Properties for the VNF Functions
def setVNFFunctionProperties(ranSlices, numVnfFunctions, vnfFunctions, resList):

    # Setting up the Graph Properties
    ranSlices[0].gp.graphName = "RAN1"\
    
    # Setting up the Vertex Properties
    for vnfFunction in ranSlices[0].vertices():
        ranSlices[0].vertex_properties.resourceCapacity[vnfFunction] = -1   

    # Setting the names for the VNF Functions
    for idx in range(numVnfFunctions):
        # Setting the resource capacity for the VNF Functions
        ranSlices[0].vertex_properties.resourceCapacity[vnfFunctions[idx]] = -1
        # Setting the resource value for the VNF Functions
        ranSlices[0].vertex_properties.resources[vnfFunctions[idx]] = resList[idx]
        # Setting the Binary Mapping Variable for the VNF Functions
        ranSlices[0].vertex_properties.binaryMappingVar[vnfFunctions[idx]] = 0

# Function to create Connections within the VNF Functions
def createVNFConnections(ranSlices, numVnfFunctions, vnfEdges):
    # Creating the connections between VNF Functions
    
    maxEdges = (numVnfFunctions*(numVnfFunctions - 1)) / 2 
    minEdges = numVnfFunctions - 1

    # randomEdges = random.randint(minEdges, maxEdges)
    randomEdges = maxEdges
    counterVar = 0

    for vertex in ranSlices[0].vertices():

        randomNode = random.choice(list(ranSlices[0].vertices()))

        while vertex == randomNode or vertex in randomNode.all_neighbors():
            randomNode = random.choice(list(ranSlices[0].vertices()))

        vnfEdge = ranSlices[0].add_edge(vertex, randomNode)
        vnfEdges.append(vnfEdge) 

        counterVar += 1

        if counterVar == minEdges:
            break

    if minEdges != randomEdges:
        counter = minEdges

        while counter < randomEdges:
            nodeOne = random.choice(list(ranSlices[0].vertices()))
            nodeTwo = random.choice(list(ranSlices[0].vertices()))

            if nodeOne != nodeTwo:
                if nodeOne in nodeTwo.all_neighbors():
                    continue
                else:
                    vnfEdge = ranSlices[0].add_edge(nodeOne, nodeTwo)
                    vnfEdges.append(vnfEdge)
                    counter += 1

    for edgeConnection in vnfEdges:
        ranSlices[0].edge_properties.bandwidth[edgeConnection] = 3

    return randomEdges;
