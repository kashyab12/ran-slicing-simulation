import Substrate as sbs
import RAN_Slice as ran
import AlgorithmOne as algoOne
import AlgorithmTwo as algoTwo
import AlgorithmThree as algoThree
import AlgorithmFour as algoFour
from graph_tool.all import *
import RembedAlgo as rm_algo
import random

ran_slice = Graph(directed=False)

# Adding vertices
ran_slice.add_vertex(4)

# Add Edges
ran_slice.add_edge(0, 1)
ran_slice.add_edge(0, 2)
ran_slice.add_edge(2, 3)
ran_slice.add_edge(3, 1)

# Set Props
ran.setRANSliceProperties(ran_slice)

# Setting the degree
for vnf in ran_slice.vertices():
    ran_slice.vp.degree[vnf] = len(ran_slice.get_all_neighbors(vnf))

# Res Cap -> -1 and Binary Mapping Var = 0
for vnf in ran_slice.vertices():
    ran_slice.vp.resourceCapacity[vnf] = -1
    ran_slice.vp.binaryMappingVar[vnf] = 0
    
# Resources - > Custom Values

ran_slice.vp.resources[ran_slice.vertex(0)] = 2
ran_slice.vp.resources[ran_slice.vertex(1)] = 3
ran_slice.vp.resources[ran_slice.vertex(2)] = 1
ran_slice.vp.resources[ran_slice.vertex(3)] = 2

# VNF Edges -> Ignore for now

for edges in ran_slice.edges():
    ran_slice.ep.bandwidth[edges] = 1

# Output this graph

vnf_ctr = 1

for vnf in ran_slice.vertices():
    ran_slice.vp.graphName[vnf] = "v" + str(vnf_ctr)
    vnf_ctr += 1    
    
pos = planar_layout(ran_slice)

graph_draw(ran_slice, pos=pos, vertex_text = ran_slice.vp.get("graphName"), output="Failure-Case/custom_ran_slice.png", output_size= (1920, 1080))

# -------- Substrate Network ---------------

sbs_layer = Graph(directed=False)

# Adding vertices
sbs_layer.add_vertex(4)

# Add Edges
sbs_layer.add_edge(0, 1)
sbs_layer.add_edge(0, 2)
sbs_layer.add_edge(2, 3)

# Set Props
sbs.setSbsNetworkProperties(sbs_layer)

# Setting the deg property
for sbs in sbs_layer.vertices():
    sbs_layer.vp.degree[sbs] = len(sbs_layer.get_all_neighbors(sbs))

# Resources -> -1  and Binary Mapping Var = -1
for sbs in sbs_layer.vertices():
    sbs_layer.vp.resources[sbs] = -1
    sbs_layer.vp.binaryMappingVar[sbs] = -1
    
# Resource Capacity - > Custom Values

sbs_layer.vp.resourceCapacity[sbs_layer.vertex(0)] = 4
sbs_layer.vp.resourceCapacity[sbs_layer.vertex(1)] = 2
sbs_layer.vp.resourceCapacity[sbs_layer.vertex(2)] = 2
sbs_layer.vp.resourceCapacity[ran_slice.vertex(3)] = 3

# Sbs Edges -> Ignore for now

for edges in sbs_layer.edges():
    sbs_layer.ep.bandwidth[edges] = 5

# Output this graph

sbs_ctr = 1

for sbs in sbs_layer.vertices():
    sbs_layer.vp.graphName[sbs] = "S" + str(sbs_ctr)
    sbs_ctr += 1    
    
pos = planar_layout(sbs_layer)

graph_draw(sbs_layer, pos=pos, vertex_text = sbs_layer.vp.get("graphName"), output="Failure-Case/custom_sbs_layer.png", output_size= (1920, 1080))


## -------------- Creation of the total network ---------------------

total_network = Graph(directed=False)
total_network = graph_union(total_network, sbs_layer, include = True, internal_props=True)
total_network = graph_union(total_network, ran_slice, include = True, internal_props=True)

# Output the total network

# pos = planar_layout(total_network)

graph_draw(total_network, vertex_text = total_network.vertex_properties.get("graphName"), output="Failure-Case/total_network_layer.png", output_size= (1920, 1080))

# Create the connections between sbs and vnf

# V1 and S1

total_network.add_edge(0, 4)
total_network.vp.resourceCapacity[total_network.vertex(0)] = total_network.vp.resourceCapacity[total_network.vertex(0)] - total_network.vp.resources[total_network.vertex(4)] 
total_network.vp.binaryMappingVar[total_network.vertex(0)] = -2
total_network.vp.binaryMappingVar[total_network.vertex(4)] = 1

