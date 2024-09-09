"""
Write a program to recurively merge sort an array
"""
def MergeSort(arr):

    def helper(arr):
    def merge(left, right):
        i = 0
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = helper(arr[:mid])
        right = helper(arr[mid:])

        return merge(left, right)



        j = 0
        res = []

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1

        # Add remaining elements from left and right subarrays
        while i < len(left):
            res.append(left[i])
            i += 1

        while j < len(right):
            res.append(right[j])
            j += 1

        return res

    return helper(arr)

print(MergeSort([5, 4, 3, 2, 1]))

