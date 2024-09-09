"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
"""

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        lookup = {}
        L = 0
        R = 0

        while R < len(nums):
            lookup[nums[R]] = lookup.get(nums[R], 0) + 1

            if lookup[nums[R]] <= 2:
                nums[L] = nums[R]
                L += 1

            R += 1

            print(R,L)
        return L

    class Solution:
        def removeDuplicates(self, nums: List[int]) -> int:

            L = 0
            R = 0

            while R < len(nums):

                count = 1
                while R + 1 < len(nums) and nums[R] == nums[R + 1]:
                    R += 1
                    count += 1

                for i in range(min(2, count)):
                    nums[L] = nums[R]
                    L += 1

                R += 1
            return L


print(Solution().removeDuplicates([1,1,1,2,2,3]))