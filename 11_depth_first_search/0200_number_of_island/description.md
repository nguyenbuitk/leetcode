# Medium
## 200. Number of Islands
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:
```
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
```
# Key Idea
** Similar to problem 130 surrounded regions **
## Approach 1 - DFS
1. Start DFS from `"1"` cell and mark them as `"X"`
2. End of DFS count += 1 and return count
```python
  def dfs(i, j):
      if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] != "1":
          return
      grid[i][j] = "#"
      for di, dj in [(0,1), (0, -1), (1,0), (-1,0)]:
          dfs(i + di, j + dj)
```


## Approach 2 - BFS
1. Instead of calling recursive DFS, we can use `queue` to store the islands.
```python
  rows, cols = len(grid), len(grid[0])
  res = 0
  directions = [(-1,0), (1,0), (0, -1), (0,1)]
  def bfs(i, j):
      queue = deque([(i, j)])
      grid[i][j] = "#"
      while queue:
          p, q = queue.popleft()
          
          for di, dj in directions:
              ni, nj = p+di, q+dj
              if 0 <= ni < rows and 0 <= nj < cols and grid[ni][nj] == "1":
                  grid[ni][nj] = '#'   
                  queue.append((ni,nj))

  for i in range(rows):
      for j in range(cols):

          if grid[i][j] == "1":
              bfs(i,j)
              res += 1
  return res
```