"""
https://leetcode.com/problems/combination-sum/

39. Combination Sum
Solved
Medium
Topics
Companies
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the
frequency
 of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.


"""
from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []


        def combination_helper(ind,target, current_list = []):

            if ind == len(candidates):
                if target==0:
                    res.append(current_list.copy())
                return


            if candidates[ind]<=target:
                current_list.append(candidates[ind])
                combination_helper(ind,target-candidates[ind], current_list)
                current_list.pop()

            combination_helper(ind+1,target, current_list)

        combination_helper(0,target, [])
        return  res

print(Solution().combinationSum([2, 3, 6, 7], target=7))


#approach 2



class Solution2:
    def subsets2(self, nums: List[int], target: int) -> List[List[int]]:
        response = []

        def backtrack(index, subset, current_sum):
            if current_sum == 0:
                response.append(subset.copy())
                return

            if current_sum<0:
                return
 
            for i in range(index, len(nums)):
                subset.append(nums[i])
                backtrack(i, subset,current_sum- nums[i])
                subset.pop()

        backtrack(0, [],target)
        return response

result = Solution2().subsets2([2, 3, 6, 7], target=7)
print(result)
