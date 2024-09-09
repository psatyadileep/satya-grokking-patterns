"""
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
lc: 34
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.



Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
"""

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        if not nums or len(nums) < 1:
            return [-1, -1]

        def istarget(index, flag):
            if flag:
                return nums[index] >= target
            else:
                return nums[index] > target

        # Finding the left boundary
        l1 = 0
        r1 = len(nums) - 1
        while l1 < r1:
            mid = (l1 + r1) // 2
            if istarget(mid, True):
                r1 = mid
            else:
                l1 = mid + 1

        # Finding the right boundary
        l2 = 0
        r2 = len(nums)
        while l2 < r2:
            mid = (l2 + r2) // 2  # Bias the mid to the right
            if istarget(mid, False):
                r2 = mid
            else:
                l2 = mid+1

        # Check if the target exists in the array
        if nums[l1] != target:
            return [-1, -1]

        # Final result as per original logic
        elif l1 == l2:
            return [l1, l2]

        else:
            return [l1, l2-1]



