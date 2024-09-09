"""
https://leetcode.com/problems/subsets/description/
78. Subsets

Companies
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


        def helper(index,curr):
            if index>=len(nums):
                response.append(curr.copy())
                return



            curr.append(nums[index])
            helper(index+1,curr)

            curr.pop()
            helper(index+1,curr)


        helper(0,[])
        return response

print(Solution().subsets([1,2,3]))