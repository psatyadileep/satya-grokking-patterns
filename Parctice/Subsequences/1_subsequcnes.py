"""
https://leetcode.com/problems/subsets/submissions/
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



        def backtrack(index,subset):



            if  index>=len(nums):
                response.append(subset.copy())
                return

            subset.append(nums[index])
            backtrack(index+1,subset)

            subset.pop()
            backtrack(index+1,subset)


        backtrack(0,[])
        return response


class Solution2:
    def subsets2(self, nums: List[int]) -> List[List[int]]:
        response = []

        def backtrack(index, subset):
            if index >= len(nums):
                response.append(subset[:])

            for i in range(index, len(nums)):
                subset.append(nums[i])
                backtrack(i + 1, subset)
                subset.pop()
                backtrack(i + 1, subset)

        backtrack(0, [])
        return response
print(Solution().subsets([1,2,3,4]))
print(Solution2().subsets2([1,2,3,4]))