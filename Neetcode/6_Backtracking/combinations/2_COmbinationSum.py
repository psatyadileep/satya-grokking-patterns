from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []




        def helper(index, curr, curr_sum):

            if curr_sum==target:
                res.append(curr.copy())
                return

            if index>= len(candidates):
                return




            if candidates[index]+curr_sum <=target:

                curr.append(candidates[index])
                helper(index,curr, curr_sum+candidates[index])

                curr.pop()
                helper(index+1, curr, curr_sum)



        helper(0,[],0)
        return res



candidates =  [2,3,6,7]
target = 7
print(Solution().combinationSum(candidates,target))
