class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:

        enclaves = 0
        rows = len(grid)
        cols = len(grid[0])

        visited = set()

        def isMove(r, c):
            return 0 <= r < rows and 0 <= c < cols and grid[r][c] == 1 and (r, c) not in visited

        def dfs(r, c):
            # Marks the cell as visited and changes it temporarily to 'V'
            visited.add((r, c))
            grid[r][c] = 0

            # Possible movements: down, right, left, up
            directions = [(1, 0), (0, 1), (0, -1), (-1, 0)]

            for dr, dc in directions:
                new_row = r + dr
                new_col = c + dc

                if isMove(new_row, new_col):
                    dfs(new_row, new_col)

        for i in range(rows):
            if grid[i][0] == 1 and isMove(i, 0):
                dfs(i, 0)
            if grid[i][cols - 1] == 1 and isMove(i, cols - 1):
                dfs(i, cols - 1)

        for j in range(cols):
            if grid[0][j] == 1 and isMove(0, j):
                dfs(0, j)
            if grid[rows - 1][j] == 1 and isMove(rows - 1, j):
                dfs(rows - 1, j)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    enclaves += 1

        return enclaves
