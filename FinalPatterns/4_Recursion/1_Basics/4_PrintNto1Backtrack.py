def PrintNto1(n):

    def helper(i):
        if i<1:
            return

        print(i)
        helper(i-1)

    helper(n)



PrintNto1(5)