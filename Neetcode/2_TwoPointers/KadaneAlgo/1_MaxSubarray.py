# import sys
"""
https://leetcode.com/problems/maximum-subarray/
"""


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        curr_sum = 0
        max_sum = nums[0]
        # prin(max_sum)

        for R in range(len(nums)):

            if curr_sum < 0:
                curr_sum = 0

            curr_sum += nums[R]

            max_sum = max(curr_sum, max_sum)

        return max_sum
