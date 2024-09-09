"""
https://leetcode.com/problems/number-of-distinct-islands/
LC694
694. Number of Distinct Islands
Solved
Medium
Topics
Companies
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

An island is considered to be the same as another if and only if one island can be translated (and not rotated or reflected) to equal the other.

Return the number of distinct islands.
"""



from typing import List

class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        lookup = set()

        def isMove(r, c):
            # Check if the move is within bounds, not visited, and is land
            return 0 <= r < rows and 0 <= c < cols and grid[r][c] == 1 and (r, c) not in visited

        def dfs(r, c, path, base_r, base_c):
            # Add the current position to visited and record the relative path
            visited.add((r, c))
            path.append((r - base_r, c - base_c))  # Store relative positions

            # Define the 4 possible directions (up, right, down, left)
            directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

            for dr, dc in directions:
                new_row = r + dr
                new_col = c + dc
                if isMove(new_row, new_col):
                    dfs(new_row, new_col, path, base_r, base_c)
            return path

        for i in range(rows):
            for j in range(cols):
                # If the cell is land and hasn't been visited, perform DFS
                if grid[i][j] == 1 and (i, j) not in visited:
                    path = dfs(i, j, [], i, j)  # Start DFS with relative position tracking
                    normalized_path = tuple(path)  # Convert to tuple for hashability

                    # Add the normalized path to lookup
                    lookup.add(normalized_path)

        # Return the number of unique island shapes
        return len(lookup)