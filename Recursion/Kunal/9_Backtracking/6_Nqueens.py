class Solution:

    def Nqueens(self,n):

        def helper(board,row):

            count = 0
            if row == len(board):
                return 1

            # palcing the queen and checkfor row and column
            for col in range(len(board)):
                #palce queen if its safe

                if isSafe(board,row,col):
                    board[row][col] = True
                    count+= helper(board,row+1)

            board[row][col] = False

        def isSafe(baord,rows,cols):

            # check Vertical row

            for row in range(rows):
                if baord[row][cols]:
                    return False


            #checj diagonal left
            maxleft = min(rows,cols)
            for i in range(1,maxleft):
                if baord[rows-1][cols-1]:
                    return False

            # check right diagonal
            maxright = min(row,len(baord)-cols-1)
            for i in range(maxright):
                if baord[rows-i][cols+i]:
                    return False


            return True
        baord = [[n]]*n
        helper(baord,0)
