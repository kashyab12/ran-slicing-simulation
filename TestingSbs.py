import Substrate as sbs
import RAN_Slice as ran
import numpy as np
import AlgorithmOne as algoOne
from graph_tool.all import *
import random
import matplotlib.pyplot as plt
import TotalNetwork as tn

# (1) no. of sbs vs no. of successfull mappings

def testParameters(algoType, subsNetwork, rnSlices, intervalFactor = tn.intervalFactor, iterations = tn.iterCount):

    noSbs = tn.numSubsNodes
    ranSlices = rnSlices
    substrateNetwork = subsNetwork
    yTwoUnsuccMappings = []
    yThreeResourceAvail = []
    yFourResourceExhuast = []    

    xOne = []
    yOne = []
    
    totalNetwork = tn.createTotalNetwork(substrateNetwork, ranSlices)

    for ctrVar in range(iterations):
    
        out = "Graph-Figures/debugSbs" + str(algoType) + str(ctrVar) + ".png"
        graph_draw(totalNetwork, vertex_text = totalNetwork.vp.get("resourceCapacity"), output=out, bg_color=[1,1,1,1], output_size=(3840, 2160))
        # totalNetwork = tn.createTotalNetwork(substrateNetwork, ranSlices)
            
        if algoType == 1:
            numMappings = tn.algoOneTest(totalNetwork)
        elif algoType == 2:
            numMappings = tn.algoTwoTest(totalNetwork)
        elif algoType == 3:
            numMappings = tn.algoThreeTest(totalNetwork)
        elif algoType == 4:
            numMappings = tn.algoFourTest(totalNetwork)
        
        xOne.append(noSbs)
        
        if len(yOne) == 0:
            yOne.append(numMappings)
        else:
            yOne.append(numMappings + yOne[-1])
    
        yTwoUnsuccMappings.append(tn.numVnfFunctions - yOne[-1])
        yThreeResourceAvail.append(tn.sbsAvailableRes(totalNetwork))
        yFourResourceExhuast.append(noSbs*tn.resCtPerSbs - yThreeResourceAvail[-1])

        addSbsNode(substrateNetwork, intervalFactor, totalNetwork=totalNetwork)
        tn.updateVnfMapVar(totalNetwork, ranSlices)
        
        noSbs += intervalFactor

    returnData = [xOne, yOne, yTwoUnsuccMappings, yThreeResourceAvail, yFourResourceExhuast]

    return returnData;
    

def addSbsNode(sbsNetwork, numVertices, totalNetwork = 0, connectivity = tn.sbsDegree):

    vertices = []
    sbsNodes =[]
    
    for node in totalNetwork.vertices():
        if totalNetwork.vp.binaryMappingVar[node] == -1:
            sbsNodes.append(node)

    for manyNodes in range(numVertices):
        # vertices.append(sbsNetwork.add_vertex())
        vertices.append(totalNetwork.add_vertex())
    
    graph_draw(sbsNetwork, output = "Graph-Figures/Adding-One.png", vertex_text = sbsNetwork.vp.get("resourceCapacity"))

    for newNode in vertices:

        toMapSbs = 0
        
        for numConnections in range(connectivity):

            while True:
                # toMapSbs = random.choice(find_vertex(sbsNetwork, sbsNetwork.vp.graphName, "Substrate"))
                toMapSbs = random.choice(sbsNodes)

                if toMapSbs not in newNode.all_neighbors() and toMapSbs != newNode:
                    break
                else:
                    continue
            
            # sbsNetwork.add_edge(newNode, toMapSbs)
            totalNetwork.add_edge(newNode, toMapSbs)
            sbsNodes.append(newNode)
            

    # sbs.setSbsTowerProperties(sbsNetwork, tn.resCapList, sbsNodes= vertices)
    sbs.setSbsTowerProperties(totalNetwork, tn.resCapList, sbsNodes= vertices)

    graph_draw(sbsNetwork, output = "Graph-Figures/Adding-Two.png", vertex_text = sbsNetwork.vp.get("resourceCapacity"))
