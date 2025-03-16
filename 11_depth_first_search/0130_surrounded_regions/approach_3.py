from collections import deque
from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return

        rows, cols = len(board), len(board[0])
        queue = deque()

        # Step 1: Find all border 'O's and mark them as 'T' (Temporary safe)
        for r in range(rows):
            for c in range(cols):
                if (r in [0, rows - 1] or c in [0, cols - 1]) and board[r][c] == 'O':
                    queue.append((r, c))
                    board[r][c] = 'T'  # Mark safe region

        # Step 2: BFS to mark all 'O's connected to borders as 'T'
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # Down, Up, Right, Left

        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == 'O':
                    queue.append((nr, nc))
                    board[nr][nc] = 'T'  # Mark as safe
        
        # Step 3: Convert all remaining 'O' to 'X' (Surrounded regions)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'  # Captured region
                elif board[r][c] == 'T':
                    board[r][c] = 'O'  # Restore non-surrounded region

