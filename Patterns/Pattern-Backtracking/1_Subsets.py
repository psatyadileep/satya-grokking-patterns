from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        response = []



        def helper(idx, curr):

            if idx>=len(nums):

                response.append(curr.copy())
                return

            curr.append(nums[idx])
            helper(idx+1,curr)

            curr.pop()
            helper(idx+1,curr)


        helper(0,[])
        return response


print(Solution().subsets([1,2,3]))


