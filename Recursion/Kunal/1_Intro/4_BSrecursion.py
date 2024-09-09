"""
Give a sorted array find the the target element in the array using recursibe Binary searc
"""



def BS(arr,target):

    def helper(l,r):

        mid = (l+r)//2
        if l>r:
            return -1

        if arr[mid] == target:
            return mid


        elif arr[mid]>target:
            return helper(l,mid-1)

        return helper(mid+1,r)


    return helper(0,len(arr)-1)




print(BS([1,2,3,4,55,66,78],4))



print(BS([1,2,3,4,55,66,78],9))