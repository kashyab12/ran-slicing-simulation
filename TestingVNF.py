import AlgorithmOne as algoOne
import AlgorithmTwo as algoTwo
import AlgorithmThree as algoThree
from graph_tool.all import *
import random
import TotalNetwork as tn
import matplotlib.pyplot as plt

intervalFactor = 2

# (1) No. of vnf vs No. of succesfull mappings

def testSuccMappings(algoType):

    noRanSlices = tn.numRnSlices

    xOne = []
    yOne = []

    substrateNetwork = tn.createSbsNetwork(tn.numSubsNodes, tn.resCapList, tn.resCtPerSbs)

    for ctrVar in range(5):

        ranSlices = tn.createRANSlice(tn.numRnSlices, noVnf, tn.resList, tn.resCtPerVnf)
        totalNetwork  = tn.createTotalNetwork(substrateNetwork, ranSlices, tn.vnfCncList, tn.vnfTotalAccList)
        
        if algoType == 1:
            numMappings = tn.algoOneTest(totalNetwork, substrateNetwork, ranSlices, tn.resList, tn.resCapList)
        elif algoType == 2:
            numMappings = tn.algoTwoTest(totalNetwork, tn.vnfCncList)
        elif algoType == 3:
            numMappings = tn.algoThreeTest(totalNetwork, tn.vnfTotalAccList)
        else:
            numMappings = tn.algoFourTest(totalNetwork, substrateNetwork, ranSlices, tn.resCapList, tn.vnfCncList)
        
        
        xOne.append(noVnf)
        yOne.append(numMappings)

        substrateNetwork.clear()
        ranSlices.clear()
        totalNetwork.clear()
        tn.resList.clear()
        tn.vnfCncList.clear()
        tn.vnfTotalAccList.clear()
        
        noVnf += intervalFactor

    returnData = [xOne, yOne]

    return returnData;
    

# (2) No. of vnf vs No. of unsuccesfull mappings

def testUnsuccMappings(algoType):

    noVnf = tn.numVnfFunctions

    xOne = []
    yOne = []

    substrateNetwork = tn.createSbsNetwork(tn.numSubsNodes, tn.resCapList, tn.resCtPerSbs)

    for ctrVar in range(5):
        
        ranSlices = tn.createRANSlice(tn.numRnSlices, noVnf, tn.resList, tn.resCtPerVnf)
        totalNetwork  = tn.createTotalNetwork(substrateNetwork, ranSlices, tn.vnfCncList, tn.vnfTotalAccList)
            
        if algoType == 1:
            numMappings = tn.algoOneTest(totalNetwork, substrateNetwork, ranSlices, tn.resList, tn.resCapList)
        elif algoType == 2:
            numMappings = tn.algoTwoTest(totalNetwork, tn.vnfCncList)
        elif algoType == 3:
            numMappings = tn.algoThreeTest(totalNetwork, tn.vnfTotalAccList)
        else:
            numMappings = tn.algoFourTest(totalNetwork, substrateNetwork, ranSlices, tn.resCapList, tn.vnfCncList)
        
        xOne.append(noVnf)
        yOne.append(noVnf - numMappings)

        substrateNetwork.clear()
        ranSlices.clear()
        totalNetwork.clear()
        tn.resList.clear()
        tn.vnfCncList.clear()
        tn.vnfTotalAccList.clear()
        
        noVnf += intervalFactor

    returnData = [xOne, yOne]

    return returnData;


# (3) No. of vnf vs No. of Available Substrate Resources

def testAvailRes(algoType):

    noVnf = tn.numVnfFunctions

    xOne = []
    yOne = []
    substrateNetwork = tn.createSbsNetwork(tn.numSubsNodes, tn.resCapList, tn.resCtPerSbs)

    for ctrVar in range(5):
        
        ranSlices = tn.createRANSlice(tn.numRnSlices, noVnf, tn.resList, tn.resCtPerVnf)
        totalNetwork  = tn.createTotalNetwork(substrateNetwork, ranSlices, tn.vnfCncList, tn.vnfTotalAccList)
            
        if algoType == 1:
            numMappings = tn.algoOneTest(totalNetwork, substrateNetwork, ranSlices, tn.resList, tn.resCapList)
        elif algoType == 2:
            numMappings = tn.algoTwoTest(totalNetwork, tn.vnfCncList)
        elif algoType == 3:
            numMappings = tn.algoThreeTest(totalNetwork, tn.vnfTotalAccList)
        else:
            numMappings = tn.algoFourTest(totalNetwork, substrateNetwork, ranSlices, tn.resCapList, tn.vnfCncList)
        
        xOne.append(noVnf)
        resAvail = tn.sbsAvailableRes(totalNetwork)
        yOne.append(resAvail)

        substrateNetwork.clear()
        ranSlices.clear()
        totalNetwork.clear()
        tn.resList.clear()
        tn.vnfCncList.clear()
        tn.vnfTotalAccList.clear()
        
        noVnf += intervalFactor

    returnData = [xOne, yOne]

    return returnData;

# (4) No. of vnf vs Amount of Exhausted Substrate Resources

def testExhaustRes(algoType):

    noVnf = tn.numVnfFunctions

    xOne = []
    yOne = []

    substrateNetwork = tn.createSbsNetwork(tn.numSubsNodes, tn.resCapList, tn.resCtPerSbs)

    for ctrVar in range(5):
        
        # One
        ranSlices = tn.createRANSlice(tn.numRnSlices, noVnf, tn.resList, tn.resCtPerVnf)
        totalNetwork  = tn.createTotalNetwork(substrateNetwork, ranSlices, tn.vnfCncList, tn.vnfTotalAccList)
            
        if algoType == 1:
            numMappings = tn.algoOneTest(totalNetwork, substrateNetwork, ranSlices, tn.resList, tn.resCapList)
        elif algoType == 2:
            numMappings = tn.algoTwoTest(totalNetwork, tn.vnfCncList)
        elif algoType == 3:
            numMappings = tn.algoThreeTest(totalNetwork, tn.vnfTotalAccList)
        else:
            numMappings = tn.algoFourTest(totalNetwork, substrateNetwork, ranSlices, tn.resCapList, tn.vnfCncList)
        
        
        xOne.append(noVnf)
        resAvail = tn.sbsAvailableRes(totalNetwork)
        yOne.append(tn.numSubsNodes*tn.resCtPerSbs - resAvail)

        substrateNetwork.clear()
        ranSlices.clear()
        totalNetwork.clear()
        tn.resList.clear()
        tn.vnfCncList.clear()
        tn.vnfTotalAccList.clear()
        
        noVnf += intervalFactor

    returnData = [xOne, yOne]

    return returnData;
