import networkx as nx

# Create an empty graph
G = nx.Graph()

# Add nodes to the graph
G.add_node("A")
G.add_node("B")
G.add_node("C")
G.add_node("D")
G.add_node("E")

# Add edges to the graph (defining connections between nodes)
G.add_edge("A", "B", weight=2)
G.add_edge("A", "C", weight=1)
G.add_edge("B", "D", weight=3)
G.add_edge("C", "D", weight=4)
G.add_edge("D", "E", weight=5)

# Find the shortest path between nodes "A" and "E"
shortest_path = nx.shortest_path(G, source="A", target="E", weight="weight")

# Calculate the shortest path length
shortest_path_length = nx.shortest_path_length(G, source="A", target="E", weight="weight")

print("Shortest Path from A to E:", shortest_path)
print("Shortest Path Length:", shortest_path_length)
