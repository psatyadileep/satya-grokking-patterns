"""
LC27:Contains Duplicate
https://leetcode.com/problems/contains-duplicate/description/
Given an integer array nums, return true if any value appears at least twice in the array
and return false if every element is distinct.



Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

Assumptions:
-> can the array be empty : yes
->  are the numbers sorted : No


Brain Storm:
->We can use the set technique
    Timne Complexity = o(n) + O(n)
    Space = o(n)
->We use hashmap
    Time Complexity =  O(n)
    Soace Complexity = O(n)
-> we can use loops
    time Complexity = O(n)^2


Approach

# """

# SOlution1 : Brute Force
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        if not nums:
            return False

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True

        return False


# SOlution2 : Using Haspmap


class Solution2:
    def containsDuplicate2(self, nums: List[int]) -> bool:

        if not nums:
            return False

        lookup = {}

        for val in nums:
            if val not in lookup:
                lookup[val] = 1
            else:
                return True
        return False


print(Solution().containsDuplicate([1, 2, 3, 1]) == True)
print(Solution().containsDuplicate([1, 2, 3, 4]) == False)
print(Solution().containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) == True)

print(Solution2().containsDuplicate2([1, 2, 3, 1]) == True)
print(Solution2().containsDuplicate2([1, 2, 3, 4]) == False)
print(Solution2().containsDuplicate2([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) == True)