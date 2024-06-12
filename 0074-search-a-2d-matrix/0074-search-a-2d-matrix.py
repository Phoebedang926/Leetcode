class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        top , bot = 0 , rows-1
        while top <= bot:
            midrow = (top +bot)//2
            if target > matrix[midrow][-1]:
                top = midrow+1
            elif target < matrix[midrow][0]:
                bot = midrow-1
            else:
                break
        


        left, right = 0, cols-1
        while left <=right:
            mid = (left+right)//2
            if target > matrix[midrow][mid]:
                left = mid+1
            elif target < matrix[midrow][mid]:
                right = mid-1
            else:
                return True
        return False
        