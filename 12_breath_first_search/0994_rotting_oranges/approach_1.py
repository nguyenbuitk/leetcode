from utils import *

def orangesRotting(grid: List[List[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    directions = [(0,1), (0,-1), (1,0), (-1,0)]
    total_orange_not_rooted = 0
    total_change = 0
    res = -1
    queue = deque([])
    
    # Get all rooted oranges
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 2:
                queue.append((i,j))
            elif grid[i][j] == 1:
                total_orange_not_rooted += 1
    
    # Process the rooted oranges with BFS
    print(queue)
    while queue:
        level_size = len(queue)
        res += 1
        print(f"\nafter {res} minutes")
        for i in range(level_size):
            x, y = queue.popleft()
            for di, dj in directions:
                ni, nj = di + x, dj + y
                if 0 <= ni < rows and 0 <= nj < cols and grid[ni][nj] == 1:
                    queue.append((ni,nj))
                    grid[ni][nj] = 2
                    print(f"\nx: {x}, y: {y}")
                    print(f"ni: {ni}, nj: {nj}")
                    total_change += 1
    print(f"minute: {res}")
    print(f"total_not_rooted: {total_orange_not_rooted}")
    print(f"total change: {total_change}")
    if total_change == total_orange_not_rooted:
        return res
    return -1
    
#print(orangesRotting([[2,1,1],[0,1,1],[1,0,1]]))
print(orangesRotting([[0]]))
print_matrix([[2,1,1],[0,1,1],[1,0,1]])