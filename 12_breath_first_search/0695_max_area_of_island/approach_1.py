from utils import *

def maxAreaOfIsland(grid: List[List[int]]) -> int:
    print_matrix(grid)
    max_are = 0
    rows, cols = len(grid), len(grid[0])
    
    def bfs(x, y) -> int:
        print(f"\nx: {x}, y: {y}")
        res = 0
        grid[x][y] = -1
        queue = deque([(x,y)])
        directions = [(0, 1), (0, -1), (1,0), (-1,0)]
        while queue:
            print(f"queue: {queue}")
            level_size = len(queue)
            for _ in range(level_size):
                i, j = queue.popleft()
                res += 1
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < rows and 0 <= nj < cols and grid[ni][nj] == 1:
                        grid[ni][nj] = -1
                        queue.append((ni, nj))
                        
        print(f"res = {res}")
        print_matrix(grid)
        return res
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                max_are = max(max_are, bfs(i, j))
    return max_are
    
#print(maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]))
print(maxAreaOfIsland([[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]))
            