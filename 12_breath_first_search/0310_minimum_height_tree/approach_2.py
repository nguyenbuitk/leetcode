from utils import *

print(buid_adjlist(4, [[1,0],[1,2],[1,3]]))

def findMinHeighTrees(n: int, edges: List[List[int]]) -> List[int]:
    if n == 1:
        return [0]
    
    # Step 1: build adjcent list and degree count
    adjList, inDegree = {}, {}
    res = []
    for i in range(n):
        adjList[i] = []
        inDegree[i] = 0
    for u, v in edges:
        adjList[u].append(v)
        adjList[v].append(u)
        inDegree[u] += 1
        inDegree[v] += 1

    # Step 2: initialize left node
    print(f"adjList: {adjList}")
    print(f"indegree: {inDegree}")
    queue = deque([])
    for key, val in inDegree.items():
        if val == 1:
            queue.append(key)
    print(f"queue: {queue}")            

    print(f"leaf node: {queue}")
    
    # Step 3: BFS to trim the tree from leaves to the center
    while n > 2:
        level_size = len(queue)
        n -= level_size
        for i in range(level_size):
            curr = queue.popleft()
            print(f"\ncurr: {curr}")
            for next in adjList[curr]:
                inDegree[next] -= 1
                if inDegree[next]  == 1:
                    queue.append(next) 
                print(f"inDegree[{next}] = {inDegree[next]}")
    
    return list(queue)
print(findMinHeighTrees(6, [[3,0],[3,1],[3,2],[3,4],[5,4]] ))
# findMinHeighTrees(3, [[0,1], [0,2]])
