import networkx as nx
import matplotlib.pyplot as plt
import random

# Create a random TSP instance with N cities
N = 10
random.seed(0)  # For reproducibility
cities = {i: (random.uniform(0, 10), random.uniform(0, 10)) for i in range(N)}

# Create a complete graph with cities as nodes
G = nx.Graph()

# Add cities as nodes with positions
for city, pos in cities.items():
    G.add_node(city, pos=pos)

# Calculate distances between cities (Euclidean distance)
distances = {(city1, city2): ((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2) ** 0.5 for city1, pos1 in cities.items() for city2, pos2 in cities.items() if city1 != city2}

# Add edges to the graph with distances as weights
for (city1, city2), distance in distances.items():
    G.add_edge(city1, city2, weight=distance)

# Solve the TSP using the nearest neighbor algorithm
tour = list(nx.approximation.traveling_salesman_problem(G, cycle=True))

# Calculate the total tour distance
total_distance = sum(G[city1][city2]['weight'] for city1, city2 in zip(tour, tour[1:]))

# Plot the TSP tour
pos = nx.get_node_attributes(G, 'pos')
nx.draw(G, pos, with_labels=True, node_size=100, node_color='lightblue')
nx.draw_networkx_edges(G, pos, edgelist=[(tour[i], tour[i + 1]) for i in range(N - 1)], edge_color='red', width=2)
nx.draw_networkx_edges(G, pos, edgelist=[(tour[N - 1], tour[0])], edge_color='red', width=2)
plt.title(f'TSP Tour (Total Distance: {total_distance:.2f})')
plt.show()
