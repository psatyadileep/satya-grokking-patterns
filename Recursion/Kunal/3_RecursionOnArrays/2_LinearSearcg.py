"""
Given a array - Find the the index fof the target element using recurison
"""


def LinearSearch(arr,target):

    def helper(i):

        if i>=len(arr):
            return -1

        if arr[i]== target:
            return i

        return helper(i+1)


    return helper(0)

print(LinearSearch([1,2,3,4,5,6,128],128))
