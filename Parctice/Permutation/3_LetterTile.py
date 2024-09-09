class Solution:
    def numTilePossibilities(self, tiles: str) -> int:



        count = 0
        res= []
        tiles =sorted(tiles)
        def helper(subset,hash):
            nonlocal count
            if subset:
                res.append("".join(subset))
                count+=1
            #
            # if (index>=len(tiles)):
            #     return
            for i in range(0,len(tiles)):
                if i>0 and tiles[i]==tiles[i-1] and i-1 not in hash:
                    continue

                if i not in hash:
                    hash.add(i)
                    subset.append(tiles[i])
                    helper(subset,hash)
                    subset.pop()
                    hash.remove(i)

        helper([],set())
        return res
print(Solution().numTilePossibilities("CDC"))


