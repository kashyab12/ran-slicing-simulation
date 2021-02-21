import TestingSbs as testSbs
import TestingSbsConnection as testSbsCon
import TestingVNF as testVnf
import TestingVnfConnection as testVnfCon
import matplotlib.pyplot as plt
import numpy as np
import TotalNetwork as tn

def outputFigure(resultOne, resultTwo, resultThree, resultFour, xLabel, yLabel, outputTitle, savedLocation, lowerBound, upperBound, intervalFactor):
    fig, ax = plt.subplots()
    ax.plot(resultOne[0], resultOne[1], label="Algo One", linestyle='-', linewidth=2.0, marker='^', color='r')
    ax.plot(resultTwo[0], resultTwo[1], label="Algo Two", linestyle='--', linewidth=2.0, marker='s', color='b')
    ax.plot(resultThree[0], resultThree[1], label="Algo Three", linestyle=':' ,linewidth=4.0, marker='p', color='m')
    ax.plot(resultFour[0], resultFour[1], label="Algo Four", linestyle='-.', linewidth=4.0, marker='*', color='g')

    majorTick = np.arange(lowerBound, upperBound, intervalFactor )
    ax.set_xticks(majorTick)

    ax.set(xlabel=xLabel, ylabel=yLabel,
    title=outputTitle)
    ax.grid()
    ax.legend(loc="best")

    fig.savefig(savedLocation)
    plt.show()
    

def generateSbsTestResults():

    xLabel = "Number of Substrate Towers"
    outputTitle = "Independent Variable - No. of Substrate Towers"

    # First Testing Against Succesfull Mappings

    resultOne = testSbs.testSuccMappings(1)
    resultTwo = testSbs.testSuccMappings(2)
    resultThree = testSbs.testSuccMappings(3)
    resultFour = testSbs.testSuccMappings(4)
    savedLocation = "ResultsOne/sbsOne.png"
    yLabel = "Number of Succesfull Mappings"

    # Now that we have all the results with the subsequent arrays

    outputFigure(resultOne, resultTwo, resultThree, resultFour, xLabel, yLabel, outputTitle, savedLocation, tn.numSubsNodes, tn.numSubsNodes + testSbs.intervalFactor*5 + 1, testSbs.intervalFactor)

    # Now test against Unsucessfull Mappings

    resultOne = testSbs.testUnsuccMappings(1)
    resultTwo = testSbs.testUnsuccMappings(2)
    resultThree = testSbs.testUnsuccMappings(3)
    resultFour = testSbs.testUnsuccMappings(4)
    savedLocation = "ResultsOne/sbsTwo.png"
    yLabel = "Number of Unsuccesfull Mappings"

    #  Now that we have all the results with the subsequent arrays

    outputFigure(resultOne, resultTwo, resultThree, resultFour, xLabel, yLabel, outputTitle, savedLocation, tn.numSubsNodes, tn.numSubsNodes + testSbs.intervalFactor*5 + 1, testSbs.intervalFactor)

    # Test Against Avail Resources

    resultOne = testSbs.testAvailRes(1)
    resultTwo = testSbs.testAvailRes(2)
    resultThree = testSbs.testAvailRes(3)
    resultFour = testSbs.testAvailRes(4)
    savedLocation = "ResultsOne/sbsThree.png"
    yLabel = "Amount of Available Resources"

    #  Now that we have all the results with the subsequent arrays

    outputFigure(resultOne, resultTwo, resultThree, resultFour, xLabel, yLabel, outputTitle, savedLocation, tn.numSubsNodes, tn.numSubsNodes + testSbs.intervalFactor*5 + 1, testSbs.intervalFactor)

    # Test Against Avail Resources

    resultOne = testSbs.testExhaustRes(1)
    resultTwo = testSbs.testExhaustRes(2)
    resultThree = testSbs.testExhaustRes(3)
    resultFour = testSbs.testExhaustRes(4)
    
    savedLocation = "ResultsOne/sbsFour.png"
    yLabel = "Amount of Exhausted Resources"

    #  Now that we have all the results with the subsequent arrays

    outputFigure(resultOne, resultTwo, resultThree, resultFour, xLabel, yLabel, outputTitle, savedLocation, tn.numSubsNodes, tn.numSubsNodes + testSbs.intervalFactor*5 + 1, testSbs.intervalFactor)

