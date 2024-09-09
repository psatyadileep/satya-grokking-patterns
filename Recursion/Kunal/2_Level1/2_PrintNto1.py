"""
Give a number N , print from N to 1 using recursion
"""



def printMain(n):

    if n<1:
        return

    printMain(n-1)
    print(n)

# printMain(5)



def printMain2(n):


    def helper(n,res):
        if n<1:
            return res

        return helper(n-1,res)

        res.append(n)

    return helper(n,[])

print(printMain2(5))