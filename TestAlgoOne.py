import Substrate as sbs
import RAN_Slice as ran
import numpy as np
import AlgorithmOne as algoOne
from graph_tool.all import *
import random
import matplotlib.pyplot as plt
import TotalNetwork as tn

# Substrate Global Variables
numSubsNodes = 100
resCapList = []
resCtPerSbs = 4
substrateNetwork = 0

# RAN Global Variables
ranSlices = []
resList = []
numRnSlices = 1 
numVnfFunctions = 200
resCtPerVnf = 2
vnfCncList = []
vnfTotalAccList = []

# Other Global
totalNetwork = 0

def randomDegreeSbs():
    return random.randint(1, numSubsNodes - 1)

def randomDegreeVnf():
    return random.randint(1, numVnfFunctions - 1)

# substrateNetwork = tn.createSbsNetwork(numSubsNodes, resCapList, resCtPerSbs)
# ranSlices = tn.createRANSlice(numRnSlices, numVnfFunctions, resList, resCtPerVnf)
# totalNetwork  = tn.createTotalNetwork(substrateNetwork, ranSlices, vnfCncList, vnfTotalAccList)

# Testing For X Parameter - Number of Substrate

# (1) no. of sbs vs no. of successfull mappings

# noSbs = numSubsNodes

# xOne = []
# yOne = []
# yTwo = []
# yThree = []

# for ctrVar in range(5):
    
#     # One
    
#     substrateNetwork = tn.createSbsNetwork(noSbs, resCapList, resCtPerSbs)
#     ranSlices = tn.createRANSlice(numRnSlices, numVnfFunctions, resList, resCtPerVnf)
#     totalNetwork  = tn.createTotalNetwork(substrateNetwork, ranSlices, vnfCncList, vnfTotalAccList)
        
#     numMappings = tn.algoOneTest(totalNetwork, substrateNetwork, ranSlices, resList, resCapList)
#     xOne.append(noSbs)
#     yOne.append(numMappings)

#     substrateNetwork.clear()
#     ranSlices[0].clear()
#     totalNetwork.clear()
#     resCapList.clear()
#     resList.clear()
#     vnfCncList.clear()
#     vnfTotalAccList.clear()
    
#     # Two
    
#     substrateNetwork = tn.createSbsNetwork(noSbs, resCapList, resCtPerSbs)
#     ranSlices = tn.createRANSlice(numRnSlices, numVnfFunctions, resList, resCtPerVnf)
#     totalNetwork  = tn.createTotalNetwork(substrateNetwork, ranSlices, vnfCncList, vnfTotalAccList)
        
#     numMappings = tn.algoTwoTest(totalNetwork, vnfCncList)
#     yTwo.append(numMappings)

#     substrateNetwork.clear()
#     ranSlices[0].clear()
#     totalNetwork.clear()
#     resCapList.clear()
#     resList.clear()
#     vnfCncList.clear()
#     vnfTotalAccList.clear()
    
#     # Three
    
#     substrateNetwork = tn.createSbsNetwork(noSbs, resCapList, resCtPerSbs)
#     ranSlices = tn.createRANSlice(numRnSlices, numVnfFunctions, resList, resCtPerVnf)
#     totalNetwork  = tn.createTotalNetwork(substrateNetwork, ranSlices, vnfCncList, vnfTotalAccList)
        
#     numMappings = tn.algoThreeTest(totalNetwork, vnfTotalAccList)
#     yThree.append(numMappings)

#     substrateNetwork.clear()
#     ranSlices[0].clear()
#     totalNetwork.clear()
#     resCapList.clear()
#     resList.clear()
#     vnfCncList.clear()
#     vnfTotalAccList.clear()
    
#     noSbs += 15
    
    

# print(xOne)
# print(yOne)
# print(yTwo)
# print(yThree)

# fig, ax = plt.subplots()
# ax.plot(xOne, yOne, label="Algo One", linestyle='-')
# ax.plot(xOne, yTwo, label="Algo Two", linestyle='--')
# ax.plot(xOne, yThree, label="Algo Three", linestyle=':')

# ax.set(xlabel='Number of Sbs', ylabel='Number of Successfull Mappings',
# title='Number of Sbs Test')
# ax.grid()
# ax.legend(loc="best")

# fig.savefig("ResultsOne/sbsOne.png")
# plt.show()

# (2) no. of sbs vs no. of unsuccesfull mappings

# noSbs = numSubsNodes

# xOne = []
# yOne = []
# yTwo = []
# yThree = []

# for ctrVar in range(5):
    
#     # One
    
#     substrateNetwork = tn.createSbsNetwork(noSbs, resCapList, resCtPerSbs)
#     ranSlices = tn.createRANSlice(numRnSlices, numVnfFunctions, resList, resCtPerVnf)
#     totalNetwork  = tn.createTotalNetwork(substrateNetwork, ranSlices, vnfCncList, vnfTotalAccList)
        
#     numMappings = tn.algoOneTest(totalNetwork, substrateNetwork, ranSlices, resList, resCapList)
#     xOne.append(noSbs)
#     yOne.append(numVnfFunctions - numMappings)

#     substrateNetwork.clear()
#     ranSlices[0].clear()
#     totalNetwork.clear()
#     resCapList.clear()
#     resList.clear()
#     vnfCncList.clear()
#     vnfTotalAccList.clear()
    
#     # Two
    
#     substrateNetwork = tn.createSbsNetwork(noSbs, resCapList, resCtPerSbs)
#     ranSlices = tn.createRANSlice(numRnSlices, numVnfFunctions, resList, resCtPerVnf)
#     totalNetwork  = tn.createTotalNetwork(substrateNetwork, ranSlices, vnfCncList, vnfTotalAccList)
        
#     numMappings = tn.algoTwoTest(totalNetwork, vnfCncList)
#     yTwo.append(numVnfFunctions - numMappings)

#     substrateNetwork.clear()
#     ranSlices[0].clear()
#     totalNetwork.clear()
#     resCapList.clear()
#     resList.clear()
#     vnfCncList.clear()
#     vnfTotalAccList.clear()
    
#     # Three
    
#     substrateNetwork = tn.createSbsNetwork(noSbs, resCapList, resCtPerSbs)
#     ranSlices = tn.createRANSlice(numRnSlices, numVnfFunctions, resList, resCtPerVnf)
#     totalNetwork  = tn.createTotalNetwork(substrateNetwork, ranSlices, vnfCncList, vnfTotalAccList)
        
#     numMappings = tn.algoThreeTest(totalNetwork, vnfTotalAccList)
#     yThree.append(numVnfFunctions - numMappings)

#     substrateNetwork.clear()
#     ranSlices[0].clear()
#     totalNetwork.clear()
#     resCapList.clear()
#     resList.clear()
#     vnfCncList.clear()
#     vnfTotalAccList.clear()
    
