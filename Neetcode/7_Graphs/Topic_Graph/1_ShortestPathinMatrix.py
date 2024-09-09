import collections


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])

        q = collections.deque()
        visited = set()

        q.append((0, 0))
        visited.add((0, 0))

        if grid[0][0] == 1 or grid[-1][-1] == 1:  # Start or end blocked
            return -1
        length = 0

        while q:

            for i in range(len(q)):

                r, c = q.popleft()

                if r == rows - 1 and c == cols - 1:
                    return length + 1
                neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
                for dr, dc in neighbors:

                    if (min(r + dr, c + dc) < 0 or (r + dr == rows) or (c + dc == cols) \
                            or grid[r + dr][c + dc] == 1 or (r + dr, c + dc) in visited):
                        continue

                    q.append((r + dr, c + dc))
                    visited.add((r + dr, c + dc))
            length += 1
        return -1


import collections
from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        if grid[0][0] == 1 or grid[-1][-1] == 1:  # Start or end blocked
            return -1

        q = collections.deque([(0, 0)])
        visited = {(0, 0)}
        length = 0

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                if r == rows - 1 and c == cols - 1:
                    return length + 1  # Return length + 1 since we're counting cells

                # Define neighbor directions (including diagonals)
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0 and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        q.append((nr, nc))

            length += 1

        return -1

