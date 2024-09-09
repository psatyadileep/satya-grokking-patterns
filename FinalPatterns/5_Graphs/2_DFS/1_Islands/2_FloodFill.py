class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        rows = len(image)
        cols = len(image[0])
        visited = set()
        source_value = image[sr][sc]

        def move(r, c):
            return 0 <= r < rows and 0 <= c < cols and (r, c) not in visited and image[r][c] == source_value

        def dfs(r, c):

            if not move(r, c):
                return

            visited.add((r, c))
            image[r][c] = color

            neighbors = [(1, 0), (0, 1), (-1, 0), (0, -1)]

            for dr, dc in neighbors:
                new_row, new_col = r + dr, c + dc
                dfs(new_row, new_col)

        dfs(sr, sc)

        return image




