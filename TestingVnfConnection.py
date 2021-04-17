import AlgorithmOne as algoOne
import AlgorithmTwo as algoTwo
import AlgorithmThree as algoThree
from graph_tool.all import *
import random
import TotalNetwork as tn
import matplotlib.pyplot as plt

# (1) No. of Connections Sbs vs No. of Succesfull Mapings 

def testSuccMappings(algoType, connectivityVnf= tn.vnfDegree, intervalFactor = tn.intervalFactor, iterations=tn.iterCount):

    connectivity = tn.vnfDegree

    xOne = []
    yOne = []

    substrateNetwork = tn.createSbsNetwork(tn.numSubsNodes, tn.resCapList, tn.resCtPerSbs, connectivity=tn.sbsDegree, random_range=tn.randUpBound)

    for ctrVar in range(iterations):
        
        # One
        
        ranSlices = tn.createRANSlice(tn.numRnSlices, tn.numVnfFunctions, tn.resList, tn.resCtPerVnf, connectivity, random_range=0)
        totalNetwork  = tn.createTotalNetwork(substrateNetwork, ranSlices)
            
        if algoType == 1:
            numMappings = tn.algoOneTest(totalNetwork)
        elif algoType == 2:
            numMappings = tn.algoTwoTest(totalNetwork)
        elif algoType == 3:
            numMappings = tn.algoThreeTest(totalNetwork)
        else:
            numMappings = tn.algoFourTest(totalNetwork)

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

def testUnsuccMappings(algoType, connectivityVnf= tn.vnfDegree, intervalFactor = tn.intervalFactor, iterations=tn.iterCount):

    connectivity = connectivityVnf

    xOne = []
    yOne = []

    substrateNetwork = tn.createSbsNetwork(tn.numSubsNodes, tn.resCapList, tn.resCtPerSbs, connectivity=tn.sbsDegree, random_range=tn.randUpBound)

    for ctrVar in range(iterations):
        
        # One
        
        ranSlices = tn.createRANSlice(tn.numRnSlices, tn.numVnfFunctions, tn.resList, tn.resCtPerVnf, connectivity, random_range=0)
        totalNetwork  = tn.createTotalNetwork(substrateNetwork, ranSlices)
            
        if algoType == 1:
            numMappings = tn.algoOneTest(totalNetwork)
        elif algoType == 2:
            numMappings = tn.algoTwoTest(totalNetwork)
        elif algoType == 3:
            numMappings = tn.algoThreeTest(totalNetwork)
        else:
            numMappings = tn.algoFourTest(totalNetwork)

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

def testAvailRes(algoType, connectivityVnf= tn.vnfDegree, intervalFactor = tn.intervalFactor, iterations=tn.iterCount):

    connectivity = connectivityVnf

    xOne = []
    yOne = []

    substrateNetwork = tn.createSbsNetwork(tn.numSubsNodes, tn.resCapList, tn.resCtPerSbs, connectivity=tn.sbsDegree, random_range=tn.randUpBound)

    for ctrVar in range(iterations):
        
        # One
        
        ranSlices = tn.createRANSlice(tn.numRnSlices, tn.numVnfFunctions, tn.resList, tn.resCtPerVnf, connectivity, random_range=0)
        totalNetwork  = tn.createTotalNetwork(substrateNetwork, ranSlices)
            
        if algoType == 1:
            numMappings = tn.algoOneTest(totalNetwork)
        elif algoType == 2:
            numMappings = tn.algoTwoTest(totalNetwork)
        elif algoType == 3:
            numMappings = tn.algoThreeTest(totalNetwork)
        else:
            numMappings = tn.algoFourTest(totalNetwork)
        
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

def testExhaustRes(algoType, connectivityVnf= tn.vnfDegree, intervalFactor = tn.intervalFactor, iterations=tn.iterCount):

    connectivity = connectivityVnf

    xOne = []
    yOne = []

    substrateNetwork = tn.createSbsNetwork(tn.numSubsNodes, tn.resCapList, tn.resCtPerSbs, connectivity=tn.sbsDegree, random_range=tn.randUpBound)

    for ctrVar in range(iterations):
        
        # One
        
        ranSlices = tn.createRANSlice(tn.numRnSlices, tn.numVnfFunctions, tn.resList, tn.resCtPerVnf, connectivity, random_range=0)
        totalNetwork  = tn.createTotalNetwork(substrateNetwork, ranSlices)
            
        if algoType == 1:
            numMappings = tn.algoOneTest(totalNetwork)
        elif algoType == 2:
            numMappings = tn.algoTwoTest(totalNetwork)
        elif algoType == 3:
            numMappings = tn.algoThreeTest(totalNetwork)
        else:
            numMappings = tn.algoFourTest(totalNetwork)
            
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
