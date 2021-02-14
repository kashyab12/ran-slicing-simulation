from graph_tool.all import *
import numpy as np
import random

def algorithmOne(totalNetwork, resList, resCapList, greedy_method):

    sortedResValList = sorted(resList, reverse=greedy_method)
    sortedSbsValList = sorted(resCapList, reverse=greedy_method)
    sbsFoundVertex = 0
    numOfMappings = 0
    ranFoundVertex = 0

    for vnfResourceValue in sortedResValList:

        foundSbsVert = False
        ranFoundVertex = find_vertex(totalNetwork, totalNetwork.vp.resources, vnfResourceValue)

        ctrVar = len(ranFoundVertex) - 1

        while ctrVar >= 0:
            if totalNetwork.vertex_properties.binaryMappingVar[ranFoundVertex[ctrVar]] == 0:
                ranFoundVertex = ranFoundVertex[ctrVar]
                break
            else:
                del ranFoundVertex[ctrVar]
                ctrVar -= 1

        if not ranFoundVertex:
            print("Empty List of Found VNF Functions")
            continue
        else:
            isNeighborMapped = False

            for neighbor in ranFoundVertex.all_neighbors():
                if totalNetwork.vp.binaryMappingVar[neighbor] == 1:
                    isNeighborMapped = True
                    break
                else:
                    continue
            
            # Case One
            if isNeighborMapped == False:
                sbsFoundVertex = find_vertex(totalNetwork, totalNetwork.vp.resourceCapacity, sortedSbsValList[0])
                
                if not sbsFoundVertex:
                    print("I am Empty")

                if totalNetwork.vertex_properties.resourceCapacity[sbsFoundVertex[0]] >= vnfResourceValue:
                    foundSbsVert = True
                
                if foundSbsVert == False:
                    print("Failed VNF Mapping Case One")
                    totalNetwork.vp.binaryMappingVar[ranFoundVertex] = 2
                    continue
                else: # Mapping Case One
                    totalNetwork.add_edge(sbsFoundVertex[0], ranFoundVertex)
                    totalNetwork.vp.binaryMappingVar[ranFoundVertex] = 1
                    numOfMappings += 1
                    totalNetwork.vp.resourceCapacity[sbsFoundVertex[0]] -= totalNetwork.vertex_properties.resources[ranFoundVertex]
                    sortedSbsValList[0] = totalNetwork.vp.resourceCapacity[sbsFoundVertex[0]]
                    sortedSbsValList = sorted(sortedSbsValList, reverse=greedy_method)
            else: # Mapping Case Two

                selectedSbsTower = []
                selectedCounter = 0
                iterCountBand = 0
                
                vnfMappedNeighbor = []
                vnfSbsMappedNeighbor = []

                mappableSbsTowers = []
                unmappableTowers = set()

                for vnf_neighbor in ranFoundVertex.all_neighbors():

                    if totalNetwork.vertex_properties.binaryMappingVar[vnf_neighbor] == 1:
                        vnfMappedNeighbor.append(vnf_neighbor)

                        substrateEdgeList = find_edge(totalNetwork, totalNetwork.ep.bandwidth, 0)

                        for edges in substrateEdgeList:
                            if edges.source() == vnf_neighbor:
                                vnfSbsMappedNeighbor.append(edges.target())
                                break
                            elif edges.target() == vnf_neighbor:
                                vnfSbsMappedNeighbor.append(edges.source())
                                break
                
                for sbsResourceValue in sortedSbsValList:
                    possibleSbsTower = find_vertex(totalNetwork, totalNetwork.vp.resourceCapacity, sbsResourceValue)
                    isFoundSbs = False

                    while True:
                        if not possibleSbsTower:
                            break
                        elif possibleSbsTower[0] in mappableSbsTowers or possibleSbsTower[0] in unmappableTowers:
                            possibleSbsTower.pop(0)
                        else:
                            break
                    
                    if not possibleSbsTower:
                        print("List of Possible is Empty")
                        continue

                    if totalNetwork.vp.resourceCapacity[possibleSbsTower[0]] >= vnfResourceValue:
                        for mappedSbsTower in vnfSbsMappedNeighbor:
                            if possibleSbsTower[0] not in mappedSbsTower.all_neighbors():   
                                if possibleSbsTower[0] == mappedSbsTower:
                                    isFoundSbs = True  
                                else:               
                                    isFoundSbs = False
                                    unmappableTowers.add(possibleSbsTower[0])
                                    break
                            else:
                                isFoundSbs = True
                        
                        if isFoundSbs == True:
                            foundSbsVert = True
                            mappableSbsTowers.append(possibleSbsTower[0])
                            selectedSbsTower.append(selectedCounter)
                        
                        selectedCounter += 1
                    else:
                        print("Resource not Satisfied Case Two")
                        unmappableTowers.add(possibleSbsTower[0])
                        if greedy_method == True:
                            break
                        else:
                            continue
                
                if foundSbsVert == False:
                    print("VNF Mapping Failure Rescource and Connection Issue")
                    totalNetwork.vp.binaryMappingVar[ranFoundVertex] = 2
                    continue
                else:
                    # Checking for Bandwidth

                    for possibleSbs in mappableSbsTowers:

                        for mappedNeighborCounter in range(len(vnfMappedNeighbor)):
                            vnfBandwidthConnection = 0
                            sbsBandwidthConnection = 0

                            # Find the Substrate Edge First

                            if vnfSbsMappedNeighbor[mappedNeighborCounter] == possibleSbs:
                                sbsFoundVertex = possibleSbs
                                foundSbsVert = True
                                continue
                            
                            for edge in possibleSbs.all_edges():
                                if edge.source() == vnfSbsMappedNeighbor[mappedNeighborCounter] or edge.target() == vnfSbsMappedNeighbor[mappedNeighborCounter]:
                                    sbsBandwidthConnection = edge
                            
                            for edge in ranFoundVertex.all_edges():
                                if edge.source() == vnfMappedNeighbor[mappedNeighborCounter] or edge.target() == vnfMappedNeighbor[mappedNeighborCounter]:
                                    vnfBandwidthConnection = edge
                
                            if totalNetwork.ep.bandwidth[sbsBandwidthConnection] >= totalNetwork.ep.bandwidth[vnfBandwidthConnection]:
                                foundSbsVert = True
                            else:
                                foundSbsVert = False
                        
                        if foundSbsVert == True:
                            sbsFoundVertex = possibleSbs
                            break
                        else:
                            continue
                    
                    if foundSbsVert == False:
                        print("VNF Mapping Failure Bandwidth Connection")
                        totalNetwork.vp.binaryMappingVar[ranFoundVertex] = 2
                        continue
                    else:

                        sortCount = 0

                        totalNetwork.add_edge(sbsFoundVertex, ranFoundVertex)
                        totalNetwork.vp.binaryMappingVar[ranFoundVertex] = 1
                        numOfMappings += 1
                        totalNetwork.vp.resourceCapacity[sbsFoundVertex] -= totalNetwork.vertex_properties.resources[ranFoundVertex]

                        # Search for the appropraite Index

                        for iterCount in range(len(mappableSbsTowers)):
                            if mappableSbsTowers[iterCount] == sbsFoundVertex:
                                sortCount = selectedSbsTower[iterCount]
                                break

                        sortedSbsValList[sortCount] = totalNetwork.vp.resourceCapacity[sbsFoundVertex]
                        sortedSbsValList = sorted(sortedSbsValList, reverse=greedy_method)

    return numOfMappings;


