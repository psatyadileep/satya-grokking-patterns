"""
* * * *
* * * *
* * * *
* * * *

1 . No of rows n
2.  nof col per row = n
3. what to print *
"""


def PrintPattern2():
    def helper(n):

        for row in range(n):
            # for every row run teh col,
            for col in range(n):
                print("*", end="")
            # after every roow pirn a new line
            print()

    helper(5)


PrintPattern2()
