"""
https://leetcode.com/problems/word-search/
9. Word Search
Medium
Topics
Companies
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.
"""


from typing import List


class Solution:
    def solveNKnights(self, n: int) -> List[List[str]]:

        board = [["."]*n for _ in range(n)]
        result = []

        def knights(row,board):
            if row >= n:
                result.append(["".join(row) for row in board])
                return

            for col in range(n):
                if is_safe(board,row, col):
                    board[row][col] = "N"
                    knights(row + 1,board)
                    board[row][col] = "."

        def is_safe(board,row, col):
            moves = [
                (-2, -1), (-2, 1), (2, -1), (2, 1),
                (-1, -2), (-1, 2), (1, -2), (1, 2)
            ]

            for move in moves:
                new_row, new_col = row + move[0], col + move[1]
                if 0 <= new_row < n and 0 <= new_col < n:
                    if board[new_row][new_col] == "N":
                        return False

            return True

        knights(0,board)
        return result

print(Solution().solveNKnights(4))