#     noSbs += 15
    
    

# print(xOne)
# print(yOne)
# print(yTwo)
# print(yThree)

# fig, ax = plt.subplots()
# ax.plot(xOne, yOne, label="Algo One", linestyle='-')
# ax.plot(xOne, yTwo, label="Algo Two", linestyle='--')
# ax.plot(xOne, yThree, label="Algo Three", linestyle=':')

# ax.set(xlabel='Number of Sbs', ylabel='Number of Unsuccessfull Mappings',
# title='Number of Sbs Test')
# ax.grid()
# ax.legend(loc="best")

# fig.savefig("ResultsOne/sbsTwo.png")
# plt.show()

# (3) No. of sbs tow vs No. of Sbs Resources Unused

# noSbs = numSubsNodes

# xOne = []
# yOne = []
# yTwo = []
# yThree = []

# for ctrVar in range(5):
    
#     # One
    
#     substrateNetwork = tn.createSbsNetwork(noSbs, resCapList, resCtPerSbs)
#     ranSlices = tn.createRANSlice(numRnSlices, numVnfFunctions, resList, resCtPerVnf)
#     totalNetwork  = tn.createTotalNetwork(substrateNetwork, ranSlices, vnfCncList, vnfTotalAccList)
        
#     numMappings = tn.algoOneTest(totalNetwork, substrateNetwork, ranSlices, resList, resCapList)
#     xOne.append(noSbs)
#     resAvail = tn.sbsAvailableRes(totalNetwork)
#     yOne.append(resAvail)
    

#     substrateNetwork.clear()
#     ranSlices[0].clear()
#     totalNetwork.clear()
#     resCapList.clear()
#     resList.clear()
#     vnfCncList.clear()
#     vnfTotalAccList.clear()
    
#     # Two
    
#     substrateNetwork = tn.createSbsNetwork(noSbs, resCapList, resCtPerSbs)
#     ranSlices = tn.createRANSlice(numRnSlices, numVnfFunctions, resList, resCtPerVnf)
#     totalNetwork  = tn.createTotalNetwork(substrateNetwork, ranSlices, vnfCncList, vnfTotalAccList)
        
#     numMappings = tn.algoTwoTest(totalNetwork, vnfCncList)
#     resAvail = tn.sbsAvailableRes(totalNetwork)
#     yTwo.append(resAvail)

#     substrateNetwork.clear()
#     ranSlices[0].clear()
#     totalNetwork.clear()
#     resCapList.clear()
#     resList.clear()
#     vnfCncList.clear()
#     vnfTotalAccList.clear()
    
#     # Three
    
#     substrateNetwork = tn.createSbsNetwork(noSbs, resCapList, resCtPerSbs)
#     ranSlices = tn.createRANSlice(numRnSlices, numVnfFunctions, resList, resCtPerVnf)
#     totalNetwork  = tn.createTotalNetwork(substrateNetwork, ranSlices, vnfCncList, vnfTotalAccList)
        
#     numMappings = tn.algoThreeTest(totalNetwork, vnfTotalAccList)
#     resAvail = tn.sbsAvailableRes(totalNetwork)
#     yThree.append(resAvail)

#     substrateNetwork.clear()
#     ranSlices[0].clear()
#     totalNetwork.clear()
#     resCapList.clear()
#     resList.clear()
#     vnfCncList.clear()
#     vnfTotalAccList.clear()
    
#     noSbs += 15
    
    

# print(xOne)
# print(yOne)
# print(yTwo)
# print(yThree)

# fig, ax = plt.subplots()
# ax.plot(xOne, yOne, label="Algo One", linestyle='-')
# ax.plot(xOne, yTwo, label="Algo Two", linestyle='--')
# ax.plot(xOne, yThree, label="Algo Three", linestyle=':')

# ax.set(xlabel='Number of Sbs', ylabel='Amount of Unused Substrate Resources',
# title='Number of Sbs Test')
# ax.grid()
# ax.legend(loc="best")

# fig.savefig("ResultsOne/sbsThree.png")
# plt.show()

# (4) No. of sbs tow vs No. of used Sbs

noSbs = numSubsNodes

xOne = []
yOne = []
yTwo = []
yThree = []

for ctrVar in range(5):
    
    # One
    
    substrateNetwork = tn.createSbsNetwork(noSbs, resCapList, resCtPerSbs)
    ranSlices = tn.createRANSlice(numRnSlices, numVnfFunctions, resList, resCtPerVnf)
    totalNetwork  = tn.createTotalNetwork(substrateNetwork, ranSlices, vnfCncList, vnfTotalAccList)
        
    numMappings = tn.algoOneTest(totalNetwork, substrateNetwork, ranSlices, resList, resCapList)
    xOne.append(noSbs)
    resAvail = tn.sbsAvailableRes(totalNetwork)
    yOne.append(noSbs*resCtPerSbs - resAvail)
    

    substrateNetwork.clear()
    ranSlices[0].clear()
    totalNetwork.clear()
    resCapList.clear()
    resList.clear()
    vnfCncList.clear()
    vnfTotalAccList.clear()
    
    # Two
    
    substrateNetwork = tn.createSbsNetwork(noSbs, resCapList, resCtPerSbs)
    ranSlices = tn.createRANSlice(numRnSlices, numVnfFunctions, resList, resCtPerVnf)
    totalNetwork  = tn.createTotalNetwork(substrateNetwork, ranSlices, vnfCncList, vnfTotalAccList)
        
    numMappings = tn.algoTwoTest(totalNetwork, vnfCncList)
    resAvail = tn.sbsAvailableRes(totalNetwork)
    yTwo.append(noSbs*resCtPerSbs - resAvail)

    substrateNetwork.clear()
    ranSlices[0].clear()
    totalNetwork.clear()
    resCapList.clear()
    resList.clear()
    vnfCncList.clear()
    vnfTotalAccList.clear()
    
    # Three
    
    substrateNetwork = tn.createSbsNetwork(noSbs, resCapList, resCtPerSbs)
    ranSlices = tn.createRANSlice(numRnSlices, numVnfFunctions, resList, resCtPerVnf)
    totalNetwork  = tn.createTotalNetwork(substrateNetwork, ranSlices, vnfCncList, vnfTotalAccList)
        
    numMappings = tn.algoThreeTest(totalNetwork, vnfTotalAccList)
    resAvail = tn.sbsAvailableRes(totalNetwork)
    yThree.append(noSbs*resCtPerSbs - resAvail)

    substrateNetwork.clear()
    ranSlices[0].clear()
    totalNetwork.clear()
    resCapList.clear()
    resList.clear()
    vnfCncList.clear()
    vnfTotalAccList.clear()
    
    noSbs += 15
    
    

