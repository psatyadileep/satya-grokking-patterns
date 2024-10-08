from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits or digits == '':
            return []

        lookup = {
            "0": "",
            "1": "",
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        res = []

        def helper(ind, curr):

            if ind > len(digits):
                return

            if len(curr) == len(digits):
                res.append("".join(curr))
                print(res)
                return

            for i in range(ind, len(digits)):

                print(i)

                for val in lookup[digits[i]]:
                    curr.append(val)
                    helper(i + 1, curr)
                    curr.pop()

        helper(0, [])
        return res

print(Solution().letterCombinations("23"))