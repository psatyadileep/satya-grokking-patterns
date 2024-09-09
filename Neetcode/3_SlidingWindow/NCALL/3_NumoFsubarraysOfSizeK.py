
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        L = 0


        if not arr or len(arr)<k:
            return 0

        currr_sum = 0
        for R, val  in  enumerate(arr):

            currr_sum+= val
            count = 0

            if R-L+1 == k:

                if currr_sum//k>= threshold:
                    count+=1


                currr_sum-= arr[L]
                L+=1


        return count







