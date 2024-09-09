class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        elements = ["a", "b", "c"]
        res = []

        def helper(ind, curr):
            if len(curr) == n:
                res.append("".join(curr))
                return

            for i in range(len(elements)):
                if curr and curr[-1] == elements[i]:
                    continue

                curr.append(elements[i])
                helper(ind + 1, curr)
                if len(res) == k:  # Stop early if we've found the k-th string
                    return
                curr.pop()

        helper(0, [])

        if len(res) < k:
            return ""
        return res[k - 1]


print(Solution().getHappyString(3, 9))
