# def numTilePossibilities(tiles: str) -> int:
#     res = []
#
#     def helper(lookup, curr):
#         # Add current permutation to result if it's not empty
#         if curr:
#             res.append("".join(curr))
#
#         # Generate permutations
#         for i in range(len(tiles)):
#             if lookup[i]:
#                 continue
#
#
#             if i>0 and tiles[i]==tiles[i-1]:
#                 continue
#
#             lookup[i] = True
#             curr.append(tiles[i])
#             print(i,lookup,curr)
#             helper(lookup, curr)
#             curr.pop()
#             lookup[i] = False
#
#     helper([False] * len(tiles), [])
#     return len(res)
#
#
# # print(numTilePossibilities("AAB"))  # Example usage
# def numTilePossibilities(tiles: str) -> int:
#     res = set()
#
#     def helper(start: int):
#         if start == len(tiles):
#             return
#
#         for i in range(start, len(tiles)):
#             # Swap the current index with the start index
#             tiles[start], tiles[i] = tiles[i], tiles[start]
#
#             # Add the current permutation to the result set
#             res.add("".join(tiles[:start + 1]))
#
#             # Recurse with the next index
#             helper(start + 1)
#
#             # Backtrack by swapping the characters back
#             tiles[start], tiles[i] = tiles[i], tiles[start]
#
#     # Convert string to list for easier swapping
#     tiles = list(tiles)
#     helper(0)
#     return len(res)
#
#
# print(numTilePossibilities("AAB"))  # Example usage



def numTilePossibilities(tiles: str):
    res = []

    def helper(ind):
        def swap(a,b):
            tiles[a], tiles[b] = tiles[b], tiles[a]


        for i in range(ind, len(tiles)):
            # Swap the current index with the start index

            if i>ind and tiles[i]==tiles[i-1]:
                continue
            swap(i,ind)
            res.append("".join(tiles[::ind + 1]))

            # Recurse with the next index
            helper(ind + 1)

            swap(ind,i)

    # Convert string to list for easier swapping
    tiles = list(tiles)
    helper(0)
    return res


print(numTilePossibilities("AAB"))



class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        self.res = 0

        def helper(lookup):
            # Count the current combination if it's not empty
            # We increment before exploring further to count all non-empty combinations
            self.res += 1

            for i in range(len(tiles)):
                if lookup[i]:
                    continue  # Skip already used tiles

                # Avoid duplicates: if the current tile is the same as the previous one and the previous one wasn't used, skip this one
                if i > 0 and tiles[i] == tiles[i - 1] and not lookup[i - 1]:
                    continue

                # Mark this tile as used
                lookup[i] = True
                helper(lookup)  # Recurse with the next index
                lookup[i] = False  # Backtrack

        # Sort the tiles to ensure duplicates are adjacent
        tiles = sorted(tiles)
        helper([False] * len(tiles))  # Track used tiles
        return self.res - 1  # Subtract one to exclude the empty combination

# Example usage
print(Solution().numTilePossibilities("AAB"))  # Should return 8