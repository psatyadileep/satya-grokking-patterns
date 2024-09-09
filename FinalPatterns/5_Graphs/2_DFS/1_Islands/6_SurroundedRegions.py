"""
https://leetcode.com/problems/surrounded-regions/description/
LC130

130. Surrounded Regions
Solved
Medium
Topics
Companies
You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:

Connect: A cell is connected to adjacent cells horizontally or vertically.
Region: To form a region connect every 'O' cell.
Surround: The region is surrounded with 'X' cells if you can connect the region with 'X' cells and none of the region cells are on the edge of the board.
A surrounded region is captured by replacing all 'O's with 'X's in the input matrix board.



Example 1:

Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]

Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

Explanation:


In the above diagram, the bottom region is not captured because it is on the edge of the board and cannot be surrounded.

Example 2:

"""

from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return

        rows, cols = len(board), len(board[0])

        def isMove(r, c):
            return 0 <= r < rows and 0 <= c < cols and board[r][c] == "O"

        def dfs(r, c):
            if not isMove(r, c):
                return
            board[r][c] = "E"  # Mark as 'E' (escaped) to avoid flipping

            # Explore all four directions (down, up, right, left)
            direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            for dr, dc in direction:
                new_row, new_col = r + dr, c + dc
                dfs(new_row, new_col)

        # Start from the first and last row
        for i in range(rows):
            if board[i][0] == "O":
                dfs(i, 0)
            if board[i][cols - 1] == "O":
                dfs(i, cols - 1)

        # Start from the first and last column
        for j in range(cols):
            if board[0][j] == "O":
                dfs(0, j)
            if board[rows - 1][j] == "O":
                dfs(rows - 1, j)

        # Flip the remaining 'O's to 'X' and 'E' back to 'O'
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "E":
                    board[i][j] = "O"
