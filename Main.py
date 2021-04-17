import OutputResults as out
import multiprocessing as mp
import TotalNetwork as tn

# Results from the Resource Allocation Part

ranSlices = tn.createRANSlice(tn.numRnSlices, tn.numVnfFunctions, tn.resList, tn.resCtPerVnf, connectivity=tn.vnfDegree, random_range=0)
substrateNetwork = tn.createSbsNetwork(tn.numSubsNodes, tn.resCapList, resCtPerSbs=tn.resCtPerSbs, connectivity=tn.sbsDegree, random_range=0)

out.generateSbsTestResults(ranSlices, substrateNetwork)
 
tn.numSubsNodes = 100
tn.numVnfFunctions = 100

out.generateVnfTestResults(ranSlices, substrateNetwork)


# Process(target=out.generateSbsTestResults, args=(ranSlices, substrateNetwork,))
# # processTwo = mp.Process(target=out.generateVnfConTestResults)
# processThree = mp.Process(target=out.generateVnfTestResults, args=(ranSlices, substrateNetwork,))
# # processFour = mp.Process(target=out.generateSbsConTestResults)

# processOne.start()
# # processTwo.start()
# processThree.start()
# # processFour.start()

# processOne.join()
# # processTwo.join()
# processThree.join()
# # processFour.join()
