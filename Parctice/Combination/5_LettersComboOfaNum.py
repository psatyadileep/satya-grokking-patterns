"""
https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
"""
from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        keypad = {
            '2': 'abc', '3': 'def',
            '4': 'ghi', '5': 'jkl', '6': 'mno',
            '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }

        response = []

        def dfs(index, path):
            if len(path) == len(digits):
                response.append(''.join(path))
                return

            for i in range(index, len(digits)):
                for letter in keypad[digits[i]]:
                    path.append(letter)
                    dfs(i + 1, path)
                    path.pop()

        dfs(0, [])
        return response

# Example usage:
result = Solution().letterCombinations("23")
print(result)
