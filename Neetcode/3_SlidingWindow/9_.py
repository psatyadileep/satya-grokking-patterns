"""
LC
239. Sliding Window Maximum

You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.



Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation:
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6


 1  3  -1  -3  5 [3  6  7]      7
Example 2:


L
[1,3,-1,-3,5,3,6,7], k = 3 max value = 3
     R

  L
[1,3,-1,-3,5,3,6,7], k = 3 max value = 3
        R


"""


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        L = 0
        high_num = float("-inf")
        result = []

        if not nums:
            return []
        for R, value in enumerate(nums):

            if R - L + 1 > k:
                result.append(high_num)
                L += 1

            if nums[R] > high_num:
                high_num = value

        return result




