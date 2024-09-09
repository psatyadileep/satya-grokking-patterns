class Solution:
    def totalNQueens(self, n: int) -> int:

        count = 0
        cols = set()
        posDiag = set()
        negDiag = set()

        def helper(r):
            nonlocal count
            if r == n:
                count += 1
                return


            for c in range(n):

                if c in cols or (r - c) in negDiag or (r + c) in posDiag:
                    continue

                cols.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)

                helper(r + 1)

                cols.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)

        helper(0)
        return count

print(Solution().totalNQueens(4))