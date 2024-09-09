def MergeSortInPlace(arr):

    def helper(start, end):
        if end - start > 1:
            mid = (start + end) // 2
            helper(start, mid)
            helper(mid, end)
            mergeInPlace(start, mid, end)

    def mergeInPlace(start, mid, end):
        left = arr[start:mid]
        right = arr[mid:end]

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[start + k] = left[i]
                i += 1
            else:
                arr[start + k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[start + k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[start + k] = right[j]
            j += 1
            k += 1

    helper(0, len(arr))

    return arr

print(MergeSortInPlace([5, 4, 3, 2, 1]))
