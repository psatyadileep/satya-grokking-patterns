# # # from typing import List
# # #
# # #
# # # class Solution:
# # #     def letterCombinations(self, digits: str) -> List[str]:
# # #         if not digits:
# # #             return []
# # #
# # #         digit_to_char = {
# # #             '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
# # #             '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
# # #         }
# # #
# # #         res = []
# # #
# # #         def helper(index, curr):
# # #             if index == len(digits):
# # #                 res.append("".join(curr))
# # #                 return
# # #
# # #             current_digit = digits[index]
# # #             for char in digit_to_char[current_digit]:
# # #                 curr.append(char)
# # #                 helper(index + 1, curr)
# # #                 curr.pop()  # backtrack
# # #
# # #         helper(0, [])
# # #         return res
# # #
# # #
# # # # Testing the function
# # # print(Solution().letterCombinations("23"))
# #
# #
# # print(True or True)
# # print(False or True)
# # print(True or False)t
# from typing import List
#
#
# # tes = "Doleep"
# #
# # print(tes[:len(tes)]-1)
#
#
# from typing import List
#
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
# # print(Solution().letterCombinations("23"))
# #
# #
# # test = "dileep"
# # start = 0
# # end = len(test)-1
# #
# #
# # print(test[start:end+1])
# # print("********")
# # print(test[end::-1])
#
#
#
# visited = set()
#
# path = [(1,2,3),(4,5,6)]
# path2 = [(4,5,6),(1,2,3)]
#
# visited.add(tuple(path))
#
#
# print(visited)
#
# if tuple(path2) in visited):
#     print(1)
# else:
#     print(0)



"""
# Definition for Employee.

"""
import collections
from collections import defaultdict
from typing import List
# class Employee:
#     def __init__(self, id: int, importance: int, subordinates: List[int]):
#         self.id = id
#         self.importance = importance
#         self.subordinates = subordinates

# class Solution:
#     def getImportance(self, employees: List['Employee'], id: int) -> int:
#
#         # visited = set()
        # adjlist = defaultdict(list)
        #
        # for eid, importance , subordinates in employees:
        #
        #     adjlist[eid].append(importance)
        #     if subordinates:
        #         adjlist[eid].append(subordinates)
        #     else:
        #         adjlist[eid].append([])
        #
        #     # print(adjlist)
        #
        #
        # q = collections.deque()
        #
        # importance = 0
        # q.append(id)
        # print(id)
        #
        # while q:
        #     employee = q.popleft()
        #     employee_importance , subordinates = adjlist[employee]
        #
        #     # print(employee_importance, subordinates)
        #
        #
        #     importance+=employee_importance
        #
        #     for subordinate in subordinates:
        #         q.append(subordinate)
        #         visited.add(subordinate)
        #
        # return importance
#
# print(Solution().getImportance([[1,5,[2,3]],[2,3,[]],[3,3,[]]],1))
#
#

path = [1,2,3,4]
path + [7]
print(path)
# path.append(9)
# print(path)




































# print(ans)