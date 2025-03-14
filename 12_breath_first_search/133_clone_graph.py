from typing import Optional, List
from collections import deque
from utils import *

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        clones = {node: Node(node.val)}  # Store cloned nodes
        #print_graph(node)
        
        queue = deque([node])  # BFS queue
        
        while queue:
            print(f"\ncurrent cloned graph:")
            print_graph(clones[node])
            curr = queue.popleft()
            for neighbor in curr.neighbors:
                if neighbor not in clones:  # it also mean neighbor not in the original node
                    clones[neighbor] = Node(neighbor.val)  # Clone the node
                    queue.append(neighbor)  # Add to BFS queue
                
                # Add cloned neighbor to the cloned node's neighbors list
                clones[curr].neighbors.append(clones[neighbor])
        
        return clones[node]

adjList= [[2,4], [1,3], [2,4], [1,3]]
graph = build_graph(adjList)

solution = Solution()
clone_graph = solution.cloneGraph(graph)
