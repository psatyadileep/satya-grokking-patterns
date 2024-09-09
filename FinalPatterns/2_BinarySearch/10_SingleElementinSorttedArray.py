class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        L = 0
        R = len(nums) - 1

        def condition(mid):
            # Ensure mid is even for pair checking
            if mid % 2 == 1:
                mid -= 1
            # Check if the pair starts at mid
            return nums[mid] != nums[mid + 1]

        while L < R:
            mid = (L + R) // 2
            if condition(mid):
                R = mid  # Move to the left half
            else:
                L = mid + 1  # Move to the right half

        return nums[L]


# Example usage
sol = Solution()
print(sol.singleNonDuplicate([1, 1, 2, 3, 3, 4, 4, 8, 8]))  # Output should be 2
print(sol.singleNonDuplicate([3, 3, 7, 7, 10, 11, 11]))  # Output should be 10


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        L = 0
        R = len(nums) - 1

        def condition(mid):
            # Ensure mid is even for pair checking
            if mid % 2 == 1:
                mid -= 1
            # Check if the pair starts at mid
            return nums[mid] != nums[mid + 1]

        while L < R:
            mid = (L + R) // 2
            if condition(mid):
                R = mid  # Move to the left half
            else:
                L = mid + 1  # Move to the right half

        return nums[L]


# Example usage
sol = Solution()
print(sol.singleNonDuplicate([1, 1, 2, 3, 3, 4, 4, 8, 8]))  # Output should be 2
print(sol.singleNonDuplicate([3, 3, 7, 7, 10, 11, 11]))  # Output should be 10
