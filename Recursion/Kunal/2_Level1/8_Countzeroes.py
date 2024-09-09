"""
Given a number count the number of zeroes
"""


def Countzeroes(n):

    def helper(n,count):
        if not n or n<0:
            return count

        if n%10 == 0:
            return helper(n//10,count+1)
        else:
            return helper(n//10, count)

    return helper(n, 0)

print(Countzeroes(1200045))