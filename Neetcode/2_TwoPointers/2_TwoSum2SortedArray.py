"""
LC167 : Two SUm 2
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
 Two Sum II - Input Array Is Sorted


Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 < numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.



Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].


Assumptions:
-> We can always assume there is one solution for sure

Barin Storm
Approach 1: Using Loops:
    -> Using Two loops
    Space Complexity = O(n)^2 , Time Compleixty = O(1)

Approach 2: Using Two Pointers
    .Use left and Right Pointers
    . If the sum is greater move the right Pointers
    . If the sum is leeser than target move the left pointer
    . else return -1 , -1

    Time Complexity = o(n) , Space Complexity = o(1)


"""


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        L = 0
        R = len(numbers) - 1

        while L < R:
            two_Sum = numbers[L] + numbers[R]

            if two_Sum > target:
                R -= 1

            elif two_Sum < target:
                L += 1

            else:
                return [L, R]
