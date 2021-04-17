import AlgorithmOne as algoOne
import AlgorithmTwo as algoTwo
import AlgorithmThree as algoThree
from graph_tool.all import *
import random
import TotalNetwork as tn
import matplotlib.pyplot as plt
import RAN_Slice as ran

# (1) No. of vnf vs No. of succesfull mappings

def testParameters(algoType, subsNetwork, rnSlices, intervalFactor = tn.intervalFactor, iterations = tn.iterCount):

    noVnf = tn.numVnfFunctions
    substrateNetwork = subsNetwork
    ranSlices = rnSlices
    xOne = []
    yOne = []
    yTwoUnsuccMappings = []
    yThreeResourceAvail = []
    yFourResourceExhuast = []   
    
    totalNetwork  = tn.createTotalNetwork(substrateNetwork, ranSlices)

    for ctrVar in range(iterations):
    
        out = "Graph-Figures/debugVnf" + str(algoType) + str(ctrVar) +".png"
        graph_draw(totalNetwork, vertex_text = totalNetwork.vp.get("resources"), bg_color=[1,1,1,1], output_size = (3840,2160), output=out)

        if algoType == 1:
            numMappings = tn.algoOneTest(totalNetwork)
        elif algoType == 2:
            numMappings = tn.algoTwoTest(totalNetwork)
        elif algoType == 3:
            numMappings = tn.algoThreeTest(totalNetwork)
        elif algoType == 4:
            numMappings = tn.algoFourTest(totalNetwork)
        
        xOne.append(noVnf)
        
        if len(yOne) == 0:
            yOne.append(numMappings)
        else:
            yOne.append(numMappings + yOne[-1])
            
        yTwoUnsuccMappings.append(noVnf - yOne[-1])
        yThreeResourceAvail.append(tn.sbsAvailableRes(totalNetwork))
        yFourResourceExhuast.append(tn.numSubsNodes*tn.resCtPerSbs - yThreeResourceAvail[-1])
            
        addVnf(ranSlices, intervalFactor, totalNetwork=totalNetwork)
        tn.updateVnfMapVar(totalNetwork, ranSlices)
        
        noVnf += intervalFactor

    returnData = [xOne, yOne, yTwoUnsuccMappings, yThreeResourceAvail, yFourResourceExhuast]

    return returnData;

def addVnf(ranSlices, numVnfs, totalNetwork=0, connectivity = tn.vnfDegree):

    vertices = []
    ranSliceNodes = []

    for node in totalNetwork.vertices():
        if totalNetwork.vp.binaryMappingVar[node] != -1:
            ranSliceNodes.append(node)

    for manyNodes in range(numVnfs):
        vertices.append(totalNetwork.add_vertex())
    
    graph_draw(ranSlices, output = "Graph-Figures/Adding-Three.png", vertex_text = ranSlices.vp.get("resources"))

    for newNode in vertices:

        toMapVnf = 0
        
        for numConnections in range(connectivity):

            while True:

                toMapVnf = random.choice(ranSliceNodes)

                if toMapVnf not in newNode.all_neighbors() and toMapVnf != newNode:
                    break
                else:
                    continue
            
            totalNetwork.add_edge(newNode, toMapVnf)
            ranSliceNodes.append(newNode)

    ran.setVNFFunctionProperties(totalNetwork, tn.resList, vnfList=vertices)

    graph_draw(ranSlices, output = "Graph-Figures/Adding-Four.png", vertex_text = ranSlices.vp.get("resources"))