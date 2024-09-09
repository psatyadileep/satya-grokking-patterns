"""
Find the factorial of a number using recurison
"""



def factorial(n):

    def helper(n):

        if n<=1:
            return 1


        return n * helper(n-1)


    return  helper(n)

print(factorial(5))

