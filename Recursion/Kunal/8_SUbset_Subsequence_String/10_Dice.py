class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        global count
        count = 0

        def helper(p, up, dice):
            global count  # Declare count as global to modify the global variable count

            if up == 0:
                if dice == 0:
                    count += 1
                    return

            for i in range(1, k + 1):
                if up - i >= 0:
                    helper(p + str(i), up - i, dice - 1)

        helper("", target, n)
        return count

print(Solution().numRollsToTarget(1,6,3))