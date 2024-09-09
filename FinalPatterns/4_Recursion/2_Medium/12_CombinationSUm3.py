from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        res = []

        def helper(ind, curr_sum, curr_set):
            if curr_sum == n:
                res.append(curr_set.copy())

            if curr_sum > n:
                return
            for i in range(ind, 10):
                curr_sum += i
                curr_set.append(i)
                helper(i + 1, curr_sum,curr_set)

                curr_sum -= i
                curr_set.pop()

        helper(0, 0, [])
        return res


print(Solution().combinationSum3(3,7))