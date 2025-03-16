# Medium
## 207. Course Schedule
There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i]` = `[ai, bi]` indicates that you must take course `bi` first if you want to take course `ai`.

For example, the pair `[0, 1]`, indicates that to take course `0` you have to first take course `1`.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.



Example 1\
Input: numCourses = 2, prerequisites = [[1,0]]\
Output: true\
Explanation: There are a total of 2 courses to take.\
To take course 1 you should have finished course 0. So it is possible\

# Key Idea
```
Ex: 
numCourses = 6
prerequisites = [[0,1],[1,3],[2,1],[4,2],[5,2],[5,4]]

0 depends on 1
1 depends on 3 # mean 3 -> 1 is one directed edge in graph
2 depends on 1
4 depends on 2
...
```

## Approach 1 - BFS
### Step 1: Build graph and compute in-degree
```
"In-degree" trong lý thuyết đồ thị có nghĩa là "bậc vào" hoặc "số bậc vào".
Nó biểu thị số lượng cạnh đi vào một đỉnh trong đồ thị có hướng.
Ví dụ: Nếu có ba cạnh đi vào một đỉnh A, thì in-degree của A là 3.
```
AdjacencyList: (hướng đi ra)
```python
graph = {
    0: [],
    1: [0, 2], # mean course 1 has 2 dependencies [0, 2]
    2: [4, 5], # 2 -> 4; 2 -> 5
    3: [1],     
    4: [5],
    5: []
}
```

In-Degre (hướng đi vào)
```python
in_degree = {
    0: 1, # Needs 1 prerequisites (from 1)
    1: 1,
    2: 1,
    3: 0, # No prerequisites
    4: 1,
    5: 2
}
```
### Step 2: Initialize BFS Queue
Courses with in-degree = 0 (no prerequisites) are added to the queue\
Initial queue: `deque([3])`

### Step 3: Process Course (BFS Traversal)
We process the queue, reducing in-degrees and adding course with `0` in-degree
**Iteration 1: Process Coures 3**
- Remove `3` from the queue
- Update dependencies of `3` with `indegree -= 1` -> in-degree[1] -= 1 =0 -> add `1` to `queue`
- Queue now: `deque([1])`

