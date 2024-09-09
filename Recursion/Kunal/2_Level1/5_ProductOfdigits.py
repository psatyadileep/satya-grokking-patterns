"""
Givevn a number find the sym of the sigits
"""


def ProductofDigits(n):


    def helper(n):

        if not n or n ==0  :
            return 1

        return n%10 * helper(n//10)

    return helper(n)


print(ProductofDigits(1342))