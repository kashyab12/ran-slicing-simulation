import AlgorithmOne as algoOne
import AlgorithmTwo as algoTwo
import AlgorithmThree as algoThree
from graph_tool.all import *
import random
import TotalNetwork as tn
import matplotlib.pyplot as plt

# (1) No. of vnf vs No. of succesfull mappings

def testSuccMappings(algoType):

    noVnf = tn.numVnfFunctions

    xOne = []
    yOne = []

    for ctrVar in range(5):

        substrateNetwork = tn.createSbsNetwork(tn.numSubsNodes, tn.resCapList, tn.resCtPerSbs)
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
        ranSlices[0].clear()
        totalNetwork.clear()
        tn.resCapList.clear()
        tn.resList.clear()
        tn.vnfCncList.clear()
        tn.vnfTotalAccList.clear()
        
        noVnf += 150

    returnData = [xOne, yOne]

    return returnData;
    

# (2) No. of vnf vs No. of unsuccesfull mappings

def testUnsuccMappings(algoType):

    noVnf = tn.numVnfFunctions

    xOne = []
    yOne = []

    for ctrVar in range(5):
        
        substrateNetwork = tn.createSbsNetwork(tn.numSubsNodes, tn.resCapList, tn.resCtPerSbs)
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
        ranSlices[0].clear()
        totalNetwork.clear()
        tn.resCapList.clear()
        tn.resList.clear()
        tn.vnfCncList.clear()
        tn.vnfTotalAccList.clear()
        
        noVnf += 150

    returnData = [xOne, yOne]

    return returnData;


# (3) No. of vnf vs No. of Available Substrate Resources

def testAvailRes(algoType):

    noVnf = tn.numVnfFunctions

    xOne = []
    yOne = []

    for ctrVar in range(5):
        
        substrateNetwork = tn.createSbsNetwork(tn.numSubsNodes, tn.resCapList, tn.resCtPerSbs)
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
        ranSlices[0].clear()
        totalNetwork.clear()
        tn.resCapList.clear()
        tn.resList.clear()
        tn.vnfCncList.clear()
        tn.vnfTotalAccList.clear()
        
        noVnf += 150

    returnData = [xOne, yOne]

    return returnData;

# (4) No. of vnf vs Amount of Exhausted Substrate Resources

def testExhaustRes(algoType):

    noVnf = tn.numVnfFunctions

    xOne = []
    yOne = []

    for ctrVar in range(5):
        
        # One
        
        substrateNetwork = tn.createSbsNetwork(tn.numSubsNodes, tn.resCapList, tn.resCtPerSbs)
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
        ranSlices[0].clear()
        totalNetwork.clear()
        tn.resCapList.clear()
        tn.resList.clear()
        tn.vnfCncList.clear()
        tn.vnfTotalAccList.clear()
        
        noVnf += 150

    returnData = [xOne, yOne]

    return returnData;
