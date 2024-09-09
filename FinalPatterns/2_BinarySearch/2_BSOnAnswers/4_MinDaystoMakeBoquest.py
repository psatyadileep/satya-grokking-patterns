"""
1482. Minimum Number of Days to Make m Bouquets
Solved
Medium
Topics
Companies
Hint
You are given an integer array bloomDay, an integer m and an integer k.

You want to make m bouquets. To make a bouquet, you need to use k adjacent flowers from the garden.

The garden consists of n flowers, the ith flower will bloom in the bloomDay[i] and then can be used in exactly one bouquet.

Return the minimum number of days you need to wait to be able to make m bouquets from the garden. If it is impossible to make m bouquets return -1.



Example 1:

Input: bloomDay = [1,10,3,10,2], m = 3, k = 1
Output: 3
Explanation: Let us see what happened in the first three days. x means flower bloomed and _ means flower did not bloom in the garden.
We need 3 bouquets each should contain 1 flower.
After day 1: [x, _, _, _, _]   // we can only make one bouquet.
After day 2: [x, _, _, _, x]   // we can only make two bouquets.
After day 3: [x, _, x, _, x]   // we can make 3 bouquets. The answer is 3.
Example 2:
"""
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        L = 0
        R = max(bloomDay)


        def isCondition(mid):

            bouqets = 0
            flowers = 0
            for day in bloomDay:

                if day<=mid:
                    flowers+=1

                    if flowers == k:
                        bouqets+=1
                        flowers = 0
                else:
                    flowers = 0 ,,
            return bouqets>=m

        while L<R:

            mid = (L+R)//2

            if isCondition(mid):
                R= mid

            else:
                L = mid+1



        return L if isCondition(L) else -1
