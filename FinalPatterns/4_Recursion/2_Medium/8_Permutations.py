def permutate(arr):

    res = []


    def helper(lookup,curr):

        if len(curr)==len(arr):
            res.append(curr.copy())
            return



        for i in range(len(arr)):

            if lookup[i]:
                continue


            lookup[i] = True
            curr.append(arr[i])
            helper(lookup,curr)
            curr.pop()
            lookup[i]= False


    helper([False] * len(arr),[])

    return res

print(permutate([1,2,3]))

