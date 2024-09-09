from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        def convert_board(board):
            converted_board = []
            for row in board:
                converted_row = ''.join('Q' if col else '.' for col in row)
                converted_board.append(converted_row)
            return converted_board

        def queens(board, row, result):
            if row == len(board):
                result.append(convert_board(board))
                return

            # Placing the queen and checking for every row and col
            for col in range(len(board)):
                # Place the queen if it is safe
                if is_safe(board, row, col):
                    board[row][col] = True
                    queens(board, row + 1, result)
                    board[row][col] = False



        def is_safe(board, row, col):
            # Check vertical row
            for i in range(row):
                if board[i][col]:
                    return False

            # Diagonal left
            max_left = min(row, col)
            for i in range(1, max_left + 1):
                if board[row - i][col - i]:
                    return False

            # Diagonal right
            max_right = min(row, len(board) - col - 1)
            for i in range(1, max_right + 1):
                if board[row - i][col + i]:
                    return False

            return True

        board = [[False for _ in range(n)] for _ in range(n)]
        result = []
        queens(board, 0, result)
        return result  # Return the result containing valid configurations
