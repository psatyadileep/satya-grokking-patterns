"""
1011. Capacity To Ship Packages Within D Days

Example 1:

Input: weights = [1,2,3,4,5,6,7,8,9,10], days = 5
Output: 15
Explanation: A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
1st day: 1, 2, 3, 4, 5
2nd day: 6, 7
3rd day: 8
4th day: 9
5th day: 10

Note that the cargo must be shipped in the order given, so using a ship of capacity 14 and splitting the packages into parts like (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) is not allowed.
Example 2:

"""

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def isCondition(max_weight):

            count = 1
            total_weight =  0
            for weight in weights:

                if total_weight+ weight <= max_weight:
                    total_weight+=weight
                else:
                    total_weight = weight
                    count+=1



            return count<=days


        L = max(weights)
        R = sum(weights)

        ans = -1
        while L<R:
            mid = (L+R)//2
            if isCondition(mid):
                R = mid

            else:
                L = mid+1


        return L
