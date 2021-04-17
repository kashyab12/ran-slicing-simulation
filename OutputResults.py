import TestingSbs as testSbs
import TestingSbsConnection as testSbsCon
import TestingVNF as testVnf
import TestingVnfConnection as testVnfCon
import TestingRan as testRan
import matplotlib.pyplot as plt
import numpy as np
import random 
import TotalNetwork as tn
from graph_tool.all import *
import copy
import multiprocessing as mp

def outputFigure(resultOne, resultTwo, resultThree, resultFour, xLabel, yLabel, outputTitle, savedLocation, maxValue = tn.numVnfFunctions):
    fig, ax = plt.subplots()
    ax.plot(resultOne[0], resultOne[1], label="Algo One", linestyle='-', linewidth=2.0, marker='^', color='r')
    ax.plot(resultTwo[0], resultTwo[1], label="Algo Two", linestyle='--', linewidth=2.0, marker='s', color='b')
    ax.plot(resultThree[0], resultThree[1], label="Algo Three", linestyle=':' ,linewidth=2.0, marker='p', color='m')
    ax.plot(resultFour[0], resultFour[1], label="Algo Four", linestyle='-.', linewidth=2.0, marker='*', color='g')

    majorTickX = np.array(resultOne[0])
    ax.set_xticks(majorTickX)
    
    minResultOne = min(resultOne[1])
    minResultTwo = min(resultTwo[1])
    minResultThree = min(resultThree [1])
    minResultFour = min(resultFour[1])
    minYValueArray = [minResultOne, minResultTwo, minResultThree, minResultFour]
    minYValue = min(minYValueArray)
    
    interval = (maxValue - minYValue) / (tn.iterCount - 1)
    yAxisIntervals = []
    
    for idx in range(tn.iterCount):
        if idx == 0:
            yAxisIntervals.append(minYValue)
        elif idx == (tn.iterCount - 1):
            yAxisIntervals.append(maxValue)
        else:
            yAxisIntervals.append(round(minYValue + idx*(interval)))
    
    yAxisTicks = np.array(yAxisIntervals)
    
    ax.set_yticks(yAxisTicks)

    ax.set(xlabel=xLabel, ylabel=yLabel,
    title=outputTitle)
    ax.grid()
    ax.legend(loc="best")

    fig.savefig(savedLocation, dpi= 1200)
    plt.show()
    

