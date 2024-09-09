"""
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


def PrintPattern5():
    def helper(n):

        for row in range(2*n-1):

            if row<=n-1:
            # for every row run teh col,
                for col in range(row + 1):
                    print("*", end="")
            else:
                for col in range(2*n -1-row):
                    print("*", end="")
                # after every roow pirn a new line
            print()

    helper(5)


PrintPattern5()
