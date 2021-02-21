import AlgorithmOne as algoOne
import AlgorithmTwo as algoTwo
import AlgorithmThree as algoThree
from graph_tool.all import *
import random
import TotalNetwork as tn
import matplotlib.pyplot as plt

# (1) No. of Connections Sbs vs No. of Succesfull Mapings 

def testSuccMappings(algoType, connectivityVnf):

    connectivity = connectivityVnf

    xOne = []
    yOne = []

    for ctrVar in range(5):
        
        # One
        
        substrateNetwork = tn.createSbsNetwork(tn.numSubsNodes, tn.resCapList, tn.resCtPerSbs, 2)
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

        substrateNetwork.clear()
        ranSlices[0].clear()
        totalNetwork.clear()
        tn.resCapList.clear()
        tn.resList.clear()
        tn.vnfCncList.clear()
        tn.vnfTotalAccList.clear()
        
        connectivity-=1

    returnData = [xOne, yOne]
    return returnData;

# (2) No. of Connections Sbs vs No. of UnSuccesfull Mapings 

def testUnsuccMappings(algoType, connectivityVnf):

    connectivity = connectivityVnf

    xOne = []
    yOne = []

    for ctrVar in range(5):
        
        # One
        
        substrateNetwork = tn.createSbsNetwork(tn.numSubsNodes, tn.resCapList, tn.resCtPerSbs, 2)
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

        substrateNetwork.clear()
        ranSlices[0].clear()
        totalNetwork.clear()
        tn.resCapList.clear()
        tn.resList.clear()
        tn.vnfCncList.clear()
        tn.vnfTotalAccList.clear()
        
        connectivity-=1
        
        returnData = [xOne, yOne]
        return returnData;


# (3) No. of Connections Sbs vs Amount of Sbs. Resouces Unused.

def testAvailRes(algoType, connectivityVnf):

    connectivity = connectivityVnf

    xOne = []
    yOne = []

    for ctrVar in range(5):
        
        # One
        
        substrateNetwork = tn.createSbsNetwork(tn.numSubsNodes, tn.resCapList, tn.resCtPerSbs, 2)
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

        substrateNetwork.clear()
        ranSlices[0].clear()
        totalNetwork.clear()
        tn.resCapList.clear()
        tn.resList.clear()
        tn.vnfCncList.clear()
        tn.vnfTotalAccList.clear()
        
        connectivity-=1

    returnData = [xOne, yOne]
    return returnData;


# (4) No. of Connections Sbs vs Amount of Sbs. Resouces Exhausted

def testExhaustRes(algoType, connectivityVnf):

    connectivity = connectivityVnf

    xOne = []
    yOne = []

    for ctrVar in range(5):
        
        # One
        
        substrateNetwork = tn.createSbsNetwork(tn.numSubsNodes, tn.resCapList, tn.resCtPerSbs, connectivity)
        ranSlices = tn.createRANSlice(tn.numRnSlices, tn.numVnfFunctions, tn.resList, tn.resCtPerVnf, 2)
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

        substrateNetwork.clear()
        ranSlices[0].clear()
        totalNetwork.clear()
        tn.resCapList.clear()
        tn.resList.clear()
        tn.vnfCncList.clear()
        tn.vnfTotalAccList.clear()
        
        connectivity-=1
        
    returnData = [xOne, yOne]
    return returnData;
