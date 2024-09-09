class Solution():
    def matrix(self, n):
        count = 0
        path = []

        def count_helper(r, c):
            nonlocal count
            if r == n-1 and c == n-1:
                count += 1
                return

            if r >= n or c >= n:
                return

            count_helper(r+1, c)
            count_helper(r, c+1)

        def find_path(r, c, curr_path):
            if r == n-1 and c == n-1:
                path.append(curr_path)
                return

            if r >= n or c >= n:
                return

            find_path(r+1, c, curr_path+"D")
            find_path(r, c+1, curr_path+"R")

        find_path(0, 0, "")
        count_helper(0, 0)

        return count, path

count, paths = Solution().matrix(3)
print("Number of paths:", count)
print("Paths:", paths)
