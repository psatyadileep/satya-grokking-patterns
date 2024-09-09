"""
https://leetcode.com/problems/subsets/
LC78: Subsets

Given an integer array nums of unique elements, return all possible
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.



Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]

"""
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        response = []
        subset = []



        def helper(ind):

            if ind>=len(nums):
                response.append(subset[::])
                return


            subset.append(nums[ind])
            helper(ind+1)

            subset.pop()
            helper(ind+1)

        helper(0)


        return response


print(Solution().subsets([1,2,3,4]))