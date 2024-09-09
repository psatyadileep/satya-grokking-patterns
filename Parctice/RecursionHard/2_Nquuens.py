from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        def queens(board, row, result):
            if row == len(board):
                result.append(["".join(row) for row in board])
                return

            # Placing the queen and checking for every row and col
            for col in range(len(board)):
                # Place the queen if it is safe
                if is_safe(board, row, col):
                    board[row][col] = "Q"
                    queens(board, row + 1, result)
                    board[row][col] = "."

        def is_safe(board, row, col):
            # Check vertical row
            for i in range(row):
                if board[i][col] == "Q":
                    return False

            # Diagonal left
            for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
                if board[i][j] == "Q":
                    return False

            # Diagonal right
            for i, j in zip(range(row - 1, -1, -1), range(col + 1, len(board))):
                if board[i][j] == "Q":
                    return False

            return True

        board = [["."] * n for _ in range(n)]
        result = []
        queens(board, 0, result)
        return result  # Return the result containing valid configurations


print(Solution().solveNQueens(4))