print(xOne)
print(yOne)
print(yTwo)
print(yThree)

# fig, ax = plt.subplots()
# ax.plot(xOne, yOne, label="Algo One", linestyle='-')
# ax.plot(xOne, yTwo, label="Algo Two", linestyle='--')
# ax.plot(xOne, yThree, label="Algo Three", linestyle=':')

# ax.set(xlabel='Number of Sbs', ylabel='Amount of Used Substrate Resources',
# title='Number of Sbs Test')
# ax.grid()
# ax.legend(loc="best")

# fig.savefig("ResultsOne/sbsFour.png")
# plt.show()

# # (1) No. of vnf vs No. of succesfull mappings

# noVnf = numVnfFunctions

# xOne = []
# yOne = []
# yTwo = []
# yThree = []

# for ctrVar in range(5):
    
#     # One
    
#     substrateNetwork = tn.createSbsNetwork(numSubsNodes, resCapList, resCtPerSbs)
#     ranSlices = tn.createRANSlice(numRnSlices, noVnf, resList, resCtPerVnf)
#     totalNetwork  = tn.createTotalNetwork(substrateNetwork, ranSlices, vnfCncList, vnfTotalAccList)
        
#     numMappings = tn.algoOneTest(totalNetwork, substrateNetwork, ranSlices, resList, resCapList)
#     xOne.append(noVnf)
#     yOne.append(numMappings)

#     substrateNetwork.clear()
#     ranSlices[0].clear()
#     totalNetwork.clear()
#     resCapList.clear()
#     resList.clear()
#     vnfCncList.clear()
#     vnfTotalAccList.clear()
    
#     # Two
    
#     substrateNetwork = tn.createSbsNetwork(numSubsNodes, resCapList, resCtPerSbs)
#     ranSlices = tn.createRANSlice(numRnSlices, noVnf, resList, resCtPerVnf)
#     totalNetwork  = tn.createTotalNetwork(substrateNetwork, ranSlices, vnfCncList, vnfTotalAccList)
        
#     numMappings = tn.algoTwoTest(totalNetwork, vnfCncList)
#     yTwo.append(numMappings)

#     substrateNetwork.clear()
#     ranSlices[0].clear()
#     totalNetwork.clear()
#     resCapList.clear()
#     resList.clear()
#     vnfCncList.clear()
#     vnfTotalAccList.clear()
    
#     # Three
    
#     substrateNetwork = tn.createSbsNetwork(numSubsNodes, resCapList, resCtPerSbs)
#     ranSlices = tn.createRANSlice(numRnSlices, noVnf, resList, resCtPerVnf)
#     totalNetwork  = tn.createTotalNetwork(substrateNetwork, ranSlices, vnfCncList, vnfTotalAccList)
        
#     numMappings = tn.algoThreeTest(totalNetwork, vnfTotalAccList)
#     yThree.append(numMappings)

#     substrateNetwork.clear()
#     ranSlices[0].clear()
#     totalNetwork.clear()
#     resCapList.clear()
#     resList.clear()
#     vnfCncList.clear()
#     vnfTotalAccList.clear()
    
#     noVnf += 150
    
    

# print(xOne)
# print(yOne)
# print(yTwo)
# print(yThree)

# fig, ax = plt.subplots()
# ax.plot(xOne, yOne, label="Algo One", linestyle='-')
# ax.plot(xOne, yTwo, label="Algo Two", linestyle='--')
# ax.plot(xOne, yThree, label="Algo Three", linestyle=':')

# ax.set(xlabel='Number of VNFs', ylabel='Number of Successful Mappings',
# title='Number of VNF Test')
# ax.grid()
# ax.legend(loc="best")

# fig.savefig("ResultsTwo/vnfOne.png")
# plt.show()

#(2) No. of vnf vs No. of unsuccesfull mappings

# noVnf = numVnfFunctions

# xOne = []
# yOne = []
# yTwo = []
# yThree = []

# for ctrVar in range(5):
    
#     # One
    
#     substrateNetwork = tn.createSbsNetwork(numSubsNodes, resCapList, resCtPerSbs)
#     ranSlices = tn.createRANSlice(numRnSlices, noVnf, resList, resCtPerVnf)
#     totalNetwork  = tn.createTotalNetwork(substrateNetwork, ranSlices, vnfCncList, vnfTotalAccList)
        
#     numMappings = tn.algoOneTest(totalNetwork, substrateNetwork, ranSlices, resList, resCapList)
#     xOne.append(noVnf)
#     yOne.append(noVnf - numMappings)

#     substrateNetwork.clear()
#     ranSlices[0].clear()
#     totalNetwork.clear()
#     resCapList.clear()
#     resList.clear()
#     vnfCncList.clear()
#     vnfTotalAccList.clear()
    
#     # Two
    
#     substrateNetwork = tn.createSbsNetwork(numSubsNodes, resCapList, resCtPerSbs)
#     ranSlices = tn.createRANSlice(numRnSlices, noVnf, resList, resCtPerVnf)
#     totalNetwork  = tn.createTotalNetwork(substrateNetwork, ranSlices, vnfCncList, vnfTotalAccList)
        
#     numMappings = tn.algoTwoTest(totalNetwork, vnfCncList)
#     yTwo.append(noVnf - numMappings)

#     substrateNetwork.clear()
#     ranSlices[0].clear()
#     totalNetwork.clear()
#     resCapList.clear()
#     resList.clear()
#     vnfCncList.clear()
#     vnfTotalAccList.clear()
    
#     # Three
    
#     substrateNetwork = tn.createSbsNetwork(numSubsNodes, resCapList, resCtPerSbs)
#     ranSlices = tn.createRANSlice(numRnSlices, noVnf, resList, resCtPerVnf)
#     totalNetwork  = tn.createTotalNetwork(substrateNetwork, ranSlices, vnfCncList, vnfTotalAccList)
        
#     numMappings = tn.algoThreeTest(totalNetwork, vnfTotalAccList)
#     yThree.append(noVnf - numMappings)

#     substrateNetwork.clear()
#     ranSlices[0].clear()
#     totalNetwork.clear()
#     resCapList.clear()
#     resList.clear()
#     vnfCncList.clear()
#     vnfTotalAccList.clear()
    
#     noVnf += 150
    
    

# print(xOne)
# print(yOne)
# print(yTwo)
# print(yThree)

# fig, ax = plt.subplots()
# ax.plot(xOne, yOne, label="Algo One", linestyle='-')
# ax.plot(xOne, yTwo, label="Algo Two", linestyle='--')
# ax.plot(xOne, yThree, label="Algo Three", linestyle=':')

