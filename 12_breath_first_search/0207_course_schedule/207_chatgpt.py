from utils import *

def canFinish(numCourses: int, prerequisites: List[List[int]]):
    # Step 1: Build adjacency list and compute in-degrees
    graph = {i: [] for i in range(numCourses)}
    in_degree = {i: 0 for i in range(numCourses)}
    count = 0
    for course, pre in prerequisites:
        graph[pre].append(course)
        in_degree[course] += 1

    print(f"graph: {graph}")
    print(f"in_degree: {in_degree}")
    
    # Step 2: Initialize queue with courses having 0 in-degree
    queue = deque([])
    for course in in_degree:
        if in_degree[course] == 0:
            queue.append(course)
    print(queue)
    
    # Step 3: Process courses using BFS
    while queue:
        course = queue.popleft()
        count += 1
        for neighbor in graph[course]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
                
    return count == numCourses
    
print(canFinish(6, [[0,1],[1,3],[2,1],[4,2],[5,2],[5,4]]))


