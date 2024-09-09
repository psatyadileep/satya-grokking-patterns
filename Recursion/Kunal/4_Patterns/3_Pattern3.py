"""
* * * * *
* * * *
* * *
* *
*
"""



def PrintPattern3():
    def helper(n):
        for row in range(n):
            # for col in range(n,row,-1):
            for col in range(n-row):     
                print("*", end="")
            # after every roow pirn a new line
            print()

    helper(5)


PrintPattern3()