# ax.set(xlabel='Number of VNFs', ylabel='Number of Unsuccessful Mappings',
# title='Number of VNF Test')
# ax.grid()
# ax.legend(loc="best")

# fig.savefig("ResultsTwo/vnfTwo.png")
# plt.show()


# (3) No. of vnf vs No. of Available Substrate Resources

# noVnf = numVnfFunctions

# xOne = []
# yOne = []
# yTwo = []
# yThree = []

# for ctrVar in range(5):
    
#     # One
    
#     substrateNetwork = tn.createSbsNetwork(numSubsNodes, resCapList, resCtPerSbs)
#     ranSlices = tn.createRANSlice(numRnSlices, noVnf, resList, resCtPerVnf)
#     totalNetwork  = tn.createTotalNetwork(substrateNetwork, ranSlices, vnfCncList, vnfTotalAccList)
        
#     numMappings = tn.algoOneTest(totalNetwork, substrateNetwork, ranSlices, resList, resCapList)
#     xOne.append(noVnf)
#     resAvail = tn.sbsAvailableRes(totalNetwork)
#     yOne.append(resAvail)

#     substrateNetwork.clear()
#     ranSlices[0].clear()
#     totalNetwork.clear()
#     resCapList.clear()
#     resList.clear()
#     vnfCncList.clear()
#     vnfTotalAccList.clear()
    
#     # Two
    
#     substrateNetwork = tn.createSbsNetwork(numSubsNodes, resCapList, resCtPerSbs)
#     ranSlices = tn.createRANSlice(numRnSlices, noVnf, resList, resCtPerVnf)
#     totalNetwork  = tn.createTotalNetwork(substrateNetwork, ranSlices, vnfCncList, vnfTotalAccList)
        
#     numMappings = tn.algoTwoTest(totalNetwork, vnfCncList)
#     esAvail = tn.sbsAvailableRes(totalNetwork)
#     yTwo.append(resAvail)

#     substrateNetwork.clear()
#     ranSlices[0].clear()
#     totalNetwork.clear()
#     resCapList.clear()
#     resList.clear()
#     vnfCncList.clear()
#     vnfTotalAccList.clear()
    
#     # Three
    
#     substrateNetwork = tn.createSbsNetwork(numSubsNodes, resCapList, resCtPerSbs)
#     ranSlices = tn.createRANSlice(numRnSlices, noVnf, resList, resCtPerVnf)
#     totalNetwork  = tn.createTotalNetwork(substrateNetwork, ranSlices, vnfCncList, vnfTotalAccList)
        
#     numMappings = tn.algoThreeTest(totalNetwork, vnfTotalAccList)
#     resAvail = tn.sbsAvailableRes(totalNetwork)
#     yThree.append(resAvail)

#     substrateNetwork.clear()
#     ranSlices[0].clear()
#     totalNetwork.clear()
#     resCapList.clear()
#     resList.clear()
#     vnfCncList.clear()
#     vnfTotalAccList.clear()
    
#     noVnf += 150
    
    

# print(xOne)
# print(yOne)
# print(yTwo)
# print(yThree)

# fig, ax = plt.subplots()
# ax.plot(xOne, yOne, label="Algo One", linestyle='-')
# ax.plot(xOne, yTwo, label="Algo Two", linestyle='--')
# ax.plot(xOne, yThree, label="Algo Three", linestyle=':')

# ax.set(xlabel='Number of VNFs', ylabel='Amount of Substrate Resources Unused',
# title='Number of VNF Test')
# ax.grid()
# ax.legend(loc="best")

# fig.savefig("ResultsTwo/vnfThree.png")
# plt.show()

# (4) No. of vnf vs Amount of Exhausted Substrate Resources

# noVnf = numVnfFunctions

# xOne = []
# yOne = []
# yTwo = []
# yThree = []

# for ctrVar in range(5):
    
#     # One
    
#     substrateNetwork = tn.createSbsNetwork(numSubsNodes, resCapList, resCtPerSbs)
#     ranSlices = tn.createRANSlice(numRnSlices, noVnf, resList, resCtPerVnf)
#     totalNetwork  = tn.createTotalNetwork(substrateNetwork, ranSlices, vnfCncList, vnfTotalAccList)
        
#     numMappings = tn.algoOneTest(totalNetwork, substrateNetwork, ranSlices, resList, resCapList)
#     xOne.append(noVnf)
#     resAvail = tn.sbsAvailableRes(totalNetwork)
#     yOne.append(numSubsNodes*resCtPerSbs - resAvail)

#     substrateNetwork.clear()
#     ranSlices[0].clear()
#     totalNetwork.clear()
#     resCapList.clear()
#     resList.clear()
#     vnfCncList.clear()
#     vnfTotalAccList.clear()
    
#     # Two
    
#     substrateNetwork = tn.createSbsNetwork(numSubsNodes, resCapList, resCtPerSbs)
#     ranSlices = tn.createRANSlice(numRnSlices, noVnf, resList, resCtPerVnf)
#     totalNetwork  = tn.createTotalNetwork(substrateNetwork, ranSlices, vnfCncList, vnfTotalAccList)
        
#     numMappings = tn.algoTwoTest(totalNetwork, vnfCncList)
#     esAvail = tn.sbsAvailableRes(totalNetwork)
#     yTwo.append(numSubsNodes*resCtPerSbs - resAvail)

#     substrateNetwork.clear()
#     ranSlices[0].clear()
#     totalNetwork.clear()
#     resCapList.clear()
#     resList.clear()
#     vnfCncList.clear()
#     vnfTotalAccList.clear()
    
#     # Three
    
#     substrateNetwork = tn.createSbsNetwork(numSubsNodes, resCapList, resCtPerSbs)
#     ranSlices = tn.createRANSlice(numRnSlices, noVnf, resList, resCtPerVnf)
#     totalNetwork  = tn.createTotalNetwork(substrateNetwork, ranSlices, vnfCncList, vnfTotalAccList)
        
#     numMappings = tn.algoThreeTest(totalNetwork, vnfTotalAccList)
#     resAvail = tn.sbsAvailableRes(totalNetwork)
#     yThree.append(numSubsNodes*resCtPerSbs - resAvail)

#     substrateNetwork.clear()
#     ranSlices[0].clear()
#     totalNetwork.clear()
#     resCapList.clear()
#     resList.clear()
#     vnfCncList.clear()
#     vnfTotalAccList.clear()
    
#     noVnf += 150
    
    

# print(xOne)
# print(yOne)
# print(yTwo)
# print(yThree)

# fig, ax = plt.subplots()
# ax.plot(xOne, yOne, label="Algo One", linestyle='-')
# ax.plot(xOne, yTwo, label="Algo Two", linestyle='--')
# ax.plot(xOne, yThree, label="Algo Three", linestyle=':')

