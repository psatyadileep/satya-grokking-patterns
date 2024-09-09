"""
Given an integer x, find the square root of x. If x is not a perfect square, then return floor(√x).
Input:
x = 5
Output: 2
Explanation: Since, 5 is not a perfect
square, floor of square_root of 5 is 2.
"""

class Solution:
    def floorSqrt(self, x):

        ans = -1

        for i in range(1, x+1):


            val = i*i

            if val<=x:
                ans = i
            else:
                break

        # print(ans)
        return i


print(Solution().floorSqrt(25))





class Solution:
    def floorSqrt(self, x):
        def isCondition(mid):
            return mid*mid>x

        L = 1
        R = x
        while L<R:
            mid = (L+R)//2


            if isCondition(mid):
                R = mid

            else:
                L = mid+1

        return L-1

print(Solution().floorSqrt(5))
print(Solution().floorSqrt(4))