""""
    *
   * *
  * * *
 * * * *
* * * * *
 * * * *
  * * *
   * *
    *
"""



def PrintPattern6():
    def helper(n):

        for row in range(2*n-1):

            if row<=n-1:
                columns= row+1
            else:
                columns = 2*n -1-row

            space = n-columns

            for i in range(space):
                print(" ", end="")
            for i in range(columns):
                print("* ",end="")
            print()
                # after every roow pirn a new line

    helper(5)

PrintPattern6()