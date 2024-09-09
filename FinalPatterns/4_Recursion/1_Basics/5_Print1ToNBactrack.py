
def Print1toN(n):

    def helper(i):
        if i<1:
            return
        helper(i - 1)
        print(i)


    helper(n)



Print1toN(5)