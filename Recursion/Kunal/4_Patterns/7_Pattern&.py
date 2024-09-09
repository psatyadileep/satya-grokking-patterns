"""
        1
      2 1 2
    3 2 1 2 3
  4 3 2 1 2 3 4
5 4 3 2 1 2 3 4 5
"""



def PrintPattern7():
    def helper(n):

        for row in range(1,n+1):
            space = n-row

            for i in range(space):
                print(" ", end="")
            for column in range(row,0,-1):
                print(column,end="")

            for column in range(2,row+1):
                print(column, end="")
            print()
                # after every roow pirn a new line

    helper(5)

PrintPattern7()