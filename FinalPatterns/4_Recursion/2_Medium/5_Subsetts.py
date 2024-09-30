from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        response = []



        def helper(ind, curr):

            response.append(curr.copy())
            print(curr)

            for i in range(ind, len(nums)):

                curr.append(nums[i])
                helper(i+1,curr)
                curr.pop()



        helper(0,[])

        return response


print(Solution().subsets([1,2,3]))

#
#
# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         response = []
#
#         def subsets_helper(ind,current_set):
#             if ind >= len(nums):
#                 response.append(current_set.copy())
#                 return
#
#             current_set.append(nums[ind])
#             subsets_helper(ind + 1,current_set)
#
#             current_set.pop()
#             subsets_helper(ind + 1,current_set)
#
#         subsets_helper(0,[])
#         return response