# ax.set(xlabel='Number of VNFs', ylabel='Amount of Substrate Resources Exhausted',
# title='Number of VNF Test')
# ax.grid()
# ax.legend(loc="best")

# fig.savefig("ResultsTwo/vnfFour.png")
# plt.show()

#---------------------------------------------------------------------------------------------------

# (1) No. of Connections Sbs vs No. of Succesfull Mapings 

# connectivity = 8

# xOne = []
# yOne = []
# yTwo = []
# yThree = []

# for ctrVar in range(5):
    
#     # One
    
#     substrateNetwork = tn.createSbsNetwork(numSubsNodes, resCapList, resCtPerSbs, connectivity)
#     ranSlices = tn.createRANSlice(numRnSlices, numVnfFunctions, resList, resCtPerVnf)
#     totalNetwork  = tn.createTotalNetwork(substrateNetwork, ranSlices, vnfCncList, vnfTotalAccList)
        
#     numMappings = tn.algoOneTest(totalNetwork, substrateNetwork, ranSlices, resList, resCapList)
#     xOne.append(connectivity)
#     yOne.append(numMappings)

#     substrateNetwork.clear()
#     ranSlices[0].clear()
#     totalNetwork.clear()
#     resCapList.clear()
#     resList.clear()
#     vnfCncList.clear()
#     vnfTotalAccList.clear()
    
#     # Two
    
#     substrateNetwork = tn.createSbsNetwork(numSubsNodes, resCapList, resCtPerSbs, connectivity)
#     ranSlices = tn.createRANSlice(numRnSlices, numVnfFunctions, resList, resCtPerVnf)
#     totalNetwork  = tn.createTotalNetwork(substrateNetwork, ranSlices, vnfCncList, vnfTotalAccList)
        
#     numMappings = tn.algoTwoTest(totalNetwork, vnfCncList)
#     yTwo.append(numMappings)

#     substrateNetwork.clear()
#     ranSlices[0].clear()
#     totalNetwork.clear()
#     resCapList.clear()
#     resList.clear()
#     vnfCncList.clear()
#     vnfTotalAccList.clear()
    
#     # Three
    
#     substrateNetwork = tn.createSbsNetwork(numSubsNodes, resCapList, resCtPerSbs, connectivity)
#     ranSlices = tn.createRANSlice(numRnSlices, numVnfFunctions, resList, resCtPerVnf)
#     totalNetwork  = tn.createTotalNetwork(substrateNetwork, ranSlices, vnfCncList, vnfTotalAccList)
        
#     numMappings = tn.algoThreeTest(totalNetwork, vnfTotalAccList)
#     yThree.append(numMappings)

#     substrateNetwork.clear()
#     ranSlices[0].clear()
#     totalNetwork.clear()
#     resCapList.clear()
#     resList.clear()
#     vnfCncList.clear()
#     vnfTotalAccList.clear()
    
#     connectivity-=1
    
    

# print(xOne)
# print(yOne)
# print(yTwo)
# print(yThree)

# fig, ax = plt.subplots()
# ax.plot(xOne, yOne, label="Algo One", linestyle='-')
# ax.plot(xOne, yTwo, label="Algo Two", linestyle='--')
# ax.plot(xOne, yThree, label="Algo Three", linestyle=':')

# ax.set(xlabel='Degree of Substrate Tower', ylabel='Number of Successful Mappings',
# title='Connectivity Test')
# ax.grid()
# ax.legend(loc="best")

# fig.savefig("ResultsThree/conOne.png")
# plt.show()

# (2) No. of Connections Sbs vs No. of UnSuccesfull Mapings 

# connectivity = 8

# xOne = []
# yOne = []
# yTwo = []
# yThree = []

# for ctrVar in range(5):
    
#     # One
    
#     substrateNetwork = tn.createSbsNetwork(numSubsNodes, resCapList, resCtPerSbs, connectivity)
#     ranSlices = tn.createRANSlice(numRnSlices, numVnfFunctions, resList, resCtPerVnf)
#     totalNetwork  = tn.createTotalNetwork(substrateNetwork, ranSlices, vnfCncList, vnfTotalAccList)
        
#     numMappings = tn.algoOneTest(totalNetwork, substrateNetwork, ranSlices, resList, resCapList)
#     xOne.append(connectivity)
#     yOne.append(numVnfFunctions - numMappings)

#     substrateNetwork.clear()
#     ranSlices[0].clear()
#     totalNetwork.clear()
#     resCapList.clear()
#     resList.clear()
#     vnfCncList.clear()
#     vnfTotalAccList.clear()
    
#     # Two
    
#     substrateNetwork = tn.createSbsNetwork(numSubsNodes, resCapList, resCtPerSbs, connectivity)
#     ranSlices = tn.createRANSlice(numRnSlices, numVnfFunctions, resList, resCtPerVnf)
#     totalNetwork  = tn.createTotalNetwork(substrateNetwork, ranSlices, vnfCncList, vnfTotalAccList)
        
#     numMappings = tn.algoTwoTest(totalNetwork, vnfCncList)
#     yTwo.append(numVnfFunctions - numMappings)

#     substrateNetwork.clear()
#     ranSlices[0].clear()
#     totalNetwork.clear()
#     resCapList.clear()
#     resList.clear()
#     vnfCncList.clear()
#     vnfTotalAccList.clear()
    
#     # Three
    
#     substrateNetwork = tn.createSbsNetwork(numSubsNodes, resCapList, resCtPerSbs, connectivity)
#     ranSlices = tn.createRANSlice(numRnSlices, numVnfFunctions, resList, resCtPerVnf)
#     totalNetwork  = tn.createTotalNetwork(substrateNetwork, ranSlices, vnfCncList, vnfTotalAccList)
        
#     numMappings = tn.algoThreeTest(totalNetwork, vnfTotalAccList)
#     yThree.append(numVnfFunctions - numMappings)

#     substrateNetwork.clear()
#     ranSlices[0].clear()
#     totalNetwork.clear()
#     resCapList.clear()
#     resList.clear()
#     vnfCncList.clear()
#     vnfTotalAccList.clear()
    
#     connectivity-=1
    

# print(xOne)
# print(yOne)
# print(yTwo)
# print(yThree)

# fig, ax = plt.subplots()
# ax.plot(xOne, yOne, label="Algo One", linestyle='-')
# ax.plot(xOne, yTwo, label="Algo Two", linestyle='--')
# ax.plot(xOne, yThree, label="Algo Three", linestyle=':')

# ax.set(xlabel='Degree of Substrate Tower', ylabel='Number of Unuccessful Mappings',
# title='Connectivity Test')
# ax.grid()
# ax.legend(loc="best")

# fig.savefig("ResultsThree/conTwo.png")
# plt.show()


