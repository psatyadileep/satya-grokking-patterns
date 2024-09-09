"""
* * * * *
* * * *
* * *
* *
*
"""



def Pattern1(n):

    def helper(row , col):

        if row==0:
            return

        if col<row:
            print("*",end="")
            helper(row,col+1)
        else:
            print()
            helper(row-1,0)


    helper(n,0)


Pattern1(5)