def generateSbsConTestResults():

    xLabel = "Connection Per Substrate Tower"
    outputTitle = "Independent Variable - Degree Per Substrate Tower"

    # First Testing Against Succesfull Mappings

    resultOne = testSbsCon.testSuccMappings(1,8)
    resultTwo = testSbsCon.testSuccMappings(2, 8)
    resultThree = testSbsCon.testSuccMappings(3, 8)
    resultFour = testSbsCon.testSuccMappings(4, 8)

    savedLocation = "ResultsTwo/sbsConOne.png"
    yLabel = "Number of Succesfull Mappings"

    # Now that we have all the results with the subsequent arrays

    outputFigure(resultOne, resultTwo, resultThree, resultFour, xLabel, yLabel, outputTitle, savedLocation, 8, 2, testSbsCon.intervalFactor)

    # Now test against Unsucessfull Mappings

    resultOne = testSbsCon.testUnsuccMappings(1, 8)
    resultTwo = testSbsCon.testUnsuccMappings(2, 8)
    resultThree = testSbsCon.testUnsuccMappings(3, 8)
    resultFour = testSbsCon.testUnsuccMappings(4, 8)
    savedLocation = "ResultsTwo/sbsConTwo.png"
    yLabel = "Number of Unsuccesfull Mappings"

    #  Now that we have all the results with the subsequent arrays

    outputFigure(resultOne, resultTwo, resultThree, resultFour, xLabel, yLabel, outputTitle, savedLocation, 8, 2, testSbsCon.intervalFactor)

    # Test Against Avail Resources

    resultOne = testSbsCon.testAvailRes(1, 8)
    resultTwo = testSbsCon.testAvailRes(2, 8)
    resultThree = testSbsCon.testAvailRes(3, 8)
    resultFour = testSbsCon.testAvailRes(4, 8)
    savedLocation = "ResultsTwo/sbsConThree.png"
    yLabel = "Amount of Available Resources"

    #  Now that we have all the results with the subsequent arrays

    outputFigure(resultOne, resultTwo, resultThree, resultFour, xLabel, yLabel, outputTitle, savedLocation, 8, 2, testSbsCon.intervalFactor)

    # Test Against Avail Resources

    resultOne = testSbsCon.testExhaustRes(1, 8)
    resultTwo = testSbsCon.testExhaustRes(2, 8)
    resultThree = testSbsCon.testExhaustRes(3, 8)
    resultFour = testSbsCon.testExhaustRes(4, 8)
    savedLocation = "ResultsTwo/sbsConFour.png"
    yLabel = "Amount of Exhausted Resources"

    #  Now that we have all the results with the subsequent arrays

    outputFigure(resultOne, resultTwo, resultThree, resultFour, xLabel, yLabel, outputTitle, savedLocation, 8, 2, testSbsCon.intervalFactor)

