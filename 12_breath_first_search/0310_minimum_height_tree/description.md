# Medium
## 310. Minimum Height Trees
A tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.

Given a `tree` of `n` nodes labelled from `0` to `n - 1`, and an array of `n - 1` edges where `edges[i] = [ai, bi]` indicates that there is an undirected edge between the two nodes `ai` and `bi` in the tree, you can choose any node of the tree as the root. When you select a node x as the root, the result tree has height h. Among all possible rooted trees, those with minimum height (i.e. min(h))  are called minimum height trees (MHTs).

Return a list of all MHTs' root labels. You can return the answer in any order.

The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.

# Key Idea
## Approach 1 - BFS self
### [Link script](./approach_1.py)
This solution is brute-force and inefficient
- It treat **every node** as a potential root and performs BFS on each node, leading to `O(n^2)` complexity
- It recomputes tree height from scratch for each node

## Approach 2 - BFS chatgpt
### [Link scripts](./approach_2.py)
**Some thoughts**
- A tree is an acyclic undirected graph
- MHTs are always **located near the middle of the longest path** in tree
- Instead of checking every node, **prune the tree layer by layer from the leaves inward**
- When 1 or 2 nodes remain, they are MHT roots
- using `adjList, inDegree = {}, {}`, to build graph, track the connect edge of vertice

**Why only 1 or 2 MHT roots?**
- The **diameter of a tree** is the **longest path** between any two nodes in the tree.
- The center(s) of the tree are the nodes closest to the middle of this logest path
- The MHT roots must be at this center location
- If a tree has an odd-length diameter, it has 1 center, if a tree has an even-length diameter, it has 2 centers.