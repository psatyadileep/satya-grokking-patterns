"""
https://leetcode.com/problems/letter-tile-possibilities/description/
LC1079
You have n  tiles, where each tile has one letter tiles[i] printed on it.

Return the number of possible non-empty sequences of letters you can make using the letters printed on those tiles.
"""

# class Solution:
#     def numTilePossibilities(self, tiles: str):
#         # print(tiles)
#         tiles =  list(tiles)
#         tiles.sort()
#         count = 0
#         res = []
#
#
#
#         def swap(a, b):
#             tiles[a] , tiles[b] = tiles[b], tiles[a]
#         def helper(idx, curr):
#             nonlocal  count
#
#
#             if curr:
#                 print(curr)
#                 res.append("".join(curr))
#                 count+=1
#
#
#
#             for i in range(idx,len(tiles)):
#
#                 if i!=idx and tiles[i] == tiles[i-1]:
#                     continue
#                 #
#                 curr.append(tiles[i])
#                 swap(i,idx)
#                 helper(idx+1,curr)
#                 swap(idx,i)
#
#
#
#         helper(0,[])
#
#
#         return count
#


#
# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         res = []
#
#         def swap(a, b):
#             a , b = b , a
#
#         def helper(index, curr):
#
#
#             if index == len(nums)-1:
#                 res.append(curr.copy())
#                 return
#
#
#             for i in range(index,len(nums)):
#
#                 swap(nums[i], nums[index])
#                 helper(index+1,curr)
#                 swap(nums[index], nums[i])
#
#         helper(0,nums)
#
#         return res

class Solution:
    def numTilePossibilities(self, tiles: str):
        tiles = list(tiles)
        tiles.sort()
        count = 0
        res = []

        def swap(a, b):
            tiles[a], tiles[b] = tiles[b], tiles[a]

        def helper(idx):
            nonlocal count

            if idx > 0:
                sequence = ''.join(tiles[:idx])
                res.append(sequence)
                count += 1

            for i in range(idx, len(tiles)):
                if i != idx and tiles[i] == tiles[idx]:
                    continue
                swap(i, idx)
                helper(idx + 1)
                swap(i, idx)

        helper(0)
        return count, res

# Test the function
solution = Solution()
count, possibilities = solution.numTilePossibilities("AAB")
print(f"Count: {count}")
print(f"Possibilities: {possibilities}")



print(Solution().numTilePossibilities("AAB"))



