"""
https://leetcode.com/problems/binary-search/
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.



Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
"""
from typing import List


class Solution:
    def FindFloor(self, nums: List[int], target: int) -> int:

        L = 0
        R = len(nums) - 1

        def condition(mid):
            return nums[mid] >= target

        while L < R:

            mid = (L + R) // 2

            if condition(mid):
                R = mid
            else:

                L = mid + 1



        return L -1 if L-1>0 else -1



ans = (Solution().FindFloor([2,3,6,8,10,12,15,18],12))
print()

