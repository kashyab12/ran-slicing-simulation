from graph_tool.all import *
import matplotlib.pyplot as ppt
import random
import numpy as np
import NetworkGraph as ng

class SubstrateNetwork(ng.NetworkGraph):

    # Default Constant Values for some vertex properities
    SUBSTRATE_VERTEX_NAME = "S"
    DEFAULT_RESOURCE_VALUE = -1
    DEFAULT_MAPPING_VAR = -1

    # Bounding values for the resource capacity and the capacity (In case of Random Values being TRUE)
    MIN_RES_CAP = 33
    MAX_RES_CAP = 50
    MIN_CAPACITY = 3
    MAX_CAPACITY = 5

    # Constructor for the SubstrateNetwork class
    def __init__(self, num_towers, resource_cap_arr=np.array([]),
                     random_res_cap=False, edge_matrix=np.array([]), random_edges = False):

        # Calling the Network Graph Super Constructer to setup properties and build the Substrate Graph
        super(SubstrateNetwork, self).__init__(num_towers, edge_matrix, random_edges)
    
        # Transforming Init Edge Matrix to a capacity_vector
        if not random_edges:
            capacity_vector = np.reshape(edge_matrix, edge_matrix.shape()[0] * edge_matrix.shape()[1])
            # Removing all the zero's which denote a lack of an edge
            capacity_vector = capacity_vector[capacity_vector != 0]
        else:
            capacity_vector = np.array([])

        # Setting the Vertex, Edge, and Graph Properties for the Substrate Network.
        sbs_nodes = [sbs_tower for sbs_tower in self.vertices()]
        self.set_sbs_tower_property(np.array(sbs_nodes), resource_cap_arr, random_res_cap, 
                                            capacity_vector, random_edges, first=True)

    def set_sbs_tower_property(self, sbs_nodes, resource_cap_arr, 
                                    random_res_cap, capacity_vector, random_edges, first=False):

        if first:
            vertex_ctr = 0
        else:
            vertex_ctr = len(self.vertices())

        # Setting up the Vertex Properties

        # Vertex Name Property
        self.set_vertex_name_property(sbs_nodes, SubstrateNetwork.SUBSTRATE_VERTEX_NAME, vertex_ctr)

        # Resource Capacity Property
        self.set_res_cap_property(sbs_nodes, resource_cap_arr, random_res_cap)

        # Resource Property
        resource_arr = np.arange(0, np.shape(sbs_nodes)[0])
        resource_arr.fill(SubstrateNetwork.DEFAULT_RESOURCE_VALUE)
        self.set_res_property(sbs_nodes, resource_arr, False)

        # Capacity Property
        sbs_edges = np.array(find_edge(self, self.ep.capacity, 0))
        self.set_capacity_property(sbs_edges, capacity_vector, random_edges)

        # Mapping Variable
        mapping_var_vector = np.arange(0, np.shape(sbs_nodes)[0])
        mapping_var_vector.fill(SubstrateNetwork.DEFAULT_MAPPING_VAR)
        self.set_mapping_property(sbs_nodes, mapping_var_vector)

        