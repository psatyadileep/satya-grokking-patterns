  # # from typing import List
# #
# #
# # class Solution:
# #     def letterCombinations(self, digits: str) -> List[str]:
# #         if not digits:
# #             return []
# #
# #         digit_to_char = {
# #             '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
# #             '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
# #         }
# #
# #         res = []
# #
# #         def helper(index, curr):
# #             if index == len(digits):
# #                 res.append("".join(curr))
# #                 return
# #
# #             current_digit = digits[index]
# #             for char in digit_to_char[current_digit]:
# #                 curr.append(char)
# #                 helper(index + 1, curr)
# #                 curr.pop()  # backtrack
# #
# #         helper(0, [])
# #         return res
# #
# #
# # # Testing the function
# # print(Solution().letterCombinations("23"))
#
#
# print(True or True)
# print(False or True)
# print(True or False)t
from typing import List


# tes = "Doleep"
#
# print(tes[:len(tes)]-1)


from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        digit_to_char = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }

        res = []

        def helper(index, curr):
            if index == len(digits):
                res.append("".join(curr))
                return

            current_digit = digits[index]
            for char in digit_to_char[current_digit]:
                curr.append(char)
                helper(index + 1, curr)
                curr.pop()  # backtrack

        helper(0, [])
        return res
print(Solution().letterCombinations("23"))