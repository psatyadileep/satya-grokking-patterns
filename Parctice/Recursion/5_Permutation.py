"""
Create all possible permuations
"""

def permutestr(nums):


    res = []
    def helper(permute,hash):

        if len(permute)>=len(nums):
            res.append(permute.copy())
            return

        for ind, val in enumerate(nums):

            if not hash.get(val,False):

                hash[val]  = True
                permute.append(val)
                helper(permute,hash)
                permute.pop()
                hash[val]= False


    helper([],{})

    return  res

print(permutestr([1,2,3,4]))