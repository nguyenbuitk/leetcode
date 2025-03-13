from typing import Optional, List
from collections import deque

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        root = Node(node.val)
        queue_root = deque([root])
        
        queue = deque([node])
        visited = set([node.val])
        while queue:
            node = queue.popleft()
            root = queue_root.popleft()
            
            for neighbor in node.neighbors:
                if neighbor.val not in visited:
                    print(f"node: {neighbor.val}")
                    visited.add(neighbor.val)
                    queue.append(neighbor)
                    
                    root.neighbors.append(neighbor)
                    queue_root.append(neighbor)
        return root
    
## helper function 
def build_graph(adjList: List[List[int]]) -> 'Node':
    """ Constructs a graph from an adjacency list and returns the first node. """
    if not adjList:
        return None
    nodes = {}
    for i in range(len(adjList)):
        nodes[i+1] = Node(i+1)
    
    for i, neighbors in enumerate(adjList):
        nodes[i+1].neighbors = [nodes[n] for n in neighbors]
        
    return nodes[1]
    