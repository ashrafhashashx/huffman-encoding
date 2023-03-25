import networkx as nx
import matplotlib.pyplot as plt

# create a binary tree
G = nx.Graph()
G.add_node(1, label="Node 1")
G.add_node(2, label="Node 2")
G.add_node(3, label="Node 3")
G.add_node(4, label="Node 4")
G.add_node(5, label="Node 5")
G.add_node(6, label="Node 6")
G.add_node(7, label="Node 7")

G.add_edge(1, 2)
G.add_edge(1, 3)
G.add_edge(2, 4)
G.add_edge(2, 5)
G.add_edge(3, 6)
G.add_edge(3, 7)

print(G)

print(len(G.nodes.items()))

# define positions of the nodes
pos = {1: (0, 0), 2: (-1, -1), 3: (1, -1), 4: (-2, -2), 5: (0, -2), 6: (2, -2), 7: (4, -2)}

# draw the nodes with labels
for node in G.nodes():
    label = G.nodes[node]['label']
    circle = plt.Circle(pos[node], radius=0.2, color='white')
    plt.gca().add_patch(circle)
    plt.text(pos[node][0], pos[node][1], label, color='black', ha='center', va='center')

# draw the edges
for edge in G.edges():
    start_pos = pos[edge[0]]
    end_pos = pos[edge[1]]
    dx = end_pos[0] - start_pos[0]
    dy = end_pos[1] - start_pos[1]
    arrow = plt.Arrow(start_pos[0], start_pos[1], dx, dy, width=0.05)
    plt.gca().add_patch(arrow)

# set the axis limits and show the plot
plt.axis('equal')
plt.axis('off')
plt.show()