# (3) No. of Connections Sbs vs Amount of Sbs. Resouces Unused.

# connectivity = 8

# xOne = []
# yOne = []
# yTwo = []
# yThree = []

# for ctrVar in range(5):
    
#     # One
    
#     substrateNetwork = tn.createSbsNetwork(numSubsNodes, resCapList, resCtPerSbs, connectivity)
#     ranSlices = tn.createRANSlice(numRnSlices, numVnfFunctions, resList, resCtPerVnf, 2)
#     totalNetwork  = tn.createTotalNetwork(substrateNetwork, ranSlices, vnfCncList, vnfTotalAccList)
        
#     numMappings = tn.algoOneTest(totalNetwork, substrateNetwork, ranSlices, resList, resCapList)
#     avRes = tn.sbsAvailableRes(totalNetwork)
#     yOne.append(avRes)

#     substrateNetwork.clear()
#     ranSlices[0].clear()
#     totalNetwork.clear()
#     resCapList.clear()
#     resList.clear()
#     vnfCncList.clear()
#     vnfTotalAccList.clear()
    
#     # Two
    
#     substrateNetwork = tn.createSbsNetwork(numSubsNodes, resCapList, resCtPerSbs, connectivity)
#     ranSlices = tn.createRANSlice(numRnSlices, numVnfFunctions, resList, resCtPerVnf, 2)
#     totalNetwork  = tn.createTotalNetwork(substrateNetwork, ranSlices, vnfCncList, vnfTotalAccList)
        
#     numMappings = tn.algoTwoTest(totalNetwork, vnfCncList)
#     yavRes = tn.sbsAvailableRes(totalNetwork)
#     yTwo.append(avRes)

#     substrateNetwork.clear()
#     ranSlices[0].clear()
#     totalNetwork.clear()
#     resCapList.clear()
#     resList.clear()
#     vnfCncList.clear()
#     vnfTotalAccList.clear()
    
#     # Three
    
#     substrateNetwork = tn.createSbsNetwork(numSubsNodes, resCapList, resCtPerSbs, connectivity)
#     ranSlices = tn.createRANSlice(numRnSlices, numVnfFunctions, resList, resCtPerVnf, 2)
#     totalNetwork  = tn.createTotalNetwork(substrateNetwork, ranSlices, vnfCncList, vnfTotalAccList)
        
#     numMappings = tn.algoThreeTest(totalNetwork, vnfTotalAccList)
#     avRes = tn.sbsAvailableRes(totalNetwork)
#     yThree.append(avRes)

#     substrateNetwork.clear()
#     ranSlices[0].clear()
#     totalNetwork.clear()
#     resCapList.clear()
#     resList.clear()
#     vnfCncList.clear()
#     vnfTotalAccList.clear()
    
#     connectivity-=1
    
    
# print(xOne)
# print(yOne)
# print(yTwo)
# print(yThree)

# x1 = np.array(xOne)
# y1 = np.array(yOne)
# y2 = np.array(yTwo)
# y3 = np.array(yThree)

# fig, ax = plt.subplots()
# ax.plot(x1, y1, label="Algo One", linestyle='-')
# ax.plot(x1, y2, label="Algo Two", linestyle='--')
# ax.plot(x1, y3, label="Algo Three", linestyle=':')

# ax.set(xlabel='Degree of Substrate Tower', ylabel='Amount of Substrate Resources Available',
# title='Connectivity Test')
# ax.grid()
# ax.legend(loc="best")

# fig.savefig("ResultsThree/conThree.png")
# plt.show()


# (4) No. of Connections Sbs vs Amount of Sbs. Resouces Exhausted


connectivity = 8

xOne = []
yOne = []
yTwo = []
yThree = []

for ctrVar in range(5):
    
    # One
    
    substrateNetwork = tn.createSbsNetwork(numSubsNodes, resCapList, resCtPerSbs, connectivity)
    ranSlices = tn.createRANSlice(numRnSlices, numVnfFunctions, resList, resCtPerVnf, 2)
    totalNetwork  = tn.createTotalNetwork(substrateNetwork, ranSlices, vnfCncList, vnfTotalAccList)
        
    numMappings = tn.algoOneTest(totalNetwork, substrateNetwork, ranSlices, resList, resCapList)
    avRes = tn.sbsAvailableRes(totalNetwork)
    yOne.append(numSubsNodes*resCtPerSbs - avRes)

    substrateNetwork.clear()
    ranSlices[0].clear()
    totalNetwork.clear()
    resCapList.clear()
    resList.clear()
    vnfCncList.clear()
    vnfTotalAccList.clear()
    
    # Two
    
    substrateNetwork = tn.createSbsNetwork(numSubsNodes, resCapList, resCtPerSbs, connectivity)
    ranSlices = tn.createRANSlice(numRnSlices, numVnfFunctions, resList, resCtPerVnf, 2)
    totalNetwork  = tn.createTotalNetwork(substrateNetwork, ranSlices, vnfCncList, vnfTotalAccList)
        
    numMappings = tn.algoTwoTest(totalNetwork, vnfCncList)
    yavRes = tn.sbsAvailableRes(totalNetwork)
    yTwo.append(numSubsNodes*resCtPerSbs - avRes)

    substrateNetwork.clear()
    ranSlices[0].clear()
    totalNetwork.clear()
    resCapList.clear()
    resList.clear()
    vnfCncList.clear()
    vnfTotalAccList.clear()
    
    # Three
    
    substrateNetwork = tn.createSbsNetwork(numSubsNodes, resCapList, resCtPerSbs, connectivity)
    ranSlices = tn.createRANSlice(numRnSlices, numVnfFunctions, resList, resCtPerVnf, 2)
    totalNetwork  = tn.createTotalNetwork(substrateNetwork, ranSlices, vnfCncList, vnfTotalAccList)
        
    numMappings = tn.algoThreeTest(totalNetwork, vnfTotalAccList)
    avRes = tn.sbsAvailableRes(totalNetwork)
    yThree.append(numSubsNodes*resCtPerSbs - avRes)

    substrateNetwork.clear()
    ranSlices[0].clear()
    totalNetwork.clear()
    resCapList.clear()
    resList.clear()
    vnfCncList.clear()
    vnfTotalAccList.clear()
    
    connectivity-=1
    
    

print(xOne)
print(yOne)
print(yTwo)
print(yThree)

fig, ax = plt.subplots()
ax.plot(xOne, yOne, label="Algo One", linestyle='-')
ax.plot(xOne, yTwo, label="Algo Two", linestyle='--')
ax.plot(xOne, yThree, label="Algo Three", linestyle=':')

ax.set(xlabel='Degree of Substrate Tower', ylabel='Amount of Substrate Resources Exhausted',
title='Connectivity Test')
ax.grid()
ax.legend(loc="best")

