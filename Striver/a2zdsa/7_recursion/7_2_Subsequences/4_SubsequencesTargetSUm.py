"""
78. Subsets

Companies
Given an integer array nums of unique elements, return all possible
subsets of a give target
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.



Example 1:

Input: nums = [1,2,3]
target  = 3
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
"""
from typing import List


class Solution:
    def subsets(self, nums: List[int],target) -> List[List[int]]:
        response = []


        def helper(index,curr, curr_sum):
            if index>=len(nums):
                if curr_sum==target:
                    response.append(curr.copy())
                return



            curr.append(nums[index])
            curr_sum+=nums[index]
            helper(index+1,curr,curr_sum)

            curr.pop()
            curr_sum -=nums[index]
            helper(index+1,curr,curr_sum)


        helper(0,[],0)
        return response

print(Solution().subsets([1,2,3],3))