from typing import List, Dict
from collections import deque

class Node:
    """ Definition for a graph nodes. """
    def __init__(self, val = 0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def print_node_and_neighbors(node: 'Node'):
    if not node:
        return
    print(f"\nnode.val: {node.val}")
    nei = []
    for neighbor in node.neighbors:
        nei.append(neighbor.val)
    print(f"Neighbors: {nei}")

def print_graph(node: Node):
    if not node:
        print("Graph is empty.")
        return
    visited = set()
    queue = deque([node])

    print("Graph Representation:")
    while queue:
        curr = queue.popleft()
        #if curr in visited:
        #    continue
        visited.add(curr)

        # Print current node and its neighbors
        neighbors_vals = [neighbor.val for neighbor in curr.neighbors]
        print(f"Node {curr.val}: {neighbors_vals}")
        
        for neighbor in curr.neighbors:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

def build_graph(adjList: List[List[int]]) -> 'Node':
    if not adjList:
        return None
    nodes = {}
    for i in range(len(adjList)):
        nodes[i + 1] = Node(i+1)
    #nodes = {i + 1: Node(i+1) for i in range(len(adjList))}
    for i, neighbors in enumerate(adjList):
        for n in neighbors:
            nodes[i+1].neighbors.append(nodes[n])
    return nodes[1]

def graph_to_adjList(node: 'Node') -> List[List[int]]:
    """ Converts a graph to an adjacency list format for testing. """
    if not node:
        return []
    adjList = {}
    queue = deque([node])
    visited = set([node])
    
    while queue:
        curr = queue.popleft()
        adjList[curr.val].append(neighbor.val)

        for neighbor in curr.neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)



adjList = [[2,4], [1,3], [2,4], [1,3]]
graph = build_graph(adjList)
print_graph(graph)
