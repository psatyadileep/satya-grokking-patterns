class Solution():
    def matrix(self, n):
        count = 0
        path = []
        def find_path(r, c, curr_path):
            if r == n-1 and c == n-1:
                path.append(curr_path)
                return

            if r >= n or c >= n:
                return

            find_path(r+1, c, curr_path+"D")
            find_path(r, c+1, curr_path+"R")

        find_path(0, 0, "")

        return  path

paths = Solution().matrix(3)

