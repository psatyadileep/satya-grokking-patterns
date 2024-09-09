def mergesort(arr):
    # Define the merge function
    def merge(left, right):
        result = []
        i = 0
        j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    # Base case: if the array has 1 or 0 elements, return it as it's already sorted
    if len(arr) <= 1:
        return arr

    # Find the middle point and divide the array into two halves
    mid = len(arr) // 2
    left = mergesort(arr[0:mid])
    right = mergesort(arr[mid:])

    # Merge the two sorted halves
    return merge(left, right)               