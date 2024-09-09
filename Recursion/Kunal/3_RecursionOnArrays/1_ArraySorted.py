"""
Check if an array is sorted
"""



def MainSorted(arr):


    def helper(l):

        if l>=len(arr)-1:
            return True


        if arr[l]<arr[l+1]:
            return helper(l+1)
        else:
            return False


    return helper(0)

print(MainSorted([1,4,8,9,10,12,0]))


print(MainSorted([1,4,8,9,10,12]))



def MainSorted(arr):


    def helper(l):

        if l>=len(arr)-1:
            return True


        return arr[l]<arr[l+1] and  helper(l+1)

    return helper(0)