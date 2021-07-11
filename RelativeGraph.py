import Substrate as sbs
import RAN_Slice as ran
import AlgorithmOne as algoOne
import AlgorithmTwo as algoTwo
import AlgorithmThree as algoThree
import AlgorithmFour as algoFour
from graph_tool.all import *
import RembedAlgo as rm_algo
import random

class RelativeGraph(Graph):

	# Setting up the Relative Graph via the Total Network provided.
	def __init__(self, total_network, failed_vnf_set):

		# Calling the Super Class Constructer to instantiate the Graph
		super(RelativeGraph, self).__init__(directed=False)
		
		# Creating the required properties for the Relative Graph
		self.create_mwis_properties(self)

		# Calling the build function in order to create the Relative Graph
		self.build_graph(self, total_network)

	def create_mwis_properties(self):
		
		# Giving each vertex a name
		vertex_name_prop = self.new_vertex_property("string")
		self.vp.vertex_name = vertex_name_prop

		# Giving each vertex a weight property
		weight_prop = self.new_vertex_property("float")
		self.vp.weight = weight_prop

		# Giving the vertex an is_live property
		live_prop = self.new_vertex_property("int")
		self.vp.is_live = live_prop

		# Giving an edge descriptor for Strong and Weak Edges
		strength_prop = self.new_edge_property("string")
		self.ep.strength = strength_prop

		# Giving the edge neighborhood property
		neighbor_prop = self.new_edge_property("uint8_t")
		self.ep.is_neighbor = neighbor_prop

		# Giving the edge an is_failed property
		failure_prop = self.new_edge_property("uint8_t")
		self.ep.is_failed = failure_prop

	# This method handles the building of the Relative Graph via the Nodes and Edges
	def build_graph(self, total_network):
		
		# Creating the VNF set and adding all the VNF's via the total_network to it
		vnf_set = set()

		for node in total_network.vertices():
			if total_network.vp.mapping_var[node] >= 0:
				vnf_set.add(node)

		# Iterating through the set of VNF and Adding a Node for every Substrate Tower it can visit

		for vnf in vnf_set:



	# Calculation of the Weight for the vertices of the graph
	def calculate_weights(self):
		pass

	def find_mwis(self):
		pass



		