# Easy
## 1971. Find if Path Exists in Graph
Problem Statement:
------------------
There is a bi-directional graph with `n` vertices, where each vertex is labeled from `0` to `n - 1` (inclusive).
The edges in the graph are represented as a 2D integer array `edges`, where each `edges[i] = [uᵢ, vᵢ]` denotes 
a bi-directional edge between vertex `uᵢ` and vertex `vᵢ`. 

- Every vertex pair is connected by **at most one** edge.
- No vertex has an edge to itself.

You want to determine if there is a **valid path** that exists from vertex `source` to vertex `destination`.

Given `edges` and the integers `n`, `source`, and `destination`, return `true` if there is a **valid path** 
from `source` to `destination`, or `false` otherwise.

Example 1:
----------
Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
Output: true

Explanation:
There are two paths from vertex 0 to vertex 2:
- 0 → 1 → 2
- 0 → 2
```
    0
   / \
  1 - 2
```