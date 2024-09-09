from typing import List


class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, new_color: int) -> List[List[int]]:
        rows, cols = len(grid), len(grid[0])
        original_color = grid[row][col]
        visited = set()
        border = set()

        def isMove(r, c):
            return 0 <= r < rows and 0 <= c < cols and (r, c) not in visited and grid[r][c] == original_color

        def dfs(r, c):
            visited.add((r, c))
            is_border = False
            directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

            for dr, dc in directions:
                new_row, new_col = r + dr, c + dc

                if not (0 <= new_row < rows and 0 <= new_col < cols) or grid[new_row][new_col] != original_color:
                    is_border = True
                elif isMove(new_row, new_col):
                    dfs(new_row, new_col)

            # If it's an edge cell or it was determined to be a border, add it to the border set
            if is_border or r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
                border.add((r, c))

        # Start DFS from the initial cell
        dfs(row, col)

        # Color the border cells with the new color
        for r, c in border:
            grid[r][c] = new_color

        return grid