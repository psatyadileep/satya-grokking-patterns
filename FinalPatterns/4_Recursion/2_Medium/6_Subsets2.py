from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        response = []



        def helper(curr,lookup):

            if len(curr)>1:
                response.append(curr.copy())

            for i in range(len(nums)):


                if lookup[i]:
                    continue

                if i!=ind and nums[i]==nums[i-1]:
                    continue


                lookup[i] = True
                curr.append(nums[i])
                helper(curr,lookup)
                lookup[i]= False
                curr.pop()



        helper(0,[],[False]*len(nums))

        return response


print(Solution().subsets([1,2,3]))