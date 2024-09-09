"""
LC259
https://leetcode.com/problems/3sum-smaller/description/
Given an array of n integers nums and an integer target, find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.



Example 1:

Input: nums = [-2,0,1,3], target = 2
Output: 2
Explanation: Because there are two triplets which sums are less than 2:
[-2,0,1]
[-2,0,3]
Example 2:

Input: nums = [], target = 0
Output: 0
Example 3:

Input: nums = [0], target = 0
"""
from astroid import List


class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:

        count = 0

        nums.sort()

        for i, val in enumerate(nums):

            L = i + 1
            R = len(nums) - 1

            while L < R:
                triplet = val + nums[L] + nums[R]

                if triplet < target:
                    count += R - L
                    L += 1

                else:
                    R -= 1
        return count
