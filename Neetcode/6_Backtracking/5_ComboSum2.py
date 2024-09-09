"""
https://leetcode.com/problems/combination-sum-ii/description/
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output:
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
"""
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        response = []

        candidates.sort()
        def helper(index, combo , sum):


            if sum==0:
                response.append(combo[::])
                return

            if index>=len(candidates) or candidates[index]>sum:
                return

            if sum>0:
                combo.append(candidates[index])
                helper(index+1,combo, target-candidates[index])
                combo.pop()

            while index+1 <len(candidates) and candidates[index] == candidates[index+1]:
                index+=1
            helper(index+1,combo, target)

        helper(0,[],target)
        return response


print(Solution().combinationSum2([10,1,2,7,6,1,5], target = 8))
