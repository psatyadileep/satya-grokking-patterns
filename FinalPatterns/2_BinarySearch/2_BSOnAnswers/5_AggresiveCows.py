"""
Given an array of length ‘N’, where each element denotes the position of a stall. Now you have ‘N’ stalls and an integer ‘K’ which denotes the number of cows that are aggressive. To prevent the cows from hurting each other, you need to assign the cows to the stalls, such that the minimum distance between any two of them is as large as possible. Return the largest minimum distance.
Eg

array: 1,2,4,8,9  &  k=3
O/P: 3
Explaination: 1st cow at stall 1 , 2nd cow at stall 4 and 3rd cow at stall 8
"""

def AggresiveCows(arr):

    L = 0
    R = len(arr)-1

    def isPossible(mid):
        if

    while L<R:
        mid = (L+R)//2

        if isPossible(mid):
            R = mid

        else:
            L = mid+1


    return L