def algorithmTwo(totalNetwork, vnfCncList):
    # Sorting the list of maximal connections for the VNF Functions
    sortedVnfCncList = sorted(vnfCncList, reverse=True)
    sbsFoundVertex = 0
    ranFoundVertex = 0
    numOfMappings = 0
    isFirst = True

    #  Step One - First store the Maximally connected VNFs and their Neighbors in a list of sets

    maximalConnectedVnfs = []
    for resVal in sortedVnfCncList:

        maxCncVertex = find_vertex(totalNetwork, totalNetwork.vp.degree, resVal)

        loopIter = len(maxCncVertex) - 1 
        maxCncList = []

        while loopIter >= 0:
            if totalNetwork.vertex_properties.binaryMappingVar[maxCncVertex[loopIter]] == 0:
                maxCncVertex = maxCncVertex[loopIter]
                break
            else:
                del maxCncVertex[loopIter]
                loopIter -= 1
        
        if not maxCncVertex:
            print("Exception has been thrown! The max connected vertex is not found due to probably being mapped")
            continue
        else:
            maxCncList.append(maxCncVertex)
            totalNetwork.vp.binaryMappingVar[maxCncVertex] = 3
        
        for maxCncVertexNeighbor in maxCncVertex.all_neighbors():
            if totalNetwork.vertex_properties.binaryMappingVar[maxCncVertexNeighbor] == 0:
                maxCncList.add(maxCncVertexNeighbor)
                totalNetwork.vp.binaryMappingVar[maxCncVertexNeighbor] = 3  

        maximalConnectedVnfs.append(maxCncList)

    # Step Two - Mapping the Neighborhoods
    
    for neighborhood in maximalConnectedVnfs:

        isFirst = True
        isFirstFailed = False

        for vnf_vertex in neighborhood:

            ranFoundVertex = vnf_vertex
            mappableSbsTowers = []

            if isFirst:
                # Make the first VNFs Mapping here and then map its neighbors in the consequent Substrate Tower
                
                sbsPositiveDifference = []
                sbsNegativeDifference = []
                negativeSbsIndex = -1
                positiveSbsIndex = -1
                finalSbsIndex = -1

                # Check if the first has a mapped neighbor 

                isMainVnfMapped = False

                for neighbors in ranFoundVertex.all_neighbors():
                    if totalNetwork.vp.binaryMappingVar[neighbors] == 1:
                        isMainVnfMapped = True
                        break
                    else:
                        continue

                # If the vnf does not have a mapped neighbor
                if not isMainVnfMapped:
                    # Try to find the Sbs Tower which would be most appropriate 
                    sbsNetwork = find_vertex(totalNetwork, totalNetwork.gp.vertexName, "Substrate")

                    # Find the Towers which can provide it with resources as well as Highest Insurance for its Neighbors
                    for sbsTower in sbsNetwork:
                        if totalNetwork.vp.resourceCapacity[sbsTower] >= totalNetwork.vp.resources[ranFoundVertex]:
                            mappableSbsTowers.append(sbsTower)
                    
                    # Even it has failed we still continue to try and find its best sbs tower
                    if not mappableSbsTowers:
                        print("The First Has Failed. ")
                        isFirstFailed = True
                        isFirst = True
                        updateList = []
                        updateList.append(ranFoundVertex)
                        updateList.append(ranFoundVertex.all_neighbors())
                        for updateVnfFunction in updateList:
                            totalNetwork.vp.totalResourcesAcc[updateVnfFunction] -= totalNetwork.vp.totalResourcesAcc[updateVnfFunction]

                        totalNetwork.vp.binaryMappingVar[ranFoundVertex] = 2
                        continue
                        
                    # Looping to find the Sbs Neighborhood Differences

                    for sbsTower in mappableSbsTowers:
                        if (totalNetwork.vp.totalResoucesAcc[sbsTower] - totalNetwork.vp.totalResourcesAcc[ranFoundVertex]) >= 0:
                            sbsPositiveDifference.append(totalNetwork.vp.totalResourcesAcc[sbsTower] - totalNetwork.vp.totalResourcesAcc[ranFoundVertex])
                            sbsNegativeDifference.append(-1000000)
                        elif (totalNetwork.vp.totalResoucesAcc[sbsTower] - totalNetwork.vp.totalResourcesAcc[ranFoundVertex]) <= 0:
                            sbsNegativeDifference.append(totalNetwork.vp.totalResourcesAcc[sbsTower] - totalNetwork.vp.totalResourcesAcc[ranFoundVertex])
                            sbsPositiveDifference.append(1000000)
                    
                    sbsPositiveDifference = np.asarray(sbsPositiveDifference)
                    sbsNegativeDifference = np.asarray(sbsNegativeDifference)

                    # Make Imporovements - Improve way of accomdating neighborhoods to Required Spots (Look at Notion Improvements Page)
                    # Another Improvement - Add all the like differences to a list (Allowing to check for the most connected Sbs Tower and take that one instead.)
                    if sbsPositiveDifference:
                        positiveSbsIndex = sbsPositiveDifference.argmin()
                        finalSbsIndex = negativeSbsIndex
                    elif sbsNegativeDifference:
                        negativeSbsIndex = sbsNegativeDifference.argmax()
                        finalSbsIndex = negativeSbsIndex
                    else:
                        print("A Failure Has Occured! Why would this happen?")
                        isFirstFailed = True
                        isFirst = True
                        continue
                    
                    # We have found our Primary Sbs Neighborhood !!
                    sbsFoundVertex = mappableSbsTowers[finalSbsIndex]

                    # In this case we can simply map now without considering connections and bandwidth

                    totalNetwork.add_edge(sbsFoundVertex, ranFoundVertex)
                    totalNetwork.vp.binaryMappingVar[ranFoundVertex] = 1
                    numOfMappings += 1
                    totalNetwork.vp.resourceCapacity[sbsFoundVertex] -= totalNetwork.vp.resources[ranFoundVertex]

                    # Must Update the Total Resources Acc For Sbs Tower and Its Neighbors
                    updateSbsList = []
                    updateSbsList.append(sbsFoundVertex)
                    updateSbsList.append(sbsFoundVertex.all_neighbors())

                    for updateFunction in updateSbsList:
                        totalNetwork.vp.totalResourcesAcc[updateFunction] -= totalNetwork.vp.resources[ranFoundVertex]

                    isFirst = False

                else:
                    # We Must Find the Best Candidate for the VNF Function Connected to an Already Mapped Neighbor
                    # Firstly, let us try to find the list of Sbs Towers that Satisfy the connection component.

                    # Mapped VNF Neighbors
                    mappedVnfNeighbor = []

                    for neighborVnfFunction in ranFoundVertex.all_neighbors():
                        if totalNetwork.vp.binaryMappingVar[neighborVnfFunction] == 1:
                            mappedVnfNeighbor.append(neighborVnfFunction)

                    # List of Neighborhood Lists to find the intersections
                    neighborhoodList = []

                    for neighborVnfFunction in mappedVnfNeighbor:
                        neighborhood = []
                        neighborhood.append(totalNetwork.vertex_index[neighborVnfFunction])

                        for neighbors in neighborVnfFunction:
                            neighborhood.append(totalNetwork.vertex_index[neighbors])
                        
                        neighborhoodList.append(neighborhood)
                        neighborhood.clear()
                    
                    # Now that we have the neighborhood list we can now find the interesection

                    # Not using mappableSbsTowers since it is not a set
                    possibleSbsTowers = set(neighborhoodList[0])

                    for neighborhood in neighborhoodList[1:]:
                        possibleSbsTowers.intersection_update(neighborhood)

                    if not possibleSbsTowers:
                        isFirstFailed = True
                        isFirst = True
                        updateList = []
                        updateList.append(ranFoundVertex)
                        updateList.append(ranFoundVertex.all_neighbors())

                        for updateVnfFunction in updateList:
                            totalNetwork.vp.totalResourcesAcc[updateVnfFunction] -= totalNetwork.vp.totalResourcesAcc[updateVnfFunction]

                        totalNetwork.vp.binaryMappingVar[ranFoundVertex] = 2
                        continue
                
                    # Now out of this list we must check for resource possibility

                    for vertexIndex in possibleSbsTowers:
                        mappableSbsTowers.append(totalNetwork.vertex(vertexIndex))

                    resRefinedMappable = []

                    for sbsTower in mappableSbsTowers:
                        if totalNetwork.vp.resourceCapacity[sbsTower] >= totalNetwork.vp.resourceCapacity[ranFoundVertex]:
                            resRefinedMappable.append(sbsTower)
                    
                    mappableSbsTowers = resRefinedMappable
                    
                    # Checking again for Failure

                    if not mappableSbsTowers:
                        print("Failure has Occured On the First Round.")
                        isFirstFailed = True
                        isFirst = True
                        updateList = []
                        updateList.append(ranFoundVertex)
                        updateList.append(ranFoundVertex.all_neighbors())

                        for updateVnfFunction in updateList:
                            totalNetwork.vp.totalResourcesAcc[updateVnfFunction] -= totalNetwork.vp.totalResourcesAcc[updateVnfFunction]

                        totalNetwork.vp.binaryMappingVar[ranFoundVertex] = 2
                        continue

                    # Checking for Bandwidth of the connections

                    # First we must find all the sbs towers our vnf neighbors are mapped to ( Approach Similar to Algo One )
                    
                    vnfNeighborMappedSbs = []

                    for neighbor in mappedVnfNeighbor:

                    # After doing so we will check which of the compatible Sbs Towers has the closest Total Resource Acc compared to the Neighborhood being dealt with.
            
            
            else: # Dealing with the Child Neighbors
                # Very Similar Approach to the Above Else Clause
    
                    
# Defining Algorithm 3 (Baskin Robbins Algorithm)
def algorithmThree(totalNetwork,resList,resCAPlist,greedy_method, totalResAccList):
    # possibleSbsTower = find_vertex(totalNetwork, totalNetwork.vp.resourceCapacity, sbsResourceValue)
    sortedAccList    = sorted(totalResAccList, reversed = True)

