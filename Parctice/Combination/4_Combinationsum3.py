"""
https://leetcode.com/problems/combination-sum-iii/description/
216. Combination Sum III
Solved
Medium
Topics
Companies
Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

Only numbers 1 through 9 are used.
Each number is used at most once.
Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.


"""
from typing import List


class Solution:

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:


        res = []



        def dfs(index,csum,clist):

            if len(clist)==k and csum==0:
                res.append(clist.copy())

            if index>9:
                return

            for i in range(index,10):

                clist.append(i)
                dfs(i+1,csum-i,clist)
                clist.pop()

        dfs(1,n,[])
        return res

print(Solution().combinationSum3(3,7))