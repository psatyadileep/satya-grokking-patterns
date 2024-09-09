def PrintMessage():


    def helper(n):

        if n==6:
            return

        print(n)
        helper(n+1)

    helper(1)

PrintMessage() 