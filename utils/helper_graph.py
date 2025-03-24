from typing import List, Dict, Optional
from collections import deque
import time
"""
graph: Dict[int, List[int]]
graph = {
    1: [2,4],
    2: [1,3],
    3: [2,4],
    4: [1,3]
}

"""
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
        

def print_node(node: Node):
    if not node:
        return
    print(f"node.val: {node.val}")
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

def buid_adjlist(n: int, edges: List[List[int]]) -> Dict:
    graph = {}
    for i in range(n):
        graph[i] = []
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    return graph

def build_graph(adjList: List[List[int]]) -> 'Node':
    """ Constructs a graph from adjacency list and returns the first nodes """
    if not adjList:
        return None
    # nodes = {i + 1: Node(i+1) for i in range(len(adjList))}

    nodes = {}
    for i in range(len(adjList)):
        nodes[i+1] = Node(i + 1)
    # print(nodes)
    # print_graph(nodes[1])
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
