"""
https://leetcode.com/problems/unique-paths-ii/
63. Unique Paths II
Attempted
Medium
Topics
Companies
Hint
You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.

Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The testcases are generated so that the answer will be less than or equal to 2 * 109.
Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right


"""

from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])


        self.count = 0

        def isSafe(r,c):
            return 0<=r<rows and 0<=c<cols and obstacleGrid[r][c]==0

        def dfs(r,c):


            if r==rows-1 and c ==cols-1:
                return 1


            directions = [(1,0),(0,1)]


            for dr , dc in directions:
                new_row , new_col = r+dr , c+dc


                if isSafe(dr,dc):
                    self.count+= dfs(dr,dc)


        dfs(0,0)
        return self.count


