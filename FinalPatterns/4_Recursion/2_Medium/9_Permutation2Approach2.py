from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Sort to handle duplicates
        res = []

        def swap(a, b):
            nums[a], nums[b] = nums[b], nums[a]

        def helper(index):
            if index == len(nums):
                res.append(nums.copy())
                return

            seen = set()  # Set to avoid duplicate elements at each recursive level
            for i in range(index, len(nums)):

                print(seen)
                if nums[i] in seen:
                    continue  # Skip duplicate elements

                seen.add(nums[i])  # Mark the element as used at this level
                swap(i, index)
                helper(index + 1)
                swap(i, index)  # Backtrack

        helper(0)
        return res


print(Solution().permuteUnique([1, 1, 2]))



from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Sort to handle duplicates
        res = []

        def swap(a, b):
            nums[a], nums[b] = nums[b], nums[a]

        def helper(index):
            if index == len(nums):
                res.append(nums.copy())
                return

            for i in range(index, len(nums)):
                # Skip duplicates (important to skip only the ones that haven't been placed in this position yet)
                if i > index and nums[i] == nums[i-1]:
                    continue

                swap(i, index)
                helper(index + 1)
                swap(i, index)  # Backtrack

        helper(0)
        return res


print(Solution().permuteUnique([1, 1, 2]))
