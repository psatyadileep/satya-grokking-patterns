def mergesort(arr):
        def merge(left, right):
                res = []

                L = 0
                R = 0

                while L < len(left) and R < len(right):

                        if left[L] < right[R]:
                                res.append(left[L])
                                L += 1

                        else:
                                res.append(right[R])

                                R+=1


                while L< len(left):
                        res.append(left[L])
                        L+=1
                while R < len(right):
                        res.append(right[R])
                        R+=1

                return res


        if len(arr)<=1:
                return

        mid = len(arr)//2
        left = mergesort(arr[:mid])

        right = mergesort((arr[mid::]))


        return merge(left,right)

