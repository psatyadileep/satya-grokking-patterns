"""
LC16
https://leetcode.com/problems/3sum-closest/description/


Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).


Input: [1, 0, 1, 1], target=100
Output: 3
Explanation: The triplet [1, 1, 1] has the closest sum to the target.


Assumptioons
-> are the numbers sorte d: no
-> can there be duplicate s: yes

Barin Storm :
-. using three loops
-> using two pointer stechnique

Approach :
-> inrate with a single and apply two poiter technique along with it
"""

from typing import List
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()


        answer = float("inf")
        if not nums:
            return -1


        for index, value in enumerate(nums):

             L = index+1
             R = len(nums)-1

             while L<R:
                triplet_sum =  value + nums[L] + nums[R]

                if abs(triplet_sum-target) < abs(answer-target):
                    answer = triplet_sum


                if triplet_sum>target:
                    R-=1

                elif triplet_sum<target:
                    L+=1

                else:
                    return target

        return answer








print(Solution().threeSumClosest([-1,2,1,-4], 1))

print(Solution().threeSumClosest([1, 0, 1, 1],100))