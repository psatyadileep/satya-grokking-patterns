"""
Give a list of intergeRS , PRINT ALL THE SIBSETS in it . Shoul dbe in creasesing order
"""



class Solution:


    def Subsetsum(self, candidates):
        res = []
        def dfs(index,csum):

            if index>=len(candidates):
                res.append(csum)
                return

            dfs(index+1,csum+candidates[index])
            dfs(index+1,csum)


        dfs(0,0)
        return res

print(Solution().Subsetsum([2,3]))