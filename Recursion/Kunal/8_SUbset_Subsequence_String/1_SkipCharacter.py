"""
Given a  string , remove all the a from it
"""




def SkipChar(arr):

    def helper(ind,res):

        if ind>=len(arr):
            return res

        if arr[ind]!="a" and arr[ind]!="A":
            res.append(arr[ind])


        return helper(ind+1,res)

    ans = helper(0,[])

    return "".join(ans)

print(SkipChar("baaccad"))
     
