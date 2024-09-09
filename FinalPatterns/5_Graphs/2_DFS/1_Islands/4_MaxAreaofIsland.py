"""
https://leetcode.com/problems/max-area-of-island/description/

You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.


"""
import sys
from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:


        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        visited = set()

        self.max_area = 0



        def isMove(r,c):
            return 0 <= r < rows and 0 <= c < cols and (r, c) not in visited and grid[r][c]==1

        def dfs(r,c):

            if not isMove(r,c):
                return 0

            area =1
            visited.add((r,c))


            directions = [(1,0),(0,1),(-1,0),(0,-1)]

            for dr, dc in directions:
                new_row , new_col = r+dr , c+dc
                area += dfs(new_row,new_col)

            return area



        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1 and (r,c) not in visited:
                    current_area = dfs(r,c)
                    self.max_area = max(self.max_area,current_area)


        return self.max_area


grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]]


print(Solution().maxAreaOfIsland(grid))