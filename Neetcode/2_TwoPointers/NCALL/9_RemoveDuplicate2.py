from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        L = 0

        for R in range(len(nums)):
            if L < 2 or nums[R] != nums[L - 2]:
                nums[L] = nums[R]
                L += 1

            print(L,R                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               )
        return L


print(Solution().removeDuplicates([0,0,1,1,1,1,2,3,3]))