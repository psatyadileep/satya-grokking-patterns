"""
LC977
https://leetcode.com/problems/squares-of-a-sorted-array/description/

Given an integer array nums sorted in non-decreasing order,
return an array of the squares of each number sorted in non-decreasing order.
Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]


Assumptiions
-> is the array sorted -> No
-> can there be deuplicates : yes

Brainstorm :
-> Brute force apply loops
-> sort the numbers , apply using two pointers


Implement
-> sort the array
[-3, 0, 1, 2, -1, 1, -2]
-3 , -2 , -1, 0, 1, 1, 2

-> combination of single loop iteration + 2 sum
 -> make sure we dont select duplicated in the dge cases

Time Complexity = Nlogn + O ( N) ^2 = o(n)^2
"""


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:



        response = []
        if not nums:
            return []

        nums.sort()

        for index,val in enumerate(nums):

            if index>0 and nums[index]==nums[index-1]:
                continue


            L = index+1
            R = len(nums)-1

            while L<R:

                triplesum= nums[index] + nums[L] + nums[R]

                if triplesum>0:
                    R-=1

                elif triplesum<0:
                    L+=1

                else:
                    response.append([val,nums[L], nums[R]])

                    L+=1

                    while nums[L] == nums[L-1] and L<R:
                        L+=1


        return response



