import Substrate as sbs
import RAN_Slice as ran
import numpy as np
import AlgorithmOne as algoOne
from graph_tool.all import *
import random
import matplotlib.pyplot as plt
import TotalNetwork as tn

# (1) no. of sbs vs no. of successfull mappings

def testSuccMappings(algoType, intervalFactor = 5, iterations = 20, numSubsNode = 10, numRnSlices = 1, numVnf = 20):

    noSbs = numSubsNode
    


    xOne = []
    yOne = []

    ranSlices = tn.createRANSlice(tn.numRnSlices, tn.numVnfFunctions, tn.resList, tn.resCtPerVnf, 3)

    for ctrVar in range(iterations):

        substrateNetwork = tn.createSbsNetwork(noSbs, tn.resCapList, tn.resCtPerSbs, 2)
        totalNetwork  = tn.createTotalNetwork(substrateNetwork, ranSlices, tn.vnfCncList, tn.vnfTotalAccList)
            
        if algoType == 1:
            numMappings = tn.algoOneTest(totalNetwork, substrateNetwork, ranSlices, tn.resList, tn.resCapList)
        elif algoType == 2:
            numMappings = tn.algoTwoTest(totalNetwork, tn.vnfCncList)
        elif algoType == 3:
            numMappings = tn.algoThreeTest(totalNetwork, tn.vnfTotalAccList)
        else:
            numMappings = tn.algoFourTest(totalNetwork, substrateNetwork, ranSlices, tn.resCapList, tn.vnfCncList)
        
        xOne.append(noSbs)
        yOne.append(numMappings)

        substrateNetwork.clear()
        totalNetwork.clear()
        tn.resCapList.clear()
        tn.vnfCncList.clear()
        tn.vnfTotalAccList.clear()
        
        noSbs += intervalFactor

    returnData = [xOne, yOne]

    return returnData;

# (2) no. of sbs vs no. of unsuccesfull mappings

def testUnsuccMappings(algoType, intervalFactor = 5, iterations = 20):

    noSbs = tn.numSubsNodes

    xOne = []
    yOne = []

    ranSlices = tn.createRANSlice(tn.numRnSlices, tn.numVnfFunctions, tn.resList, tn.resCtPerVnf, 3)

    for ctrVar in range(iterations):
        
        # One
        
        substrateNetwork = tn.createSbsNetwork(noSbs, tn.resCapList, tn.resCtPerSbs, 2)
        totalNetwork  = tn.createTotalNetwork(substrateNetwork, ranSlices, tn.vnfCncList, tn.vnfTotalAccList)
            
        if algoType == 1:
            numMappings = tn.algoOneTest(totalNetwork, substrateNetwork, ranSlices, tn.resList, tn.resCapList)
        elif algoType == 2:
            numMappings = tn.algoTwoTest(totalNetwork, tn.vnfCncList)
        elif algoType == 3:
            numMappings = tn.algoThreeTest(totalNetwork, tn.vnfTotalAccList)
        else:
            numMappings = tn.algoFourTest(totalNetwork, substrateNetwork, ranSlices, tn.resCapList, tn.vnfCncList)

        xOne.append(noSbs)
        yOne.append(tn.numVnfFunctions - numMappings)

        substrateNetwork.clear()
        totalNetwork.clear()
        tn.resCapList.clear()
        tn.vnfCncList.clear()
        tn.vnfTotalAccList.clear()
        
        noSbs += intervalFactor
        
    returnData = [xOne, yOne]

    return returnData;

# (3) No. of sbs tow vs No. of Sbs Resources Unused

def testAvailRes(algoType, intervalFactor = 5, iterations = 20):

    noSbs = tn.numSubsNodes

    xOne = []
    yOne = []

    ranSlices = tn.createRANSlice(tn.numRnSlices, tn.numVnfFunctions, tn.resList, tn.resCtPerVnf, 3)

    for ctrVar in range(iterations):
        
        # One
        
        substrateNetwork = tn.createSbsNetwork(noSbs, tn.resCapList, tn.resCtPerSbs, 2)
        totalNetwork  = tn.createTotalNetwork(substrateNetwork, ranSlices, tn.vnfCncList, tn.vnfTotalAccList)
            
        if algoType == 1:
            numMappings = tn.algoOneTest(totalNetwork, substrateNetwork, ranSlices, tn.resList, tn.resCapList)
        elif algoType == 2:
            numMappings = tn.algoTwoTest(totalNetwork, tn.vnfCncList)
        elif algoType == 3:
            numMappings = tn.algoThreeTest(totalNetwork, tn.vnfTotalAccList)
        else:
            numMappings = tn.algoFourTest(totalNetwork, substrateNetwork, ranSlices, tn.resCapList, tn.vnfCncList)

        xOne.append(noSbs)
        resAvail = tn.sbsAvailableRes(totalNetwork)
        yOne.append(resAvail)
        

        substrateNetwork.clear()
        totalNetwork.clear()
        tn.resCapList.clear()
        tn.vnfCncList.clear()
        tn.vnfTotalAccList.clear()
        
        noSbs += intervalFactor

    returnData = [xOne, yOne]

    return returnData;

# (4) No. of sbs tow vs No. of used Sbs

def testExhaustRes(algoType, intervalFactor = 5, iterations = 20):

    noSbs = tn.numSubsNodes

    xOne = []
    yOne = []

    ranSlices = tn.createRANSlice(tn.numRnSlices, tn.numVnfFunctions, tn.resList, tn.resCtPerVnf, 3)

    for ctrVar in range(iterations):
        
        # One
        
        substrateNetwork = tn.createSbsNetwork(noSbs, tn.resCapList, tn.resCtPerSbs, 2)
        totalNetwork  = tn.createTotalNetwork(substrateNetwork, ranSlices, tn.vnfCncList, tn.vnfTotalAccList)
            
        if algoType == 1:
            numMappings = tn.algoOneTest(totalNetwork, substrateNetwork, ranSlices, tn.resList, tn.resCapList)
        elif algoType == 2:
            numMappings = tn.algoTwoTest(totalNetwork, tn.vnfCncList)
        elif algoType == 3:
            numMappings = tn.algoThreeTest(totalNetwork, tn.vnfTotalAccList)
        else:
            numMappings = tn.algoFourTest(totalNetwork, substrateNetwork, ranSlices, tn.resCapList, tn.vnfCncList)

        xOne.append(noSbs)
        resAvail = tn.sbsAvailableRes(totalNetwork)
        yOne.append(noSbs*tn.resCtPerSbs - resAvail)
        

        substrateNetwork.clear()
        totalNetwork.clear()
        tn.resCapList.clear()
        tn.vnfCncList.clear()
        tn.vnfTotalAccList.clear()
        
        noSbs += intervalFactor

    returnData = [xOne, yOne]

    return returnData;