def generateVnfTestResults():

    xLabel = "Number of VNF Functions"
    outputTitle = "Independent Variable - No. of VNF Functions"

    # First Testing Against Succesfull Mappings

    resultOne = testVnf.testSuccMappings(1)
    resultTwo = testVnf.testSuccMappings(2)
    resultThree = testVnf.testSuccMappings(3)
    resultFour = testSbs.testSuccMappings(4)

    savedLocation = "ResultsThree/vnfOne.png"
    yLabel = "Number of Succesfull Mappings"

    # Now that we have all the results with the subsequent arrays

    outputFigure(resultOne, resultTwo, resultThree, resultFour, xLabel, yLabel, outputTitle, savedLocation, tn.numVnfFunctions, tn.numVnfFunctions + testVnf.intervalFactor*5 + 1, testVnf.intervalFactor )

    # Now test against Unsucessfull Mappings

    resultOne = testVnf.testUnsuccMappings(1)
    resultTwo = testVnf.testUnsuccMappings(2)
    resultThree = testVnf.testUnsuccMappings(3)
    resultFour = testSbs.testUnsuccMappings(4)
    savedLocation = "ResultsThree/vnfTwo.png"
    yLabel = "Number of Unsuccesfull Mappings"

    #  Now that we have all the results with the subsequent arrays

    outputFigure(resultOne, resultTwo, resultThree, resultFour, xLabel, yLabel, outputTitle, savedLocation, tn.numVnfFunctions, tn.numVnfFunctions + testVnf.intervalFactor*5 + 1, testVnf.intervalFactor )

    # Test Against Avail Resources

    resultOne = testVnf.testAvailRes(1)
    resultTwo = testVnf.testAvailRes(2)
    resultThree = testVnf.testAvailRes(3)
    resultFour = testSbs.testAvailMappings(4)
    savedLocation = "ResultsThree/vnfThree.png"
    yLabel = "Amount of Available Resources"

    #  Now that we have all the results with the subsequent arrays

    outputFigure(resultOne, resultTwo, resultThree, resultFour, xLabel, yLabel, outputTitle, savedLocation, tn.numVnfFunctions, tn.numVnfFunctions + testVnf.intervalFactor*5 + 1, testVnf.intervalFactor )

    # Test Against Avail Resources

    resultOne = testVnf.testExhaustRes(1)
    resultTwo = testVnf.testExhaustRes(2)
    resultThree = testVnf.testExhaustRes(3)
    resultFour = testSbs.testExhaustMappings(4)
    savedLocation = "ResultsThree/vnfFour.png"
    yLabel = "Amount of Exhausted Resources"

    #  Now that we have all the results with the subsequent arrays

    outputFigure(resultOne, resultTwo, resultThree, resultFour, xLabel, yLabel, outputTitle, savedLocation, tn.numVnfFunctions, tn.numVnfFunctions + testVnf.intervalFactor*5 + 1, testVnf.intervalFactor )

def generateVnfConTestResults():

    xLabel = "Connection Per VNF Function"
    outputTitle = "Independent Variable - Degree Per VNF Function"

    # First Testing Against Succesfull Mappings

    resultOne = testVnfCon.testSuccMappings(1, 8)
    resultTwo = testVnfCon.testSuccMappings(2, 8)
    resultThree = testVnf.testSuccMappings(3, 8)
    resultFour = testSbs.testSuccMappings(4, 8)
    savedLocation = "ResultsFour/vnfConOne.png"
    yLabel = "Number of Succesfull Mappings"

    # Now that we have all the results with the subsequent arrays

    outputFigure(resultOne, resultTwo, resultThree, resultFour, xLabel, yLabel, outputTitle, savedLocation, 8, 2, testVnfCon.intervalFactor)

    # Now test against Unsucessfull Mappings

    resultOne = testVnf.testUnsuccMappings(1, 8)
    resultTwo = testVnf.testUnsuccMappings(2, 8)
    resultThree = testVnf.testUnsuccMappings(3, 8)
    resultFour = testSbs.testUnsuccMappings(4, 8)
    savedLocation = "ResultsFour/vnfConTwo.png"
    yLabel = "Number of Unsuccesfull Mappings"

    #  Now that we have all the results with the subsequent arrays

    outputFigure(resultOne, resultTwo, resultThree, resultFour, xLabel, yLabel, outputTitle, savedLocation, 8, 2, testVnfCon.intervalFactor)

    # Test Against Avail Resources

    resultOne = testVnf.testAvailRes(1, 8)
    resultTwo = testVnf.testAvailRes(2, 8)
    resultThree = testVnf.testAvailRes(3, 8)
    resultFour = testSbs.testAvailMappings(4, 8)
    savedLocation = "ResultsFour/vnfConThree.png"
    yLabel = "Amount of Available Resources"

    #  Now that we have all the results with the subsequent arrays

    outputFigure(resultOne, resultTwo, resultThree, resultFour, xLabel, yLabel, outputTitle, savedLocation, 8, 2, testVnfCon.intervalFactor)

    # Test Against Avail Resources

    resultOne = testVnf.testExhaustRes(1, 8)
    resultTwo = testVnf.testExhaustRes(2, 8)
    resultThree = testVnf.testExhaustRes(3, 8)
    resultFour = testSbs.testExhaustMappings(4, 8)
    savedLocation = "ResultsFour/vnfConFour.png"
    yLabel = "Amount of Exhausted Resources"

    #  Now that we have all the results with the subsequent arrays

    outputFigure(resultOne, resultTwo, resultThree, resultFour, xLabel, yLabel, outputTitle, savedLocation, 8, 2, testVnfCon.intervalFactor)




