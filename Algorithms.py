from graph_tool.all import *
import random

def algorithmOne(totalNetwork, resList, resCapList, substrateNetwork):

    sortedResValList = sorted(resList, reverse=True)
    sortedSbsValList = sorted(resCapList, reverse=True)
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
                    sortedSbsValList = sorted(sortedSbsValList, reverse=True)
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
                        if possibleSbsTower[0] in mappableSbsTowers or possibleSbsTower[0] in unmappableTowers:
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
                        break
                
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
                        sortedSbsValList = sorted(sortedSbsValList, reverse=True)

    return numOfMappings;


def algorithmsTwo(totalNetwork,substrateNetwork, maxCncVnfList, maxCncSubList):
        
    sortedVnfCncList = sorted(maxCncVnfList, reverse=True)    #change the name of the RanCnclist         
    sortedSbsCncList = sorted(maxCncSubList, reverse=True)    #chnage the name of the SbsCnclsit
    isNeighborMapped = False
    sbsFoundVertex = 0
    numOfMappings = 0
    ranFoundVertex = 0

    for vnfCncValue in sortedVnfCncList: # Checking for the max
        
        foundVnfvert = False
        vnfFoundVertex = find_vertex(totalNetwork, totalNetwork.vp.connection, vnfCncValue)
            
        for sbsCncValue in sortedSbsCncList: # Checking for the max 
            foundSbsvert = False
            sbsFoundVertex = find_vertex(totalNetwork, totalNetwork.vp.connection, sbsCncValue)
            
        ctrVar = len(ranFoundVertex) - 1

        while ctrVar >= 0:
            if totalNetwork.vertex_properties.binaryMappingVar[vnfFoundVertex[ctrVar]] == 0:
                vnfFoundVertex = vnfFoundVertex[ctrVar]
                foundSbsVert = True
                break
            else:
                del vnfFoundVertex[ctrVar]
                ctrVar -= 1
                
        ctrVar = len(vnfFoundVertex) - 1

        while ctrVar >= 0:
            if totalNetwork.vertex_properties.binaryMappingVar[sbsFoundVertex[ctrVar]] == 0:
                sbsFoundVertex = sbsFoundVertex[ctrVar]
                foundSbsVert = True
                break
            else:
                del sbsFoundVertex[ctrVar]
                ctrVar -= 1
                
        if not vnfFoundVertex:
            print("Empty List of Found VNF Functons")
        if not sbsFoundVertex:
            print("Empty List of Found Substrate Functons")
            
            #case One

        if isNeighborMapped == False:
            sbsFoundVertex = find_vertex(totalNetwork, totalNetwork.vp.connection, sortedVnfCncList[0])
            vnfFoundVertex = find_vertex(totalNetwork, totalNetwork.vp.connection, sortedSbsCncList[0])
                
        if totalNetwork.vertex_properties.resourceCapacity[sbsFoundVertex[0]] >= vnfFoundVertex[0]: 
            foundSbsVert = True
        if foundSbsVert == False:
                print("Failed VNF Mapping Case One")
                totalNetwork.vp.binaryMappingVar[sbsFoundVertex[0]] = 2
        else: # Mapping Case One 
            totalNetwork.add_edge(sbsFoundVertex[0], vnfFoundVertex[0])
            totalNetwork.vp.binaryMappingVar[vnfFoundVertex[0]] = 1
            numOfMappings +=1
            
        #Case two        
        if totalNetwork.vp.binaryMappingVar[vnfFoundVertex[0]]==1:
            if totalNetwork.vertex_properties.resourceCapacity[sbsFoundVertex[0]] >= vnfFoundVertex[1]:
                totalNetwork.add_edge(sbsFoundVertex[0], vnfFoundVertex[1])
                totalNetwork.vp.binaryMappingVar[vnfFoundVertex[1]] = 1
                numOfMappings +=1
                

