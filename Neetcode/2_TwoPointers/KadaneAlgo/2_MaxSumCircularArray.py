"""

https://leetcode.com/problems/maximum-sum-circular-subarray/description/
Maximum Sum Circular Subarray -


Approach :

1 . Max Subarray + min Subbaray = Total Sum
 2. Max Subarray = Total Sum - MinSubarray

there are two possibilities:
1. Max sum being inbetween
2. MAx subarray being being Circular

1 . Max Subarray being inbetween -> use Kadanes Algo
2 For Max Circular Subarray
    -> total Sum - Min Subarray
    -> Use Kadanes ALgo For min SUbarray

    Find Max_Sum , MinSum , CircualrSUm

"""


from typing import List

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # Calculate the total sum of the array
        total_sum = sum(nums)

        # Kadane's algorithm to find the max and min subarray sum
        def kadanes(flag):
            # Initialize current and ma ximum sums
            curr_sum = nums[0]
            max_sum = nums[0]

            # Traverse the list from the second element to the end
            for i in range(1, len(nums)):
                if flag:
                    # For maximum subarray sum
                    curr_sum = max(curr_sum + nums[i], nums[i])
                    max_sum = max(max_sum, curr_sum)
                else:
                    # For minimum subarray sum
                    curr_sum = min(curr_sum + nums[i], nums[i])
                    max_sum = min(max_sum, curr_sum)

            return max_sum

        # Get the maximum subarray sum using Kadane's algorithm
        max_sum = kadanes(True)
        # Get the minimum subarray sum using the modified Kadane's algorithm
        min_sum = kadanes(False)

        # Calculate the maximum circular subarray sum
        circular_sum = total_sum - min_sum

        # Return the maximum of the non-circular and circular sums
        # If all elements are negative, max_sum will be the least negative number, and we should return it
        if max_sum > 0:
            return max(max_sum, circular_sum)
        else:
            return max_sum
