class Solution:
    def findMin(self, nums: List[int]) -> int:
        def isCondition(mid):

            if nums[mid] <= nums[R]:
                return True
            else:
                return False

        L = 0
        R = len(nums) - 1

        if nums[L] < nums[R]:
            return nums[0]


        else:

            while L < R:
`
                mid = (L + R) // 2

                if isCondition(mid):
                    R = mid

                else:
                    L = mid + 1

            return nums[L]

