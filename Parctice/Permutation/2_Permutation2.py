"""
https://leetcode.com/problems/permutations-ii/description/
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.



Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

"""

from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res =[]
        def dfs(currlist, hash):

            if len(currlist) >= len(nums):
                res.append(currlist.copy())
                return

            for i in range(0, len(nums)):

                if i>0 and nums[i]==nums[i-1] and i-1 not in hash:
                    continue

                if i not in hash:
                    hash.add(i)
                    currlist.append(nums[i])
                    dfs(currlist, hash)
                    currlist.pop()
                    hash.remove(i)

        dfs([],set())
        return res

print(Solution().permuteUnique([1,1,2]))