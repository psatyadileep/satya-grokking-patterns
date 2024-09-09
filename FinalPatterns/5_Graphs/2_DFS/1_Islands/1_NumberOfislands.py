from typing import List

#
# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         rows = len(grid)
#         cols = len(grid[0])
#         visited = set()
#
#         self.count = 0
#
#         def Move(r, c):
#             # Check if the cell is within bounds, is not visited, and is land ('1')
#             if 0 <= r < rows and 0 <= c < cols and (r, c) not in visited and grid[r][c] == '1':
#                 return True
#             else:
#                 return False
#
#         def dfs(r, c):
#             # Perform DFS and mark all connected '1's as visited
#             if not Move(r, c):
#                 return
#
#             visited.add((r, c))
#
#             directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
#
#             for dr, dc in directions:
#                 new_row, new_col = r + dr, c + dc
#                 dfs(new_row, new_col)
#
#         for r in range(rows):
#             for c in range(cols):
#                 # Start a DFS if you find an unvisited '1'
#                 if grid[r][c] == '1' and (r, c) not in visited:
#                     self.count += 1
#                     dfs(r, c)
#
#         return self.count
#
#
# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         rows = len(grid)
#         cols = len(grid[0])
#         visited = set()
#
#         self.count = 0
#
#         def Move(r, c):
#             # Check if the cell is within bounds, is not visited, and is land ('1')
#             if 0 <= r < rows and 0 <= c < cols and (r, c) not in visited and grid[r][c] == '1':
#                 return True
#             else:
#                 return False
#
#         def dfs(r, c):
#             # Perform DFS and mark all connected '1's as visited
#             if not Move(r, c):
#                 return
#
#             visited.add((r, c))
#
#             directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
#
#             for dr, dc in directions:
#                 new_row, new_col = r + dr, c + dc
#                 dfs(new_row, new_col)
#
#         for r in range(rows):
#             for c in range(cols):
#                 # Start a DFS if you find an unvisited '1'
#                 if grid[r][c] == '1' and (r, c) not in visited:
#                     self.count += 1
#                     dfs(r, c)
#
#         return self.count

# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         rows = len(grid)
#         cols = len(grid[0])
#         visited = set()
#         self.count = 0

# def Move(r, c):
#     # Check if the cell is within bounds, is not visited, and is land ('1')
#     if 0 <= r < rows and 0 <= c < cols and (r, c) not in visited and grid[r][c] == '1':
#         return True
#     else:
#         return False

#         def dfs(r, c):
#             # Perform DFS and mark all connected '1's as visited
#             if not Move(r, c):
#                 return

#             visited.add((r, c))

#             directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

#             for dr, dc in directions:
#                 new_row, new_col = r + dr, c + dc
#                 dfs(new_row, new_col)

#         for r in range(rows):
#             for c in range(cols):
#                 # Start a DFS if you find an unvisited '1'
#                 if grid[r][c] == '1' and (r, c) not in visited:
#                     self.count += 1
#                     dfs(r, c)

#         return self.count

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Step 1: Initialize variables
        rows = len(grid)
        cols = len(grid[0])
        island_count = 0

        # Step 2: Define a function to check valid moves
        def Move(r, c):
            return 0 <= r < rows and 0 <= c < cols and grid[r][c] == '1'

        # Step 3: Define the DFS function
        def dfs(r, c):
            # Mark the cell as visited by changing '1' to '0'
            grid[r][c] = '0'

            # Explore all 4 possible directions
            directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            for dr, dc in directions:
                new_r, new_c = r + dr, c + dc
                if Move(new_r, new_c):
                    dfs(new_r, new_c)

        # Step 4: Traverse the entire grid
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    # Start a new DFS for each unvisited '1'
                    island_count += 1
                    dfs(r, c)

        # Step 5: Return the total number of islands found
        return island_count



grid = [ ["1", "0", "0", "0", "1"],
         ["0", "1", "0", "1", "0"],
         ["0", "0", "1", "0", "0"],
         ["0", "1", "0", "1"," 0"] ]


print(Solution().numIslands(grid))