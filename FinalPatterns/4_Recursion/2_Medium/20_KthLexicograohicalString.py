"""

"""



class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        res = []
        lookup = ["a", "b", "c"]
        count = 0  # To track how many valid happy strings have been generated

        def helper(curr):
            nonlocal count
            if len(curr) == n:
                print(curr)
                return

            for i in range(len(lookup)):
                if not curr or curr[-1] != lookup[i]:  # Ensure no consecutive same characters
                    curr.append(lookup[i])
                    helper(curr)
                    curr.pop()  # Backtrack

        helper([])

        # If there are fewer than k valid happy strings, return an empty string
        return res[0] if len(res) > 0 else ""


# Test the function
print(Solution().getHappyString(3, 9))  # Example test case
