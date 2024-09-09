from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def helper(curr, lookup):
            if len(curr) == len(nums):  # Check if the current permutation is complete
                res.append(curr.copy())  # Append a copy of the current permutation
                return

            for i in range(len(nums)):

                if i>0 and nums[i]==nums[i-1]:
                    continue
                if lookup[i]:  # Skip if the number is already used in the current permutation
                    continue
                lookup[i] = True  # Mark the number as used
                curr.append(nums[i])
                helper(curr, lookup)
                curr.pop()  # Backtrack
                lookup[i] = False  # Unmark the number

        helper([], [False] * len(nums))  # Initialize the lookup list with False
        return res

# Testing the function
print(Solution().permute([2,1,1, 3]))
