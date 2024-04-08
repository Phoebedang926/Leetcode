class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prevrow = [1] * n

        for r in range(m-2, -1, -1):
            currow = [1] * n
            for c in range(n - 2, -1, -1):
                currow[c] = currow[c+1] + prevrow[c]
            prevrow = currow

        return prevrow[0]
    
# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         # Initialize the grid with all elements as 1
#         grid = [[1] * n for _ in range(m)]

#         # Start from the second-to-last row and iterate upwards
#         for r in range(m - 2, -1, -1):
#             # Start from the second-to-last column and iterate backwards
#             for c in range(n - 2, -1, -1):
#                 # The number of unique paths to reach the bottom-right corner
#                 # from the current cell is the sum of the paths from the cell to
#                 # the right and the cell below it in the grid
#                 grid[r][c] = grid[r+1][c] + grid[r][c+1]

#         # The top-left corner of the grid now contains the total number of unique paths
#         return grid[0][0]

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Initialize the grid with all elements as 1
        grid = [[1] * n for i in range(m)]

        # Start from the second-to-last row and iterate upwards
        for r in range(1, m):
            # Start from the second-to-last column and iterate backwards
            for c in range(1, n):
                # The number of unique paths to reach the bottom-right corner
                # from the current cell is the sum of the paths from the cell to
                # the right and the cell below it in the grid
                grid[r][c] = grid[r-1][c] + grid[r][c-1]

        # The top-left corner of the grid now contains the total number of unique paths
        return grid[m-1][n-1]