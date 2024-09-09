"""
https://leetcode.com/problems/permutations/description/
46. Permutations
Solved
Medium
Topics
Companies
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.



Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
"""
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []



        def dfs(currlist,hash):

            if len(currlist)>=len(nums):
                res.append(currlist.copy())


            for i in range(0,len(nums)):

                if not hash.get(i,False):
                    hash[i] = True
                    currlist.append(nums[i])
                    dfs(currlist,hash)
                    currlist.pop()
                    hash[i]= False
        dfs([],{})
        return res

print(Solution().permute([1,2,3]))