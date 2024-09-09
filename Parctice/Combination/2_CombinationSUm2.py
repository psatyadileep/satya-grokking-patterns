"""
https://leetcode.com/problems/combination-sum-ii/description/
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.
xample 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output:
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]

"""
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        response = []



        def dfs(index,currlist,currsum):

            if currsum == 0:
                response.append(currlist.copy())

            if index>=len(candidates):
                return


            for i in range(index,len(candidates)):

                if i>index and candidates[i] == candidates[i]-1:
                    continue

                if candidates[i]>target:
                    break

                currlist.append(candidates[i])
                dfs(index+1,currlist,currsum-candidates[i])
                currlist.pop()


        dfs(0,[],target)
        return response


print(Solution().combinationSum2([2,3,6,7], target = 7))
