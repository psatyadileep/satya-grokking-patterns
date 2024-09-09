"""
https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/description/
LC1498

You are given an array of integers nums and an integer target.

Return the number of non-empty subsequences of nums such that the sum of the minimum and maximum element on it is less or equal to target. Since the answer may be too large, return it modulo 109 + 7.



Example 1:

Input: nums = [3,5,6,7], target = 9
Output: 4
Explanation: There are 4 subsequences that satisfy the condition.
[3] -> Min value + max value <= target (3 + 3 <= 9)
[3,5] -> (3 + 5 <= 9)
[3,5,6] -> (3 + 6 <= 9)
[3,6] -> (3 + 6 <= 9)
Example 2:

Input: nums = [3,3,6,8], target = 10
Output: 6
Explanation: There are 6 subsequences that satisfy the condition. (nums can have repeated numbers).
[3] , [3] , [3,3], [3,6] , [3,6] , [3,3,6]


Explore:
1 Can the array be empty : yes
2. can ther ebe duplicates : yes
3. is the array sorted : no


Brain Storm :
1. Brtue FOrce approach : using two loops

2. Using Soring and two poiters

"""


class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:

        count = 0
        curr_sum = 0
        L = 0

        if not nums:
            return count

        for index,val in enumerate(nums):
            curr_sum+=val

            if curr_sum<=target:
                count+=1

            else:
                curr_sum-=nums[L]
                L+=1

        return count