def generateSbsTestResults(ranSlices, substrateNetwork):

    xLabel = "Number of Substrate Towers"
    
    # ranSlices = tn.createRANSlice(tn.numRnSlices, tn.numVnfFunctions, tn.resList, tn.resCtPerVnf, connectivity=tn.vnfDegree, random_range=0)
    # substrateNetwork = tn.createSbsNetwork(tn.numSubsNodes, tn.resCapList, resCtPerSbs=tn.resCtPerSbs, connectivity=tn.sbsDegree, random_range=0)

    # First testing - Abundance
    returnOne = testSbs.testParameters(1, substrateNetwork, ranSlices)
    returnTwo = testSbs.testParameters(2, substrateNetwork, ranSlices)
    returnThree = testSbs.testParameters(3, substrateNetwork, ranSlices)
    returnFour = testSbs.testParameters(4, substrateNetwork, ranSlices)
    
    output_text = open(r"ResultsOne/num-sbs-tower-abundance.txt", "w")
    output_text.writelines("Abundance")
    output_text.write(str("X-Values - " + str(returnOne[0]) + str("\n")))
    output_text.write(str("Algo One - ") + str(returnOne[1]) + str("\n"))
    output_text.write(str("Algo Two - ") + str(returnTwo[1]) + str("\n"))
    output_text.write(str("Algo Three - ") + str(returnThree[1]) + str("\n"))
    output_text.write(str("Algo Four - ") + str(returnFour[1]) + str("\n"))
    
    # Now that we have all the results with the subsequent arrays
    
    savedLocation = "ResultsOne/sbsOneAbundance.png"
    yLabel = "Number of Successful Mappings"
    outputTitle = "Abundant Substrate Layer"
    resultOne = [returnOne[0], returnOne[1]]
    resultTwo = [returnTwo[0], returnTwo[1]]
    resultThree = [returnThree[0], returnThree[1]]
    resultFour = [returnFour[0], returnFour[1]]
    
    outputFigure(resultOne, resultTwo, resultThree, resultFour, xLabel, yLabel, outputTitle, savedLocation)
    
    # Variable Resources for Substrate
    deficitResSbsNetwork = copy.deepcopy(substrateNetwork)
    
    varResNetwork(deficitResSbsNetwork, tn.randUpBoundSbs, layer = "Substrate")
    # varDegSbs(deficitResSbsNetwork, varSbsDeg)
    # varBandSbs(deficitResSbsNetwork, varBandSbs)
    
    returnOne = testSbs.testParameters(1, deficitResSbsNetwork, ranSlices)
    returnTwo = testSbs.testParameters(2, deficitResSbsNetwork, ranSlices)
    returnThree = testSbs.testParameters(3, deficitResSbsNetwork, ranSlices)
    returnFour = testSbs.testParameters(4, deficitResSbsNetwork, ranSlices)
    
    # Now that we have all the results with the subsequent arrays
    
    savedLocation = "ResultsOne/sbsOneResDeficit.png"
    yLabel = "Number of Successful Mappings"
    outputTitle = "Resource Deficit for Substrate Node"
    resultOne = [returnOne[0], returnOne[1]]
    resultTwo = [returnTwo[0], returnTwo[1]]
    resultThree = [returnThree[0], returnThree[1]]
    resultFour = [returnFour[0], returnFour[1]]
    
    output_text = open(r"ResultsOne/num-sbs-tower-res_deficit.txt", "w")
    output_text.writelines("Resource Deficit for Substrate")
    
    output_text.write(str("X-Values - " + str(returnOne[0]) + str("\n")))
    output_text.write(str("Algo One - ") + str(returnOne[1]) + str("\n"))
    output_text.write(str("Algo Two - ") + str(returnTwo[1]) + str("\n"))
    output_text.write(str("Algo Three - ") + str(returnThree[1]) + str("\n"))
    output_text.write(str("Algo Four - ") + str(returnFour[1]) + str("\n"))
    
    outputFigure(resultOne, resultTwo, resultThree, resultFour, xLabel, yLabel, outputTitle, savedLocation)
    
    # Varying Bandwidth for Substrate
    
    deficitBandSbsNetwork = copy.deepcopy(substrateNetwork)
    
    varBandSbs(deficitResSbsNetwork, tn.varSbsBand)
    
    returnOne = testSbs.testParameters(1, deficitResSbsNetwork, ranSlices)
    returnTwo = testSbs.testParameters(2, deficitResSbsNetwork, ranSlices)
    returnThree = testSbs.testParameters(3, deficitResSbsNetwork, ranSlices)
    returnFour = testSbs.testParameters(4, deficitResSbsNetwork, ranSlices)
    
    # Now that we have all the results with the subsequent arrays
    
    savedLocation = "ResultsOne/sbsOneBandDeficit.png"
    yLabel = "Number of Successful Mappings"
    outputTitle = "Bandwidth Deficit for Substrate Node"
    resultOne = [returnOne[0], returnOne[1]]
    resultTwo = [returnTwo[0], returnTwo[1]]
    resultThree = [returnThree[0], returnThree[1]]
    resultFour = [returnFour[0], returnFour[1]]
    
    output_text = open(r"ResultsOne/num-sbs-tower-band_deficit.txt", "w")
    output_text.writelines("Bandwidth Deficit for Substrate")
    
    output_text.write(str("X-Values - " + str(returnOne[0]) + str("\n")))
    output_text.write(str("Algo One - ") + str(returnOne[1]) + str("\n"))
    output_text.write(str("Algo Two - ") + str(returnTwo[1]) + str("\n"))
    output_text.write(str("Algo Three - ") + str(returnThree[1]) + str("\n"))
    output_text.write(str("Algo Four - ") + str(returnFour[1]) + str("\n"))
    
    outputFigure(resultOne, resultTwo, resultThree, resultFour, xLabel, yLabel, outputTitle, savedLocation)

