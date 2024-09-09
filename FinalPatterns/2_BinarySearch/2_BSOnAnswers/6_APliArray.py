from typing import List


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        def canSplit(max_sum: int) -> bool:
            current_sum = 0
            required_subarrays = 1

            for num in nums:
                if current_sum + num > max_sum:
                    required_subarrays += 1
                    current_sum = num
                    if required_subarrays > k:
                        return False
                else:
                    current_sum += num

            return True

        L, R = max(nums), sum(nums)

        while L < R:
            mid = (L + R) // 2
            if canSplit(mid):
                R = mid
            else:
                L = mid + 1

        return L