import AlgorithmOne as algoOne
import AlgorithmTwo as algoTwo
import AlgorithmThree as algoThree
from graph_tool.all import *
import random
import TotalNetwork as tn
import matplotlib.pyplot as plt

intervalFactor = -1

# (1) No. of Connections Sbs vs No. of Succesfull Mapings 

def testSuccMappings(algoType, connectivityVnf):

    connectivity = connectivityVnf

    xOne = []
    yOne = []

    substrateNetwork = tn.createSbsNetwork(tn.numSubsNodes, tn.resCapList, tn.resCtPerSbs, 3)

    for ctrVar in range(5):
        
        # One
        
        ranSlices = tn.createRANSlice(tn.numRnSlices, tn.numVnfFunctions, tn.resList, tn.resCtPerVnf, connectivity)
        totalNetwork  = tn.createTotalNetwork(substrateNetwork, ranSlices, tn.vnfCncList, tn.vnfTotalAccList)
            
        if algoType == 1:
            numMappings = tn.algoOneTest(totalNetwork, substrateNetwork, ranSlices, tn.resList, tn.resCapList)
        elif algoType == 2:
            numMappings = tn.algoTwoTest(totalNetwork, tn.vnfCncList)
        elif algoType == 3:
            numMappings = tn.algoThreeTest(totalNetwork, tn.vnfTotalAccList)
        else:
            numMappings = tn.algoFourTest(totalNetwork, substrateNetwork, ranSlices, tn.resCapList, tn.vnfCncList)

        xOne.append(connectivity)
        yOne.append(numMappings)

        ranSlices.clear()
        totalNetwork.clear()
        tn.resList.clear()
        tn.vnfCncList.clear()
        tn.vnfTotalAccList.clear()
        
        connectivity+= intervalFactor

    returnData = [xOne, yOne]
    return returnData;

# (2) No. of Connections Sbs vs No. of UnSuccesfull Mapings 

def testUnsuccMappings(algoType, connectivityVnf):

    connectivity = connectivityVnf

    xOne = []
    yOne = []

    substrateNetwork = tn.createSbsNetwork(tn.numSubsNodes, tn.resCapList, tn.resCtPerSbs, 3)

    for ctrVar in range(5):
        
        # One
        
        ranSlices = tn.createRANSlice(tn.numRnSlices, tn.numVnfFunctions, tn.resList, tn.resCtPerVnf, connectivity)
        totalNetwork  = tn.createTotalNetwork(substrateNetwork, ranSlices, tn.vnfCncList, tn.vnfTotalAccList)
            
        if algoType == 1:
            numMappings = tn.algoOneTest(totalNetwork, substrateNetwork, ranSlices, tn.resList, tn.resCapList)
        elif algoType == 2:
            numMappings = tn.algoTwoTest(totalNetwork, tn.vnfCncList)
        elif algoType == 3:
            numMappings = tn.algoThreeTest(totalNetwork, tn.vnfTotalAccList)
        else:
            numMappings = tn.algoFourTest(totalNetwork, substrateNetwork, ranSlices, tn.resCapList, tn.vnfCncList)

        xOne.append(connectivity)
        yOne.append(tn.numVnfFunctions - numMappings)

        ranSlices.clear()
        totalNetwork.clear()
        tn.resList.clear()
        tn.vnfCncList.clear()
        tn.vnfTotalAccList.clear()
        
        connectivity+= intervalFactor
        
    returnData = [xOne, yOne]
    return returnData;


# (3) No. of Connections Sbs vs Amount of Sbs. Resouces Unused.

def testAvailRes(algoType, connectivityVnf):

    connectivity = connectivityVnf

    xOne = []
    yOne = []

    substrateNetwork = tn.createSbsNetwork(tn.numSubsNodes, tn.resCapList, tn.resCtPerSbs, 3)

    for ctrVar in range(5):
        
        # One
        
        ranSlices = tn.createRANSlice(tn.numRnSlices, tn.numVnfFunctions, tn.resList, tn.resCtPerVnf, connectivity)
        totalNetwork  = tn.createTotalNetwork(substrateNetwork, ranSlices, tn.vnfCncList, tn.vnfTotalAccList)
            
        if algoType == 1:
            numMappings = tn.algoOneTest(totalNetwork, substrateNetwork, ranSlices, tn.resList, tn.resCapList)
        elif algoType == 2:
            numMappings = tn.algoTwoTest(totalNetwork, tn.vnfCncList)
        elif algoType == 3:
            numMappings = tn.algoThreeTest(totalNetwork, tn.vnfTotalAccList)
        else:
            numMappings = tn.algoFourTest(totalNetwork, substrateNetwork, ranSlices, tn.resCapList, tn.vnfCncList)
        
        avRes = tn.sbsAvailableRes(totalNetwork)
        xOne.append(connectivity)
        yOne.append(avRes)

        ranSlices.clear()
        totalNetwork.clear()
        tn.resList.clear()
        tn.vnfCncList.clear()
        tn.vnfTotalAccList.clear()
        
        connectivity+= intervalFactor

    returnData = [xOne, yOne]
    return returnData;


# (4) No. of Connections Sbs vs Amount of Sbs. Resouces Exhausted

def testExhaustRes(algoType, connectivityVnf):

    connectivity = connectivityVnf

    xOne = []
    yOne = []

    substrateNetwork = tn.createSbsNetwork(tn.numSubsNodes, tn.resCapList, tn.resCtPerSbs, 3)

    for ctrVar in range(5):
        
        # One
        
        ranSlices = tn.createRANSlice(tn.numRnSlices, tn.numVnfFunctions, tn.resList, tn.resCtPerVnf, connectivity)
        totalNetwork  = tn.createTotalNetwork(substrateNetwork, ranSlices, tn.vnfCncList, tn.vnfTotalAccList)
            
        if algoType == 1:
            numMappings = tn.algoOneTest(totalNetwork, substrateNetwork, ranSlices, tn.resList, tn.resCapList)
        elif algoType == 2:
            numMappings = tn.algoTwoTest(totalNetwork, tn.vnfCncList)
        elif algoType == 3:
            numMappings = tn.algoThreeTest(totalNetwork, tn.vnfTotalAccList)
        else:
            numMappings = tn.algoFourTest(totalNetwork, substrateNetwork, ranSlices, tn.resCapList, tn.vnfCncList)
            
        avRes = tn.sbsAvailableRes(totalNetwork)
        xOne.append(connectivity)
        yOne.append(tn.numSubsNodes*tn.resCtPerSbs - avRes)

        ranSlices.clear()
        totalNetwork.clear()
        tn.resList.clear()
        tn.vnfCncList.clear()
        tn.vnfTotalAccList.clear()
        
        connectivity+= intervalFactor
        
    returnData = [xOne, yOne]
    return returnData;
