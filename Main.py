import OutputResults as out
import multiprocessing as mp

# Results from the Resource Allocation Part

processOne = mp.Process(target=out.generateSbsTestResults)
processTwo = mp.Process(target=out.generateVnfConTestResults)
processThree = mp.Process(target=out.generateVnfTestResults)
processFour = mp.Process(target=out.generateSbsConTestResults)

processOne.start()
processTwo.start()
processThree.start()
processFour.start()

processOne.join()
processTwo.join()
processThree.join()
processFour.join()