fig.savefig("ResultsThree/conFour.png")
plt.show()

#---------------------------------------------------------------------------------------------------

# (1) No. of Connections Sbs vs No. of Succesfull Mapings 

# connectivity = 8

# xOne = []
# yOne = []
# yTwo = []
# yThree = []

# for ctrVar in range(5):
    
#     # One
    
#     substrateNetwork = tn.createSbsNetwork(numSubsNodes, resCapList, resCtPerSbs, connectivity)
#     ranSlices = tn.createRANSlice(numRnSlices, numVnfFunctions, resList, resCtPerVnf)
#     totalNetwork  = tn.createTotalNetwork(substrateNetwork, ranSlices, vnfCncList, vnfTotalAccList)
        
#     numMappings = tn.algoOneTest(totalNetwork, substrateNetwork, ranSlices, resList, resCapList)
#     xOne.append(connectivity)
#     yOne.append(numMappings)

#     substrateNetwork.clear()
#     ranSlices[0].clear()
#     totalNetwork.clear()
#     resCapList.clear()
#     resList.clear()
#     vnfCncList.clear()
#     vnfTotalAccList.clear()
    
#     # Two
    
#     substrateNetwork = tn.createSbsNetwork(numSubsNodes, resCapList, resCtPerSbs, connectivity)
#     ranSlices = tn.createRANSlice(numRnSlices, numVnfFunctions, resList, resCtPerVnf)
#     totalNetwork  = tn.createTotalNetwork(substrateNetwork, ranSlices, vnfCncList, vnfTotalAccList)
        
#     numMappings = tn.algoTwoTest(totalNetwork, vnfCncList)
#     yTwo.append(numMappings)

#     substrateNetwork.clear()
#     ranSlices[0].clear()
#     totalNetwork.clear()
#     resCapList.clear()
#     resList.clear()
#     vnfCncList.clear()
#     vnfTotalAccList.clear()
    
#     # Three
    
#     substrateNetwork = tn.createSbsNetwork(numSubsNodes, resCapList, resCtPerSbs, connectivity)
#     ranSlices = tn.createRANSlice(numRnSlices, numVnfFunctions, resList, resCtPerVnf)
#     totalNetwork  = tn.createTotalNetwork(substrateNetwork, ranSlices, vnfCncList, vnfTotalAccList)
        
#     numMappings = tn.algoThreeTest(totalNetwork, vnfTotalAccList)
#     yThree.append(numMappings)

#     substrateNetwork.clear()
#     ranSlices[0].clear()
#     totalNetwork.clear()
#     resCapList.clear()
#     resList.clear()
#     vnfCncList.clear()
#     vnfTotalAccList.clear()
    
#     connectivity-=1
    
    

# print(xOne)
# print(yOne)
# print(yTwo)
# print(yThree)

# fig, ax = plt.subplots()
# ax.plot(xOne, yOne, label="Algo One", linestyle='-')
# ax.plot(xOne, yTwo, label="Algo Two", linestyle='--')
# ax.plot(xOne, yThree, label="Algo Three", linestyle=':')

# ax.set(xlabel='Degree of Substrate Tower', ylabel='Number of Successful Mappings',
# title='Connectivity Test')
# ax.grid()
# ax.legend(loc="best")

# fig.savefig("ResultsThree/conOne.png")
# plt.show()

# (2) No. of Connections Sbs vs No. of UnSuccesfull Mapings 

# connectivity = 8

# xOne = []
# yOne = []
# yTwo = []
# yThree = []

# for ctrVar in range(5):
    
#     # One
    
#     substrateNetwork = tn.createSbsNetwork(numSubsNodes, resCapList, resCtPerSbs, connectivity)
#     ranSlices = tn.createRANSlice(numRnSlices, numVnfFunctions, resList, resCtPerVnf)
#     totalNetwork  = tn.createTotalNetwork(substrateNetwork, ranSlices, vnfCncList, vnfTotalAccList)
        
#     numMappings = tn.algoOneTest(totalNetwork, substrateNetwork, ranSlices, resList, resCapList)
#     xOne.append(connectivity)
#     yOne.append(numVnfFunctions - numMappings)

#     substrateNetwork.clear()
#     ranSlices[0].clear()
#     totalNetwork.clear()
#     resCapList.clear()
#     resList.clear()
#     vnfCncList.clear()
#     vnfTotalAccList.clear()
    
#     # Two
    
#     substrateNetwork = tn.createSbsNetwork(numSubsNodes, resCapList, resCtPerSbs, connectivity)
#     ranSlices = tn.createRANSlice(numRnSlices, numVnfFunctions, resList, resCtPerVnf)
#     totalNetwork  = tn.createTotalNetwork(substrateNetwork, ranSlices, vnfCncList, vnfTotalAccList)
        
#     numMappings = tn.algoTwoTest(totalNetwork, vnfCncList)
#     yTwo.append(numVnfFunctions - numMappings)

#     substrateNetwork.clear()
#     ranSlices[0].clear()
#     totalNetwork.clear()
#     resCapList.clear()
#     resList.clear()
#     vnfCncList.clear()
#     vnfTotalAccList.clear()
    
#     # Three
    
#     substrateNetwork = tn.createSbsNetwork(numSubsNodes, resCapList, resCtPerSbs, connectivity)
#     ranSlices = tn.createRANSlice(numRnSlices, numVnfFunctions, resList, resCtPerVnf)
#     totalNetwork  = tn.createTotalNetwork(substrateNetwork, ranSlices, vnfCncList, vnfTotalAccList)
        
#     numMappings = tn.algoThreeTest(totalNetwork, vnfTotalAccList)
#     yThree.append(numVnfFunctions - numMappings)

#     substrateNetwork.clear()
#     ranSlices[0].clear()
#     totalNetwork.clear()
#     resCapList.clear()
#     resList.clear()
#     vnfCncList.clear()
#     vnfTotalAccList.clear()
    
#     connectivity-=1
    

# print(xOne)
# print(yOne)
# print(yTwo)
# print(yThree)

# fig, ax = plt.subplots()
# ax.plot(xOne, yOne, label="Algo One", linestyle='-')
# ax.plot(xOne, yTwo, label="Algo Two", linestyle='--')
# ax.plot(xOne, yThree, label="Algo Three", linestyle=':')

# ax.set(xlabel='Degree of Substrate Tower', ylabel='Number of Unuccessful Mappings',
# title='Connectivity Test')
# ax.grid()
# ax.legend(loc="best")

# fig.savefig("ResultsThree/conTwo.png")
# plt.show()


# (3) No. of Connections Sbs vs Amount of Sbs. Resouces Unused.

# connectivity = 2

