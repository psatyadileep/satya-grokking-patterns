from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        curr = []
        res = []

        def isPalindrome(start: int, end: int) -> bool:
            while start < end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True

        def helper(ind: int):

            if curr:
                res.append(curr[:])  # pend a copy of curr

            for i in range(ind, len(s)):
                print(s[ind:i+1])
                if isPalindrome(ind, i):
                    curr.append(s[ind:i + 1])  # Add the current palindrome substring
                    helper(i + 1)  # Move to the next index
                    curr.pop()  # Backtrack

        helper(0)
        return res


print(Solution().partition("AAB"))
