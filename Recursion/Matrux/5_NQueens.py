class Solution:
    def Nqueens(self, n):
        col = set()
        posiDiag = set()  # r + c
        negDiag = set()  # r - c
        count = 0
        res = []

        board = [["."]*n for i in range(n)]

        def helpercount(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return 1  # We've placed all queens successfully

            local_res = 0
            for c in range(n):
                if c in col or (r + c) in posiDiag or (r - c) in negDiag:
                    continue  # Skip if placing queen here violates rules

                # Place the queen
                col.add(c)
                posiDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "q"

                # Recurse to the next row
                local_res += helpercount(r + 1)

                # Remove the queen
                col.remove(c)
                posiDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."

            return local_res

        count = helpercount(0)
        return count, res

# Testing the function with 3 queens
print(Solution().Nqueens(4))  # Should return 0 since 3 queens on 3x3 is not possible
print(Solution().Nqueens(8))