"""
https://leetcode.com/problems/subsets-ii/description/
Given an integer array nums that may contain duplicates, return all possible
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.



Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
"""
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:


        res = []



        def dfs(index,subset):

            if index>=len(nums):
                res.append(subset.copy())



            subset.append(nums[index])
            dfs(index+1,subset)
            subset.pop()
            while index+1 <len(nums) and nums[index] == nums[index+1]:
                index+=1

            dfs(index+1)

        dfs(0,[])

        return res
