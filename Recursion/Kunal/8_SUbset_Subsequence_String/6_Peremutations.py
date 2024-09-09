
class Solution:
    def permute(self,arr):
        res = []

        def permute_helper(p, up):


            if not up:
                print(p)
                return

            ch = up[0]

            for i in range(len(p)+1):


                left = p[0:i]
                right = p[i:len(p)]
                permute_helper(left+ch+right,up[1:])

        permute_helper("",arr)



# Solution().permute("abc")




class Solution:
    def permute2(self,arr):
        res = []

        def permute_helper(p, up):

            if len(p)>=len(arr):
                res.append(p)
                return

            ch = up[0]

            for i in range(len(p)+1):


                left = p[0:i]
                right = p[i:len(p)]
                permute_helper(left+ch+right,up[1:])

        permute_helper("",arr)

        return res



print(Solution().permute2("abc"))
