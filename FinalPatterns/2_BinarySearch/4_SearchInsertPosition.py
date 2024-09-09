class Solution:
    def searchInsert(self, nums, target):
        L = 0
        R = len(nums)

        def isCondition(index):
            return nums[index] >= target

        while L < R:
            mid = L + (R - L) // 2
            if isCondition(mid):
                R = mid
            else:
                L = mid + 1

        return L


