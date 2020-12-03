import networkx as nx
import matplotlib.pyplot as pypt
import math

# Creating Controlled Substrate Network

subsOne = nx.Graph()


#Creating the Towers

for i in range(1,6):
    subsOne.add_node('s' + str(i), resource = 4)

#Connections between towers

subsOne.add_edge('s1', 's3')
subsOne.add_edge('s1', 's5')

subsOne.add_edge('s2', 's3')
subsOne.add_edge('s2', 's4')
subsOne.add_edge('s2', 's5')

subsOne.add_edge('s3', 's4')

subsOne.add_edge('s4', 's5')

# Creating Controlled RAN Slices

ranSlices = []

for i in range (0,2):
    ranSlices.append(nx.Graph())

# For each RAN Slice we create Controlled VNF Functions

ranSlices[0].add_node('r11', resource = 3)
ranSlices[0].add_node('r12', resource = 3)
ranSlices[0].add_node('r13', resource = 1)

ranSlices[1].add_node('r21',  resource = 2)
ranSlices[1].add_node('r22',  resource = 3)

# Connecting the VNF Functions

ranSlices[0].add_edge('r11', 'r12')
ranSlices[0].add_edge('r11', 'r13')
ranSlices[0].add_edge('r11', 'r13')

ranSlices[1].add_edge('r21', 'r22')

# Connecting the Substrates with the VNF Functions of respective RAN Slices.

subsOne.add_edges_from(ranSlices[0].edges)
subsOne.add_edges_from(ranSlices[1].edges)

subsOne.add_edge('s2', 'r11')
subsOne.add_edge('s3', 'r12')
subsOne.add_edge('s4', 'r13')

subsOne.add_edge('s1', 'r21')
subsOne.add_edge('s5', 'r22')

layout = nx.spectral_layout(subsOne)
nx.draw(subsOne, layout, with_labels= 1)
# nx.draw_networkx_edge_labels(subsOne, layout)
pypt.show()