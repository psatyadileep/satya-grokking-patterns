from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def swap(a, b):
            a , b = b , a

        return
        def helper(index, curr):


            if index == len(nums)-1:
                res.append(curr.copy())


            for i in range(index,len(nums)):

                swap(nums[i], nums[index])
                helper(index+1,curr)
                swap(nums[index], nums[i])

        helper(0,nums)

        return res



print(Solution().permute([1,2,3]))