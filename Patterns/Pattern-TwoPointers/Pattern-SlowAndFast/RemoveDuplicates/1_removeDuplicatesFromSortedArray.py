
"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array/
LC26 :  Remove Duplicates from Sorted Array
"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        L = 0

        if not nums:
            return 0

        for R in range(1, len(nums)):
            if nums[L] != nums[R]:
                nums[L + 1] = nums[R]
                L += 1

        return L + 1


class Solution2:
    def removeDuplicates(self, nums: List[int]) -> int:
        L = 1

        for R in range(1, len(nums)):
            if nums[R] != nums[R - 1]:
                nums[L] = nums[R]
                L += 1
            print(L, R)

        return L


print(Solution2().removeDuplicates([0,1,1,2,3,3]))