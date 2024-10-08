"""
https://leetcode.com/problems/word-search/description/

79. Word Search
Solved
Medium
Topics
Companies
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.
"""
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def right_move(row, col, ind):
            # Check if the position is valid and matches the current character in the word
            return (0 <= row < len(board) and
                    0 <= col < len(board[0]) and
                    board[row][col] == word[ind])

        def backtrack(row, col, ind):
            # If we have matched all characters in the word
            if ind >= len(word):
                return True

            # If the current move is invalid
            if not right_move(row, col, ind):
                return False

            # Temporarily mark the cell as visited
            temp = board[row][col]
            board[row][col] = None

            # Directions for moving right, down, left, and up
            directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

            # Explore all directions
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if backtrack(new_row, new_col, ind + 1):
                    return True

            # Restore the original character in the board
            board[row][col] = temp
            return False

        # Start backtracking from each cell in the board
        for r in range(len(board)):
            for c in range(len(board[0])):
                if backtrack(r, c, 0):
                    return True

        return False



