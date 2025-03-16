from utils import *

def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    graph = {}
    indepent_course = set()
    queue = deque([])           # store the course completed
    for i in range(numCourses):
        graph[i] = []
    
    for course, pre in prerequisites:
        graph[course].append(pre)
    
    for key, value in graph.items():
        if not value:
            indepent_course.add(key)
            queue.append(key)
    print(f"graph: {graph}")
    print(f"independent course: {indepent_course}")        
    print(f"queue: {queue}")

    while queue:
        curr = queue.popleft()
        # curr = 5, remove all course depent to 5
        # example graph[2] = [4,5] -> graph[2] = 4
        for key, value in graph.items():
            if curr in value:
                graph[key].remove(curr)
                if not graph[key] and key not in indepent_course:
                    queue.append(key)
                    indepent_course.add(key)
        print(f"graph after remove {curr}: {graph}")
        time.sleep(0.2)
    return len(indepent_course) == numCourses
        
    
    
print(canFinish(6, [[0,1],[1,3],[2,1],[4,2],[5,2],[5,4]]))
    