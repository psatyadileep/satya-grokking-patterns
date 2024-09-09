"""
https://leetcode.com/problems/sudoku-solver/description/
"""
from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        empty = find_empty(baord)
        if not empty:
            return True




        def is_safe(board,row,col,num):

            # check the row

            for i in range(0,len(board)):
                #check the number is present

                if board[row][col]==num:
                    return False


            # check col

            for i in range(0,len(board)):
                #check the number is present

                if board[row][col]==num:
                    return False


