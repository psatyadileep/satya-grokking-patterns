""""
https://leetcode.com/problems/n-queens/description/
51. N-Queens
Attempted
Hard
Topics
Companies
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.
Approach:
-> Placed the quuens row by row
-> check if its sface to space
-> palce the quuens
"""
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:


        #create the baord:
        board = [["."]*n for _ in range(n)]



        result = []

        def queens(board,row):

            if row>=len(board):
                result.append(["".join(row) for row in board])
                return


            for col in range(len(board)):
                if is_safe(board,row,col):
                    board[row][col]="Q"
                    queens(board,row+1)
                    board[row][col]="."



        def is_safe(board,row,col):

            #Check Vertically:

            for i in range(row):
                if board[i][col]=="Q":
                    return False


            # Check Left DIagonal decreasing and column decaresing at the same time

            i = row-1
            j = col-1

            while i>=0 and j>=0:
                if board[i][j]=="Q":
                    return False
                i-=1
                j-=1


            # CHeck RIght Diagonal : Roww decreases and column increase

            i = row-1
            j = col+1
            while i>=0 and j<len(board):
                if board[i][j]=="Q":
                    return False
                i-=1
                j+=1

            return True

        queens(board,0)
        return result


print(Solution().solveNQueens(4))





