from graph_tool.all import *
import numpy as np
import random



def algorithmTwo(totalNetwork, vnfCncList):
    
    # Sorting the list of maximal connections for the VNF Functions
    sortedVnfCncList = sorted(vnfCncList, reverse=True)
    sbsFoundVertex = 0
    ranFoundVertex = 0
    numOfMappings = 0

    # Step One - First store the Maximally connected VNFs and their Neighbors in a list of sets

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
                maxCncList.append(maxCncVertexNeighbor)

        maximalConnectedVnfs.append(maxCncList)
    
    for vertex in totalNetwork.vertices():
        totalNetwork.vp.binaryMappingVar[vertex] = 0

    # Step Two - Mapping the Neighborhoods

    for neighborhood in maximalConnectedVnfs:

        isFirstFailed = False
        isFirst = True

        for vnf_vertex in neighborhood:

            ranFoundVertex = vnf_vertex
            mappableSbsTowers = []

            sbsPositiveDifference = []
            sbsNegativeDifference = []
            negativeSbsIndex = -1
            positiveSbsIndex = -1
            finalSbsIndex = -1

            # Check if the first has a mapped neighbor

            isMainVnfMapped = False

            if totalNetwork.vp.binaryMappingVar[ranFoundVertex] == 2 or totalNetwork.vp.binaryMappingVar[ranFoundVertex] == 1:
                continue

            for neighbors in ranFoundVertex.all_neighbors():
                if totalNetwork.vp.binaryMappingVar[neighbors] == 1:
                    isMainVnfMapped = True
                    break
                else:
                    continue

            # If the vnf does not have a mapped neighbor
            if not isMainVnfMapped:
                # Try to find the Sbs Tower which would be most appropriate
                sbsNetwork = find_vertex(totalNetwork, totalNetwork.vp.graphName, "Substrate")

                # Find the Towers which can provide it with resources as well as Highest Insurance for its Neighbors
                for sbsTower in sbsNetwork:
                    if totalNetwork.vp.resourceCapacity[sbsTower] >= totalNetwork.vp.resources[ranFoundVertex]:
                        mappableSbsTowers.append(sbsTower)

                # Even it has failed we still continue to try and find its best sbs tower
                if not mappableSbsTowers:

                    print("Failure has occured (Case I due to Resources)")
                    totalNetwork.vp.binaryMappingVar[ranFoundVertex] = 2

                    updateList = []
                    updateList.append(ranFoundVertex)

                    for neighbors in ranFoundVertex.all_neighbors():
                        updateList.append(neighbors)

                    for updateVnfFunction in updateList:
                        totalNetwork.vp.totalResourcesAcc[updateVnfFunction] -= totalNetwork.vp.totalResourcesAcc[ranFoundVertex]

                    if isFirst:
                        print("The failure is the first")
                        isFirstFailed = True
                        break
                    else:
                        isFirst = False
                        continue

                # Looping to find the Sbs Neighborhood Differences

                for sbsTower in mappableSbsTowers:
                    if (totalNetwork.vp.totalResourcesAcc[sbsTower] - totalNetwork.vp.totalResourcesAcc[ranFoundVertex]) >= 0:
                        sbsPositiveDifference.append(totalNetwork.vp.totalResourcesAcc[sbsTower] - totalNetwork.vp.totalResourcesAcc[ranFoundVertex])
                        sbsNegativeDifference.append(-1000000)
                    elif (totalNetwork.vp.totalResourcesAcc[sbsTower] - totalNetwork.vp.totalResourcesAcc[ranFoundVertex]) <= 0:
                        sbsNegativeDifference.append(totalNetwork.vp.totalResourcesAcc[sbsTower] - totalNetwork.vp.totalResourcesAcc[ranFoundVertex])
                        sbsPositiveDifference.append(1000000)

                sbsPositiveDifference = np.asarray(sbsPositiveDifference)
                sbsNegativeDifference = np.asarray(sbsNegativeDifference)

                # Make Imporovements - Improve way of accomdating neighborhoods to Required Spots (Look at Notion Improvements Page)
                # Another Improvement - Add all the like differences to a list (Allowing to check for the most connected Sbs Tower and take that one instead.)
                if sbsPositiveDifference.size > 0:
                    positiveSbsIndex = sbsPositiveDifference.argmin()
                    finalSbsIndex = positiveSbsIndex
                elif sbsNegativeDifference.size > 0:
                    negativeSbsIndex = sbsNegativeDifference.argmax()
                    finalSbsIndex = negativeSbsIndex
                else:
                    print("A Failure Has Occured! Why would this happen?")
                    exit

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

                # First we must find all the sbs towers our vnf neighbors are mapped to ( Approach Similar to Algo One )
                
                mappedVnfSbsNeighbor = []

                for mappedVnfFunction in mappedVnfNeighbor:
                    edgeConnections = find_edge(totalNetwork, totalNetwork.ep.bandwidth, 0)

                    if not edgeConnections:
                        print("No Connections Have Been Made! How is this possible")
                        exit

                    for edge in edgeConnections:
                        if edge.source() == mappedVnfFunction:
                            mappedVnfSbsNeighbor.append(edge.target())
                            break
                        elif edge.target() == mappedVnfFunction:
                            mappedVnfSbsNeighbor.append(edge.source())
                            break

                # List of Neighborhood Lists to find the intersections
                neighborhoodList = []

                for neighborVnfFunction in mappedVnfSbsNeighbor:
                    neighborhood = []
                    neighborhood.append(totalNetwork.vertex_index[neighborVnfFunction])

                    for neighbors in neighborVnfFunction.all_neighbors():
                        neighborhood.append(totalNetwork.vertex_index[neighbors])

                    neighborhoodList.append(neighborhood)

                # Now that we have the neighborhood list we can now find the interesection
                # Not using mappableSbsTowers since it is not a set
                possibleSbsTowers = set(neighborhoodList[0])

                # Finding the Sbs Tower that matches all the connections
                for neighborhood in neighborhoodList[1:]:
                    possibleSbsTowers.intersection_update(neighborhood)

                if not possibleSbsTowers:
        
                    print("Failure has occured ( Case II Due to Connections )")
                    totalNetwork.vp.binaryMappingVar[ranFoundVertex] = 2

                    updateList = []
                    updateList.append(ranFoundVertex)

                    for neighbors in ranFoundVertex.all_neighbors():
                        updateList.append(neighbors)

                    for updateVnfFunction in updateList:
                        totalNetwork.vp.totalResourcesAcc[updateVnfFunction] -= totalNetwork.vp.totalResourcesAcc[ranFoundVertex]

                    if isFirst:
                        print("The failure is the first")
                        isFirstFailed = True
                        break 
                    else:
                        isFirst = False
                        continue

                # Now out of this list we must check for resource possibility

                for vertexIndex in possibleSbsTowers:
                    mappableSbsTowers.append(totalNetwork.vertex(vertexIndex))

                print(len(mappableSbsTowers))

                resRefinedMappable = []

                for sbsTower in mappableSbsTowers:
                    if totalNetwork.vp.resourceCapacity[sbsTower] >= totalNetwork.vp.resources[ranFoundVertex]:
                        resRefinedMappable.append(sbsTower)

                mappableSbsTowers = resRefinedMappable

                # Checking again for Failure

                if not mappableSbsTowers:

                    print("Failure has occured ( Case II Due to Resources ")
                    totalNetwork.vp.binaryMappingVar[ranFoundVertex] = 2

                    updateList = []
                    updateList.append(ranFoundVertex)

                    for neighbors in ranFoundVertex.all_neighbors():
                        updateList.append(neighbors)

                    for updateVnfFunction in updateList:
                        totalNetwork.vp.totalResourcesAcc[updateVnfFunction] -= totalNetwork.vp.totalResourcesAcc[ranFoundVertex]

                    if isFirst:
                        print("The failure is the first")
                        isFirstFailed = True
                        break
                    else:
                        isFirst = False
                        continue

                # Checking for Bandwidth of the connections

                # We have now gotten our Mapped Neighbor VNFs and their Corresponding Sbs Towers ( Which they are mapped to )
                # Let us now Firstly, create a list of the bandwidth of the edges between the ranFoundVertex and its neighbors.

                vnfNeighborBand = []

                for vnfFunction in mappedVnfNeighbor:
                    # Let us first find the edge between the vnfFunction Neighbor and the ranFoundVertex
                    for neighborEdge in ranFoundVertex.all_edges():
                        if neighborEdge.source() == vnfFunction or neighborEdge.target() == vnfFunction:
                            vnfNeighborBand.append(totalNetwork.ep.bandwidth[neighborEdge])
                            break

                # Now let us find the same for the substarte towers

                sbsNeighborBand = []

                for sbsTower in mappableSbsTowers:

                    towerN = []

                    # Each mapable tower needs to be compared with the vnf neighbors corresponding sbs towers.
                    for vnfMappedSbs in mappedVnfSbsNeighbor:

                        # Taking care of the fact that one of the mappable sbs towers could be the mappedVnfSbsNeighbor
                        if sbsTower == vnfMappedSbs:
                            towerN.append(0)
                            continue

                        if vnfMappedSbs in sbsTower.all_neighbors():
                            print("I am here")

                        # Now let us try finding the edge between these towers and add their bandwidth info to the list.
                        for neighborEdge in vnfMappedSbs.all_edges():
                            if neighborEdge.source() == sbsTower or neighborEdge.target() == sbsTower:
                                towerN.append(totalNetwork.ep.bandwidth[neighborEdge])
                                break

                    # Is this an issue ?
                    sbsNeighborBand.append(towerN)

                # Now that we have our Bandwidth information for Sbs and Vnfs let make a comparison so as to refine our list.

                booleanList = []
                print(len(mappableSbsTowers))
                print(vnfNeighborBand)
                print(sbsNeighborBand)

                for sbsBandComp in sbsNeighborBand:
                    
                    passBandTest = True

                    for ctrVar in range(len(vnfNeighborBand)):
                        if sbsBandComp[ctrVar] == 0:
                            continue
                        elif vnfNeighborBand[ctrVar] > sbsBandComp[ctrVar]:
                            passBandTest = False
                            break

                    if not passBandTest:
                        booleanList.append(False)
                    else:
                        booleanList.append(True)

                bandRefinedMapping = []

                for ctrVar in range(len(mappableSbsTowers)):
                    if booleanList[ctrVar]:
                        bandRefinedMapping.append(mappableSbsTowers[ctrVar])

                if not bandRefinedMapping:

                    print("Failure has occured (Case II Due to Bandwidth)")
                    totalNetwork.vp.binaryMappingVar[ranFoundVertex] = 2

                    updateList = []
                    updateList.append(ranFoundVertex)

                    for neighbors in ranFoundVertex.all_neighbors():
                        updateList.append(neighbors)

                    for updateVnfFunction in updateList:
                        totalNetwork.vp.totalResourcesAcc[updateVnfFunction] -= totalNetwork.vp.totalResourcesAcc[ranFoundVertex]

                    if isFirst:
                        print("The failure is the first")
                        isFirstFailed = True
                        break
                    else:
                        isFirst = False
                        continue

                mappableSbsTowers = bandRefinedMapping

                # After doing so we will check which of the compatible Sbs Towers has the closest Total Resource Acc compared to the Neighborhood being dealt with.

                # Looping to find the Sbs Neighborhood Differences

                for sbsTower in mappableSbsTowers:
                    if (totalNetwork.vp.totalResourcesAcc[sbsTower] - totalNetwork.vp.totalResourcesAcc[ranFoundVertex]) >= 0:
                        sbsPositiveDifference.append(totalNetwork.vp.totalResourcesAcc[sbsTower] - totalNetwork.vp.totalResourcesAcc[ranFoundVertex])
                        sbsNegativeDifference.append(-1000000)
                    elif (totalNetwork.vp.totalResourcesAcc[sbsTower] - totalNetwork.vp.totalResourcesAcc[ranFoundVertex]) <= 0:
                        sbsNegativeDifference.append(totalNetwork.vp.totalResourcesAcc[sbsTower] - totalNetwork.vp.totalResourcesAcc[ranFoundVertex])
                        sbsPositiveDifference.append(1000000)

                sbsPositiveDifference = np.asarray(sbsPositiveDifference)
                sbsNegativeDifference = np.asarray(sbsNegativeDifference)

                # Make Imporovements - Improve way of accomdating neighborhoods to Required Spots (Look at Notion Improvements Page)
                # Another Improvement - Add all the like differences to a list (Allowing to check for the most connected Sbs Tower and take that one instead.)
                if sbsPositiveDifference.size > 0:
                    positiveSbsIndex = sbsPositiveDifference.argmin()
                    finalSbsIndex = negativeSbsIndex
                elif sbsNegativeDifference.size > 0:
                    negativeSbsIndex = sbsNegativeDifference.argmax()
                    finalSbsIndex = negativeSbsIndex
                else:
                    # Could optimize this PORTION as well ( Dont know if giving the next vertex the title of First would be a good idea )
                    # Maybe Try Just Finding the closest sbs instead ( in terms of Total Resources Acc. )
                    print("A Failure Has Occured! Why would this happen? (Case II)")
                    exit

                # We have found our Primary Sbs Neighborhood !!
                sbsFoundVertex = mappableSbsTowers[finalSbsIndex]

                # Let us now Perform the Mapping

                totalNetwork.add_edge(sbsFoundVertex, ranFoundVertex)
                totalNetwork.vp.binaryMappingVar[ranFoundVertex] = 1
                numOfMappings += 1
                totalNetwork.vp.resourceCapacity[sbsFoundVertex] -= totalNetwork.vp.resources[ranFoundVertex]

                # Must Update the Total Resources Acc For Sbs Tower and Its Neighbors
                updateSbsList = []
                updateSbsList.append(sbsFoundVertex)

                for updateFunction in updateSbsList:
                    totalNetwork.vp.totalResourcesAcc[updateFunction] -= totalNetwork.vp.resources[ranFoundVertex]

                isFirst = False
    
    return numOfMappings;