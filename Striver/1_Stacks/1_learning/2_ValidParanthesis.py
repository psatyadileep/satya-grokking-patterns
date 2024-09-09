"""

20. Valid Parentheses
https://leetcode.com/problems/valid-parentheses/description/
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.


Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
"""

class Solution:
    def isValid(self, s: str) -> bool:

        if not s:
            return False

        hashmap = {"}": "{", ")": "(", "]": "["}

        stack = []
        for val in s:
            if val in hashmap:
                if stack and stack[-1] == hashmap[val]:
                    stack.pop()
                else:
                    return False

            else:
                stack.append(val)

        return not stack