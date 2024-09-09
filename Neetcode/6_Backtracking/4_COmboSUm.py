from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []



        def helper(index,subset, sum ):


            if sum ==0:
                res.append(subset[::])

            if len(subset)>=len(candidates):
                return


            if sum>=1:
                subset.append(candidates[index])
                helper(index,subset,target-candidates[index])
                subset.pop()
            helper(index+1, subset, target - candidates[index])

        return res


