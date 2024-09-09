"""
Print all the numbers from N to 1
"""


def printMain(n):


    def helper(n,res):
        if n<1:
            return res
        res.append(n)

        return helper(n-1,res)

    return helper(n,[])

print(printMain(5))