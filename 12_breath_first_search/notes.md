![alt text](validpath-ex2.png "test")

```
n = 6
edges = [[0,1], [0,2], [3,5], [3,4], [4,5]]
```
### Steps 1: Initialize graph
```
graph = {}
for i in range(n):
    graph[i] = []

or 
graph = {i: [] for i in range(n)}

# output
graph = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
```

### Steps 2: Add edges from edges:
```
for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)
```

#### After addings edges
```
graph = {
    0: [1, 2],
    1: [0],
    2: [0],
    3: [4, 5],
    4: [3, 5],
    5: [3, 4]
}
```

### Step 3 - DFS example
**Checking if there is a path from `source = 0` to `destination = 3` using DFS**
```python
visisted = set()
def dfs(node):
    if node == destination:
        return True
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited and dfs(neighbor):
            return True
    return False
```
**Explain**
1. Start at `0` -> Mark `0` as visited
    - Neighbors: [1, 2]
2. Visit `1` -> Mark `1` as visited
    - dfs(1) -> return False -> continue
3. Visit `2` -> Mark `2` as visited
    - dfs(2) -> return False 

### Step 3 - BFS example
```python
queue = deque([source])
visited = set([source])

while queue:
    node = queue.popleft()
    if node == destination:
        return True
    for neighbor in graph[node]:
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append(neighbor)
```