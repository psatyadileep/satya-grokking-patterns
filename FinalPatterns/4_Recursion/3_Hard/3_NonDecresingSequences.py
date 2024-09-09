"""
https://leetcode.com/problems/non-decreasing-subsequences/
"""
from typing import List

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []

        def helper(ind, curr):
            if len(curr) >= 2:
                res.append(curr[:])

            seen = set()
            for i in range(ind, len(nums)):
                if nums[i] in seen:
                    continue
                seen.add(nums[i])
                print(seen)
                if not curr or nums[i] >= curr[-1]:
                    curr.append(nums[i])
                    helper(i + 1, curr)
                    curr.pop()

        helper(0, [])
        return res

# Test the function
print(Solution().findSubsequences([4, 6, 7, 7]))
print(Solution().findSubsequences([4, 4, 3, 2, 1]))
