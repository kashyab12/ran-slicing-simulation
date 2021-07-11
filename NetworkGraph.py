from graph_tool.all import *
import math
import random
import numpy as np
import MathTools as math
from matplotlib import pyplot as plt

# Blueprint class for the Substrate Network and RAN Slices.
class NetworkGraph(Graph):

	'''
	Aim: To setup the Network via calling the Super Constructor (via GraphTools)
	Issue(s):
		- None as of yet.
	'''
	def __init__(self, num_nodes, edge_matrix, random_edges):

		# Calling the Super Class Constructor
		super(NetworkGraph, self).__init__(directed=False)

		# Setting up the properties for the Network
		self.create_network_properties()

		# Building the Network Graph
		self.build_network_graph(num_nodes, edge_matrix, random_edges)

	'''
	Aim : To Create the Network Properties for the Network Graph.
	Issue(s): 
		- None as of yet
	'''
	def create_network_properties(self):

		# Setting up the Graph Name Property
		graph_name_prop = self.new_vertex_property("string")
		self.vp.graph_name = graph_name_prop

		# Giving the Vertices a Resource Capacity Property
		resource_cap_prop = self.new_vertex_property("int")
		self.vp.resource_cap = resource_cap_prop

		# Giving the Vertices a Resource Property
		resource_prop = self.new_vertex_property("int")
		self.vp.resource = resource_prop

		# Giving the Vertices a Capacity Property
		capacity_prop = self.new_edge_property("int")
		self.ep.capacity = capacity_prop

		# Giving the Vertices a Mapping Variable Property
		mapping_var_prop = self.new_vertex_property("int")
		self.vp.mapping_var = mapping_var_prop

	# Add the vertices and edges to the Network Graph
	def build_network_graph(self, num_nodes, edge_matrix, random_edges):   

		# Creating the set of Substrate Nodes.
		node_array = []

		# Creating the Substrate Nodes and adding them to the set.

		for ctr_var in range(num_nodes):
			node_array.append(self.add_vertex())

		node_array = np.array(node_array)

		if random_edges:
			
			for node in node_array:
				
				random_degree = np.random.randint(1, num_nodes)
				ctr_var = 0

				while ctr_var < random_degree:

					try:
						random_node = random.choice([rand_node for rand_node in node_array if rand_node 
																		not in self.get_all_edges(node) and rand_node != node])
					except:
						break
					
					self.add_edge(node, random_node)
					ctr_var += 1
		else:
		
			# Iterating through 2D Array of Edge Values and Creating the Connections
			x_ctr = 0

			for y_ctr in range(np.shape(edge_matrix)[0]):

				# Symmetric Matrix due to which certain indices need not be visited.
				x_ctr = y_ctr

				while x_ctr in range(np.shape(edge_matrix)[1]):

					if y_ctr == x_ctr or edge_matrix[y_ctr][x_ctr] == 0:
						pass
					else:
						self.add_edge(node_array[y_ctr], node_array[x_ctr])

					x_ctr += 1

	def set_vertex_name_property(self, graph_nodes, vertex_name, init_ctr):
		
		for node in graph_nodes:
			self.vp.graph_name[node] = vertex_name + str(init_ctr)
			init_ctr += 1

	def set_res_cap_property(self, graph_nodes, resource_cap_arr, random_res_cap):

		# Populating the Resource Cap array in case of random being True
		if random_res_cap:
			resource_cap_arr = np.random.randint(self.MIN_RES_CAP, high=self.MAX_RES_CAP+1, size= (np.shape(graph_nodes)[0]))

		# Setting the Resource Cap for the Nodes within the graph_nodes list.
		for node, res_cap in np.c_[graph_nodes, resource_cap_arr]:
			self.vp.resource_cap[node] = res_cap
 
	def set_res_property(self, graph_nodes, resource_arr, random_res):

		# Populating the Resource Cap array in case of random being True
		if random_res:
			resource_arr = np.random.randint(self.MIN_RES, high=self.MAX_RES+1, size= np.shape(graph_nodes)[0])

		# Setting the Resource Cap for the Nodes within the graph_nodes list.
		for node, res in np.c_[graph_nodes, resource_arr]:
			self.vp.resource[node] = res


	def set_capacity_property(self, graph_edges, capacity_vector, random_edges):
		
		if random_edges:
			capacity_vector = np.random.randint(self.MIN_CAPACITY, high=self.MAX_CAPACITY+1, size= np.shape(graph_edges)[0])
		
		for edge, capacity_val in np.c_[graph_edges, capacity_vector]:
			self.ep.capacity[edge] = capacity_val

	def set_mapping_property(self, graph_nodes, mapping_var_vector):
		
		for node, mapping_var_val in np.c_[graph_nodes, mapping_var_vector]:
			self.vp.mapping_var[node] = mapping_var_val


	def visualize_network(self, prop = "graph_name"):

		graph_draw(self, vertex_text = self.vp.get(prop))

	
