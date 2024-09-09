from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Ensure the list is sorted to handle duplicates properly
        res = []

        def swap(a, b):
            nums[a], nums[b] = nums[b], nums[a]

        def helper(index):


            if index == len(nums) - 1:
                res.append(nums.copy())
                return
            # lookup = set()


            for i in range(index, len(nums)):
                swap(i,index)
                helper(index + 1)
                swap(index, i)

        helper(0)

        return res


print(Solution().permuteUnique([1,1,2]))

print(Solution().permuteUnique([1,2,3]))