def generateVnfTestResults(ranSlices, substrateNetwork):

    xLabel = "Number of VNF"

    # First testing - Abundance
    returnOne = testVnf.testParameters(1, substrateNetwork, ranSlices)
    returnTwo = testVnf.testParameters(2, substrateNetwork, ranSlices)
    returnThree = testVnf.testParameters(3, substrateNetwork, ranSlices)
    returnFour = testVnf.testParameters(4, substrateNetwork, ranSlices)
    
    output_text = open(r"ResultsThree/num-vnf-abundance.txt", "w")
    output_text.writelines("Abundance")
    output_text.write(str("X-Values - " + str(returnOne[0]) + str("\n")))
    output_text.write(str("Algo One - ") + str(returnOne[1]) + str("\n"))
    output_text.write(str("Algo Two - ") + str(returnTwo[1]) + str("\n"))
    output_text.write(str("Algo Three - ") + str(returnThree[1]) + str("\n"))
    output_text.write(str("Algo Four - ") + str(returnFour[1]) + str("\n"))
    
    # Now that we have all the results with the subsequent arrays
    
    savedLocation = "ResultsThree/vnfOneAbundance.png"
    yLabel = "Number of Successful Mappings"
    outputTitle = "Abundant Substrate Layer"
    resultOne = [returnOne[0], returnOne[1]]
    resultTwo = [returnTwo[0], returnTwo[1]]
    resultThree = [returnThree[0], returnThree[1]]
    resultFour = [returnFour[0], returnFour[1]]
    
    outputFigure(resultOne, resultTwo, resultThree, resultFour, xLabel, yLabel, outputTitle, savedLocation)
    
    # Variable Resources for Substrate
    deficitResSbsNetwork = copy.deepcopy(substrateNetwork)
    
    varResNetwork(deficitResSbsNetwork, tn.randUpBoundSbs, layer = "Substrate")
    
    returnOne = testVnf.testParameters(1, deficitResSbsNetwork, ranSlices)
    returnTwo = testVnf.testParameters(2, deficitResSbsNetwork, ranSlices)
    returnThree = testVnf.testParameters(3, deficitResSbsNetwork, ranSlices)
    returnFour = testVnf.testParameters(4, deficitResSbsNetwork, ranSlices)
    
    # Now that we have all the results with the subsequent arrays
    
    savedLocation = "ResultsThree/vnfOneResDeficit.png"
    yLabel = "Number of Successful Mappings"
    outputTitle = "Resource Deficit for Substrate Node"
    resultOne = [returnOne[0], returnOne[1]]
    resultTwo = [returnTwo[0], returnTwo[1]]
    resultThree = [returnThree[0], returnThree[1]]
    resultFour = [returnFour[0], returnFour[1]]
    
    output_text = open(r"ResultsThree/num-vnf-res_deficit.txt", "w")
    output_text.writelines("Resource Deficit for Substrate")
    
    output_text.write(str("X-Values - " + str(returnOne[0]) + str("\n")))
    output_text.write(str("Algo One - ") + str(returnOne[1]) + str("\n"))
    output_text.write(str("Algo Two - ") + str(returnTwo[1]) + str("\n"))
    output_text.write(str("Algo Three - ") + str(returnThree[1]) + str("\n"))
    output_text.write(str("Algo Four - ") + str(returnFour[1]) + str("\n"))
    
    outputFigure(resultOne, resultTwo, resultThree, resultFour, xLabel, yLabel, outputTitle, savedLocation)
    
    # Varying Bandwidth for Substrate
    
    deficitBandSbsNetwork = copy.deepcopy(substrateNetwork)
    
    varBandSbs(deficitResSbsNetwork, tn.varSbsBand)
    
    returnOne = testVnf.testParameters(1, deficitResSbsNetwork, ranSlices)
    returnTwo = testVnf.testParameters(2, deficitResSbsNetwork, ranSlices)
    returnThree = testVnf.testParameters(3, deficitResSbsNetwork, ranSlices)
    returnFour = testVnf.testParameters(4, deficitResSbsNetwork, ranSlices)
    
    # Now that we have all the results with the subsequent arrays
    
    savedLocation = "ResultsThree/vnfOneBandDeficit.png"
    yLabel = "Number of Successful Mappings"
    outputTitle = "Bandwidth Deficit for Substrate Node"
    resultOne = [returnOne[0], returnOne[1]]
    resultTwo = [returnTwo[0], returnTwo[1]]
    resultThree = [returnThree[0], returnThree[1]]
    resultFour = [returnFour[0], returnFour[1]]
    
    output_text = open(r"ResultsThree/num-vnf-band_deficit.txt", "w")
    output_text.writelines("Bandwidth Deficit for Substrate")
    
    output_text.write(str("X-Values - " + str(returnOne[0]) + str("\n")))
    output_text.write(str("Algo One - ") + str(returnOne[1]) + str("\n"))
    output_text.write(str("Algo Two - ") + str(returnTwo[1]) + str("\n"))
    output_text.write(str("Algo Three - ") + str(returnThree[1]) + str("\n"))
    output_text.write(str("Algo Four - ") + str(returnFour[1]) + str("\n"))
    
    outputFigure(resultOne, resultTwo, resultThree, resultFour, xLabel, yLabel, outputTitle, savedLocation)

