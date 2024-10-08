from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        response = []
        res = []

        def helper(index,curr_sum,curr):


            if curr_sum == target:
                res.append(curr.copy())
                return

            if curr_sum>target:
                return

            for i in range(index,len(candidates)):

                curr.append(candidates[i])
                helper(i,curr_sum+candidates[i],curr)
                curr.pop()

        helper(0,0, [])

        return res


print(Solution().combinationSum([2,3,6,7],6))
