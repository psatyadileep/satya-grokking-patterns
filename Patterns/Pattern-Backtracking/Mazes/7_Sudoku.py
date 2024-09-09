import collections
from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        # Initialize the sets with the current state of the board
        for r in range(9):
            for c in range(9):
                if board[r][c] != '.':
                    num = int(board[r][c])
                    rows[r].add(num)
                    cols[c].add(num)
                    squares[(r // 3, c // 3)].add(num)

        def isSafe(r, c, num):
            return num not in rows[r] and num not in cols[c] and num not in squares[(r // 3, c // 3)]

        def helper():
            for r in range(9):
                for c in range(9):
                    if board[r][c] == '.':
                        for num in range(1, 10):
                            if isSafe(r, c, num):
                                board[r][c] = str(num)
                                rows[r].add(num)
                                cols[c].add(num)
                                squares[(r // 3, c // 3)].add(num)

                                if helper():
                                    return True

                                board[r][c] = '.'
                                rows[r].remove(num)
                                cols[c].remove(num)
                                squares[(r // 3, c // 3)].remove(num)

                        return False
            return True

        helper()


# Example usage
board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]

Solution().solveSudoku(board)
for row in board:
    print(row)
