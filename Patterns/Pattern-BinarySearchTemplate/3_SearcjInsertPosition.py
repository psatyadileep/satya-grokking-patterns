"""
https://leetcode.com/problems/search-insert-position/
35. Search Insert Position
Solved
Easy
Topics
Companies
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.



Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
"""


class Solution:
    def searchInsert(self, nums, target):
        L = 0
        R = len(nums)

        def isCondition(index):
            return nums[index] >= target

        while L < R:
            mid = L + (R - L) // 2
            if isCondition(mid):
                R = mid
            else:
                L = mid + 1

        return L
#
#
# Very classic application of binary search.
# We are looking for the minimal k value satisfying nums[k] >= target, and we can just copy-paste our template. Notice that our solution is correct regardless of whether the input array nums has duplicates.
# Also notice that the input target might be larger than all elements in nums and therefore needs to placed at the end of the array.
# That's why we should initialize right = len(nums) instead of right = len(nums) - 1.
#
#
