from utils import *

def findOrder(numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    res = []
    adjacentList = {}        # hướng đi ra. Ex: 2: [4,5] -> course 2 có 2 dependency
    in_degree = {}          # hướng đi vào. Ex: 5: 2 -> course 5 có 2 prequisites
    queue = deque([])
    # Step 1. Build adjacenList (outbout) and in_degree (inbout)
    for i in range(numCourses):
        adjacentList[i] = []
        in_degree[i] = 0
    for degree, pre in prerequisites:
        adjacentList[pre].append(degree)
        in_degree[degree] += 1
    print(f"adjList: {adjacentList}")
    print(f"in_degree: {in_degree}")
    for key, val in in_degree.items():
        if val == 0:
            res.append(key)
            queue.append(key)
    while queue:
        curr = queue.popleft()              # course can complete
        for dependency in adjacentList[curr]:
            in_degree[dependency] -= 1
            if in_degree[dependency] == 0:
                queue.append(dependency)
                res.append(dependency)
    if len(res) == numCourses:
        return res
    else: return []
            
            
print(findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))
    
    
    