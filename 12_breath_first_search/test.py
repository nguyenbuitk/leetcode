import networkx as nx
import matplotlib.pyplot as plt
from ascii_graph import Pyasciigraph


def visualize_graph_ascii(graph):
    G = nx.Graph(graph)

    # Convert edges to a textual format
    edges = []
    for u, v in G.edges():
        edges.append(f"{u} -- {v}")

    # Generate ASCII representation
    graph_visual = Pyasciigraph()
    for line in graph_visual.graph("Graph Visualization", [(edge, 1) for edge in edges]):
        print(line)


# Define the graph
graph = {
    0: [1, 2],
    1: [0],
    2: [0],
    3: [4, 5],
    4: [3, 5],
    5: [3, 4]
}

# Visualize the graph in ASCII
visualize_graph_ascii(graph)
