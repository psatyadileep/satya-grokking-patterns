from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []



        def dfs(currlist,hash):

            if len(currlist)>=len(nums):
                res.append(currlist.copy())


            for i in reversed(range(0,len(nums))):

                if not hash.get(i,False):
                    hash[i] = True
                    currlist.append(nums[i])
                    dfs(currlist,hash)
                    currlist.pop()
                    hash[i]= False
        dfs([],{})
        return res

print(Solution().permute([1,2,3]))
print(Solution().permute(["A","B","C"]))