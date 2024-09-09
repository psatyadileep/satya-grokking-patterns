def bs(arr, target ):

    l = 0
    r = len(arr)-1



    def condition(mid):

        return arr[mid]>=target

    while l<r:

        mid = (l+r)//2


        print(f"Before : l {l} , r {r} , mid:{mid}")

        if condition(mid):
            r = mid

        else:
            l = mid+1

    return l



print(bs([2,3,6,8,10,12,15,18],12))