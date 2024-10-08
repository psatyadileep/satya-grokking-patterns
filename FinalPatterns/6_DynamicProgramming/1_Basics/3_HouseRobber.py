"""
https://leetcode.com/problems/house-robber/description/
198. House Robber
Solved
Medium
Topics
Companies
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of eac
money you can rob tonight without alerting the police.
"""


#approach 1 - recurison

class Solution:
    def rob(self, nums: List[int]) -> int:

        def helper(index):

            if index>=len(nums):
                return 0

            rob = nums[index] + help(index+1)

            skip = helper(index+1)


            return max(rob,skip)


        return helper(0)



# apporach 2: Memomization


class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}

        def helper(index):

            if index in cache:
                return cache[index]

            if index >= len(nums):
                return 0

            rob = nums[index] + helper(index + 2)

            skip = helper(index + 1)

            cache[index] = max(rob, skip)

            return cache[index]

        return helper(0)


#appaorach 3
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        # Create a DP array to store the max sum at each house
        dp = [0] * n

        # Base cases
        dp[0] = nums[0]  # Rob the first house
        dp[1] = max(nums[0], nums[1])  # Either rob the first or second house, whichever is more profitable

        # Fill the dp array
        for i in range(2, n):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])

        # The last element in dp contains the answer
        return dp[n-1]
