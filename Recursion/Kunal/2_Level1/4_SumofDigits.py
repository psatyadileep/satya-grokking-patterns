"""
Givevn a number find the sym of the sigits
"""


def SumofDigits(n):


    def helper(n):

        if not n :
            return 0

        return n%10 + helper(n//10)

    return helper(n)


print(SumofDigits(1342))