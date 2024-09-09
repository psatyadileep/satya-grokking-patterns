"""
https://leetcode.com/problems/koko-eating-bananas/description/
"""

import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L, R = 1, max(piles)

        def isCondition(mid):

            time = 0
            for pile in piles:

                if pile<mid:
                    time+=1

                else:
                    current_time = math.ceil(pile/mid)
                    time+=current_time

            return time<=h

        while L<R:

            mid = (L+R)//2


            if isCondition(mid):
                R=mid

            else:
                L = mid+1


        return L


print(Solution().minEatingSpeed([3,6,7,11], h = 8))
print(Solution().minEatingSpeed([30,11,23,4,20], h = 5))
print(Solution().minEatingSpeed([30,11,23,4,20], h = 6))