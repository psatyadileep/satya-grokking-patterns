class Solution:
    def Nqueens(self, n):
        res = []

        board = [["."]*n for i in range(n)]
        def helpercount(board,r, result):
            if r>=len(board):
                result.append("".join(row) for row in board)

            for c in range(len(board)):
                if isSafe(r,c):

                    board[r][c] = "Q"
                    helpercount(baord,r+1, result)
                    board[r][c] = "."




            def isSafe(r,c):

                #Check vertical:
                for r in range(len(board)):
                    if board[c][r]=="q":
                        return False

                #check left horizontal:

                for r in range(r,-1,-1):
                    for c in range(c,-1,-1):
                        if board[r][c] == "q":
                            return False

                # check right Horizontal




