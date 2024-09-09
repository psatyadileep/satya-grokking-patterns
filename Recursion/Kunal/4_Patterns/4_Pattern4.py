def PrintPattern4():
    def helper(n):

        for row in range(1,n+1):
            # for every row run teh col,
            for col in range(1,row+1):
                print(col, end="")
            # after every roow pirn a new line
            print()

    helper(5)


PrintPattern4()