# V3 and S3

total_network.add_edge(2, 6)
total_network.vp.resourceCapacity[total_network.vertex(2)] = total_network.vp.resourceCapacity[total_network.vertex(2)] - total_network.vp.resources[total_network.vertex(6)] 
total_network.vp.binaryMappingVar[total_network.vertex(2)] = -2
total_network.vp.binaryMappingVar[total_network.vertex(6)] = 1

# V4 and S4

total_network.add_edge(3, 7)
total_network.vp.resourceCapacity[total_network.vertex(3)] = total_network.vp.resourceCapacity[total_network.vertex(3)] - total_network.vp.resources[total_network.vertex(7)] 
total_network.vp.binaryMappingVar[total_network.vertex(3)] = -2 # Sbs has a VNF emebedded.
total_network.vp.binaryMappingVar[total_network.vertex(7)] = 1 

# V2 Failed

total_network.vp.binaryMappingVar[total_network.vertex(5)] = 2 # Failed Mapping

graph_draw(total_network, vertex_text = total_network.vertex_properties.get("graphName"), output="Failure-Case/mapped_total_network_layer.png", output_size= (1920, 1080))

# Output the resource and binary mapping var. values

sbs_list = [sbs for sbs in total_network.vertices() if total_network.vp.graphName[sbs][0] == 'S']
vnf_list = [vnf for vnf in total_network.vertices() if total_network.vp.graphName[vnf][0] == 'v']

print("Substrate Towers Values After Mapping")

for sbs in sbs_list:
    print(str(total_network.vp.graphName[sbs]) + "|||   Resource Cap. = " + str(total_network.vp.resourceCapacity[sbs]) + "| Binary Value = " + str(total_network.vp.binaryMappingVar[sbs]))
    
print("VNF Values After Mapping")    

for vnf in vnf_list:
    print(str(total_network.vp.graphName[vnf]) + "|||   Resource Val. = " + str(total_network.vp.resources[vnf]) + "| Binary Value = " + str(total_network.vp.binaryMappingVar[vnf]))
    
def simulate_failure(total_network, failed_sbs):

    num_rembed = 0

    print("-----------------")
    print("Failure Sim")
    print("-----------------")

    print("Failure has occured for the Substrate Tower - " + str(total_network.vp.graphName[failed_sbs]))

    # Getting the set of failed vnf embedded to the failed_sbs
    failed_vnf_set_before_failure = set(vnf for vnf in total_network.get_all_neighbors(failed_sbs) if total_network.vp.binaryMappingVar[vnf] == 1)
    # Removing all the edges of the substrate tower
    total_network.clear_vertex(failed_sbs)
    # Removing the substrate tower
    total_network.remove_vertex(failed_sbs)
    # Now updating the set with the VNFs after the Sbs has been removed.
    failed_vnf_set = set()
    
    for vnf_fail in failed_vnf_set_before_failure:
        failure_node = find_vertex(total_network, total_network.vp.graphName, total_network.vp.graphName[vnf_fail])
        failed_vnf_set.add(failure_node[0])
    
    # Make the Mapping Variable equal to 0 (Test) Print the name of the vertices 
    print("The failed vnf set is given as -")
    for vnf in failed_vnf_set:
        total_network.vp.binaryMappingVar[vnf] = 0
        print(str(total_network.vp.graphName[vnf]) + "|||   " + str(total_network.vp.binaryMappingVar[vnf]))
        
    # (Test) Output the resulting graph
    graph_draw(total_network, vertex_text = total_network.vertex_properties.get("graphName"), output="Failure-Case/failed_total_network_layer.png", output_size= (1920, 1080))
    
    # Case (a) - Try to Rembed the possible VNFs via the Res. Alloc Algo
    
    mappings = algoTwo.algorithmTwo(total_network, list(failed_vnf_set), failure=True) # Debug Output
    
    print("The Number of Mappings is given as - " + str(mappings)) # Print the number of embeddings
    
    graph_draw(total_network, vertex_text = total_network.vertex_properties.get("graphName")) # Displaying the graph after running the res alloc algo
    
    if mappings == len(failed_vnf_set):
        print("Number of Rembeddings = " + str(num_rembed))
    else:
        tm_algo.algoOne(total_network, num_rembed, )

    
    

    
simulate_failure(total_network, total_network.vertex(3))