# xOne = []
# yOne = []
# yTwo = []
# yThree = []

# for ctrVar in range(5):
    
#     # One
    
#     substrateNetwork = tn.createSbsNetwork(numSubsNodes, resCapList, resCtPerSbs, connectivity)
#     ranSlices = tn.createRANSlice(numRnSlices, numVnfFunctions, resList, resCtPerVnf, connectivity)
#     totalNetwork  = tn.createTotalNetwork(substrateNetwork, ranSlices, vnfCncList, vnfTotalAccList)
        
#     numMappings = tn.algoOneTest(totalNetwork, substrateNetwork, ranSlices, resList, resCapList)
#     avRes = tn.sbsAvailableRes(totalNetwork)
#     yOne.append(avRes)

#     substrateNetwork.clear()
#     ranSlices[0].clear()
#     totalNetwork.clear()
#     resCapList.clear()
#     resList.clear()
#     vnfCncList.clear()
#     vnfTotalAccList.clear()
    
#     # Two
    
#     substrateNetwork = tn.createSbsNetwork(numSubsNodes, resCapList, resCtPerSbs, connectivity)
#     ranSlices = tn.createRANSlice(numRnSlices, numVnfFunctions, resList, resCtPerVnf, 2)
#     totalNetwork  = tn.createTotalNetwork(substrateNetwork, ranSlices, vnfCncList, vnfTotalAccList)
        
#     numMappings = tn.algoTwoTest(totalNetwork, vnfCncList)
#     yavRes = tn.sbsAvailableRes(totalNetwork)
#     yTwo.append(avRes)

#     substrateNetwork.clear()
#     ranSlices[0].clear()
#     totalNetwork.clear()
#     resCapList.clear()
#     resList.clear()
#     vnfCncList.clear()
#     vnfTotalAccList.clear()
    
#     # Three
    
#     substrateNetwork = tn.createSbsNetwork(numSubsNodes, resCapList, resCtPerSbs, connectivity)
#     ranSlices = tn.createRANSlice(numRnSlices, numVnfFunctions, resList, resCtPerVnf, 2)
#     totalNetwork  = tn.createTotalNetwork(substrateNetwork, ranSlices, vnfCncList, vnfTotalAccList)
        
#     numMappings = tn.algoThreeTest(totalNetwork, vnfTotalAccList)
#     avRes = tn.sbsAvailableRes(totalNetwork)
#     yThree.append(avRes)

#     substrateNetwork.clear()
#     ranSlices[0].clear()
#     totalNetwork.clear()
#     resCapList.clear()
#     resList.clear()
#     vnfCncList.clear()
#     vnfTotalAccList.clear()
    
#     connectivity-=1
    
    

# print(xOne)
# print(yOne)
# print(yTwo)
# print(yThree)

# fig, ax = plt.subplots()
# ax.plot(xOne, yOne, label="Algo One", linestyle='-')
# ax.plot(xOne, yTwo, label="Algo Two", linestyle='--')
# ax.plot(xOne, yThree, label="Algo Three", linestyle=':')

# ax.set(xlabel='Degree of Substrate Tower', ylabel='Amount of Substrate Resources Available',
# title='Connectivity Test')
# ax.grid()
# ax.legend(loc="best")

# fig.savefig("ResultsThree/conThree.png")
# plt.show()


# # (4) No. of Connections Sbs vs Amount of Sbs. Resouces Exhausted


# connectivity = 8

# xOne = []
# yOne = []
# yTwo = []
# yThree = []

# for ctrVar in range(5):
    
#     # One
    
#     substrateNetwork = tn.createSbsNetwork(numSubsNodes, resCapList, resCtPerSbs, connectivity)
#     ranSlices = tn.createRANSlice(numRnSlices, numVnfFunctions, resList, resCtPerVnf, 2)
#     totalNetwork  = tn.createTotalNetwork(substrateNetwork, ranSlices, vnfCncList, vnfTotalAccList)
        
#     numMappings = tn.algoOneTest(totalNetwork, substrateNetwork, ranSlices, resList, resCapList)
#     avRes = tn.sbsAvailableRes(totalNetwork)
#     yOne.append(numSubsNodes*resCtPerSbs - avRes)

#     substrateNetwork.clear()
#     ranSlices[0].clear()
#     totalNetwork.clear()
#     resCapList.clear()
#     resList.clear()
#     vnfCncList.clear()
#     vnfTotalAccList.clear()
    
#     # Two
    
#     substrateNetwork = tn.createSbsNetwork(numSubsNodes, resCapList, resCtPerSbs, connectivity)
#     ranSlices = tn.createRANSlice(numRnSlices, numVnfFunctions, resList, resCtPerVnf, 2)
#     totalNetwork  = tn.createTotalNetwork(substrateNetwork, ranSlices, vnfCncList, vnfTotalAccList)
        
#     numMappings = tn.algoTwoTest(totalNetwork, vnfCncList)
#     yavRes = tn.sbsAvailableRes(totalNetwork)
#     yTwo.append(numSubsNodes*resCtPerSbs - avRes)

#     substrateNetwork.clear()
#     ranSlices[0].clear()
#     totalNetwork.clear()
#     resCapList.clear()
#     resList.clear()
#     vnfCncList.clear()
#     vnfTotalAccList.clear()
    
#     # Three
    
#     substrateNetwork = tn.createSbsNetwork(numSubsNodes, resCapList, resCtPerSbs, connectivity)
#     ranSlices = tn.createRANSlice(numRnSlices, numVnfFunctions, resList, resCtPerVnf, 2)
#     totalNetwork  = tn.createTotalNetwork(substrateNetwork, ranSlices, vnfCncList, vnfTotalAccList)
        
#     numMappings = tn.algoThreeTest(totalNetwork, vnfTotalAccList)
#     avRes = tn.sbsAvailableRes(totalNetwork)
#     yThree.append(numSubsNodes*resCtPerSbs - avRes)

#     substrateNetwork.clear()
#     ranSlices[0].clear()
#     totalNetwork.clear()
#     resCapList.clear()
#     resList.clear()
#     vnfCncList.clear()
#     vnfTotalAccList.clear()
    
#     connectivity-=1
    
    

# print(xOne)
# print(yOne)
# print(yTwo)
# print(yThree)

# fig, ax = plt.subplots()
# ax.plot(xOne, yOne, label="Algo One", linestyle='-')
# ax.plot(xOne, yTwo, label="Algo Two", linestyle='--')
# ax.plot(xOne, yThree, label="Algo Three", linestyle=':')

# ax.set(xlabel='Degree of Substrate Tower', ylabel='Amount of Substrate Resources Exhausted',
# title='Connectivity Test')
# ax.grid()
# ax.legend(loc="best")

# fig.savefig("ResultsThree/conFour.png")
