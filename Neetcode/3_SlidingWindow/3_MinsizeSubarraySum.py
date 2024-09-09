"""
LC209 Minimum Size Subarray Sum

https://leetcode.com/problems/minimum-size-subarray-sum/description/
Given an array of positive integers nums and a positive integer target, return the minimal length of a
subarray
 whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.



Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0

Explore:
-> can the array be empty : Yes

Brain Storm :
1. Using Two Loops
    Time Compleixty = O(N)^2

[2,3,1,2,4,3]

2. Using Two Pointer
    .Use two pointers L = 0 , return
    .Pointer R runs thriugh the array
    . The sum is calculate as we iterate
    . if the sum if greater than equal to 7:
    .we store the min length
    . we move the left pointer until the length is less than 7
    , return the min length recorded


"""
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L = 0
        min_length = float("inf")
        sub_array_sum = 0

        for R in range(len(nums)):

            sub_array_sum += nums[R]

            while sub_array_sum >= target:
                min_length = min(min_length, R - L + 1)
                sub_array_sum -= nums[L]
                L += 1

        return 0 if min_length == float("inf") else min_length
