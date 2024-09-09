"""
LC15:
Given an integer array nums, r
eturn all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.


"""
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        response = []
        nums.sort()
        for index , value in enumerate(nums):

            if index>0 and nums[index]==nums[index-1]:
                continue


            L = index + 1
            R = len(nums)-1

            while L<R:
                triplet_sum = value + nums[L] + nums[R]

                if triplet_sum>0:
                    R-=1

                elif triplet_sum<0:
                    L+=1

                else:
                    response.append(value,nums[L],nums[R])
                    L+=1
                    R-=1
                    while nums[L]==nums[L]-1 and L<R:
                        L+=1


        return  response


