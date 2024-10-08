"""


"""
from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        res = []

        curr = []

        def helper(ind, curr, c_sum):

            if len(curr) == k and c_sum == n:
                res.append(curr)
                print(curr)
                return

            if ind > 9:
                return

            for i in range(ind, 9):
                curr.append(i)
                helper(i + 1, curr, c_sum + i)
                curr.pop()

        helper(1, [], 0)


print(Solution().combinationSum3(3,9))