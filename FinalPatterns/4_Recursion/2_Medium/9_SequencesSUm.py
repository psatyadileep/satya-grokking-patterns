# User function Template for python3
class Solution:
    def perfectSum(self, arr, n, sum):

        count = 0

        def helper(ind, curr_sum):
            nonlocal count

            if curr_sum == sum:
                count += 1
                return

            if curr_sum > sum:
                return

            for i in range(ind, len(arr)):
                curr_sum += arr[i]
                helper(i + 1, curr_sum)
                curr_sum -= arr[i]

        helper(0, 0)

        return count

print(Solution().perfectSum([5, 2, 3, 10, 6, 8],6,10))