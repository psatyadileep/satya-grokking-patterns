class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        turtle = hare = nums[0]

        while True:
            turtle = nums[turtle]
            hare = nums[nums[hare]]

            if turtle == hare:
                break

        turtle = nums[0]

        while turtle != hare:
            turtle = nums[turtle]
            hare = nums[hare]

        return hare
