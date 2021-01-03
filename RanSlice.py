# Import Statements
from graph_tools import *

# Declaring Global Variables

ranSlices = []
vnfFunctions = []
resList = [3, 2, 1]
vnfConnections = [(0, 1), (0, 2), (1, 2)]
vnfEdges = []

def createRANSlices():

    # Creating the RAN Slices

    for idx in range(1):
        ranSlices.append(Graph(directed=False))


def setRANSliceProperties():

    # Creating Properties for the RAN Slices
    # --------------------------------------

    # Giving the VNF Functions a Name Property
    nameProp = ranSlices[0].new_vertex_property("string")
    ranSlices[0].vertex_properties.vertexName = nameProp

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


def createVNFFunctions():
    
    # Creating the VNF Functions
    
    for idx in range(3):
        ranVertex = ranSlices[0].add_vertex()
        vnfFunctions.append(ranVertex)


def setVNFFunctionProperties():

    # Setting the names for the VNF Functions

    for idx in range(3):
        ranSlices[0].vertex_properties.vertexName[vnfFunctions[idx]] = "S" + str(idx)

    # Setting the resource capacity for the VNF Functions

    for idx in range(3):
        ranSlices[0].vertex_properties.resourceCapacity[vnfFunctions[idx]] = -1

    # Setting the resource value for the VNF Functions

    for idx in range(3):
        ranSlices[0].vertex_properties.resources[vnfFunctions[idx]] = resList[idx]

    # Setting the Binary Mapping Variable for the VNF Functions

    for idx in range(3):
        ranSlices[0].vertex_properties.binaryMappingVar[vnfFunctions[idx]] = 0


def createVNFConnections():
    # Creating the connections between VNF Functions

    for vnf_connection in vnfConnections:
        ranSlicesEdges = ranSlices[0].add_edge(vnf_connection[0], vnf_connection[1])
        vnfEdges.append(ranSlicesEdges) 

    # Setting the Bandwidth Property on the Connections between the Substrate Networks
    # !! Hard Coded Value Included within this Loop !!

    for edgeConnection in vnfEdges:
        ranSlices[0].edge_properties.bandwidth[edgeConnection] = 3

