class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            return
        rows, cols = len(matrix), len(matrix[0])
        self.prefix = [[0]* (cols+1) for r in range(rows+1)]
        for r in range(1, rows+1):
            for c in range(1, cols+1):
                cur = (matrix[r-1][c-1] + self.prefix[r-1][c] + self.prefix[r][c-1] - self.prefix[r-1][c-1])
                self.prefix[r][c] = cur

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1, row2, col2 = row1+1, col1+1, row2+1, col2+1
        cursum = self.prefix[row2][col2] - self.prefix[row1-1][col2] - self.prefix[row2][col1-1] + self.prefix[row1-1][col1-1]
        return cursum



# class NumMatrix:

#     def __init__(self, matrix: List[List[int]]):
#         rows, cols = len(matrix), len(matrix[0])
#         self.prefix = [[0] * (cols + 1) for _ in range(rows + 1)]
#         for r in range(1, rows + 1):
#             for c in range(1, cols + 1):
#                 self.prefix[r][c] = matrix[r - 1][c - 1] + self.prefix[r - 1][c] + self.prefix[r][c - 1] - self.prefix[r - 1][c - 1]

#     def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
#         row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
#         cursum = self.prefix[row2][col2] - self.prefix[row1 - 1][col2] - self.prefix[row2][col1 - 1] + self.prefix[row1 - 1][col1 - 1]
#         return cursum


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)