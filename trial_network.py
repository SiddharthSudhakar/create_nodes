import networkx as nx
import matplotlib.pyplot as plt


# Create graph instance
G = nx.Graph()

# Data node
cities_data = {"a": "Mumbai", "b": "Kolkata", "c": "Chennai"}

edge_list = [("a", "b"), ("b","c"), ("d","e"), ("c","f"), ("f", "e")]

G.add_edges_from( edge_list)

# Relabel nodes according to their labels
H = nx.relabel_nodes(G, cities_data)


print("Nodes of the graph", H.nodes())
print("Edges of the graph", H.edges())

print("Node type", type(H.nodes()))
print("Edges type", type(H.edges()))

# Plot it
nx.draw_networkx(H)
# plt.savefig("simple_path.png") # save as png
plt.show() # display