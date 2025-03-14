from typing import List, Dict
from collections import deque
from utils import *

adjList = [[2,4], [1,3], [2,4], [1,3]]
graph = build_graph(adjList)
print_graph(graph)
