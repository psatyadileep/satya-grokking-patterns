from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        L = 0

        for R in range(len(nums)):

            if nums[L] != 0:
                L += 1

            if nums[R] != 0 and R > L:
                nums[R], nums[L] = nums[L], nums[R]


            print(L, R)


        return nums



print(Solution().moveZeroes([0,1,0,3,12]))