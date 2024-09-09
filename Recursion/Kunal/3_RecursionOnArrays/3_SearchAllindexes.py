"""
Given a na rray return all the indexes of the target
"""



def LinearSearch(arr,target):

    def helper(i,res):

        if i>=len(arr):
            return res

        if arr[i]== target:
            res.append(i)

        return helper(i+1,res)


    return helper(0,[])

print(LinearSearch([1,2,128,3,4,5,6,128],128))
