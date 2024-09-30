def permuteUnique(arr):
    res = []
    arr.sort()  # Sorting the array to handle duplicates

    def helper(lookup, curr):
        if len(curr) == len(arr):
            res.append(curr.copy())
            return

        for i in range(len(arr)):
            # Skip the element if it's already used in the current permutation
            if lookup[i]:
                continue

            # Skip duplicates: if the current element is the same as the previous one
            # and the previous one was not used in the current recursion level, skip it
            if i > 0 and arr[i] == arr[i - 1] and not lookup[i - 1]:
                continue

            lookup[i] = True
            curr.append(arr[i])
            helper(lookup, curr)
            curr.pop()
            lookup[i] = False

    helper([False] * len(arr), [])
    return res

# Test the function with duplicates
print(permuteUnique([1, 1, 2]))