# Work In Progress
def generateRanTestResults():

    xLabel = "Number of RAN Slices"
    outputTitle = "Independent Variable - No. of Ran Slices"

    # First Testing Against Succesfull Mappings

    resultOne = testRan.testSuccMappings(1)
    resultTwo = testRan.testSuccMappings(2)
    resultThree = testRan.testSuccMappings(3)
    resultFour = testRan.testSuccMappings(4)

    savedLocation = "ResultsFive/ranOne.png"
    yLabel = "Number of Succesfull Mappings"

    # Now that we have all the results with the subsequent arrays

    outputFigure(resultOne, resultTwo, resultThree, resultFour, xLabel, yLabel, outputTitle, savedLocation, tn.numRnSlices, tn.numRnSlices + testVnf.intervalFactor*tn.numRnSlices, testVnf.intervalFactor )

    # Now test against Unsucessfull Mappings

    resultOne = testRan.testUnsuccMappings(1)
    resultTwo = testRan.testUnsuccMappings(2)
    resultThree = testRan.testUnsuccMappings(3)
    resultFour = testRan.testUnsuccMappings(4)
    savedLocation = "ResultsFive/ranTwo.png"
    yLabel = "Number of Unsuccesfull Mappings"

    #  Now that we have all the results with the subsequent arrays

    outputFigure(resultOne, resultTwo, resultThree, resultFour, xLabel, yLabel, outputTitle, savedLocation, tn.numRnSlices, tn.numRnSlices + testVnf.intervalFactor*tn.numRnSlices, testVnf.intervalFactor )

    # Test Against Avail Resources

    resultOne = testRan.testAvailRes(1)
    resultTwo = testRan.testAvailRes(2)
    resultThree = testRan.testAvailRes(3)
    resultFour = testRan.testAvailRes(4)
    savedLocation = "ResultsFive/ranThree.png"
    yLabel = "Amount of Available Resources"

    #  Now that we have all the results with the subsequent arrays

    outputFigure(resultOne, resultTwo, resultThree, resultFour, xLabel, yLabel, outputTitle, savedLocation, tn.numRnSlices, tn.numRnSlices + testVnf.intervalFactor*tn.numRnSlices, testVnf.intervalFactor )

    # Test Against Avail Resources

    resultOne = testRan.testExhaustRes(1)
    resultTwo = testRan.testExhaustRes(2)
    resultThree = testRan.testExhaustRes(3)
    resultFour = testRan.testExhaustRes(4)
    savedLocation = "ResultsFive/ranFour.png"
    yLabel = "Amount of Exhausted Resources"

    #  Now that we have all the results with the subsequent arrays

    outputFigure(resultOne, resultTwo, resultThree, resultFour, xLabel, yLabel, outputTitle, savedLocation, tn.numRnSlices, tn.numRnSlices + testVnf.intervalFactor*tn.numRnSlices, testVnf.intervalFactor )


