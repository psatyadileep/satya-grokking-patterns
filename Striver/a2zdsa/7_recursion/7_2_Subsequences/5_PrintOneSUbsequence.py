
from typing import List


class Solution:
    def subsets(self, nums: List[int],target) -> List[List[int]]:
        response = []


        def helper(index,curr, curr_sum):
            if index>=len(nums):
                if curr_sum==target:
                    response.append(curr.copy())
                    return True

                else:
                    return False



            curr.append(nums[index])
            curr_sum+=nums[index]
            if helper(index+1,curr,curr_sum):
                return True

            curr.pop()
            curr_sum -=nums[index]
            if helper(index+1,curr,curr_sum):
                return True

            return False



        helper(0,[],0)
        return response

print(Solution().subsets([1,2,3],3))