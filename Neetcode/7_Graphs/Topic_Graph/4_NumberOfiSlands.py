class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        visited = set()

        q = collections.deque()

        island = 0

        def bfs(r, c):
            q = collections.deque()
            visited.add((r, c))
            q.append((r, c))

            while q:

                directions = [(1, 0), (-1, 0), (0, 1), (0, -1), ]
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc

                    if (row < 0 or col < 0 or row == rows or col == cols or (row, col) in visited or grid[row][
                        col] == "0"):
                        continue

                    visited.add((row, col))
                    q.append((row, col))

        for r in range(rows):
            for c in range(cols):

                if (r, c) not in visited and grid[r][c] == "1":
                    bfs(r, c)
                    island += 1

        return island