def varResNetwork(networkLayer, bound, layer = "RAN"):

    if layer == "RAN":
        for node in networkLayer.vertices():
            networkLayer.vp.resources[node] += random.randint(0, bound)
    elif layer == "Substrate":
        for node in networkLayer.vertices():
            networkLayer.vp.resourceCapacity[node] += random.randint(bound, 0)
            
def resetVarResNetwork(networkLayer, resourceCount, layer = "RAN"):
    
    if layer == "RAN":
        for node in networkLayer.vertices():
            networkLayer.vp.resources[node] = resourceCount
    elif layer == "Substrate":
        for node in networkLayer.vertices():
            networkLayer.vp.resourceCapacity[node] = resourceCount

            
def varDegSbs(sbsNetwork, newSbsDeg):

    # sbsNetwork.set_fast_edge_removal(True)
    
    for node in reversed(sorted(sbsNetwork.vertices())):
        if sbsNetwork.vp.degree[node] > newSbsDeg:
            nodeEdges = []
            deletedEdges = []
            
            for edge in sbsNetwork.edges():
                if edge.source() == node or edge.target() == node:
                    nodeEdges.append(edge)
                    
            ctrVar = len(nodeEdges) - 1
            
            while ctrVar >= 0:
                if sbsNetwork.vp.degree[node] == newSbsDeg:
                    break
                elif nodeEdges[ctrVar].source() == node and nodeEdges[ctrVar].target().is_valid():
                    if  sbsNetwork.vp.degree[nodeEdges[ctrVar].target()] > newSbsDeg:
                        sbsNetwork.remove_edge(nodeEdges[ctrVar])
                        sbsNetwork.vp.degree[node] -= 1
                        sbsNetwork.vp.degree[nodeEdges[ctrVar].target()] -= 1
                # elif toRemEdge.target() == node and toRemEdge.source().is_valid():
                #     if sbsNetwork.vp.degree[toRemEdge.source()] > newSbsDeg:
                #         sbsNetwork.remove_edge(toRemEdge)
                #         sbsNetwork.vp.degree[node] -= 1
                #         sbsNetwork.vp.degree[toRemEdge.source()] -= 1
            
            # for toRemEdge in reversed(sorted(nodeEdges)):
            #     if sbsNetwork.vp.degree[node] == newSbsDeg:
            #         break
            #     elif toRemEdge.source() == node and toRemEdge.target().is_valid():
            #         if  sbsNetwork.vp.degree[toRemEdge.target()] > newSbsDeg:
            #             sbsNetwork.remove_edge(toRemEdge)
            #             sbsNetwork.vp.degree[node] -= 1
            #             sbsNetwork.vp.degree[toRemEdge.target()] -= 1
            #     elif toRemEdge.target() == node and toRemEdge.source().is_valid():
            #         if sbsNetwork.vp.degree[toRemEdge.source()] > newSbsDeg:
            #             sbsNetwork.remove_edge(toRemEdge)
            #             sbsNetwork.vp.degree[node] -= 1
            #             sbsNetwork.vp.degree[toRemEdge.source()] -= 1
                        

def varBandSbs(sbsNetwork, newSbsBand):
    
    for edge in sbsNetwork.edges():
        sbsNetwork.ep.bandwidth[edge] += random.randint(tn.varSbsBand, 0)