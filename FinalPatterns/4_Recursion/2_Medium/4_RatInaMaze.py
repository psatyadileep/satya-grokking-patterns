class Solution:
    def findPath(self, mat):
        res = []
        def helper(r, c, path):
            if r == len(mat) - 1 and c == len(mat[0]) - 1:
                res.append(path)
                return


            directions = [(0,1,"R"), (0,-1,"L"), (1,0,"D"), (-1,0,"U")]

            for dr, dc, di in directions:
                nr, nc = r+dr, c+dc
                if 0<=nr<len(mat) and 0<=nc<len(mat[0]) and mat[nr][nc] == 1:
                    mat[nr][nc] = 0  # mark as visited
                    helper(nr, nc, path + di)  # append current direction to path
                    mat[nr][nc] = 1  # unmark after visiting

        if mat[0][0] == 1:  # if source cell is not blocked, start the search
            helper(0, 0, "")
        return res

print(Solution().findPath([[1,0,0,0],[1,1,0,1],[1,1,0,0],[0,1,1,1]]))